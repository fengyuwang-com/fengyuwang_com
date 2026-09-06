# todo — fengyuwang_com

## 待办队列（需站长决策）

- [ ] FlyGo 仓库目前是 private（fengyuwang-com/FlyGo），flygo.html 已挂它的 Release/GitHub 链接，访客会 404 — 需决定：公开仓库或建 Open-FlyGo 镜像（参照 FengMedia→Open-FengMedia 惯例）
- [ ] CF Web Analytics 仍是占位符 token（check_site [config] 节长期 PASS 提醒项）

## 已完成（2026-09-07 本轮，接 HANDOFF-2026-09-07-flygo-navbar-buttons.md）

- [x] 接续交接文档：拉取 dev，三件待办全部完成
- [x] 按钮等高：根因 = `.default-btn-one` 的 margin-top:5px 在 flex 行里让 `.default-btn` 被 stretch 多撑 5px（54 vs 49）；修复 = `.cta-row` 内两按钮 margin 清零（style.css 全局）；全站扫描 81 页 9 混排组 0 不匹配
- [x] flygo.html ×3 hero cta-row 加「下载 Release」（蓝）+「查看 GitHub 仓库」（白），文案/属性沿用 fengmedia 惯例（target=_blank rel=noopener）
- [x] 导航栏完整性检查节（check_site.py 第 15 节，子代理）：静态解析 navbar JS，三语 27 页全可达无孤儿页，copy 三语各 88 键一致，*Href 三语路径一致且目标存在，含负向测试
- [x] navbar JS 两处硬编码文案提取成三语 copy key：siteTracks（按主线浏览网站）、menuToggle（切换菜单/切換選單/Toggle menu）——修复而非豁免
- [x] 导航栏 JS 版本号全站 bump v=26.08.06.19.08 → v=26.09.07.04.10（442 文件，d0631c2 漏做 cache-bust；字节级操作保留 364 个 CRLF 文件原始行尾）
- [x] 按钮等高固化 check_site.py 第 16 节（搭第 13 节同一趟渲染采样，按父元素身份分组）：33 组混排 0 不匹配
- [x] 清掉残留 _site（gitignored 中断构建产物）；全量门禁全绿（469 页暗色审计 0 问题，死链 7213 引用 0 断链）
