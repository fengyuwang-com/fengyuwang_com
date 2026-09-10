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
│       └── human-in-the-loop/                     ← Human-in-the-Loop framework viewer (React)
├── en/                    ← English site pages
│   ├── index.html         ← Home
│   ├── mkt.html           ← Marketing (市场学)
│   ├── invest.html        ← Investment (投资)
│   ├── portfolio.html     ← Technical portfolio (技术作品)
│   ├── capabilities.html  ← Capability structure (能力结构)
│   ├── human-in-the-loop.html        ← Human-in-the-Loop Framework
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

设计参数唯一源头是 `DESIGN.md`（§6 间距含白色横线、§7 组件含内容块/卡片/chips/QA、§8 响应式、§9 暗色）。
行为规范见 `AGENTS.md`，任务索引见 `AGENTS.md` 末表。

---

## Key Rules

- **Never manually delete `assets/`** — it contains all shared CSS/JS/images
- `hugo/content/` has the article Markdown. Edit there, then rebuild (`hugo/deploy.sh`)
- All three languages use `translationKey` to pair articles
- 行为规范与门禁见 `AGENTS.md`；发版流程见 `docs/guide/release-gate.md`

## Design Principles

- **Relaxed sincerity** — Short sentences. Real details. No second-person. No self-praise.
- **White space is a feature. Frosted glass. Each page answers one question. Three languages, one source.**
- 全文见 `DESIGN.md` §1 与 `docs/guide/voice-and-translation.md`。

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

```powershell
docker compose up -d    # Start preview at test.fengyuwang.com
docker compose down     # Stop
```

完整步骤（含 Tunnel token 配置）与 Secrets 管理见 `docs/guide/release-gate.md`（Docker Preview、Privacy 节）。
`.env` 永不提交。

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
