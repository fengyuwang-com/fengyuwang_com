# Design

> Personal brand site of Fengyu WANG — market strategy, value investing, software engineering.  
> Three domains, one root logic.  

This document is a complete design specification. Another agent reading it should be able to recreate every page pixel-for-pixel.

---

## 1. Design Principles

**理性 · 客观 · 不坑人.** The site does not sell itself. It states what it is and trusts that to be enough. No second-person ("you can", "我给你"). No self-praise. Let the work speak.

**White space is a feature.** The 12 px gap between `.content-block` sections is deliberate — the white `page-wrap` background naturally flows through these gaps. They are breathing room, not empty space.

**Frosted over solid.** Overlays use `backdrop-filter: blur(20px)` with translucent backgrounds, never opaque `rgba()` fills. Applied to the navbar, section backgrounds, and submenu portal.

**One question per page.** Each page has a thought anchor (思想锚点) — one sentence the entire page answers. The hero sets it up, sections unpack it.

---

## 2. Site Map

```
index.html (language selector — auto-redirect by navigator.language)
  en/ → English pages
  zh-cn/ → Simplified Chinese pages  
  zh-hk/ → Traditional Chinese (Hong Kong) pages
```

Each language folder has identical structure. Only the copy differs.

**Pages per language:**
- `index.html` — Home (hero slider, about, track cards, blog cards)
- `capabilities.html` — Capabilities (triangular loop model)
- `mkt.html` — Marketing strategy cases
- `portfolio.html` — Tech portfolio
- `invest.html` — Investment research
- `5dt-pd.html` — 5DT-PD framework viewer
- `ai.html` — AI engineering
- `cloud.html` — Cloud infrastructure
- `web3.html` — Web3 deep research
- `automation.html` — Automation methodology
- `ethos.html` — Personal philosophy (7 sections: tbc, journey, work, tech-ethics, relations, east-west, unfit)
- `art.html` — Art hub (card grid linking to sub-pages + teaser sections) — EXCEPTION: warm museum palette, see §14
- `art-painting.html` — Painting & empty space
- `art-sculpture.html` — Sculpture & spirit
- `art-architecture.html` — Architecture & garden
- `art-music.html` — Music
- `art-literature.html` — Literature
- `art-design.html` — Design philosophy
- `art-film.html` — Film & narrative
- `blog/` — Hugo-generated blog listing + posts

---

## 3. HTML Template

Every page follows this exact structure:

### Head

```html
<!doctype html>
<html lang="en">   <!-- or zh-CN, zh-HK -->
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="theme-color" content="#0f172a">
    <meta name="format-detection" content="telephone=no">
    <title>Page Title | Fengyu WANG</title>
    <!-- SEO: max 160 chars -->
    <meta name="description" content="...">
    <meta name="keywords" content="Fengyu WANG, ...">
    <meta name="author" content="王丰羽">
    <meta name="robots" content="index,follow">
    <!-- Canonical & hreflang — three languages + x-default -->
    <link rel="canonical" href="/en/page.html">
    <link rel="alternate" hreflang="en" href="/en/page.html">
    <link rel="alternate" hreflang="zh-CN" href="/zh-cn/page.html">
    <link rel="alternate" hreflang="zh-HK" href="/zh-hk/page.html">
    <link rel="alternate" hreflang="x-default" href="/en/page.html">
    <!-- OG -->
    <meta property="og:site_name" content="Fengyu WANG">
    <meta property="og:locale" content="en_US">
    <meta property="og:type" content="website">
    <meta property="og:title" content="...">
    <meta property="og:description" content="...">
    <meta property="og:url" content="https://fengyuwang.com/en/page.html">
    <meta property="og:image" content="/assets/img/logo.png">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">
    <!-- Twitter -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="...">
    <meta name="twitter:description" content="...">
    <meta name="twitter:image" content="/assets/img/logo.png">
    <!-- JSON-LD: Person schema for homepage, WebSite for subpages -->
    <script type="application/ld+json">{...}</script>
    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@400;600;700;800;900&display=swap" rel="stylesheet">
    <link rel="icon" type="image/png" href="../assets/img/logo.png">
    <!-- CSS (order matters) -->
    <link rel="stylesheet" href="../assets/css/bootstrap.min.css">
    <link rel="stylesheet" href="../assets/css/animate.min.css">
    <link rel="stylesheet" href="../assets/css/meanmenu.css">
    <link rel="stylesheet" href="../assets/css/fontawesome.min.css">
    <link rel="stylesheet" href="../assets/css/magnific-popup.min.css">
    <link rel="stylesheet" href="../assets/css/owl.carousel.min.css">
    <link rel="stylesheet" href="../assets/css/style.css">
    <link rel="stylesheet" href="../assets/css/responsive.css">
    <!-- Page-specific styles in <style> block -->
    <style>...</style>
</head>
```

### Body

```html
<body>
    <!-- Navbar — loaded via JS, data-section="page-key" -->
    <div id="shared-subpage-navbar" data-section="home|capabilities|cases|portfolio|investment|blog"></div>
    <script src="../assets/js/shared-subpage-navbar.js?v=26.07.03.14.30"></script>

    <!-- Preloader -->
    <div id="preloader">
        <div id="preloader-status">
            <div class="preloader-position loader"><span></span></div>
        </div>
    </div>

    <!-- Main content -->
    <div class="page-wrap">
        <div class="container">
            <div class="marketing-hero">
                <h1>Page Title</h1>
                <p>Thought anchor / description</p>
            </div>
            <div class="card-grid">
                <!-- One .mkt-card per section, scrollIntoView -->
            </div>
        </div>
        <div class="content-block" id="section-1">
            <div class="block-inner">...</div>
        </div>
        <div class="content-block section-bg" style="--section-bg-img:url(...)">
            <div class="block-inner">
                <div class="section-card">...</div>
            </div>
        </div>
        <!-- ... more content-block sections ... -->
        <div class="link-card">
            <p>Cross-link guiding text</p>
            <a class="default-btn" href="/en/next-page.html">Next →</a>
        </div>
    </div>

    <!-- Footer — loaded via JS -->
    <div id="shared-site-footer"></div>
    <script src="../assets/js/shared-site-footer.js"></script>

    <!-- JS (order matters) -->
    <script src="../assets/js/jquery.min.js"></script>
    <script src="../assets/js/bootstrap.min.js"></script>
    <script src="../assets/js/jquery.meanmenu.js"></script>
    <script src="../assets/js/jquery.appear.min.js"></script>
    <script src="../assets/js/jquery.waypoints.min.js"></script>
    <script src="../assets/js/jquery.counterup.min.js"></script>
    <script src="../assets/js/owl.carousel.min.js"></script>
    <script src="../assets/js/jquery.magnific-popup.min.js"></script>
    <script src="../assets/js/wow.min.js"></script>
    <script src="../assets/js/main.js"></script>

    <!-- Cloudflare Web Analytics -->
    <script defer src="https://static.cloudflareinsights.com/beacon.min.js" data-cf-beacon='{"token": "YOUR_CLOUDFLARE_TOKEN"}'></script>

    <!-- Back to top -->
    <button class="back-to-top" id="backToTop" onclick="window.scrollTo({top:0,behavior:'smooth'})">↑</button>
    <script>(function(){var btn=document.getElementById("backToTop");if(!btn)return;window.addEventListener("scroll",function(){if(window.scrollY>300)btn.classList.add("show");else btn.classList.remove("show")})})();</script>
</body>
```

---

## 4. Typography

**Font:** Nunito Sans, served via Google Fonts. No serif faces anywhere.

**Weights used:**
- 400 — body text, controls, menu items, tab labels
- 600 — block subtitles (`.block-subtitle`), chip text, card buttons
- 700 — only inside content-text-card h3
- 800 — all headings (h1, h2), card titles
- 900 — loaded but not used in UI

**Scale:**

| Level | Size | Weight | Line Height | Color (light) | Color (dark) |
|-------|------|--------|-------------|---------------|--------------|
| Hero h1 | `clamp(30px,4vw,44px)` | 800 | 1.08 | `#0f172a` | `#e5ecf4` |
| Section h2 | `1.6rem` | 800 | — | `#0f172a` | `#e5ecf4` |
| Card h3 (mkt-card) | `1.2rem` | 800 | — | `#fff` | `#fff` |
| Content-text-card h3 | `1.05rem` | 700 | — | `#0f172a` | `#e5ecf4` |
| Block subtitle | `.95rem` | 600 | 1.7 | `#6b7280` | `#94a3b8` |
| Body | `.97rem` | 400 | 1.85 | `#475569` | `#9fb0c3` |
| Small / card-btn | `.78rem` | 600 | — | `#fff` | `#fff` |
| Nav links | `12px` | 400 | — | `#1d1d1f` | `#f5f5f7` |
| Card-grid p | `.82rem` | — | 1.45 | `rgba(255,255,255,.82)` | same |
| Kicker (track-card) | `12px` | 700 | — | `#bfdbfe` | same |
| Stack-chip | `.8rem` | 600 | — | `#1e293b` | `#e5ecf4` |
| Footer copy | ~`.82rem` | 400 | — | muted | muted |

No italics in UI chrome. No bold (700+) outside content cards. Visual emphasis comes from color and stroke, not weight.

---

## 5. Colors

### Palette (cold-tone slate + single blue accent)

| Token | Light | Dark | Role |
|-------|-------|------|------|
| `page-wrap` bg | `#ffffff` | `#0a0e1a` | Full-page background |
| `content-block` bg | `#f5f5f7` | `#111827` | Section background |
| `section-bg` ::after | `rgba(245,245,247,.72)` | `rgba(17,24,39,.88)` | Frosted glass overlay |
| Text primary | `#0f172a` | `#e5ecf4` | Headings, body |
| Text muted | `#475569` / `#6b7280` / `#64748b` | `#9fb0c3` / `#94a3b8` | Description, meta |
| Accent blue | `#0071e3` | `#2997ff` | Links, hover, default-btn |
| Subtle blue | `#2563eb` | `#6b9aff` | Punchline text |
| Navbar | `rgba(255,255,255,0.72)` | `rgba(10,14,26,0.72)` | Frosted bar |
| Button bg | `#0071e3` | `#4f7eff` | `.default-btn` |
| Button hover | `#0062cc` | `#3a6af0` | `.back-to-top` hover |
| Track shell | `linear-gradient(135deg, rgba(15,23,42,0.98), rgba(30,41,59,0.96))` | same (stacked) | Homepage tracks |
| Track card | `rgba(255,255,255,.08)` | `rgba(15,23,42,.82)` | Track grid cards |
| Section card | `rgba(255,255,255,.90)` | `rgba(30,41,59,.90)` | Frosted card |
| Content text card | `#ffffff` | `#0f172a` | Solid card |
| Nav link text | `#1d1d1f` | `#f5f5f7` | Navbar links |
| Nav hover | `#0071e3` | `#2997ff` | Nav link active/hover |

### Color rules
- No warm colors exist in the system (no orange, red, yellow, green in UI).
- No second accent color. Do not introduce one.
- Semantic colors (success/error/warning) are used only for alert status indicators, never for primary UI.

---

## 6. Spacing & Layout

### Signature white gaps
```css
.page-wrap { background: #ffffff; }
.content-block { margin-bottom: 12px; }
.content-block:last-of-type { margin-bottom: 0; }
```
All `.content-block` elements must be direct children of `.page-wrap`. Closing `page-wrap` early breaks the white gap.

### Key measurements

| Element | Value |
|---------|-------|
| `.content-block` padding | `44px 0 40px` |
| `.content-block` (≤991px) | `36px 0 28px` |
| `.content-block` (≤599px) | `28px 0 20px` |
| `.block-inner` max-width | `720px`, margin `0 auto`, padding `0 24px` |
| `.marketing-hero` padding | `52px 0 40px` |
| `.marketing-hero` (≤991px) | `36px 24px` |
| `.marketing-hero` (≤599px) | `28px 16px` |
| Card grid gap | `20px` |
| Card grid bottom padding | `48px` |
| `.section-card` padding | `32px` |
| `.content-text-card` padding | `20px 24px` |
| Text wrapping (global) | `.content-text-card, .block-inner { overflow-wrap: break-word; word-break: break-word }` in `assets/css/style.css` — CJK kinsoku + `/` rules can form unbreakable line-end chunks; without this they overflow the card |
| `.link-card` padding | `48px 0 72px` |
| Nav icon height | `32px` |
| Nav shell max-width | `1200px`, padding `0 20px` |

### Border radius

| Element | Radius |
|---------|--------|
| `.section-card` | `18px` |
| `.content-text-card` | `14px` |
| `.mkt-card` | `18px` |
| `.track-card` | `24px` |
| `.track-split-shell` | `32px` |
| `.default-btn` / `.default-btn-one` | `50px` (pill) |
| `.stack-chip` / `.card-btn` | `999px` (pill) |
| Submenu portal | `14px` |
| Theme toggle | `20px` |
| Menu toggle (hamburger) | `8px` |
| Language-selector card | `28px` |
| `.back-to-top` | `50%` (circle) |

### Shadows

| Element | Box-shadow |
|---------|-----------|
| Homepage language card | `0 30px 80px rgba(15,23,42,0.12)` |
| Language selector links | `0 16px 40px rgba(15,23,42,0.08)`, hover: `0 20px 48px rgba(15,23,42,0.12)` |
| `.section-card` | `0 4px 16px rgba(15,23,42,.06)` |
| `.content-text-card` | `0 2px 8px rgba(15,23,42,.04)` |
| Navbar | `0 1px 0 rgba(0,0,0,0.1)` — just a hairline |
| Mobile panel portal | `0 18px 48px rgba(0,0,0,0.12)` |
| Submenu portal | `0 18px 48px rgba(0,0,0,0.12), 0 0 0 0.5px rgba(255,255,255,0.04)` |
| Back-to-top | `0 8px 24px rgba(0,113,227,.3)` |
| Dark submenu portal | `0 18px 48px rgba(0,0,0,0.4), 0 0 0 0.5px rgba(255,255,255,0.04)` |
| Track card hover | `translateY(-2px)` on anchor hover (homepage) |

---

## 7. Components

### 7.1 Navigation (`shared-subpage-navbar.js`)

A single JS file (`assets/js/shared-subpage-navbar.js`) generates the entire navbar. It injects its own styles, HTML, and behavior.

**Structure:** The script reads `lang` from `<html>` attribute, reads `data-section` from the container element, builds a nav object with three language copies, then replaces the container with full HTML.

**CSS (injected via JS `style` element):**

**Base layout:**
```css
.shared-subpage-nav {
  position: fixed; top: 0; left: 0; right: 0; z-index: 9999;
  background: rgba(255, 255, 255, 0.72);
  backdrop-filter: saturate(180%) blur(20px);
  -webkit-backdrop-filter: saturate(180%) blur(20px);
  box-shadow: 0 1px 0 rgba(0,0,0,0.1);
}
.shared-subpage-nav .nav-shell {
  max-width: 1200px; margin: 0 auto; padding: 0 20px;
  min-height: 44px; display: flex; align-items: center;
  justify-content: space-between; gap: 20px;
}
body { padding-top: 44px !important; }
```

**Desktop menu:**
```css
.shared-subpage-nav .desktop-menu {
  display: flex; align-items: center; gap: 2px; flex-wrap: wrap;
}
.shared-subpage-nav .desktop-menu a {
  display: block; padding: 8px 12px; color: #1d1d1f;
  font-size: 12px; font-weight: 400;
}
.shared-subpage-nav .desktop-menu a:hover,
.shared-subpage-nav .desktop-menu a.active { color: #0071e3; }
.shared-subpage-nav .nav-caret {
  display: inline-block; margin-left: 4px; font-size: 8px;
  transition: transform 0.2s ease;
}
.shared-subpage-nav li:hover > a .nav-caret { transform: rotate(180deg); }
```

**Submenu portal (body-level):**
```css
#submenu-portal {
  position: fixed; z-index: 10000; pointer-events: none;
}
#submenu-portal.active { pointer-events: auto; }
#submenu-portal .sp-wrap {
  margin-top: 8px; min-width: 200px; padding: 6px 0;
  background: rgba(255,255,255,0.72);
  backdrop-filter: saturate(180%) blur(20px);
  border-radius: 14px;
  border: 0.5px solid rgba(255,255,255,0.3);
  box-shadow: 0 18px 48px rgba(0,0,0,0.12), 0 0 0 0.5px rgba(255,255,255,0.04);
  opacity: 0; transform: translateY(-6px);
  transition: opacity 0.2s ease, transform 0.25s cubic-bezier(0.25,0.1,0.25,1);
  max-height: calc(100vh - 80px);   /* fallback; showPortal() overrides inline */
  overflow-y: auto; overscroll-behavior: contain;
  scrollbar-width: thin; scrollbar-color: rgba(0,0,0,0.2) transparent;
}
#submenu-portal .sp-wrap::-webkit-scrollbar { width: 6px; }
#submenu-portal .sp-wrap::-webkit-scrollbar-thumb { background: rgba(0,0,0,0.18); border-radius: 3px; }
#submenu-portal.active .sp-wrap { opacity: 1; transform: translateY(0); }
#submenu-portal .sp-wrap a {
  display: block; padding: 8px 18px;
  border-bottom: 1px solid rgba(0,0,0,0.05);
  color: #1d1d1f; font-size: 12px; font-weight: 400;
}
#submenu-portal .sp-wrap a:hover { color: #0071e3; background: rgba(0,113,227,0.06); }
```

**Theme toggle:**
```css
.shared-subpage-nav .theme-toggle {
  display: inline-flex; align-items: center; gap: 6px;
  min-height: 32px; padding: 6px 12px;
  border: 0; border-radius: 20px;
  background: rgba(0,0,0,0.08); color: #1d1d1f;
  cursor: pointer; font-size: 12px; font-weight: 400;
}
```

**Hamburger (hidden on desktop, shown ≤991px):**
```css
.shared-subpage-nav .menu-toggle {
  display: none; width: 36px; height: 36px;
  border: 0; border-radius: 8px;
  background: rgba(0,0,0,0.08); cursor: pointer;
}
.shared-subpage-nav .menu-toggle span {
  display: block; width: 16px; height: 1.5px;
  background: #0a0e1a; margin: 6px auto;
}
@media (max-width: 991px) {
  .shared-subpage-nav .nav-main { display: none; }
  .shared-subpage-nav .menu-toggle { display: inline-block; }
}
```

**Mobile portal (body-level drawer):**
```css
#mobile-panel-portal {
  position: fixed; top: 44px; left: 0; right: 0; bottom: 0; z-index: 9998;
  overflow-y: auto; -webkit-overflow-scrolling: touch;   /* the drawer is the scroll container */
  background: rgba(255,255,255,0.85);
  backdrop-filter: saturate(180%) blur(20px);
  box-shadow: 0 18px 48px rgba(0,0,0,0.12);
  opacity: 0; pointer-events: none;
  transform: translateY(-10px);
  transition: opacity 0.3s ease, transform 0.3s ease;
}
#mobile-panel-portal.open { opacity: 1; pointer-events: auto; transform: translateY(0); }
#mobile-panel-portal .mobile-menu a {
  display: block; padding: 12px; color: #1d1d1f;
  font-size: 18px; font-weight: 500;
}
```

**Mobile submenu caret (`+/-`):**
```css
.mobile-caret::before { content: "+"; font-size: 22px; font-weight: 300; color: #6e6e73; }
.mobile-item.open > .mobile-link-row .mobile-caret::before { content: "−"; color: #0071e3; }
```

**Desktop menu items (injected order):**
1. Home (▾ submenu: Welcome, About, "Explore the site by track")
2. Capabilities
3. Marketing (▾ submenu: **Marketing Overview**, 5DT-PD Framework)
4. Tech (▾ submenu: **Tech Overview**, 软件项目: Jingxin/FengOffice/FengMedia/Search King, 技术研究: Web3/AI/Automation/Cloud)
5. Investment (▾ submenu: **Investment Overview**, FengInvest — the investment tool belongs here, not under Tech)
6. Art (▾ submenu: **Art Overview**, Painting & Sculpture, Sculpture, Architecture & Garden, Music, Literature, Design, Film & Narrative)
7. Ethos (▾ submenu: **Ethos Overview**, then 7 anchor links — tbc, journey, work, tech-ethics, relations, east-west, unfit)
8. Blog
9. Sites (▾ submenu: GitHub, LinkedIn, YouTube, BiliBili)
10. Language (▾ submenu: English, 简体中文, 繁體中文)

**Submenu auto-fit & scroll (global):** every dropdown follows the same rule — expand to full content height when the screen has room, scroll only when it doesn't. Never cap a dropdown with a fixed pixel height that clips content; the only cap is the available viewport space.

Desktop portal (`showPortal()`):
- On open, sets `max-height` to the space below the trigger: `window.innerHeight - rect.bottom - 16` (min 160px). `.sp-wrap` is `overflow-y: auto` with a thin styled scrollbar. Short menus render fully expanded with no scrollbar; long menus (e.g. the Tech menu, 12 items) scroll only when the window is too short.
- CSS fallback `max-height: calc(100vh - 80px)` applies if the inline value is absent.

Mobile drawer:
- `.mobile-submenu` opens to its **exact content height** (`scrollHeight` set inline by the toggle handler) — smooth animation, nothing clipped. The drawer `#mobile-panel-portal` is the scroll container (`overflow-y: auto`); it scrolls only when the whole menu doesn't fit the screen.

The Tech dropdown is a single column with two `nav-group` headers, and leads with its own overview link — matching the Marketing, Investment and Art submenus:

```
技术概览
软件项目
Jingxin
FengOffice
FengMedia
Search King
技术研究
Web3
AI
Automation
Cloud
```

Rules:
- No two-column grids, no fixed max-height caps — dropdowns auto-fit the viewport and scroll only when needed.
- Every submenu leads with its own **overview link** (`XXX概览` / `XXX Overview`, one per language in `copy`) — never remove it: Marketing/Tech/Investment/Art lead with their page overview, Ethos leads with Ethos Overview followed by the anchor links. This replaces the old "page's own link" pattern so 投资 ▾ no longer shows a bare 投资 item (which looked duplicated).
- Group headers live in the three-language `copy` objects as their own keys (`software`, `techResearch`) — never hard-code a header string.
- The mobile drawer mirrors the same item list and group headers, single-column.
- New items go under the correct group header and must be added to all three language `copy` objects.

**Dark mode navbar:**
```css
body[data-theme="dark"] .shared-subpage-nav {
  background: rgba(10, 14, 26, 0.72);
  box-shadow: 0 1px 0 rgba(255,255,255,0.1);
}
body[data-theme="dark"] .shared-subpage-nav .desktop-menu a { color: #f5f5f7; }
body[data-theme="dark"] .shared-subpage-nav .desktop-menu a:hover { color: #2997ff; }
body[data-theme="dark"] .theme-toggle { background: rgba(255,255,255,0.1); color: #f5f5f7; }
body[data-theme="dark"] .menu-toggle { background: rgba(255,255,255,0.1); }
body[data-theme="dark"] .menu-toggle span { background: #f5f5f7; }
body[data-theme="dark"] #mobile-panel-portal { background: rgba(10, 14, 26, 0.85); }
body[data-theme="dark"] .mobile-caret::before { color: #86868b; }
```

**JS Behavior:**
- Theme is stored in `localStorage.setItem('site-theme', theme)` and applied on load
- Default: respects `prefers-color-scheme` media query
- Desktop submenus: on `mouseenter`, clone the submenu HTML into `#submenu-portal`, position it, set `max-height` to the space below the trigger (auto-fit), fade in. On `mouseleave`, fade out after 100 ms delay. Portal itself has `mouseenter`/`mouseleave` handlers to prevent closing while the cursor travels. Scrolls inside the dropdown only when the window is too short.
- Mobile: click on `.mobile-link-row` toggles `.open` on `.mobile-item`, which reveals `.mobile-submenu` to its exact content height (`scrollHeight`, no fixed cap). Only one submenu open at a time; the drawer scrolls when the whole menu doesn't fit.
- Hamburger click toggles `#mobile-panel-portal.open`.
- On viewport resize ≥992px, mobile panel closes.

### 7.2 Buttons

**`.default-btn`** (primary CTA):
```css
.default-btn {
  display: inline-block; text-align: center;
  color: #ffffff; background-color: #0071e3;
  border: 2px solid #0071e3; border-radius: 50px;
  font-weight: 700; font-size: 15px;
  padding: 12px 35px;
  transition: 0.4s;
}
.default-btn:hover { color: #0071e3; background-color: transparent; }
```

**`.default-btn-one`** (secondary CTA):
```css
.default-btn-one {
  display: inline-block; text-align: center;
  color: #333; background-color: transparent;
  border: 2px solid #333; border-radius: 50px;
  font-weight: 700; font-size: 15px;
  padding: 12px 35px; margin-top: 5px; margin-right: 20px;
  transition: 0.4s;
}
.default-btn-one:hover { color: #fff; background-color: #333; }
```

**Dark mode buttons:** `.default-btn` bg becomes `#4f7eff` on `back-to-top` hover. The `.default-btn`/`.default-btn-one` themselves don't have dark overrides — they inherit from the template.

### 7.3 Cards

**`.card-grid` container:**
```css
.card-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 20px; padding: 0 0 48px;
}
@media (max-width: 991px) { .card-grid { grid-template-columns: repeat(2, 1fr); } }
@media (max-width: 599px) { .card-grid { grid-template-columns: 1fr; } }
```

**`.mkt-card`** (image card for section navigation):
```css
.mkt-card {
  position: relative; border-radius: 18px; overflow: hidden;
  height: 160px; display: flex; flex-direction: column;
  justify-content: flex-end; cursor: pointer;
  border: 1px solid rgba(148,163,184,.14);
  background-size: cover; background-position: center;
}
.mkt-card::after {
  content: ''; position: absolute; inset: 0;
  background: linear-gradient(transparent 30%, rgba(0,0,0,.7));
  pointer-events: none;
}
.mkt-card .card-content {
  position: relative; z-index: 1;
  padding: 22px 20px 20px; color: #fff;
}
.mkt-card .card-content h3 {
  font-size: 1.2rem; font-weight: 800; margin-bottom: 3px;
}
.mkt-card .card-content p {
  font-size: .82rem; color: rgba(255,255,255,.82);
  margin-bottom: 12px; line-height: 1.45;
}
```
> **Font size rule (CRITICAL):** `.mkt-card .card-content h3` is always `1.2rem`, `.mkt-card .card-content p` is always `.82rem`, `.card-btn` is always `.78rem`. These are **frozen values**. Do not increase them — bigger card text breaks the grid's visual rhythm. The art page is the only exception (see §14), and even there the card font sizes are identical to the standard template.

**`.card-btn`** (button inside mkt-card):
```css
.card-btn {
  display: inline-flex; align-items: center; gap: 4px;
  background: rgba(255,255,255,.18);
  border: 1px solid rgba(255,255,255,.25);
  border-radius: 999px; color: #fff;
  font-size: .78rem; font-weight: 600;
  padding: 6px 14px; cursor: pointer;
  font-family: inherit; transition: background .2s;
  pointer-events: none;
}
```

**`.invest-card`** (dark variant of mkt-card):
```css
.invest-card {
  background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
  display: flex; flex-direction: column;
  justify-content: center; align-items: center;
  text-align: center; border: none; cursor: pointer;
}
.invest-card .card-content { color: #f8fafc; }
.invest-card .card-content p { color: rgba(248,250,252,.7); margin-bottom: 14px; }
.invest-card .card-btn {
  background: rgba(255,255,255,.12);
  border-color: rgba(255,255,255,.2);
  pointer-events: none;
}
```

**`.section-card`** (frosted white card inside section-bg):
```css
.section-card {
  background: rgba(255,255,255,.90);
  backdrop-filter: blur(8px); -webkit-backdrop-filter: blur(8px);
  border-radius: 18px; padding: 32px;
  border: 1px solid rgba(148,163,184,.10);
  box-shadow: 0 4px 16px rgba(15,23,42,.06);
}
```

**`.content-text-card`** (solid white sub-card):
```css
.content-text-card {
  background: #fff; border-radius: 14px;
  padding: 20px 24px; margin-bottom: 18px;
  border: 1px solid rgba(148,163,184,.10);
  box-shadow: 0 2px 8px rgba(15,23,42,.04);
  color: #475569; line-height: 1.85; font-size: .97rem;
}
.content-text-card:last-child { margin-bottom: 0; }
.content-text-card h3 { font-size:1.05rem; font-weight:700; margin-bottom:8px; color:#0f172a; }
```

### 7.4 Frosted Glass Container

Used when a section has a background image:
```css
.content-block.section-bg {
  background: var(--section-bg-img) center/cover no-repeat;
  background-color: #1e293b;
}
.content-block.section-bg::after {
  content: ''; position: absolute; inset: 0;
  background: rgba(245,245,247,.72);
  backdrop-filter: saturate(180%) blur(20px);
  -webkit-backdrop-filter: saturate(180%) blur(20px);
  pointer-events: none;
}
.content-block.section-bg .block-inner { position: relative; z-index: 1; }
```

Usage:
```html
<div class="content-block section-bg" style="--section-bg-img:url('https://images.unsplash.com/photo-XXXXX?w=1000&q=80')">
  <div class="block-inner">
    <div class="section-card">
      <h2>Punchline</h2>
      <p class="block-subtitle">Subtitle</p>
      <!-- content -->
    </div>
  </div>
</div>
```

Dark mode:
```css
body[data-theme="dark"] .content-block.section-bg::after {
  background: rgba(17,24,39,.88);
  backdrop-filter: blur(20px);
}
```

### 7.5 Track Cards (Homepage Only)

**Shell:**
```css
.track-split-shell {
  background: linear-gradient(135deg, rgba(15,23,42,0.98) 0%, rgba(30,41,59,0.96) 100%);
  border-radius: 32px; padding: 42px;
  box-shadow: 0 28px 60px rgba(15,23,42,.16);
}
.track-split-head { text-align: center; max-width: 760px; margin: 0 auto 28px; }
.track-split-head h2 { color: #f8fafc; font-size: 2.2rem; font-weight: 800; }
```

**Grid (3 columns → 1 column at 991px):**
```css
.track-grid { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 22px; }
@media (max-width: 991px) { .track-grid { grid-template-columns: 1fr; } }
```

**Card:**
```css
.track-card {
  background: rgba(255,255,255,.08);
  border: 1px solid rgba(255,255,255,.12);
  border-radius: 24px; padding: 26px;
  color: #f8fafc; display: flex; flex-direction: column; gap: 16px;
}
.track-card .track-kicker {
  display: inline-flex; align-self: center;
  padding: 6px 10px; border-radius: 999px;
  background: rgba(96,165,250,.16); color: #bfdbfe;
  font-size: 12px; font-weight: 700; letter-spacing: .04em; text-transform: uppercase;
}
.track-card h3 { font-size: 1.35rem; font-weight: 700; margin: 0; color: #fff; text-align: center; }
.track-card p { color: rgba(226,232,240,.82); line-height: 1.75; margin: 0; text-align: center; }
.track-card ul { margin: 0; padding-left: 18px; color: rgba(226,232,240,.88); line-height: 1.8; }
```

### 7.6 Content Block Patterns

**Basic content block:**
```html
<div class="content-block">
  <div class="block-inner">
    <h2>Punchline title</h2>
    <p class="block-subtitle">Subtitle / intro</p>
    <div class="content-text-card">
      <p>Body text...</p>
    </div>
  </div>
</div>
```

**Frosted section with background image:** (see 7.4)

**Capability chips group:**
```html
<div class="punchline">Group punchline (blue, bold)</div>
<div class="cap-group">
  <div class="cap-group-title">Group Name</div>
  <div class="cap-chips">
    <span class="stack-chip">Skill 1</span>
    <span class="stack-chip">Skill 2</span>
  </div>
</div>
```
```css
.punchline { font-size: 1.15rem; font-weight: 700; color: #2563eb; margin-bottom: 24px; }
.cap-group { margin-bottom: 20px; }
.cap-group-title { font-size: .92rem; font-weight: 700; color: #334155; margin-bottom: 8px; }
.cap-chips { display: flex; flex-wrap: wrap; gap: 8px; }
.stack-chip {
  display: inline-flex; padding: 6px 13px; border-radius: 999px;
  background: rgba(15,23,42,.06); color: #1e293b;
  font-size: .82rem; font-weight: 600;
  border: 1px solid rgba(148,163,184,.14);
}
body[data-theme="dark"] .punchline { color: #6b9aff; }
body[data-theme="dark"] .cap-group-title { color: #cbd5e1; }
body[data-theme="dark"] .stack-chip { background: rgba(148,163,184,.12); color: #e5ecf4; border-color: rgba(148,163,184,.10); }
```

**Cross-link card (end of every sub-page):**
```html
<div class="link-card">
  <p>Guiding text for the next page</p>
  <a class="default-btn" href="/en/next-page.html">Next page →</a>
</div>
```
```css
.link-card { text-align: center; padding: 48px 0 72px; }
.link-card p { color: #6b7280; margin-bottom: 12px; }
.link-card .default-btn { min-width: 200px; }
body[data-theme="dark"] .link-card p { color: #94a3b8; }
```

**CTA row (portfolio page):**
```css
.cta-row { display: flex; flex-wrap: wrap; gap: 14px; justify-content: center; margin-top: 18px; }
.cta-row .default-btn, .cta-row .default-btn-one { min-width: 160px; text-align: center; }
```

### 7.7 Projects Zone (Dark Shell)

**Purpose:** delivered projects get a visually distinct zone so visitors instantly see they are not the same kind of content as the ideology/capability sections. A dark shell wraps the project cards; inside, only light cards.

**When to use:** anywhere delivered work must be visually separated from principles/capabilities (e.g. the Tech page's four software projects). Reuse the `track-split-shell` dark gradient token — do not invent a new dark style.

**Placement:** the shell sits **directly after the card grid, before the ideology sections** (deliverables first, principles after). On the Tech page the order is: card grid → projects shell → ideology (`不问对，不开始` … `交付为开始`) → capability → Web3/AI/Cloud promos → cross-link. Keep the card grid's own ordering aligned with the shell and the nav dropdown: software project cards first, then ideology cards. The shell must be a **direct child of `page-wrap`** (same level as `.content-block`) — never inside `.container` (its max-width/padding would leave white strips on both sides).

**Structure:**
```html
<!-- Projects zone: 软件项目（深色专区，与理念区视觉分层） -->
<div class="projects-shell">
  <div class="projects-head">
    <h2>软件项目</h2>
    <p>交付为开始——每个项目都走完从需求到维护的完整闭环。</p>
  </div>

  <!-- Project 1: 静心 Jingxin -->
  <div id="jingxin" class="project-card">
    <div class="block-inner">
      <div class="section-card">
        <!-- unchanged card content -->
      </div>
    </div>
  </div>
  <!-- + more project-card divs -->
</div>
```

**CSS (page-level style block):**
```css
/* Projects zone (storm shell): 电闪雷鸣炫光蓝 */
.projects-shell {
  margin: 12px 0; padding: 42px 42px 18px;
  position: relative; overflow: hidden;
  /* NO border-radius — square edges embed it in the white page */
  /* storm glow-blue: 3 radial glows + 2 diagonal light beams + blue gradient */
  background:
    radial-gradient(ellipse 70% 70% at 50% -8%, rgba(147,197,253,.55) 0%, transparent 62%),
    radial-gradient(ellipse 45% 40% at 10% 14%, rgba(191,219,254,.40) 0%, transparent 55%),
    radial-gradient(ellipse 40% 45% at 92% 10%, rgba(96,165,250,.38) 0%, transparent 55%),
    linear-gradient(115deg, transparent 38%, rgba(255,255,255,.12) 44%, transparent 52%),
    linear-gradient(115deg, transparent 66%, rgba(255,255,255,.08) 70%, transparent 76%),
    linear-gradient(135deg, #1e3a8a 0%, #2563eb 60%, #1d4ed8 100%);
  box-shadow: 0 14px 44px rgba(37,99,235,.38);
  animation: storm-glow 4.5s ease-in-out infinite;
}
.projects-shell::before {
  content: ''; position: absolute; inset: 0; pointer-events: none;
  background: radial-gradient(ellipse 50% 40% at 22% 6%, rgba(255,255,255,.28) 0%, transparent 60%);
  animation: storm-flash 4.5s ease-in-out infinite; /* lightning double-flash */
}
.projects-shell .projects-head, .projects-shell .project-card { position: relative; z-index: 1; }
@keyframes storm-glow {
  0%, 100% { box-shadow: 0 14px 44px rgba(37,99,235,.38); }
  50% { box-shadow: 0 14px 80px rgba(96,165,250,.70); }
}
@keyframes storm-flash {
  0%, 100% { opacity: .35; } 6% { opacity: 1; } 8% { opacity: .25; }
  10% { opacity: .85; } 12% { opacity: .4; } 40% { opacity: .55; } 70% { opacity: .4; }
}
/* Dark mode: same storm, but clearly a BLUE glowing body — never near-black
   (#0b1530-style dark starts read as a "black square" against #0a0e1a) */
body[data-theme="dark"] .projects-shell {
  background:
    radial-gradient(ellipse 70% 70% at 50% -8%, rgba(96,165,250,.45) 0%, transparent 62%),
    radial-gradient(ellipse 45% 40% at 10% 14%, rgba(147,197,253,.26) 0%, transparent 55%),
    radial-gradient(ellipse 40% 45% at 92% 10%, rgba(59,130,246,.34) 0%, transparent 55%),
    linear-gradient(115deg, transparent 38%, rgba(255,255,255,.08) 44%, transparent 52%),
    linear-gradient(115deg, transparent 66%, rgba(255,255,255,.06) 70%, transparent 76%),
    linear-gradient(135deg, #16295c 0%, #1e3a8a 55%, #2547c8 100%);
  box-shadow: 0 0 46px rgba(37,99,235,.28); /* uniform blue halo — no offset, no black */
  animation: none; /* freeze storm-glow so the halo value is not overridden */
}
body[data-theme="dark"] .projects-shell::before {
  background: radial-gradient(ellipse 50% 40% at 22% 6%, rgba(147,197,253,.22) 0%, transparent 60%);
}
.projects-shell .projects-head { text-align: center; margin-bottom: 28px; }
.projects-shell .projects-head h2 { color: #fff; font-size: 1.55rem; font-weight: 800; margin: 0; }
.projects-shell .projects-head p { color: #94a3b8; font-size: .95rem; margin: 8px 0 0; }
.projects-shell .project-card { padding: 20px 0; }
.projects-shell .project-card + .project-card { margin-top: 12px; } /* dark divider between cards */
body[data-theme="dark"] .projects-shell .section-card {
  background: rgba(30,41,59,.92); border: 1px solid rgba(148,163,184,.12);
}
@media (max-width: 599px) {
  .projects-shell { padding: 28px 20px 10px; }
}
```

Rules:
- **No border-radius on the shell** — square edges embed it in the white `page-wrap` (the homepage `track-split-shell` keeps its 32px radius; that's a homepage card container, a different context).
- Inside the shell only light cards (`section-card` / `content-text-card`) — never nested dark shells or dark cards.
- `.project-card` replaces `content-block section-bg` for each project (drop the frosted `section-bg` class and its `--section-bg-img` style).
- The 12px gap between `.project-card`s shows the shell background — the dark equivalent of the white divider rule.
- The projects-head h2/p are white-on-dark inside the shell (overriding the light-mode h2 color).
- `.section-card` dark-mode inside the shell gains a hairline border so cards stay visible on the dark gradient.

### 7.7.1 Software-Project Storm Glow (`storm-bg`) — ONE-TIME effect (Tech page only)

**This is a bespoke, one-off visual effect.** It lives ONLY on the four software-project sections of `zh-cn/tech.html` (`jingxin`, `fengoffice`, `fengmedia`, `search-king`), which are the storm-glow showcase for the "deliverables first" philosophy.

- **Do NOT spread it to other pages.** A page gets the `storm-bg` class only when someone explicitly asks for this exact treatment. It is not a default site style and must not be copied into new pages or other languages without an explicit request.
- **What it does:** `.content-block.storm-bg::before` overlays an animated blue gradient on top of each section's normal background image (`--section-bg-img`). The overlay is a pseudo-element, so it does **not** remove or replace the section's background image, and it does **not** touch the white 12px divider gaps between sections.
- **Animation:** `storm-flow`, a 6s ease-in-out loop that keeps the blue **always present** and only gently breathes (opacity 0.82 ↔ 1.00, slight hue-rotate/saturate). It is a constant flowing gradient — never a strobe/flash. (Earlier iterations used a flashing `storm-flash` 1.2s keyframe; that was rejected because it looked like a flicker. Do not reintroduce flashing.)
- **CSS location:** inline `<style>` block at the top of `zh-cn/tech.html`. Class `.content-block.storm-bg` + `@keyframes storm-flow`, with `body[data-theme="dark"] .content-block.storm-bg::before` for the dark mode variant.
- **Markup:** the four sections keep `class="content-block section-bg storm-bg"` and keep their own `style="--section-bg-img:url(...)"` (the storm overlay is `::before`, independent of the image).
- If this effect is ever removed or disabled, the sections simply fall back to their normal frosted `section-bg` look — the overlay is purely additive.

### 7.8 Homepage Language Selector (`index.html`)

Root `index.html` at site root. Standalone page, not a sub-page.

```css
:root {
  --bg: linear-gradient(135deg, #f8fafc 0%, #eef2ff 52%, #e0f2fe 100%);
  --card: rgba(255, 255, 255, 0.92);
  --text: #0f172a; --muted: #475569; --accent: #2563eb;
  --border: rgba(15, 23, 42, 0.08);
}
body {
  min-height: 100vh; display: flex; align-items: center; justify-content: center;
  padding: 24px; font-family: "Segoe UI", Arial, sans-serif;
  background: var(--bg); color: var(--text);
}
.card {
  width: min(720px, 100%); background: var(--card);
  border: 1px solid var(--border); border-radius: 28px;
  box-shadow: 0 30px 80px rgba(15, 23, 42, 0.12); padding: 36px;
}
.links { display: grid; grid-template-columns: repeat(3, 1fr); gap: 14px; margin-top: 24px; }
.links a {
  display: flex; flex-direction: column; gap: 8px;
  min-height: 124px; padding: 18px; border-radius: 18px;
  background: #fff; border: 1px solid var(--border); color: var(--text);
  box-shadow: 0 16px 40px rgba(15,23,42,0.08);
  transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
}
.links a:hover { transform: translateY(-2px); box-shadow: 0 20px 48px rgba(15,23,42,0.12); border-color: rgba(37,99,235,0.28); }
@media (max-width: 767px) { .links { grid-template-columns: 1fr; } .links a { min-height: 0; } }
```

Auto-redirect JS:
```javascript
(function () {
  var lang = (navigator.language || '').toLowerCase();
  var target = 'en/index.html';
  if (lang.indexOf('zh-hk') === 0 || lang.indexOf('zh-tw') === 0 || lang.indexOf('zh-hant') === 0) {
    target = 'zh-hk/index.html';
  } else if (lang.indexOf('zh') === 0) {
    target = 'zh-cn/index.html';
  }
  window.location.replace(target);
})();
```

Also has `<meta http-equiv="refresh" content="0; url=zh-cn/index.html">` as fallback.

### 7.9 Homepage Sections (English example)

**Hero Slider:**
- Owl Carousel 2-slide fade
- Full-width background images from `assets/img/slider/slider-1.jpg` and `slider-2.jpg`
- `data-overlay-dark="3"` for dark overlay
- Slide 1: h4 "Identify Real Needs → Create Value → Scale Systems", h1 "Market Strategy · Value Investing · Engineering", two buttons
- Slide 2: h4 "Automation Methodology", h2 "5DT-PD Framework", description p, two buttons

**What's New section:**
- Light grey background (`#f5f5f7`), 40px padding
- Centered heading "What's New" + subtitle "Videos & Updates"
- Single Bilibili link card: icon (40px sq, blue gradient), title, description, arrow

**About section:**
- Two-column layout (text left, image right)
- h2 "Market strategy, investing, and code — one integrated perspective"
- Description paragraph
- Two buttons
- Image: `assets/img/about.jpg`, max-width 55%

**Blog Cards section:**
- Two cards in flex row
- Card 1: Blog — cover image (`assets/img/blog-card.jpg`), category "Blog", h3 "Insights & Thoughts", description
- Card 2: LinkedIn — cover image (`assets/img/linkedin-card.jpg`), category "Social", h3 "Articles & Updates", description

### 7.10 Back to Top Button

```css
.back-to-top {
  position: fixed; bottom: 30px; right: 30px;
  width: 48px; height: 48px; border-radius: 50%;
  background: #0071e3; color: #fff; border: none;
  box-shadow: 0 8px 24px rgba(0,113,227,.3);
  cursor: pointer; font-size: 20px;
  display: none; align-items: center; justify-content: center;
  z-index: 999; transition: opacity .2s;
}
.back-to-top.show { display: flex; }
.back-to-top:hover { background: #0062cc; }
body[data-theme="dark"] .back-to-top { background: #4f7eff; box-shadow: 0 8px 24px rgba(79,126,255,.25); }
body[data-theme="dark"] .back-to-top:hover { background: #3a6af0; }
```

JS (inline at page bottom):
```javascript
(function(){
  var btn=document.getElementById("backToTop");
  if(!btn)return;
  window.addEventListener("scroll",function(){
    if(window.scrollY>300) btn.classList.add("show");
    else btn.classList.remove("show");
  });
})();
```

### 7.11 Preloader

```html
<div id="preloader">
  <div id="preloader-status">
    <div class="preloader-position loader"><span></span></div>
  </div>
</div>
```
Styled by the template's `style.css`. Shows a CSS spinner on page load, hidden when the page is ready (handled by `main.js`).

### 7.12 Blog Posts

There are two blog post templates. Both share the same base structure but differ in whether a table-of-contents sidebar is included.

#### Base Structure (both types)

```html
<div class="blog-back-shell"><a class="blog-back-btn" href="/en/blog/">Back to Blog</a></div>
<article class="blog-article">
    <h1>Post Title</h1>
    <div class="article-meta">
        <span class="article-date">2026-04-22</span>
        <span class="meta-sep">·</span>
        <span style="display:inline-flex;padding:4px 10px;border-radius:999px;background:rgba(0,113,227,.08);color:#0071e3;font-size:.8rem;font-weight:600;">Tag</span>
    </div>
    <div class="article-content">
        <!-- post body -->
    </div>
</article>
```

**`.blog-article` base CSS (inline `<style>` block):**
```css
.blog-article { background:#fff; border-radius:24px; padding:40px; box-shadow:0 8px 30px rgba(15,23,42,.08); }
body[data-theme="dark"] .blog-article { background:#1e293b; }
.blog-article h1 { font-size:2rem; font-weight:800; margin:0 0 16px; color:#111827; line-height:1.3; }
body[data-theme="dark"] .blog-article h1 { color:#e5ecf4; }
.blog-article .article-meta { display:flex; align-items:center; gap:12px; flex-wrap:wrap; margin-bottom:20px; font-size:.88rem; color:#6b7280; }
.blog-article .article-meta .article-date { font-weight:600; }
body[data-theme="dark"] .blog-article .article-meta { color:#9fb0c3; }
.blog-article .article-content { margin-top:8px; }
.blog-article .article-content h2 { font-size:1.4rem; margin-top:1.8em; margin-bottom:.7em; color:#111827; }
.blog-article .article-content p,.blog-article .article-content li { line-height:1.8; color:#374151; }
body[data-theme="dark"] .blog-article .article-content h2 { color:#e5ecf4; }
body[data-theme="dark"] .blog-article .article-content p,body[data-theme="dark"] .blog-article .article-content li { color:#9fb0c3; }
@media (max-width:767px) { .blog-article { padding:24px; } }
```

**`.blog-back-btn` CSS (shared across all blog posts):**
```css
.blog-back-shell { margin-bottom: 48px; }
.blog-back-btn { display: inline-flex; align-items: center; gap: 8px; padding: 10px 22px; border-radius: 999px; background: rgba(0,113,227,.08); color: #0071e3; font-weight: 600; font-size: .9rem; text-decoration: none; transition: background .2s, transform .2s; }
.blog-back-btn:hover { background: rgba(0,113,227,.14); transform: translateX(-3px); }
.blog-back-btn::before { content: "\2190"; }
body[data-theme="dark"] .blog-back-btn { background: rgba(41,151,255,.12); color: #60a5fa; }
body[data-theme="dark"] .blog-back-btn:hover { background: rgba(41,151,255,.2); }
```
The `←` is generated via `::before`. Do **not** include `←` in the button text itself — use plain text like `返回博客` / `Back to Blog`.

**`.back-to-top` CSS (shared across all blog posts):**
```css
.back-to-top { position:fixed; bottom:30px; right:30px; width:48px; height:48px; border-radius:50%; background:#0071e3; color:#fff; border:none; box-shadow:0 8px 24px rgba(0,113,227,.3); cursor:pointer; font-size:20px; display:none; align-items:center; justify-content:center; z-index:999; transition:opacity .2s; }
.back-to-top.show { display:flex; }
.back-to-top:hover { background:#0062cc; }
body[data-theme="dark"] .back-to-top { background:#4f7eff; box-shadow:0 8px 24px rgba(79,126,255,.25); }
body[data-theme="dark"] .back-to-top:hover { background:#3a6af0; }
```

#### Type A: Standard Blog (no TOC)

**Used by:** Most blog posts (PDCA, 第一性原理, 职场生存, etc.)

**Structure:** `blog-back-shell` → `article.blog-article` → `h1` + `.article-meta` + `.article-content`

**CSS required (inline `<style>` block):**
- `.blog-article` + `.article-meta` + `.article-content h2,p,li` (base CSS above)
- `.blog-back-shell` + `.blog-back-btn` (shared above)
- `.back-to-top` (shared above)
- No TOC sidebar, no `.blog-layout` grid

#### Type B: Blog with TOC Sidebar

**Used by:** Long-form articles with many sections (e.g., web3-deep-research)

**Structure:**
```html
<div class="blog-back-shell"><a class="blog-back-btn" href="/en/blog/">Back to Blog</a></div>
<div class="blog-layout">
    <aside class="toc-sidebar" id="tocSidebar">
        <div class="toc-title">Table of Contents</div>
        <ul class="toc-list" id="tocList"></ul>
    </aside>
    <div class="blog-article-wrap">
        <article class="blog-article">
            <h1>Post Title</h1>
            <div class="article-meta">...</div>
            <div class="article-content">...</div>
        </article>
    </div>
</div>

<!-- Mobile TOC drawer -->
<button class="toc-mob-btn" id="tocMobBtn">☰</button>
<div class="toc-overlay" id="tocOverlay"></div>
<div class="toc-drawer" id="tocDrawer">
    <div class="toc-drawer-header">
        <div class="toc-title">Table of Contents</div>
        <button class="toc-close" id="tocClose">✕</button>
    </div>
    <ul class="toc-list" id="tocDrawerList"></ul>
</div>

<!-- Back to top -->
<button class="back-to-top" id="backToTop" onclick="window.scrollTo({top:0,behavior:'smooth'})">&uarr;</button>
```

**Key differences from Type A:**
1. `.blog-article` is wrapped in `.blog-article-wrap` (a child of `.blog-layout`)
2. `.blog-layout` is a CSS Grid at ≥1400px: `grid-template-columns: 250px 1fr` — sidebar on left, article on right
3. `aside.toc-sidebar` — sticky sidebar (desktop only, hidden `<1400px`). White card with border-radius, box-shadow, max-height `calc(100vh - 140px)`, overflow-y auto
4. TOC mobile drawer (shown at `<1400px`): fixed position drawer from left, triggered by floating "☰" button, with overlay
5. TOC list is **auto-generated by JS**: scans `.article-content` for h2/h3/h4, builds nested list with `.toc-h2`/`.toc-h3`/`.toc-h4` classes
6. **Scroll-spy**: IntersectionObserver watching h2/h3/h4 elements (`rootMargin: '-80px 0px -60% 0px'`), adds `.toc-active` class to current heading

**TOC CSS required (inline `<style>` block, in addition to base blog CSS and `.back-to-top`):**
```css
.toc-sidebar { display: none; }
.toc-title { font-size: 11px; font-weight: 800; letter-spacing: .08em; text-transform: uppercase; color: #64748b; padding: 0 18px 10px; border-bottom: 1px solid #e2e8f0; margin-bottom: 6px; }
.toc-list { list-style: none; padding: 0; margin: 0; }
.toc-list a { display: block; padding: 5px 18px; font-size: 12.5px; line-height: 1.45; color: #475569; text-decoration: none; transition: all .15s; border-left: 3px solid transparent; }
.toc-h2 { font-weight: 700; padding-top: 7px; }
.toc-h3 { padding-left: 32px !important; font-size: 11.5px; color: #64748b; }
.toc-h4 { padding-left: 50px !important; font-size: 11px; color: #94a3b8; }
.toc-active { color: #0071e3 !important; background: rgba(0,113,227,.06) !important; border-left-color: #0071e3 !important; }
.blog-layout { display: block; }
@media (min-width: 1400px) {
    .blog-layout { display: grid; grid-template-columns: 250px 1fr; gap: 0 40px; }
    .blog-layout .toc-sidebar { display: block !important; position: sticky; top: 100px; max-height: calc(100vh - 140px); overflow-y: auto; background: #fff; border: 1px solid rgba(148,163,184,.16); border-radius: 16px; padding: 18px 0; }
}
.toc-mob-btn { /* floating button, fixed bottom-right at 100px */ }
.toc-overlay { /* full-screen overlay */ }
.toc-drawer { /* left-side drawer */ }
/* + dark mode variants for all above */
```

**TOC JS (auto-generate from article content + scroll-spy):**
```javascript
(function(){
  var content = document.querySelector('.article-content');
  var headings = content ? content.querySelectorAll('h2,h3,h4') : [];
  var tocList = document.getElementById('tocList');
  var tocDrawerList = document.getElementById('tocDrawerList');
  if (!tocList || !headings.length) return;
  function buildLink(h) {
    var id = h.textContent.trim().toLowerCase().replace(/[^a-z0-9一-鿿]+/g,'-').replace(/^-|-$/g,'');
    h.id = h.id || id;
    var li = document.createElement('li');
    var a = document.createElement('a');
    a.href = '#' + h.id;
    a.textContent = h.textContent;
    a.className = 'toc-' + h.tagName.toLowerCase();
    li.appendChild(a);
    return li;
  }
  var frag = document.createDocumentFragment();
  var fragDrawer = document.createDocumentFragment();
  headings.forEach(function(h) {
    var li = buildLink(h);
    frag.appendChild(li.cloneNode(true));
    fragDrawer.appendChild(li.cloneNode(true));
  });
  tocList.appendChild(frag);
  if (tocDrawerList) tocDrawerList.appendChild(fragDrawer);

  // IntersectionObserver scroll-spy
  var links = tocList.querySelectorAll('a');
  var observer = new IntersectionObserver(function(entries) {
    entries.forEach(function(entry) {
      if (entry.isIntersecting) {
        links.forEach(function(l) { l.classList.remove('toc-active'); });
        var id = entry.target.id;
        var match = tocList.querySelector('a[href="#' + id + '"]');
        if (match) match.classList.add('toc-active');
      }
    });
  }, { rootMargin: '-80px 0px -60% 0px' });
  headings.forEach(function(h) { observer.observe(h); });

  // Smooth scroll on click
  links.forEach(function(a) {
    a.addEventListener('click', function(e) {
      e.preventDefault();
      var target = document.getElementById(this.getAttribute('href').slice(1));
      if (target) target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    });
  });

  // Mobile drawer toggle
  var mobBtn = document.getElementById('tocMobBtn');
  var overlay = document.getElementById('tocOverlay');
  var drawer = document.getElementById('tocDrawer');
  var closeBtn = document.getElementById('tocClose');
  // ... toggle open/close classes
})();
```

**Important:** When creating a Type B (TOC) blog post, the article content **must** use semantic h2/h3/h4 headings for the TOC to generate correctly. The JS scans headings inside `.article-content` only.



---

## 8. Responsive Breakpoints

| Breakpoint | Changes |
|-----------|---------|
| `≤991px` (tablet) | Nav: hamburger appears, desktop menu hidden. Card-grid: 2 columns. Hero h1: 2.4rem. Content-block padding: 36/28px. Section h2: 1.4rem. Track grid: 1 column. |
| `≤767px` | Language selector: 1-column grid |
| `≤599px` (mobile) | Card-grid: 1 column. Hero h1: smaller. Content-block padding: 28/20px. Section h2: 1.25rem. |

**Mobile text-width recovery (all content sub-pages, added 2026-08-06):**
On mobile (`≤599px`) the nested card chain — `.block-inner(0 24px) → .section-card(32px) → .content-text-card(0 24px)` — used to eat 160px of horizontal space, leaving only ~215px of text width on a 375px phone (~8 CJK chars/line). Fixed by shrinking the three paddings **inside the 599px media block only**:

```css
@media (max-width: 599px) {
  .block-inner { padding-left: 12px; padding-right: 12px; }      /* 0 24px -> 0 12px */
  .section-card { padding: 20px; }                               /* 32px    -> 20px  */
  .content-text-card { padding-left: 16px; padding-right: 16px; }/* 0 24px  -> 0 16px */
}
```

This recovers ~64px → ~279px usable width (~14 chars/line). Cards keep their rounded-corner look. Apply this to every content sub-page (tech/mkt/invest/ai/cloud/web3/automation/ethos/art*/5dt-pd/capabilities/feng*). The homepage `track-split-shell` is a different structure and is **not** affected. The batch script `scripts/apply-mobile-fix.js` applies these inline (per-page CSS in both minified and spaced variants).

**CTA buttons equal width (`≤ any width`, added 2026-08-06):** Buttons inside `.cta-row` used to size by their text (so a row of "查看官网 →" and "GitHub" looked uneven). Set them to stretch to the longest and cap:

```css
.cta-row .default-btn, .cta-row .default-btn-one {
  flex: 1 1 auto; min-width: 160px; max-width: 240px; text-align: center;
}
```

Applies only to pages using `.cta-row` (zh-cn feng*/jingxin/search-king/tech + en/tech + zh-hk/tech).

**Reduced motion:**
```css
@media (prefers-reduced-motion:reduce) {
  *,*::before,*::after {
    animation-duration:0.01ms !important;
    animation-iteration-count:1 !important;
    transition-duration:0.01ms !important;
    scroll-behavior:auto !important;
  }
}
```

---

## 9. Dark Mode (Complete Mapping)

Activated by: `body[data-theme="dark"]` set via `localStorage` or `prefers-color-scheme`.

| Selector (Light → Dark) | Light | Dark |
|--------------------------|-------|------|
| `body` / `.page-wrap` bg | defaults from `style.css` | `#0a0e1a !important` |
| `body` text color | defaults | `#f5f5f7` |
| `.content-block` bg | `#f5f5f7` | `#111827` |
| `.content-block.section-bg` bg-color | `#1e293b` | `#0a0e1a` |
| `.content-block.section-bg::after` bg | `rgba(245,245,247,.72)` | `rgba(17,24,39,.88)` |
| `.marketing-hero h1` color | `#0f172a` | `#e5ecf4` |
| `.marketing-hero p` color | `#64748b` | `#9fb0c3` |
| `.block-inner h2` color | `#0f172a` | `#e5ecf4` |
| `.block-subtitle` color | `#6b7280` / `#64748b` | `#94a3b8` |
| `.block-inner p, ul` color | `#475569` | `#9fb0c3` |
| `.section-card` bg | `rgba(255,255,255,.90)` | `rgba(30,41,59,.90)` |
| `.section-card` border | `rgba(148,163,184,.10)` | `rgba(148,163,184,.04)` |
| `.section-card` shadow | `0 4px 16px rgba(15,23,42,.06)` | `0 4px 16px rgba(0,0,0,.2)` |
| `.content-text-card` bg | `#ffffff` | `#0f172a` |
| `.content-text-card` border | `rgba(148,163,184,.10)` | `rgba(148,163,184,.03)` |
| `.content-text-card` color | `#475569` | `#9fb0c3` |
| `.content-text-card h3` color | `#0f172a` | `#e5ecf4` |
| `.mkt-card` border | `rgba(148,163,184,.14)` | `transparent` / `#0a0e1a` |
| `.link-card p` color | `#6b7280` | `#94a3b8` |
| `.punchline` color | `#2563eb` | `#6b9aff` |
| `.cap-group-title` color | `#334155` | `#cbd5e1` |
| `.stack-chip` bg | `rgba(15,23,42,.06)` | `rgba(148,163,184,.12)` |
| `.stack-chip` color | `#1e293b` | `#e5ecf4` |
| `.stack-chip` border | `rgba(148,163,184,.14)` | `rgba(148,163,184,.10)` |
| Navbar bg | `rgba(255,255,255,0.72)` | `rgba(10,14,26,0.72)` |
| Nav link color | `#1d1d1f` | `#f5f5f7` |
| Nav hover | `#0071e3` | `#2997ff` |
| Theme toggle bg | `rgba(0,0,0,0.08)` | `rgba(255,255,255,0.1)` |
| Menu toggle bg | `rgba(0,0,0,0.08)` | `rgba(255,255,255,0.1)` |
| Menu toggle span | `#0a0e1a` | `#f5f5f7` |
| Mobile panel | `rgba(255,255,255,0.85)` | `rgba(10,14,26,0.85)` |
| Mobile caret | `#6e6e73` | `#86868b` |
| Mobile caret open | `#0071e3` | `#2997ff` |
| Submenu portal | `rgba(255,255,255,0.72)` | `rgba(10,14,26,0.72)` |
| Submenu link | `#1d1d1f` | `#f5f5f7` |
| Submenu link hover | `#0071e3` | `#2997ff` |
| Back-to-top bg | `#0071e3` | `#4f7eff` |
| Back-to-top hover | `#0062cc` | `#3a6af0` |
| Back-to-top shadow | `0 8px 24px rgba(0,113,227,.3)` | `0 8px 24px rgba(79,126,255,.25)` |
| Blog cards bg | `#f5f5f7` | `#111827` |
| Card/anchor bg in blog | `#ffffff` | `#1e293b` |
| Blog card h3 | `#1d1d1f` | `#e5ecf4` |
| Blog card p | `#6e6e73` | `#9fb0c3` |
| `.track-split-shell` (dark) | `linear-gradient(135deg, rgba(15,23,42,0.98), rgba(30,41,59,0.96))` | `linear-gradient(135deg, #020617, #111827)` |
| `.track-card` (dark) | `rgba(255,255,255,.08)` border `rgba(255,255,255,.12)` | `rgba(15,23,42,.82)` border `rgba(148,163,184,.16)` |

---

## 10. Index Page (Language Selector)

Root `index.html` (not in any language folder). Contains:
- Three language cards in a 3-column responsive grid
- Auto-redirect based on browser language
- Fallback `<meta http-equiv="refresh">`

---

## 11. File Structure

```
/
├── index.html                ← Language selector (auto-redirect)
├── 404.html                  ← Custom 404
├── robots.txt
├── sitemap.xml
├── llms.txt
├── DESIGN.md                 ← This file
├── AGENTS.md                 ← AI editing handbook
├── assets/
│   ├── css/
│   │   ├── bootstrap.min.css
│   │   ├── animate.min.css
│   │   ├── meanmenu.css
│   │   ├── fontawesome.min.css
│   │   ├── magnific-popup.min.css
│   │   ├── owl.carousel.min.css
│   │   ├── style.css          ← Main template CSS
│   │   └── responsive.css     ← Template responsive
│   ├── js/
│   │   ├── shared-subpage-navbar.js  ← Navigation generator
│   │   ├── shared-site-footer.js     ← Footer generator
│   │   ├── jquery.min.js
│   │   ├── bootstrap.min.js
│   │   ├── jquery.meanmenu.js
│   │   ├── jquery.appear.min.js
│   │   ├── jquery.waypoints.min.js
│   │   ├── jquery.counterup.min.js
│   │   ├── owl.carousel.min.js
│   │   ├── jquery.magnific-popup.min.js
│   │   ├── wow.min.js
│   │   └── main.js
│   ├── img/
│   │   ├── logo.png
│   │   ├── logo-black.png
│   │   ├── about.jpg
│   │   ├── blog-card.jpg
│   │   ├── linkedin-card.jpg
│   │   └── slider/
│   │       ├── slider-1.jpg
│   │       └── slider-2.jpg
├── en/                       ← English pages
│   ├── index.html
│   ├── capabilities.html
│   ├── mkt.html
│   ├── portfolio.html
│   ├── invest.html
│   ├── 5dt-pd.html
│   ├── ai.html
│   ├── cloud.html
│   ├── web3.html
│   └── blog/                 ← Hugo-generated
├── zh-cn/                    ← Simplified Chinese (mirror structure)
├── zh-hk/                    ← Traditional Chinese (mirror structure)
├── hugo/                     ← Hugo blog source
└── _scripts/                 ← Build utilities
```

---

## 12. i18n: Three-Language Parallel

- `en/` (English), `zh-cn/` (Simplified Chinese), `zh-hk/` (Traditional Chinese, Hong Kong)
- All three have **identical file structure and HTML structure**
- Only copy differs between them
- zh-hk uses Hong Kong formal Traditional Chinese with 信达雅 localization
- Section titles and punchlines should preserve meaning, not literal translation
- Each HTML page has `<link rel="alternate" hreflang="en|zh-CN|zh-HK">` for all three plus `x-default`

---

## 13. Do's and Don'ts

- **Do** let the 12 px white gap breathe. It is the site's signature.
- **Don't** nest `.content-block` outside `page-wrap`'s direct-child chain.
- **Do** pick from the five existing card types before inventing a new one.
- **Don't** introduce a second accent color. The palette has one blue.
- **Do** start every section with a punchline `h2` (≤12 words, attitude OK).
- **Don't** use second-person ("you can", "我给你"). The site speaks in objective truths.
- **Do** mirror all three languages structurally. Only the copy differs.
- **Don't** hard-code `#FFF` or `#000`. Use the dark-mode-aware value.
- **Do** write punchlines that make the reader pause and nod.
- **Don't** over-explain. The white space and the words do the same job.
- **Do** add every new page to the navbar's three language copies in `shared-subpage-navbar.js`.
- **Don't** use magic numbers in CSS. If the spacing scale lacks a step, revisit the design.
- **Do** keep card font sizes at the frozen values: h3=`1.2rem`, p=`.82rem`, card-btn=`.78rem`. Never increase them.
- **Don't** deviate from the standard color palette (cold-tone slate + single blue accent) except on the art page (see §14).
- **Do** keep all non-art pages on the standard template. The art page is the ONLY exception.

---

## 14. Art Page Exception

**The art page (`art.html`) is the only page that does not follow the standard template.** It has its own visual system to create a museum/gallery atmosphere. All other pages (`capabilities`, `mkt`, `portfolio`, `invest`, `ai`, `cloud`, `web3`, `ethos`, and all art sub-pages like `art-painting.html`) follow the common template described in the sections above — cold-tone slate palette, `#f5f5f7` content blocks, `#ffffff` page-wrap.

### What makes art.html different

| Property | Standard Template | Art Page |
|----------|-----------------|----------|
| `page-wrap` background | `#ffffff` | Radial gradients over `#d0c2ad` (warm beige) — three ellipses at desktop, two at tablet, one at mobile, fading from white at center to transparent at edge |
| `page-wrap::before` | Hidden or absent | `display: none` — intentionally suppressed |
| `content-block` bg | `#f5f5f7` | `#ede8df` (warm cream) |
| `section-bg` default | `#1e293b` (dark slate) | `#d9d2c5` (warm tan) |
| `section-bg ::after` | `rgba(245,245,247,.72)` | `rgba(247,243,237,.78)` (warm frosted) |
| Dark `section-bg ::after` | `rgba(17,24,39,.88)` | Same (shared) |
| Text primary | `#0f172a` | `#1d1d1f` |
| Text muted | `#475569` / `#64748b` | `#515154` / `#8e8e93` |
| `section-card` border | `rgba(148,163,184,.10)` | `rgba(0,0,0,.04)` |
| `section-card` shadow | `0 4px 16px rgba(15,23,42,.06)` | `0 4px 16px rgba(0,0,0,.04)` |
| `content-text-card` bg | `#ffffff` (solid) | `rgba(255,255,255,.85)` (subtle translucent) |
| `content-text-card` shadow | `0 2px 8px rgba(15,23,42,.04)` | `0 2px 8px rgba(0,0,0,.03)` |
| `.mkt-card` | `border: 1px solid rgba(148,163,184,.14)` | No border — relies on box-shadow only |
| Card grid responsive | `repeat(3, 1fr)` → `repeat(2, 1fr)` → `1fr` | `repeat(3, minmax(0, 1fr))` → `repeat(2, minmax(0, 1fr))` → `1fr` (minmax clause) |
| Dark card shadows (global) | `body[data-theme="dark"] .mkt-card` / `.section-card` → **`box-shadow: none`** (2026-08-05: black shadows rendered as "black square frames" around every card in dark mode; cards separate via grid gap + border instead) |
| Hero text colors | `#0f172a` / `#64748b` | `#1d1d1f` / `#8e8e93` |

### How the art page backgrounds work

The art page creates a museum-like lighting effect through CSS radial gradients on `.page-wrap`:

```css
.page-wrap {
  background:
    radial-gradient(ellipse 500px 900px at 17% -20px, rgba(255,255,255,1) 0%, rgba(255,252,248,0.6) 30%, transparent 55%),
    radial-gradient(ellipse 500px 900px at 50% -20px, rgba(255,255,255,1) 0%, rgba(255,252,248,0.6) 30%, transparent 55%),
    radial-gradient(ellipse 500px 900px at 83% -20px, rgba(255,255,255,1) 0%, rgba(255,252,248,0.6) 30%, transparent 55%),
    #d0c2ad;
}
```

Three ellipse gradients are positioned at 17%, 50%, and 83% width — simulating gallery spotlights from above. On tablet (≤991px), two gradients at 25% and 75%. On mobile (≤599px), one centered gradient. The base color `#d0c2ad` is a warm museum-beige that shows through the gaps between `.content-block` sections.

Section backgrounds (`section-bg`) use the standard frosted-glass pattern (CSS `backdrop-filter: blur(20px)` with translucent overlay) but with warm-toned overlay `rgba(247,243,237,.78)` instead of the standard `rgba(245,245,247,.72)`.

Card grid images (`mkt-card`) use `background-image: url(...)` with inline `style=` attributes, the same pattern as the standard template. Each card has a gradient overlay (`::after`) with `background: linear-gradient(transparent 30%, rgba(0,0,0,.7))`.

Dark mode switches to a dark art-gallery feel: the radial gradients use `rgba(210,210,220,0.25)` highlights over `#0a0e1a` base — subtle cool-white spotlights instead of warm.

### Card grid on art page

The `.mkt-card` elements on `art.html` are `<a>` tags (not `<div>`) so the entire card is clickable. This is the only page where `mkt-card` serves as a navigation hub rather than a section preview. Each card links to an art sub-page (painting, sculpture, architecture, etc.).

### What stays the SAME as the template

Despite the different visual system, these values are preserved on the art page:
- `.mkt-card` dimensions: `height: 160px`, `border-radius: 18px`
- Card font sizes: h3=`1.2rem`, p=`.82rem`, `.card-btn`=`.78rem`, font-weight=`800`
- `.block-inner` max-width: `720px`
- `.content-block` padding/margin: `44px 0 40px`, `margin-bottom: 12px`
- Responsive breakpoints: same at 991px and 599px
- `.back-to-top`, navbar, footer: identical
- Link-card structure and spacing: identical

### Important: this exception is exclusive

**No other page** should use warm colors, radial gradient backgrounds, or deviate from the standard cold-tone slate palette. The art page has this exception because its content is about art, aesthetics, and museum culture — the warm palette is itself a design statement that reinforces the content. Every other page (including art sub-pages like `art-painting.html`) must follow the standard template exactly.

---

*Design source of truth. When `AGENTS.md` conflicts with this file, this file wins.*
