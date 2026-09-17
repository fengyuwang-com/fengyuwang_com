# 体系全景页 —— 董事长需求文档（2026-09-18）

> 这份文档只说一件事：fengyuwang.com 的「体系全景」页到底要做什么、不要做什么。
> 它是站内文档（进本站 `docs/`，**不进博客**），也是接手这件事的人的第一份读物。
> 上一版（2026-09-17 落 dev 的 `system.html`）被董事长判「完全不满意，没掌握到精髓」，本文件是那次判词之后的返工依据。

---

## 0. 一句话

把「体系全景」页从「项目清单」改成「董事长到底在做什么」的说明书：用主网站自己的模板写，讲全自有项目与它们之间的关系，讲透三条根本观点。

---

## 1. 董事长原话（要求原文，不许转述走样）

- 「这个网站要有我的主网站的风格。」
- 「本来模板已经写好，为什么不直接改？加点爱。」
- 「这个网站应该包括我全部的项目信息，并且展示它们之间相互关系。」
- 「它应该深入地去理解我到底做了什么事。」
- 「Galaxy 和黑金都已经明确放弃了。」
- 「2LIP 是没错，但是两层界面原则要说清楚，最好不要用缩写。」
- 「MD 作为 AI 的控制面……这个也是我根本的一个观点。」
- 「`FengOS/web/index.html` 这个是我设计的依据，但是它不完全符合我站点的设计要求，所以希望稍微重做。」
- 「桌面那份不是我的网站研究报告让你发表，而是只是一个研究报告，我内部参考的。你放到我这个网站的文档，不是放到我网站的那个博客里面。」
- 「这个我完全不满意，因为它没有掌握到我那个精髓。」（对上一版的结论）

---

## 2. 这一页的骨头：三条根本观点（缺一条就是没掌握精髓）

### 2.1 一人公司，是一道工程题

一家公司被当成一道工程题来解，分五层：**意图 / 组织 / 人才 / 执行 / 保障**。
董事长本人只做两件事：**下目标**、**签字验收**。其余交给文档、Skill、编排与人机协作机制承担。

### 2.2 两层界面原则

全称写全，**不要用缩写「2LIP」**。

- 对话层：对 AI 说话，负责「做」；
- 观景层：看 AI 在做什么，负责「看」；
- 文档层：管 AI 怎么被操作，负责「管」。

要点：这不是 UI 的消亡，是**操作权的转移**——人从「自己操作工具」变成「下达目标 + 验收结果」。

### 2.3 MD 是 AI 的控制面（董事长的根本观点）

四件套范式：

- `AGENTS.md` —— 规则，唯一真源；
- `MISSION.md` —— 北极星与 DoD；
- `todo.md` —— 任务账本；
- `FENGMEM.md` —— 会话日志。

辅以 Skill（`SKILL.md`）作为可复用的操作封装。

运行机制：AI 开工先读文档，拿到身份、规则与任务；行动结果回写账本与日志；规则变更回写 `AGENTS.md`。

收口：**文档即控制平面**——两层界面原则回答「人怎么操作 AI」，「AI 怎么被操作」由**文档**回答；文档的读者从「人」扩展为「人与 AI」，且 **AI 是更严格的读者**（它逐字执行）。

出处（董事长的既有文字，写作时照此口径）：本站 `TWO-LAYER-INTERFACE.md`（对应已发布博文 `two-layer-interface`）；`FengOrchestrator/docs/两层界面原则与全生态审查.md`。

---

## 3. 内容范围

- **全部自有项目，一个不落**（当前口径见文末附录）。
- **5DT-PD 与这一页一起重做**（董事长 2026-09-18 令）。5DT-PD（`C:\FengProj\5dt-pd`，=「五层双轨双循环盈利型内容智造架构」）本机已有两张成品图，必须在这次重做里一并上站：
  - **框架图**（`5dt-pd-framework.jsx`，516 行）：五层 L0 交付 / L1 生成 / L2 语义 / L3 产品 / L4 战略；双轨 = 机（左轨）/ 人（右轨）；双循环 = 战略大环（L0 ↔ L4）/ 战术小环（L1 ↔ L2）；三根横梁 = 风控 / 资产 / 成本（贯穿全层）；另含三条护城河文案与技术内核映射。
  - **软件工程架构图**（`5dt-pd-architecture.jsx`，645 行）：4 核心构件（Router / Asset / Executor / Delivery）+ 2 人接口（Gate 审批门 / Knob 调参口）+ 事件总线（Event Bus）+ 贯穿式治理（Governance）；含主管线（生产流）/ 反馈流（双循环）/ 治理流（贯穿）三条流与 Task DTO 契约表。
  - 支撑资产：`5dt-pd/` 下的 TypeScript 骨架（router / asset / executor / governance / human(gate,knob) / event-bus，BullMQ + Redis + OpenAI）、`5dt-pd-viewer`（React + Vite 查看器，`npm run dev`）。
  - 站内现状：只在 `system.html` 里有一张文字卡片，**没有任何图** —— 这正是要重做的地方。
- **项目之间的关系**：谁引用谁、谁依赖谁；两张图必须用同一套关系口径（生成器里的 `project_pairs()`）。
- **六大领域**及各自项目数、跨领域关系。
- 每个项目要能看出「它是什么、和别人什么关系」，不是一串名字。

---

## 4. 设计依据与站规约束

- **设计依据**：`FengOS/web/index.html`（苹果风、白底、单一强调色 `#0071e3`、无暖色）。
- 但它「**不完全符合站点设计要求**」→ 必须**按站点已有模板与类重做**：
  `page-wrap` / `container` / `marketing-hero` / `content-block` / `block-inner` / `section-card` / `block-subtitle` / `content-text-card` / `punchline` / `cta-row` / `default-btn` / `card-grid` / `mkt-card` / `back-to-top`。
  不是把 `index.html` 搬过来，更不是再自造一套 CSS。
- **站点硬约束**（详见 `docs/guide/release-gate.md` 与 `FengOS/docs/交接-体系全景静态页-2026-09-17.md`）：
  零运行时；三语齐平（zh-cn / zh-hk / en）；en 页零汉字（含属性与注释）；h1/h2/h3/`.punchline` 需字面 `font-size`；暗色主题单独覆盖；`master` = Production，**未经董事长明确批准不推**。

---

## 5. 明确禁区（已放弃的方向，不许复活）

- `galaxy.html` 黑金 Three.js 版图；
- `FengOS/web/index.html` 里 canvas 星系图（Galaxy）那套画法；
- 自造平行 CSS 命名空间（`sys-*` / `dg-*` / `gn-*` 那类）；
- 把这一页写成博客文章；
- 用缩写「2LIP」代替「两层界面原则」；
- **本机已有的成品图不许重画、不许"另做一版"**——董事长的原话是「你把我本地的东西放上，对我本地的东西丰富一下」，本地的图是素材是资产，搬上去、讲透它，不是推倒重来。

## 5.1 「丰富一下」是什么意思

不是加更多项目名字，而是：本地的图、本地的数字、本地的状态（哪张图对应哪个论断、哪条关系有何证据、哪条是私有的哪条公开可点）都要落到页面上；页面要能把「本地的这份资产」讲清楚，而不是给出一堆概括词。


---

## 6. 配套交付

- 桌面那份研究报告是**内部参考**：归档进本站 `docs/`，不做成博客文章、不对外发布。
- **本文件**同样进本站 `docs/`（活文档，页面上线后转 `docs/archive/`）。

---

## 7. 图清单（2026-09-18 澄清：不是二选一，是全都要）

董事长对上一版 todo 的口径更正：**「环也是要的，那个三元也是要的。这些东西它不是同一个东西，那个星系什么的，那个本身就是废掉。」**

所以要上站的是**全套本地成品图**，彼此不替代：

| 图 | 来源 | 状态 |
|---|---|---|
| 研究层圆环（五段圆环 + MD 宪法） | `FengOS/web/index.html` 的 **`.pdca-ring`** 块（HTML 581–627 行、CSS 341–368 行、i18n zh 984–990 / en 886–892） | 要 |
| 研究层三元流程（Sources → Engines → Stores 三段线性） | `FengOS/web/index.html` · `rschDiagram()`（1389–1422 行） | 要（**独立于上一行**） |
| 两纸三元 + 治理底座 | `FengOS/web/index.html` | 要 |
| 授权 → API 第二路 | `FengOS/web/index.html` | 要 |
| 服务 / 自动化 / 项目 / 一篇论文一张图 等既有分节图 | `FengOS/web/index.html` | 要 |
| 五层双轨双循环框架图 | `C:\FengProj\5dt-pd\5dt-pd-framework.jsx` | 要（新） |
| 5DT-PD 软件工程架构图 | `C:\FengProj\5dt-pd\5dt-pd-architecture.jsx` | 要（新） |
| ~~canvas 星系图（Galaxy）~~ | `FengOS/web/index.html` `<canvas id="galaxy">` | **废，不上** |

## 8. 引用必须过得住门槛：引用 ↔ 图 综合检查（新增，董事长 2026-09-18 令）

原文：「它的那引用没有经过门槛的检查，就是你要搞一个综合检查——**我引用，我怎么可能没有这个东西的图呢？**」

要求：页面上**每一处引用都必须能落到一张图或一件实物产物**上；引用与图/产物对不上，就是缺陷。

要做的是一个**综合检查脚本**（门槛），至少覆盖：

1. 页面上出现的每个项目 slug ↔ 本地目录/仓库 → 必须存在，且卡片里的行数、日期、关系条数可复算；
2. 页面上每条「关系」↔ 生成器 `project_pairs()` 的口径 → 必须一致、可追溯；
3. 页面上每处论断/引用 ↔ 一张图或一个产物 → **缺图即报警**（这就是董事长问的那句）；
4. 本地已有的成品图清单 ↔ 页面上实际用的图 → 反向对账，本机有图却没上站的要列出来。

该检查纳入 `tools/check_site.py` 的 `system` 门禁组，与既有的 div 配平、卡片数、navbar key 数、暗色审计同级——**过不了就不许上线**。

## 9. 听写澄清（2026-09-18 董事长已确认）

原话里的「**MGS**」是语音听写误差，董事长确认**说的是 jsx**：即 5DT-PD 的那两个 `.jsx` 图**本身有问题**，这次要一起修、一起放进页面。因此对 5DT-PD 的要求是「移植 + 诊断 + 修正」，不是原样照搬。

## 9.1 当务之急：先把本地图的效果引过来，再套站点格式（2026-09-18 董事长令）

原话：「你先把那个效果引用过来，再加上我的网站的那个格式，这个是当务之急了。」

执行方式：**并行派多个子代理**，每张图一个独立模块与预览页，互不冲突；图上文字走三语 copy 字典、颜色取站点既有字面色值（见 §9.1.1）、零运行时。产出汇总在：

- `FengOrchestrator/FengOS/scripts/system_figs/fig_5dt_framework.py`（5DT-PD 五层双轨双循环框架图）
- `FengOrchestrator/FengOS/scripts/system_figs/fig_5dt_architecture.py`（5DT-PD 软件工程架构图）
- `FengOrchestrator/FengOS/scripts/system_figs/fig_research_ring.py`（研究层圆环 + MD 宪法）
- `FengOrchestrator/FengOS/scripts/system_figs/fig_paper_trinity.py`（两纸三元 + 治理底座）
- `FengOrchestrator/FengOS/scripts/system_figs/fig_auth_api.py`（授权 → API 第二路）
- `FengOrchestrator/FengOS/scripts/system_figs/fig_project_relations.py`（项目关系静态图，**非星系**）
- 预览页统一放 `FengOrchestrator/FengOS/reports/fig_preview/*.html`

以上为并列图，**彼此不替代**（董事长：「这些东西它不是同一个东西」）。

## 9.1.1 站点样式实况（2026-09-18 实测，绘图契约按此为准）

`assets/css/style.css`（75,776 字节）实测：**0 个 `var(--)`、无 `:root` 自定义属性**——站点**没有 CSS 变量体系**，颜色全是**字面色值**（唯一强调色 `#0071e3`，出现 93 处；正文一级 `#0f172a`、卡片底 `#ffffff`、发丝线 `rgba(148,163,184,.10)`）。暗色**不是** `prefers-color-scheme`、也不是 `.dark`，而是 **`[data-theme="dark"]` 属性选择器覆盖**（style.css 约 3576–3586 行一带）。

因此图的产出契约是：模块暴露 `TEXT`（三语字典，键集一致）+ `render(lang)`（只返回 SVG/HTML 结构，不带 `<style>`）+ **`CSS`（该图所需 scoped 样式文本，含 `[data-theme="dark"]` 覆盖，不带 `<style>` 标签本身）**；类名统一 `fig-<图名>-` 前缀；色值一律取站点既有字面值，不新配色、不加暖色，暗色下阴影 `none`。

（此条同时更正本文件 §4 里「用 CSS 变量」的旧说法。）

## 9.2 桌面文稿的落位（2026-09-18 董事长令）

原话：「`C:\Users\a8881\Desktop\fengyuwang_com.md` 我是让你这个文稿并进我的那个网站的文稿。」

该文件 445 行 / 36KB，是对本站的只读侦察报告（工程结构 / 设计语言 / 页面骨架 / 多语规范 / 资源限制 / 已知雷区）。处置：**并进**站内文稿 corpus——按主题做最小增量合并（设计语言 → `DESIGN.md` 或 `docs/guide/page-structure.md`；门禁与雷区 → `docs/guide/release-gate.md`、`docs/guide/pitfalls.md`；多语与写作 → `docs/guide/voice-and-translation.md`；工程结构 → `README.md`/`AGENTS.md`），无归宿的原文归档到 `docs/notes/`；**不改 `docs/archive/`，不进博客**。



---

## 11. 落位方案（图 → 页面位置，2026-09-18 主会话定）

生成器 `FengOrchestrator/FengOS/scripts/build_system_page.py` 现有段落次序：hero → `#thinking` 思想体系 → `#domains` 领域关系图 → `#projects` 项目全清单 → link-card。

图模块统一放 `FengOS/scripts/system_figs/`，每个导出 `TEXT` / `render(lang)` / `CSS`。集成时把各模块的 `CSS` 汇总追加进页面 `<style>`（紧随 `PAGE_CSS` 之后），把 `render(lang)` 插进对应段落。

| 图模块 | 落位 |
|---|---|
| `fig_paper_trinity`（两纸三元与治理底座：两层界面原则） | `#thinking` 的图位。**它取代已有的 `svg_thinking(L)`**——后者画的正是 L1 对话层 / L2 观景层 / 文档治理面，与本图重复；本图是其超集（多出 人·AI·系统 三元、两纸、C1/C2 约束、五枚药丸、独立审查与 tagline）。`#thinking` 的 h2、subtitle、`punchline`、四个 `sys-point` 全部保留。 |
| `fig_research_ring`（五段圆环 + MD 宪法） | 新增「研究层」段落 |
| `fig_research_tri`（Sources → Engines → Stores 三元流程） | 同上段落，与圆环并列，**互不替代** |
| `fig_auth_api`（授权 → API 第二路） | 同上段落（研究层的第二条路） |
| `fig_5dt_framework`（五层双轨双循环框架图） | 新增「5DT-PD」段落 |
| `fig_5dt_architecture`（5DT-PD 软件工程架构图） | 同上段落，与框架图并列 |
| `fig_project_relations`（项目关系静态图，非星系） | `#domains` 段落，紧接 `svg_domain_graph` 之后（领域图讲领域，本图讲项目级，口径同源 `project_pairs()`） |

三条根观点（一人公司是一道工程题 / 两层界面原则 / MD 是 AI 的控制面）的**文字**落位：两点并入 `#thinking` 的 `sys-point`，两点并入新增段落，措辞照 §2 的原文口径，不得用「2LIP」缩写。

已知待办：`svg_thinking` 若因替换而失去唯一调用点，连同其**独占**的辅助函数一并删除（共享的如 `_wrap_fit` 保留）——删前先确认没有第二个调用点。

## 12. 听写/事实勘误台账

- **「研究层圆环」的出处写错过**：原写 `rschDiagram()`，实际圆环在 `index.html` 的 `.pdca-ring` 块（HTML 581–627、CSS 341–368）；`rschDiagram()` 是**另一张**三元线性流程图（1389–1422），已单列为 `fig_research_tri`。见 §7。
- 「MGS」= 听写误差，实为 jsx（§9）。
- **5DT-PD 架构图原稿与 `5dt-pd/src/` 真实代码有 3 处不符**（移植时已按代码修正）：
  1. **没有 Delivery 构件**。`src/index.ts` 自述组装的是「Router + Asset + Executor + Governance + Gate + Knob」，全仓只有 `delivery.published` / `delivery.metric_updated` / `delivery_publish` 等**事件名**，无 Delivery 实现文件——原 JSX 把 Delivery 画成核心构件属外推。
  2. **事件名不符**：JSX 用的 `task.done` / `task.posted` / `anchor.patch` 在 `src/types/events.ts` 的 `EventTypeEnum` 里不存在；真值应为 `task.delivered` / `delivery.published` / `user.reacted` / `anchor.patch_proposed`。
  3. **DTO 字段数不符**：JSX 表只有 9 行，`src/types/task.ts` 的 `TaskSchema` 是 **12** 个顶层字段。
- **5DT-PD 框架图原稿的其余缺陷**（15 条，已在移植中修，摘要）：深色写死为默认；22 个写死色值（五层五色 `#6366f1 #3b82f6 #0ea5e9 #06b6d4 #14b8a6` + 三梁红绿琥珀 `#ef4444 #84cc16 #f59e0b`）；「三根横梁贯穿全层」与「双轨」其实都只是**卡内一列**、层与层之间断开（名不副实）；战术小环 `L1 ↔ L2` 的标注落在 L1/L0 之间（与文案自相矛盾）；循环与层序硬编码索引 `i >= 2 && i <= 3`；靠 React `useState` 折叠；i18n 键名 `zh-CN/zh-HK` 与站点 `zh-cn/zh-hk` 不一致且缺键静默回退；emoji（`🛡📦💰⚙👤`）写在文案值里会原样进 en 页；箭头既在文案里又被剥掉再补画；三语长度差近一倍却无折行（SVG 定宽必溢出）；全文件 `aria` 出现 0 次；中英混排无空格、中文里夹半角括号、用斜杠与箭头当连词。修法：浅色为基准 + `[data-theme="dark"]` 覆盖；五层不再靠色相区分，改用**层号 + 位置 + 形状**（实心方块=机 / 空心圆=人；三角=风控 / 方=资产 / 菱形=成本）；三梁做成每层下沿**车道 x 对齐**的横带并跨层续接；双轨做成**贯穿层栈**的左右竖轨；小环精确跨 L2 卡顶→L1 卡底；三语各自折行排版。

- **5DT-PD 架构图原稿的其余缺陷**（已在移植中修）：硬编码多套配色（`DARK_COMP`/`LIGHT_COMP`/`mvpColors` + 内联色散落）；写死 `theme="dark"` 与 `minHeight:"100vh"`；出现绿 `#84cc16`、琥珀 `#f59e0b`、红 `#ef4444`、teal、cyan 等暖色/多强调色；组件数与副标题自相矛盾（副标题漏 Governance 却画了 8 个盒）；Governance 既称「不占流程节点」又被画进主链 `Executor→Governance→Gate→Delivery`；依赖 React `useState` 运行时与内嵌 i18n 组件。修法：配色收敛为一份 `CSS`（全取站点字面色值）、三条流改用**线型**（实线/虚线/点线）+ 图例区分、治理改为横向贯通带、DTO 补足 12 行、改为纯静态 SVG + 三语字典。

## 13. 待董事长裁决（图里发现、不宜擅自改的语义问题）

1. **层 ↔ 4P 映射顺序**：原稿把 `Pricing` 放在 L0 交付层、`Product` 放在 L3 产品层，4P 的 P 顺序被打散（Product / Promotion / Price·Place 分别落在 L3 / L1 / L0）。是原稿有意按「交付倒推」排的，还是笔误？本次移植**保留原样**，未擅改。
2. **「算力精算」（三根横梁之一）与 L4 战略层的「算力预算」**：两者层级与职责疑似重复。是同一个概念的两处说法，还是成本控制的两级（预算在 L4、精算贯穿全层）？本次保留原样。
3. **5DT-PD 缺 Delivery 实现**：图面把它画成 4 核心构件之一，但 `5dt-pd/src/` 里只有 Delivery 相关**事件名**、没有实现文件（`src/index.ts` 自述组装的是 Router + Asset + Executor + Governance + Gate + Knob）。是尚未落地、还是本就不设此构件？本次按原稿保留盒子并在图上标注未落地。

---

## 10. 验收标准

1. `python tools/check_site.py` 全绿（含 Chromium 暗色对比度审计）。
2. 董事长本人验收并认可「掌握了精髓」。上一版被判「完全不满意」的教训：**别把项目清单当精髓**。

---

## 附录：数据口径（快照 2026-09-17，重做时须重新生成）

- 自有项目 **78** 个：本地 **36** / 仅云端 **42**；代码行数（本地）1,432,605。
- 领域 6 个：工具与实验 38 / 内容创作 23 / 基础设施与编排 19 / 知识与人机协作 14 / 自动化执行 12 / 投资金融 6。
- 项目关系对 **75** 组（引用 ≥ 2 次）；连通节点 41 / 孤立节点 37。
- 连接度 hubs：resume 24、fengyuwang_com 16、fengorchestrator 9、fengmedia 9、feng-media 7、fenginvest 7、fengasni 6。
- 公开仓库链接 34 个 / 身份标签 44 个。
