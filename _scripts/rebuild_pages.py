#!/usr/bin/env python3
"""Rebuild AI and Cloud pages with card grid and fresh Unsplash images."""

import os

SRC = r'C:\Users\a8881\Desktop\fengyuwang_com'

# Each section: (id, h2, subtitle, section_bg, card_bg, items)
# items: list of (label, desc)

PAGES = {
    'ai': {
        'zh-cn': {
            'title': 'AI \u5de5\u7a0b\u4e0e\u81ea\u52a8\u5316',
            'desc': '\u4ece Harness Engineering \u5230 AI Agent\u2014\u2014\u6784\u5efa\u80fd\u591f\u601d\u8003\u3001\u884c\u52a8\u3001\u8fed\u4ee3\u7684\u7cfb\u7edf',
            'hero_h': 'AI \u5de5\u7a0b\u4e0e\u81ea\u52a8\u5316',
            'hero_p': '\u4ece Harness Engineering \u5230 AI Agent\u2014\u2014\u6784\u5efa\u80fd\u591f\u601d\u8003\u3001\u884c\u52a8\u3001\u8fed\u4ee3\u7684\u7cfb\u7edf',
        },
        'en': {
            'title': 'AI Engineering & Automation',
            'desc': 'From Harness Engineering to AI Agents\u2014building systems that think, act, and iterate',
            'hero_h': 'AI Engineering & Automation',
            'hero_p': 'From Harness Engineering to AI Agents\u2014building systems that think, act, and iterate',
        },
        'zh-hk': {
            'title': 'AI \u5de5\u7a0b\u8207\u81ea\u52d5\u5316',
            'desc': '\u5f9e Harness Engineering \u5230 AI Agent\u2014\u2014\u69cb\u5efa\u80fd\u5920\u601d\u8003\u3001\u884c\u52d5\u3001\u8fed\u4ee3\u7684\u7cfb\u7d71',
            'hero_h': 'AI \u5de5\u7a0b\u8207\u81ea\u52d5\u5316',
            'hero_p': '\u5f9e Harness Engineering \u5230 AI Agent\u2014\u2014\u69cb\u5efa\u80fd\u5920\u601d\u8003\u3001\u884c\u52d5\u3001\u8fed\u4ee3\u7684\u7cfb\u7d71',
        },
    },
    'cloud': {
        'zh-cn': {
            'title': '\u4e91\u670d\u52a1\u67b6\u6784\u4e0e\u5b9e\u6218',
            'desc': '\u4ece Docker \u5bb9\u5668\u5316\u5230 Cloudflare \u90e8\u7f72\u2014\u2014\u6784\u5efa\u53ef\u6269\u5c55\u3001\u9ad8\u53ef\u7528\u7684\u4e91\u57fa\u7840\u8bbe\u65bd',
            'hero_h': '\u4e91\u670d\u52a1\u67b6\u6784\u4e0e\u5b9e\u6218',
            'hero_p': '\u4ece Docker \u5bb9\u5668\u5316\u5230 Cloudflare \u90e8\u7f72\u2014\u2014\u6784\u5efa\u53ef\u6269\u5c55\u3001\u9ad8\u53ef\u7528\u7684\u4e91\u57fa\u7840\u8bbe\u65bd',
        },
        'en': {
            'title': 'Cloud Architecture & Practice',
            'desc': 'From Docker containerization to Cloudflare deployment\u2014building scalable infrastructure',
            'hero_h': 'Cloud Architecture & Practice',
            'hero_p': 'From Docker containerization to Cloudflare deployment\u2014building scalable, high-availability infrastructure',
        },
        'zh-hk': {
            'title': '\u96f2\u7aef\u670d\u52d9\u67b6\u69cb\u8207\u5be6\u6218',
            'desc': '\u5f9e Docker \u5bb9\u5668\u5316\u5230 Cloudflare \u90e8\u7f72\u2014\u2014\u69cb\u5efa\u53ef\u64f4\u5c55\u3001\u9ad8\u53ef\u7528\u7684\u96f2\u7aef\u57fa\u790e\u8a2d\u65bd',
            'hero_h': '\u96f2\u7aef\u670d\u52d9\u67b6\u69cb\u8207\u5be6\u6218',
            'hero_p': '\u5f9e Docker \u5bb9\u5668\u5316\u5230 Cloudflare \u90e8\u7f72\u2014\u2014\u69cb\u5efa\u53ef\u64f4\u5c55\u3001\u9ad8\u53ef\u7528\u7684\u96f2\u7aef\u57fa\u790e\u8a2d\u65bd',
        },
    },
}

# Shared section data (same across languages, just h2/subtitle differ)
SECTIONS = {
    'ai': [
        ('harness', 'Harness Engineering', '\u591a\u6a21\u578b\u7f16\u6392\u4e0e\u5de5\u7a0b\u5316 AI \u7cfb\u7edf',
         'Harness Engineering', 'Multi-model orchestration & engineered AI systems',
         'Harness Engineering', '\u591a\u6a21\u578b\u7de8\u6392\u8207\u5de5\u7a0b\u5316 AI \u7cfb\u7d71',
         'https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=1000&q=80',
         'https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&q=80',
         [
            ('\u591a\u6a21\u578b\u7f16\u6392', '\u6839\u636e\u5404\u6a21\u578b\u7684\u80fd\u529b\u7279\u957f\uff0c\u5c06\u5b50\u4efb\u52a1\u8def\u7531\u5230\u6700\u5408\u9002\u7684\u6a21\u578b\u3002'),
            ('\u4e0a\u4e0b\u6587\u7ba1\u7406', '\u5728\u6a21\u578b\u5207\u6362\u65f6\u5206\u6bb5\u548c\u603b\u7ed3\u4e0a\u4e0b\u6587\uff0c\u7ef4\u62a4\u957f\u65f6\u95f4\u5bf9\u8bdd\u7684\u8fde\u8d2f\u6027\u3002'),
            ('\u964d\u7ea7\u4e0e\u91cd\u8bd5', '\u5728 AI \u5de5\u4f5c\u6d41\u4e2d\u5185\u7f6e\u5bb9\u9519\u673a\u5236\uff0c\u5355\u4e2a\u6a21\u578b\u5931\u8d25\u4e0d\u4f1a\u5bfc\u81f4\u6574\u4e2a\u6d41\u7a0b\u4e2d\u65ad\u3002'),
            ('\u6027\u80fd\u76d1\u63a7', '\u8ffd\u8e2a\u5404\u6a21\u578b\u7684 Token \u6d88\u8017\u3001\u5ef6\u8fdf\u548c\u8f93\u51fa\u8d28\u91cf\uff0c\u4f18\u5316\u6210\u672c\u4e0e\u901f\u5ea6\u3002'),
         ]),
        ('agent', 'AI Agent \u5f00\u53d1', '\u81ea\u4e3b\u611f\u77e5\u3001\u51b3\u7b56\u4e0e\u884c\u52a8\u7684\u667a\u80fd\u7cfb\u7edf',
         'AI Agent Development', 'Autonomous systems that perceive, decide, and act',
         'AI Agent \u958b\u767c', '\u81ea\u4e3b\u611f\u77e5\u3001\u6c7a\u7b56\u8207\u884c\u52d5\u7684\u667a\u80fd\u7cfb\u7d71',
         'https://images.unsplash.com/photo-1531746790095-e5cb1577d651?w=1000&q=80',
         'https://images.unsplash.com/photo-1531746790095-e5cb1577d651?w=600&q=80',
         [
            ('\u6d4f\u89c8\u5668\u81ea\u52a8\u5316 Agent', '\u4ece Selenium \u8fc1\u79fb\u5230 Playwright\uff0c\u5c55\u793a Agent \u5982\u4f55\u5bfc\u822a\u590d\u6742\u7f51\u9875\u754c\u9762\u3002'),
            ('\u81ea\u5b9a\u4e49 Agent \u6d41\u6c34\u7ebf', '\u6784\u5efa\u7ed3\u5408 LLM \u63a8\u7406\u4e0e API \u8c03\u7528\u3001\u6587\u4ef6 I/O\u3001\u7ed3\u6784\u5316\u6570\u636e\u5904\u7406\u7684 Agent\u3002'),
            ('\u5de5\u5177\u8c03\u7528\u6a21\u5f0f', '\u8bbe\u8ba1 Agent \u5728\u51b3\u7b56\u8fc7\u7a0b\u4e2d\u8c03\u7528\u5916\u90e8\u5de5\u5177\u7684\u80fd\u529b\u3002'),
         ]),
        ('prompt', 'Prompt Engineering', '\u8bbe\u8ba1\u8f93\u5165\u4ee5\u83b7\u5f97\u53ef\u9760\u8f93\u51fa\u7684\u6280\u827a',
         'Prompt Engineering', 'The craft of designing inputs for reliable outputs',
         'Prompt Engineering', '\u8a2d\u8a08\u8f38\u5165\u4ee5\u7372\u5f97\u53ef\u9760\u8f38\u51fa\u7684\u6280\u85dd',
         'https://images.unsplash.com/photo-1504639725590-34d0984388bd?w=1000&q=80',
         'https://images.unsplash.com/photo-1504639725590-34d0984388bd?w=600&q=80',
         [
            ('\u7ed3\u6784\u5316\u63d0\u793a', '\u4f7f\u7528\u7cfb\u7edf\u63d0\u793a\u8bcd\u3001\u89d2\u8272\u5b9a\u4e49\u548c\u8f93\u51fa\u683c\u5f0f\u7ea6\u675f\u6765\u89c4\u8303\u6a21\u578b\u884c\u4e3a\u3002'),
            ('\u601d\u7ef4\u94fe\u63a8\u7406', '\u5c06\u590d\u6742\u4efb\u52a1\u5206\u89e3\u4e3a\u9010\u6b65\u63a8\u7406\u94fe\uff0c\u63d0\u9ad8\u51c6\u786e\u6027\u548c\u53ef\u89e3\u91ca\u6027\u3002'),
            ('\u5c11\u6837\u672c\u4e0e\u96f6\u6837\u672c\u6a21\u5f0f', '\u9009\u62e9\u5408\u9002\u7684\u8303\u4f8b\u6216\u7f16\u5199\u7cbe\u786e\u6307\u4ee4\uff0c\u5728\u4e0d\u6d6a\u8d39 Token \u7684\u60c5\u51b5\u4e0b\u83b7\u5f97\u6700\u4f73\u7ed3\u679c\u3002'),
            ('\u8fed\u4ee3\u4f18\u5316', '\u7cfb\u7edf\u5316\u6d4b\u8bd5\u63d0\u793a\u8bcd\u53d8\u4f53\u3001\u8861\u91cf\u8f93\u51fa\u8d28\u91cf\u3001\u6536\u655b\u5230\u6700\u4f73\u8868\u8ff0\u3002'),
         ]),
        ('automation', 'AI \u9a71\u52a8\u7684\u81ea\u52a8\u5316', '\u5c06 AI \u63a5\u5165\u771f\u5b9e\u5de5\u4f5c\u6d41',
         'AI-Driven Automation', 'Bringing AI into real workflows',
         'AI \u9a45\u52d5\u7684\u81ea\u52d5\u5316', '\u5c07 AI \u63a5\u5165\u771f\u5be6\u5de5\u4f5c\u6d41',
         'https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?w=1000&q=80',
         'https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?w=600&q=80',
         [
            ('\u5de5\u4f5c\u6d41\u96c6\u6210', '\u901a\u8fc7 API \u548c Webhook \u5c06 AI \u6d41\u6c34\u7ebf\u8fde\u63a5\u5230\u90ae\u4ef6\u3001\u65e5\u5386\u3001CRM \u7b49\u65e5\u5e38\u5de5\u5177\u3002'),
            ('\u6570\u636e\u5904\u7406\u6d41\u6c34\u7ebf', '\u4f7f\u7528 AI \u4ece\u975e\u7ed3\u6784\u5316\u6765\u6e90\u4e2d\u63d0\u53d6\u3001\u8f6c\u6362\u548c\u5206\u6790\u6570\u636e\u3002'),
            ('\u4eba\u5728\u56de\u8def\u6a21\u5f0f', '\u8bbe\u8ba1\u81ea\u52a8\u5316\u77e5\u9053\u4f55\u65f6\u9700\u8981\u4eba\u5de5\u5ba1\u6279\u7684\u673a\u5236\u3002'),
         ]),
    ],
    'cloud': [
        ('docker', '\u5bb9\u5668\u5316\u4e0e Docker', '\u4ece\u5f00\u53d1\u5230\u751f\u4ea7\u7684\u4e00\u81f4\u6027\u4ea4\u4ed8',
         'Containerization & Docker', 'Consistent delivery from development to production',
         '\u5bb9\u5668\u5316\u8207 Docker', '\u5f9e\u958b\u767c\u5230\u751f\u7522\u7684\u4e00\u81f4\u6027\u4ea4\u4ed8',
         'https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=1000&q=80',
         'https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600&q=80',
         [
            ('\u955c\u50cf\u6784\u5efa', '\u7f16\u5199 Dockerfile \u548c docker-compose.yml\uff0c\u786e\u4fdd\u5f00\u53d1\u548c\u751f\u4ea7\u73af\u5883\u5b8c\u5168\u4e00\u81f4\u3002'),
            ('\u591a\u9636\u6bb5\u6784\u5efa', '\u4f18\u5316\u955c\u50cf\u5927\u5c0f\uff0c\u51cf\u5c11\u90e8\u7f72\u65f6\u95f4\u548c\u5b58\u50a8\u6210\u672c\u3002'),
            ('\u6570\u636e\u6301\u4e45\u5316', '\u4f7f\u7528\u5377\u548c\u7ed1\u5b9a\u6302\u8f7d\u7ba1\u7406\u72b6\u6001\u6570\u636e\uff0c\u4fdd\u6301\u5bb9\u5668\u7684\u65e0\u72b6\u6001\u7279\u6027\u3002'),
            ('\u5bb9\u5668\u7f51\u7edc', '\u914d\u7f6e\u5185\u90e8\u7f51\u7edc\u3001\u7aef\u53e3\u6620\u5c04\uff0c\u5b9e\u73b0\u670d\u52a1\u95f4\u5b89\u5168\u901a\u4fe1\u3002'),
         ]),
        ('cloudflare', 'Cloudflare \u90e8\u7f72', '\u8fb9\u7f18\u7f51\u7edc\u4e0e\u5168\u7403\u52a0\u901f',
         'Cloudflare Deployment', 'Edge network & global acceleration',
         'Cloudflare \u90e8\u7f72', '\u908a\u7de3\u7db2\u7d61\u8207\u5168\u7403\u52a0\u901f',
         'https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=1000&q=80',
         'https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&q=80',
         [
            ('Pages \u90e8\u7f72', '\u8fde\u63a5 Git \u4ed3\u5e93\u81ea\u52a8\u90e8\u7f72\u9759\u6001\u7ad9\u70b9\uff0c\u652f\u6301\u9884\u89c8\u5206\u652f\u548c\u56de\u6eda\u3002'),
            ('\u81ea\u5b9a\u4e49\u57df\u540d\u4e0e SSL', '\u914d\u7f6e DNS\u3001\u4ee3\u7406\u72b6\u6001\u548c\u81ea\u52a8\u8bc1\u4e66\u7ba1\u7406\u3002'),
            ('\u8fb9\u7f18\u7f13\u5b58\u4e0e\u4f18\u5316', '\u5229\u7528 Cloudflare CDN \u52a0\u901f\u5168\u7403\u8bbf\u95ee\uff0c\u914d\u7f6e\u7f13\u5b58\u89c4\u5219\u3002'),
            ('\u5b89\u5168\u4e0e DDoS \u9632\u62a4', '\u542f\u7528 Web Application Firewall\u3001\u901f\u7387\u9650\u5236\u548c\u673a\u5668\u4eba\u7ba1\u7406\u3002'),
         ]),
        ('infra', '\u57fa\u7840\u8bbe\u65bd\u8bbe\u8ba1', '\u53ef\u9760\u3001\u53ef\u6269\u5c55\u7684\u7cfb\u7edf\u67b6\u6784',
         'Infrastructure Design', 'Reliable, scalable system architecture',
         '\u57fa\u790e\u8a2d\u65bd\u8a2d\u8a08', '\u53ef\u9760\u3001\u53ef\u64f4\u5c55\u7684\u7cfb\u7d71\u67b6\u69cb',
         'https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=1000&q=80',
         'https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=600&q=80',
         [
            ('\u9ad8\u53ef\u7528\u67b6\u6784', '\u8bbe\u8ba1\u65e0\u5355\u70b9\u6545\u969c\u7684\u7cfb\u7edf\uff0c\u4f7f\u7528\u8d1f\u8f7d\u5747\u8861\u548c\u5065\u5eb7\u68c0\u67e5\u4fdd\u8bc1\u670d\u52a1\u8fde\u7eed\u6027\u3002'),
            ('\u6c34\u5e73\u6269\u5c55', '\u901a\u8fc7\u589e\u52a0\u5b9e\u4f8b\u6570\u91cf\u800c\u975e\u5355\u4e2a\u5b9e\u4f8b\u89c4\u683c\u6765\u5e94\u5bf9\u589e\u957f\u3002'),
            ('\u76d1\u63a7\u4e0e\u544a\u8b66', '\u5efa\u7acb\u65e5\u5fd7\u805a\u5408\u3001\u6307\u6807\u6536\u96c6\u548c\u544a\u8b66\u4f53\u7cfb\uff0c\u53ca\u65f6\u53d1\u73b0\u548c\u5904\u7406\u5f02\u5e38\u3002'),
            ('\u707e\u96be\u6062\u590d', '\u5236\u5b9a\u5907\u4efd\u7b56\u7565\u548c\u6062\u590d\u6d41\u7a0b\uff0c\u786e\u4fdd\u6570\u636e\u5b89\u5168\u548c\u4e1a\u52a1\u8fde\u7eed\u6027\u3002'),
         ]),
        ('devops', 'DevOps \u4e0e CI/CD', '\u81ea\u52a8\u5316\u6d41\u6c34\u7ebf\u52a0\u901f\u4ea4\u4ed8',
         'DevOps & CI/CD', 'Automated pipelines for faster delivery',
         'DevOps \u8207 CI/CD', '\u81ea\u52d5\u5316\u6d41\u6c34\u7dda\u52a0\u901f\u4ea4\u4ed8',
         'https://images.unsplash.com/photo-1618401471353-b98afee0b2eb?w=1000&q=80',
         'https://images.unsplash.com/photo-1618401471353-b98afee0b2eb?w=600&q=80',
         [
            ('\u6301\u7eed\u96c6\u6210', '\u4ee3\u7801\u63d0\u4ea4\u81ea\u52a8\u89e6\u53d1\u6784\u5efa\u548c\u6d4b\u8bd5\uff0c\u65e9\u671f\u53d1\u73b0\u96c6\u6210\u95ee\u9898\u3002'),
            ('\u6301\u7eed\u90e8\u7f72', '\u901a\u8fc7\u81ea\u52a8\u5316\u6d41\u6c34\u7ebf\u5c06\u4ee3\u7801\u4ece\u4ed3\u5e93\u5b89\u5168\u63a8\u9001\u5230\u751f\u4ea7\u73af\u5883\u3002'),
            ('\u57fa\u7840\u8bbe\u65bd\u5373\u4ee3\u7801', '\u4f7f\u7528 Docker Compose \u7b49\u5de5\u5177\u5c06\u57fa\u7840\u8bbe\u65bd\u914d\u7f6e\u7eb3\u5165\u7248\u672c\u7ba1\u7406\u3002'),
            ('\u7248\u672c\u7ba1\u7406\u89c4\u8303', '\u8bed\u4e49\u5316\u7248\u672c\u53f7\u4e0e Git \u5206\u652f\u7b56\u7565\u914d\u5408\uff0c\u7ba1\u7406\u53d1\u5e03\u548c\u56de\u6eda\u3002'),
         ]),
    ],
}

def make_page(topic, lang):
    meta = PAGES[topic][lang]
    secs = SECTIONS[topic]
    
    # Build card grid (2-col)
    cards = ''
    for s in secs:
        sid, h2_zhcn, sub_zhcn, h2_en, sub_en, h2_zhhk, sub_zhhk, bg, card_bg, items = s
        if lang == 'zh-cn':
            h2, sub = h2_zhcn, sub_zhcn
        elif lang == 'en':
            h2, sub = h2_en, sub_en
        else:
            h2, sub = h2_zhhk, sub_zhhk
        cards += f'''            <div class="mkt-card" style="background-image:url('{card_bg}')" onclick="document.getElementById('{sid}').scrollIntoView({{behavior:'smooth'}})">
                <div class="card-content">
                    <h3>{h2}</h3>
                    <p>{sub}</p>
                    <button class="card-btn">\u4e86\u89e3\u8be6\u60c5</button>
                </div>
            </div>
'''
    
    # Build sections
    sec_html = ''
    for s in secs:
        sid, h2_zhcn, sub_zhcn, h2_en, sub_en, h2_zhhk, sub_zhhk, bg, card_bg, items = s
        if lang == 'zh-cn':
            h2, sub = h2_zhcn, sub_zhcn
        elif lang == 'en':
            h2, sub = h2_en, sub_en
        else:
            h2, sub = h2_zhhk, sub_zhhk
        
        item_html = ''
        for label, desc in items:
            item_html += f'                    <li><strong>{label}</strong>\uff1a{desc}</li>\n'
        
        sec_html += f'''    <div id="{sid}" class="content-block section-bg" style="--section-bg-img:url('{bg}')">
        <div class="block-inner">
            <div class="section-card">
                <h2>{h2}</h2>
                <p class="block-subtitle">{sub}</p>
                <div class="content-text-card">
                    <ul>
{item_html}                    </ul>
                </div>
            </div>
        </div>
    </div>

'''
    
    # Cross-link
    link_p = '\u5de5\u7a0b\u80fd\u529b\u9700\u8981\u5546\u4e1a\u573a\u666f\u624d\u6709\u4ef7\u503c'
    link_href = f'/{lang}/invest.html'
    link_btn = '\u63a2\u7d22\u6295\u8d44\u6846\u67b6 \u2192'
    if lang == 'en':
        link_p = 'Engineering capability needs business context to create value'
        link_btn = 'Explore Investment Framework \u2192'
    
    return f'''<!doctype html>
<html lang="{lang}">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="theme-color" content="#0f172a">
    <meta name="format-detection" content="telephone=no">
    <title>{meta['title']} | \u738b\u4e30\u7fbd Fengyu WANG</title>
    <meta name="description" content="{meta['desc']}">
    <meta name="keywords" content="{meta['title']}, Docker, Cloudflare, DevOps, \u738b\u4e30\u7fbd">
    <meta name="author" content="\u738b\u4e30\u7fbd">
    <meta name="robots" content="index,follow">
    <link rel="canonical" href="/{lang}/{topic}.html">
    <link rel="alternate" hreflang="en" href="/en/{topic}.html">
    <link rel="alternate" hreflang="zh-CN" href="/zh-cn/{topic}.html">
    <link rel="alternate" hreflang="zh-HK" href="/zh-hk/{topic}.html">
    <meta property="og:site_name" content="Fengyu WANG">
    <meta property="og:locale" content="{'zh_CN' if lang == 'zh-cn' else 'en_US' if lang == 'en' else 'zh_HK'}">
    <meta property="og:type" content="website">
    <meta property="og:title" content="{meta['title']} | \u738b\u4e30\u7fbd Fengyu WANG">
    <meta property="og:description" content="{meta['desc']}">
    <meta property="og:url" content="https://fengyuwang.com/{lang}/{topic}.html">
    <meta property="og:image" content="/assets/img/logo.png">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{meta['title']} | \u738b\u4e30\u7fbd Fengyu WANG">
    <meta name="twitter:description" content="{meta['desc']}">
    <meta name="twitter:image" content="/assets/img/logo.png">
    <link href="https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@400;600;700;800;900&display=swap" rel="stylesheet">
    <link rel="icon" type="image/png" href="../assets/img/logo.png">
    <link rel="stylesheet" href="../assets/css/bootstrap.min.css">
    <link rel="stylesheet" href="../assets/css/animate.min.css">
    <link rel="stylesheet" href="../assets/css/meanmenu.css">
    <link rel="stylesheet" href="../assets/css/fontawesome.min.css">
    <link rel="stylesheet" href="../assets/css/magnific-popup.min.css">
    <link rel="stylesheet" href="../assets/css/owl.carousel.min.css">
    <link rel="stylesheet" href="../assets/css/style.css">
    <link rel="stylesheet" href="../assets/css/responsive.css">
    <style>
        html {{ scroll-behavior: smooth; }}
        .page-wrap {{ background: #ffffff; }}
        .marketing-hero {{ text-align: center; padding: 52px 0 40px; }}
        .marketing-hero h1 {{ font-size: 3rem; font-weight: 800; margin-bottom: 10px; color: #0f172a; }}
        .marketing-hero p {{ color: #64748b; font-size: 1.1rem; line-height: 1.8; max-width: 640px; margin: 0 auto; }}

        .card-grid {{ display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 20px; padding: 0 0 48px; }}
        .mkt-card {{ position: relative; border-radius: 18px; overflow: hidden; height: 160px; display: flex; flex-direction: column; justify-content: flex-end; cursor: pointer; border: 1px solid rgba(148,163,184,.14); background-size: cover; background-position: center; }}
        .mkt-card::after {{ content: ''; position: absolute; inset: 0; background: linear-gradient(transparent 30%, rgba(0,0,0,.7)); pointer-events: none; }}
        .mkt-card .card-content {{ position: relative; z-index: 1; padding: 22px 20px 20px; color: #fff; }}
        .mkt-card .card-content h3 {{ font-size: 1.2rem; font-weight: 800; margin-bottom: 3px; }}
        .mkt-card .card-content p {{ font-size: .82rem; color: rgba(255,255,255,.82); margin-bottom: 12px; line-height: 1.45; }}
        .card-btn {{ display: inline-flex; align-items: center; gap: 4px; background: rgba(255,255,255,.18); border: 1px solid rgba(255,255,255,.25); border-radius: 999px; color: #fff; font-size: .78rem; font-weight: 600; padding: 6px 14px; cursor: pointer; font-family: inherit; transition: background .2s; pointer-events: none; }}

        .content-block {{ position: relative; padding: 44px 0 40px; margin-bottom: 12px; background-color: #f5f5f7; }}
        .content-block:last-of-type {{ margin-bottom: 0; }}
        .content-block.section-bg {{ background: var(--section-bg-img) center/cover no-repeat; background-color: #1e293b; }}
        .content-block.section-bg::after {{ content: ''; position: absolute; inset: 0; background: rgba(245,245,247,.72); backdrop-filter: saturate(180%) blur(20px); -webkit-backdrop-filter: saturate(180%) blur(20px); }}
        .content-block.section-bg .block-inner {{ position: relative; z-index: 1; }}
        .section-card {{ background: rgba(255,255,255,.90); backdrop-filter: blur(8px); -webkit-backdrop-filter: blur(8px); border-radius: 18px; padding: 32px; border: 1px solid rgba(255,255,255,.22); }}
        .block-inner {{ max-width: 720px; margin: 0 auto; padding: 0 24px; }}
        .block-inner h2 {{ font-size: 1.6rem; font-weight: 800; color: #0f172a; margin-bottom: 6px; }}
        .block-subtitle {{ color: #2563eb; font-weight: 600; font-size: .95rem; margin-bottom: 14px; }}
        .block-inner p {{ color: #475569; line-height: 1.85; margin-bottom: 14px; font-size: .97rem; }}
        .block-inner ul {{ margin: 0; padding-left: 18px; color: #475569; line-height: 1.85; font-size: .93rem; }}
        .block-inner ul li + li {{ margin-top: 5px; }}
        .content-text-card {{ background: #fff; border-radius: 14px; padding: 20px 24px; border: 1px solid rgba(148,163,184,.12); }}
        .link-card {{ text-align: center; padding: 48px 0 72px; }}
        .link-card p {{ color: #6b7280; margin-bottom: 12px; }}
        .link-card .default-btn {{ min-width: 200px; }}

        body[data-theme="dark"] .page-wrap {{ background: #0a0e1a; }}
        body[data-theme="dark"] .content-block {{ background-color: #111827; }}
        body[data-theme="dark"] .content-block.section-bg {{ background-color: #0a0e1a; }}
        body[data-theme="dark"] .content-block.section-bg::after {{ background: rgba(17,24,39,.88); backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px); }}
        body[data-theme="dark"] .marketing-hero h1 {{ color: #e5ecf4; }}
        body[data-theme="dark"] .marketing-hero p {{ color: #9fb0c3; }}
        body[data-theme="dark"] .mkt-card {{ border-color: transparent; background-color: #0a0e1a; }}
        body[data-theme="dark"] .section-card {{ background: rgba(30,41,59,.90); border-color: rgba(148,163,184,.20); }}
        body[data-theme="dark"] .block-inner h2 {{ color: #e5ecf4; }}
        body[data-theme="dark"] .block-subtitle {{ color: #6b9aff; }}
        body[data-theme="dark"] .block-inner p, body[data-theme="dark"] .block-inner ul {{ color: #9fb0c3; }}
        body[data-theme="dark"] .content-text-card {{ background: #0f172a; }}
        body[data-theme="dark"] .link-card p {{ color: #94a3b8; }}

        @media (max-width: 991px) {{
            .marketing-hero {{ padding: 36px 24px; }}
            .marketing-hero h1 {{ font-size: 2.4rem; }}
            .card-grid {{ grid-template-columns: repeat(2, minmax(0, 1fr)); }}
            .content-block {{ padding: 36px 0 28px; }}
            .block-inner h2 {{ font-size: 1.4rem; }}
        }}
        @media (max-width: 599px) {{
            .marketing-hero {{ padding: 28px 16px; }}
            .card-grid {{ grid-template-columns: 1fr; }}
            .content-block {{ padding: 28px 0 20px; }}
            .block-inner h2 {{ font-size: 1.25rem; }}
        }}
    </style>
</head>
<body>

    <div id="shared-subpage-navbar" data-section="portfolio"></div>
    <script src="../assets/js/shared-subpage-navbar.js?v=26.07.03.14.30"></script>

    <div class="page-wrap">
        <div class="container">
            <div class="marketing-hero">
                <h1>{meta['hero_h']}</h1>
                <p>{meta['hero_p']}</p>
            </div>
            <div class="card-grid">
{cards}            </div>
        </div>

{sec_html}
        <div class="link-card">
            <p>{link_p}</p>
            <a class="default-btn" href="{link_href}">{link_btn}</a>
        </div>
    </div>

    <div id="shared-site-footer"></div>
    <script src="../assets/js/shared-site-footer.js"></script>
    <script src="../assets/js/jquery.min.js"></script>
    <script src="../assets/js/bootstrap.min.js"></script>
    <script src="../assets/js/jquery.meanmenu.js"></script>
    <script src="../assets/js/main.js"></script>
    <script defer src="https://static.cloudflareinsights.com/beacon.min.js" data-cf-beacon='{{"token": "YOUR_CLOUDFLARE_TOKEN"}}'></script>
    <button class="back-to-top" id="backToTop" onclick="window.scrollTo({{top:0,behavior:'smooth'}})">\u2191;</button>
    <script>(function(){{var btn=document.getElementById('backToTop');if(!btn)return;window.addEventListener('scroll',function(){{if(window.scrollY>300)btn.classList.add('show');else btn.classList.remove('show')}})}})();</script>
</body>
</html>
'''

for topic in ['ai', 'cloud']:
    for lang in ['zh-cn', 'en', 'zh-hk']:
        html = make_page(topic, lang)
        path = f'{SRC}/{lang}/{topic}.html'
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f'Written: {path}')
print('Done')

