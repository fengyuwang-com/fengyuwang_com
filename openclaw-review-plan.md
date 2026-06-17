# fengyuwang.com — Skill 研究报告

## 轮次 1 (03:47, 2026-06-18)

### 搜到的 Skill

1. **UI/UX Design Pro** — clawhub.ai/saifyxpro/ui-ux-design-pro
   - 关键：12 个参考文件必须按序读（设计方向、token 架构、色彩系统、排版、间距布局、深度与层级、组件模式、动画、模式库、无障碍、认知原则、自评协议）
   - "你生成的东西会看起来很模板化"——这是它要解决的问题
   - 强调能区分 premium 和 generic 输出的是**设计系统 token**
   - 推荐默认 light mode

2. **Design Style** — clawhub.ai/benangel65/design-style
   - 多种设计风格预设：Academia、ArtDeco、Bauhaus、Cyberpunk、Fluent2、HumanistLiterary、Kinetic 等 20+ 种
   - 每种风格有完整的设计系统 prompt
   - HumanistLiterary 可能是你网站适合的方向（warm, literary, conversational）

3. **UI/UX Pro Max** — 34.8k 下载，373 安装，很热门
   - 设计系统 token 生成 + 前端代码结合
   - 覆盖 HTML/CSS/JS/React/Next.js/Vue/Svelte/Tailwind
   - 强调生成 complete design system 后再编码

4. **frontend-design-ultimate**（之前已读）
   - Anti-AI-slop 原则
   - 排版不要 Inter/Roboto/Arial
   - 配色 70-20-10 规则
   - 每个设计要有一个"让人记住的东西"

### 对 fengyuwang.com 的思考

1. **设计系统一致性** — 你的网站有 Bootstrap + custom CSS，但缺少统一的设计 token。建议用 CSS 变量整理：`--primary`、`--accent`、`--surface`、`--text`
2. **审美方向** — HumanistLiterary 或 Editorial/Magazine 风格可能适合你的个人品牌
3. **"令人记住的元素"** — 目前网站功能完整但缺少"unforgettable moment"
4. **i18n 体系** — 已经研究清楚了，JSON 是数据源，HTML 是 fallback

### 明早建议

等丰林醒了，可以讨论：
- 是否建立一个小的设计 token 系统（CSS 变量）
- 暗色/亮色的配色方案优化
- 首页记忆点设计
- i18n 体系的清理或精简