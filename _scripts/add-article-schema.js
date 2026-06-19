/**
 * add-article-schema.js
 * 
 * 为所有 blog 静态文章页面添加 Article JSON-LD schema
 * 从现有 HTML 结构提取：headline(h1), datePublished, description(meta), tags
 * 
 * 用法: node _scripts/add-article-schema.js
 * 
 * 安全设计：
 * - 保留全文 (html, head, body)
 * - 只在 </title> 之后、<link> 之前注入 JSON-LD
 * - 如果已有 application/ld+json 则跳过
 */

const fs = require('fs');
const path = require('path');

const SITE_URL = 'https://fengyuwang.com';
const SITE_LOGO = '/assets/img/logo.png';
const AUTHOR_NAME = 'Fengyu WANG';
const AUTHOR_URL = '/';
const PUBLISHER_NAME = 'Fengyu WANG';
const PUBLISHER_LOGO = '/assets/img/logo.png';

// 语言目录列表
const LANG_DIRS = ['en', 'zh-cn', 'zh-hk'];

let totalProcessed = 0;
let totalSkipped = 0;
let totalErrors = 0;

LANG_DIRS.forEach(lang => {
    const postsDir = path.join(__dirname, '..', lang, 'blog', 'posts');
    
    if (!fs.existsSync(postsDir)) {
        console.log(`[${lang}] 目录不存在: ${postsDir}`);
        return;
    }

    const entries = fs.readdirSync(postsDir, { withFileTypes: true });
    
    entries.forEach(entry => {
        if (!entry.isDirectory()) return;
        
        const indexPath = path.join(postsDir, entry.name, 'index.html');
        if (!fs.existsSync(indexPath)) return;

        console.log(`[${lang}/${entry.name}] 处理中...`);
        
        try {
            const html = fs.readFileSync(indexPath, 'utf-8');
            
            // 检查是否已有 JSON-LD
            if (html.includes('application/ld+json')) {
                console.log(`  ⏭️  已存在 JSON-LD，跳过`);
                totalSkipped++;
                return;
            }

            // 提取标题 (从 <title> 标签)
            const titleMatch = html.match(/<title>(.*?)<\/title>/);
            const fullTitle = titleMatch ? titleMatch[1] : '';
            // 从 "Blog Title | Fengyu WANG" 提取纯标题
            const headline = fullTitle.replace(/\s*\|\s*Fengyu WANG\s*$/, '').trim();

            // 提取描述 (从 <meta name="description">)
            const descMatch = html.match(/<meta name="description" content="([^"]+)"/);
            const description = descMatch ? descMatch[1] : '';

            // 提取日期 (从 <span class="article-date">)
            const dateMatch = html.match(/<span class="article-date">([^<]+)<\/span>/);
            const datePublished = dateMatch ? dateMatch[1].trim() : '';

            // 提取标签 (从 article-meta 里的 tag spans)
            const tagRegex = /<span style="display:inline-flex;padding:4px 10px;border-radius:999px;background:rgba\(0,113,227,\.08\);color:#0071e3;font-size:\.8rem;font-weight:600;">([^<]+)<\/span>/g;
            const tags = [];
            let tagMatch;
            while ((tagMatch = tagRegex.exec(html)) !== null) {
                tags.push(tagMatch[1]);
            }

            // 提取 canonical URL
            const canonicalMatch = html.match(/<link rel="canonical" href="([^"]+)"/);
            const canonicalPath = canonicalMatch ? canonicalMatch[1] : `/${lang}/blog/posts/${entry.name}/`;
            const pageUrl = SITE_URL + canonicalPath;

            // 构建 Article JSON-LD
            const articleSchema = {
                '@context': 'https://schema.org',
                '@type': 'Article',
                'headline': headline,
                'image': SITE_URL + SITE_LOGO,
                'datePublished': datePublished ? datePublished : undefined,
                'dateModified': datePublished ? datePublished : undefined,
                'author': {
                    '@type': 'Person',
                    'name': AUTHOR_NAME,
                    'url': SITE_URL + AUTHOR_URL
                },
                'publisher': {
                    '@type': 'Organization',
                    'name': PUBLISHER_NAME,
                    'logo': {
                        '@type': 'ImageObject',
                        'url': SITE_URL + PUBLISHER_LOGO
                    }
                },
                'description': description,
                'keywords': tags.length > 0 ? tags.join(', ') : undefined,
                'mainEntityOfPage': {
                    '@type': 'WebPage',
                    '@id': pageUrl
                }
            };

            // 清理 undefined 字段
            Object.keys(articleSchema).forEach(key => {
                if (articleSchema[key] === undefined) {
                    delete articleSchema[key];
                }
            });

            const jsonLD = JSON.stringify(articleSchema, null, 2);
            const scriptTag = `\n\t<script type="application/ld+json">${jsonLD}</script>`;
            
            // 注入点：在 </title> 之后、前面的 meta/link 之前
            // 更安全：在 <link rel="canonical" ...> 那一行之后注入
            // 或者在 <link rel="alternate" hreflang="x-default" ...> 之后注入
            const injectionTarget = '<link rel="alternate" hreflang="x-default"';
            const injectPos = html.lastIndexOf(injectionTarget);
            
            if (injectPos === -1) {
                // 后备：在 <title> 之后注入
                const titleEndPos = html.indexOf('</title>');
                if (titleEndPos === -1) {
                    console.log(`  ❌ 找不到注入点`);
                    totalErrors++;
                    return;
                }
                const before = html.slice(0, titleEndPos + 8); // after </title>
                const after = html.slice(titleEndPos + 8);
                
                // 找到第一个非空白行后的位置
                const firstLink = after.search(/<link\s/);
                if (firstLink === -1) {
                    console.log(`  ❌ 找不到 link 标签`);
                    totalErrors++;
                    return;
                }
                
                const newHtml = before + scriptTag + '\n\t' + after.slice(firstLink);
                fs.writeFileSync(indexPath, newHtml, 'utf-8');
            } else {
                // 在 x-default 行之后注入
                const xDefaultEnd = injectPos + injectionTarget.length;
                const hrefStart = html.indexOf('href="', xDefaultEnd);
                const hrefEnd = html.indexOf('">', hrefStart);
                const afterXdefault = hrefEnd + 2; // after ">
                const before = html.slice(0, afterXdefault);
                const after = html.slice(afterXdefault);
                
                const newHtml = before + scriptTag + '\n\t' + after;
                fs.writeFileSync(indexPath, newHtml, 'utf-8');
            }

            console.log(`  ✅ Added: "${headline}" (${datePublished})`);
            totalProcessed++;
            
        } catch (err) {
            console.error(`  ❌ Error: ${err.message}`);
            totalErrors++;
        }
    });
});

console.log(`\n=== 完成 ===`);
console.log(`处理: ${totalProcessed} | 跳过: ${totalSkipped} | 错误: ${totalErrors}`);
