# 迁移计划：FenglinProj → C:\FengProj（工作目录归位）

> 原则：FengProj 是工作目录。除工作目录外不该有活跃工作。
> 原则：任何在用的文件夹一律不动（稳健第一）。

## 目标
把 `C:\Users\a8881\FenglinProj\` 下的工作项目迁到 `C:\FengProj\`，
旧路径保留 **junction 别名**，让历史引用继续有效。

## 铁律（用户确认）
- 在用的文件夹不迁。
- `fengyuwang_com`（本会话沙箱 + server.py）不迁。
- `DiannaLee55-yb-export-tool-cc8b17f`（YB Export 扫描中 + VS Code 打开其文件）不迁。
- 裸 `yb-export-tool`（未占用）**可迁**。
- `.claude`（Claude 工具）→ 迁到 `C:\Users\a8881\.claude`。
- `.zcode`（ZCode 工具）→ 不动。
- `.playwright-cli`、`.agently-cli-backup`、`Lecoo Backup`、`FengProj.7z` → 备份/日志区，留原处。

## 迁移清单

### ① 安全迁移（无进程引用）→ `C:\FengProj\<name>` + 旧路径 junction
（以实际存在的子目录为准，见 `scripts/migrate-fengproj.ps1` 内 SAFE_LIST）

### ② 绝不迁
- `fengyuwang_com` 🔒
- `DiannaLee55-yb-export-tool-cc8b17f` 🔒

### ③ 工具/备份留原处
- `.claude` → 单独迁至 `C:\Users\a8881\.claude`
- `.zcode`、`.playwright-cli`、`.agently-cli-backup`、`Lecoo Backup`、`FengProj.7z`

## 方法
每个项目：
```
robocopy "<src>" "<dst>" /MOVE /E /COPY:DAT /XJ /LOG+:migrate.log
mklink /J "<src>" "<dst>"
```
- `/MOVE` = copy + delete source
- `/COPY:DAT` = data + attributes + timestamps（不拷安全/审计，避免权限问题）
- `/XJ` = 排除 junction（不把已有的联接递归拷走）
- 遇锁 → 跳过记日志，继续下一个

## 验证
- 新路径内容完整
- 旧路径经 junction 访问同一数据
- git 仓库移动后正常（`.git` 相对引用不受影响）
- 被锁项目完全未被碰

## 执行结果（2026-08-05 12:25）

**迁移完成：total=57 moved=57 skipped=7**（exit 0）

- ✅ 57 个项目全部迁移到 `C:\FengProj\`，旧路径 `junction` 已验证可用
  （抽查 Search-King/FengMail/AutoApply3/ReadyO/yb-export-tool 均 `LinkType=Junction`，
   新旧两路径访问同一数据）
- ✅ 锁定的 7 项完全未动（仍在原路径，未破坏）：
  `fengyuwang_com`(沙箱) / `DiannaLee55-yb-export-tool-cc8b17f`(YB Export) /
  `Lecoo Backup`(备份) / `.claude`(已单独移 ~/.claude) / `.zcode` / `.playwright-cli` / `.agently-cli-backup`
- ✅ `.claude` → `C:\Users\a8881\.claude\settings.local.json`（Claude 正位），原残留已清理

滚动日志：
`scripts/migrate.log`（每项目「已迁移/跳过」）。

## 未完成 / 待后续（维护窗口）
- `fengyuwang_com`（本会话沙箱）→ 待重启 ZCode 从 `C:\FengProj\fengyuwang_com` 启动后再迁
- `DiannaLee55-yb-export-tool-cc8b17f` → 等 YB Export 扫描 + VS Code 关闭后迁

## 配套改动（本次提交 7e9ec3e，dev）
- `docs/rename-fengproj.md` 本文件
- `scripts/migrate-fengproj.ps1` 迁移脚本（幂等，可续跑）
- `.gitignore` 新增 `.zcode/`、`scripts/migrate.log`（并清理 `nul` 残留）
- 全局 `~/.zcode/AGENTS.md`（CLAUDE.md 适配版）、`~/.claude/settings.local.json` 不在本仓库内
