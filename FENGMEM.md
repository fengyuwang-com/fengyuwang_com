# FENGMEM — 会话记忆

> 按全局 AGENTS.md 约定维护：每轮对话末尾追加记录，只追加不覆盖。
> 格式：`## YYYY-MM-DD HH:MM — 第 N 轮`

## 2026-08-05 17:55 — 第 1 轮（补建，覆盖本日全部工作）

- 用户要求:
  - 导航下拉「概览」化：市场学/技术/投资/艺术首项改「XXX概览」，理念下拉补「理念概览」
  - 首页 What's New 加 FengInvest 卡（「迄今为止最具有野心的项目」，B 站卡上方）
  - 投资页 `#fenginvest` 移到顶部第一节
  - 技术页项目区与理念「完整分隔」→ 深色专区外壳（新范式）
  - 修复技术页「快捷指令：/publish、…/brainstorm。」溢出
  - 技术页软件项目专区：移到概览卡之下、理念区之上；卡片网格软件项目 4 卡排最前；去圆角；改炫光蓝→「电闪雷鸣」炫光；暗色模式不能是黑色方框
  - 建立 FENGMEM.md 并填充
- AI 行动:
  - push 了先前 10 个提交到 dev（GitHub + Gitee，未碰 master）
  - 三语 labels（`casesOverview`/`portfolioOverview`/`investmentOverview`/`artOverview`/`ethosOverview`）× 桌面/移动下拉模板改
  - 首页插 FengInvest 卡 + 副标题「项目、博客、视频与动态」
  - 投资页 `#fenginvest` 移至第 1 节（后续 section 注释顺延）
  - 技术页 4 项目节包进 `.projects-shell`（初版深灰圆角壳）→ 修复为 page-wrap 直接子元素（消除左右白条）→ 去圆角 → 炫光蓝 → storm 6 层背景 + `storm-glow`/`storm-flash` 动画 → 暗色提亮为蓝色 + 蓝辉光
  - `assets/css/style.css` 加全局 `overflow-wrap: break-word`（溢出根因：CJK kinsoku + `/` 禁断行）
  - DESIGN.md §7.7 新建「Projects Zone (Dark Shell)」+ 位置/圆角/炫光规则；AGENTS.md #6/#7/#8；docs/2026-08-new-projects-plan.md 待办
  - 提交：d8bba39（概览化+首页+投资+专区+溢出）、7b9935a（专区上移+卡片重排+去圆角+炫光蓝）、bb30c98（电闪雷鸣）、（最新一轮：暗色提亮）——均未 push
- 产出: 版本 26.08.05.17.44 → 26.08.05.17.5x；zh-cn 全站生效；en/zh-hk 同步待办在 docs/2026-08-new-projects-plan.md §6.5
- 关键决策:
  - 导航下拉首项一律「XXX概览」（不再放裸页面名，投资▾不再出现重复「投资」）
  - `.projects-shell` 必须是 page-wrap 直接子元素——放 container 内会出现左右白条（踩过坑）
  - 专区无圆角（直边嵌入白底）；背景 = 3 径向光斑 + 2 斜向光束 + 蓝渐变 + 双动画；暗色模式必须明显是蓝色发光体（`#16295c→#2547c8`），渐变起点近黑（`#0b1530`）会被误认为「黑色方框」（踩过坑）
  - 暗色模式 `animation: none` + 蓝辉光，避免动画覆盖阴影产生方形光晕
  - zh-cn 先行验证，en/zh-hk 延后（用户验证阶段）
  - 未跟踪文件 `docs/migrate-lecoo-backup-and-sandbox.md`、`server-newpath.log` 不带入任何 commit

## 2026-08-05 18:10 — 第 2 轮

- 用户要求:
  - 建立 FENGMEM.md 并填充
  - 暗色模式下「每一个壳子都套一个黑色方形框」——查根因
- AI 行动:
  - 排查暗色规则 → 根因：全站 `body[data-theme="dark"] .mkt-card`（`0 20px 50px -8px rgba(0,0,0,.35)`）与 `.section-card`（`0 4px 16px rgba(0,0,0,.2)`）的**黑色 box-shadow**，每张卡在暗底上呈现「黑色方框」
  - 批量修复 32 个 HTML（zh-cn 14 + en 9 + zh-hk 9）：暗色 mkt-card/section-card → `box-shadow: none`（卡片靠 gap/border 分隔）；浅色阴影不动
  - DESIGN.md 暗色 token 表补记录（期间误删「Card grid responsive」行已恢复）
  - FENGMEM.md 追加本轮
- 产出: 版本 26.08.05.18.x；全站暗色模式黑色方框消除
- 关键决策:
  - 暗色模式下**任何元素不使用黑色 box-shadow**（在 #0a0e1a 背景上必显黑框）——这是暗色模式设计红线
  - 纯 CSS bug 修复全站三语同步（非内容改动，不占 en/zh-hk 翻译待办）
