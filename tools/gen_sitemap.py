#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成全站 sitemap.xml（纯静态：仓库根目录即 Cloudflare Pages 输出）。

用法: python3 tools/gen_sitemap.py   （hugo/deploy.sh 已挂钩，部署后自动执行）
规则:
- 扫描根目录 *.html（排除 404.html）+ 各 {lang}/ 目录下全部 *.html；
  URL 以页面内 <link rel="canonical"> 为准，无 canonical 时按路径推导。
- 博文 lastmod 取 hugo frontmatter 的 lastmod（无则 date），重部署稳定；
  其余页面取该文件最近一次 git 提交日期，git 不可用时退回文件 mtime。
"""
import datetime
import glob
import os
import re
import subprocess
import sys
import unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
BASE = "https://www.fengyuwang.com"
LANGS = ("zh-cn", "zh-hk", "en")

CANON_RE = re.compile(r'<link\b[^>]*rel="canonical"[^>]*href="([^"]+)"')
FM_RE = re.compile(r"^---\n(.*?)\n---\n", re.S)
POST_FILE_RE = re.compile(r"^(zh-cn|zh-hk|en)/blog/posts/([^/]+)/index\.html$")


def read(path):
    with open(path, encoding="utf-8", errors="ignore") as fh:
        return fh.read()


def fm_field(fm, key):
    m = re.search(rf"^{key}:\s*\"?([^\"\n]+?)\"?\s*$", fm, re.M)
    return m.group(1).strip() if m else ""


# 博文 (lang, 部署目录名) -> lastmod-or-date；目录名规则与 check_site.py 的 url_seg 保持一致
post_dates = {}
for lang in LANGS:
    for f in glob.glob(f"hugo/content/{lang}/blog/posts/*/index.md"):
        m = FM_RE.match(read(f))
        if not m:
            continue
        fm = m.group(1)
        if re.search(r"^draft:\s*true", fm, re.M):
            continue
        d = os.path.basename(os.path.dirname(f))
        seg = unicodedata.normalize("NFC", (fm_field(fm, "slug") or d).replace(" ", "-"))
        date = (fm_field(fm, "lastmod") or fm_field(fm, "date"))[:10]
        if date:
            post_dates[(lang, seg)] = date


def git_lastmod(path):
    try:
        out = subprocess.run(["git", "log", "-1", "--format=%as", "--", path],
                             capture_output=True, text=True, timeout=10)
        v = out.stdout.strip()
        if v:
            return v
    except Exception:
        pass
    return datetime.date.fromtimestamp(os.path.getmtime(path)).isoformat()


def url_for(path):
    m = CANON_RE.search(read(path))
    if m:
        return m.group(1)
    rel = path.replace(os.sep, "/")
    if rel == "index.html":
        return BASE + "/"
    if rel.endswith("/index.html"):
        return BASE + "/" + rel[: -len("index.html")]
    return BASE + "/" + rel[: -len(".html")]


files = [p for p in glob.glob("*.html") if os.path.basename(p) != "404.html"]
for lang in LANGS:
    files += sorted(glob.glob(f"{lang}/**/*.html", recursive=True))

entries = {}
for f in files:
    url = url_for(f)
    rel = f.replace(os.sep, "/")
    m = POST_FILE_RE.match(rel)
    if m and (m.group(1), m.group(2)) in post_dates:
        lastmod = post_dates[(m.group(1), m.group(2))]
    else:
        lastmod = git_lastmod(f)
    entries[url] = max(entries.get(url, ""), lastmod)

urls = sorted(entries, key=lambda u: (u != BASE + "/", u))
body = "\n".join(
    "  <url>\n    <loc>%s</loc>\n    <lastmod>%s</lastmod>\n  </url>" % (u, entries[u])
    for u in urls
)
xml = (
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<urlset xmlns="http://sitemaps.org/schemas/sitemap/0.9">\n'
    + body + "\n</urlset>\n"
)
with open("sitemap.xml", "w", encoding="utf-8") as fh:
    fh.write(xml)

n_posts = sum(1 for u in urls if "/blog/posts/" in u)
print(f"[sitemap] {len(urls)} 个 URL（其中博文 {n_posts} 篇）→ sitemap.xml")
if n_posts == 0:
    print("[sitemap] 警告: 未扫到任何博文 URL, 检查 {lang}/blog/posts/ 是否已部署", file=sys.stderr)
    sys.exit(1)
