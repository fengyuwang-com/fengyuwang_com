# Fengyu WANG — AI Editing Guide

> 开工前必读本文件 + `DESIGN.md`。本文件只收**不可逆条目**（违反后低成本改不回来：分支、安全、架构、不变量）。
> **防复发锁：新增规则默认进 `docs/guide/` 手册，不进本文件正文；进正文的唯一标准是"违反后能否低成本改回来"，由该标准判定。**

三语个人网站 (zh-cn / en / zh-hk) + Hugo 博客。核心差异：**一个人用一套统一的底层逻辑，贯穿市场、投资、工程三个领域。**

> **架构铁律（必读）**：本站永久保持纯静态（0 运行时，仅 Cloudflare Pages）；一切 AI 功能走 BYOK（访客自带 API Key，浏览器端 JS 直连提供商）；不做自建后端、不做独立子域部署。详见 `docs/decisions/DECISION-0001-zero-runtime-byok.md`，不得悄悄偏离。

---

## 目录与命令

- `assets/` = shared CSS/JS/images — **DO NOT DELETE**
- `hugo/content/{lang}/blog/posts/` = article source (Markdown)
- `hugo/deploy.sh` = build + copy (hugo 构建 → 仓库根 {lang}/blog)
- `en/`, `zh-cn/`, `zh-hk/` = site pages (one HTML file per page per language)
- 博客改动后：`cd hugo && hugo --gc --cleanDestinationDir && bash deploy.sh`
- 日常 dev 检查：`python3 tools/check_site.py --no-dark`；发版前全量见"分支与门禁"
- Todo 纪律：先记 todo 再开工；做完即勾掉清掉，不留已完成堆积；聊到但暂未做的先记入 `todo.md`，不口头欠账

---

## 压缩不变量（违反必返工，只列红线，写法见链接）

1. **页面文件名一律英文**（`invest.html` 而非拼音；品牌用既定英文名）。改名断 URL/SEO，不可逆。详见 `docs/guide/page-structure.md`。
2. **白色横线结构**：所有 `.content-block` 须为 `page-wrap` 直接子元素，`margin-bottom: 12px` 自然流出白线；勿多加 `</div>` 提前关闭 `page-wrap`。详见 `DESIGN.md` §6。
3. **暗色无全局兜底**：本站无 `body[data-theme="dark"] h1,h2,h3,p` 全局回退，每个可见文字须有显式暗色覆盖（标题 `#e5ecf4`、正文 `#9fb0c3`/`#94a3b8`）。详见 `DESIGN.md` §9、对照表见本文件"任务索引"。
4. **Cross-link 链固定**：mkt→portfolio→invest→blog（完整映射见 `docs/guide/page-structure.md`）；`link-card` 须在 `page-wrap` 内、sections 之后。
5. **标题与语气**：section `h2` = punchline（12 词内、具体、有态度），`.block-subtitle` = 正常说明；**NO second-person，NO self-praise**（客观表述，不说"你/我给你"）。详见 `docs/guide/voice-and-translation.md`。
6. **`storm-bg` 仅 Tech 页一次性效果**，禁复制扩散，禁闪烁。详见 `DESIGN.md` §7.7.1。

---

## 分支与门禁（一句话 + 链接）

日常 dev 只跑快速检查 `python3 tools/check_site.py --no-dark`；合并推送 master 前跑全量 `python3 tools/check_site.py`（含浏览器审计）+ 用户明确批准。全文见 `docs/guide/release-gate.md`。

| Branch | Purpose | Deploys |
|--------|---------|---------|
| `master` | Production | ✅ Cloudflare Pages — **NEVER push without explicit user approval** |
| `dev` | Daily work | ❌ Never deploys directly; push freely after checks pass |

---

## 安全红线

- **NEVER** git push without explicit user approval.
- **NEVER** push to `main` without explicit user approval.
- **NEVER** commit to `main` directly. Always use `dev`.
- **NEVER** delete files from `assets/` without confirmation.
- Never commit `.env` or any file with API keys, tokens, or passwords.

---

## 任务索引（遇到具体任务再读）

| 任务 | 读这份 |
|---|---|
| 写文案、翻译、punchline、简繁规则 | `docs/guide/voice-and-translation.md` |
| 改页面结构、卡片网格、cross-link、文件名 | `docs/guide/page-structure.md` |
| 改样式、卡片参数、白色横线、内容块、chips、QA、暗色、响应式 | `DESIGN.md`（视觉唯一源头：§6 间距、§7 组件、§8 响应式、§9 暗色） |
| 发版、Git 流程、检查脚本、Docker 预览、Privacy | `docs/guide/release-gate.md` |
| 报错、样式异常、踩坑对照 | `docs/guide/pitfalls.md` |
| 写博客文章 | `docs/guide/WRITING-博文写作规范.md` |
| 架构决策、能否加后端 | `docs/decisions/DECISION-0001-zero-runtime-byok.md` |
| 文档找不到、历史追溯 | `docs/README.md`（地图）、`docs/archive/`（归档） |
