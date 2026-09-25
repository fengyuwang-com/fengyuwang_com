# 通宵/定时任务管线（Overnight Task Pipeline）

> 任何 AI 接到"通宵任务/定时推进"类站长令，读本文件即可开工。源自 2026-09-12/13 博客清理通宵实战（台账：`docs/notes/博客清理-执行台账.md`）。

## 0. 站长令解析（开工前 5 分钟）

- **目标句式**：`/goal + 目标 + 提醒节奏 + "你全权负责 不得问我"`。全权授权 = 所有内容/代码决策自主；**不覆盖 AGENTS.md 红线**（不碰 master、不 push main、不动 assets/、不 commit 密钥）。
- **先落台账再动手**：建 `docs/notes/<任务名>-执行台账.md`，顶部写四要素——站长令原文、依据文档、铁律声明（只推 dev 等）、**DONE 判据**（可验证的完成条件，供定时任务自检自删）。
- **建定时自动化**（用户要求"每 N 分钟提醒"时）：CronCreate，prompt 要点见 §4。

## 1. 核心纪律（实战验证过）

1. **todo.md 是唯一真相源**：每轮唤醒先读 todo，断点未完先接着做，不重开新题；做完即勾，暂不做的记欠账条目，不口头承诺。
2. **台账是执行账本**：每个阶段（S1/S2/…）条目化，完成即 `[x]` + commit 哈希；新发现的问题**当场入账再修**，不许"顺手改了不记账"。
3. **每阶段收口动作固定**：hugo build + deploy.sh → `python3 tools/check_site.py --no-dark` 全绿 → commit → push dev。**阶段不绿不提交**。
4. **写文案前重读 `voice-and-translation.md`**，不凭记忆（教训：卡片 h3 写成名词标签被打回）。
5. **批量修改先 dry-run 列样本人工核**，再全量 apply；apply 后抽样 diff 复核。
6. **rebase/合并后必须 `git show` 验证关键文件仍在**，不能只看哈希（事故：文章提交被 rebase 静默丢弃，靠站长肉眼发现）。
7. 门禁检不出的盲区要**手动清单补扫**（例：opencc s2hk 对 戶/户 互穿，检不出「户」；字形标准 説≠說）。

## 2. 标准阶段骨架（按任务裁剪）

```
S0 审计/盘点   —— 依据文档（如 AUDIT-*.md）逐条列清单入台账
S1 删除/下线   —— 先列清单后动手；hugo build + check 全绿才 commit
S2 重写/修补   —— 逐篇过规范（--article 必过）；三语齐备才转正
S3 批量修补    —— 脚本先 dry-run；逐字类替换用"密文清单+opencc"双保险
S4 收尾       —— 全量 check_site（含暗色）→ 台账标 DONE → todo 勾清 → 短报告站长
```

## 3. 收尾协议（DONE 时刻）

- 全量 `check_site.py`（含暗色审计）**全绿**是 DONE 的硬条件，不绿不收。
- 台账顶部加 `## ✅ DONE（日期）` 一段：一句总账 + master 未动声明。
- 定时自动化**删除自己**（CronDelete；写 prompt 时就写明"台账顶部见 DONE 即自删"）。
- 给站长的终报固定三段：总账（干了什么，带 commit 哈希）/ 留给站长决策的挂账 / 红线状态（master 未动）。

## 4. 定时自动化 prompt 模板要素

- 每轮开工必读：todo.md（断点）+ 台账（进度）+ 依据文档。
- "按台账勾选状态找到第一个未完成步骤继续推进"。
- 阶段门禁句式："每阶段 hugo build+deploy.sh+check_site 全绿后 commit 推 dev，绝不碰 master"。
- 收尾句式："若台账所有条目完成且最终全量 check_site 通过，完成收尾并简短汇报；台账顶部标 DONE 后删除本条定时任务。"
- 节奏参考：20 分钟适合审计处置/批量修补类；30 分钟适合写作类（每轮 3 篇+审读）。

## 5. 本次实战沉淀的技术教训（跨任务复用）

| 教训 | 处置 |
|---|---|
| Hugo `.Site.RegularPages` 按日期排，"同标签取前 N"= 取最新 N 篇 | 相关阅读用 `[related]` 倒排索引 + `.Related` |
| Goldmark `**"` 紧邻引号开不上 `<strong>` | check_site `mdbold` 门禁（--article + 全量） |
| opencc s2hk 检不出 户/价/谁 等纯简体（映射互穿或阈值>3） | 密文清单直接 `str.count` 补扫 |
| zh-hk 新文禁「」禁粤语口语；説≠說、裏/裡 口径 | 见 voice-and-translation.md |
| git push 408 中断 | 原样重试即可 |
| 全量暗色审计耗时数分钟且易被打断 | `run_in_background` 跑，结果落 /tmp 日志 |
