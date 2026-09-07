#!/usr/bin/env python3
"""
site_audit.py — 全站统一体检（Oracle-style self-test）

用法:
    python3 _scripts/site_audit.py            # 全部检查
    python3 _scripts/site_audit.py --quiet    # 只输出失败项和总结

检查范围（每次改站后、push 前运行）:
  1. 三语言页面集合一致（en / zh-cn / zh-hk 顶层页 + blog 结构）
  2. 每个内容页: 回顶按钮元素 + 公共 CSS + 主题 JS，且无内联 back-to-top 副本
  3. 暗色模式: 页面自定义类必须有对应 body[data-theme="dark"] 覆盖
     （启发式: 内联 style 里出现浅色 background/color 的自定义类集合求差）
  4. 语言元信息: hreflang 四件套无重复、og:url 指向本语言目录、<html lang> 正确
  5. 根语言跳转: 无 meta refresh 抢跑、head 内有 site-lang 判断逻辑
  6. 404 页: head 内有解析跳转、独立样式与暗色规则存在
  7. sitemap.xml 覆盖三语言全部顶层页

退出码: 0 = 全部通过, 1 = 有失败。CI / pre-push hook 可直接用。
"""

import glob
import re
import sys
from collections import defaultdict

ROOT_LANGS = ('en', 'zh-cn', 'zh-hk')
EXCLUDE_DIRS = ('.git', 'hugo', '_scripts', 'scripts', 'docs')

# 有意不套公共体系的特例（新增特例必须在此登记并写明原因）
ALLOWLIST_NO_BUTTON = {
    'index.html',            # 语言选择页，无滚动内容
    '404.html',              # 独立样式页（见其内联注释），自带按钮
    'check-shell.html',      # 内部检查工具页
}
ALLOWLIST_INLINE_BTT = {
    '404.html',              # 不加载公共 CSS，按钮样式必须内联（页内有注释说明）
}

QUIET = '--quiet' in sys.argv
failures = []


def fail(f, check, detail=''):
    failures.append((f, check, detail))


def load(f):
    with open(f, encoding='utf-8', errors='replace') as fh:
        return fh.read()


def all_html():
    out = []
    for f in glob.glob('**/*.html', recursive=True):
        if f.startswith(EXCLUDE_DIRS):
            continue
        out.append(f)
    return sorted(out)


def check_language_parity(files):
    by_page = defaultdict(set)
    for f in files:
        parts = f.split('/')
        if len(parts) == 2 and parts[0] in ROOT_LANGS:
            by_page[parts[1]].add(parts[0])
    for page, langs in sorted(by_page.items()):
        missing = set(ROOT_LANGS) - langs
        if missing:
            fail(f'*/{page}', 'language-parity', f'missing: {sorted(missing)}')
    if not by_page:
        fail('(root)', 'language-parity', 'no top-level pages found at all')


def check_shared_components(files):
    for f in files:
        if f in ALLOWLIST_NO_BUTTON:
            continue
        s = load(f)
        if 'http-equiv="refresh"' in s:
            continue  # 纯跳转页无需组件
            continue  # 纯跳转页无需组件
        if 'class="back-to-top"' not in s:
            fail(f, 'back-to-top', 'button element missing')
        if 'assets/css/style.css' not in s:
            fail(f, 'shared-css', 'does not load assets/css/style.css')
        if 'shared-subpage-navbar.js' not in s:
            fail(f, 'theme-js', 'theme/navbar JS missing (dark mode switch lives there)')
        if re.search(r'\.back-to-top\s*\{position', s) and f not in ALLOWLIST_INLINE_BTT:
            fail(f, 'inline-back-to-top', 'inline .back-to-top CSS copy — use shared CSS')


CUSTOM_CLASS_RE = re.compile(r'\.([a-z][a-z0-9-]{3,})\s*\{[^}]*background[^}]*\}', re.I)


def check_dark_mode(files):
    for f in files:
        if f in ALLOWLIST_NO_BUTTON:
            continue
        s = load(f)
        if 'http-equiv="refresh"' in s:
            continue  # 纯跳转页无暗色概念
        if 'data-theme="dark"' not in s and 'shared-subpage-navbar.js' not in s:
            fail(f, 'dark-mode', 'no dark selectors and no theme JS')
            continue
        styles = '\n'.join(re.findall(r'<style[^>]*>(.*?)</style>', s, re.S))
        custom = {c for c in CUSTOM_CLASS_RE.findall(styles)
                  if not c.startswith(('btn-', 'owl-', 'mean', 'fa-'))}
        dark = set(re.findall(r'data-theme="dark"\][^{]*\.([a-z][a-z0-9-]{3,})', styles))
        # 页面特有的类（不在公共 CSS 出现的近似判断：至少出现 2 次的样式类）
        from collections import Counter
        counts = Counter(re.findall(r'\.([a-z][a-z0-9-]{3,})', styles))
        page_specific = {c for c, n in counts.items() if n >= 2} & custom
        uncovered = {c for c in page_specific if c not in dark and f'data-theme="dark"] .{c}' not in styles
                     and f'data-theme="dark"] [class' not in styles}
        # 宽容处理: 只报告同时带 color/background 定义的类中缺口最多的部分
        if len(uncovered) >= 4:
            fail(f, 'dark-mode', f'uncovered custom classes: {sorted(uncovered)[:8]}')


def check_lang_meta(files):
    for f in files:
        parts = f.split('/')
        if len(parts) != 2 or parts[0] not in ROOT_LANGS:
            continue
        d, name = parts
        s = load(f)
        hrefs = re.findall(r'hreflang="([^"]+)"', s)
        if name != 'index.html':
            if sorted(hrefs) != sorted(['en', 'zh-CN', 'zh-HK', 'x-default']):
                fail(f, 'hreflang', f'got {hrefs}')
        og = re.search(r'og:url" content="([^"]+)"', s)
        if og and f'/{d}/' not in og.group(1):
            fail(f, 'og:url', og.group(1))
        lang = re.search(r'<html lang="([^"]+)"', s)
        want = {'en': 'en', 'zh-cn': 'zh-CN', 'zh-hk': 'zh-HK'}[d]
        if not lang or lang.group(1) != want:
            fail(f, 'html-lang', lang.group(1) if lang else 'missing')


def check_root_redirect():
    s = load('index.html')
    if 'http-equiv="refresh"' in s:
        fail('index.html', 'root-redirect', 'meta refresh must not exist (it forces zh-cn and races JS)')
    head = s.split('</head>')[0]
    if 'site-lang' not in head or 'location.replace' not in head:
        fail('index.html', 'root-redirect', 'head script must resolve language before render')
    if '[data-theme="dark"]' not in s:
        fail('index.html', 'dark-mode', 'selector page lacks dark support')


def check_404():
    s = load('404.html')
    head = s.split('</head>')[0]
    if 'resolveTarget' not in head:
        fail('404.html', '404-redirect', 'resolution JS must run in <head> before render')
    if 'data-theme="dark"' not in s:
        fail('404.html', 'dark-mode', '404 page lacks dark rules')
    if 'Standalone page' not in s:
        fail('404.html', 'inline-css-note', 'keep the explanatory comment for the inline style')


def check_sitemap(files):
    try:
        sm = load('sitemap.xml')
    except FileNotFoundError:
        fail('sitemap.xml', 'sitemap', 'missing')
        return
    for f in files:
        parts = f.split('/')
        if len(parts) == 2 and parts[0] in ROOT_LANGS:
            url = f'https://fengyuwang.com/{f[:-5] if not f.endswith("index.html") else f.split("/")[0]}/'
            if url not in sm and f'https://fengyuwang.com/{f}' not in sm:
                fail('sitemap.xml', 'sitemap', f'not listed: {url}')


def main():
    files = all_html()
    check_language_parity(files)
    check_shared_components(files)
    check_dark_mode(files)
    check_lang_meta(files)
    check_root_redirect()
    check_404()
    check_sitemap(files)

    if failures:
        by_file = defaultdict(list)
        for f, c, d in failures:
            by_file[f].append((c, d))
        print(f'FAIL — {len(failures)} problem(s) in {len(by_file)} file(s):\n')
        for f in sorted(by_file):
            print(f'  {f}')
            for c, d in by_file[f]:
                print(f'    [{c}] {d}')
        sys.exit(1)
    print(f'PASS — {len(files)} pages checked: language parity, shared components, '
          f'dark mode, hreflang/og:url/lang, root redirect, 404, sitemap.')
    sys.exit(0)


if __name__ == '__main__':
    main()
