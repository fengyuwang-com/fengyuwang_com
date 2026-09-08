# 发版与门禁

> 从 `AGENTS.md` 瘦身搬入：Git & Versioning、Release Gate、Privacy、Docker Preview 全文。
> "何时跑全量"的唯一出处是本篇；别处只写一句话 + 链接。

## Git Strategy

| Branch | Purpose | Deploys |
|--------|---------|---------|
| `master` | Production | ✅ Cloudflare Pages — **NEVER push without explicit user approval** |
| `dev` | Daily work | ❌ Never deploys directly; push freely after checks pass |

## Commit Flow

1. (内容改动后) `cd hugo && hugo --gc --cleanDestinationDir && bash deploy.sh` 把博客构建部署到仓库根
2. 日常 dev：跑快速检查 `python3 tools/check_site.py --no-dark`，通过再 commit
3. `git add -A && git commit -m "descriptive message"`
4. push dev（master 不动）
5. 发版（= 合并并 push 到 master）前：跑全量 `python3 tools/check_site.py`（含浏览器审计），全绿才合，**必须先获得用户明确批准**

## Release Gate — 全站大脚本（发版到 master 前必跑）

全站只有**一个**检查脚本：`tools/check_site.py`。所有能机械判定的检查全部合并在这里
（16 节：内容规范 / 三语对齐 / 简繁质量 / 围栏结构 / 部署一致性 / sitemap / 站点配置 /
死链 / en 中文泄漏 / 三语页面对等 / 全站搜索索引 / 暗色+亮色对比度浏览器审计 /
导航栏完整性 / 按钮等高；节数随脚本增长，以脚本注释头为准）。

**三条铁律（只卡发版，不卡日常 dev）：**

1. **发版 = 合并并 push 到 master 之前**：把本次改动暴露的、能机械判定的新问题类型
   **固化成新的检查节并入大脚本**，然后跑全量 `python3 tools/check_site.py`，
   全绿（"全部检查通过 ✔"）才发版。不允许只修问题不加检查——同样的 bug 不许出现第二次。
2. **日常 dev 提交/push 到 dev**：跑快速检查 `python3 tools/check_site.py --no-dark` 通过即可，
   不必每次都跑几分钟的浏览器审计。线上或本地发现 bug 并修复后，发版前再用全量做回归。
3. 检查逻辑只写在大脚本这一处；不要另建零散检查脚本（写作用单篇模式即可）。

**用法：**

```bash
python3 tools/check_site.py                      # 全量 (含对比度审计, 约几分钟, 发版必跑)
python3 tools/check_site.py --no-dark            # 快速静态检查 (跳过浏览器审计)
python3 tools/check_site.py --article <index.md> # 单篇发布前校验 (痕迹词+字数+直角引号)
python3 tools/check_site.py --max-dark-pages 20  # 调试: 只审计前 N 页
```

对比度审计原理：无头 Chromium 真实渲染 466 页，逐页双向 (暗+亮) 切换，按 WCAG
计算每个可见文字的有效对比度，<4.5 (大字 <3.0) 报问题；只报"对照模式下正常"的
主题 bug。已知设计豁免：`5dt-pd.html` 架构图 (站长拍板)。若新增设计豁免，须用户确认后
写入 `DESIGN_ALLOWLIST`。

**退出码：** 有任何问题 => 1，全部通过 => 0。CI/人工都以退出码为准。

## Privacy

- Prefix title with `*` + `draft: true` for personal info.
- Never commit `.env` or any file with API keys, tokens, or passwords.

## Docker Preview

```powershell
docker compose up -d    # Start preview at test.fengyuwang.com
docker compose down     # Stop
```

The tunnel uses a token from Cloudflare Zero Trust → Tunnels. Put it in `.env`.
