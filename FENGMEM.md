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

## 2026-08-05 18:36 — 第 3 轮

- 用户要求:
  - 「截张图看一下暗色模式到底是怎么回事，就会多出一个壳子」
  - 「你把我优美的圆角矩形删掉了，只剩下那个硬朗的那个正方形外壳的，我刚好要，相反，我要那个圆角矩形，不要那个正方形外壳」
- AI 行动:
  - 截图确认：暗色模式下 .section-card（`rgba(15,25,50,.62)` 半透明深蓝背景 + 18px 圆角）与 .content-text-card（`rgba(10,18,40,.55)`）形成可见的深色圆角矩形「壳」
  - 误判：将 section-card/content-text-card 改为透明 → 用户反馈「圆角矩形被删了，只剩方形外壳」
  - 纠正：恢复 section-card/content-text-card 为正常不透明外观（圆角矩形保留）；改为将 projects-shell 本身在暗色模式下透明化（`background: transparent; box-shadow: none; animation: none; ::before { background: none; }`）
  - 服务器多次重启（端口 8001 多进程冲突），最终清理干净
- 产出:
  - zh-cn/tech.html：暗色模式下 projects-shell 透明（无蓝色方形轮廓），section-card/content-text-card 保持正常外观（圆角矩形可见）
  - 亮色模式不变：蓝色风暴效果 + 半透明卡片
- 关键决策:
  - 暗色模式下 projects-shell 应完全透明——用户要的是圆角矩形卡片，不要蓝色方形壳
  - 「圆角矩形」= section-card 的 `border-radius: 18px` 外观，「方形外壳」= projects-shell 的蓝色渐变背景矩形轮廓——两者不要混淆
  - 修复方向：去掉 shell 背景而非去掉卡片背景

## 2026-08-06 00:40 — 第 4 轮

- 用户要求:
  - 「现在是抽搐的一闪一闪，有时候有蓝色有时候没有，改成一直有蓝色但有渐变效果」→ 修复 storm 动画
  - Tech 页验收通过后「归纳一下 Tech 页面从很久以前的 Commit 之后到底是什么变化，然后做一个把它覆盖到全局的计划，在文档里也要更新」
  - 「注意我的闪电炫光蓝背景，这个是一次性的效果，不能作为全局的，但要在 Design MD 里说明白这是怎么回事」
- AI 行动:
  - 定位基线 commit 494b052（本次会话工作前最后一次提交）
  - Tech 页变化归纳：(A) 全局可复用——暗色黑框修复(已 32 页)、移动端文字过窄修复、CTA 按钮等宽；(B) tech 独有一次性——软件项目「闪电炫光蓝」storm-bg；(C) 已全局不动作——projects-shell 等
  - 写批量脚本 scripts/apply-mobile-fix.js（幂等，按 1.25rem 唯一锚点匹配 minified/spaced 三种 CSS 变体）
  - 执行：Fix A 移动端 padding（block-inner 0 12/20px 等）应用到 en/zh-cn/zh-hk 全部内容子页；Fix B cta 按钮等宽应用到 8 个 cta-row 页
  - 处理边角：EN art-* 的 @media(minified) 块缺 1.25rem 锚点（截断块）→ 脚本加 fallback 插在 599 块开括号后
  - 抽验 4 类代表页（web3 minified / capabilities 960 / art.html 多块 / art-architecture 截断），无重复无错位
  - DESIGN.md 新增 §7.7.1（storm-bg 一次性说明）+ §8 移动端文字恢复 & CTA 等宽；AGENTS.md Common Mistakes #7/#8
- 产出:
  - scripts/apply-mobile-fix.js（全局批量修复脚本，幂等可重跑）
  - 三语 ~57 内容页 Fix A + 8 页 Fix B 全部应用，无遗漏无重复
  - DESIGN.md/AGENTS.md 文档同步
- 关键决策:
  - storm-bg 明确为 tech 页面一次性效果，不扩散；在 DESIGN.md §7.7.1 记录其位置/动画参数/不闪烁红线
  - 批量脚本锚点统一用每页唯一的 `.block-inner h2{font-size:1.25rem}`（599 块尾部规则），兼容三种 CSS 变体
  - 首页 3 个 index 结构不同，不需 Fix A/B（排除）
  - 本次不 push，待用户全局确认后再 push

## 2026-08-06 — 第 5 轮

- 用户要求:
  - 「先push，然后随机检查所有页面是否正常（中/英/繁）——但检查放在下面事情做完之后」
  - 「现在有出现深色的暗色模式字体的情况，比如是黑色的字体，你检查一下全局有哪些这样的情况，design md 里有没有？没有的话加上」
  - 「FengMedia 有个严重问题，它应该是市场学里面的，不是技术里面的。把卡片、图片、还有它的描述整体迁移到市场学，放到顶上，卡片放最前面。不需要炫光。先不要操作告诉我计划」→ 后改为「所有网页3种语言，在做之前先push」
- AI 行动:
  - push 当前 dev（工作树干净，无待推提交）
  - 暗色字体调研（Explore agent）：发现「所有页面无全局标签级暗色兜底，凡未被 body[data-theme=dark] 覆盖的亮色深字都会贴在暗底」
    - 实际可见2处：zh-cn/index.html L72 span `#0f172a`；5dt-pd.html ×3 的 `.section-card h1`
    - 潜在2处：art.html ×3 `.content-text-card h3 #1d1d1f`；capabilities ×3 `.tree-toggle #7a5c33`
  - 修复：zh-cn/index span 改 `#00a1d6`（与en/zh-hk一致）；5dt-pd/art/capabilities 各加针对性暗色覆盖（三语同步）
  - DESIGN.md §9 补全暗色映射表（qa-group/case-card/pillar-card/content-text-card ul/section-card h1/node-tree/tree-toggle）+ 新增「暗色文字覆盖原则」说明；AGENTS.md Common Mistakes #11
  - FengMedia 迁移：zh-cn/tech 移除卡+storm-bg专区（div 100/100 平衡无残留）；zh-cn/en/zh-hk 三个 mkt 顶部加 FengMedia 卡+磨砂 section（无炫光）；en/zh-hk 用 GitHub 链接（因无对应官网页，避免死链）
- 产出:
  - 暗色字体：index/5dt-pd/art/capabilities 修复（三语）+ DESIGN.md/AGENTS.md 文档
  - FengMedia：zh-cn/tech→zh-cn/en/zh-hk mkt 迁移，三语 mkt div 平衡
- 关键决策:
  - FengMedia 作为市场学工具移到 mkt 顶部；tech 去掉其炫光专区，storm-bg 只留 tech 其余3项目
  - en/zh-hk 因无 fengmedia 官网页，cta「Open GitHub」链接到 github.com/fengyuwang-com（遵循 en 既有惯例，避免 /en/fengmedia.html 死链）
  - 暗色兜底：明确「任何展示文字的元素必须有 body[data-theme=dark] 覆盖」，写入 DESIGN.md/AGENTS.md
  - 随机抽查放最后（用户指示）

## 2026-08-06 — 第 6 轮

- 用户要求:
  - 「要把网站变成 3 种语言。现在有一些网站只有简体中文，查看哪些，把它们翻译到三语」
- AI 行动:
  - 盘点三语文件差异：发现 5 个官方产品页只存在于 zh-cn（fenginvest / fengmedia / fengoffice / jingxin / search-king），en/zh-hk 缺失，而 sitemap.xml 和 zh-cn 页的 hreflang 早已声明其三语存在
  - 读 5 个 zh-cn 页全文，按「结构副本 + 只译语言相关」生成 10 个新文件（en × 5 + zh-hk × 5）：
    - 逐字复制：inline <style> 块、Unsplash 图 URL、共享 navbar/footer 脚本、author=王丰羽、og:image=logo.png、back-to-top
    - 翻译：全部正文文案 + head 语言 metas（lang/title/description/canonical/hreflang/og:locale/og:url/twitter/JSON-LD）
    - 交叉链接 href 改 /en//zh-hk/；FengInvest data-section=investment，其余 portfolio
    - search-king 额外携带 .content-text-card pre 样式（正文+暗色）
  - 翻译遵循 AGENTS.md：relaxed sincerity、不用第二人称、h2 punchline、zh-hk 香港繁体（與/從/構建）
- 产出:
  - 10 个新文件：en/{fengmedia,fenginvest,fengoffice,jingxin,search-king}.html + zh-hk/ 同名
  - 验证：全 10 文件 div 平衡（46-48 对）；三语结构一致（6 section + 6 card）；cross-link 无死链；dark-mode + 移动 Fix A 齐全
- 关键决策:
  - en/zh-hk 官网页缺失是 sitemap 已声明但文件未建的缺口 → 本次补齐
  - en/zh-hk 页面也用 GitHub 链接为主外链；不建死链
  - 结构完全复刻 zh-cn（含 mobile Fix A 和暗色覆盖），只换语言相关文案

## 2026-08-06 — 第 7 轮

- 用户要求:
  - 「fengmedia nav bar 没有迁移成功 修正并检查其他 navbar对应」
  - （背景：上一轮把 FengMedia 从技术迁到市场学，但导航没跟上）
- AI 行动:
  - 排查导航：# navbar.js 里 FengMedia 仍在技术(portfolio)下拉的「软件项目」分组；fengmedia 页 data-section=portfolio（访问时高亮「技术」而非「市场学」）
  - 修正：
    1. 3 个 fengmedia.html 的 data-section: portfolio → cases（市场学）
    2. navbar.js 从技术下拉 software 组移除 fengmedia 行（桌面+移动）
    3. navbar.js 在市场学 cases 下拉加 fengmedia 行（概览之后，桌面+移动）
    4. 因改共享 navbar JS，把全站 shared-subpage-navbar.js?v=26.08.05.01.04 提升到 26.08.06.18.03（207 页 + hugo baseof），cache-bust 使改动生效
  - 检查其他 navbar 对应：fengoffice/jingxin/search-king 仍属技术(portfolio)正确（只有 FengMedia 迁走）；fenginvest 仍属投资(investment)
- 产出:
  - fengmedia 导航归位市场学，技术软件项目分组仅剩 jingxin/fengoffice/search-king
  - 全站 navbar JS 版本刷新
- 关键决策:
  - FengMedia 作为市场学工具，导航应出现在市场学下拉，且访问时高亮市场学
  - 其余未迁移产品页(office/jingxin/search-king)留在技术正确，不动
  - 浏览器 broker 反复断连，导航验证以静态结构+逻辑检查为准；请用户在浏览器确认视觉效果

## 2026-08-07 — 第 8 轮

- 用户要求:
  - 「你只更新了没有英语的网页。完全没有更新有英语但是变化了的网页，这些网页很多的。中文版的变化了，英文版的还没变过来，因为中文版的已经加了很多介绍了」
- AI 行动:
  - 全面审计(Explore agent)三语内容差异，锁定 8 组页面在 zh-cn 有内容但 en/zh-hk 缺失或未扩写
  - 按类别同步(A类整段缺失、B类文案扩写)，全部翻译加入 en 和 zh-hk：
    - tech.html: en/zh-hk 补 3 个软件项目专区(静心/FengOffice/Search King)+ 3 张卡 + storm-bg 炫光 CSS(::before + storm-flow)
    - invest.html: en/zh-hk 补 fenginvest 专区 + 卡(放最前)，并重排 section 注释编号
    - mkt.html: en/zh-hk 补 FengOffice case-card(链接对应语言 fengoffice.html)
    - art-painting.html: en/zh-hk 扩写第1段(4段) + 补第2块「精神比真实更重要」
    - art-architecture/design/literature/music: en/zh-hk 扩写各 section 详细文案(段落数与 zh-cn 严格一致)
- 产出:
  - 8 组页面 × 3 语言结构完全一致(div 平衡、section/card 数量、段落数全部 match)
  - 无死链；en/zh-hk tech 含 storm-bg/暗色/移动 Fix A
- 关键决策:
  - 扩写时严格对齐 zh-cn 的段落数(含 link-card 机制：某句在 body 或 link-card 的位置与 zh-cn 一致)
  - art-* 页中「好的音乐/设计和写作一样」等收尾句，确认属于 link-card 而非 section body，避免重复计数
  - 翻译遵循 AGENTS.md 语气(不用第二人称、h2 punchline)，zh-hk 繁体

## 2026-09-07 04:40 — 第 9 轮

- 用户要求:
  - 拉最新 dev，按 docs/HANDOFF-2026-09-07-flygo-navbar-buttons.md 继续三件待办：①按钮等高（蓝 .default-btn vs 白 .default-btn-one）②flygo 页加 GitHub/Release 链接 ③导航栏完整性并入 check_site.py
- AI 行动:
  - 按钮等高：playwright 实测定位根因 = .default-btn-one 的 margin-top:5px 在 flex 行里让 .default-btn 被 stretch 多撑 5px（54 vs 49）；修复 = style.css 全局 .cta-row 内两按钮 margin 清零（间距交给 gap）；全站扫描 81 页 9 混排组 0 不匹配
  - flygo ×3 hero cta-row 加「下载 Release」（蓝）+「查看 GitHub 仓库」（白），文案/属性沿用 fengmedia 惯例；仓库 = fengyuwang-com/FlyGo（gh 查得，private！站是公开的，链接访客 404——已在 todo.md 记待站长决策：公开或建 Open-FlyGo）
  - 发现 d0631c2 改 navbar JS 但没升 cache-bust 版本号 → 全站 bump v=26.08.06.19.08 → v=26.09.07.04.10（442 文件）；首次用 Python 文本模式误把 364 个 CRLF 文件规范化成 LF（diff 暴涨到 1.9 万行），改用 git ls-files -z + cat-file blob 字节级重做保住原始行尾（最终 diff 456+/442-）
  - 子代理（后台）完成 check_site.py 第 15 节导航栏完整性：静态解析 navbar JS（copy 对象花括号配平 + 模板数组方括号配平），可达性三语 27 页全绿无孤儿页，三语 copy 各 86 键一致，*Href 三语路径一致且目标存在；带负向测试
  - 检查抓出 navbar JS 两处硬编码旧问题 → 修复而非豁免：「按主线浏览网站」内联三元提取成 siteTracks copy key（三语），汉堡 aria-label="Toggle menu" 提取成 menuToggle（zh-cn 切换菜单 / zh-hk 切換選單）；node --check + 三语渲染冒烟通过
  - check_site.py 新增第 16 节按钮等高：BTN_EVAL_JS 搭第 13 节同一趟无头渲染采样（零额外成本），同容器蓝白混排组 offsetHeight 必须相等
  - 清掉残留 _site（gitignored，上次中断构建产物；hugo 本机未装，sitemap 节按"构建后已清理"路径跳过）
  - 新建项目根 todo.md 入账（全局 AGENTS.md 要求）
- 产出: 全量 check_site.py 待收口（后台跑中）→ 全绿后 commit + push dev
- 关键决策:
  - 硬编码文案一律提取成 copy key 修复，不加豁免（AGENTS.md #6 铁律）
  - FlyGo 仓库 private 仍按用户指令挂链接（jingxin.html 挂 private Jingxin 仓有先例），但 private 导致访客 404 必须上报站长拍板
  - Windows 下批量改文件必须字节级操作（git blob 读原文件），文本模式 open() 会毁 CRLF
  - 收口: 全量门禁全绿 (EXIT=0, 469 页暗色 0 问题, btn-height 33 组 0 不匹配), commit 3c45dc6 已 push dev (GitHub+Gitee), master 未动

## 2026-09-07 06:02 — 第 10 轮
- 用户要求: 建一个 Open（Open-FlyGo），其余几个 Open 项目原仓有更新的一并同步；红线=财产/密码/绝对个人私密绝不泄露，个人观点可透露，其他都能透露；子代理有名额就派
- AI 行动: 后台子代理并行（并发限 2，两单被弹后排队补派）——新建 Open-FlyGo（184→165 文件，剔真实激活码/tailnet 主机名/FengInvest 持仓截图[财产红线]/会话记录/exe，Release v2026.09.07-0130）；同步 Open-FengMedia（+1937 文件）并发现 8-23 初始提交曾把 FENGMEM.md 推上公开仓约两周 → filter-repo 清史强推；同步 Open-FengInvest（剔 Discussion/design/真实持仓数，BYOK 零泄露，226 处路径消毒）；核实 Open-FengOffice 已同步、Open-FengOrchestrator 落后 2 提交已补（剔 DeepSeek 余额数字）；五镜像当前树+git 历史双扫；flygo.html×3 改链 Open-FlyGo；全站门禁全绿
- 产出: Open-FlyGo 新仓+首个 Release；Open-FengMedia master=536322c；Open-FengInvest=02d77e4；Open-FengOrchestrator=e36519e；本仓 flygo 链接修复 + todo/FENGMEM 记账（本轮 commit）
- 关键决策: FengMedia 镜像源取本地最新（GitHub 私仓已与本地分叉且 push remote 指 Gitee，不擅自推私仓，上报待收敛）；git 历史清洗（force push）按隐私红线授权由主 Agent 亲自执行；GitHub 悬空 SHA 残留需站长提工单，入 todo；私仓跟踪 FENGMEM.md 的再泄漏风险上报待批
