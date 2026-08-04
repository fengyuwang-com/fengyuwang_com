# 2026-08 新项目上线规划

> 目标：把近期开源项目融入个人网站，体现"三条线，一个根"——投资、市场、技术互相增强。

---

## 1. 项目清单

| 项目 | GitHub | 定位 | 语言 | 归属页面 |
|------|--------|------|------|---------|
| **Open-FengInvest** | https://github.com/fengyuwang-com/Open-FengInvest | AI 协作投资分析框架：七层状态机、数据管道、量化工具、Web UI | Python | **旗舰项目**：invest.html 卡片置顶 + 独立页面 `open-fenginvest.html` |
| **Jingxin（静心）** | https://github.com/fengyuwang-com/Jingxin | 极简冥想引导 App：呼吸 / 正念 / 引导 / 放松 | Flutter/Dart | `portfolio.html`（技术页） |
| **Open-FengOffice** | https://github.com/fengyuwang-com/Open-FengOffice | FengOffice：AI 统一邮件 + CRM（CLI 邮件 + Twenty CRM + Newsletter/Listmonk） | Python | `portfolio.html` 主体 + `mkt.html` 交叉引用 |

---

## 2. 核心决策：项目融入卡片，旗舰置顶

### 概念

**不做 What's New 区块。** 项目直接做成卡片，**自然地融入现有页面**（hero 下方的 card-grid）。每个领域都有自己的"旗舰项目"，放在该页所有项目卡片的**最顶上**，让新东西第一时间露出来。

### 旗舰项目规则

- **invest.html**：`Open-FengInvest` 是旗舰，排在卡片网格第一个（最顶上）
- **portfolio.html**：`Jingxin` / `Open-FengOffice` 作为最新项目，排在卡片网格前面
- **mkt.html**：`Open-FengOffice`（内容运营工具）作为最新项目，排在项目卡片前面
- 卡片点击后滚动到对应 content-block section（与现有卡片行为一致）

### 卡片样式

完全复用现有 `.mkt-card`：
- 背景图 + 渐变遮罩，标题 h3 + 一句话描述 p + `.card-btn`
- 点击 `scrollIntoView` 到对应 section
- 不新增 content-block 方框，不破坏白色横线结构

---

## 3. 放置策略

### 3.1 Open-FengInvest → 旗舰项目

**为什么是旗舰**：七层状态机 + 数据管道 + 量化工具 + 4 AI Agent 并行定性 + Web UI，是投资分析框架从理念到工程化的完整落地，也是投资、市场、技术三条线的汇合实证。**定位语：这是迄今为止最具有野心的项目。**

**展示方式**：
1. **invest.html**：card-grid **第一个卡片**放 Open-FengInvest，点击滚动到新增的 content-block section。
2. **独立项目页** `open-fenginvest.html`（三语各一份），完全复用现有设计体系：
   - Hero：项目名 + 一句话定位
   - card-grid 或直接 sections：项目描述（为什么做、解决什么问题）、核心架构（七层流程）、关键特性、技术栈 / 快速上手、GitHub 按钮
   - 毛玻璃 section + 暗色模式
3. **首页**（可选）：如需要入口，可在首页 About/Projects 区域自然放一张 Open-FengInvest 卡片，指向独立页面。

### 3.2 Jingxin（静心）→ portfolio.html

**为什么放技术页**：Flutter 移动端作品，是跨平台开发能力的实证。portfolio 页有 Flutter 能力 chips，需要一个真实作品来支撑。

**放置位置**：card-grid 排在前面（作为最新项目）；Section 5「交付为开始」（`#delivery`）之后新增一个 content-block（`#tech-capability` 能力区块之前）。

**区块设计**：
- 标题（h2，punchline）：`一个 App，四种呼吸方式`（或 `静下来，也是技术活`）
- block-subtitle：极简风格的冥想引导应用——呼吸、正念、引导、放松四种模式
- 内容要点：
  - 数据模型 `MeditationSession`：时长 / 模式 / 完成状态
  - Provider 状态管理（flutter_provider）
  - 呼吸动画组件 `BreathingCircle`
  - 支持 Web / Android / iOS / Windows 多平台构建
- 卡片网格：portfolio.html 顶部 card-grid 新增一张卡，点击滚动到该区块
- 外部链接：GitHub 按钮

### 3.3 Open-FengOffice → portfolio.html 主体 + mkt.html 交叉引用

**为什么"技术+市场"两面**：项目本质是"内容运营的基础设施"——
- 技术侧：CLI 邮件客户端、Twenty CRM、Newsletter 系统，是工程交付
- 市场侧：CRM + 邮件 + 订阅分发，是市场/内容运营的工具链

**双面方案**（推荐）：
1. **portfolio.html 主体**：作为工程作品展示（API 集成、自动化、Docker 部署），与 Jingxin 相邻或同区块；card-grid 排前面。
2. **mkt.html 交叉引用**：在「项目」section 的 case-grid 里加一个 case-card（排在前面），说明这是「内容运营与 CRM 的落地工具」，链接到 portfolio.html 对应区块。

**portfolio.html 区块设计**：
- 标题（h2，punchline）：`邮件、CRM、Newsletter，一条链`（或 `从收件箱到客户关系`）
- block-subtitle：AI 统一邮件与 CRM——CLI 邮件客户端 + Twenty CRM + 订阅分发
- 内容要点：
  - `fengmail.py` CLI：IMAP 收信 + SMTP 回信
  - `docker-compose.yml`：一键部署 Twenty CRM（端口 3002）
  - `newsletter/`：Listmonk + Postgres 订阅系统
  - 四级邮件分类体系（docs/email-classification.md）
  - 全套 AI 管理脚本：加订阅、退订、发 campaign、处理退订邮件

**mkt.html 交叉引用**：
- 标题：`FengOffice 内容运营基础设施`
- 描述：把邮件、CRM、Newsletter 收进一条自动化链路，市场操作不再散落在 Excel 和人工里。

---

## 4. 实施顺序

1. **zh-cn 先行**：
   - 新建 `zh-cn/open-fenginvest.html`（独立项目页，复用现有设计体系）
   - `zh-cn/invest.html`：card-grid 顶部加 Open-FengInvest 卡片 + 新增 content-block section
   - `zh-cn/portfolio.html`：card-grid 加 Jingxin / Open-FengOffice 卡片 + 新增 content-block
   - `zh-cn/mkt.html`：case-grid 加 Open-FengOffice 交叉引用
   - 本地预览验证
2. **en 同步**：新建 `en/open-fenginvest.html` + 同步 en 首页/invest/portfolio/mkt
3. **zh-hk 同步**：新建 `zh-hk/open-fenginvest.html` + 用 opencc-js cn→hk 转换后人工修正
4. **收尾**：更新 sitemap.xml、README.md、AGENTS.md 页面清单、`_redirects`（如需）、运行 update-version.ps1

## 5. 注意事项

- **项目融入卡片**：不新增 What's New 区块；项目以 `.mkt-card` 形式融入各页 card-grid，旗舰置顶
- **独立页面融入设计体系**：open-fenginvest.html 三语结构一致，复用 hero + card-grid + content-block + 毛玻璃 + 暗色模式
- **白色横线规则**：新增的 content-block 必须是 `page-wrap` 直接子元素；插入后原 `:last-of-type` 自动获得 margin-bottom
- **暗色模式**：新区块必须同时有 `body[data-theme="dark"]` 变体
- **卡片字号统一**：h3=1.2rem、p=.82rem、.card-btn=.78rem
- **链接指向**：跨语言链接 `href="/zh-cn/...` 必须与页面语言一致
- **no self-praise**：描述用客观事实，不用"我的能力是..."句式
- **文案风格**：punchline 用短句、有态度，不超过 12 字；不用"本章节将介绍..."
