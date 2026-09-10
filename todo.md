# todo — fengyuwang_com

## 待办队列（需站长决策）

- [ ] GitHub 悬空提交清理：Open-FengMedia 旧提交（含 FENGMEM.md，997b3ae / 7a3a680）与 Open-FengOffice 旧历史（含 HR 姓名邮箱，旧头 8243ac3 / 初始 0674b73）强推后仍可按 SHA 直达，彻底清除需站长向 GitHub Support 提工单（可同单）
- [ ] FengMedia 私仓分叉：GitHub master=5ca356e（总纲/AI丰林章程/丰林人格.md）与本地 db0f2f5（prompt工坊/5部新视频）互相有独有提交；且本地 push remote 指向 Gitee。需站长决定收敛方式（Open 镜像当前=本地 db0f2f5 口径）
- [ ] 私仓跟踪 FENGMEM.md（会话记录）有再泄漏风险：FlyGo / FengOffice / FengOrchestrator 均在 git 跟踪里，未来全量同步可能重演 Open-FengMedia 泄漏；建议各私仓 git rm --cached + gitignore（私仓操作待站长批准）
- [ ] Open-FengMedia 镜像 main（默认分支，落地 README）与 master（同步分支）双分支并存，是否合并/切默认由站长定
- [ ] Open-FlyGo Release 暂只有源码（flygo.exe 内嵌 365 处编译机路径已连历史剔除）；干净重编译（cargo --remap-path-prefix）后可附回二进制
- [x] CF Web Analytics 占位符已解决（2026-09-11: 60 处占位 beacon 删除, 统计由 Pages 项目开关自动注入, 后台已有数据）
- [x] 内部文档同步改名（2026-09-12 定时审计完成）：DESIGN.md / README.md / docs/guide/{WRITING,pitfalls,page-structure,release-gate}.md / _scripts/{uam,fix-seo-descriptions}.py 全部换 "Feng Human-in-the-Loop" 与 human-in-the-loop 路径；fix-seo-descriptions 失效键已修；docs/archive/ 按历史档案保留原文不改

- [x] 全站字号体系深审第一期（2026-09-12 定时审计）：h2/h3 字号声明纳入 key-selector 门禁（审计时全站已合规，0 违规，规则防新增页回归）；正文 p 与颜色清单待第二期
- [ ] 首页 index.html hero 结构一致性（slider-caption 等）纳入门禁（page-elements 已覆盖子页 10 项）
- [ ] 暗色模式人工抽检实战块：human-in-the-loop 页新增的实战块暗色对比已过门禁，建议站长肉眼复核一次观感

（第 13 轮站长令：接下来一律只推 dev，未经批准不碰 master；每小时定时任务按本清单继续）

## 定时写作任务（2026-09-12 站长令：每 15 分钟唤醒，每轮新写 3 篇博文，查重后从语料挖新主题）

- [x] 第 1 篇 macau-casino-fallacy《百万曹公，救不了赌场》三语齐备：brief 见 docs/briefs/，--article 校验过、gate 全绿，已推 dev。语料源 deepseek/raw/962dbd5f（澳门博彩辩论）；顺带修了 zh-hk-simp 检查器对正体「稅」的误报（s2hk 误映射到简体时不再计为泄漏）
- [ ] 第 2 篇（断点）：语料高命中候选——黄金(9041)/汇率(5007)/复利(4005)/杠杆(10759)/保险(14506)，需读上下文定题并对照查重清单；杠杆注意与 do-the-math/quant-paradigm-shift 查重
- [ ] 第 3 篇（断点）：同上，从黄金/汇率/复利/保险里挖未写过角度；二手车(595)、装修(3532) 备选

（第 11 轮站长拍板：除上述外其余待办等日后举措）

## 已完成（2026-09-07 第 12 轮：站长令——上线主线生产）

- [x] dev → master 合并推送（merge commit 886635c，GitHub+Gitee 双推确认）：上线 dev 全量约 57 个提交——FlyGo 专题页+Open 镜像链接、首页改版、博客多批次、全站搜索、暗色对比度修复；合并前全站门禁全绿（EXIT=0），合并树与 dev 完全一致；Cloudflare Pages 自动部署
- [x] 顺带收编 master-ahead-of-dev 残留：远端 master 独有 652c368（relicense，LICENSE 与 dev 同 blob）经合并自然归位，master/dev 不再分叉

## 已完成（2026-09-07 第 11 轮：站长拍板——email-classification.md 第三方 HR 姓名邮箱脱敏）

- [x] Open-FengOffice docs/email-classification.md 脱敏（站长拍板「取消掉」）：3 个 HR 个人邮箱（vincci@… / recruitment.globalhr@… / thomas@dayuse…）+ 8 个人名 →【已脱敏】，git filter-repo --replace-text 全历史重写，强推 master 8243ac3→feef33a，GitHub 现文件验证 0 命中；文档本体（四级分类体系）保留，README/CLAUDE.md 引用不断链；公司系统邮箱（Webull/OKX/Ollama 等公开企业地址）非个人隐私，保留。**⚠️ 未来从私仓同步此文件必须重做同样脱敏**
- [x] 网站状态核实：dev=8f47440 已推（flygo×3 链 Open-FlyGo），全站门禁全绿 EXIT=0，master 未动

## 已完成（2026-09-07 第 10 轮：Open 镜像体系——站长拍板"建 Open-FlyGo + 其余 Open 全量同步"）

- [x] 新建 github.com/fengyuwang-com/Open-FlyGo（public）：184 跟踪文件→165，剔 21 项（真实激活码×2、私人 tailnet 主机名、FengInvest 持仓盈亏截图×3[财产红线]、FENGMEM.md、AI 交接记录×3、flygo.exe[365 处 C:\Users\a8881]）；商业计划书.md 审查后保留（纯策略模型，无财产数字）；Release v2026.09.07-0130 可解析；exe 连 git 历史一并剔除（main=6e2586e）
- [x] 同步 Open-FengMedia（master=536322c，+1937 文件）：prompt工坊23任务/5部新视频项目/WebUI改版进镜像；剔 FENGMEM.md×3、会话转储 _tmp_user_cn.txt、B站登录二维码×2；**发现 8-23 初始提交曾把 FENGMEM.md 推上公开仓（暴露约两周）→ git filter-repo 清洗历史 + 强推归零**
- [x] 同步 Open-FengInvest（02d77e4，167 文件）：8-13 消毒快照→9-05 全部增量（BYOK Web UI、24 新工具、知识库）；剔 Discussion/16 文件、design/16 文件（会话记录+站长原话）、真实持仓数（"14 个"）、个人投资决策记录（research_list）；BYOK 配置确认零 key 实值；226 处本机绝对路径按既有惯例消毒
- [x] 核实 Open-FengOffice 已同步（凭据 accounts.json/credentials.md/.env 全 ignored，历史干净）；Open-FengOrchestrator 落后 2 提交 → 已补（e36519e，286 文件：263 角色库/cao-ceo skill/愿景蓝图；DeepSeek 余额 -0.03 数字剔除，本机路径脱敏）
- [x] flygo.html ×3 链接改指 Open-FlyGo（仓库+Release，对齐 fengmedia.html 链 Open 镜像先例）
- [x] 五个公开镜像当前树 + git 历史 secret/隐私双扫归零（Office/Orch 历史本来就干净）
- [x] 全站门禁全绿（EXIT=0，navbar/btn-height/dark 全过）→ commit → push dev（master 未动）
