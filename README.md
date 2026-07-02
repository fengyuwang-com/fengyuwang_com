# Fengyu WANG — Personal Website & Blog

三语个人网站 + Hugo 博客。一个 git 仓库，跨机器、跨系统。

## Core Philosophy

**三个领域 · 一套底层逻辑 · 干净赚钱 · 长期主义**

> 大多数人的能力是平行的。当不同的能力相互增强的时候，这就是真正的稀缺。

### 底层链条（从《第一性原理》提取）

```
赚钱 → 创造价值 → 解决问题 → 识别真需求 → 实践反馈 → 快速迭代 → 验证模型 → 系统复制 → 杠杆
```

### 三条线，一个根

| 领域 | 表面理解 | 真实理解 |
|------|---------|---------|
| **市场学** | 推广/带货 | 数据洞察真需求 + 创意表达价值 = 双向联系 |
| **投资** | 炒股价/猜涨跌 | 理解企业价值 + 安全边际 + 长期复利 |
| **技术** | 写代码/搞技术 | 定义真问题 → 结构设计 → 工程交付 |

三项的共同底层：**都不是表面那层。** 每一项都往回追溯到"识别真需求"和"建立可复用的系统"。

### 核心思想锚点（每页一句）

| 页面 | 思想锚点 | 说明 |
|------|---------|------|
| 首页 | `理性 · 客观 · 不坑人` | 底色：不是口号，是每篇文章都在验证的东西 |
| 市场学 | `科学与艺术之间` | 市场学不是单向输出，是双向联系 |
| 投资 | `买公司，不是买彩票` | 和"炒股"做切割，买的是企业的长期发展 |
| 技术 | `交付为开始` | 代码只是中间产物，交付才是起点 |
| 能力结构 | `三条线，一个根` | 三个方向的能力从同一底层逻辑延伸出来 |

---

## Quick Start

```bash
# 1. Install Hugo
# Windows: winget install Hugo.Hugo.Extended
# macOS:   brew install hugo
# Linux:   snap install hugo

# 2. Build blog
cd hugo
hugo --cleanDestinationDir

# 3. Copy blog files to site
.\deploy.ps1  # or bash deploy.sh

# 4. Start local server
cd ..
python -m http.server 8001
```

---

## Project Structure

```
/
├── *.html                 ← Root-level pages (index, redirects)
├── assets/                ← CSS / JS / images / i18n (shared, NEVER delete)
│   └── js/
│       ├── shared-subpage-navbar.js    ← Universal navbar
│       ├── shared-site-footer.js       ← Universal footer
│       └── 5dt-pd/                     ← 5DT-PD framework viewer (React)
├── en/                    ← English site pages
│   ├── index.html         ← Home
│   ├── mkt.html           ← Marketing (市场学)
│   ├── invest.html        ← Investment (投资)
│   ├── portfolio.html     ← Technical portfolio (技术作品)
│   ├── capabilities.html  ← Capability structure (能力结构)
│   ├── 5dt-pd.html        ← 5DT-PD Framework
│   └── web3.html          ← Web3
├── zh-cn/                 ← Simplified Chinese (same structure as en/)
├── zh-hk/                 ← Traditional Chinese (same structure as en/)
├── hugo/                  ← Blog source + build config
│   ├── hugo.toml
│   ├── content/{lang}/blog/posts/{slug}/  ← Article Markdown
│   ├── layouts/blog/                      ← Templates (DO NOT modify)
│   ├── deploy.ps1 / deploy.sh             ← Build + copy
│   └── _site/                             ← Temporary build output
├── scripts/               ← Utility scripts
│   └── update-version.ps1 ← Auto-update version before commits
├── 文章/                  ← Original article Markdown files
├── robots.txt
└── sitemap.xml
```

---

## Site Architecture & Page Flow

### Visitor Journey (Cross-Link Chain)

```
  Home (index.html)
    ├── 市场学 (mkt.html)  →  Cross-link →  技术作品 (portfolio.html)
    ├── 投资 (invest.html) →  Cross-link →  博客 (blog)
    └── 技术作品 (portfolio.html) →  Cross-link →  投资框架 (invest.html)
```

**Cross-link 原则**：
- 每页底部有一个 `link-card`，以"还需要X能力"的引导语指向下一页
- 市场学 → 技术：数据与创意之外，还需要工程交付能力
- 技术 → 投资：工程交付之外，还需要商业判断力
- 投资 → 博客：框架之外，还需要持续的思考输出

### Capabilities Page (能力结构)

Capabilities 页是整合展示页面，不参与 Cross-link 链，但包含以下结构：

```
Triangular Loop (三角闭环)
    └── 市场理解力 → 技术实现力 → 商业判断力
        └── 完整能力清单 (折叠/展开技能树)
```

### Page Internal Structure (Apple-Style Content Hierarchy)

```
思想锚点（h1-level, 撑起整页）
  └── Hero / Intro
      └── Section 1: 大标题（3-5字）
          └── 介绍性用语（一句话）
              └── 内容卡片 / 列表 / 网格
      └── Section 2: 大标题
          └── 介绍性用语
              └── 内容卡片 / 列表 / 网格
      └── ...
      └── Cross-link（页尾，引导到下一页面）
```

---

## Visual Design System

### White Divider Pattern (白色横线)

每个 `.content-block` 之间必须有 12px 白色横线分隔。

```
page-wrap { background: #ffffff }
.content-block { margin-bottom: 12px }
.content-block:last-of-type { margin-bottom: 0 }
```

详见 `AGENTS.md` → "页面设计模式：Sections 之间的白色横线"。

### Content Block Types

1. **.content-block** — 基础区块，背景色 `#f5f5f7`
2. **.content-block.section-bg** — 带背景图 + 毛玻璃效果
   - `::after` 伪元素提供 `backdrop-filter: saturate(180%) blur(20px)`
3. **.section-card** — 白色圆角卡片（放在 content-block 内部）
   - `background: rgba(255,255,255,.90)`, `border-radius: 18px`
4. **.content-text-card** — 纯白不透明小卡片
   - `background: #fff`, `border-radius: 14px`
5. **.link-card** — Cross-link 容器，居中，底部留白

### Capability Chips

```html
.stack-chip            ← 圆角 999px 药丸徽章
.cap-group             ← 分组容器
.cap-group-title       ← 组标题
```

### QA Groups (5DT-PD Answers)

```html
.qa-group              ← 每个 Q&A 对
.qa-group-title        ← 问题（粗体深色）
.qa-group p            ← 回答（正文）
```

### Dark Mode

所有组件均有 `body[data-theme="dark"]` 变体：
- page-wrap → `#0a0e1a`
- content-block → `#111827`
- section-card → `rgba(30,41,59,.90)`
- 文字色 → `#e5ecf4` / `#9fb0c3`

### Responsive Breakpoints

- Max 991px: 网格变 2 列，字体缩小
- Max 599px: 单列布局

---

## Key Rules

- **Never manually delete `assets/`** — it contains all shared CSS/JS/images
- `hugo/content/` has the article Markdown. Edit there, then rebuild
- `hugo/deploy.ps1` handles build + copy. Run it after editing articles
- All three languages use `translationKey` to pair articles

## Design Principles

- **Relaxed sincerity** — Short sentences. Real details. No second-person ("我给你").
- **No self-praise** — Let the work speak. Use objective framing.
- **White space is a feature** — The white gaps between sections are deliberate.
- **Frosted glass** — Background images use `backdrop-filter` blur, not solid overlays.
- **Each page answers one question** — The思想锚点 is the punchline.
- **Three languages, one source** — zh-cn / en / zh-hk are parallel; content differs only by translation.

---

## Analytics

Cloudflare Web Analytics 已集成。需要在 Cloudflare Dashboard → Web Analytics 获取 token，替换所有页面中的 `YOUR_CLOUDFLARE_TOKEN`。

## URL Shortener / Redirects

`_redirects` 文件（根目录）定义了短链映射表。Cloudflare Pages 自动识别。格式：
```
/source    /destination或https://    301或302
```
编辑 `_redirects` 文件后重新部署即可。

---

## ⚠️ 安全规则

- **没有得到明确指令，绝对不能执行 git push。**
- 任何修改后想推到 GitHub，必须先问用户确认。

---

## Development Preview with Docker

### Prerequisites
- Docker Desktop installed
- A Cloudflare account (free tier)

### Setup

1. Create a Cloudflare Tunnel:
   - Go to Cloudflare Dashboard → Zero Trust → Networks → Tunnels
   - Create a new tunnel (e.g. "fengyu-dev")
   - Set the service to `http://web:8001`
   - Set the domain to `test.fengyuwang.com`
   - Copy the tunnel token

2. Create `.env` file from `.env.example`:
   ```powershell
   copy .env.example .env
   ```
   Edit `.env` and paste your tunnel token.

3. Start the preview server:
   ```powershell
   docker compose up -d
   ```

4. Open https://test.fengyuwang.com in your browser.

### Daily Workflow

```powershell
# Start preview
docker compose up -d

# Stop preview
docker compose down

# View logs
docker compose logs -f
```

### What gets deployed
- Only the `main` branch triggers Cloudflare Pages production deployment.
- The `dev` branch is never deployed to production.
- The Docker preview is purely local + Cloudflare Tunnel — no Pages deployment involved.

---

## Secrets Management

### Never commit these files
- `.env` — Contains Cloudflare Tunnel token and other secrets
- Any file with API keys, tokens, passwords

### What to do if a secret is accidentally committed

1. **Do NOT panic.** The secret can be rotated or history can be cleaned.
2. If the secret is already on GitHub:
   - Add it to `.gitignore` immediately
   - Use `git filter-repo --path <file> --invert-paths` to remove from history
   - Force push: `git push origin <branch> --force`
3. For tokens that cannot be rotated:
   - Clean the git history using the method above
   - The token stays valid, but is removed from public view

### How to verify no secrets are tracked
```powershell
git ls-files .env
git ls-files | Select-String -Pattern "token|secret|key|password"
```

---

## Version

**Current: 26.07.02.13.39** (yy.MM.dd.HH.mm)

Run `scripts/update-version.ps1` before commits.

---

## Git Strategy

| Branch | Purpose | Deploys to Cloudflare |
|--------|---------|----------------------|
| `main` | Production | ✅ Yes |
| `dev` | Daily work | ❌ No |

- NEVER commit to `main` directly.
- NEVER push without explicit user approval.
