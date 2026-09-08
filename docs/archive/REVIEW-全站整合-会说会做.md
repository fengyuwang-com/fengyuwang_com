# REVIEW — 全站整合评审：让站点显出「不仅会说，而且会做」（v1）

> 2026-09-05/06。用户令：全站内容与文档对账，把"会说"（55 篇博文）和"会做"（工程实证）之间的桥搭起来。
> 约束：纯静态铁律不动（DECISION-0001）；手写页结构/URL 不动；v6.2 正文禁「」；corpus 只读；master 不动，一切推 dev。

## 一、审计结论（对账结果）

### 站上已有的"会做"（强，但互相孤立）
| 资产 | 位置 | 状态 |
|---|---|---|
| FengInvest 七层状态机（fengstate.py / fengdata.py / 数据门禁） | zh-cn/fenginvest.html | 强，GitHub 已链 |
| Jingxin / FengOffice / Search King 作品集 | zh-cn/tech.html + 各自页 | 强 |
| verify-011 回测代码（代码即论证） | 博文 four-filters 正文 | 强 |
| 5DT-PD 方法框架 | zh-cn/5dt-pd.html | 强 |

### 缺口（会说 → 会做的桥没搭）
1. **零反链**：55 篇博文无一篇链接到任何工程页；fenginvest/tech/search-king 也不链相关文章。访客看不出"文章里的定理有做出来的系统兜着"。
2. **验证文化不可见**：论断编号制（verify-011、claim_supported、results.json 存档，notes/A.md L34）站上零提及——这是"审计式投资学"的招牌。
3. **llms.txt 过时**：指向不存在的 /en/portfolio.html；缺 FengInvest/SearchKing/FengOffice/Jingxin/FengMedia/狗拿钱定理页；无博客精选。
4. **dog-ate-my-money.html 是孤页**：无任何页面链它；description 还用「」。
5. **"做"类文章缺口**：100-题里最硬的工程实录未生产——#75《我给 Docker 报了一个级联 bug》（docker/desktop-feedback #527，级联 socket，notes/B.md E1 全套素材）、#87《模型的记忆是供应商锁定》（AIExport 动机，notes/D.md）、#11《用代码审判自己的投资格言》。

### 文档 ↔ 站点对照关系（已核实）
- notes/A.md L34 验证文化 → 应落在 fenginvest.html
- notes/B.md E1 Docker 级联 bug（篇140）→ 应生产为博文 #75
- notes/B.md E2 亲自修 bug（篇044）→ 备用素材
- notes/D.md E2 llm-text-processor（GitHub 项目）→ 应入 tech.html 工具链证据
- notes/D.md AIExport 动机原话（篇128）→ 数据主权线选题 #87
- docs/STRATEGY-战略区.md 定理 70 条/文章 100 题 → 生产总库（按 v6.2 逐篇走）

## 二、执行计划（线性，不找子代理）

**Phase 1 搭桥（本轮）**
1. llms.txt 重写：修死链、补全项目页/方法论页/博客精选/验证文化一句话。
2. fenginvest.html 加"验证文化"节（论断编号制：断言→编号→回测→claim_supported→存档）+ 文末相关博文（four-filters / do-the-math / adjusted-price / rearview-mirror）。三语同步。
3. invest.html 加狗拿钱定理页 + four-filters 文章链接；dog-ate-my-money.html description 去「」。三语同步。
4. 博文文末"延伸"链接（轻量，不动正文）：four-filters → FengInvest；dog-where → 狗拿钱定理页。三语同步。
5. tech.html 补 llm-text-processor（开源工具证据链，notes/D.md E2）。三语同步。

**Phase 2 生产"做"类文章（本轮起，逐篇走 v6.2 全流程）**
6. #75《我给 Docker 报了一个级联 bug》：brief（docs/briefs/docker-cascade-bug.md，素材=篇140 逐字+回合表）→ zh-cn → 痕迹词/引号清零 → zh-hk（zh2hk.py）→ en 手译 → Hugo 构建 → 推 dev。体式：调试日志/issue 时间线体（与既有 12 篇套路互异）。
7. 首页"最新"区加该文卡片（会做的第一张公开名片）。
8. 后续按 100-题推进：#87 记忆=供应商锁定（AIExport 动机）→ #73 Docker 就是个软件商店 → #11 论断#11 → 数据主权线。

## 三、验证清单（每轮收尾必做）
- grep 直角引号（正文）全零；tools/check_article.py 痕迹词全零
- /Users/fengmac/.local/bin/hugo 构建通过；curl 本地 server 标题正常
- git 只推 origin/dev；master 停在 ba74ccd 不动
