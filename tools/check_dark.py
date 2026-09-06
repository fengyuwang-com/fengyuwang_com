#!/usr/bin/env python3
"""暗色模式对比度审计 (2026-09-06)

用无头 Chromium 真实渲染每个页面, 强制 body[data-theme="dark"],
枚举所有可见文本元素, 计算前景色 vs 有效背景色(沿祖先链混合)的 WCAG 对比度,
< 4.5 (大字 < 3.0) 记为问题; 同时跑一遍对照模式:
- 暗色问题 = 亮色正常、暗色才变差 (暗色模式 bug, 如蓝底黑字);
- 亮色问题 = 暗色正常、亮色才变差 (亮色模式 bug, 如浅底亮字)。
两种模式都低的是设计元素 (如彩色徽章), 不算主题 bug。
专门抓 "暗色下蓝底/浅底出现黑字灰字" 和 "亮色下浅底出现白字" 这两类。

用法: python3 tools/check_dark.py [--port 8091] [--max-pages N]
在仓库根目录执行; 自己起 http.server, 与已运行的服务不冲突。
退出码: 有问题 => 1
"""
import argparse
import glob
import http.server
import os
import socketserver
import threading
import functools

os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ROOT = os.getcwd()
LANGS = ["zh-cn", "zh-hk", "en"]

EVAL_JS = r"""
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
  // 沿祖先链把半透明背景逐层混合, 得到有效底色; 遇到背景图/渐变返回 null (无法判定)
  function effectiveBg(el) {
    let stack = [];
    for (let n = el; n && n.nodeType === 1; n = n.parentElement) {
      const cs = getComputedStyle(n);
      if (cs.backgroundImage && cs.backgroundImage !== 'none') return null;
      const bg = parse(cs.backgroundColor);
      if (bg) stack.push(bg);
      if (bg && bg[3] >= 1) break;
    }
    let out = [255, 255, 255, 1]; // 兜底白色
    for (let i = stack.length - 1; i >= 0; i--) {
      const b = stack[i];
      if (b[3] >= 1) { out = b.slice(0, 3); continue; }
      const a = b[3];
      out = out.map((v, j) => b[j] * a + v * (1 - a));
    }
    return out;
  }
  const bodyBg = (() => {
    let c = parse(getComputedStyle(document.body).backgroundColor) || [255, 255, 255, 1];
    if (c[3] < 1) { const h = parse(getComputedStyle(document.documentElement).backgroundColor);
      if (h && h[3] >= 1) c = c.slice(0,3).map((v,i)=>v*c[3]+h[i]*(1-c[3])).concat([1]); }
    return c.slice(0, 3);
  })();
  const problems = [];
  const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  const seen = new Set();
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
    let bg = effectiveBg(el);
    if (!bg) { continue; } // 垫在背景图/渐变上, 无法可靠计算, 跳过
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


def discover_pages():
    pages = sorted(glob.glob("*.html"))
    for l in LANGS:
        pages += sorted(p for p in glob.glob(f"{l}/**/*.html", recursive=True))
    return pages


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a):
        pass


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--port", type=int, default=8091)
    ap.add_argument("--max-pages", type=int, default=0, help="调试: 限制页面数")
    args = ap.parse_args()

    handler = functools.partial(QuietHandler, directory=ROOT)
    httpd = socketserver.TCPServer(("127.0.0.1", 0), handler)  # 自动选空闲端口
    args.port = httpd.server_address[1]
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    base = f"http://127.0.0.1:{args.port}"

    from playwright.sync_api import sync_playwright

    pages = discover_pages()
    if args.max_pages:
        pages = pages[: args.max_pages]
    total_bad = 0
    # 设计豁免: 整页判为刻意设计的彩色图示, 不参与对比度判定 (2026-09-07 站长拍板)
    DESIGN_ALLOWLIST = ("5dt-pd",)
    with sync_playwright() as p:
        browser = p.chromium.launch()
        ctx = browser.new_context(viewport={"width": 1280, "height": 900})
        # 外链 (字体/统计) 与审计无关, 全部拦截提速
        ctx.route("**://*/**", lambda route: route.continue_()
                  if route.request.url.startswith("http://127.0.0.1") else route.abort())
        page = ctx.new_page()
        for i, path in enumerate(pages):
            url = base + "/" + path
            try:
                page.goto(url, wait_until="load", timeout=15000)
            except Exception:
                try:
                    page.wait_for_load_state("domcontentloaded", timeout=10000)
                except Exception:
                    print(f"  [skip] 加载失败: {path}")
                    continue
            try:
                # 冻结过渡/动画: 否则采样到 transition 中间色, 产生大量误报
                page.add_style_tag(content="*, *::before, *::after { transition: none !important; animation: none !important; }")
                page.evaluate("() => { if (window.__siteTheme) window.__siteTheme.applyTheme('dark'); else document.body.setAttribute('data-theme','dark'); }")
                page.wait_for_timeout(60)
                dark = page.evaluate(EVAL_JS)
                page.evaluate("() => { if (window.__siteTheme) window.__siteTheme.applyTheme('light'); else document.body.removeAttribute('data-theme'); }")
                page.wait_for_timeout(60)
                light = page.evaluate(EVAL_JS)
            except Exception as e:
                # 个别页面会 JS 自动跳转, 销毁执行环境: 回退后跳过
                print(f"  [skip] evaluate 失败 {path}: {type(e).__name__}")
                try:
                    page.goto("about:blank", timeout=5000)
                except Exception:
                    pass
                continue
            # 对照模式下的既存低对比 (设计元素) 不算主题 bug; 双向都报
            dark_keys = {(x["desc"], x["text"]) for x in dark}
            light_keys = {(x["desc"], x["text"]) for x in light}
            dark_probs = [x for x in dark if (x["desc"], x["text"]) not in light_keys]
            light_probs = [x for x in light if (x["desc"], x["text"]) not in dark_keys]
            probs = dark_probs
            if light_probs:
                probs = probs + [dict(x, mode="light") for x in light_probs]
                probs += []
            if any(k in path for k in DESIGN_ALLOWLIST):
                continue
            if probs:
                total_bad += len(probs)
                print(f"\n== {path} ({len(probs)} 个问题)")
                for x in probs[:12]:
                    tag = " [亮色]" if x.get("mode") == "light" else ""
                    print(f"   {x['ratio']:>5.2f}  fg={x['fg']} bg={x['bg']}{tag}  <{x['desc']}>  \"{x['text']}\"")
                if len(probs) > 12:
                    print(f"   ... 还有 {len(probs) - 12} 个")
        browser.close()
    httpd.shutdown()
    print(f"\n暗色模式审计: {len(pages)} 页, {total_bad} 个低对比度问题")
    raise SystemExit(1 if total_bad else 0)


if __name__ == "__main__":
    main()
