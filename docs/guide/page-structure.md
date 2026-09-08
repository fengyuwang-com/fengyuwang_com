# 页面结构与跳转

> 从 `AGENTS.md` 瘦身搬入：Site Architecture、Page Internal Structure、Page List、Cross-Link Strategy 全文。
> 视觉参数唯一源头是 `DESIGN.md`（§6 间距、§7.6 内容块、§7 卡片）；本篇只讲结构与跳转。
> `AGENTS.md` 正文只留压缩不变量（文件名规范、white-divider 直接子元素、cross-link 链）。

## Visitor Journey (Cross-Link Chain)

```
Home (index.html)
  ├── 市场学 (mkt.html)  ── Cross-link ──→ 技术作品 (portfolio.html)
  ├── 投资 (invest.html) ── Cross-link ──→ 博客 (blog)
  └── 技术作品 (portfolio.html) ── Cross-link ──→ 投资框架 (invest.html)
```

## Page Internal Structure

All sub-pages (portfolio, mkt, capabilities, ai, cloud, web3, invest) follow this structure:

```html
<!-- Hero -->
<div class="container">
    <div class="marketing-hero">
        <h1>Page Title</h1>
        <p>Page description / thought anchor</p>
    </div>

    <!-- Card Grid: one card per section below, links via scrollIntoView -->
    <div class="card-grid">
        <div class="mkt-card" onclick="document.getElementById('section-1').scrollIntoView({behavior:'smooth'})">
            <div class="card-content">
                <h3>Card Title</h3>
                <p>Short description</p>
                <button class="card-btn">了解详情</button>
            </div>
        </div>
        <!-- + more cards, one per section -->
    </div>
</div>

<!-- Section 1 -->
<div id="section-1" class="content-block section-bg" style="--section-bg-img:url(...)">
    <div class="block-inner">
        <div class="section-card">
            <h2>Section Title</h2>
            <p class="block-subtitle">Section subtitle (one line)</p>
            <div class="content-text-card">
                <ul>
                    <li><strong>Point label</strong>：Description</li>
                </ul>
            </div>
        </div>
    </div>
</div>

<!-- Section 2, 3, ... (same pattern) -->

<!-- Cross-link at bottom -->
<div class="link-card">
    <p>Guiding text: why the next page matters</p>
    <a class="default-btn" href="/en/next-page.html">Next Page →</a>
</div>
```

Key rules:

- **Card grid is required**: every topic/sub-page needs a card grid at the top (between hero and sections), with one card per section below.
- Card grid uses 2-column layout on desktop, 1-column on mobile.
- Each card's onclick scrolls to its corresponding section by id.
- Cards use Unsplash background images (different from section bg images).

## Page List with Key Characteristics

| Page | Key Sections | Cross-link To | Special Elements |
|------|-------------|--------------|-----------------|
| **index.html** | Hero, Track cards, About, Blog | None (hub) | Homepage track-grid |
| **mkt.html** | Data, Creative, Listen, Global, Projects, Market Capabilities, 5DT-PD Answers | portfolio.html | Cap chip groups, QA groups |
| **portfolio.html** | Delivery, Tech capability, Web/App/Automation/Design | invest.html | mkt-card grid, CTA row |
| **invest.html** | Academic, Business judgment | blog | Frosted glass sections |
| **capabilities.html** | Market understanding, Tech capability, Business judgment, Triangular Loop | None (standalone) | Cap chips, Stack chips, Full skill tree |
| **5dt-pd.html** | Framework viewer (React), Minimal answers | None | React viewer in #root |

## Cross-Link Strategy

Every page (except home and standalone pages) ends with a `link-card` that guides visitors to the next logical page. This creates a deliberate funnel.

### Cross-Link Mapping

| From Page | Guiding Text (en) | Link To |
|-----------|------------------|---------|
| mkt.html | "Beyond data and creativity, engineering delivery capability is also needed" | portfolio.html |
| portfolio.html | "Explore Investment Framework →" | invest.html |
| invest.html | "Read Blog Posts →" | blog |

### Cross-Link Implementation

```html
<!-- Cross-link -->
<div class="link-card">
    <p>Beyond data and creativity, engineering delivery capability is also needed</p>
    <a class="default-btn" href="/en/portfolio.html">See Technical Work →</a>
</div>
```

The `link-card` is always placed **inside** `page-wrap`, after all `content-block` sections, and before closing `page-wrap`.

## 页面文件名规范

**All page filenames must use English words/abbreviations, never Chinese pinyin.**
Examples: `invest.html` (not `touzi.html`), `ethos.html` (not `linian.html`), `dog-ate-my-money.html` (not `gou-na-qian.html`), `tribute-to-laozi.html` (not `zhijing-laozi.html`).
Brand/project names use their established English names: `fenginvest.html`, `jingxin.html`, `search-king.html`.

## 内容块 / Chips / QA 写法

代码写法见 `DESIGN.md`：§7.6 Content Block Patterns、§7.3 卡片（含 `.stack-chip`/`.cap-group`）、§7 QA Groups、§6 Signature white gaps。复制 pattern 时以 DESIGN.md 为准，本篇不重复贴代码。
