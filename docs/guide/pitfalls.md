# 踩坑记录

> 从 `AGENTS.md` Common Mistakes 搬入详细修复法 + `LESSONS.md` 教训正文。
> 压缩不变量在 `AGENTS.md` 正文；"何时跑全量"以 `release-gate.md` 为准，本篇不重复。
> 另见 `DESIGN.md` §7.1（导航下拉）、§7.7（Projects Zone）、§7.7.1（storm-bg）、§8（移动端）、§9（暗色）。

## 1. Extra `</div>` closing `page-wrap` early

**Symptom**: White dividers disappear after a certain point. Content below has no white background.

**Root cause**: An extra `</div>` was added, closing `page-wrap` before all sections.

**Fix**: Count `<div` vs `</div>` in the body section. They must balance. Remove the extra `</div>`.

## 2. Cross-link pointing to wrong page

**Symptom**: Visitor flow is broken — clicking the bottom link goes to an unexpected page.

**Fix**: Check the Cross-Link Mapping table in `page-structure.md`. The mkt page should always link to portfolio (technical).

## 3. Human-in-the-Loop section without white divider

**Symptom**: The Human-in-the-Loop Answers section on mkt.html has no 12px gap above it.

**Fix**: Ensure the previous section (`:last-of-type` before insertion) is no longer `:last-of-type` after insertion — `margin-bottom: 12px` applies automatically.

## 4. Self-praise wording

**Symptom**: Text uses "你的" (your/yours) to describe capabilities positively.

**Fix**: Rewrite as objective statements. Instead of "你的能力是互相增强的", use "当不同的能力相互增强的时候".

## 5. "一个打三个" vs "超越三者之和的价值"

The capabilities page used to say "一个打三个" (one beats three). The correct framing is "超越三者之和的价值" (value that exceeds the sum of its three parts) — it's about synergy, not competition.

## 6. Adding items to the Tech navbar dropdown

**Symptom**: The Tech ▾ dropdown grows too long, or a new software/topic link is added in the wrong place.

**Fix**: Dropdowns are **auto-fit with scroll-when-needed** (global behavior, see DESIGN.md §7.1 "Submenu auto-fit & scroll"): they expand to full content height when the screen has room and scroll only when it doesn't — never introduce a two-column grid or a fixed-height cap. The Tech dropdown is a single column with two group headers. Rules:

- Every submenu leads with its own **overview link** (`XXX概览` / `XXX Overview`): Tech ▾ leads with `技术概览`, same as `市场学概览`/`投资概览`/`艺术概览` lead their submenus, and Ethos ▾ leads with `理念概览` before its anchor links. The overview labels come from the per-language `casesOverview`/`portfolioOverview`/`investmentOverview`/`artOverview`/`ethosOverview` keys in the `copy` objects — never hard-code or revert to a bare page-name item (e.g. 投资 ▾ must show `投资概览`, not a duplicate `投资`).
- Software projects go under the `软件项目` header, tech topics under `技术研究`.
- **FengInvest lives under the Investment ▾ dropdown** (it's an investment tool, and its pages declare `data-section="investment"`) — not under Tech's 软件项目.
- Every item and header label must be added to **all three language `copy` objects** in `shared-subpage-navbar.js` (`software`, `techResearch`, etc.) — never hard-code a string.
- The mobile drawer mirrors the same list single-column; don't give it its own different structure.

## 7. `storm-bg` is a ONE-TIME Tech-page effect — do not copy it elsewhere

**Symptom**: The 「闪电炫光蓝」 storm-glow on `zh-cn/tech.html`'s four software sections gets copy-pasted into other pages/languages, or a flashing variant is reintroduced.

**Fix**: `.content-block.storm-bg` + `@keyframes storm-flow` are a **bespoke, one-off** effect for the Tech page's software-project showcase only. Rules:

- Do **not** add `storm-bg` to any other page without an explicit request.
- The blue is a `::before` overlay — it stays **always present**, gently breathing (6s flow), and must **never flash/strobe**. (A 1.2s `storm-flash` flicker was tried and rejected).
- The class is additive: it sits on `content-block section-bg storm-bg`, keeps the section's own `--section-bg-img`, and the white divider gaps stay white.
- See DESIGN.md §7.7.1 for full documentation.

## 8. Mobile nested-card padding & CTA button width

**Symptom**: On mobile, text inside `.block-inner → .section-card → .content-text-card` renders too narrow (~8 CJK chars/line) because the three nested paddings never shrink at `≤599px`; or `.cta-row` buttons size unevenly by their text length.

**Fix**: Apply the standard mobile overrides in each page's `@media (max-width: 599px)` block (see DESIGN.md §8 "Mobile text-width recovery") and the equal-width `.cta-row` rule (see DESIGN.md §8 "CTA buttons equal width"). The batch script `scripts/apply-mobile-fix.js` applies both across en/zh-cn/zh-hk idempotently. When touching a new content sub-page, make sure it already has these two rules; run the script after adding a new page rather than hand-editing each CSS variant.

## 9. Text overflowing its card (e.g. `、/brainstorm。`)

**Symptom**: A long unbreakable phrase (CJK + `/` + `、` at line end, e.g. `快捷指令：/publish、/rage-mode、/fetch-topics、/review、/brainstorm。`) spills outside the card's right edge.

**Root cause**: CJK kinsoku rules forbid `、` at line start and `/` before a break, so the whole tail chunk can't break and overflows — the site had no `overflow-wrap` rule.

**Fix**: The global rule in `assets/css/style.css` (`overflow-wrap: break-word; word-break: break-word` on `.content-text-card, .block-inner`) handles it site-wide. Don't add per-page hacks; if a case still overflows, check the element is inside `.content-text-card` or `.block-inner` (per-page inline styles on other wrappers don't inherit the fix).

## 10. Project sections without the dark shell

**Symptom**: A delivered project section on the Tech page uses the same frosted `content-block section-bg` as the ideology sections — the projects don't read as a different kind of content.

**Fix**: Wrap the projects in `.projects-shell` (storm glow-blue shell; structure/CSS in DESIGN.md §7.7 "Projects Zone (Dark Shell)"). Each project keeps `class="project-card"` instead of `content-block section-bg` (drop `--section-bg-img`), and keeps its inner `.block-inner > .section-card` unchanged. Inside the shell only light cards; dark-mode cards get a hairline border via `body[data-theme="dark"] .projects-shell .section-card`. Rules: direct child of `page-wrap` (never inside `.container` — white strips appear on both sides); placed directly after the card grid, before the ideology sections; **no border-radius** (square edges embed it in the white page); **storm glow-blue** background — 3 radial glows + 2 diagonal light beams + blue gradient, plus `storm-glow` (pulsing halo) and `storm-flash` (lightning double-flash on `::before`) animations; **dark mode must stay a clearly BLUE glowing body** (`#16295c → #2547c8` gradient, uniform `0 0 46px` blue halo, `animation: none`) — a near-black start (`#0b1530`) or an offset black shadow reads as a "black square" against the `#0a0e1a` page (the 方形外壳 bug); never plain dark gray.

## 11. Dark-mode text left near-black

**Symptom**: In dark mode some text is hard or impossible to read because it keeps its light-mode dark color on the dark background.

**Fix**: This site has **no global `body[data-theme="dark"] h1,h2,h3,p { … }` fallback** — every dark text color is a per-class, per-page inline rule, and anything not covered stays near-black. Every user-facing text element must get an explicit `body[data-theme="dark"]` override (light `#e5ecf4` headings, `#9fb0c3`/`#94a3b8` body). Known gaps already fixed: `human-in-the-loop` (原5dt-pd) `.section-card h1`, `art.html` `.content-text-card h3`, `capabilities` `.tree-toggle`, homepage About 区/博客卡片/分页/blockquote/全局 `p`/`a`/`code` (2026-09-07 全站双向审计归零). Call out — never leave a `#0f172a`/`#1d1d1f`/`#1e293b`/`#475569`/`#515154` color on a text element without a dark counterpart. See DESIGN.md §9.

## 12. zh-hk 混入粤语口语 / 残留简体（from LESSONS.md)

- zh-hk = 香港繁体书面语，NOT 粤语口语（嘅/佢/咗/唔係/睇/喺/邊度/乜嘢 → 的/他/了/不是/看/在/哪裡/什麼）。
- 从 zh-cn 复制后用 opencc-js（cn→hk）全文件转换，勿逐字 sed；转换后把`王豐羽`改回`王丰羽`。
- 三语语义一致（信达雅），不逐字翻译；「信息」→「資訊」等地道用词。
- 卡片字体 frozen values：h3=1.2rem, p=.82rem, .card-btn=.78rem，任何页不得偏离。
- 跨语言 href 必须与页面语言一致；navbar data-section 与实际页面匹配；link-card 导航链见 `page-structure.md`。
- 新增页面同步更新 sitemap.xml；card 图 `w=600`、section 图 `w=1000`；art 暖色是唯一例外色板。
- 不出现 ADHD/dyslexia/「艺术比工作重要」等求职不利内容。
- 暗色黑框红线：暗底上不用黑色 box-shadow。
- 工具链：`grep -P` 在 MinGW 不可用，用 `grep -E`；`sed -i` 与 Edit 工具勿混用。

## 13. master 领先 dev 事故（from LESSONS.md, 2026-09-05）

- 开工前必须 `git fetch origin` 并检查 `git log --oneline dev..origin/master`（及反向），确认相对位置再动；master 领先先合并进 dev 再开工。
- 主分支纪律：未经用户明确允许不得 push 到 main/master；dev 是唯一默认推送目标。
- 批量重写 HTML 用二进制读写保留 CRLF，避免整文件假 diff。

## 14. 新增页面门禁雷区（速查，2026-09-17 侦察归并）

新增 `{lang}/*.html` 展示页时最容易踩红的点（节号见 `docs/guide/release-gate.md` 门禁节速查，权威以 `tools/check_site.py` 为准）：

- **`parity`（第 11 节）**：三语页面清单逐条对等 → 新增页必须**同时**建 `zh-cn/x.html`、`zh-hk/x.html`、`en/x.html`，文件名完全相同（英文名，禁拼音）。
- **`navbar`（第 15 节）**：每个 `{lang}/*.html` 必须能从导航栏到达。做法是改 `assets/js/shared-subpage-navbar.js`：三个语言 `copy` 对象各加 `xxx` / `xxxHref` 两个 key（键集三语必须一致），且**桌面模板数组与移动 drawer 都要真正引用** `labels.xxxHref`——**只加 key 不加引用仍判不可达**。`*Href` 三语路径结构只差语言前缀；界面文案一律走 copy key，不许硬编码（豁免仅 `NAVBAR_TEXT_EXEMPT`：English/简体中文/繁體中文/GitHub/LinkedIn/YouTube/BiliBili）。`NAVBAR_EXEMPT_PAGES` 只有 `404.html`，不许私自豁免真实内容页。改完 bump `?v=` 版本串。
- **`page-elements`（16.5c）**：10 项必备片段缺一即红，清单见 `check_site.py` 的 `REQUIRED_SNIPPETS`。
- **`h1-size` / `key-selector`（16.5 / 16.5d）**：页内 `<style>` 必须**无属性**地写（写成 `<style type="text/css">` 会被正则漏掉）；h1 必须声明 `font-size`；用了 `.section-card` 时 h2/h3 也要声明 `font-size`，`.punchline` / `.case-desc` 还要声明 `color`（暗色另写 `body[data-theme="dark"]` 覆盖）。
- **`seo-url`（16.5b）**：canonical / og:url / hreflang / JSON-LD 的绝对 URL 必须是 `https://www.fengyuwang.com/...` 且不带 `.html`（带 `.html` 会被 Cloudflare Pages 308）。
- **`link`（第 8 节）不校验 `<script src>`**：死链检查先整体剥掉 `<script>…</script>`（连标签一起），所以 `<script src>` 指向不存在的文件**永远查不出来**，只能人工盯。**历史实例（已修）**：`a07373ae` 把 `5dt-pd` 改名 `human-in-the-loop` 时，只改了**目录名**没改**文件名**——三语页面全被改成引用 `../assets/js/human-in-the-loop/human-in-the-loop-viewer.js`，盘上却只有 `5dt-pd-viewer.js`，被引文件 404 → `#root` 空、架构图 viewer 完全不加载（2026-09-17 侦察发现，躲过门禁；2026-09-18 `git mv` 对齐文件名修复，三语 headless 复验渲染正常）。**改名类提交必须同时核对「目录名 / 文件名 / 引用串」三者，别只改前两个。**
- **`btn-height`（第 16 节）**：同容器 `.default-btn` 与 `.default-btn-one` 混排时高度必须相等（`.default-btn-one` 的 `margin-top:5px` 会撑高兄弟按钮 5px）；用 `.cta-row` + `flex:1 1 auto; min-width:160px; max-width:240px`。
- **`hover`（12.5）**：页内 `<style>` 里 `:hover` 若显式声明背景色，与文字色配对的 WCAG 必须 ≥4.5（历史 bug：首页 `.default-btn-one` 暗色 hover 白底白字）。
- **`redirects`（16.6）**：`_redirects` 不得丢 5 条金丝雀、有效规则 ≥29（2026-09-11 曾被一次盲写覆盖 39 行既有规则）；任何整文件重写先备份。
- **`en-han` / `en-ui`（第 9 节）**：en 页面可见文本不得出现 2+ 连续汉字；en 博文汉字 >50 判漏翻。

**数据可视化先例（新页无现成可抄）**：全站手写页原本 0 个手写 `<svg>` / `<canvas>`（2026-09-18 的 `system.html` 是首个例外）；现成"图形化"做法只有两条——纯 CSS 渐变/伪元素（`tech.html` 的 `storm-bg`、`art.html` 的展厅光），或仿 `human-in-the-loop.html` 的 `#root` + 本地打包 JS（`5dt-pd-viewer.js`，188 KB React bundle）。**没有 chord / force / D3 / ECharts 先例**；要做图优先手写内联 SVG（零依赖，自带暗色与 reduced-motion 兜底）。
