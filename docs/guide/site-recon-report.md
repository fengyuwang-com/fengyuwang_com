只读侦察任务（不要改任何文件、不要提交）。目标：把 C:\Projects\fengyuwang_com（Hugo 站点，生产 https://www.fengyuwang.com）的设计语言与工程规范摸清楚，为"新增一个纯静态展示页"提供可落地的依据。当前分支 dev。

请给出结构化报告（中文，带文件路径与关键代码片段引用）：

1. **工程结构**：hugo 目录布局（content/{zh-cn,zh-hk,en}/…、layouts、assets、static、data 等）、主题是哪套（自带主题还是自定义 layouts？）、是否用 Hugo Modules；构建命令与门禁脚本位置（例如 check_site.py，列出其全部检查项与运行方式、如何只跑单页 --article）。
2. **设计语言（重点）**：CSS 变量/设计 token 文件路径与全部主要变量（背景色、文字三级灰、强调色、圆角、发丝线、阴影、字体栈、字号阶梯、行高）；浅色/暗色两套如何切换（class 名、是否有 prefers-color-scheme、暗色审计门禁要求）；栅格与容器宽度、卡片/面板的既有视觉范式（边框、玻璃、阴影）；是否有动画/滚动 reveal 的既有做法与性能约定。
3. **页面骨架与组件**：基础 layout（baseof/single/list）如何组织；导航与页脚如何引入；h1 字号门禁（h1-size）具体规则；已存在的自定义/特殊页面有哪些（尤其非文章类页面，如 landing、专题页、工具页），给 1-2 个最接近"数据可视化/仪表盘"型页面的实现路径与写法（front matter、layout 覆盖方式、是否允许内联 <script>/<style>）。
4. **内容与多语规范**：文章 front matter 必填字段、slug/translationKey 约定、三语如何对齐（opencc s2hk 转换? en 全译?）；正文写作约束（禁用词、直角引号禁令、痕迹词清单、字数下限、参考文献格式）；canonical/og:url 规则与 seo-url 门禁细节（www、无 .html）。
5. **资源与限制**：图片放哪、命名与尺寸规范、是否可放 JS/CSS 独立文件（static/ 还是 assets/ 走 pipeline？）、有无 CSP/无外部 CDN 的约定、页面体积或依赖限制；有没有现成的图表/可视化先例（SVG 手写？canvas？chord/force 图？）。
6. **已知雷区**：门禁里最容易踩红的点（列举脚本里的具体检查函数名与阈值）、以及历史上因为什么被门禁拦过（可查 git log 里的门禁相关提交信息）。

只读证据优先：直接读文件、跑只读命令（如 python check_site.py --help 之类只读用法、grep），不要写文件、不要 push。

I'll start by mapping the repository structure and finding the key files.

# fengyuwang_com 只读侦察报告

> 分支 `dev`，未做任何写操作。所有路径为绝对路径。核心结论一句话：**这个仓库的根目录就是 Cloudflare Pages 的发布目录**，`hugo/` 只负责博客；手写页面（`{lang}/*.html`）是独立于 Hugo 的静态 HTML，新增展示页应当走这条路径。

---

## 1. 工程结构

### 1.1 双层结构（关键认知）

```
C:\Projects\fengyuwang_com\            ← Cloudflare Pages 发布根（根目录即产物）
├── index.html                          语言选择页（唯一有 :root 变量的一页）
├── 404.html / robots.txt / sitemap.xml / llms.txt / llms-full.txt
├── _headers / _redirects               CF Pages 配置（39 条跳转规则）
├── assets/{css,js,img,fonts,i18n}      全站共享静态资源（相对路径 ../assets/... 引用）
├── {zh-cn,zh-hk,en}/                   每语言一套手写 HTML（一级页面 + blog/ 产物）
│   ├── *.html                          手写页（27 个/语言）
│   └── blog/ tags/ archive/            ← hugo 构建产物被 deploy.sh 拷进来
├── blog-static.css / blog-static.js    与 assets/ 下同名文件内容完全一致（diff 无差异）
├── hugo/                               ← Hugo 工程（只产博客）
│   ├── hugo.toml
│   ├── content/{zh-cn,zh-hk,en}/{blog/posts,archive,blog/_index.md}
│   ├── layouts/                        ← 极简自定义，无主题
│   └── deploy.sh
├── tools/                              check_site.py / gen_sitemap.py / zh2hk.py / even_dates.py / merge_tags.py
└── _scripts/                           一次性批处理脚本（site_audit.py、translate-en-pages.py 等，非门禁）
```

### 1.2 主题 / Hugo Modules

- **没有主题，没有 Hugo Modules**：无 `hugo/go.mod`、无 `hugo/themes/`、无 `module` 段。
- `hugo/layouts/` 全量只有 7 个文件：
  - `C:\Projects\fengyuwang_com\hugo\layouts\_default\baseof.html`（博客 baseof）
  - `hugo\layouts\_default\term.html`
  - `hugo\layouts\blog\list.html`、`list.json`、`rss.xml`、`single.html`
  - `hugo\layouts\archive\single.html`
- **Hugo 也不走 asset pipeline**：没有 `hugo/assets/`、没有 `static/`（全仓 `find -name static` 为空）。`baseof.html` 直接写死绝对路径 `/assets/css/style.css`、`/blog-static.css`，即引用仓库根的真实文件。

### 1.3 hugo.toml 要点（`C:\Projects\fengyuwang_com\hugo\hugo.toml`）

```toml
baseURL = "https://www.fengyuwang.com/"
defaultContentLanguage = "zh-cn"
defaultContentLanguageInSubdir = true
publishDir = "../_site"
disableKinds = ["home", "sitemap", "robotsTXT", "404"]
[languages]  zh-cn / zh-hk / en  → contentDir = "content/{lang}"
[taxonomies] category / tag
[outputs]    section = ["HTML","RSS","JSON"]; page=["HTML"]; home=["HTML"]
[related]    tags=100 / title=60 / text=40（相关阅读按题材相关度）
```

**推论（对新增页至关重要）**：Hugo 只输出到 `../_site`，而 `deploy.sh` **只把 `blog/`、`tags/`、`archive/` 拷回根目录**。因此：
- 想在 `content/{lang}/` 下加一个 Hugo 页 → 构建产物在 `_site/` 里，**不会被部署**。
- **纯静态展示页的正确落点是仓库根 `{lang}/xxx.html`（三语各一份）**，与现有 27 个手写页同构。

### 1.4 构建命令（`C:\Projects\fengyuwang_com\hugo\deploy.sh`）

```bash
hugo --cleanDestinationDir
for lang in zh-cn zh-hk en; do
  cp -r ../_site/$lang/blog    ../$lang/blog    # 同理 tags / archive
done
python3 ../tools/gen_sitemap.py
rm -rf ../_site
```

日常：`cd hugo && hugo --gc --cleanDestinationDir && bash deploy.sh`
`gen_sitemap.py` 会**自动扫描根 `{lang}/**/*.html`**，新页无需手改 sitemap（见 §4.4）。

### 1.5 门禁脚本：`C:\Projects\fengyuwang_com\tools\check_site.py`（1128 行）

运行方式（在**仓库根目录**执行）：

```bash
python3 tools/check_site.py                      # 全量：静态 + 无头 Chromium 对比度审计（约几分钟，发版必跑）
python3 tools/check_site.py --no-dark            # 日常 dev 快速检查（跳过浏览器审计）
python3 tools/check_site.py --article <md>...    # 单篇发布前校验（痕迹词+汉字数+直角引号+加粗引号）
python3 tools/check_site.py --max-dark-pages 20  # 调试：只审计前 N 页
```
退出码：有问题 `1`，全绿 `0`。

**`--article` 模式（第 49–70 行）**：参数一给就立即处理并 `sys.exit(0)`，其余全部检查不执行。对每个 md 打印：
`汉字=<正文汉字数> 痕迹词=[...] 直角引号=N 处 加粗紧邻引号=N`
判定项：`TRACES` 命中、`md_bold_quote_hits()` 命中 → 行首标 `!!!`（但**退出码仍是 0**，不卡 CI）。

**全量检查节清单（按脚本注释头 + 代码）**：

| 节 | 类别 tag | 检查内容 | 关键阈值 |
|---|---|---|---|
| 1 | `trace`/`quote`/`mdbold`/`desc`/`short` | 内容规范 | 痕迹词 0；date≥`2026-08-15` 的新文「」=0；description <10 字报错；zh 正文汉字 <200 报错 |
| 2 | `translate` | 三语对齐 | 非 draft 文章必须凑齐 3 语（按 translationKey，缺则用目录名） |
| 3 | `zh-hk-simp`/`zh-cn-trad` | 简繁泄漏 | zh-hk 可转简体 >3 处报错；zh-cn 出现繁体字即报错 |
| 4 | `fence`/`rawhtml` | 代码围栏闭合 / 裸 HTML 无 ```html 围栏 |
| 5 | `deploy` | 源 vs 根 `{lang}/blog/posts/*` 篇数一致；RSS item 数 = min(20, 篇数) |
| 6 | `sitemap` | URL 覆盖全部博文；三语 blog/archive/tags URL 齐全 |
| 7 | `headers`/`llms`/`config` | `_headers` 覆盖三语 `/blog*`；llms.txt 链接存在；CF token 占位符提示 |
| 8 | `link` | 死链（根 `*.html` + `{lang}/**/*.html` 的 href/src） |
| 9 | `en-han`/`en-ui` | en 博文汉字 >50 报错；en 页面可见文本出现 2+ 汉字报错 |
| 10 | `home` | 三语首页 `FengInvest` 出现次数对等 |
| 11 | `parity` | **三语根目录一级页面清单必须完全一致** |
| 11.5 | `struct` | div 配平；三语首页结构不变量（单张 `slider-single-item` + `hero-static` + `100svh` + `software-cards-section` 位置 + 三个项目卡）；模板署名不得残留 Zoomin/Barakah |
| 12 | `search` | `{lang}/blog/index.json` ≥90 条、字段齐、正文非空；列表页 8 个必需元素；archive 页存在 |
| 12.5 | `hover` | 静态解析 CSS，`:hover` 背景 × 文字色 WCAG <4.5 报错 |
| 13 | `dark` | 无头 Chromium 逐页双向（暗+亮）真实渲染对比度，<4.5（大字 <3.0）报错 |
| 15 | `navbar` | 导航可达性 + 三语 copy 键对齐 + 无硬编码文案 |
| 16 | `btn-height` | 同容器 `.default-btn` 与 `.default-btn-one` 高度一致 |
| 16.5 | `h1-size` | 含 `<h1>` 的 `{lang}/*.html` 页内 `<style>` 必须声明 h1 `font-size` |
| 16.5b | `seo-url` | canonical/og:url/hreflang/jsonld-url 必须 `https://www.fengyuwang.com` 且不带 `.html` |
| 16.5c | `page-elements` | 每页 10 个必备片段 |
| 16.5d | `key-selector` | 用 `.section-card` 的页面，h2/h3/`.punchline`/`.case-desc` 必须声明 font-size，后两者还需 color |
| 16.6 | `redirects` | `_redirects` 5 条金丝雀 + 有效规则数 ≥29 |

---

## 2. 设计语言（重点）

### 2.1 设计 token 的存在形式：**没有 token 文件**

- `assets/css/style.css` 里 **0 个 CSS 自定义属性、0 处 `var(--`**；`.page-wrap`/`.content-block`/`.section-card` 等核心样式**不在**主 CSS 里，而是**每页内联 `<style>` 里各写一份**。
- 全仓唯一的内联自定义属性是 `--section-bg-img`（126 处，`style="--section-bg-img:url(...)"`）。
- 唯一有 `:root` 变量的文件是根 `C:\Projects\fengyuwang_com\index.html`（语言选择页，独立体系）。
- **`C:\Projects\fengyuwang_com\DESIGN.md` 是唯一 token 源头**（1484 行）。新页必须从 §5/§6/§9 抄值，复制既有页的 `<style>` 块是最稳做法。

### 2.2 全部主要变量（DESIGN.md §4/§5/§6，已核对页面实值）

**颜色**

| 角色 | 浅色 | 暗色 |
|---|---|---|
| page-wrap 底 | `#ffffff` | `#0a0e1a` |
| content-block 底 | `#f5f5f7` | `#111827` |
| section-bg 底 | `#1e293b` | `#0a0e1a` |
| section-bg `::after` 磨砂 | `rgba(245,245,247,.72)` + `blur(20px)` | `rgba(17,24,39,.88)` |
| 文字一级（标题） | `#0f172a`（art 页 `#1d1d1f`） | `#e5ecf4` |
| 文字二级（正文） | `#475569` | `#9fb0c3` |
| 文字三级（次要/meta） | `#6b7280` / `#64748b` | `#94a3b8`（浅一档 `#8296ac`） |
| 强调蓝（链接/hover） | `#0071e3` | `#2997ff` |
| 次强调蓝（punchline） | `#2563eb` | `#6b9aff` |
| 按钮底 | `#0071e3` | `#4f7eff`（仅 back-to-top；`.default-btn` 本身无暗色覆盖） |
| 按钮 hover | `#0062cc` | `#3a6af0` |
| navbar 磨砂 | `rgba(255,255,255,0.72)` | `rgba(10,14,26,0.72)` |
| 导航链接 | `#1d1d1f` | `#f5f5f7` |
| section-card | `rgba(255,255,255,.90)` | `rgba(30,41,59,.90)` |
| content-text-card | `#ffffff` | `#0f172a` |

铁律：**只有一种强调色**，无暖色（唯一例外是 `art.html` 美术馆暖米色，§14 明确"exclusive"）；暗底**禁用黑色 box-shadow**（会成"黑方框"）。

**字体栈**：全站 `Nunito Sans`，Google Fonts 引入（`family=Nunito+Sans:wght@400;600;700;800;900`），无衬线、无 italic；权重 400/600/700/800。

**字号阶梯 + 行高**（DESIGN.md §4 表）

| 层级 | 字号 | 字重 | 行高 |
|---|---|---|---|
| Hero h1 | `clamp(30px,4vw,44px)` | 800 | 1.08 |
| Section h2 | `1.6rem`（≤991px `1.4rem`；≤599px `1.25rem`） | 800 | — |
| `.mkt-card` h3 | `1.2rem`（**frozen**） | 800 | — |
| content-text-card h3 | `1.05rem` | 700 | — |
| `.block-subtitle` | `.95rem` | 600 | 1.7 |
| 正文 | `.97rem` | 400 | 1.85 |
| `.mkt-card` p | `.82rem`（**frozen**） | — | 1.45 |
| `.card-btn` | `.78rem`（**frozen**） | 600 | — |
| 导航链接 | `12px` | 400 | — |
| `.stack-chip` | `.82rem` | 600 | — |
| `.punchline` | `1.15rem` | 700 | — |

**圆角**：section-card 18px / content-text-card 14px / mkt-card 18px / track-card 24px / track-split-shell 32px / 按钮 50px pill / chip 999px / submenu 14px / theme-toggle 20px / 汉堡 8px / 语言卡 28px / back-to-top 50%。

**发丝线（hairline）**：卡片边框统一 `1px solid rgba(148,163,184,.10)`（暗色 `.04`/`.03`）；navbar 阴影就是一根发丝 `0 1px 0 rgba(0,0,0,0.1)`；submenu 用 `border: 0.5px solid rgba(255,255,255,0.3)` + `0 0 0 0.5px rgba(255,255,255,0.04)`。

**阴影**：section-card `0 4px 16px rgba(15,23,42,.06)`；content-text-card `0 2px 8px rgba(15,23,42,.04)`；语言卡 `0 30px 80px rgba(15,23,42,0.12)`；portal `0 18px 48px rgba(0,0,0,0.12)`；back-to-top `0 8px 24px rgba(0,113,227,.3)`。**暗色下卡片阴影一律 `none`**（黑框红线）。

### 2.3 栅格与容器

| 元素 | 值 |
|---|---|
| `.block-inner` | `max-width: 720px; margin: 0 auto; padding: 0 24px` |
| `.content-block` | `padding: 44px 0 40px; margin-bottom: 12px`（≤991px `36/28`；≤599px `28/20`） |
| `.marketing-hero` | `padding: 52px 0 40px` |
| `.card-grid` | `grid-template-columns: repeat(3, minmax(0,1fr)); gap: 20px; padding: 0 0 48px`（DESIGN.md §7.3；`page-structure.md` 写的是 2 列，**两处口径不一致，以 DESIGN.md 为准**） |
| 响应式 | ≤991px 2 列、≤599px 1 列；navbar 断点 991px |
| `.section-card` padding | 32px（≤599px 20px） |
| nav shell | `max-width:1200px; padding:0 20px; min-height:44px`；`body{padding-top:44px!important}` |
| 移动端补偿 | ≤599px 时 `.block-inner` 12px、`.section-card` 20px、`.content-text-card` 16px（§8 "Mobile text-width recovery"） |

### 2.4 浅/暗切换机制

- 载体：`<body data-theme="dark">`（`applyTheme('dark')` 走 `window.__siteTheme`，无则直接 `setAttribute`）。
- 存储：`localStorage['site-theme']`；首次加载**尊重 `prefers-color-scheme`**（DESIGN.md §7.1 JS Behavior）。
- **无全局兜底**：全站没有 `body[data-theme="dark"] h1,h2,h3,p{...}` 统一回退，**每个可见文字元素必须自己写暗色覆盖**（AGENTS.md 不变量 3、DESIGN.md §9、pitfalls.md §11）。
- 暗色审计门禁：check_site 第 13 节，无头 Chromium 逐页双向渲染，标准 WCAG `<4.5`（≥24px 或 ≥18.66px+600 权重的大字 `<3.0`）；只报"另一模式正常"的主题 bug；豁免名单 `DESIGN_ALLOWLIST = ("human-in-the-loop",)`；新增豁免须用户确认。

### 2.5 卡片/面板既有范式

- **磨砂**：`backdrop-filter: saturate(180%) blur(20px)` + 半透明底（navbar、submenu、mobile drawer、section-bg `::after`）；卡片用 `blur(8px)`。
- 五种卡片先选后用：`.mkt-card`（图卡导航）、`.invest-card`（深色变体）、`.section-card`（磨砂白）、`.content-text-card`（实心白子卡）、`.track-card`（首页深壳内）。
- 白线是签名：`.content-block` 必须是 `.page-wrap` 直接子元素，靠 `margin-bottom: 12px` 露出白底。

### 2.6 动画 / reveal / 性能约定

- 已有库：`wow.min.js` + `animate.min.css`（scroll reveal 现成能力）、`jquery.appear/waypoints/counterup`、`owl.carousel`（首页轮播已停用）。
- 滚动 reveal 无统一约定，首页/子页主要靠 CSS transition + `IntersectionObserver`（博客 TOC scroll-spy，`rootMargin: '-80px 0px -60% 0px'`）。
- **必须带 reduced-motion 兜底**（DESIGN.md §8，各页内联块末尾）：
```css
@media (prefers-reduced-motion:reduce){*,*::before,*::after{animation-duration:0.01ms!important;animation-iteration-count:1!important;transition-duration:0.01ms!important;scroll-behavior:auto!important}}
```
- 性能约定：禁闪烁/频闪（storm-glow 从 1.2s flash 改成 6s 呼吸）、禁黑底阴影、审计时冻结 transition 防误报。

---

## 3. 页面骨架与组件

### 3.1 Hugo 侧骨架

`C:\Projects\fengyuwang_com\hugo\layouts\_default\baseof.html`（博客专用）：head 里 canonical/og/twitter/hreflang/JSON-LD 由模板生成，body 只挂 `#shared-subpage-navbar[data-section=blog]` → `section.content-section > .container > {{ block "main" }}` → footer 无（博客页无 footer），JS 只引 jquery/bootstrap/meanmenu/main/blog-static。

`blog/single.html`、`blog/list.html`、`archive/single.html`、`_default/term.html` 各自 `define "main"`，把 CSS 全写在自己的 `<style>` 里（含完整暗色覆盖）。`blog/list.json` 供搜索索引，`blog/rss.xml` 只保留最近 20 篇全文。

### 3.2 手写页骨架（新增展示页应复制这个）

`C:\Projects\fengyuwang_com\zh-cn\human-in-the-loop.html` 是**最接近"仪表盘/可视化"型**的样板（整页 146 行，单行压缩排版）：

```html
<body>
  <div id="shared-subpage-navbar" data-section="pd5"></div>
  <script src="../assets/js/shared-subpage-navbar.js"></script>
  <div class="page-wrap">
    <div id="root"></div>
    <script type="module" src="../assets/js/human-in-the-loop/human-in-the-loop-viewer.js"></script>
    <div class="content-block section-bg" style="--section-bg-img:url('https://images.unsplash.com/...')">
      <div class="block-inner"><div class="section-card">
        <h1>…</h1><p class="punchline">…</p>
        <div class="qa-group"><div class="qa-group-title">…</div>
          <div class="qa-chips"><span class="stack-chip">…</span></div>
        </div>
      </div></div>
    </div>
    <div class="link-card">
      <p>从极简框架到完整能力结构</p>
      <a class="default-btn" href="/zh-cn/capabilities.html">查看能力结构 →</a>
    </div>
  </div>
  <div id="shared-site-footer" class="bg-grey"></div>
  <script src="../assets/js/shared-site-footer.js"></script>
  <!-- jquery/bootstrap/meanmenu/appear/waypoints/counterup/owl/magnific/wow/main -->
  <button class="back-to-top" id="backToTop" onclick="window.scrollTo({top:0,behavior:'smooth'})">↑</button>
</body>
```

同类参考：
- `C:\Projects\fengyuwang_com\zh-cn\dog-ate-my-money.html`（332 行，纯内容展示页：5×content-block + 15×content-text-card + marketing-hero + link-card，无 card-grid）
- `C:\Projects\fengyuwang_com\zh-cn\tribute-to-laozi.html`（230 行，有 `.pillar-grid`/`.pillar-card` 自定义网格）
- `C:\Projects\fengyuwang_com\zh-cn\tech.html`（唯一有 `.projects-shell` + `storm-bg` 的页）

**导航/页脚引入方式**：不是 HTML 片段，而是 **JS 运行时注入**。页面只放空挂载点 `<div id="shared-subpage-navbar" data-section="...">` 和 `<div id="shared-site-footer">`，再引 `assets/js/shared-subpage-navbar.js` / `shared-site-footer.js`；navbar 读 `<html lang>` + `data-section`，`container.outerHTML = [...]` 整体替换（桌面菜单与移动 drawer 同一数组）。

### 3.3 h1-size 门禁规则（check_site 第 16.5 节，1004–1017 行）

```python
for f in glob("zh-cn/*.html") + glob("en/*.html") + glob("zh-hk/*.html"):
    if "<h1" not in s: continue
    style = " ".join(re.findall(r"<style>(.*?)</style>", s, re.S))
    if re.search(r"h1[^{}]*\{[^}]*font-size\s*:", style): ok(...)
    elif "slider-caption" in s: ok(... "由主题 .slider-caption h1 50px 接管 (豁免)")
    else: err("h1-size", "... 含 <h1> 但页内 CSS 未声明 h1 字号 (会掉主题默认巨字号)")
```
要点：**只扫 `{lang}/` 一级 `*.html`**；正则要求 `<style>` **无属性**（写成 `<style type="text/css">` 会被误判为未声明）；h1 规则可以在任意选择器里（`.section-card h1{font-size:...}` 也算）；例外只有首页 `slider-caption`。

配套第 16.5d `key-selector`：用了 `.section-card` 的页面，若出现 `.punchline` / `.case-desc` / `<h2>` / `<h3>`，**每个都必须在页内 `<style>` 里显式声明 `font-size`**，且 `.punchline` / `.case-desc` 必须声明 `color`（暗色覆盖另行写 `body[data-theme="dark"]`）。

### 3.4 特殊/非文章页面清单（三语各有 27 个一级页）

首页 `index.html`；专题/框架页 `human-in-the-loop.html`、`capabilities.html`、`mkt.html`、`invest.html`、`tech.html`、`ai/cloud/web3/automation.html`；艺术簇 `art*.html`（9 个，`art.html` 是唯一暖色例外）；产品页 `fenginvest/fengmedia/fengoffice/flygo/jingxin/search-king.html`；手写理念页 `dog-ate-my-money.html`、`tribute-to-laozi.html`、`ethos.html`。

**内联 `<script>` / `<style>` 完全允许且是常态**：每个手写页都有自己的 `<style>`（含暗色块 + 599px 块 + reduced-motion 块）和若干内联 `<script>`（back-to-top 等）；博客 layout 也是内联样式 + 内联脚本。只有"不引入后端、不引入构建期依赖"是硬约束（`docs/decisions/DECISION-0001-zero-runtime-byok.md`：永久纯静态、0 运行时、BYOK、不做自建后端/独立子域）。

---

## 4. 内容与多语规范

### 4.1 文章 front matter（实样：`hugo/content/zh-cn/blog/posts/two-layer-interface/index.md`）

```yaml
---
title: "两层界面原则：AI 时代的软件交互架构"
date: 2026-09-13
description: "对话层为人机主通道……"     # 必填，≥10 字（门禁 desc）
slug: "two-layer-interface"             # 与目录名一致
translationKey: "two-layer-interface"   # 三语配对键（三语必须同名）
tags: ["技术", "商业"]
draft: false
# lastmod: 2026-01-01                   # 可选，仅修订旧文时填，驱动 dateModified/sitemap
---
```
`hugo/archetypes/default.md` 是 TOML `+++` 版骨架（`draft = true` + 注释字段）。目录约定：`hugo/content/{lang}/blog/posts/<slug>/index.md`。

### 4.2 三语对齐

- **zh-cn 原创 → zh-hk 用 opencc s2hk 转换 → en 全译**（WRITING 规范 §6："三语齐备才上线"）。
- 转换工具：`C:\Projects\fengyuwang_com\tools\zh2hk.py`（`OpenCC("s2hk")` + `王豐羽→王丰羽` 回改）。
- 门禁：check_site 第 2 节按 `translationKey`（缺则目录名）分组，非 draft 必须三语齐；第 3 节用 opencc 双向查简体/繁体泄漏（zh-hk 可转简体 >3 处报错）。
- zh-hk 语体铁律（`docs/guide/voice-and-translation.md`）：**香港书面正体，禁粤语口语**（嘅/唔/係/咗/喺/啲/嘢/乜嘢/佢/哋/嗰/呢/咁…）；港式术语（光模組/伺服器）照用；用「互相」不用「相互」。
- en：正文汉字 >50 即判漏翻（白名单 `王丰羽/王豐羽/静心/jingxin/损不足以奉有余/不足/有余`）；en 页面可见文本出现 2+ 汉字即报错；`zh_ui_strs` 清单（返回博客/上一页/下一页/搜索文章/排序/查看详情/去看看/查看/排序方式/首页）在 en 页面出现即报错。
- **三语页面清单必须严格对等**（第 11 节 `parity`）：新增页必须三语同时存在，文件名完全相同（英文文件名，禁拼音）。

### 4.3 正文写作约束（`docs/guide/WRITING-博文写作规范.md` v6.3）

- **痕迹词禁令**（脚本 `TRACES`，命中即红）：`元宝`、`它说`、`我问它`、`这场对话`、`跟AI聊`、`跟 AI 聊`。
- **直角引号禁令「」**：只约束 `date >= 2026-08-15` 的新文（`NEW_CUTOFF`）；旧文与手写页是用户原稿，明文豁免不回改。概念醒目改用双引号。
- **字数下限**：zh-cn/zh-hk 正文汉字 `<200` 报错。
- **description**：缺失或 <10 字报错。
- **加粗紧邻引号**（`md_bold_quote_hits`）：`**"` 或 `"**汉字` 触发 —— Goldmark 左翼规则导致 `**` 开不上 `<strong>`、星号外露（两层界面篇教训，2026-09-13 新增门禁 `mdbold`）。
- 其它硬规矩：代码围栏必须闭合；正文里裸 `<!DOCTYPE`/`<html` 必须包在 ` ```html ` 围栏内（否则 Hugo 静默丢弃）；禁第二人称（"你/我给你"）、禁自我吹捧；punchline 放 h2（≤12 词）；参考文献格式见 `two-layer-interface` 篇（正文末尾参考文献节 + 原文存档 GitHub 链接）。
- 发布机械检查：`python3 tools/check_site.py --article <index.md>`（三语各跑一次）→ 再 `--no-dark`。

### 4.4 canonical / og:url / seo-url 门禁（第 16.5b 节，1019–1036 行）

```python
SEO_URL_PATS = [
    (r'rel="canonical" href="([^"]*)"', "canonical"),
    (r'property="og:url" content="([^"]*)"', "og:url"),
    (r'hreflang="[^"]*" href="([^"]*)"', "hreflang"),
    (r'"url":\s*"([^"]*)"', "jsonld-url"),
]
# 对 zh-cn/*.html + en/*.html + zh-hk/*.html + index.html 逐个匹配
if u.startswith("http"):
    if not u.startswith("https://www.fengyuwang.com"): err("seo-url", f"{f}: {label} 非 www 统一域: {u}")
    elif ".html" in u: err("seo-url", f"{f}: {label} 带 .html (会 308): {u}")
```
即：**canonical / og:url / hreflang / JSON-LD url 必须是 `https://www.fengyuwang.com/...`，且不得带 `.html`**（相对路径如 `/zh-cn/xxx` 不校验，但 hreflang 里带 `https://` 就会被校验）。实样（`zh-cn/human-in-the-loop.html`）：
```html
<link rel="canonical" href="https://www.fengyuwang.com/zh-cn/human-in-the-loop">
<link rel="alternate" hreflang="en" href="/en/human-in-the-loop">
<link rel="alternate" hreflang="zh-CN" href="/zh-cn/human-in-the-loop">
<link rel="alternate" hreflang="zh-HK" href="/zh-hk/human-in-the-loop">
<link rel="alternate" hreflang="x-default" href="/en/human-in-the-loop">
```
sitemap 的 URL 取自页面 canonical（`tools/gen_sitemap.py` `CANON_RE`），无 canonical 才按路径推导并去掉 `.html`。`gen_sitemap.py` 自动 glob 根 `*.html` + `{lang}/**/*.html`，**新页无需手工登记**；lastmod 取该文件最近一次 git 提交日期。

---

## 5. 资源与限制

### 5.1 图片

- 位置：`C:\Projects\fengyuwang_com\assets\img\`（logo.png / logo-black.png / about.jpg / blog-card.jpg / linkedin-card.jpg / og-card.jpg / slider/slider-1.jpg / shots/*）。
- **大量背景图走外链 Unsplash**：`https://images.unsplash.com/photo-...?w=1000&q=80`，三语页面共 213 处引用（这是既定做法）。
- 尺寸约定（`docs/guide/pitfalls.md` §12）：**卡片图 `w=600`，section 背景图 `w=1000`**。
- OG 图：`https://www.fengyuwang.com/assets/img/og-card.jpg`；不要写 `og:image:width/height`（曾因 logo 30×30 失实被清理）。
- 图片压缩脚本：`C:\Projects\fengyuwang_com\_scripts\compress-images.py`。

### 5.2 JS / CSS 放哪

- **没有 `static/`，Hugo pipeline 完全未启用**。新页的独立 JS/CSS 一律放 `C:\Projects\fengyuwang_com\assets\{js,css}\`，页面用相对路径 `../assets/js/xxx.js` 引用（手写页）或绝对 `/assets/...`（博客）。
- 缓存：`_headers` 对 `*.js` / `*.css` 设 `no-cache, must-revalidate`；`*.svg/png/jpg/webp/woff2` `max-age=86400`；`/*.html` 与 `/blog*` 全部 `no-store`。
- 引用带版本查询串是既有习惯：`shared-subpage-navbar.js?v=26.09.07.04.10`（改 JS 后要 bump 版本号并全站替换）。
- 先例：`assets/js/human-in-the-loop/5dt-pd-viewer.js`（**188 KB 打包版 React 生产 bundle**，`<script type="module">` 引一个 `#root` 挂载点）—— 说明"重量级前端库单文件打包进 assets"是允许的，但注意下面的雷。

### 5.3 CSP / 外部依赖

- **`_headers` 里没有任何 CSP / X-Frame-Options 等安全头**，只有 Cache-Control/Pragma/Expires。
- **并非"无外部 CDN"**：外链实际使用 Google Fonts（27 处）与 images.unsplash.com（213 处）；Cloudflare Web Analytics beacon 在**手写页**保留（博客 baseof 已注释掉，改由 Pages 项目开关注入，避免重复计数）。
- **JS 全部本地**，无外部 JS CDN。
- 页面体积/依赖：无成文硬限制；但 `release-gate.md` 记录对比度审计要真实渲染"466 页"，说明体量敏感度在构建/审计耗时上。

### 5.4 图表/可视化先例（重要）

- **全站手写页 0 个 `<svg>`、0 个 `canvas`**（`grep -lc "<svg" zh-cn/*.html en/*.html zh-hk/*.html` 无输出；`canvas` 只出现在 en/art.html 的文案与 bootstrap.bundle.min.js 内部）。
- 现成的"图形化"实现只有两条：
  1. **纯 CSS 渐变/伪元素**画示意图与光效（`tech.html` 的 `.projects-shell` storm-glow、`art.html` 的 radial-gradient 展厅光）。
  2. **React 打包 bundle**：`assets/js/human-in-the-loop/5dt-pd-viewer.js`（188 KB，内部有 6 处 `svg` 字符串），页面挂 `#root` + `<script type="module">`。
- **没有任何 chord / force / D3 / ECharts 先例**。若新页要做数据可视化，最贴合现状的两条路是"手写内联 SVG（零依赖，需自带暗色 `currentColor`/CSS 变量式配色与 reduced-motion）"或"仿 human-in-the-loop 的 `#root` + 本地打包 JS"。

### 5.5 已发现的现存缺陷（新页别照抄这个坑）

`zh-cn|en|zh-hk/human-in-the-loop.html` 三页都引 `../assets/js/human-in-the-loop/human-in-the-loop-viewer.js`，但该目录下**只有 `5dt-pd-viewer.js`**，被引文件不存在 → 架构图 viewer 实际未加载。门禁查不出：第 8 节死链检查先 `re.sub(r"<script\b[^>]*>.*?</script>", "", html)` **连 `<script src>` 标签一起剥掉**，所以 script 的 `src` 从不做存在性校验。

---

## 6. 已知雷区（新增展示页最可能踩红的地方）

### 6.1 按"必踩概率"排序的门禁红线

1. **`parity`（第 11 节）**：`{lang}/*.html` 三语页面清单必须逐字节一致 → 新增页必须**同时**建 `zh-cn/x.html`、`zh-hk/x.html`、`en/x.html`（文件名完全相同、英文名，禁拼音）。
2. **`navbar`（第 15 节，最硬）**：每个 `{lang}/*.html`（除 `404.html`）必须能从导航栏到达，否则报"不在任何导航入口（桌面菜单/移动 drawer 均未链接其 href）"。做法是改 `C:\Projects\fengyuwang_com\assets\js\shared-subpage-navbar.js`：
   - 三个 `copy` 对象（en 在 `:12`、`'zh-cn'` 在 `:102`、`'zh-hk'` 在 `:192`）各加 `xxx`（文案）+ `xxxHref`（如 `/zh-cn/x.html`）两个 key，**键集必须三语完全一致**（多/少 key 都报）；
   - 桌面模板数组（`container.outerHTML = [` 起，`:461`）与移动抽屉（`:611` 附近）都要真正引用 `labels.xxxHref` —— **只加 key 不加引用仍会判不可达**；
   - `*Href` 三语路径结构必须只差语言前缀；
   - **不许硬编码界面文案**（模板字面量、`aria-label`、`siteLinks` label 里出现可见文字即红；豁免仅 `NAVBAR_TEXT_EXEMPT`：English/简体中文/繁體中文/GitHub/LinkedIn/YouTube/BiliBili）；
   - `NAVBAR_EXEMPT_PAGES` 只有 `404.html`，注释明确"不许私自豁免真实内容页"。
3. **`page-elements`（第 16.5c 节）**：每页必备 10 项，缺一即红：
   `id="shared-subpage-navbar"`、`id="shared-site-footer"`、`id="backToTop"`、`name="description"`、`rel="canonical"`、`property="og:title"`、`property="og:description"`、`property="og:image"`、`name="twitter:card"`、`hreflang="x-default"`。
4. **`h1-size`（16.5）**：页内必须有匹配 h1 且带 `font-size` 的规则（且 `<style>` 不能带属性）。
5. **`key-selector`（16.5d）**：用 `.section-card` 时 h2/h3 必须有 `font-size`；`.punchline`/`.case-desc` 必须有 `font-size` + `color`。
6. **`seo-url`（16.5b）**：canonical/og:url/hreflang/jsonld 的绝对 URL 必须 `https://www.fengyuwang.com` 且不带 `.html`。
7. **`struct`（11.5）**：`{lang}/*.html` 的 `<div>` 与 `</div>` 必须数量相等（历史事故：多写一个 `</div>` 提前关掉 `page-wrap`，白线消失、头图错位）；另外**首页**有额外结构不变量（单张 `slider-single-item` + `hero-static` + `100svh` + `software-cards-section` 位置 + FengInvest/FengMedia/FlyGo 三卡），非首页不受此限。
8. **`link`（第 8 节）**：`{lang}/**/*.html` 的所有 `href`/`src`（含相对路径）必须指向真实存在的文件或目录（目录自动补 `index.html`）；外链/`#`/`data:`/`mailto:` 跳过；`<script>` 内容与标签被整体剥离，`{`/`\` 的模板串跳过。
9. **`dark`（第 13 节）**：新页每个可见文字元素都要有 `body[data-theme="dark"]` 覆盖，且对比度 ≥4.5（大字 ≥3.0）。历史最易翻车的点（pitfalls §11）：漏给 `<h1>`、`.content-text-card h3`、内联 `style="color:..."` 的 span 写暗色。
10. **`hover`（12.5）**：页内 `<style>` 里 `:hover` 若显式声明背景色，与文字色配对的 WCAG 必须 ≥4.5（历史 bug：首页 `.default-btn-one` 暗色 hover 白底白字）。
11. **`btn-height`（16）**：同容器里 `.default-btn` 与 `.default-btn-one` 混排时高度必须相等（`.default-btn-one` 的 `margin-top:5px` 会撑高兄弟按钮 5px）。用 `.cta-row` + `flex:1 1 auto; min-width:160px; max-width:240px`。
12. **`en-han`/`en-ui`（9）**：en 页面可见文本不得出现 2+ 连续汉字；en 博文汉字 >50 判漏翻。
13. **`redirects`（16.6）**：`_redirects` 不得丢 5 条金丝雀、有效规则 ≥29（当前 39 条）。**任何整文件重写都可能踩**（2026-09-11 曾被盲写覆盖 39 行规则）。
14. **`search`（12）**：`{lang}/blog/index.json` ≥90 条 —— 只跟博客相关，但 `--no-dark` 也会跑，动 Hugo 输出后要注意。
15. **`deploy`（5）/`sitemap`（6）**：改了博客必须 `hugo` + `deploy.sh`，否则"源文件未部署"直接红。

### 6.2 git log 里的"被门禁拦过"证据

| commit | 教训 |
|---|---|
| `ab9de9a2` | 新增 `seo-url` 检查，**修掉 81 页漏网 og:url 非 www**；同时给 `h1-size` 加 `slider-caption` 豁免 |
| `a07373ae` | 5dt-pd→human-in-the-loop 改名：h1 显式字号修复 + 门禁新增 `h1-size` 与 `_redirects` 金丝雀 |
| `a1c30273` | 防线入门禁：`page-elements` 必备 10 项 + `key-selector` 字号/颜色，补齐 **27 页** og:description/twitter:card |
| `5545b105` | `key-selector` 扩到 h2/h3 字号声明（全站合规固化） |
| `b1f60380` | 全量门禁全绿前修掉 **4 类低对比度**（archive-date/page-gap 灰、RSS chip 橙、author-home 暗底、TOC/相关/邮件链接蓝） |
| `c4da6174` | 修首页按钮**暗色 hover 白底白字**，随后新增 `hover` 检查节 |
| `3c45dc6f` | 新增第 15/16 节（导航栏完整性、按钮等高），navbar 硬编码文案提取为 copy key |
| `0d7381ea` | 新增 `struct` 节（div 配平 + 首页结构不变量），修暗色 CTA 对比度 |
| `5e440826` / `8affbed6` | 两层界面篇 `**"` 导致 `<strong>` 不渲染、星号外露 → 新增 `mdbold` 门禁 |
| `bccbcd31` / `867f8d98` | zh-hk 简体残留（户→戶、说→説等）+ 粤语字（冇）全站清扫 |
| `d19f8bd4` | `check_site` 取两条工作线并集，避免合并丢检查节 |

### 6.3 落地清单（给新增纯静态展示页的最小动作集）

1. 三语各建 `C:\Projects\fengyuwang_com\{zh-cn,zh-hk,en}\<english-name>.html`，复制 `human-in-the-loop.html` 或 `dog-ate-my-money.html` 的骨架与 `<style>` 块（含暗色 + 599px + reduced-motion 三段）。
2. head 补齐：canonical（www、无 .html）、4 条 hreflang + x-default、og:title/description/image、twitter:card、description、JSON-LD（若加 `"url"` 必须 www 无 .html）。
3. body 挂 `#shared-subpage-navbar[data-section=...]` + `#shared-site-footer` + `#backToTop`，页内 `<style>` 里写 h1（及 h2/h3/.punchline/.case-desc）字号与颜色。
4. 在 `assets/js/shared-subpage-navbar.js` 三语 `copy` 各加 `xxx`/`xxxHref`，并在桌面模板数组与移动 drawer 各加一行 `<li>`（否则 `navbar` 节必红）；改完 bump `?v=` 版本串。
5. zh-hk 用 `python3 tools/zh2hk.py` 生成（或 opencc s2hk），en 全译、正文汉字清零。
6. 独立 JS/CSS 放 `assets/js|css/`，图片放 `assets/img/`（卡图 `w=600`、section 图 `w=1000`），需要图表就手写内联 SVG（无先例，注意暗色与 reduced-motion）。
7. 跑 `python3 tools/check_site.py --no-dark` 到全绿；发版前全量 `python3 tools/check_site.py`（含 Chromium 对比度审计），`sitemap.xml` 由 `deploy.sh` 里的 `tools/gen_sitemap.py` 自动刷新。