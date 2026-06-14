# Fengyu WANG — Personal Website & Blog

三语个人网站 + Hugo 博客。一个 git 仓库，跨机器、跨系统。

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

## Project Structure
```
/
├── assets/         ← CSS / JS / images / i18n (shared, never delete)
├── en/             ← English site pages
├── zh-cn/          ← Simplified Chinese pages
├── zh-hk/          ← Traditional Chinese pages
├── hugo/           ← Blog source + build config
│   ├── hugo.toml
│   ├── content/{lang}/blog/posts/{slug}/  ← Article Markdown
│   ├── layouts/blog/                      ← Templates
│   ├── deploy.ps1 / deploy.sh             ← Build + deploy
│   └── _site/                             ← Temporary build output
├── scripts/        ← Utility scripts
├── 文章/           ← Original article Markdown files
├── robots.txt
└── sitemap.xml
```

## Key Rules
- **Never manually delete `assets/`** — it contains all shared CSS/JS/images
- `hugo/content/` has the article Markdown. Edit there, then rebuild
- `hugo/deploy.ps1` handles build + copy. Run it after editing articles
- All three languages use `translationKey` to pair articles
## Analytics

Cloudflare Web Analytics 已集成。需要在 Cloudflare Dashboard → Web Analytics 获取 token，替换所有页面中的 `YOUR_CLOUDFLARE_TOKEN`。

## URL Shortener / Redirects

`_redirects` 文件（根目录）定义了短链映射表。Cloudflare Pages 自动识别。格式：
```
/source    /destination或https://    301或302
```
编辑 `_redirects` 文件后重新部署即可。

## ⚠️ 安全规则

**没有得到明确指令，绝对不能执行 git push。**
任何修改后想推到 GitHub，必须先问用户确认。

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

You are on the **dev** branch by default. Edit files locally, refresh the browser to see changes.

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
