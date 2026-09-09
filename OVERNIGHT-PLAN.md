# 通宵升级计划（2026-09-10 夜，站长批准）

> **本文件是通宵任务唯一真相源。** 每次唤醒：读本文件 → 按任务清单从上往下找第一个未完成任务 → 派子代理执行 → 验收 → commit → 在"进度日志"追加一行。全部完成后写"晨报"并停止开新工作。
> 站长原话目标：这个网站要变得非常好——软件介绍很多只有字没有图，素材里有图片可以盖上去；别的东西都要提升；本地 AI 对话导出文章里找可用素材。

## 铁律（违反即返工）

1. **分支**：只在 `overnight/2026-09-10` 上干活（先 `git checkout overnight/2026-09-10`）。**绝不 push / merge 到 master 或 dev**；本 overnight 分支在 check 全绿后允许 `git push origin overnight/2026-09-10`。
2. **门禁**：每次 commit 前 `python3 tools/check_site.py --no-dark` 必须全绿。
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
- [ ] **T0.1** bundle 回退（子代理）：删除 15 处无效 `oversight:"…"` 字段；把监督文案并入各层 `subtitle` 尾部（如 `subtitle:"定方向·控成本·守红线｜监督：签字（审批月度预算）"`，三语 15 处一一对应，简繁英各自措辞）。验收：`grep -o oversight …viewer.js | wc -l` = 0，`grep -c "｜监督" viewer.js` ≥ 5，JS 无语法破坏（node --check 或 hugo 构建通过）。
- [ ] **T0.2** 博文三语进 Hugo（子代理，1 个写 zh-cn，再派 2 个译 zh-hk/en）：基于理论文档压缩成 1500-2500 字《给 5DT-PD 立一块墓碑：从人机协作七十五年到组织级缺口》（标题可润），必含：墓志铭段（呼应网站 5dt-pd.html 的墓碑）、理论谱系表（Parasuraman 2000 → RLHF/CAI → 过程监督 → 组织级缺口）、开源项目对照（LangGraph/CrewAI/AutoGen/Spec Kit）、本站框架定位。frontmatter 按规范，slug 英文，translationKey 一致。
- [ ] **T0.3** `cd hugo && hugo --gc --cleanDestinationDir && bash deploy.sh` + 门禁 + commit + push 分支。

### T1 软件页配图（站长点名最高价值）
- [ ] **T1.1** fengmedia.html 三语配图（子代理×3 或 1 个串行三语）：挑 2-4 张 fengmedia 截图做"产品截图展示区"（参考 flygo.html 做法：img/shots 引用 + alt + lazy + 暗色适配 + 不破坏白线结构；截图放对应介绍段落之后）。门禁 + commit。
- [ ] **T1.2** fenginvest.html 三语配图：同法，3 张图（desktop / report-narrative / mobile）分配到对应段落。门禁 + commit。
- [ ] **T1.3** fengoffice.html / search-king.html：用 aik 搜本地库找有没有可用截图素材（关键词如 "fengoffice 截图"、"search-king 运行"）；找不到 → 写进"晨间决策"（建议站长补图），不改页面。门禁 + commit（若有改动）。

### T2 文章挖掘（ai-export）
- [ ] **T2.1**（子代理）aik 多关键词检索（如 OPC/一人公司、人机协作、AI 编辑器、求职自动化、投资复盘），产出 **≥10 条候选博文**（标题 + 3 句话大纲 + 素材出处文件:行号），写入下方"附录 A"。
- [ ] **T2.2**（子代理）挑最有把握的 1-2 条写成三语博文，**draft:true**（草稿态，晨审后才发布），进 Hugo 但构建后确认草稿不出现在产物里。
- [ ] **T2.3** 门禁 + commit + push 分支。

### T3 全站体检
- [ ] **T3.1**（子代理 + 主代理修）跑全量 `python3 tools/check_site.py`（含暗色审计）：FAIL 逐个修，PASS 但有 warning 的记录。
- [ ] **T3.2**（子代理）软件四页 + mkt/capabilities 的 meta description / OG 标签完整性、死链、alt 缺失扫描；小问题直接修，大问题记录"晨间决策"。
- [ ] **T3.3** 全部任务完成后写"晨报"。

## 进度日志（每次唤醒追加，格式：`[HH:MM] 完成… / commit abc123 / 下一手…`）

- [setup] 计划创建；改名批次（Q5×2 页三语 + 墓碑×三语 5dt-pd.html）已在工作区，随首个 commit 进 overnight/2026-09-10 分支。

## 晨间决策（夜里不拍板，留给站长）

-（空）

## 晨报

-（待全部完成后写）

## 附录 A：候选博文清单（T2.1 填）

-（空）
