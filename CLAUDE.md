# Fengyu WANG 网站

三语言个人网站：简体中文、繁体中文（香港）、英语。

## 工作流程

1. **先写 zh-cn，再翻译**。功能/内容先在 zh-cn 验证通过后，再翻译成 en 和 zh-hk。
2. **zh-hk = 香港繁体书面语，不是粤语口语**。用 opencc-js 做 cn→hk 转换，然后修正 `王豐羽`→`王丰羽`。
3. **三语言语义必须一致**（信达雅），不逐字翻译。

## 暗色模式规范

每个页面**必须**同时定义亮色和暗色模式样式。页面写完/修改后必须检查暗色模式是否完整。

### 必需规则（art 子页面用）

```
body[data-theme="dark"] .page-wrap{background:#0a0e1a}
body[data-theme="dark"] .content-block{background-color:#111827}
body[data-theme="dark"] .content-block.section-bg::after{background:rgba(17,24,39,.88);backdrop-filter:blur(20px)}
body[data-theme="dark"] .marketing-hero h1{color:#e5ecf4}
body[data-theme="dark"] .marketing-hero p{color:#9fb0c3}
body[data-theme="dark"] .block-inner h2{color:#e5ecf4}
body[data-theme="dark"] .block-inner p{color:#9fb0c3}
body[data-theme="dark"] .section-card{background:rgba(30,41,59,.90)}
body[data-theme="dark"] .content-text-card{background:#0f172a;color:#9fb0c3}
body[data-theme="dark"] .block-subtitle{color:#6b9aff}
body[data-theme="dark"] .link-card p{color:#94a3b8}
```

### 额外规则（card-grid/营销页面增加）

```
body[data-theme="dark"] .mkt-card{border:0;background-color:#0a0e1a;box-shadow:...}
body[data-theme="dark"] .section-card{border-color:rgba(148,163,184,.20)}
body[data-theme="dark"] .stack-chip{background:rgba(148,163,184,.12);color:#e5ecf4;border-color:rgba(148,163,184,.10)}
body[data-theme="dark"] .block-inner ul{color:#9fb0c3}
```

### 验证方法

**首选（2026-09-07 起）：跑全站大脚本，机器判定，不再靠肉眼。**

```bash
python3 tools/check_site.py   # 全量含暗+亮双向对比度审计 (466页), 全绿才允许 commit/push
```

它用无头浏览器逐页真实渲染，按 WCAG 对比度公式逐文字检查（暗色问题=亮色正常暗色才坏，
亮色问题反之），退出码 0 = 全过。发版前、修 bug 后都必须跑（三条铁律见 AGENTS.md
"Release Gate"节）。手工抽验仅作补充：切暗色看 h1/h2/p/block-subtitle/link-card p/
section-card/content-text-card 是否全部可见。

## 固定规则（不可偏离）

- 卡片字体：h3=1.2rem, p=.82rem, .card-btn=.78rem — 所有页面统一
- art 页面是唯一例外色板（暖色调），但卡片字号不变
- 跨语言链接：`href="/zh-` 必须与页面语言一致，不要指向 zh-cn 或 en
- link-card 导航链固定：ai→invest, cloud→mkt, mkt→portfolio, portfolio→invest, invest→blog, web3→web3-deep-research, art→ethos, ethos→blog
- 不出现 ADHD/dyslexia/「艺术比工作重要」等求职不利内容
- 新增页面后同步更新 sitemap.xml
- Unsplash 图片：card 用 `w=600`，section 用 `w=1000`

## 项目记忆

- LESSONS.md 记录跨会话高频错误的根本原因和修复方法
- `.claude/projects/C--Users-a8881-Desktop-fengyuwang-com/memory/` 存持久化记忆
- **全站唯一检查脚本 = `tools/check_site.py`**（14 节全合并：内容/三语/简繁/部署/死链/
  搜索索引/暗亮对比度浏览器审计）。发版门禁三铁律见 AGENTS.md "Release Gate"节：
  ① 大改后、上 master 前，把新问题类型固化成检查节并入大脚本再跑全量；② 出问题修复后
  用大脚本回归归零再 push；③ 不另建零散检查脚本。
