# todo — fengyuwang_com

## 待办队列（需站长决策）

- [ ] GitHub 悬空提交清理：Open-FengMedia 旧提交（含 FENGMEM.md）强推后仍可按 SHA 直达（997b3ae / 7a3a680），彻底清除需站长向 GitHub Support 提工单
- [ ] FengMedia 私仓分叉：GitHub master=5ca356e（总纲/AI丰林章程/丰林人格.md）与本地 db0f2f5（prompt工坊/5部新视频）互相有独有提交；且本地 push remote 指向 Gitee。需站长决定收敛方式（Open 镜像当前=本地 db0f2f5 口径）
- [ ] 私仓跟踪 FENGMEM.md（会话记录）有再泄漏风险：FlyGo / FengOffice / FengOrchestrator 均在 git 跟踪里，未来全量同步可能重演 Open-FengMedia 泄漏；建议各私仓 git rm --cached + gitignore（私仓操作待站长批准）
- [ ] Open-FengMedia 镜像 main（默认分支，落地 README）与 master（同步分支）双分支并存，是否合并/切默认由站长定
- [ ] Open-FlyGo Release 暂只有源码（flygo.exe 内嵌 365 处编译机路径已连历史剔除）；干净重编译（cargo --remap-path-prefix）后可附回二进制
- [ ] Open-FengOffice docs/email-classification.md 含第三方真实姓名/邮箱（招聘方 HR）与站长求职痕迹，非红线、初版就有，如需保守可后续脱敏
- [ ] CF Web Analytics 仍是占位符 token（check_site [config] 节长期 PASS 提醒项）

## 已完成（2026-09-07 第 10 轮：Open 镜像体系——站长拍板"建 Open-FlyGo + 其余 Open 全量同步"）

- [x] 新建 github.com/fengyuwang-com/Open-FlyGo（public）：184 跟踪文件→165，剔 21 项（真实激活码×2、私人 tailnet 主机名、FengInvest 持仓盈亏截图×3[财产红线]、FENGMEM.md、AI 交接记录×3、flygo.exe[365 处 C:\Users\a8881]）；商业计划书.md 审查后保留（纯策略模型，无财产数字）；Release v2026.09.07-0130 可解析；exe 连 git 历史一并剔除（main=6e2586e）
- [x] 同步 Open-FengMedia（master=536322c，+1937 文件）：prompt工坊23任务/5部新视频项目/WebUI改版进镜像；剔 FENGMEM.md×3、会话转储 _tmp_user_cn.txt、B站登录二维码×2；**发现 8-23 初始提交曾把 FENGMEM.md 推上公开仓（暴露约两周）→ git filter-repo 清洗历史 + 强推归零**
- [x] 同步 Open-FengInvest（02d77e4，167 文件）：8-13 消毒快照→9-05 全部增量（BYOK Web UI、24 新工具、知识库）；剔 Discussion/16 文件、design/16 文件（会话记录+站长原话）、真实持仓数（"14 个"）、个人投资决策记录（research_list）；BYOK 配置确认零 key 实值；226 处本机绝对路径按既有惯例消毒
- [x] 核实 Open-FengOffice 已同步（凭据 accounts.json/credentials.md/.env 全 ignored，历史干净）；Open-FengOrchestrator 落后 2 提交 → 已补（e36519e，286 文件：263 角色库/cao-ceo skill/愿景蓝图；DeepSeek 余额 -0.03 数字剔除，本机路径脱敏）
- [x] flygo.html ×3 链接改指 Open-FlyGo（仓库+Release，对齐 fengmedia.html 链 Open 镜像先例）
- [x] 五个公开镜像当前树 + git 历史 secret/隐私双扫归零（Office/Orch 历史本来就干净）
- [x] 全站门禁全绿（EXIT=0，navbar/btn-height/dark 全过）→ commit → push dev（master 未动）
