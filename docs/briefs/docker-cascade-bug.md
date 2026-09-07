# brief — docker-cascade-bug

①想法一句话:一个 0 字节的删不掉的 socket 文件能让整台引擎起不来,连修三处才见底——故障会级联,是因为代码里写了"清不掉就死";可靠是底线,底线要留活门。

②素材引文逐字(篇140_Docker Desktop在Windows Insider Build崩溃问题.md):
- L27:"Docker Desktop 4.71.0 and later (up to 4.82.0) crashes on startup on Windows 11 Insider Preview Build 26200. The Inference manager creates an AF_UNIX socket file on NTFS, which becomes corrupted and unremovable after any unclean exit, causing a permanent crash loop."(issue 原文)
- L37:afd.sys 对 NTFS 上 AF_UNIX socket 处理有 bug;非干净退出后 socket 文件 MFT 条目损坏。(后经复核更像 reparse point 孤儿化,见 L224-238)
- L52:"Cleaning one corrupted socket exposes the next."(issue 原文,级联句)
- L52 上下文:dockerInference → engine.sock → userAnalyticsOtlpHttp.sock 三连。
- L69:彻底 workaround=降级 4.69.0(build 224084),该版本关 Beta 功能即完全禁用 Inference manager;L60:EnableDockerAI:false 被默认 admin provider 覆盖(开关摆设);B.md E1:重命名父目录可行(目录能改名而内容不能触碰)。
- L282:error 1920(0 字节 ReparsePoint 文件无法删除)。
- L211:4.82.0(2026-07-13)release notes 只修 Mac/Linux socket 路径长度,Windows NTFS 坑没提;issue 已转 docker/desktop-feedback,#527。
- L224(用户质疑):"原作者把根因归到 afd.sys + NTFS MFT 条目损坏,这个描述里有几处是跳步甚至误诊的"→ 更可能是 reparse point 孤儿化。(对已提交 issue 的自我复核)

③对手戏回合表:
| 回合 | 用户 | AI |
|---|---|---|
| R1 | 贴 issue #527:解释一下这个 bug(L144) | 提炼因果链:Inference→NTFS socket→afd→MFT→remove() 失败→崩溃循环(L144-145) |
| R2 | 质疑 root cause:MFT 损坏是不是误诊?(L221) | 分层拆:方向对(afd×NTFS reparse),MFT 是误诊,更像 reparse 孤儿(L224-259) |
| R3 | (自我复核成立)issue 的诊断有一版是错的 | 确认:删不掉该降级不该 fatal;settings 关不掉那段对(L265-267) |

④方法:工程笔记体/时间线;数字去向(三个 socket 依次);立破成藏于自我复核段。
⑤气质:察为主,断收口;不骂人身,骂机制(开关是摆设)。
⑥形状:工程实录,~950 字。
⑦不适用边界:不谈 Docker 优劣、不谈容器技术本身;这是 Windows AF_UNIX×NTFS×可选组件设计三个问题叠加,不能推广成"Docker 不行"。
