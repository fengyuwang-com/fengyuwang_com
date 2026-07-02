# Fengyu WANG — AI Editing Guide

## Structure
- `assets/` = shared CSS/JS/images — DO NOT DELETE
- `hugo/content/{lang}/blog/posts/` = article source
- `hugo/deploy.ps1` = build + copy

## Style
Relaxed sincerity. Short sentences. Real details. NO second-person ("我给你").

## Translation
zh-hk = Hong Kong formal Traditional. 信达雅. Localize jokes.
Use `translationKey` to pair articles across languages.

## Privacy
Prefix title with `*` + `draft: true` for personal info.
## ⚠️ 安全规则
NEVER git push without explicit user approval.

## ⚠️ 当前临时措施（2026-06）
description 同时作为正文第一段。这是为了修复历史文章的结构问题。新文章不要这样做。

## Git Branches

- `main` — Production. Only merge from dev when ready to deploy.
- `dev` — Daily work. Push freely, never triggers Cloudflare Pages.

## Docker Preview

```powershell
docker compose up -d    # Start preview at test.fengyuwang.com
docker compose down     # Stop
```

The tunnel uses a token from Cloudflare Zero Trust → Tunnels. Put it in `.env`.

## ⚠️ Safety Rules
- NEVER push to `main` without explicit user approval.
- NEVER commit to `main` directly. Always use `dev`.
- NEVER `git push` without asking.

## Versioning
Format: \yy.MM.dd.HH.mm\ (auto-updated). Run \scripts\\update-version.ps1\ before commits.

## 页面设计模式：Sections 之间的白色横线

每个 `.content-block` 之间必须有白色横线分隔。这是贯穿全站的设计原则。

### 实现原理

```
page-wrap { background: #ffffff }        ← 白色背景从间隙中"自然流出来"
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
