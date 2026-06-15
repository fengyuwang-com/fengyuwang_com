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
