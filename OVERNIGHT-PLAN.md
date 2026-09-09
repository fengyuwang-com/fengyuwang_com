# 通宵升级计划（2026-09-10 夜，站长批准）

> **本文件是通宵任务唯一真相源。** 每次唤醒：读本文件 → 按任务清单从上往下找第一个未完成任务 → 派子代理执行 → 验收 → commit → 在"进度日志"追加一行。全部完成后写"晨报"并停止开新工作。
> 站长原话目标：这个网站要变得非常好——软件介绍很多只有字没有图，素材里有图片可以盖上去；别的东西都要提升；本地 AI 对话导出文章里找可用素材。

## 铁律（违反即返工）

1. **分支**：只在 `overnight/2026-09-10` 上干活（先 `git checkout overnight/2026-09-10`）。**绝不 push / merge 到 master 或 dev**；本 overnight 分支在 check 全绿后允许 `git push origin overnight/2026-09-10`。
2. **门禁**：每次 commit 前 `python3 tools/check_site.py --no-dark` 必须全绿。**唯一例外**：跨文件批次中间态（如博文三语翻译未齐时的 translationKey/deploy 差异 FAIL）允许带已知 FAIL commit，但必须在 commit 信息与进度日志中列明 FAIL 清单与消除条件；与本次改动无关的 FAIL 一律先修再提。
3. **子代理分工**（站长指令"一定要分子代理干"）：主代理只做派工、验收、git；文件编辑/搜索/写作/翻译一律派子代理，prompt 必须自包含（文件路径、规范要点、验收标准）。browser-use 浏览器操作不给子代理用。
4. **安全**：assets/ 只增不删；页面文件名保持英文不改 URL；绝不提交密钥/.env。
5. **风格**（AGENTS.md/DESIGN.md）：所有可见文字要有暗色显式覆盖（标题 #e5ecf4、正文 #9fb0c3/#94a3b8）；`.content-block` 是 page-wrap 直接子元素、白线靠 margin-bottom:12px 自然流出；文案 NO second-person、NO self-praise；zh-hk 用香港正式繁体；`<img>` 一律带 alt、加载 `loading="lazy"`。
6. **构建**：博客/Hugo 改动后 `cd hugo && hugo --gc --cleanDestinationDir && bash deploy.sh`，然后跑门禁。
7. **素材检索**：本地 AI 对话库用 `python3 ~/Documents/private-AIExport/tools/aik.py search "关键词"`（站长已授权；命中后 `aik read <文件> <行号>` 局部读）。
8. **不问问题**：拿不准的决策写进"晨间决策"区，继续下一项，不停摆。

## 关键地图（今天摸底结论，直接用）

- **软件截图素材**：`assets/img/shots/` 已有 11 张——fenginvest-desktop / fenginvest-mobile / fenginvest-report-narrative-desktop / fengmedia-desktop / fengmedia-home-desktop / fengmedia-projects-desktop / fengmedia-prompt-workshop-desktop / fengmedia-ai-draft-gate-desktop / fengmedia-mobile / flygo-desktop / flygo-mobile。无需外找。
- **配图参考实现**：`zh-cn/flygo.html`（已用 img/shots，grep `img/shots` 抄布局模式，三语同改）。
- **0 图软件页（本夜主目标）**：`fenginvest.html`（3 张 fenginvest 图可用）、`fengmedia.html`（6 张 fengmedia 图可用）、`fengoffice.html`、`search-king.html`（无对应截图 → 只记录，不硬编占位图）。
- **Bundle 回退证据**：`assets/js/5dt-pd/5dt-pd-viewer.js` 中 oversight 出现 15 次（纯数据），subtitle 24 次、risk 35 次（数据+代码引用）→ 组件**不渲染** oversight 字段。
- **理论文档**（T0.2 博文原料）：`/Users/fengmac/Documents/FengOrchestrator/docs/理论谱系-荟萃研究.md`、`人机协作改进蓝图.md`。
- **博文规范**：`docs/guide/WRITING-博文写作规范.md`；Hugo 源 `hugo/content/{lang}/blog/posts/<中文目录名>/index.md`；三语同发、translationKey 一致、draft:false 仅限 T0.2（站长已批"进hugo没关系"），T2.2 新稿一律 draft:true。
- 本地预览服务器：http://127.0.0.1:8080 （已在跑）。

## 任务清单

### T0 收尾上一批（HITL 改名 + 墓碑 + 监督列）
- [x] **T0.1** bundle 回退（子代理）：删除 15 处无效 `oversight:"…"` 字段；把监督文案并入各层 `subtitle` 尾部（如 `subtitle:"定方向·控成本·守红线｜监督：签字（审批月度预算）"`，三语 15 处一一对应，简繁英各自措辞）。验收：`grep -o oversight …viewer.js | wc -l` = 0，`grep -c "｜监督" viewer.js` ≥ 5，JS 无语法破坏（node --check 或 hugo 构建通过）。
- [x] **T0.2** 博文三语进 Hugo（子代理，1 个写 zh-cn，再派 2 个译 zh-hk/en）：基于理论文档压缩成 1500-2500 字《给 5DT-PD 立一块墓碑：从人机协作七十五年到组织级缺口》（标题可润），必含：墓志铭段（呼应网站 5dt-pd.html 的墓碑）、理论谱系表（Parasuraman 2000 → RLHF/CAI → 过程监督 → 组织级缺口）、开源项目对照（LangGraph/CrewAI/AutoGen/Spec Kit）、本站框架定位。frontmatter 按规范，slug 英文，translationKey 一致。
- [x] **T0.3** `cd hugo && hugo --gc --cleanDestinationDir && bash deploy.sh` + 门禁 + commit + push 分支。

### T1 软件页配图（站长点名最高价值）
- [x] **T1.1** fengmedia.html 三语配图（子代理×3 或 1 个串行三语）：挑 2-4 张 fengmedia 截图做"产品截图展示区"（参考 flygo.html 做法：img/shots 引用 + alt + lazy + 暗色适配 + 不破坏白线结构；截图放对应介绍段落之后）。门禁 + commit。
- [x] **T1.2** fenginvest.html 三语配图：同法，3 张图（desktop / report-narrative / mobile）分配到对应段落。门禁 + commit。（实际：发现 fenginvest-desktop.png 与 report-narrative 字节级相同，已删重复 figure，页面留 2 张）
- [x] **T1.3** fengoffice.html / search-king.html：用 aik 搜本地库找有没有可用截图素材（关键词如 "fengoffice 截图"、"search-king 运行"）；找不到 → 写进"晨间决策"（建议站长补图），不改页面。门禁 + commit（若有改动）。（实际：本地零命中；两者均为纯 CLI 无 GUI 可截，页面 0 img 自洽，不改）

### T2 文章挖掘（ai-export）
- [x] **T2.1**（子代理）aik 多关键词检索（如 OPC/一人公司、人机协作、AI 编辑器、求职自动化、投资复盘），产出 **≥10 条候选博文**（标题 + 3 句话大纲 + 素材出处文件:行号），写入下方"附录 A"。（实际产出 14 条 → 见 `OVERNIGHT-CANDIDATES.md`：高可信 8 / 中高 2 / 中 3 / 低 1；Top 2 =《一人公司带数百 AI 员工，翻译成工程语言就五层》《把投资纪律写成状态机：不懂即 PASS》）
- [x] **T2.2**（子代理）挑最有把握的 1-2 条写成三语博文，**draft:true**（草稿态，晨审后才发布），进 Hugo 但构建后确认草稿不出现在产物里。（实际：Top 1《一人公司带数百个 AI 员工，翻译成工程语言就五层》zh-cn 草稿完成，1774 汉字，素材出处 30+ 条真实行号；draft:true 构建验证不出产物。注意：草稿暂无 translationKey，翻译时需三语同加。）
- [x] **T2.3** 门禁 + commit + push 分支。（实际：随 cff3459 一并完成，门禁全绿）

### T3 全站体检
- [x] **T3.1**（子代理 + 主代理修）跑全量 `python3 tools/check_site.py`（含暗色审计）：FAIL 逐个修，PASS 但有 warning 的记录。（实际：全绿 0 FAIL 0 warning；暗色审计 472 页 0 问题；24 条 [skip] 为分页重定向壳预期跳过；唯一跟进项 = CF Web Analytics 占位 token，入晨间决策）
- [x] **T3.2**（子代理）软件四页 + mkt/capabilities 的 meta description / OG 标签完整性、死链、alt 缺失扫描；小问题直接修，大问题记录"晨间决策"。（实际：必修 0；修复 en description 压缩 ×6 + 失实 og:image 尺寸声明全站清除 53 文件含模板与 DESIGN.md，死链/alt/og 齐全性全过；建议补 1200×630 OG 卡片图入晨间决策）
- [x] **T3.3** 全部任务完成后写"晨报"。

## 进度日志（每次唤醒追加，格式：`[HH:MM] 完成… / commit abc123 / 下一手…`）

- [setup] 计划创建；改名批次（Q5×2 页三语 + 墓碑×三语 5dt-pd.html）已在工作区，随首个 commit 进 overnight/2026-09-10 分支。
- [T0.1✔] 子代理完成 bundle 回退：15 处 oversight 字段删除、监督文案并入 subtitle 尾部（简 5/繁 5/英 5），node --check 语法过，check_site --no-dark 全绿。
- [T0.1 commit] d23a257 已 push overnight 分支。
- [T2.1✔] 子代理完成 aik 挖掘：16 词检索 13 命中，14 条候选（高可信 8）写入 OVERNIGHT-CANDIDATES.md，Top 2 推荐 OPC 五层总纲篇 + 投资纪律状态机篇。T2.2 起草 Top 1（zh-cn，draft:true）。
- [T0.2✔ zh-cn] 博文原稿完成：hugo/content/zh-cn/blog/posts/给5DT-PD立一块墓碑——人机协作75年与组织级缺口/index.md（1559 汉字、slug tombstone-for-5dt-pd、translationKey tombstone-5dt-pd、draft:false、规范检查 OK）。zh-hk/en 翻译已派出。
- [T0.2 commit] 61888be zh-cn 原稿已 push。
- [T1.1✔] fengmedia 三语配图完成：4 张截图（home/ai-draft-gate/projects/prompt-workshop）插入对应段落 section-card 内，shot-figure 组件 + 暗色覆盖，div 配平 46/46、0 断链。check_site 仅剩 3 个中间态 FAIL（博文未构建/翻译未齐），按门禁例外规则 commit。
- [T1.1 commit] 1bb2083 已 push。
- [T0.2✔ 三语] zh-hk 翻译完成（1559 字逐字对应，港式用词 10 项经语料裁定：説/裏/復盤/函數/算法/賬/鏈接/摺合/羣/質量）；en 翻译完成（1444 词，五词术语英文化，首版括注中文触发 en-han 检查已删）。hugo 构建+deploy 完成，三语 tombstone-for-5dt-pd 已部署。
- [T2.2✔] OPC 五层草稿完成（draft:true，1774 汉字）。check_site 草稿原触发 [translate] 三语不齐——修复：摘草稿 translationKey + tools/check_site.py 第 2 节补 draft 跳过（与第 5 节先例一致，+2 行）。
- [T0.2/T0.3/T2.2 commit] cff3459 已 push，门禁全绿 ✔。T0 全部完成。下一手：T1.2 fenginvest 配图。
- [T1.2✔] fenginvest 三语配图：#architecture 配 report-narrative-desktop、#start 配 mobile（shot-narrow 竖版变体）；发现 fenginvest-desktop.png 与 report-narrative 字节级相同（MD5 3e3d77e0）→ 删重复 figure，页面留 2 张；晨间决策记录重导需求。commit 44a70af 已 push。
- [T1.3✔] fengoffice/search-king 素材检索：aik 本地库零命中，两者纯 CLI 无 GUI；不改页面，无图结论+终端演示图建议入晨间决策。记账 commit e57c156。
- [T3.1✔] 全量 check_site（含暗色）全绿：0 FAIL 0 warning，暗色审计 472 页 0 问题；24 条 [skip] = blog/tags 分页重定向壳预期跳过；跟进项 CF Analytics token 入晨间决策。
- [T3.2✔] 元信息审计+修复：18 页审计必修 0；en description 压缩 ×6（147-153 字符）；失实 og:image:width/height（声明 1200×630，实际 logo.png 30×30）全站清除——三语 53 个文件 + rebuild_pages.py 模板 + DESIGN.md（重跑脚本不再复发），og:image 本体全保留。死链/alt/lazy 全过。
- [T3.2 commit] b8dfa4e 已 push；快速+全量门禁双绿 ✔。
- [T3.3✔] 晨报已写入本文件，通宵任务全部完成。

## 晨间决策（夜里不拍板，留给站长）

- **fenginvest-desktop.png 需重导**：现文件与 report-narrative 字节级相同（同一张报告页截图）。建议重导一张真正的桌面端概览（首页/决策台视图）覆盖 `assets/img/shots/fenginvest-desktop.png`，之后在 fenginvest.html #quality 段把删掉的 figure 加回（三语同位置，版式 shot-figure 现成）。
- **OPC 草稿博文待晨审**：《一人公司带数百个 AI 员工，翻译成工程语言就五层》draft:true 已在库（1774 汉字，素材来自 FengOrchestrator 愿景对话真实行号）。晨审满意→三语翻译+发布；需要改→直接改 zh-cn 稿。候选清单另 13 条见 OVERNIGHT-CANDIDATES.md。
- **fengoffice / search-king 无图结论**：本地全路径检索零命中，且两者均为纯命令行工具（search-king 是 bash wrapper 起 scraper.py；fengoffice 是 CLI 邮件 + Twenty CRM Docker 栈），性质上无 GUI 截图可配。建议：跑一次真实命令截终端演示图（输出本身好看，如 search-king 多引擎回退链），页面图位版式可抄 fengmedia 的 shot-figure；或者接受无图现状（页面结构自洽）。Twenty CRM 界面图属第三方项目，需另行部署截取。
- **OG 分享卡片图缺真图**：全站 og:image 一直指向 logo.png（30×30），社交平台分享卡片效果差；本次已把失实的 1200×630 尺寸声明全部删除（53 文件+模板+DESIGN.md），元数据现在诚实但分享图仍小。建议制作一张真 1200×630 站点卡片图放 `assets/img/`，然后全站 og:image/twitter:image 换新（改一处模板 + 批量替换即可，rebuild_pages.py 模板已同步可改）。
- **CF Web Analytics 仍是占位 token**：check_site [config] 项提示。要启用统计就填真实 token；不打算用可忽略。

## 晨报

**通宵任务全部完成（T0-T3），分支 `overnight/2026-09-10`，全程未碰 master/dev。** 最终门禁：快速 `--no-dark` 与全量（含暗色审计）双绿。

### 做了什么（按 commit 链）

| commit | 内容 |
|---|---|
| bc659b8 | 上一批收尾进分支：Q5"和行业已有工作什么关系" chips（三语×2页）+ 5DT-PD 墓碑（三语 5dt-pd.html）+ 框架图监督数据 |
| d23a257 | T0.1 bundle 回退：viewer.js 15 处 oversight 死数据删除，监督文案并入五层 subtitle 尾部（三语）——组件本就不渲染该字段，信息零丢失 |
| 4fae5f7 | T2.1 aik 本地对话库挖掘：16 关键词 13 命中 → 14 条候选博文（`OVERNIGHT-CANDIDATES.md`，高可信 8 条） |
| 61888be→cff3459 | T0.2/T0.3 墓碑博文三语进 Hugo 并构建部署（《给 5DT-PD 立一块墓碑》，zh 1559 字/en 1444 词，理论谱系+开源对照+墓志铭）；en 括注中文触发 en-han 已清 |
| 9ba9182 | T2.2 OPC 五层草稿（draft:true，1774 汉字，素材 30+ 条真实行号）；check_site 补草稿跳过（与先例一致 +2 行） |
| 1bb2083 | T1.1 fengmedia 三语配图：4 张产品截图入对应段落（shot-figure 组件+暗色覆盖） |
| 44a70af | T1.2 fenginvest 三语配图：报告叙事+移动端 2 张；**发现 fenginvest-desktop.png 与 report-narrative 字节级相同**，删重复 figure |
| e57c156 | T1.3 收口：fengoffice/search-king 本地零素材且纯 CLI 无 GUI，无图结论入晨间决策 |
| b8dfa4e | T3.2 全站元信息修复：en 页 description 压缩 ×6；**失实 og:image 尺寸声明（1200×630 vs 实际 30×30）全站清除 53 文件**+生成脚本模板+DESIGN.md，重跑脚本不复发 |

### T3 体检结论

- 全量 check_site（含暗色 472 页审计）：**0 FAIL 0 warning**；24 条 [skip] 为 blog/tags 分页重定向壳的预期跳过。
- 18 页元信息审计：死链 0、alt/lazy 缺失 0、og 标签齐全。

### 交给站长的早晨清单

1. **晨审 OPC 草稿**《一人公司带数百个 AI 员工，翻译成工程语言就五层》（`hugo/content/zh-cn/blog/posts/一人公司带数百个AI员工——翻译成工程语言就五层/index.md`，draft:true）→ 满意就三语翻译+发布。
2. **重导 fenginvest-desktop.png**（现与 report-narrative 相同），之后在 fenginvest.html #quality 把删掉的 figure 加回（三语，版式现成）。
3. **决定 fengoffice / search-king 配图**：终端演示截图 or 保持无图。
4. **OG 卡片图 / CF Analytics token**：见晨间决策两条。
5. 另有 13 条候选博文在 `OVERNIGHT-CANDIDATES.md` 等排期。

## 附录 A：候选博文清单（T2.1 填）

-（空）
