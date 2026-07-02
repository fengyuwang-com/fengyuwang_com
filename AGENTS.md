# Fengyu WANG — AI Editing Guide

This document captures everything an AI agent needs to know to edit this website correctly.
Read it thoroughly before making any changes. **It preserves context across sessions.**

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Structure](#structure)
3. [Style & Voice](#style--voice)
4. [Design Philosophy](#design-philosophy)
5. [Site Architecture & Page Flow](#site-architecture--page-flow)
6. [Visual Design System](#visual-design-system)
7. [页面设计模式：Sections 之间的白色横线](#页面设计模式sections-之间的白色横线)
8. [Content Block Patterns](#content-block-patterns)
9. [Capability Chips Pattern](#capability-chips-pattern)
10. [QA Group Pattern (5DT-PD)](#qa-group-pattern-5dt-pd)
11. [Cross-Link Strategy](#cross-link-strategy)
12. [Dark Mode](#dark-mode)
13. [Responsive Design](#responsive-design)
14. [Translation](#translation)
15. [Git & Versioning](#git--versioning)
16. [Privacy](#privacy)
17. [Safety Rules](#safety-rules)
18. [Docker Preview](#docker-preview)
19. [Common Mistakes & Fixes](#common-mistakes--fixes)

---

## Project Overview

三语个人网站 (zh-cn / en / zh-hk) + Hugo 博客。
核心差异：**一个人用一套统一的底层逻辑，贯穿市场、投资、工程三个领域。**

### 底层链条

```
赚钱 → 创造价值 → 解决问题 → 识别真需求 → 实践反馈 → 快速迭代 → 验证模型 → 系统复制 → 杠杆
```

### 三条线，一个根

| 领域 | 表面理解 | 真实理解 |
|------|---------|---------|
| **市场学** | 推广/带货 | 数据洞察真需求 + 创意表达价值 = 双向联系 |
| **投资** | 炒股价/猜涨跌 | 理解企业价值 + 安全边际 + 长期复利 |
| **技术** | 写代码/搞技术 | 定义真问题 → 结构设计 → 工程交付 |

---

## Structure

- `assets/` = shared CSS/JS/images — **DO NOT DELETE**
- `hugo/content/{lang}/blog/posts/` = article source (Markdown)
- `hugo/deploy.ps1` = build + copy
- `en/`, `zh-cn/`, `zh-hk/` = site pages (one HTML file per page per language)

---

## Style & Voice

- **Relaxed sincerity.** Short sentences. Real details.
- **NO second-person** (never use "我给你", "you can", etc.).
- **NO self-praise.** Let the work speak. Use objective framing.
  - BAD: "你的能力是互相增强的" → sounds like bragging
  - GOOD: "当不同的能力相互增强的时候，这就是真正的稀缺" → objective truth
- Be direct. Avoid marketing fluff. Sound like a real person.

---

## Design Philosophy

### Core Principles

1. **White space is a feature.** The 12px gaps between sections are deliberate — the white background "naturally flows out" from `page-wrap`.
2. **Each page answers one question.** The 思想锚点 (thought anchor) is the punchline that sets up everything below it.
3. **Frosted glass, not solid overlays.** Background images use `backdrop-filter: blur(20px)`, not opaque `rgba()` overlays.
4. **Content hierarchy matters.** Every page follows: 思想锚点 → Sections (标题 → 介绍语 → 内容卡片).
5. **Cross-link chain.** Pages are connected in a deliberate visitor journey: mkt → portfolio → invest → blog.
6. **Three domains, one logic.** Market, investment, and tech are not parallel skills — they reinforce each other.

### 思想锚点 (每页一句)

| 页面 | 思想锚点 | 整页回答的问题 |
|------|---------|--------------|
| 首页 | `理性 · 客观 · 不坑人` | "这人信什么？" |
| 市场学（mkt） | 没有显式锚点，用标题 `市场学` | "市场学是什么？" |
| 投资（invest） | `买公司，不是买彩票` | "投资到底是什么？" |
| 技术（portfolio） | `交付为开始` | "技术是为了什么？" |
| 能力结构（capabilities） | `三条线，一个根` | "你的能力怎么组合的？" |

### Triangular Loop (三角闭环)

Capabilities 页的核心概念：
- **市场理解力**：让人想买，而不是让人烦
- **技术实现力**：想得到，做得出
- **商业判断力**：知道什么值得做

这三个能力不是并列的——它们是互相喂的。市场发现机会，技术实现产品，商业判断方向，来回验证。
**当不同的能力相互增强的时候，这就是真正的稀缺。**

---

## Site Architecture & Page Flow

### Visitor Journey (Cross-Link Chain)

```
Home (index.html)
  ├── 市场学 (mkt.html)  ── Cross-link ──→ 技术作品 (portfolio.html)
  ├── 投资 (invest.html) ── Cross-link ──→ 博客 (blog)
  └── 技术作品 (portfolio.html) ── Cross-link ──→ 投资框架 (invest.html)
```

### Page Internal Structure

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

### Page List with Key Characteristics

| Page | Key Sections | Cross-link To | Special Elements |
|------|-------------|--------------|-----------------|
| **index.html** | Hero, Track cards, About, Blog | None (hub) | Homepage track-grid |
| **mkt.html** | Data, Creative, Listen, Global, Projects, Market Capabilities, 5DT-PD Answers | portfolio.html | Cap chip groups, QA groups |
| **portfolio.html** | Delivery, Tech capability, Web/App/Automation/Design | invest.html | mkt-card grid, CTA row |
| **invest.html** | Academic, Business judgment | blog | Frosted glass sections |
| **capabilities.html** | Market understanding, Tech capability, Business judgment, Triangular Loop | None (standalone) | Cap chips, Stack chips, Full skill tree |
| **5dt-pd.html** | Framework viewer (React), Minimal answers | None | React viewer in #root |

---

## Visual Design System

### Key CSS Classes

| Class | Purpose | Key Styles |
|-------|---------|-----------|
| `.page-wrap` | White background container | `background: #ffffff` |
| `.content-block` | Basic section | `padding: 44px 0 40px; margin-bottom: 12px; background: #f5f5f7` |
| `.content-block.section-bg` | Frosted glass section | `background: var(--section-bg-img)` + `::after` pseudo |
| `.block-inner` | Centered content wrapper | `max-width: 720px; margin: 0 auto` |
| `.section-card` | White card inside frosted sections | `background: rgba(255,255,255,.90); border-radius: 18px; padding: 32px` |
| `.content-text-card` | Solid white sub-card | `background: #fff; border-radius: 14px; padding: 20px 24px` |
| `.link-card` | Cross-link container | `text-align: center; padding: 48px 0 72px` |
| `.default-btn` | Blue CTA button | Blue background, white text, border-radius |
| `.stack-chip` | Pill badge | `border-radius: 999px; padding: 6px 13px; font-weight: 600` |
| `.punchline` | Section subtitle emphasis | Blue color `#2563eb`, bold |
| `.mkt-card` | Image card in grid | `border-radius: 18px; height: 160px` |
| `.invest-card` | Dark card variant | `background: linear-gradient(135deg, #0f172a, #1e293b)` |

---

## 页面设计模式：Sections 之间的白色横线

**这是贯穿全站的核心设计原则。** 每个 `.content-block` 之间必须有白色横线分隔。

### 实现原理

```
page-wrap { background: #ffffff }         ← 白色背景从间隙中"自然流出来"
.content-block { margin-bottom: 12px }    ← 每个 section 底部留出 12px 间隙
.content-block:last-of-type { margin-bottom: 0 }
```

### 结构要求

所有 `.content-block` 必须是 `page-wrap` 的**直接子元素**：

```html
<div class="page-wrap">                           ← 白色背景
    <div class="container"> ... </div>             ← hero + 卡片网格

    <div class="content-block section-bg"> ... </div>   ← section 1
    <!-- ↑ 12px 白色横线 ↑ -->
    <div class="content-block section-bg"> ... </div>   ← section 2
    <!-- ↑ 12px 白色横线 ↑ -->
    <div class="content-block section-bg"> ... </div>   ← section 3

    <div class="link-card"> ... </div>
</div>
```

### ⚠️ 常见错误

- **不要多加 `</div>`** — 一个多余的 `</div>` 会提前关闭 `page-wrap`，导致后续内容脱离白色背景，白色横线消失。
- **所有 content-block 必须是 page-wrap 的直接子元素** — 不能被额外嵌套在其他容器内。
- **深色模式**：`body[data-theme="dark"] .page-wrap { background: #0a0e1a; }` 同样需要 `background-color` 覆盖。
- **插入新 section 时**：确保原来的 `:last-of-type` 自动获得 `margin-bottom: 12px`（不再是最后一个）。

---

## Content Block Patterns

### 1. Basic Content Block

```html
<div class="content-block">
    <div class="block-inner">
        <div class="section-card">
            <h2>Title</h2>
            <p class="block-subtitle">Subtitle / intro</p>
            <div class="content-text-card">
                <p>Content text...</p>
            </div>
        </div>
    </div>
</div>
```

### 2. Frosted Glass Section (with background image)

```html
<div class="content-block section-bg" style="--section-bg-img:url('https://images.unsplash.com/...?w=1000&q=80')">
    <div class="block-inner">
        <div class="section-card">
            <h2>Title</h2>
            <!-- content -->
        </div>
    </div>
</div>
```

The `::after` pseudo-element provides:
- `backdrop-filter: saturate(180%) blur(20px)`
- `background: rgba(245,245,247,.72)` (light mode)
- `background: rgba(17,24,39,.88)` (dark mode)

### 3. Section with Pillar Grid

```html
<div class="pillar-grid">
    <div class="pillar-card">
        <h3>Pillar Title</h3>
        <p>Description...</p>
    </div>
    <div class="pillar-card">
        <h3>Pillar Title</h3>
        <p>Description...</p>
    </div>
</div>
```

### 4. Section with Case Grid

```html
<div class="case-grid">
    <div class="case-card">
        <h3>Case Title</h3>
        <p>Description...</p>
    </div>
</div>
```

---

## Capability Chips Pattern

Used on capabilities.html and mkt.html to show skill tags.

```html
<div class="punchline">Section punchline (blue, bold)</div>

<div class="cap-group">
    <div class="cap-group-title">Group Name</div>
    <div class="cap-chips">
        <span class="stack-chip">Skill 1</span>
        <span class="stack-chip">Skill 2</span>
        <span class="stack-chip">Skill 3</span>
    </div>
</div>
```

---

## QA Group Pattern (5DT-PD)

Used in the 5DT-PD Minimal Answers section (mkt.html and 5dt-pd.html).

```html
<div class="qa-group">
    <div class="qa-group-title">Q1: Question text?</div>
    <p>Answer text...</p>
</div>
```

CSS:
```css
.qa-group { margin-bottom: 22px; }
.qa-group:last-child { margin-bottom: 0; }
.qa-group-title { font-size: 1.05rem; font-weight: 700; color: #0f172a; margin-bottom: 10px; }
body[data-theme="dark"] .qa-group-title { color: #e5ecf4; }
```

---

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

---

## Dark Mode

All components require `body[data-theme="dark"]` variants.

| Component | Light | Dark |
|-----------|-------|------|
| `page-wrap` | `#ffffff` | `#0a0e1a` |
| `content-block` | `#f5f5f7` | `#111827` |
| `section-card` | `rgba(255,255,255,.90)` | `rgba(30,41,59,.90)` |
| `content-text-card` | `#fff` | `#0f172a` |
| `h2` / headings | `#0f172a` | `#e5ecf4` |
| Body text | `#475569` | `#9fb0c3` |
| `.punchline` | `#2563eb` | `#6b9aff` |
| `.cap-group-title` | `#334155` | `#cbd5e1` |
| `.stack-chip` | `rgba(15,23,42,.06)` bg | `rgba(148,163,184,.12)` bg |
| `.qa-group-title` | `#0f172a` | `#e5ecf4` |
| Pillar cards | Gradient blue | Darker gradient blue |
| `default-btn` | `#0071e3` | `#4f7eff` |

---

## Responsive Design

```css
/* Tablet (max 991px) */
@media (max-width: 991px) {
    .card-grid { grid-template-columns: repeat(2, 1fr); }
    .marketing-hero h1 { font-size: 2.4rem; }
    .content-block { padding: 36px 0 28px; }
    .block-inner h2 { font-size: 1.4rem; }
    .pillar-grid, .case-grid, .content-text-grid { grid-template-columns: 1fr; }
}

/* Mobile (max 599px) */
@media (max-width: 599px) {
    .card-grid { grid-template-columns: 1fr; }
    .content-block { padding: 28px 0 20px; }
    .block-inner h2 { font-size: 1.25rem; }
}
```

---

## Translation

- **zh-hk** = Hong Kong formal Traditional Chinese. 信达雅. Localize jokes.
- Use `translationKey` to pair articles across languages.
- Keep structure identical across all three languages.
- Section titles: translate meaning, not literally.
- Punchlines: may need adaptation, not direct translation.
- **zh-hk uses 互相** (not 相互). Example: "當不同的能力互相增強的時候".

### Punchline Writing Style

Punchlines are **not** section introductions — they are one-line statements that sound cool, sharp, or undeniable.
Think "Just Do It" or "Think Different." They should make the reader pause and nod.

**Rules:**
- Keep it under 12 words where possible.
- No explanations, no context — the section body does that.
- Be specific, not generic. "算力像水电一样" beats "云服务的核心优势".
- A little attitude is OK. Self-deprecation or brutal honesty works better than marketing fluff.

**Examples (good):**
- 有些门，本地推不开
- 试过了，所以知道
- 去中心化的梦，中心化的服务器

**Examples (bad):**
- 本章节将介绍云服务的核心能力
- 本节讨论本地部署的局限性


---

## Git & Versioning

### Version Format

`yy.MM.dd.HH.mm` — auto-updated by `scripts/update-version.ps1`.
Run this script **before every commit**.

### Git Strategy

| Branch | Purpose | Deploys |
|--------|---------|---------|
| `main` | Production | ✅ Cloudflare Pages |
| `dev` | Daily work | ❌ Never deploys |

### Commit Flow

1. Run `scripts/update-version.ps1`
2. `git add -A`
3. `git commit -m "descriptive message"`
4. Get user approval before push
5. `git checkout master && git merge dev && git push origin master`
6. `git checkout dev`

---

## Privacy

- Prefix title with `*` + `draft: true` for personal info.
- Never commit `.env` or any file with API keys, tokens, or passwords.

---

## Safety Rules

- **NEVER** git push without explicit user approval.
- **NEVER** push to `main` without explicit user approval.
- **NEVER** commit to `main` directly. Always use `dev`.
- **NEVER** delete files from `assets/` without confirmation.

---

## Docker Preview

```powershell
docker compose up -d    # Start preview at test.fengyuwang.com
docker compose down     # Stop
```

The tunnel uses a token from Cloudflare Zero Trust → Tunnels. Put it in `.env`.

---

## Common Mistakes & Fixes

### 1. Extra `</div>` closing `page-wrap` early

**Symptom**: White dividers disappear after a certain point. Content below has no white background.

**Root cause**: An extra `</div>` was added, closing `page-wrap` before all sections.

**Fix**: Count `<div` vs `</div>` in the body section. They must balance. Remove the extra `</div>`.

### 2. Cross-link pointing to wrong page

**Symptom**: Visitor flow is broken — clicking the bottom link goes to an unexpected page.

**Fix**: Check the Cross-Link Mapping table above. The mkt page should always link to portfolio (technical).

### 3. 5DT-PD section without white divider

**Symptom**: The 5DT-PD Answers section on mkt.html has no 12px gap above it.

**Fix**: Ensure the previous section (`:last-of-type` before insertion) is no longer `:last-of-type` after insertion — `margin-bottom: 12px` applies automatically.

### 4. Self-praise wording

**Symptom**: Text uses "你的" (your/yours) to describe capabilities positively.

**Fix**: Rewrite as objective statements. Instead of "你的能力是互相增强的", use "当不同的能力相互增强的时候".

### 5. "一个打三个" vs "超越三者之和的价值"

The capabilities page used to say "一个打三个" (one beats three). The correct framing is "超越三者之和的价值" (value that exceeds the sum of its three parts) — it's about synergy, not competition.

