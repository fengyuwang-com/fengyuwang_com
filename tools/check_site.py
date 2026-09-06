#!/usr/bin/env python3
"""全站综合检测脚本 (v2, 2026-09-06)

覆盖审计 docs/AUDIT-全站内容完整审计-2026-09-05.md 中所有可机械判定的 bug 类型:
  1. 内容规范: 痕迹词 / 新文直角引号「」 / 描述过短 / 汉字过少
  2. 三语对齐: translationKey 三语成组 / frontmatter 必填字段
  3. 简繁质量: zh-hk 正文简体泄漏 (opencc 可转而未转的字符) / zh-cn 繁体泄漏
  4. 结构: 代码围栏闭合 (```html 必须有收尾 ```) / Hugo 原始 HTML 是否会被丢弃
  5. 部署一致性: hugo/content 与根目录 /{lang}/blog 副本篇数是否一致 (P0 漂移检测)
  6. sitemap: URL 数 vs 实际页面数
  7. 站点配置: _headers 是否覆盖 /{lang}/blog* / llms.txt 链接是否存在 /
     CF beacon 占位符 / 死链检查 (根目录 HTML 相对引用)
用法: python3 tools/check_site.py   (在仓库根目录执行)
"""
import glob
import os
import re
import sys
import urllib.parse

os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ROOT = os.getcwd()
LANGS = ["zh-cn", "zh-hk", "en"]
TRACES = ["元宝", "它说", "我问它", "这场对话", "跟AI聊", "跟 AI 聊"]
NEW_CUTOFF = "2026-08-15"  # v6.3 规范生效后的新文 (直角引号禁令)

try:
    from opencc import OpenCC
    cc = OpenCC("s2hk")
    cc_t = OpenCC("hk2s")
except ImportError:
    cc = cc_t = None

issues = []
notes = []


def err(cat, msg):
    issues.append(f"[{cat}] {msg}")


def ok(cat, msg):
    notes.append(f"[{cat}] {msg}")


# ---------- 收集博文 ----------
posts = {}  # (lang) -> list of (path, fm, body, date)
for lang in LANGS:
    posts[lang] = []
    for f in sorted(glob.glob(f"hugo/content/{lang}/blog/posts/*/index.md")):
        t = open(f, encoding="utf-8").read()
        m = re.match(r"^---\n(.*?)\n---\n", t, re.S)
        if not m:
            err("frontmatter", f"{f}: 缺 frontmatter")
            continue
        fm, body = m.group(1), t[m.end():]
        dm = re.search(r"^date:\s*(\d{4}-\d{2}-\d{2})", fm, re.M)
        posts[lang].append({
            "path": f, "fm": fm, "body": body, "date": dm.group(1) if dm else "",
            "dir": os.path.basename(os.path.dirname(f)),
        })

# ---------- 1. 内容规范 ----------
for lang in LANGS:
    for p in posts[lang]:
        full = p["fm"] + p["body"]
        for t in TRACES:
            if t in full:
                err("trace", f"{p['path']}: 痕迹词「{t}」")
        if p["date"] >= NEW_CUTOFF and "「" in p["body"]:
            err("quote", f"{p['path']}: 新文含直角引号「")
        dm = re.search(r'description:\s*"?([^"\n]*)"?', p["fm"])
        if not dm or len(dm.group(1).strip()) < 10:
            err("desc", f"{p['path']}: description 缺失或过短 ({dm.group(1) if dm else ''!r})")
        if lang in ("zh-cn", "zh-hk"):
            han = len(re.findall(r"[\u4e00-\u9fff]", p["body"]))
            if han < 200:
                err("short", f"{p['path']}: 汉字仅 {han}")

# ---------- 2. 三语对齐 ----------
groups = {}
for lang in LANGS:
    for p in posts[lang]:
        tk = re.search(r'translationKey:\s*"?([^"\n]+)"?', p["fm"])
        key = tk.group(1).strip() if tk else p["dir"]
        groups.setdefault(key, {})[lang] = p["path"]
bad = {k: v for k, v in groups.items() if len(v) < 3}
if bad:
    for k, v in sorted(bad.items()):
        err("translate", f"translationKey「{k}」三语不齐: {sorted(v)}")
else:
    ok("translate", f"translationKey 三语成组: {len(groups)} 组全部对齐")

# ---------- 3. 简繁质量 ----------
if cc:
    for p in posts["zh-hk"]:
        resid = {}
        for ch in set(p["body"]):
            if "\u4e00" <= ch <= "\u9fff" and cc_t.convert(ch) != ch and cc.convert(ch) != ch:
                resid[ch] = p["body"].count(ch)
        # 只报 opencc s2hk 能转的简体字 (上下文相关字如 里/干/佣/游 不算)
        simp = {ch: n for ch, n in resid.items() if cc.convert(ch) != ch}
        if sum(simp.values()) > 3:
            err("zh-hk-simp", f"{p['path']}: 简体泄漏 {sum(simp.values())} 处: {simp}")
    from opencc import OpenCC as _O
    cc_t2s = _O("t2s")
    for p in posts["zh-cn"]:
        trad = [ch for ch in set(p["body"]) if "\u4e00" <= ch <= "\u9fff" and cc_t2s.convert(ch) != ch]
        if trad:
            err("zh-cn-trad", f"{p['path']}: 繁体泄漏 {trad[:10]}")

# ---------- 4. 围栏 / 原始 HTML ----------
for lang in LANGS:
    for p in posts[lang]:
        opens = len(re.findall(r"^```", p["body"], re.M))
        if opens % 2:
            err("fence", f"{p['path']}: 代码围栏不闭合 ({opens} 个 ```)")
        if re.search(r"^<!DOCTYPE|^\s*<html", p["body"], re.M | re.I) and not re.search(r"```\s*html", p["body"]):
            err("rawhtml", f"{p['path']}: 裸 HTML 无围栏, Hugo 会静默丢弃")

# ---------- 5. 部署一致性 (P0 漂移) ----------
import unicodedata

for lang in LANGS:
    def url_seg(p):
        fm = p["fm"]
        s = re.search(r'^slug:\s*"?([^"\n]+)"?', fm, re.M)
        return unicodedata.normalize("NFC", (s.group(1).strip() if s else p["dir"])).replace(" ", "-")
    src = {url_seg(p) for p in posts[lang] if 'draft: true' not in p['fm']}
    dep = {unicodedata.normalize("NFC", os.path.basename(d)) for d in glob.glob(f"{lang}/blog/posts/*") if os.path.isdir(d)}
    miss = src - dep
    extra = dep - src
    if miss:
        err("deploy", f"{lang}: {len(miss)} 篇源文件未部署: {sorted(miss)[:5]}… (需 hugo + deploy.sh)")
    if extra:
        err("deploy", f"{lang}: {len(extra)} 篇部署副本无源文件: {sorted(extra)[:5]}")
    # RSS 一致
    rss = f"{lang}/blog/index.xml"
    if os.path.exists(rss):
        n = open(rss, encoding="utf-8").read().count("<item>")
        if n != len(src):
            err("deploy", f"{lang}: 根目录 RSS {n} 条 vs 源 {len(src)} 篇")
    else:
        err("deploy", f"{lang}: 根目录 RSS 缺失")
ok("deploy", f"部署副本: " + ", ".join(f"{l} {len(glob.glob(l+'/blog/posts/*'))} 篇" for l in LANGS))

# ---------- 6. sitemap ----------
if os.path.exists("sitemap.xml"):
    sm = open("sitemap.xml", encoding="utf-8").read()
    locs = sm.count("<loc>")
    pages = len(glob.glob("_site/**/*.html", recursive=True))
    if pages == 0:
        notes.append("[sitemap] _site 不存在 (构建后已清理), 跳过数量比对; 当前 loc={}".format(locs))
    elif abs(locs - pages) > 5:
        err("sitemap", f"sitemap {locs} loc vs 构建 {pages} 页, 需重生成")
    else:
        ok("sitemap", f"sitemap {locs} loc ≈ 构建 {pages} 页")
    if "https://fengyuwang.com/en/blog/" not in sm:
        err("sitemap", "sitemap 缺博客索引 URL")
else:
    err("sitemap", "根目录 sitemap.xml 缺失")

# ---------- 7. 站点配置 ----------
h = open("_headers", encoding="utf-8").read() if os.path.exists("_headers") else ""
for l in LANGS:
    if f"/{l}/blog*" not in h:
        err("headers", f"_headers 缺 /{l}/blog* 缓存规则")
if h and "/blog*" in h and "/zh-cn/blog*" in h:
    ok("headers", "_headers 已覆盖三语 blog 路径")

if os.path.exists("llms.txt"):
    lt = open("llms.txt", encoding="utf-8").read()
    for m in re.findall(r"\((/[^\s)]+)\)", lt):
        path = urllib.parse.unquote(m.split("#")[0])
        if path.endswith("/"):
            path += "index.html"
        if not path.lstrip("/").startswith("_"):
            path = path.lstrip("/")
        if not os.path.exists(path):
            err("llms", f"llms.txt 引用不存在: {m}")
    ok("llms", "llms.txt 链接检查完成")

b = open("hugo/layouts/_default/baseof.html", encoding="utf-8").read()
if "YOUR_CLOUDFLARE_TOKEN" in b:
    notes.append("[config] CF Web Analytics 仍是占位符 token (需站长填真实 token)")

# ---------- 8. 死链 (根目录 HTML 相对/绝对引用) ----------
def check_ref(page, ref):
    if ref.startswith(("http://", "https://", "mailto:", "tel:", "data:", "#", "//")):
        return True
    ref = urllib.parse.unquote(ref.split("#")[0].split("?")[0])
    if not ref:
        return True
    base = os.path.dirname(page)
    target = os.path.normpath(os.path.join(base, ref)) if not ref.startswith("/") else ref.lstrip("/")
    if os.path.isdir(target):
        target = os.path.join(target, "index.html")
    if not target.endswith(".xml") and not os.path.splitext(target)[1]:
        target = os.path.join(target, "index.html")
    return os.path.exists(target)

refs = broken = 0
for page in glob.glob("*.html") + [p for l in LANGS for p in glob.glob(f"{l}/**/*.html", recursive=True)]:
    html = open(page, encoding="utf-8", errors="ignore").read()
    for m in re.findall(r'(?:href|src)="([^"]+)"', html):
        if "{" in m or "{{" in m or "\\" in m:
            continue
        refs += 1
        if not check_ref(page, m):
            broken += 1
            err("link", f"{page} -> {m}")
ok("link", f"死链检查: {refs} 个引用, {broken} 断链")

# ---------- 汇总 ----------
print("=" * 60)
for n in notes:
    print("  PASS", n)
print("=" * 60)
if issues:
    print(f"发现 {len(issues)} 个问题:")
    for i in issues:
        print("  !!", i)
    sys.exit(1)
print("全部检查通过 ✔")
