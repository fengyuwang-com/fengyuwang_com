# Merge Review — feature/overnight-enhance → dev

> 日期：2026-08-05
> 原则：只合/新增经过审查、干净、不改变内容的 **性能改进 与 bug 修复**。
> 全程在 **dev** 分支执行，不碰 master，不改变 markdown 正文，安全第一。

## 结论速览

| 类别 | 决定 |
|------|------|
| Bug 修复：博客语言切换卡 "Redirecting" | ✅ 合并（**只取源码部分**，跳过 32 个 zh-hk .md） |
| 服务器缓存方案（server.py + _headers） | ✅ 合并，并切换后台预览使用 |
| docker-compose.yml 改用 server.py | ✅ 合并（**不加 openclaw**） |
| `_site/` 取消 git 跟踪 | ✅ 已在 .gitignore 第 23 行，无需改动 |
| 博客 HTML 重建（e5c0f36） | ❌ 不合并（博客只能 Hugo 重新生成） |
| SEO / 文案优化（f845f7c / fd33141 / a9e793e） | ❌ 不合并（属"内容"，用户选择跳过） |
| overnight 记录 / openclaw 容器（bb92d3b / dcef058） | ❌ 不合并 |

## 逐项审查记录

### 1) Bug 修复 589264a —— 合并（部分）

commit 消息 / root cause：
> zh-hk 博客用繁体 translationKey，而 en/zh-cn 用简体，导致 Hugo `.IsTranslated` 失败，
> langUrl() 的回退字符串替换在简体/繁体 slug 不同时生成了错误 URL。

源码修复（**取**）：
- `assets/js/shared-subpage-navbar.js` — `langUrl()`：博客路径不再硬替换语言前缀，改跳博客列表（+1 行）
- `hugo/layouts/_default/baseof.html` — hreflang 改用 `.AllTranslations`（Hugo 层真修复）
- `404.html` — 博客 404 重定向到正确语言的博客列表，而不回首页

跳过（**不取**，属用户内容，最近也被用户编辑过）：
- 32 个 `hugo/content/zh-hk/blog/posts/*/index.md` 的 translationKey 规范化

### 2) 服务器缓存方案 server.py + _headers —— 合并

- `server.py`：读 Cloudflare 风格 `_headers` 规则应用缓存头；未匹配默认 no-cache；绑定 0.0.0.0；无隐藏依赖
- `_headers`：HTML 不缓存；.js/.css 短缓存 revalidate；静态图片/字体长缓存
- `docker-compose.yml`：`web.command` → `python /site/server.py`；**移除 openclaw 容器**

### 3) _site 清理 —— 已满足，不改

`.gitignore` 第 23 行已有 `_site/`，无需改动。

## 验证清单（每一步都要复核）

- [x] 后台服务器切换后，Tailscale `100.123.90.16:8001` 仍 HTTP 200（已实测）
- [x] HTML 缓存头 no-cache / JS revalidate / 图片 max-age=86400（已实测 server.py）
- [x] 博客跨语言切换改用 hidden-trans / 博客列表回退，不再生成破损 URL（代码核对通过）
- [x] dev 分支工作区干净，已一次 commit（e0951d9）
- [x] 不在内容上做任何改动（git diff 复核：无 .env、无 hugo/content markdown）

## 执行结果

- Commit：`e0951d9`（dev），8 文件，+232/−8
- 后台服务器已切换为 `server.py`，PID 监听 0.0.0.0:8001
- 未 push（按规则需用户确认）

