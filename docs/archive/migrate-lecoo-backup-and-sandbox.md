# 迁移计划：Lecoo Backup + 沙箱→C:\FengProj / 家目录归位

> 状态：**计划稿**（用户将换新 session 执行；本 session 不执行破坏性迁移）
> 原则：Proj 是工作目录；除工作目录外不该有活跃工作；在用的文件夹一律不动。

## 目标
1. `Lecoo Backup\a8881\` 里的**家目录 dot-工具** → 归位到 `C:\Users\a8881\.{claude,codex,...}`
   （含 3.4G 的 `.claude`，这就是「claude 怎么还这么大」的原因）。
2. `Lecoo Backup\FengProj\` 快照 → 并入 `C:\FengProj`。
3. 沙箱 `fengyuwang_com`（本 session）→ 换 session 后迁到 `C:\FengProj\fengyuwang_com`。

## 现状（已核实）

### `Lecoo Backup`（现 8.0G，含 2 个子目录）
| 项 | 大小 | 内容 | 去向 |
|----|------|------|------|
| `a8881/.claude` | **3.4G** | Claude 完整 home（skills/plugins/sessions/commands/telemetry/server.log） | → `C:\Users\a8881\.claude` |
| `a8881/.openclaw` | 2.3G | OpenClaw 数据 | → `C:\Users\a8881\.openclaw` |
| `a8881/.codex` | 1.2G | Codex home | → `C:\Users\a8881\.codex`（谨慎合并） |
| `a8881/.agent-browser` | 428M | agent-browser | → `C:\Users\a8881\.agent-browser` |
| `a8881/.zcode` | 370M | ZCode home | → `C:\Users\a8881\.zcode`（谨慎合并） |
| `a8881/.cc-switch` | 293M | cc-switch | → `C:\Users\a8881\.cc-switch` |
| `a8881/.docker` | 111M | docker | → `C:\Users\a8881\.docker` |
| `a8881/.claude.json` | 12K | Claude Code 配置 | → `C:\Users\a8881\.claude.json` |
| `a8881/.bashrc/.zshrc/.gitconfig/.hermes.md/.git-gitee-credentials/.futu_skill_version` | 小 | home 小文件 | → `C:\Users\a8881\` |
| `FengProj/` | 16K | 基本为空/桩 | → 并入 `C:\FengProj`（如有内容） |

### 当前真实家目录对比（决定覆盖 or 跳过）
| dot | 备份大小 | 当前真实大小 | 操作建议 |
|-----|---------|-------------|---------|
| `.claude` | 3.4G | 1K | **迁移覆盖**（完整 home） |
| `.openclaw` | 2.3G | 146M | 迁移 |
| `.codex` | 1.2G | 154M | 迁移（先备份当前） |
| `.zcode` | 370M | 303M | 迁移（先备份当前） |
| `.agent-browser` | 428M | 不存在 | 迁移 |
| `.cc-switch` | 293M | 不存在 | 迁移 |
| `.docker` | 111M | 590M | **备份比当前小→跳过或合并**，勿覆盖 |
| `.claude.json` | 12K | 不存在 | 迁移 |

## 实施阶段（新 session 执行）

### 阶段 0 — 前置
- 确认哪个 session 执行；新 session 的 CWD 应在 `C:\FengProj\fengyuwang_com`（或不在沙箱内），以便最后也能迁沙箱。
- C: 盘空间核对（需额外 ~8G 峰值，实为移动到同盘≈即时）。

### 阶段 1 — 家目录 dot-工具归位
逐项对备份→真实 home，统一方法：
```
robocopy "<Lecoo Backup>\a8881\.<tool>" "C:\Users\a8881\.<tool>" /E /COPY:DAT /XJ /MOVE
```
- `/MOVE` 移动后源备份即空。
- **覆盖前先备份当前真实 home**（尤其 .codex/.zcode/.docker）。
- `.docker`、`.codex`、`.zcode` 等若当前更大/更新 → **先比对再决定**，不盲目覆盖。

### 阶段 2 — 沙箱 `fengyuwang_com` 收尾
- **本 session 之后**，新 session 从 `C:\FengProj\fengyuwang_com` 启动。
- 确认 `fengyuwang_com` 的 server.py / git repo 无进程占用后，用既有 `scripts/migrate-fengproj.ps1` 逻辑（或直接 robocopy+MKLINK）迁到 `C:\FengProj\fengyuwang_com`，旧路径建 junction。

### 阶段 3 — Lecoo Backup 快照清理
- 移完后 `Lecoo Backup` 应只剩空壳/可由用户删除。**删除前需用户确认**。
- `FengProj/` 快照并入 `C:\FengProj`。

## 验证
- 每个 dot 工具迁移后：新 home 可读、关键子项在；备份源已空。
- `.claude` 3.4G 迁移后 `C:\Users\a8881\.claude` 体积≈3.4G（不再是 1K）。
- 沙箱迁移后新旧两路径访问同一 git 仓库。
- 重启 ZCode/Claude 无配置丢失。

## 风险 / 注意
- **覆盖真实 home 有风险**：`.codex`/`.zcode`/`.docker` 当前可能比备份新 → 先备份当前再动。
- `.docker` 备份仅 111M < 当前 590M → **不应覆盖**，跳过或仅补缺。
- `NTUSER.DAT*`、`.TM*` 是注册表事务文件 → **不迁移**（系统专属）。
- `Lecoo Backup` 是备份，删除前必须用户确认。
