# 交接文档 — FlyGo 页面 / 导航栏检查 / 按钮高度（2026-09-07）

分支：`dev`（master 未动，用户明确「现在暂时不要主线」，master push 需用户再次明确批准）。
上一笔已提交并 push 的 commit：`c4da617`（首页 About 按钮 dark hover 对比度修复 + check_site.py 新增 12.5 节 hover 对比度检查）。

## 一、工作区未提交内容（已完成但未跑门禁、未 commit）

`git status`：
- 新增 `zh-cn/flygo.html`、`en/flygo.html`、`zh-hk/flygo.html` — FlyGo 专用页（Windows PC → 全功能 NAS）。
- `zh-cn/index.html` / `en/index.html` / `zh-hk/index.html` — 首页 FlyGo 卡片链接从 `/{lang}/tech.html` 改为 `/{lang}/flygo.html`。
- `assets/js/shared-subpage-navbar.js` — 技术 ▾ 软件项目组新增 FlyGo（桌面 submenu 一处 + 移动 drawer 一处），三个语言 copy 对象各加 `flygo` / `flygoHref` 两键（约 89-90 / 177-178 / 265-266 行）。`node --check` 通过，渲染已验证。

构建素材（临时文件，机器重启会丢，内容已固化进 flygo.html）：
- `/tmp/flygo_tpl.html`（@@token@@ 模板）、`/tmp/flygo_data.json`（三语文案）。

FlyGo 页 hero 按用户要求做成了「大标题 + 一张大截图」（参照已废弃的 Apple-tile 首页原型 ed4f1ba/b8f2c2f 的视觉语言），截图用 `assets/img/shots/flygo-desktop.png`，不是 mkt-card 方块网格。

## 二、待办三件事（用户最新指令，均未完成）

### 1. 按钮 高度必须一致 — 蓝的 `.default-btn` vs 白的 `.default-btn-one`

用户原话：「如果一个蓝一个白的两个控件的话，高度必须要一样」「全站的那个脚本也要搞清楚」。

已查明（`assets/css/style.css`）：
- `.default-btn`（187-212 行）：font-weight 700, font-size 15px, border 2px solid #0071e3；**padding 行没读完（202 行起）**，这是对齐的关键。
- `.default-btn-one`（214-234 行）：font-size 15px, font-weight 700, border 2px solid #333, padding 12px 35px, radius 50px。

做法建议：读 `.default-btn` 完整 padding/line-height，让两者总高相等（建议统一 padding 或用 `box-sizing` + 固定 min-height），作为全局修复落在 style.css，不要只改 flygo 页。修复后用无头浏览器量两个按钮的 `offsetHeight` 验证（flygo hero 和首页 About 行都出现这一对按钮）。

### 2. FlyGo 页加 GitHub 仓库链接 + Release 下载链接

用户：「GitHub 里面有个 release 的」。仓库 URL 未知 — 之前 `curl api.github.com` 失败是 zsh glob 报错（URL 里 `?` 未加引号！），不是 API 失败。重试：

```bash
curl -s 'https://api.github.com/users/fengyuwang-com/repos?per_page=100'
```

参考先例：FengMedia 用 https://github.com/fengyuwang-com/Open-FengMedia。找到 FlyGo 仓库名后，在三个 flygo.html 加「GitHub 仓库 / 下载 Release」按钮（建议放 services 区或 hero 的 cta-row，Release 链接格式 `https://github.com/fengyuwang-com/<repo>/releases/latest`）。

### 3. 导航栏完整性纳入 check_site.py（新检查节）

用户：「导航栏是不是包含所有页面这件事本身也要去搞定…包括导航栏的 3 种语言等等」。

要求：新加一节检查，对每个语言（en/zh-cn/zh-hk）：
- `{lang}/*.html` 的每个页面 href 是否都能从 `assets/js/shared-subpage-navbar.js` 构建出的导航结构中到达（桌面 + 抽屉）；
- 每个 label 是否同时存在于三个语言 `copy` 对象（不许硬编码、不许某语言缺键）。

跑出来缺的页面要么补进导航栏，要么建显式豁免清单（新豁免需用户确认，参照 DESIGN_ALLOWLIST 惯例）。

## 三、收尾流程（AGENTS.md 门禁）

1. 完成上述三件事后跑 `python3 tools/check_site.py` 全量（含暗色审计，必须 exit 0 全绿）。
2. `git add -A && git commit`（描述性中文信息）→ push 到 **dev**。
3. master 一律不碰，部署上线需用户明确批准。

## 四、已知坑（本次会话踩过）

- shared-subpage-navbar.js 移动 drawer 缩进是 10 空格，桌面 submenu 是 12 空格，字符串替换两处都要改。
- 页面内联 `<style>` 在 style.css 之后加载，同特异性时覆盖全局 → dark hover 白底白字 bug 的根源（已修 + 已固化检查 12.5 节）。
- check_site.py 的 hover 对比度节有「resolved」豁免逻辑：更高特异性的 :hover 规则声明了达标颜色则跳过。
- 生成页面模板别用 str.format（CSS 花括号冲突），用 @@token@@ + replace。
- 铁律：`assets/` 不删；纯静态 0 运行时 BYOK（DECISION-0001）；个人隐私文章 `*` 前缀 + draft。
