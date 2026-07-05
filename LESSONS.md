# LESSONS.md — Fengyu WANG 网站维护经验教训

## 高频错误（跨多个会话反复出现）

### 1. zh-hk 繁体页面混入粤语口语

**错误表现**：zh-hk 页面使用「嘅、佢、咗、唔係、睇、呢、啲、俾、嘢、喺、邊度、乜嘢」等粤语口语字，而非标准香港繁体书面语。

**正确做法**：zh-hk = 香港繁体书面语，NOT 粤语口语。使用「的、它/他、了、不是、看、這、些、給、東西、在、哪裡、什麼」。

**触发场景**：任何包含中文字符串的 zh-hk 页面。

**修复方法**：全量替换，而非局部 patch。使用对照字典段落式重写。

### 2. zh-hk 页面残留简体中文

**错误表现**：zh-hk 文件中出现简体中文字符（如内置、不会、迁移、设计、系统等）。

**触发场景**：从 zh-cn 复制内容到 zh-hk 后未完整转换。

**修复方法**：使用 opencc-js (`npm install opencc-js`)，Node.js 调用 `OpenCC.Converter({ from: 'cn', to: 'hk' })` 做全文件转换。不要用逐字符 sed 替换——sed 既遗漏字符又会造成错字（如 复→復 导致 复杂→復杂）。

**已验证正确的 opencc-js require 路径**：
```js
const OpenCC = require('C:/Users/a8881/AppData/Local/Temp/node_modules/opencc-js/dist/umd/full.js');
```

**注意**：opencc-js 会将「王丰羽」误转为「王豐羽」（丰作姓氏时不变），转换后需单独修正回来：`sed -i 's/王豐羽/王丰羽/g'`。

### 3. 翻译不达「信达雅」标准

**错误表现**：英文或 zh-hk 与 zh-cn 语义不对齐。直译导致表达生硬，不符合目标语言习惯。

**正确做法**：三语言必须语义一致。zh-hk 用香港繁体书面习惯遣词造句（如「信息」→「資訊」），en 用地道英文表达。不要逐字翻译。

### 4. 卡片字体偏离模板规格

**错误表现**：增大 `.mkt-card .card-content h3` 或 `p` 的 font-size。

**正确做法**：h3=1.2rem, p=.82rem, .card-btn=.78rem 是 frozen values，任何页面不得偏离。

**例外**：仅 art.html 使用不同的色板（暖色调 #d0c2ad、径向渐变），但卡片字体尺寸仍必须遵循上述值。

### 5. 跨语言链接指向错误语言

**错误表现**：zh-hk 页面的 link-card 或 href 写出 `/zh-cn/xxx.html` 而非 `/zh-hk/xxx.html`。

**触发场景**：复制粘贴跨语言模板时未全部替换语言路径。

**修复方法**：检查所有 `href="/zh-` 和 `href="/en/` 路径，确认与页面语言一致。

### 6. 导航栏 Cantonese 未随内容更新

**错误表现**：shared-subpage-navbar.js 中的 zh-hk 文案使用粤语（如「致唔應該來嘅人」），与页面正文标准书面语不统一。

**修复方法**：改成标准书面语（「致不應該來的人」）。nav 文案和页面正文应使用同一语体。

### 7. 不利于求职的内容

**错误表现**：提及 ADHD、阅读障碍（dyslexia）、或「艺术比工作更重要」等 HR 可能减分的个人信息。

**修复方法**：完全删除。艺术页面用「藝術是我的生命」代替「藝術好比生命——遠比工作重要」。任何疾病、认知障碍相关内容不出现。

### 8. sitemap.xml 未同步更新

**错误表现**：新增页面（ethos, art*, automation, blog/posts）后 sitemap.xml 未更新，搜索引擎无法发现新内容。

**修复方法**：每次上线前检查 sitemap.xml 是否涵盖所有页面。

### 9. 设计图片 URL 错误

**错误表现**：art.html 等页面使用的 Unsplash 图片与主题不符（如艺术页面使用监狱图片）。

**修复方法**：每个页面选择与主题匹配的 Unsplash 图片。card 背景用 `w=600` 版本，section 背景用 `w=1000` 版本。

### 10. bg image 标记未更新

**错误表现**：删除页面中旧的设计图片后，`style="--section-bg-img:url(...)"` 残留旧的 placeholder 图片。

**修复方法**：同步更新所有 card 和 section 的 background-image。

---

## 本次会话（2026-07-06）新增教训

### 11. `sed -i` 与 Edit 工具冲突

**错误表现**：先用 `sed -i` 修改了文件，然后 Edit 工具报错 "File has been modified since read"。

**原因**：Edit 工具跟踪文件的读取时间戳，shell 命令修改文件后未通知 Editor。

**解决方法**：要么全部用 Edit 工具修改，要么全部用 sed/bash 修改，不要混用。如果用 sed 修改后还需要 Edit，先重新 Read。

### 12. grep -P 在 MinGW bash 不可用

**错误表现**：`grep -P` 报错 "grep: -P supports only unibyte and UTF-8 locales"。

**解决方法**：使用 `grep -E`（ERE 模式），不支持 PCRE 的 `(?:...)` non-capturing groups 等语法。

### 13. 逐字符 sed S→T 转换不可靠

**错误表现**：`sed -i 's/复/復/g'` 把「复杂」变成「復杂」（应该是「複雜」），且遗漏大量字符（如 场→場、价→價、种→種、体→體 等）。

**解决方法**：使用 opencc-js 做完整字典匹配转换。保留 HTML 结构和英文内容不受影响。

### 14. /tmp 路径映射问题

**错误表现**：在 Git Bash 中 `npm install` 到 `/tmp`，但 Node.js 的 require 找不到模块。

**原因**：Git Bash 中 `/tmp` 实际映射到 `C:\Users\<user>\AppData\Local\Temp`。用 MSYS2 路径 require 不生效。

**解决方法**：使用完整 Windows 路径：
```js
require('C:/Users/a8881/AppData/Local/Temp/node_modules/opencc-js/dist/umd/full.js')
```

### 15. 工具链兼容性 — Windows + Git Bash

**错误表现**：Unix 工具（grep -P, sed -i 的 POSIX 扩展）在 MinGW 环境下不支持。

**解决方法**：使用基础的 sed 和 grep -E 语法。复杂转换用 Node.js 脚本实现。

### 16. zh-hk art 子页面缺少暗色模式样式

**错误表现**：zh-hk art-literature.html, art-music.html, art-architecture.html, art-painting.html, art-sculpture.html, art-film.html, art-design.html 的 `body[data-theme="dark"]` 区块缺少多项规则：`.block-inner h2`、`.block-subtitle`、`.block-inner p`、`.section-card` 边框色、`.link-card p`。暗色模式下标题和正文不可见（白字/浅灰字在浅色背景上）。

**触发场景**：从 zh-cn 复制模板后未补齐完整的暗色模式规则集。

**检查方法**：在浏览器中切换到暗色模式，确认所有文本元素（h1, h2, p, block-subtitle, link-card p）颜色正确。或 gre  count `data-theme` 规则数。

### 17. 「去到邊度都先去博物館」为粤语口语

**错误表现**：zh-hk/art.html 第 214 行使用「去到邊度都先去博物館」——「邊度」是粤语口语词，应使用标准书面语。

**正确写法**：「到任何地方都先去博物館」

**修复方法**：使用「到任何地方」代替「去到邊度」，这是贯穿全文的主题句，必须与第二段的「到任何地方都先去博物館」保持一致。所有 zh-hk 页面在引用此句时统一。

---

## 审查清单（上线前逐条确认）

- [ ] 所有 zh-hk 页面无粤语口语
- [ ] 所有 zh-hk 页面无简体字（用 opencc cn→hk 转换 + 王丰羽修正）
- [ ] 三语言语义一致（信达雅）
- [ ] 卡片字体未偏离 spec（h3=1.2rem, p=.82rem, .card-btn=.78rem）
- [ ] 非 art 页面使用冷色调板（#f5f5f7/#475569/#64748b），不使用艺术页面暖色
- [ ] art 页面是唯一例外，不做 palette 扩展
- [ ] 所有跨语言 href 指向正确路径
- [ ] navbar data-section 与实际页面匹配
- [ ] link-card 导航链完整：ai→invest, cloud→mkt, mkt→portfolio, portfolio→invest, invest→blog, web3→blog/posts/web3-deep-research/, art→ethos, ethos→blog
- [ ] sitemap.xml 包含所有页面
- [ ] 无 ADHD/dyslexia/「艺术比工作重要」等求职不利内容
- [ ] 设计图片与页面主题匹配
- [ ] dark mode 样式正常
- [ ] section-bg 使用 blur(20px) + translucent overlay 模式
- [ ] 图片 URL 使用 w=600（card）和 w=1000（section）版本
