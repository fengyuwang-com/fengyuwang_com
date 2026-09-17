# 发版与门禁

> 从 `AGENTS.md` 瘦身搬入：Git & Versioning、Release Gate、Privacy、Docker Preview 全文。
> "何时跑全量"的唯一出处是本篇；别处只写一句话 + 链接。

## Git Strategy

| Branch | Purpose | Deploys |
|--------|---------|---------|
| `master` | Production | ✅ Cloudflare Pages — **NEVER push without explicit user approval** |
| `dev` | Daily work | ❌ Never deploys directly; push freely after checks pass |

## Commit Flow

1. (内容改动后) `cd hugo && hugo --gc --cleanDestinationDir && bash deploy.sh` 把博客构建部署到仓库根
2. 日常 dev：跑快速检查 `python3 tools/check_site.py --no-dark`，通过再 commit
3. `git add -A && git commit -m "descriptive message"`
4. push dev（master 不动）
5. 发版（= 合并并 push 到 master）前：跑全量 `python3 tools/check_site.py`（含浏览器审计），全绿才合，**必须先获得用户明确批准**

## Release Gate — 全站大脚本（发版到 master 前必跑）

全站只有**一个**检查脚本：`tools/check_site.py`。所有能机械判定的检查全部合并在这里
（16 节：内容规范 / 三语对齐 / 简繁质量 / 围栏结构 / 部署一致性 / sitemap / 站点配置 /
死链 / en 中文泄漏 / 三语页面对等 / 全站搜索索引 / 暗色+亮色对比度浏览器审计 /
导航栏完整性 / 按钮等高；节数随脚本增长，以脚本注释头为准）。

**三条铁律（只卡发版，不卡日常 dev）：**

1. **发版 = 合并并 push 到 master 之前**：把本次改动暴露的、能机械判定的新问题类型
   **固化成新的检查节并入大脚本**，然后跑全量 `python3 tools/check_site.py`，
   全绿（"全部检查通过 ✔"）才发版。不允许只修问题不加检查——同样的 bug 不许出现第二次。
2. **日常 dev 提交/push 到 dev**：跑快速检查 `python3 tools/check_site.py --no-dark` 通过即可，
   不必每次都跑几分钟的浏览器审计。线上或本地发现 bug 并修复后，发版前再用全量做回归。
3. 检查逻辑只写在大脚本这一处；不要另建零散检查脚本（写作用单篇模式即可）。

**用法：**

```bash
python3 tools/check_site.py                      # 全量 (含对比度审计, 约几分钟, 发版必跑)
python3 tools/check_site.py --no-dark            # 快速静态检查 (跳过浏览器审计)
python3 tools/check_site.py --article <index.md> # 单篇发布前校验 (痕迹词+字数+直角引号)
python3 tools/check_site.py --max-dark-pages 20  # 调试: 只审计前 N 页
```

**`--article` 单篇模式**（脚本第 49–70 行）：参数一给就立即处理并 `sys.exit(0)`，其余检查全部不跑；对每篇打印
`汉字=<正文汉字数> 痕迹词=[...] 直角引号=N 处 加粗紧邻引号=N`，命中 `TRACES` 或 `md_bold_quote_hits()` 时行首标 `!!!`，
**但退出码仍是 0**（不卡 CI，靠人看输出）。判定词清单与写作口径见 `docs/guide/WRITING-博文写作规范.md`。

**检查节速查**（脚本会增长，权威以 `tools/check_site.py` 注释头为准）：

| 节 | 类别 tag | 检查内容 | 关键阈值 |
|---|---|---|---|
| 1 | `trace`/`quote`/`mdbold`/`desc`/`short` | 内容规范 | 痕迹词 0；`date>=2026-08-15` 的新文「」=0；description <10 字；zh 正文汉字 <200 |
| 2 | `translate` | 三语对齐 | 非 draft 必须按 `translationKey` 凑齐 3 语 |
| 3 | `zh-hk-simp`/`zh-cn-trad` | 简繁泄漏 | zh-hk 可转简体 >3 处；zh-cn 出现繁体字 |
| 4 | `fence`/`rawhtml` | 代码围栏闭合 / 裸 HTML 未包 ` ```html ` |
| 5 | `deploy` | 源 vs 根 `{lang}/blog/posts/*` 篇数一致；RSS item = min(20, 篇数) |
| 6 | `sitemap` | URL 覆盖全部博文；三语 blog/archive/tags 齐全 |
| 7 | `headers`/`llms`/`config` | `_headers` 覆盖三语 `/blog*`；llms.txt 链接存在 |
| 8 | `link` | 死链（根 `*.html` + `{lang}/**/*.html` 的 href/src；**`<script>…</script>` 被整体剥离，src 不校验**） |
| 9 | `en-han`/`en-ui` | en 博文汉字 >50；en 页面可见文本 2+ 汉字 |
| 10 | `home` | 三语首页 `FengInvest` 出现次数对等 |
| 11 | `parity` | 三语根目录一级页面清单必须完全一致 |
| 11.5 | `struct` | div 配平；首页结构不变量；模板署名不得残留 Zoomin/Barakah |
| 12 | `search` | `{lang}/blog/index.json` ≥90 条；列表页 8 个必需元素；archive 页存在 |
| 12.5 | `hover` | 静态解析 CSS，`:hover` 背景 × 文字色 WCAG <4.5 |
| 13 | `dark` | 无头 Chromium 逐页双向（暗+亮）真实渲染对比度 |
| 15 | `navbar` | 导航可达性 + 三语 `copy` 键对齐 + 无硬编码文案（`NAVBAR_EXEMPT_PAGES` 只有 `404.html`，不许私自豁免真实内容页） |
| 16 | `btn-height` | 同容器 `.default-btn` 与 `.default-btn-one` 等高 |
| 16.5 | `h1-size` | 含 `<h1>` 的 `{lang}/*.html` 页内 `<style>` 必须声明 h1 `font-size`（正则要求 `<style>` 无属性，写成带属性会漏判） |
| 16.5b | `seo-url` | canonical/og:url/hreflang/jsonld-url 必须 `https://www.fengyuwang.com` 且不带 `.html` |
| 16.5c | `page-elements` | 每页 10 个必备片段（导航/页脚/backToTop/description/canonical/og:title/og:description/og:image/twitter:card/hreflang x-default） |
| 16.5d | `key-selector` | 用 `.section-card` 的页，h2/h3/`.punchline`/`.case-desc` 必须声明 `font-size`，后两者还须 `color` |
| 16.6 | `redirects` | `_redirects` 5 条金丝雀齐全、有效规则 ≥29 |
| 16.7 | `jsonld` | 逐页解析 JSON-LD（防 2026-09-16 Search Console Unparsable 复发） |

对比度审计原理：无头 Chromium 真实渲染 466 页，逐页双向 (暗+亮) 切换，按 WCAG
计算每个可见文字的有效对比度，<4.5 (大字 <3.0) 报问题；只报"对照模式下正常"的
主题 bug。已知设计豁免：`human-in-the-loop.html` 架构图 (站长拍板)。若新增设计豁免，须用户确认后
写入 `DESIGN_ALLOWLIST`。

**退出码：** 有任何问题 => 1，全部通过 => 0。CI/人工都以退出码为准。

## Privacy

- Prefix title with `*` + `draft: true` for personal info.
- Never commit `.env` or any file with API keys, tokens, or passwords.

## Docker Preview

```powershell
docker compose up -d    # Start preview at test.fengyuwang.com
docker compose down     # Stop
```

The tunnel uses a token from Cloudflare Zero Trust → Tunnels. Put it in `.env`.
