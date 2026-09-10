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

## 定时写作任务（2026-09-12 站长令：每 5 分钟唤醒；子代理写正文、主代理选题/查重/主观审读/门禁/推送）

本轮（第 8 轮唤醒）产出：
- [x] 站长令补规（zh-hk 语体铁律）：粤语口语体不可接受——根因是规范只写"繁体+s2hk 字形"未禁口语体，子代理直接成文时把繁体写成了香港口语。已补进 WRITING-博文写作规范.md 第六节、voice-and-translation.md 翻译规则、定时任务 prompt（含审读逐句检查条款）
- [x] 第 19 篇 infra-legacy《泡沫死了，路还在》三语齐备：铁路电报光纤三笔遗产对照、铺路者不收费、九十年代 backbone 铺路对应 AI 算力扩产；语料源 doubao 补爬《穿越周期系列内容规划》_651714
- [x] 第 20 篇 top-bottom-signals《我不猜点位，我数信号》三语齐备：六个信号（人人荐股/新玩家涌入/估值锚失效/现金成贬/新词造富/从众替代判断）；信号数位置不数时间；可证伪收口；语料源同上
- [x] 第 21 篇 over-under-now《被高估的，被低估的》三语齐备：叙事密度尺子、被高估 4 项（纯概念/无壁垒上游/商业化预期/巨头估值）、被低估 4 项（被虹吸旧赛道/资源周期品/价值资产/加密）、产能过剩滞后性；语料源同上
- [x] 主观审读由专职子代理完成（依 WRITING v6.3 八问+素材围墙）：修回 8 处——围墙外杜撰（点位数字/天气比喻/现金流与巨头自有钱/国家的铁路网意象）、元话语泄漏（同一次辩论里最强的版本/但反方也该出场/本质上）、zh-hk over-under-now 粤语口语体整篇重写为书面繁体（光模組/伺服器 港式术语）；审读代理的「説→說」P0 经 OpenCC 实证驳回（s2hk 映射 說→説，站内字形以 説 为准）
- [x] 三篇 9 文件均过 --article（汉字 678/903/802 等）+ hugo 构建 + --no-dark 全绿，docs/briefs/ 三份 brief（含七要素+对手戏回合表）存档，已推 dev
- 下一轮候选（需查重）：英伟达三重嵌套周期（_651714）、达利欧债务周期事实核查、特斯拉盈利超预期、判断文章 AI 生成概率 _247042（与 ai-flip-flop 重叠风险需查重）

本轮（第 7 轮唤醒，首次子代理分工）产出：
- [x] 第 16 篇 silicon-cycle《亏钱也要生产的生意》三语齐备：硅周期 3-4 年/沉没成本→停产比降价更贵/2017-18 存储超级周期+2022-24 寒冬/2000·2017-18·2025-26 三轮结构性高峰对比/看开工率与扩产潮不看头条；语料源 doubao 补爬《穿越周期系列内容规划》_651714
- [x] 第 17 篇 narrative-rotation《没人讨论，才是底部的样子》三语齐备：减半周期+流动性双钟/2013·2017·2021 三轮同剧本/叙事轮动=每轮只有一个主线/注意力就是边际买家/被遗忘阶段=底部布局期；语料源同上 _651714
- [x] 第 18 篇 baijiu-dual-market《白酒也是一种周期品》三语齐备：消费+金融双轨合流互相点火/需求恒定≠没有周期（金融属性才是波动来源）/囤积程度+永恒叙事=周期化判据；语料源同上 _651714（站长口述白酒段）
- [x] 流程验证：主代理查重落 3 份 brief → 3 个子代理并行写三语 → 主代理审核（零痕迹/禁「」/s2hk 字形）→ --article 9/9 → 构建门禁全绿 → push dev
- 下一轮候选（同对话仍有富矿）：基建泡沫遗产（铁路/光纤闲置 vs 算力，泡沫死公司基建留下）、英伟达三重嵌套周期、高估低估清单（第 10 集）、周期顶底十信号（第 11 集）；另判断文章 AI 生成概率 _247042（与 ai-flip-flop 有重叠风险，需再查重）；达利欧债务周期事实核查、特斯拉盈利超预期待评估

本轮（第 6 轮唤醒）产出：
- [x] 第 13 篇 persona-as-contract《人设是一份还不完的契约》三语齐备：2011 隐形契约（交朋友/厚道定价=容错标准更低）、对标标签反困衣柜、亲民从习惯变 KPI、手机能蒙汽车蒙不过、SU7 沉默三天、机盖庭审法务撕掉"雷军承诺=小米承诺"、性价比悖论+生态链去小米化；语料源 doubao 补爬 md 雷军争议与小米商业模式深度解析（站长亲写 15 集大纲，idx=1 素材围墙）
- [x] 第 14 篇 four-nested-cycles《四种周期，一套嵌套》三语齐备：基钦库存 3-5y/朱格拉设备 7-11y/库兹涅茨地产 15-25y/康波技术 45-60y，嵌套 1:3:6:12，五轮康波史；嵌套的价值是定位不是预测拐点，时间颗粒度对齐操作层级；语料源 doubao/raw/38432075186195458.jsonl
- [x] 第 15 篇 ai-flip-flop《问它是谁写的，它就说是谁》三语齐备：同文两问两答翻转；三层机制（指令导向>事实判断/无鉴定模块/模糊语境折中迎合）；诚实的边界辩护只对一半；AI 检测工具基本不可信；语料源 doubao/raw/32903234445881346.jsonl
- [x] 三篇均过 --article（汉字 915/872/829）+ hugo 构建 + --no-dark 全绿（顺带把 ai-flip-flop zh-hk 的「說」统一为站内 s2hk 字形「説」），docs/briefs/ 三份 brief 存档，已推 dev
- 下一轮候选（未定题，需读对话定角度并查重）：穿越周期系列内容规划（doubao 38431623301651714，76 条消息，疑似富矿）、判断文章 AI 生成概率（doubao 32902193272247042，10 条，含"为了反对而反对"思辨讨论）、达利欧债务周期与价格规律事实核查、特斯拉盈利超预期后股价走势、粘滞信息（仍偏薄）、豆包 642 标题池继续挖

本轮（第 5 轮唤醒）产出：
- [x] 第 10 篇 quant-desymbolization《股票在量化手里只是筹码》三语齐备：去符号化（股票=筹码/管因子不管故事）、精密工厂三硬约束（流动性/成本/波动率）、散户三重降维打击（军备竞赛/利润不可触达/只学频率丢风控）、时间维度的套利=做农夫不做猎人；语料源 gemini/raw c_e39bd6bb25ecefa7
- [x] 第 11 篇 scaling-not-parameters《Scaling 不再是堆数字》三语齐备：Kaplan 2020 2.7:1 → Chinchilla 2022 每参数 20 Token → 推理成本入账 → MoE 总参数=记忆/激活=推理（记忆吃参数、推理吃数据）；GLM-5.3 同基座 753B/40B 53→60=控制变量实验；语料源 gemini/raw c_596c016b7ac55c99
- [x] 第 12 篇 production-creates-wealth《财富不是钱，是使你能赚钱的东西》三语齐备：生产=重新排列（渔夫/汽车/医生）、鲁宾逊渔网循环、分工与富足扩散、货币可印可蒸发 vs 生产不可没收、成功来自生产不是破坏；语料源 doubao/raw/20518930643854850.jsonl（《专业投机原理》生产创造富足）
- [x] 三篇均过 --article（汉字 1081/808/894）+ hugo 构建 + --no-dark 全绿，docs/briefs/ 三份 brief 存档，已推 dev
- 下一轮候选（未定题，需读对话定角度并查重）：粘滞信息 von Hippel（doubao 32673110770319362，素材偏薄仅 4 条消息，定义+创新发生在信息源头+领先用户，需评估）、雷军争议与小米商业模式（raw 缺失，仅 conversations_日常号_补爬 md，需确认正文）、四大经济周期梳理、无意义标点对 token 的影响（轻量趣味向）、豆包 642 标题池继续挖

本轮（第 4 轮唤醒）产出：
- [x] 第 7 篇 low-money-is-money《Low 的钱也是钱》三语齐备：PDD 低品牌经济学——审美是成本线、土味=筛选器/防御色、渣打 "Now it's your time for wealth"→"这次你一定要提现"、8 倍市盈率=Low 的价签、直面三反论；语料源 doubao/raw c_6d66dbcfb7abffbb
- [x] 第 8 篇 priced-in-new-york《港股的定价权，深夜在纽约》三语齐备：南向单季 2200 亿港元纪录但分化（红利股内资>50% 已夺权/科技股外资 40%+）、ADR 双胞胎套利、拼多多三重折价、中东主权资本+回购注销反制；语料源 gemini/raw c_78dc397b49188036（与上轮中概股同源不同层）
- [x] 第 9 篇 spread-not-direction《汇率涨跌都能赚的钱》三语齐备：找换店价差生意——摆摊的人不持仓、风险压缩到几分钟（库存周转+远期/期权对冲）、服务溢价+客户绑定、中间价平台追问=软肋反证、位置>眼光；语料源 doubao/raw/24499395430682114.jsonl
- [x] 三篇均过 --article（汉字 957/980/939）+ hugo 构建 + --no-dark 全绿，docs/briefs/ 三份 brief 存档，已推 dev
- 下一轮候选（未定题，需读对话定角度并查重）：大模型 Scaling 精细化运营（c_596c016b7ac55c99，用户原话仅一句，素材偏转述，需评估）、量化去符号化与精密工厂、豆包 456 对话再挖（找换店已用）

本轮（第 3 轮唤醒）产出：
- [x] 第 4 篇 financing-first-hk《融资全球第一，涨幅没得看》三语齐备：2025 港股 IPO 集资 374 亿美元(+231%, 全球第一)+再融资 660 亿；卖场/摊位费/导购结构；四路资金来路；"两个人抬价"价格错觉；语料源 gemini/raw/c_9f83157e34cea552（港股抽血对话，与 hold-is-buy 同源不同层）
- [x] 第 5 篇 rule-of-three《三个人做不出决定》三语齐备：2:1 联盟固化/决策僵局/责任稀释三裂缝；罗马后三巨头+苏联三驾马车三次对照；方案 A 分工制/方案 B 监督外置；语料源 gemini/raw/c_f7ffb9ad467508da
- [x] 第 6 篇 actuary-cant-predict《精算师也预测不了未来》三语齐备：Gen Re 石棉/卡特里娜/长护险/AIG/日本利差损 5-6% 预定利率翻车史；伯克希尔三池现金(60-70% 受限+200-300亿安全垫)；冗余>模型精度；语料源 gemini/raw/c_dca33b1d16148a36
- [x] 修正上轮错误记录：豆包语料并非"只有标题无正文"——raw/ 456 个 jsonl 全部含完整对话(约 700MB)，conversations/ 的 282 个 3 行空壳只是渲染成品缺失；找换店等豆包题材下轮可写
- 下一轮候选（未定题，需读对话定角度并查重）：找换店盈利模式（doubao/raw/24499395430682114.jsonl，价差+对冲+库存周转，正文已确认在）、大模型 Scaling 精细化运营（c_596c016b7ac55c99，用户原话仅一句，素材偏转述，需评估）、中概股低迷四大原因（c_78dc397b49188036）

（第 2 轮唤醒产出存档：
- [x] 第 2 篇 hold-is-buy《持有就是买入》三语齐备：评级分布（腾讯 42 买入/2 持有/1 卖出）、胜率 50-55% 公开可查、目标价 550 被打脸也要上调；语料源 gemini/raw/c_9f83157e34cea552（港股研报对话）。已推 dev 0a6d77ea
- [x] 第 3 篇 leverage-cant-buy-time《杠杆借不来时间》三语齐备：无限借钱投伯克希尔的永动机构想 → 利息每秒计提 vs 回报不均匀 + 30-50% 回撤 + 保证金平仓 + 体量天花板 → 不对称下注才是成功者的赌；语料源 gemini/raw/c_95dc01201c49d51b。已推 dev
- 注：豆包语料只有标题无正文（conv stub 3 行），不能当素材围墙；gemini/deepseek/yuanbao 是可用语料

- [ ] 下一轮候选（未定题，需读对话定角度并查重）: 港股抽血（c_9f83157e34cea552 同对话内的抽血/南向资金部分）、三人决策制的致命陷阱（c_f7ffb9ad467508da）、量化去符号化与精密工厂、大模型 Scaling 精细化运营、找换店盈利模式（正文缺，需先确认语料是否存在）
- [x] 第 1 篇 macau-casino-fallacy《百万曹公，救不了赌场》三语齐备：brief 见 docs/briefs/，--article 校验过、gate 全绿，已推 dev。语料源 deepseek/raw/962dbd5f（澳门博彩辩论）；顺带修了 zh-hk-simp 检查器对正体「稅」的误报（s2hk 误映射到简体时不再计为泄漏）
- [x] ~~第 2 篇断点（黄金/汇率/复利/杠杆）~~：已按 gemini 标题清单改道定题（hold-is-buy / leverage-cant-buy-time），命中率更高

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
