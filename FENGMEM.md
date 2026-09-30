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

## 2026-09-07 06:16 — 第 11 轮
- 用户要求: 确认网站是否搞定；拍板「第三方 HR 真实姓名邮箱得取消掉」；其余待办等日后举措
- AI 行动: 核实 dev=8f47440 已推、flygo×3 链 Open-FlyGo、门禁绿；Open-FengOffice docs/email-classification.md 脱敏——3 个 HR 个人邮箱 + 8 个人名 →【已脱敏】，git filter-repo --replace-text 全历史重写（仅该文件含这些 PII，已验证），强推 master 8243ac3→feef33a，GitHub 现文件 0 命中；全站门禁全绿 EXIT=0
- 产出: Open-FengOffice 干净历史 feef33a；todo.md 悬空提交项并入 Open-FengOffice 旧 SHA；第 11 轮入账 commit 推 dev
- 关键决策: 保留分类文档本体（README/CLAUDE.md 引用不断链），只脱敏第三方个人 PII；公司系统邮箱（Webull/OKX 等公开企业地址）保留；未来私仓同步该文件必须重做同样脱敏；旧提交悬空归入 GitHub Support 工单待办（与 Open-FengMedia 可同单）

## 2026-09-07 15:25 — 第 12 轮
- 用户要求: 网站 push 到主线生产（明确上线批准）
- AI 行动: 部署前再跑全站门禁（全绿 EXIT=0）；发现 master/dev 分叉——origin/master 多 652c368（relicense，即 LESSONS 所记事件残留）、本地 master 落后远端；先 ff 同步本地 master 到远端，再合并 dev（LICENSE 两边同 blob 干净通过，合并树与 dev 逐字节一致），push master
- 产出: master=886635c（GitHub ls-remote + Gitee 输出双确认），Cloudflare Pages 自动部署；dev 已切回、工作树干净；todo/FENGMEM 第 12 轮入账 commit 推 dev
- 关键决策: 652c368 独有提交经合并自然归位（不 rebase 不强推）；上线内容 = dev 全量（约 57 提交：FlyGo 页/首页改版/博客批次/搜索/暗色修复/check_site 门禁）

## 2026-09-08 20:42 — 第 13 轮

- 用户要求:
  - 首页头图单图仍可滑动（原 2 图减为 1 图后轮播未摘），要求去掉滑动
  - 轮播代码注释保留（以后恢复多图可复用）；模板署名 Zoomin/Barakah 改 FengTemplate；2021/2022 年统一 2026（含 DESIGN.md）
  - 澄清门禁误解：全量回归只在发版到 master 前跑，日常 dev 只跑快速检查；AGENTS.md 瘦身，细节搬 docs/ 子文件夹，docs/ 根下只留文件夹
  - 计划先落盘再找独立子代理审查；CLAUDE 改指针文件、FENGMEM 冻结不动、README 同步瘦身；补本轮 FENGMEM
- AI 行动:
  - 三语 index.html：`owl-carousel owl-theme` → `hero-static` 静态容器，去滑动；DESIGN.md §7.9 同步为单图静态说明
  - main.js 头图轮播块整体注释并写两步恢复路径；style.css/responsive.css 头改为 FengTemplate、2026
  - check_site.py 加 hero-static/残留 owl/模板署名检查；AGENTS.md 门禁改为"dev 跑 --no-dark，master 前跑全量+批准"
  - `--no-dark` 全绿后 commit 到 dev（未 push）；写 PLAN-文档瘦身与重组-2026-09-08.md 并找独立子代理评审（approve-with-changes，意见并入 §7）
  - 按用户意见更新计划：CLAUDE 指针化、FENGMEM 冻结、README/LESSONS 同步瘦身
- 产出:
  - dev 本地提交 1 个（含头图去轮播+改名+门禁措辞）；落盘计划 1 份（含评审意见 §7）
  - 本轮 FENGMEM 记录（第 13 轮）
- 关键决策:
  - 单图 + loop:true + 轮播容器 = 仍可拖动；根治是静态容器 + 注释初始化，两步可恢复
  - 文档瘦身标准：违反后能否低成本改回来；不可逆（分支/安全/架构）留正文，可逆细节藏链接后
  - FENGMEM 冻结存档一字不动；CLAUDE 瘦成指针；README 保留门面可读性下同步瘦身

## 2026-09-08 21:30 — 第 14 轮

- 用户要求:
  - 远端有没有更新（有则麻烦）；审查刚做的工作是否符合文档要求；"开始"合并修复
- AI 行动:
  - 查远端：origin/dev 有 9-07 功能线 4 提交（导航栏完整性 §15 / 按钮等高 §16 / FlyGo 改链 Open / master 上线 886635c），本地有文档瘦身线 5 提交；执行 git merge origin/dev
  - 冲突 2 处手工合流：FENGMEM.md 两边历史并存（远端第 9-12 轮保留，本地第 9 轮改记第 13 轮）；check_site.py 取并集（远端 §15/§16/BTN_EVAL + 本地用法措辞 dev--no-dark/master 全量 + 头图静态/署名检查 + archive 审计路径）
  - 其余自动合流：style.css（品牌头+cta-row 等高）、index×3（hero-static+导航 v=26.09.07.04.10）、navbar JS、博客重建页
  - `git add` 标记解决 → `check_site.py --no-dark` 全绿（含 navbar §15、hover、struct、parity）→ commit d19f8bd 到 dev（未 push）
- 产出:
  - 合并提交 d19f8bd（dev 本地，未 push）；工作树干净；本轮 FENGMEM 记录（第 14 轮）
- 关键决策:
  - 回轮号唯一递增（本地 9→13，合并收尾记 14），避免与远端 9-12 重号
  - 门禁口径：合并验证用 --no-dark 即可；全量暗色审计只在发版 master 前跑

## 2026-09-13 — FengOrchestrator 会话代办
- 用户要求: 写学术级文章放本仓库根目录（待编入网站）。
- AI 行动/产出: 根目录新增 TWO-LAYER-INTERFACE.md（两层界面原则：chat-first + Generative UI + local-first + 文档治理面三元命题，含参考文献）。未动 hugo/zh-cn 结构，待丰羽收录。

## 2026-09-13 — 事故记录：文章提交被 rebase 丢弃后恢复
- 事故: pull --rebase origin dev 时，文章提交 3635e801 被静默丢弃（rebase finish 落在 fb4c048a，未保留补丁），本地文件一并消失，gitee 也被 force 到无文章的 fb4c048a——即此前"dev 同步"结论覆盖的是不含文章的状态。
- 处置: reflog 定位 3635e801 → cherry-pick 为 b2147654 → GitHub+gitee 双推成功（fb4c048a..b2147654）。
- 教训: rebase 后必须 git show 验证关键文件仍在远端，不能只对哈希；本次用户以"fb4c048a 有我文章吗"抓住，主会话此前核验不严。

## 2026-09-13 — 博客清理通宵任务 + 博客/AI 页优化（主会话）
- 用户要求: 通宵执行博客审计处置（删/重写/批量修，全权负责）；后追加：opc 三语补齐、相关阅读题材化+加框、博客列表阅读时长、用 TWO-LAYER-INTERFACE.md 优化 AI 页、博客原样推送、文案须对照 voice-and-translation 规范。
- AI 行动/产出:
  - S1 删 37 目录×3 语=111 篇（60fdfce9）；S2 重写/修补 R1-R9（0f334732、867f8d98）；S3 zh-hk 简体全站清扫（户等 opencc 盲区 46 文件）+ 三语 39 篇正文半角→全角 2830 处（bccbcd31）；S4 全量门禁绿 + 顺带修 4 类改版遗留低对比度（b1f60380）。台账 docs/notes/博客清理-执行台账.md 标 DONE。
  - opc 五层三语补齐转正（cd6f4b65，每语 170 篇上线，sitemap 616）。
  - 相关阅读弃时间序改 [related] 倒排索引（tags100/title60/text40）+ 淡蓝面板框（fb4c048a）。
  - 博客列表页三语阅读时长 chip（card-rt + JSON rt 字段 + 搜索结果渲染同步）。
  - AI 页×3 编入两层界面原则：跨两列卡片 + 第五节四条 + hero/meta 改写（45df5895）。
- 关键决策:
  - 教训：写文案前必须重读 docs/guide/voice-and-translation.md，不可凭记忆——卡片 h3 曾写成名词标签（generic 反例），经站长提醒后改 punchline「说话就是操作/Talking is the operation/説話就是操作」。
  - opencc s2hk 对 戶/户 互穿、检不出 户：zh-hk 简体扫描必须叠加密文清单（户/价/谁/叙/霉/准 等）。
  - 相关阅读 first 3 取的是日期序：Hugo 页面默认按日期排，"同标签取前3"恒等于"最新3篇"。
  - master 全程未动，上线待发版门禁+站长批准。

## 2026-09-18 — 体系全景页：需求文档落定 + 待办立账（主会话）
- 用户要求: 先写文档说清「体系全景页要干什么」，文档同时进站内 docs（不是博客）；写完更新 todo，更新完汇报 todo 是什么；本轮不做任何实现。
- AI 行动/产出:
  - 新增 docs/notes/REQUIREMENTS-体系全景页-2026-09-18.md：董事长原话 10 条 + 三条根本观点（一人公司是工程题五层 / 两层界面原则全称不缩写 / MD 是 AI 的控制面四件套）+ 内容范围 + 设计依据与站规约束 + 明确禁区（galaxy 黑金与 canvas 星系图已放弃、禁自造 sys-*/dg-* CSS）+ 配套交付 + 待指认项 + 验收 + 数据口径附录（78 项目/6 领域/75 关系对）。
  - docs/README.md 的 notes 行补记该活文档及归 archive 的时点。
  - todo.md 待办队列加一条：返工任务指向 FengOrchestrator/FengOS/todo.md（T53/T54/T55），并注明 `{lang}/system.html` 只落 dev 未推 master。
- 关键决策:
  - 「网站的文档」= 仓库 docs/（站内无公开 /docs/ 页面），与博客分离；研究报告按内部参考处理，不发布。
  - 星系/Galaxy 与黑金两条线判为放弃，写进需求文档禁区，避免下一棒复活。
  - 相互关系用哪张图仍需董事长指认（index.html 成品图多张），列为 T54 阻塞项。
  - master 未动。

## 2026-09-18（续）— 体系全景页需求文档二次修订：5DT-PD 并入 + 引用↔图 门槛（主会话）
- 用户要求（要点）: 体系全景页要与 5DT-PD 一起重做；5DT-PD 站内只有文字卡、引用没过门槛检查（「我引用，我怎么可能没有这个东西的图呢」）；环与三元不是同一个东西、全都要，废掉的只是星系；把本地的东西放上去、丰富本地的东西。
- AI 行动/产出:
  - docs/notes/REQUIREMENTS-体系全景页-2026-09-18.md 修订：§3 增 5DT-PD（含两张本机成品图说明）、§5 增「本地成品图不许重画」、§5.1 定义「丰富一下」、§7 重写为图清单（环/三元/授权→API/分节图 + 5DT-PD 两图，星系不上）、新增 §8 引用↔图 综合检查四项、新增 §9 待确认听写「MGS」、验收顺延 §10。
  - todo.md 入口行同步（T53/T54/T55/T56）。
- 关键决策:
  - 「网站的文档」= 仓库 docs/，与博客分离（延续本日上一轮）。
  - 本地图是资产：搬上站讲透，不重画。
  - master 未动。

## 2026-09-18 — 续轮（图站点化 + 门禁 + 文档勘误）
- 用户要求: 延续——本地成品图引上站并套站点格式（当务之急）；体系全景页与 5DT-PD 一起重做；引用必须过「引用↔图」综合门禁；桌面文稿并进站内 docs。
- AI 行动:
  - `docs/notes/REQUIREMENTS-体系全景页-2026-09-18.md` 增补：**§9.1.1 站点样式实况**（`assets/css/style.css` 实测 0 个 `var(--)`、无 `:root`；暗色靠 `[data-theme="dark"]` 属性选择器；强调 `#0071e3` ×93、暗色 `#2997ff`；模块契约补 `CSS: str` 导出与 `fig-<名>-` 类名前缀），并更正 §153 旧的「颜色只用站点 CSS 变量」说法。
  - 同文件新增 **§11 落位方案**（每张图落到生成器的哪一段）与 **§12 听写/事实勘误台账**。
  - §7 图清单更正：**研究层圆环的出处是 `index.html` 的 `.pdca-ring` 块**（HTML 581–627 / CSS 341–368），不是 `rschDiagram()`；`rschDiagram()` 是另一张**三元线性流程**（1389–1422 行），已单列一行。
  - 桌面文稿并进已由子代理完成（9 个文档 +97/−2，原文归档 `docs/notes/REPORT-站点设计与工程规范侦察-2026-09-17.md`）。
  - 派出后台子代理在 `tools/check_site.py` 实现「引用↔图」四条综合检查，纳入 `system` 门禁组。
- 关键决策:
  - 图的产出契约以 §9.1.1 实测为准，**不引入 CSS 变量体系**；暗色一律 `[data-theme="dark"]` 覆盖。
  - 集成时 `fig_paper_trinity` 取代生成器内已有的 `svg_thinking(L)`（同一主题、本图是其超集），避免一页两处讲同一件事。
  - 分支 `dev`；master 未动，未做任何 commit / push。

## 2026-09-18 — 口径翻转轮：过度产物封存，体系全景页退回「小修小改」
- 用户要求（原话）: 「我只是让你把我本地的那个 Web 小修小改一下，你现在给我画成一堆图，搞了一个页面中转，搞了一堆页面。」「我本来有那个很美妙的东西……我本来怎么样就怎么样。」「我让你在我的网站上做这个事。」
- AI 行动:
  - 停止对 `tools/check_site.py` 的「引用↔图」门禁改造（子代理中途被打断，工作区留 +272 行未收尾，**未回退、未 commit**）。
  - 冻结现状：`{zh-cn,zh-hk,en}/system.html` 里上一棒生成的「7 图版」原样留盘，不再往上叠；**不删除任何东西**，等董事长裁决。
  - 重派 1 个后台子代理，把 `FengOS/web/index.html`（董事长的设计依据）**小修小改**成站点上的一个页面：分节/节序/文案/已有图原样保留，只换站点样式与静态预渲染形态；星系节删除；**零新增文件**。
- 关键决策:
  - 站点设计要求按实测口径执行：**无 CSS 变量**（`style.css` 0 个 `var(--)`）、颜色写字面值；暗色走 `body[data-theme="dark"]`；导航页脚 JS 注入；en 页零汉字；静态预渲染零运行时。
  - 分支 `dev`；master 未动，未做任何 commit / push。

## 2026-09-18 — 修复 human-in-the-loop 页架构图不显示（改名对不上）
- 用户反馈（原话）: 「http://127.0.0.1:8080/zh-cn/human-in-the-loop.html 这不是有个 5DT 吗？怎么还是没了呀？那个 5DT 要改名字了。那个页面显示不出来，是因为那个东西名字改了之后，它那个没对上，知道吧？还是叫 5DT。」
- 诊断（用户判断正确）: 提交 `a07373ae`（`5dt-pd` 改名 `human-in-the-loop`）**只改了目录名，没改文件名** —— 三语页面被改成引用 `../assets/js/human-in-the-loop/human-in-the-loop-viewer.js`，盘上却只有 `5dt-pd-viewer.js`。实测：新名字 **404**、老名字 **200** → `<script type="module">` 加载失败 → `#root` 空 → 架构图整块不显示。
- 全站对账: 扫所有 html 的本地 `src`/`href` 引用 ↔ 实物，缺失**仅此一处**（另 3 处 `../{lang}/blog/` 是 Hugo 构建期产物，非缺失）。
- 修复: `git mv assets/js/human-in-the-loop/5dt-pd-viewer.js assets/js/human-in-the-loop/human-in-the-loop-viewer.js`（对齐页面已有引用，页面零改动）。
- 复验: headless Chromium 跑三语，`#root` 均渲染成功、**零失败请求、零控制台错误**；截图确认五层（L4→L0）× 双轨（机/人）× 双循环（L0↔L4、L1↔L2）× 三横梁完整绘出。
- 文档: `docs/guide/pitfalls.md` 里那条「**现存实例**」已改写成「历史实例（已修）」，并补上教训 —— **改名类提交必须同时核对「目录名 / 文件名 / 引用串」三者**。
- 暴露的查漏: 门禁 `link` 检查会整体剥掉 `<script>` 标签，`<script src>` 404 永远查不出（这就是它躲过门禁的原因）；已记入 `FengOS/todo.md` T54 须补「本地资源引用↔实物」检查。
- 未 commit、未 push；分支 `dev`，master 未动。

## 2026-09-18 — 体系全景页「小修小改」版落盘（三语）
- 用户要求: 把本地 `FengOS/web/index.html` 按站点设计要求小修小改成一个页面。
- AI 行动: 三份 `{zh-cn,zh-hk,en}/system.html` 重做为该页的站点静态版（约 2992 行/份）；生成器 `FengOS/scripts/build_system_page.py` 改动只在其自身。**零新增文件**。
- 页序: hero（抬头 + 3 KPI：1,432,605 行代码 / 78 项目 / 11 种语言）→ 服务（6 项 + 端口）→ 自动化（五段圆环 + MD 宪法）→ 两纸三元 → 思想 → 领域关系 → 项目清单（78 卡）→ 尾卡。**星系节删除**。
- 门禁: 生效版 `tools/check_site.py` **270 PASS / 0 FAIL**（含 Chromium 暗色审计 730 页 0 低对比度）；修掉门禁抓出的 3 处真实对比度缺陷。另：工作区那份未收尾的 272 行改造**跑不起来**（`AttributeError: ... has no attribute 'project_pairs'`），已封存不启用。
- 文案诚实化: 服务/自动化的 hint 由「实时探活·一键启停」改为「静态快照：本页只列，不起停」（本页无启停按钮，照抄等于吹牛）。
- 分支 `dev`；master 未动，未 commit、未 push。

## 2026-09-30 — 体系全景三语页回归设计系统（死代码清理 + 补回 §7.3 卡片）
- 用户要求（原话）: 「回归之前先确定push一下工作区干净，然后再直接把它搞成符合我设计系统的创新型设计」；选项选了「全面回归设计系统 / 先注释掉 / 按实际内容修正导航 / 全部换成规范色」。
- 根因（三条）:
  1. **`.content-text-card` 从未被定义** —— 全站唯一引用点是 `assets/css/style.css:1316` 的 `word-break` 工具类，不是卡片本体。提交 `2820f7ee` 的说明写「补 content-text-card 规范样式」，实际 `git show --stat` 只有 3 个 RSS 文件，样式压根没落盘 → 三张方法卡裸奔（padding 0、无底色无边框）。
  2. **85% 死 CSS** —— `pd5-*`/`tri-*`/`rsch-*`/`dg-*`/`md-*`/`think-*` 六套早期图形系统的遗留，liveRules 611~642 → 157~194。
  3. **侧栏 7 个锚点里 6 个悬空** —— `#pd5` 那条 `data-rail` 早已无对应 id，正是它掩盖了约 100 条 `pd5-*` 死规则的判定。
- 做法: `.cleanup_dead_css.py`（一次性脚本）—— 死判定 = 选择器触及的 class/id 在 HTML `class=`、JS `classList`/`className=`/`querySelector`、`id=` 中全无引用；死代码**注释掉不删**（可回滚），内部 `*/` `/*` 做转义防早闭合；越界色按 DESIGN §5 映射（`#30d158`→`#0071e3`、`#1f3b8a`→`#2563eb` 等 13 条，canvas 的 `ctx.strokeStyle` 走整档替换）。
- 三个真实 bug（都是自己写的，逐一修掉）:
  1. 追加卡片定义的条件误判 `prefers-reduced-motion`，导致 `system.html` 三语**根本没插入**定义（浏览器实测 padding 仍 0px）→ 去掉该条件。
  2. 条件写成按 `<style>` 块判定 → 同一规则在页内每个 style 块重复 2~3 份 → 改为**按文件**只插一次。
  3. **`process()` 返回的是 CSS 裸体，`<style>` 标签属于正则 span 不属于规则** —— 我把 `CONTENT_TEXT_CARD` 拼到 `block`（含标签）上，污染了块尾，浏览器整段 CSS 解析失败，页面全裸。改为剥标签→拼接→处理→重新包标签。
- 验证: `.verify_cleanup.py` 用**字符串感知 CSS tokenizer**（朴素 `count('/*')` 会被死代码里的转义和 `*/ /*` 连写带偏，之前的假阳性就来自这）比对 `git show HEAD:` 原文。终态 **9 文件全 OK：killed_live 0 / dangling 0 / offpalette 0**。
- 浏览器实测（这是唯一可信口径）: `.content-text-card` 计算值 = `padding 20px 24px` / `radius 14px` / `bg #fff` / `border 1px rgba(148,163,184,.1)` / `shadow 0 2px 8px rgba(15,23,42,.04)` / `color #475569` / `line-height 1.85` / h3 `1.05rem 700 #0f172a` —— 与 DESIGN §7.3 原值逐项吻合。关系图 canvas、KPI 卡、项目卡均正常。
- 门禁: `python tools/check_site.py --no-dark` **0 FAIL / exit 0**（末尾 `✔` 打印在 Windows GBK 控制台抛 UnicodeEncodeError，属既有编码问题，非检查失败；用 `PYTHONIOENCODING=utf-8` 复跑 exit=0）。
- 遗留待用户裁决: `gn-*`（关系图 SVG）/`fx-*`（滚动进场）/`sys-*`（KPI/筛选/卡片）三套**活着**的创新类是否按 `track-split-shell` 先例正式登记进 DESIGN.md —— 用户原话「你先给我看看效果，如果效果好，我就进」。
- 分支 `dev`；master 未动，**未 commit、未 push**。

## 2026-09-30 — 体系全景三语页：删说明文案 + 去掉「实时」假声明
- 用户要求（原话）: 「快照 2026-09-17…逐条可核，非估算」上面这番话全部删掉；「节点大小按该领域被标注的项目数缩放…阈值规则…依据口径…」也全部删掉；「这个右上角有个一有个二的全都删掉」；随后追加: 「本机 36 · 仅云端 42 这个不要说」「另有 13 个项目未识别语言这也不要说」「实时 · 实测这是错的，根本就没有实时的」「那个颜色…一部分有渐变一部分左右两边就没有了呀」。
- 删掉的三块（三语 × 3 页 = 9 文件）:
  1. `.sys-hero-note` —— 过期的「快照 2026-09-17」溯源行（今天已 30 号）。
  2. `ul.sys-caption` —— 领域图下方四条方法论（节点缩放/边宽/阈值规则/依据口径）。
  3. `span.fx-ghost` —— 右上角大字ghost节号「01」「02」。
  连同 8 条失效 CSS 一并删（含 `@media(max-width:599px)` 里的 `.fx-ghost` 与 3 条藏在 DEAD CODE 注释里的同名规则）。**注释内的也要删**：类名已不存在，留着是误导。
- 「实时」是**事实性错误**，不是文案口味问题: 78 节点 / 135 边全部烤死在 `<script type="application/json">` 里，KPI 三个数字是字面量 markup，运行时零请求。所以「实时 · 实测」「每个项目，实时可查」「本页每一个数字都从这台机器实时测得」三处都在声称一件页面没做的事。改为「快照 · 实测」「逐条可查」「实测得出」；en 同步改 SNAPSHOT · MEASURED / item by item / was measured…Nothing estimated。
- 顺带删掉两条 `.sys-stat-note`（本机/云端拆分、未识别语言数）—— 同一个静态快照问题，且拆分不是关于项目的用户可见事实。
- **EKG「渐变」不是 bug**: `.base` 是 `rgba(0,113,227,.16)` 通栏细线（实测 bbox 0→420 全宽），`.pulse` 是 150px 亮段 `stroke-dasharray:150 850` + `fx-ekg` 3.4s 循环扫过（实测 offset 215→817 连续变化）。用户看到的「中间有颜色、左右没有」就是亮段扫到哪算哪。**已向用户说明，未改** —— 要不要改成常亮满线是设计选择，不是缺陷。
- 三个自己的 bug（都记下来）:
  1. `strip_notes.py` 打印 `ghost=None` 崩在循环里 → 只处理了 1 个文件就中断，后 8 个文件处于半处理状态。脚本必须**幂等**且不能在写文件前崩。
  2. `[^{}]*\.cls[^{}]*\{` 在这种体量的样式表上**灾难性回溯**，跑 100s 没完 → 换成花括号扫描器（`drop_dead_rules`），秒级。
  3. 扫描器只认顶层规则，`@media` 里的死规则看不见 → 加递归；死代码注释头用 `[^*]*` 匹配会撞上注释自己的 `*/` → 改成精确匹配那一行固定文案。
- 验证: 三语 9 文件 `note=0 cap=0 ghostMarkup=0 退役类彻底移除`；`.verify_cleanup.py` 报的 `killed_live` 恰为这 8 条**有意删除**的规则（逐条核对无附带损伤）；门禁 `check_site.py --no-dark` **0 FAIL / exit=0**；浏览器实测 DOM 中 `.sys-hero-note`/`.sys-caption`/`.fx-ghost` 均为 0，h2 标题文字完好。
- 分支 `dev`；master 未动，未 commit、未 push。

---

## 2026-09-30 22:20 — 体系全景：取消本机/云端二分 + 查看仓库改规范药丸 + 删口径说明卡
- 用户要求: ①「不要区分什么本机和云端仓库」②「这个查看仓库符合我设计原则吗？它怎么是裸着」③「口径说明/数据来源这种说明性的文字也不需要」
- 查证结论:
  - **查看仓库确实不符合**。DESIGN §7.3 定的卡内链接组件是 `.card-btn`（`999px` 药丸 + 半透明填充 + 描边 + `.78rem/600` + `6px 14px` + hover 换背景），而 `.sys-card-repo` 当时是「粗体蓝字 + 只有 hover 下划线」，一个裸文本 run，没有任何容器 —— 这就是「裸着」的来源。**拿 `.card-btn` 的参数**（白卡上白填充看不见，改为 accent 淡染 `rgba(0,113,227,.08)` + `rgba(0,113,227,.16)` 描边，hover 加深到 .16），暗色沿用同套 `rgba(41,151,255,…)`（§9 映射）。
  - **本机/云端是采集方式的产物，不是项目属性**（本地路径扫描 + GitHub 仓库列表两路合并而来），访客不关心。四处全删：卡片徽章、meta 行（`本机代码 4,126 行`→`代码 4,126 行`；云端条目那行「无本机代码统计」整个删掉，因为它只说明「这个没有数」）、`来源` 下拉筛选（连带 JS 里 `sv` 变量与 `data-source` 判断）、以及 graph 页 JSON 节点 `badges` 里的同两个串。
  - `.sys-note-card`（口径说明 + 数据来源）三语全删，附带 7 条失效 CSS。
  - `.sys-scope-note` 原本也是二分口径的散文版（「42 个私有仓与 2 个仅本机项目…」），改写成只讲还成立的事：私有仓不给外链、清单一条不减。
- 保留未动: 关系 chip 的 `title` 里「本机源码文本词边界命中（graph.py 口径）」是**证据方法**说明，不是二分；两条项目描述里的「本机环境自己治」是行文。**170 处「本机」里绝大多数属这两类，不该删。**
- 自己的事故（重要）: 中途我为了清掉脚本的半成品跑了 `git checkout -- <9 个文件>`，**把本会话前几轮未提交的成果全冲掉了**（reveal 修复、删文案、去「实时」）。`git fsck` 找不回（checkout 就地覆盖，不产生 blob）。**所幸 5 个一次性脚本都还在盘上且确定性可重放**，按序重跑 5 步完全复现（步骤 1 输出 504/446/477 条选择器、rail 片段一致；步骤 2 各文件 note/caption/ghost 计数一致），再叠加本轮改动。**教训：清理脚本前先 commit，或至少先 `git stash`；`checkout --` 是不可逆的。**
- 第二个自己的 bug: `.fix_source2.py` 里删 hover 规则的正则 `\.sys-card-repo:hover\{[^}]*\}` 匹配到的是**新写的规则**，把旧 hover 留下了，于是 `:hover{text-decoration:underline}` 仍生效。改成按整段字面量精确替换。**改样式前要先 `print` 出磁盘上真实的规则串，别凭记忆写正则。**
- 验证: 门禁 `check_site.py --no-dark` **0 FAIL / exit=0**（中途因删 note-card 多吃了 2 个 `</div>` 报 struct FAIL 322 vs 320，对照 HEAD 确认原位有 `</div></div>` 后补回，balance 归 0）；浏览器三语实测 —— 78 卡、34 个查看仓库全部 `999px`/`6px 14px`/accent 淡染、徽章只剩语言、`来源` select 与 note-card 均 false、卡片 opacity 全 1（无灰带）、暗色切到 `rgba(41,151,255,.12)` 正常。
- 踩过的坑: 同一次 `setAttribute('data-theme','dark')` 后立刻读 `getComputedStyle` 会读到**旧值**（层叠未重算），一度误判暗色失效；分两次调用就正常。`document.styleSheets` 里 Google Fonts 那张跨域表读 `cssRules` 抛 SecurityError，遍历必须 try/catch 跳过。
- 分支 `dev`；master 未动，未 commit、未 push。辅助脚本 `.cleanup_dead_css.py` `.strip_notes.py` `.fix_claims.py` `.fix_reveal.py` `.fix_source.py` `.fix_source2.py` `.verify_cleanup.py` 仍未跟踪。

---

## 2026-09-30 22:55 — 修复我自己搞崩的关系图画布（SyntaxError 全块失效）
- 用户要求: 承接上轮，截图确认「左右两边有白斑」是否消除。
- 事故: 上轮 `.fix_source.py` 的 `kill_src_var` 正则把 `if(!q||!d` 连同 `sysSource` 那行一起吃掉，9 个文件句首都剩一条裸的 `||!s||!out)return;`。**这是 SyntaxError，而 `<script>` 里任何一处语法错会让该块内每一条语句都不执行** —— 关系图 draw 脚本因此整块没跑，canvas 渲染成一块纯白矩形，就是用户说的「白斑」。三语 9 页同时中招。**门禁全绿也照样空**：它查 CSS/结构/JSON，查不到这个。
- 修复: `.fix_filterscript.py` —— 有 `#sysFilterBar` 的 3 页重写 IIFE（去掉来源筛选），没有的 6 页整段删除（本来就是死代码，查一个不存在的元素就 return）。随后又单独修了两遍被同一条正则啃坏的 graph JSON（`"badges":TypeScript"` → `"badges":["TypeScript"]]` → `"badges":["TypeScript"]`）。
- 自己的第二个 bug: 校验用的 node 脚本用 `<script(?![^>]*application/ld\+json)(?![^>]*src=)` 匹配，**没排除 `application/json`**，把关系图数据块当 JS 解析，报 3 个假 FAIL。数据块要在 JS 检查里显式分流到 JSON.parse。
- 验证: node 复核 9 文件 **36 段内联脚本 + 12 个 JSON 块全过**，div 配平（25/25、22/22、322/322）；canvas 实测 92.3% 非白像素、`stage.dataset.sn2==="1"`。**门禁只在我点名时才跑**（用户明确要求，之后我自己起的一次全量门禁已被叫停）。
- 分支 `dev`；未 commit、未 push。

---

## 2026-09-30 23:20 — 关系图：卡片脱离 720px 文字栏 + 78 个标签不再糊成一团
- 用户要求: ①「system.html、system-graph.html 跟技术概览直接去拼一下」②「这个审美崩溃了，也不符合我的设计体系」③「你截个截图看看，左右两边有白斑」
- 白斑的真正成因（先量后改，**不是 bug，是布局规则用错了地方**）: `.block-inner` 按 DESIGN §6「Key measurements」限宽 720px，于是卡片实际 672px，落在 1425px 的页面正中 —— 左右各 352px 空白。对**正文**这个栏宽是对的，对一张 1440×920 的画布就把图压成了一枚邮票。
- 依据: DESIGN §7.7 已经写过同一条道理 —— 宽组件绝不能待在 `.container` 里，「its max-width/padding would leave white strips on both sides」。关系图是同一个情形，只是当年没被登记为组件。
- 改法: 关系图页的 `.block-inner` 放到 **1200px**（DESIGN 导航壳层同宽），`h2` 与副标题仍留在 720px 文字栏 —— 长标题该量的地方继续量，卡片本身做视觉锚点。实测两侧空白 352px → **170px**，画布 606px → **1086px**。该页三语各只有一个 `.block-inner`，无 id 限定也安全。
- 审美崩溃的第二个成因: 标签层对 **78 个节点无条件全画**，默认视口下全部挤在约 600px 里叠成一团蓝字糊。改为三档 —— 悬停/选中的节点及其邻居必画；闲置时只画 **14 个最高连接度节点**（度数降序、id 兜底平局）当骨架；其余只画球，名字等悬停。复用 hover 已经算好的 `nbr` 邻接表，没多存状态。**确定性**：无随机，每页每次加载标签集合一致。
- 验证: 悬停 `Resume`（度数 25）→ tooltip 出现、邻居点亮并全部带名、cursor 变 pointer；点击 → 面板显示 h3 `Resume`、语言徽章 `Python`、25 条关系；暗色下整图重绘正常；其余两语结构一致。node 解析 36 脚本 + 12 JSON 全过、div 配平。**未跑门禁**（用户要求只在他点名时跑）。
- 待办: 「三个页面拼一下」这一条**还没做**，需要先跟他确认「拼」是指内容合并、还是互相串联导航 —— 我没擅自改页面结构。
- 分支 `dev`；未 commit、未 push。新增辅助脚本 `.fix_graph_width.py` / `.fix_graph_labels.py` 仍未跟踪。

---

## 2026-09-30 23:55 — 更新文档 + 把体系三页与技术概览真正拼成一套
- 用户要求: ①「更新所有文档啊，然后再去搞」②「刚才那个网站，我说合并你还没搞定」
- 先补文档（上一轮欠的账）:
  - `FENGMEM.md` 补上两轮缺失记录（SyntaxError 白屏事故轮 + 关系图宽度/标签轮）。
  - `DESIGN.md` 新增 **§6.1「When the 720px measure yields (full-bleed card)」** —— 这是本轮**偏离了 DESIGN 原有默认值**，所以必须登记成规则而不是只改代码。写清了判据（单内容块、以看为主）、做法（`1200px` + `h2`/副标题留 `720px`）、以及为什么症状读起来像「白斑」。Key measurements 表加了一行指向 §6.1。
  - `docs/guide/pitfalls.md` 新增 **§15**（一个 `<script>` 任何一处语法错 = 整块不执行，附症状对照表和 node 校验命令）与 **§16**（画布页别套 720px 文字栏 + 标签不可无脑全画）。
- 「合并」的实际情况（先量后改）: 三页本来**互相都链了**，但不一致 —— `system.html` 只有体系内一跳、没有第二行；两个叶子页各带**两个** link-card（体系 + 「继续往下看」），视觉上就是那段松白缝。`tech.html` 是四页里**唯一谁都不链**的：所有页都通到它，它通不到任何一页。
- 改法（三语 ×4 页 = 12 文件）:
  1. `system.html` 补上叶子页本来就有的第二行，凑成一致的两步走：先体系内，再出到 tech/invest/blog。
  2. 叶子页两个 link-card **并成一个、两个 cta-row**，链接文字与顺序全部沿用盘上原有。「继续往下看」那句随第二张卡一起消失 —— 它只是在复述下面按钮已经说的话。实测卡片高度 2×216px → 281px。
  3. `tech.html` 补一条回体系的路。tech 原本只有一枚裸 `<a>` 没有 `cta-row`（别的三页都有），所以新链接连同 `cta-row` 一起加，把原来的 invest 链接**移进**容器而不是撂在上面。invest 一行原样保留（同 class、同箭头、同位置）。
- 验证: 12 文件 div 深度全 0；node 解析 **39 段内联脚本 + 15 个 JSON 块全过**；浏览器实测 link-card=1 / cta-row=2、五个链接路径全对；按钮等宽 240px，system 系 51px、tech 系 74px（英文长句换行，同行等高，**不触 `btn-height`**）；链接图三语一致，tech 不再是死端。**未跑门禁**（用户要求只在他点名时跑）。
- 自己的事故（记下来）: `.stitch_pages.py` 第一版用**重复写四次的 `\t`** 拼正则，而 `\t` 在某些写入路径下会变成字面反斜杠+t，于是**正则看着完全正确却一个都不匹配** —— 脚本第一版崩在中途，而它**已经把 zh-cn/system.html 写坏了一半**（吃掉了体系卡的 `</div>`、又多插了一张卡）。修了两次才补平，最后用**从文档开头数 `<div>`/`</div>` 的净深度**当断言（zh-cn 一度是 -1）才把结构验对。
  - **教训 1**：写这类一次性改 HTML 的脚本，**断言必须基于不依赖正则的结构量**（标签净深度、元素计数），正则只是定位手段，不能同时当验证手段。
  - **教训 2**：脚本**必须幂等**，且崩在中途时要能自愈 —— 第二版按 `link-card` 计数分流（已有就跳过），所以重跑才安全。
  - **教训 3**：`src.count("link-card")` 会把 CSS 里的 `.link-card` 一起数进去（一度报 5），要数的是 `<div class="link-card">`。
- 分支 `dev`；未 commit、未 push。新增脚本 `.stitch_pages.py` / `.stitch_tech.py` 未跟踪。

---

## 2026-10-01 03:10 — 三页合一落地：tech.html + system.html + system-graph.html 合成一页（三语）
- 用户要求: 「我是让你把这3个东西用合理的方式合并到一个页面里面去」—— 不是互相串联导航，是**合成一页**。此前只做了串联，没做合并。
- 用户已定的两个决定（AskUserQuestion，已告知后果后确认）:
  1. **主 URL = `tech.html`** —— 它身上挂 51 处入链 / 33 个页面 + 5 条重定向（`/tech` 302、3 条历史 `/portfolio.html` 301），选它意味着 51 处链接一行不用改写。
  2. **删掉 `system.html` / `system-graph.html`，不留任何重定向规则** —— 后果是 `/{lang}/system` 与 `/{lang}/system-graph` 直接 404，用户明确接受。
- 合并结果（15 个内容块）: 快照 hero → `#domains` → `#method` → `#net` → card-grid（3 旗舰项目）→ tech 原有 12 块 → 合并后的 link-card。
  - **只留一个 h1**（system 的 hero）。建第二个 `.marketing-hero` 会在页面中段开 92px 空带，就是最初那个「白斑」。tech 的「技术」降级为 `#domains` 的 h2。
  - **1200px 按块放开，不按页放开**: `#net .block-inner{ max-width:1200px; }`，其余 14 块保持 720px。全局放开会破坏 DESIGN §6 的文字栏。`#domains` 不放开（SVG viewBox 自适应）。
  - **`.content-block{ scroll-margin-top:76px }` 是功能性必需**：tech 有 8 处 `scrollIntoView` 却没这条规则，合并前靠卡片够高侥幸没被固定导航栏盖住，合并后区块相邻丢了它 9 张卡全部点进导航栏底下。实测 8 个目标全部落在 76px，导航栏 44px，余量 32px。
  - reveal / rail / progress 各只留一份；`fx-rail` 建成静态 3 项（`#domains`/`#method`/`#net`）。`sn2Data` 逐语言分别取（en 23027 vs zh-cn 15227，跨语言复制是静默的）。
- 导航改动: `assets/js/shared-subpage-navbar.js` 删 4 行模板（桌面 submenu 2 + 移动 drawer 2）+ 12 个键（`system`/`systemHref`/`systemGraph`/`systemGraphHref` × 3 语言）；保留 `systemProjectsHref`（那个页面还在）。
  - **cache-bust 全站 bump** 到 `26.10.01.01.00`（1331 个文件）：改共享 navbar 就必须全站 bump，否则每个页面都在发带死链的旧导航。原先全站并存三个版本串（712 + 625 + 3），只改 3 个合并页会留下 1334 个页面发旧导航。
- 其他: `system-projects.html` ×3 删掉指向被删两页的整条 cta-row，caption 改「78 个项目，往下看」；`sitemap.xml` 删 6 个**完整 `<url>` 元素**（628 → 622，minidom 验证良构）；`_redirects` 不动（实测零引用）。
- 产出: `.merge_tech_system.py`、`{zh-cn,zh-hk,en}/tech.html`（合并后）、删 6 个文件、`shared-subpage-navbar.js`、1331 个文件的 cache-bust、`system-projects.html` ×3、`sitemap.xml`、`DESIGN.md` §6.1、`docs/guide/pitfalls.md` §16 改写 + 新增 §17、`docs/notes/NOTE-三页合一-2026-10-01.md`
- 关键决策:
  - **安全网必须是结构量和位置量**（标签净深度、id 唯一、`<style>` 是否在 `<head>` 里），不能是正则内容匹配，也不能是靠嵌套深度的遍历。本次 7 个 bug 全是「惰性正则 / 偏移算错 / 插错位置」这一类，naive 脚本会把它们当成正常页面推上去。
  - **`str.replace` 找不到就原样返回且不报错** —— 这是前两个合并 bug 的共同根因。凡是 replace 之后要断言的，一律先断言 needle 存在且唯一。
- 踩坑（已写进 `docs/guide/pitfalls.md` §17）:
  1. **`<style>`/`<script>` 是纯文本不是标记**，深度遍历必须在这两种标签处直接停。本次在 `tech.html` 上一次吞掉约 9KB 正文。
  2. **源文件本身就有没闭合的 `<style>`**：`tech.html` 的 `<head>` 里 3 个 `<style>` 开、2 个 `</style>` 闭 —— img-caption 那张表开在 prefers-reduced-motion 表**里面**，共用一个闭合标签（`git show HEAD:zh-cn/tech.html` 可复核，**早于本次改动**）。按嵌套切会留下没闭合的表，**它会把后面所有内容当纯文本吞掉**，包括刚注入的合并样式表。
  - 两者叠加的症状极具误导性：合并后的 `<head>` 里出现 `<style><style>`，浏览器把内层标签之后的一切当纯文本，**整张样式表静默失效** —— 页面照样渲染，只是画布缩回 720px、左右白斑回来。`check_site.py` 全绿，因为 CSS 语法没错，错的是它在文档里的**位置**。
  - **判据：拼样式表不能只验「内容在」，要验「在 `<style>` 里面」** —— 拼完直接问浏览器 `document.querySelectorAll('style')` 的 `.textContent`，比正则可靠也比正则快。
- 验证（**未跑门禁**，用户要求只在他点名时跑）:
  - 浏览器实测三语 × 明/暗 × 1440/375：`#net .block-inner` = 1200px、白色 stage 卡 = 1086px（1440 下）；两侧是 section 自己的浅灰 `#f5f5f7`，**不是白斑**。画布墨迹 bbox 左右各留 11%（zh-cn）/ 26%（en），差的是力导向布局的自然散布不是渲染故障。
  - 移动 375px：`scrollWidth - innerWidth = 0`，无横向溢出；`.fx-rail` 按设计在 <1280px 隐藏。
  - 三语 fetch 回来做 DOM 比对：15 个块的 id 序列**完全一致**（parity）、h1 各 1、id 零重复、div 128/128 配平、`application/json` 全过。
  - 计数器到 1,432,605 / 78 / 11；暗色下 stage `rgb(15,23,42)`、标签可读。
  - 工具本身不稳：`computer screenshot` 反复超时或给出过期缩放面（视口实测 1440×900 但截图是 800×505 的放大面），最后改用**数值测量**（getBoundingClientRect + canvas getImageData 求墨迹 bbox）作为证据 —— 比截图强。
- **提交时踩的一个坑（已修）**：`0507c9d1` 的 commit message 写了「cache-bust 全站 bump 到 26.10.01.01.00」，但 `git add` 只加了 `assets/js/shared-subpage-navbar.js` 一个文件 —— **1331 个 HTML 的 `?v=` 一个都没进去**。是 merge master 之后 `git status` 仍有 715 个 modified 文件才发现的。补了一笔 `b0d2c00a`。**教训：commit message 描述的范围必须和 `git show --stat` 对得上**；批量改动先 `git status --short | wc -l` 数一遍再 add。

- 分支 `dev`；已 commit 并 push 到 dev（GitHub + Gitee）。master 的 4 个提交此前未合入，已按 pitfalls §13 合并（无冲突，无文件重叠）。辅助脚本 `.merge_tech_system.py` 等 15 个 `.py` 与 `.merge_backup/` 仍未跟踪（不进版本库，留作恢复路径）。
