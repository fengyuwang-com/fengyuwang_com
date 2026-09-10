# 语音与翻译

> 从 `AGENTS.md` 瘦身搬入：Style & Voice、Translation 全文。`AGENTS.md` 正文只留压缩不变量。

- **Relaxed sincerity.** Short sentences. Real details.
- **NO second-person** (never use "我给你", "you can", etc.).
- **NO self-praise.** Let the work speak. Use objective framing.
  - BAD: "你的能力是互相增强的" → sounds like bragging
  - GOOD: "当不同的能力相互增强的时候，这就是真正的稀缺" → objective truth
- Be direct. Avoid marketing fluff. Sound like a real person.

## 思想锚点（每页一句）

| 页面 | 思想锚点 | 整页回答的问题 |
|------|---------|--------------|
| 首页 | `理性 · 客观 · 不坑人` | "这人信什么？" |
| 市场学（mkt） | 没有显式锚点，用标题 `市场学` | "市场学是什么？" |
| 投资（invest） | `买公司，不是买彩票` | "投资到底是什么？" |
| 技术（portfolio） | `交付为开始` | "技术是为了什么？" |
| 能力结构（capabilities） | `三条线，一个根` | "你的能力怎么组合的？" |

## Triangular Loop（三角闭环）

Capabilities 页的核心概念：

- **市场理解力**：让人想买，而不是让人烦
- **技术实现力**：想得到，做得出
- **商业判断力**：知道什么值得做

这三个能力不是并列的——它们是互相喂的。市场发现机会，技术实现产品，商业判断方向，来回验证。
**当不同的能力相互增强的时候，这就是真正的稀缺。**

## 翻译规则

- **zh-hk** = Hong Kong **formal written** Traditional Chinese. 信达雅. Localize jokes.
  - **粤语口语体不可接受（2026-09-12 站长令）：** zh-hk 一律书面正体，禁用口语字词——嘅/唔/係/咗/喺/啲/嘢/乜嘢/佢/哋/嗰/呢/咁/唔该/搬屋 等；「嗰批」「幾時先返嚟」式口语句一律改为书面句（那批/甚麼時候才回來）。
  - 判据：把 zh-hk 正文念出来像书面文章，不像 TVB 台词。存疑时以 zh-cn 语义为底做书面繁体转换。
  - 港式术语照用：光模組、伺服器、軟體不強改（依站内既有用法），但语体必须书面。
- Use `translationKey` to pair articles across languages.
- Keep structure identical across all three languages.
- Section titles: translate meaning, not literally.
- Punchlines: may need adaptation, not direct translation.
- **zh-hk uses 互相** (not 相互). Example: "當不同的能力互相增強的時候".

## Punchline 写法

Punchlines go in **h2** — they ARE the section title, not the subtitle.
Keep block-subtitle for normal explanatory text.

This applies to card grids too: the **h3** in each .mkt-card should be punchy (same style as h2),
and the **p** inside .card-content should be the normal description.

Full element mapping:

| Element | Role | Example |
|---------|------|---------|
| section > h2 | Punchline | 试过了，所以知道 |
| section > .block-subtitle | Normal description | AI 本地部署与 Web3 节点的亲身验证 |
| .mkt-card > .card-content > h3 | Punchline (short) | 试过了，所以知道 |
| .mkt-card > .card-content > p | Normal description | AI 本地部署与 Web3 节点的亲身验证 |

Examples of correct structure:

```
<h2>试过了，所以知道</h2>
<p class="block-subtitle">AI 本地部署与 Web3 节点的亲身验证</p>
```

Think "Just Do It" or "Think Different." They should make the reader pause and nod.

**Rules:**

- Keep it under 12 words where possible.
- No explanations, no context — the section body does that.
- Be specific, not generic. "算力像水电一样" beats "云服务的核心优势".
- A little attitude is OK. Self-deprecation or brutal honesty works better than marketing fluff.

**Examples (good):**

- 有些门，本地推不开
- 试过了，所以知道
- 去中心化的梦，中心化的服务器

**Examples (bad):**

- 本章节将介绍云服务的核心能力
- 本节讨论本地部署的局限性
