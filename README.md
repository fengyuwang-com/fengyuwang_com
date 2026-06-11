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
