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
用法: python3 tools/check_site.py [--no-dark]          全站发版大检查 (默认含对比度审计)
      python3 tools/check_site.py --article <md>...   单篇发布前校验
在仓库根目录执行
"""
import argparse
import functools
import glob
import http.server
import importlib.util
import json
import os
import re
import socketserver
import sys
import threading
import urllib.parse

_ap = argparse.ArgumentParser(description="全站综合检测大脚本 (每次发版必跑)")
_ap.add_argument("--no-dark", action="store_true", help="跳过暗色/亮色对比度浏览器审计 (最耗时)")
_ap.add_argument("--article", nargs="+", metavar="MD", help="单篇发布前校验模式: 痕迹词+汉字数+直角引号")
_ap.add_argument("--max-dark-pages", type=int, default=0, help="调试: 限制对比度审计页数")
ARGS = _ap.parse_args()

os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ROOT = os.getcwd()
LANGS = ["zh-cn", "zh-hk", "en"]
TRACES = ["元宝", "它说", "我问它", "这场对话", "跟AI聊", "跟 AI 聊"]
NEW_CUTOFF = "2026-08-15"  # v6.3 规范生效后的新文 (直角引号禁令)


# ---------- 模式 0: 单篇发布前校验 (--article) ----------
if ARGS.article:
    for path in ARGS.article:
        text = open(path, encoding="utf-8").read()
        body = re.sub(r"^---.*?---", "", text, flags=re.S)
        hits = [t for t in TRACES if t in text]
        han = len(re.findall(r"[\u4e00-\u9fff]", body))
        nq = text.count("「")
        status = "OK " if not hits else "!!!"
        print(f"{status} {path}  汉字={han}  痕迹词={hits if hits else '无'}  直角引号={nq} 处 (旧文豁免, 新文必须为 0)")
        for t in hits:
            i = text.find(t)
            print(f"    -> …{text[max(0, i - 30):i + 30]}…")
    sys.exit(0)

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
    # hreflang alternate 是 Hugo 自动生成的跨语言提示, 三语 slug 不对齐是设计使然, 不算死链
    html = re.sub(r'<link rel="alternate" hreflang="[^"]*"[^>]*>', "", html)
    # <script> 里的字符串拼接 (如 '+p.url+') 不是真实链接, 扫描前整体剥离
    html = re.sub(r"<script\b[^>]*>.*?</script>", "", html, flags=re.S)
    for m in re.findall(r'(?:href|src)="([^"]+)"', html):
        if "{" in m or "{{" in m or "\\" in m:
            continue
        refs += 1
        if not check_ref(page, m):
            broken += 1
            err("link", f"{page} -> {m}")
ok("link", f"死链检查: {refs} 个引用, {broken} 断链")

# ---------- 9. en 页面中文泄漏 ----------
# en 博文: 正文 (含代码围栏内) 汉字 > 50 视为漏翻 (slug/translationKey 除外)
# 例外白名单: 品牌名与专有名词
HAN_WHITELIST = ["王丰羽", "王豐羽", "静心", "jingxin", "损不足以奉有余", "不足", "有余"]
for p in posts["en"]:
    han = len(re.findall(r"[\u4e00-\u9fff]", p["body"]))
    if han > 50:
        err("en-han", f"{p['path']}: en 正文汉字 {han} (>50, 疑似漏翻)")

# en 静态页可见文本: 过滤标签/脚本后出现汉字 (品牌名白名单除外)
zh_ui_strs = ["返回博客", "上一页", "下一页", "搜索文章", "排序", "查看详情", "去看看",
              "查看", "排序方式", "首页"]
for page in glob.glob("en/**/*.html", recursive=True):
    html = open(page, encoding="utf-8", errors="ignore").read()
    visible = re.sub(r"<(script|style)[^>]*>.*?</\1>", "", html, flags=re.S)
    visible = re.sub(r"<[^>]+>", "", visible)
    for w in HAN_WHITELIST:
        visible = visible.replace(w, "")
    seqs = re.findall(r"[\u4e00-\u9fff]{2,}", visible)
    seqs = [s for s in seqs if s not in HAN_WHITELIST]
    if seqs:
        err("en-han", f"{page}: en 页面出现中文: {sorted(set(seqs))[:8]}")
for page in glob.glob("en/blog/posts/*/index.html"):
    html = open(page, encoding="utf-8", errors="ignore").read()
    for s in zh_ui_strs:
        if s in html:
            err("en-ui", f"{page}: en 页面含中文 UI 文案「{s}」")

# ---------- 10. 三语首页卡片对等 ----------
home_cards = {}
for l in LANGS:
    hf = f"{l}/index.html"
    if os.path.exists(hf):
        home_cards[l] = open(hf, encoding="utf-8").read().count("FengInvest")
    else:
        err("home", f"{hf} 缺失")
if len(set(home_cards.values())) == 1 and home_cards:
    ok("home", f"三语首页 FengInvest 卡片对等: {home_cards}")
elif home_cards:
    err("home", f"三语首页 FengInvest 卡片数量不一: {home_cards}")

# ---------- 11. 三语页面清单对等 (根目录一级页面) ----------
for l in ("zh-cn", "zh-hk", "en"):
    pages_l = {os.path.basename(p) for p in glob.glob(f"{l}/*.html")}
    if l == "zh-cn":
        base = pages_l
    elif pages_l != base:
        miss = base - pages_l
        extra = pages_l - base
        if miss or extra:
            err("parity", f"{l}: 与 zh-cn 页面清单不一 缺{sorted(miss)[:5]} 多{sorted(extra)[:5]}")
if not issues or all(not i.startswith("[parity]") for i in issues):
    ok("parity", "三语根目录一级页面清单对等")

# ---------- 11.5 页面结构与头图 (div 配平 + 首页结构不变量) ----------
# 背景 1: 首页改版时多写一个 </div> 提前关闭容器, 头图错位、白色分隔消失 —— div 必须配平。
# 背景 2: 首页结构契约: 单张头图(刚好一屏) → 软件项目三卡 → 关于 → 三主线 → 博客卡。
DIV_OPEN = re.compile(r"<div\b")
DIV_CLOSE = re.compile(r"</div\b")
for l in ("zh-cn", "zh-hk", "en"):
    for page in sorted(glob.glob(f"{l}/*.html")):
        h = open(page, encoding="utf-8").read()
        n_open, n_close = len(DIV_OPEN.findall(h)), len(DIV_CLOSE.findall(h))
        if n_open != n_close:
            err("struct", f"{page} <div>/</div> 不配平: {n_open} 开 vs {n_close} 闭")
for l in ("zh-cn", "zh-hk", "en"):
    hf = f"{l}/index.html"
    if not os.path.exists(hf):
        continue
    hfull = open(hf, encoding="utf-8").read()
    h = hfull[hfull.index("<body"):]  # 结构类检查只看 body, head 里的 CSS/JS 引用不计
    n_slides = h.count("slider-single-item")
    if n_slides != 1:
        err("struct", f"{hf} 头图应为单张 slider-single-item, 实际 {n_slides} 张")
    if "100svh" not in hfull:
        err("struct", f"{hf} 头图缺 100svh 一屏兜底")
    if "whats-new-section" in h:
        err("struct", f"{hf} 仍存在已移除的「最新」区块 (whats-new-section)")
    i_soft, i_about = h.find("software-cards-section"), h.find('id="about"')
    if i_soft == -1:
        err("struct", f"{hf} 缺软件项目区 (software-cards-section)")
    elif i_about == -1:
        err("struct", f"{hf} 缺关于区 (id=about)")
    elif not (h.find("End Home Slider") < i_soft < i_about):
        err("struct", f"{hf} 软件项目区必须紧跟头图之后、关于区之前")
    for proj in ("FengInvest", "FengMedia", "FlyGo"):
        if proj not in h:
            err("struct", f"{hf} 软件项目区缺 {proj} 卡片")
if not issues or all(not i.startswith("[struct]") for i in issues):
    ok("struct", "div 配平 + 三语首页结构不变量全部通过")

# ---------- 12. 全站搜索 (JSON 索引 + 列表页搜索元素) ----------
for l in LANGS:
    idx_file = f"{l}/blog/index.json"
    if not os.path.exists(idx_file):
        err("search", f"{idx_file} 缺失 (需 hugo JSON 输出 + deploy)")
        continue
    try:
        items = json.load(open(idx_file, encoding="utf-8"))
    except Exception as e:
        err("search", f"{idx_file} 解析失败: {e}")
        continue
    n = len(items)
    if n < 90:
        err("search", f"{idx_file} 仅 {n} 条 (<90, 索引不完整)")
    bad_fields = [i for i, it in enumerate(items) if not it.get("url") or not it.get("title") or "content" not in it]
    empty_body = [it.get("url", i) for i, it in enumerate(items) if len((it.get("content") or "").strip()) < 100]
    if bad_fields:
        err("search", f"{idx_file} {len(bad_fields)} 条缺 url/title/content 字段: {bad_fields[:5]}")
    if empty_body:
        err("search", f"{idx_file} {len(empty_body)} 条正文为空 (<100 字符): {empty_body[:5]}")
    if not bad_fields and not empty_body and n >= 90:
        ok("search", f"{idx_file}: {n} 条, 字段齐全, 正文非空")
    lp = f"{l}/blog/index.html"
    if os.path.exists(lp):
        lh = open(lp, encoding="utf-8").read()
        for needle, label in [('id="blogSearch"', "搜索框"), ('id="searchResults"', "搜索结果容器"),
                              ("index.json", "索引引用"), ('id="blogGrid"', "文章网格")]:
            if needle not in lh:
                err("search", f"{lp} 缺{label} ({needle})")

# ---------- 12.5 hover 态对比度 (静态 CSS 分析) ----------
# 背景: 首页 default-btn-one 暗色 hover 白底白字 bug (内联暗色规则压过全局 hover 规则)。
# 原理: 收集主 CSS + 各页内联 <style> 中所有带 ":hover" 且显式声明背景色的规则;
# 把 hover 背景与 (hover 规则自身 + 同一基础选择器的其他规则, 含暗色变体) 声明的
# 文字色两两配对, 按 WCAG 算对比度, <4.5 报问题。
# 跳过: vendor 压缩库、背景 transparent/none、无显式 hover 背景 (无法可靠配对)。
def _css_parse_color(v):
    v = v.strip().rstrip(";").strip()
    if v.startswith("!"): return None
    m = re.match(r"#([0-9a-fA-F]{3}|[0-9a-fA-F]{6})$", v)
    if m:
        h = m.group(1)
        if len(h) == 3: h = "".join(c * 2 for c in h)
        return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
    m = re.match(r"rgba?\(([\d.]+),\s*([\d.]+),\s*([\d.]+)(?:,\s*([\d.]+))?", v)
    if m:
        rgba = [float(x) for x in m.groups()]
        return tuple(int(x) for x in rgba[:3]) + (rgba[3],) if len(rgba) == 4 else tuple(int(x) for x in rgba[:3])
    return None

def _css_contrast(fg, bg):
    def lin(c):
        c /= 255.0
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    l1 = 0.2126 * lin(fg[0]) + 0.7152 * lin(fg[1]) + 0.0722 * lin(fg[2])
    l2 = 0.2126 * lin(bg[0]) + 0.7152 * lin(bg[1]) + 0.0722 * lin(bg[2])
    hi, lo = max(l1, l2), min(l1, l2)
    return (hi + 0.05) / (lo + 0.05)

_rule_re = re.compile(r"([^{}]+)\{([^{}]*)\}")
HOVER_CSS_FILES = ("assets/css/style.css", "assets/css/responsive.css", "assets/css/blog-static.css")
hover_sources = {}
for cf in HOVER_CSS_FILES:
    if os.path.exists(cf):
        hover_sources[cf] = open(cf, encoding="utf-8").read()
for l in LANGS:
    for hp in glob.glob(f"{l}/*.html"):
        hs = open(hp, encoding="utf-8").read()
        blocks = re.findall(r"<style[^>]*>(.*?)</style>", hs, re.S)
        if blocks:
            hover_sources[hp] = "\n".join(blocks)

def _norm_sel(s):
    return re.sub(r"\s+", " ", s.strip())

hover_pairs = []  # (source, base_selector, bg, fg)
_hover_colors = []  # (css_text, selector_normalized) for cross-source color collection
for src, css in hover_sources.items():
    for sel, body in _rule_re.findall(css):
        decls = dict(
            (d.split(":", 1)[0].strip().lower(), d.split(":", 1)[1])
            for d in body.split(";") if ":" in d
        )
        if "color" in decls:
            _hover_colors.append((css, _norm_sel(sel), decls["color"]))
for src, css in hover_sources.items():
    for sel, body in _rule_re.findall(css):
        if ":hover" not in sel or "," in sel:
            continue
        decls = dict(
            (d.split(":", 1)[0].strip().lower(), d.split(":", 1)[1])
            for d in body.split(";") if ":" in d
        )
        bg = _css_parse_color(decls.get("background-color") or decls.get("background") or "")
        if bg is None or (len(bg) == 4 and bg[3] < 0.5):
            continue  # 无显式背景 / 半透明背景无法可靠计算
        base = _norm_sel(sel).replace(":hover", "")
        base_nodark = re.sub(r'^body\[data-theme="dark"\]\s*', "", base)
        base_is_dark = base_nodark != base
        fgs = set()
        c_hover = _css_parse_color(decls.get("color", ""))
        if c_hover: fgs.add(c_hover)
        # 收集同样作用于该 hover 元素的文字色: 跨文件 (页面内联可覆盖全局 CSS),
        # 同选择器或更长 (更具体, 如暗色变体 body[data-theme=dark] x y z)。 
        # hover 规则自己声明了 color 时, 同选择器的基底 color 被覆盖, 不配对。
        for css2, sel2, cval2 in _hover_colors:
            if "data-theme" in sel2 and not base_is_dark:
                continue
            if base_is_dark and not sel2.startswith("body[data-theme"):
                continue
            s2 = re.sub(r'^body\[data-theme="dark"\]\s*', "", sel2)
            if s2 == base_nodark and c_hover:
                continue
            if s2 == base_nodark or s2.endswith(" " + base_nodark):
                c2 = _css_parse_color(cval2)
                if c2: fgs.add(c2)
        for fg in fgs:
            if len(fg) == 4 and fg[3] < 0.5: continue
            hover_pairs.append((src, base, bg, fg if len(fg) == 3 else tuple(
                round(fg[i] * fg[3] + bg[i] * (1 - fg[3])) for i in range(3))))

_hover_bad = []
_hover_rules = []  # (base_nodark, is_dark, color_parsed, bg_parsed, sel_len)
for src, css in hover_sources.items():
    for sel, body in _rule_re.findall(css):
        if ":hover" not in sel or "," in sel: continue
        d = dict((x.split(":", 1)[0].strip().lower(), x.split(":", 1)[1])
                 for x in body.split(";") if ":" in x)
        s = _norm_sel(sel).replace(":hover", "")
        sn = re.sub(r'^body\[data-theme="dark"\]\s*', "", s)
        _hover_rules.append((sn, sn != s, _css_parse_color(d.get("color", "")),
                             _css_parse_color(d.get("background-color") or d.get("background") or ""),
                             len(s)))
for src, base, bg, fg in hover_pairs:
    cr = _css_contrast(fg, bg)
    if cr >= 4.5: continue
    # 若存在更具体、声明了 color 的 :hover 规则, 其自身配色达标, 则视为已被覆盖, 不报
    base_nodark = re.sub(r'^body\[data-theme="dark"\]\s*', "", base)
    base_is_dark = base_nodark != base
    resolved = any(
        r2_color and (r2_bg or bg) and _css_contrast(
            r2_color, r2_bg if r2_bg else bg) >= 4.5
        for rn, rd, r2_color, r2_bg, _ in _hover_rules
        if rn.endswith(base_nodark) and rd == base_is_dark and rn != base_nodark
    )
    if not resolved:
        _hover_bad.append((src, base, cr, fg, bg))
if _hover_bad:
    for src, base, cr, fg, bg in sorted(_hover_bad, key=lambda x: x[2])[:20]:
        err("hover", f"{src}: '{base}' hover 底#{'%02x%02x%02x'%bg} 上文字#{'%02x%02x%02x'%fg} 对比度 {cr:.2f}")
else:
    ok("hover", f"hover 态对比度: {len(hover_pairs)} 组 (文字色xhover背景) 全部 ≥4.5")

# ---------- 13. 暗色/亮色对比度审计 (无头浏览器真实渲染) ----------
# 用无头 Chromium 真实渲染每个页面, 强制切换暗色/亮色, 枚举可见文本元素,
# 计算 WCAG 对比度 (<4.5, 大字 <3.0 记为问题); 双向对照:
#   暗色问题 = 亮色正常、暗色才变差 (如蓝底黑字)
#   亮色问题 = 暗色正常、亮色才变差 (如浅底亮字)
# 两种模式都低的是设计元素, 不算主题 bug。5dt-pd 图示为站长拍板的设计豁免。
# 跳过: 垫在背景图/渐变上的文字无法可靠计算; /page/1/ 等自动跳转页。
DESIGN_ALLOWLIST = ("5dt-pd",)

DARK_EVAL_JS = r"""
() => {
  function parse(c) {
    const m = c.match(/rgba?\(([\d.]+),\s*([\d.]+),\s*([\d.]+)(?:,\s*([\d.]+))?\)/);
    if (!m) return null;
    return [ +m[1], +m[2], +m[3], m[4] === undefined ? 1 : +m[4] ];
  }
  function lum(r) {
    const f = v => { v /= 255; return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4); };
    return 0.2126 * f(r[0]) + 0.7152 * f(r[1]) + 0.0722 * f(r[2]);
  }
  function ratio(a, b) {
    const l1 = lum(a), l2 = lum(b);
    return (Math.max(l1, l2) + 0.05) / (Math.min(l1, l2) + 0.05);
  }
  function hex(r) {
    return '#' + r.slice(0, 3).map(v => Math.round(v).toString(16).padStart(2, '0')).join('');
  }
  function effectiveBg(el) {
    let stack = [];
    for (let n = el; n && n.nodeType === 1; n = n.parentElement) {
      const cs = getComputedStyle(n);
      if (cs.backgroundImage && cs.backgroundImage !== 'none') return null;
      const bg = parse(cs.backgroundColor);
      if (bg) stack.push(bg);
      if (bg && bg[3] >= 1) break;
    }
    let out = [255, 255, 255, 1];
    for (let i = stack.length - 1; i >= 0; i--) {
      const b = stack[i];
      if (b[3] >= 1) { out = b.slice(0, 3); continue; }
      const a = b[3];
      out = out.map((v, j) => b[j] * a + v * (1 - a));
    }
    return out;
  }
  const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  const seen = new Set();
  const problems = [];
  while (walker.nextNode()) {
    const t = walker.currentNode.textContent.trim();
    if (!t) continue;
    const el = walker.currentNode.parentElement;
    if (!el || seen.has(el)) continue;
    seen.add(el);
    const cs = getComputedStyle(el);
    if (cs.display === 'none' || cs.visibility === 'hidden' || +cs.opacity === 0) continue;
    if (!el.getClientRects().length) continue;
    const fg = parse(cs.color);
    if (!fg || fg[3] === 0) continue;
    const bg = effectiveBg(el);
    if (!bg) { continue; }
    const size = parseFloat(cs.fontSize);
    const bold = +cs.fontWeight >= 600;
    const large = size >= 24 || (size >= 18.66 && bold);
    const r = ratio(fg.slice(0,3), bg);
    const min = large ? 3.0 : 4.5;
    if (r < min) {
      const desc = el.tagName.toLowerCase() +
        (el.id ? '#' + el.id : '') +
        (el.className && typeof el.className === 'string' && el.className.trim()
          ? '.' + el.className.trim().split(/\s+/).slice(0, 3).join('.') : '');
      const key = desc + '|' + hex(fg) + '|' + hex(bg);
      if (!seen.has(key)) {
        seen.add(key);
        problems.push({ desc, text: t.slice(0, 40), fg: hex(fg), bg: hex(bg), ratio: +r.toFixed(2) });
      }
    }
  }
  return problems;
}
"""


def run_dark_audit(max_pages=0):
    """返回 (输出文本, 是否通过)。自起 http.server + 无头 Chromium 逐页双向审计。"""
    lines = []

    class QuietHandler(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *a):
            pass

    handler = functools.partial(QuietHandler, directory=ROOT)
    httpd = socketserver.TCPServer(("127.0.0.1", 0), handler)  # 自动选空闲端口
    port = httpd.server_address[1]
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    base = f"http://127.0.0.1:{port}"

    pages = sorted(glob.glob("*.html"))
    for l in LANGS:
        pages += sorted(p for p in glob.glob(f"{l}/**/*.html", recursive=True))
    if max_pages:
        pages = pages[:max_pages]

    from playwright.sync_api import sync_playwright

    total_bad = 0
    with sync_playwright() as p:
        browser = p.chromium.launch()
        ctx = browser.new_context(viewport={"width": 1280, "height": 900})
        # 外链 (字体/统计) 与审计无关, 全部拦截提速
        ctx.route("**://*/**", lambda route: route.continue_()
                  if route.request.url.startswith("http://127.0.0.1") else route.abort())
        page = ctx.new_page()
        for path in pages:
            if any(k in path for k in DESIGN_ALLOWLIST):
                continue
            url = base + "/" + path
            try:
                page.goto(url, wait_until="load", timeout=15000)
            except Exception:
                try:
                    page.wait_for_load_state("domcontentloaded", timeout=10000)
                except Exception:
                    lines.append(f"  [skip] 加载失败: {path}")
                    continue
            try:
                # 冻结过渡/动画: 否则采样到 transition 中间色, 产生大量误报
                page.add_style_tag(content="*, *::before, *::after { transition: none !important; animation: none !important; }")
                page.evaluate("() => { if (window.__siteTheme) window.__siteTheme.applyTheme('dark'); else document.body.setAttribute('data-theme','dark'); }")
                page.wait_for_timeout(60)
                dark = page.evaluate(DARK_EVAL_JS)
                page.evaluate("() => { if (window.__siteTheme) window.__siteTheme.applyTheme('light'); else document.body.removeAttribute('data-theme'); }")
                page.wait_for_timeout(60)
                light = page.evaluate(DARK_EVAL_JS)
            except Exception as e:
                # 个别页面会 JS 自动跳转 (如 /page/1/), 销毁执行环境: 回退后跳过
                lines.append(f"  [skip] evaluate 失败 {path}: {type(e).__name__}")
                try:
                    page.goto("about:blank", timeout=5000)
                except Exception:
                    pass
                continue
            dark_keys = {(x["desc"], x["text"]) for x in dark}
            light_keys = {(x["desc"], x["text"]) for x in light}
            probs = [x for x in dark if (x["desc"], x["text"]) not in light_keys]
            probs += [dict(x, mode="light") for x in light if (x["desc"], x["text"]) not in dark_keys]
            if probs:
                total_bad += len(probs)
                lines.append(f"\n== {path} ({len(probs)} 个问题)")
                for x in probs[:12]:
                    tag = " [亮色]" if x.get("mode") == "light" else ""
                    lines.append(f"   {x['ratio']:>5.2f}  fg={x['fg']} bg={x['bg']}{tag}  <{x['desc']}>  \"{x['text']}\"")
                if len(probs) > 12:
                    lines.append(f"   ... 还有 {len(probs) - 12} 个")
        browser.close()
    httpd.shutdown()
    audited = len(pages) - len([k for k in DESIGN_ALLOWLIST])
    summary = f"暗色模式审计: {audited} 页, {total_bad} 个低对比度问题"
    lines.append(summary)
    ok_flag = total_bad == 0
    return "\n".join(lines), ok_flag


dark_out = None
if ARGS.no_dark:
    notes.append("[dark] 按参数跳过暗色对比度审计 (--no-dark)")
elif importlib.util.find_spec("playwright") is None:
    notes.append("[dark] 未安装 playwright, 跳过暗色对比度审计 (pip install playwright && playwright install chromium)")
else:
    print("暗色模式审计运行中 (全站真实渲染, 需几分钟)…")
    dark_out, dark_ok = run_dark_audit(ARGS.max_dark_pages)
    if dark_ok:
        ok("dark", dark_out.splitlines()[-1].strip())
    else:
        err("dark", f"发现低对比度问题, 明细见下方 [dark] 输出")

# ---------- 汇总 ----------
if dark_out:
    print("=" * 60)
    print("[dark] 对比度审计明细:")
    for line in dark_out.splitlines():
        if line.strip():
            print("  " + line)
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
