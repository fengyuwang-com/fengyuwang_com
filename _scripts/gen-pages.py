import re

def make_ai_en():
    """Generate en/ai.html from en/web3.html template"""
    with open('en/web3.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Head section
    head = html[:html.find('</head>') + 7]
    
    # Replace meta
    head = re.sub(r'<title>.*?</title>', '<title>AI Engineering & Automation | Fengyu WANG</title>', head)
    head = re.sub(r'<meta name="description" content=".*?">', '<meta name="description" content="A comprehensive exploration of AI engineering \u2014 Harness Engineering, AI Agent development, Prompt Engineering, multi-model collaboration, and AI-driven workflow automation.">', head)
    head = re.sub(r'<meta name="keywords" content=".*?">', '<meta name="keywords" content="AI engineering, AI Agent, Harness Engineering, Prompt Engineering, AI automation, multi-model collaboration, Fengyu WANG">', head)
    head = re.sub(r'<link rel="canonical" href="/en/web3.html">', '<link rel="canonical" href="/en/ai.html">', head)
    head = re.sub(r'hreflang="zh-CN" href="/zh-cn/web3.html"', 'hreflang="zh-CN" href="/zh-cn/ai.html"', head)
    head = re.sub(r'hreflang="zh-HK" href="/zh-hk/web3.html"', 'hreflang="zh-HK" href="/zh-hk/ai.html"', head)
    head = re.sub(r'<meta property="og:locale" content="zh_HK">', '<meta property="og:locale" content="en_US">', head)
    head = re.sub(r'<meta property="og:title" content=".*?">', '<meta property="og:title" content="AI Engineering & Automation | Fengyu WANG">', head)
    head = re.sub(r'<meta property="og:description" content=".*?">', '<meta property="og:description" content="A systematic exploration of AI engineering\u2014Harness Engineering, AI Agents, Prompt Engineering, multi-model collaboration, and automation workflows.">', head)
    head = re.sub(r'<meta property="og:url" content="/en/web3.html">', '<meta property="og:url" content="/en/ai.html">', head)
    head = re.sub(r'<meta name="twitter:title" content=".*?">', '<meta name="twitter:title" content="AI Engineering & Automation | Fengyu WANG">', head)
    head = re.sub(r'<meta name="twitter:description" content=".*?">', '<meta name="twitter:description" content="AI engineering from Harness Engineering to AI Agent development\u2014building systems that think and act.">', head)

    # Navbar - data-section
    head = re.sub(r'data-section="[^"]*"', 'data-section="portfolio"', head)

    # Body start
    body_start = '<body>\n    <div id="shared-subpage-navbar" data-section="portfolio"></div>\n    <script src="../assets/js/shared-subpage-navbar.js?v=26.07.02.01.24"></script>\n\n    <div class="page-wrap">'

    # Hero section
    hero = '''
        <div class="container">
            <div class="article-hero" style="background:linear-gradient(135deg, #0f172a 0%, #3b82f6 58%, #6366f1 100%)">
                <span class="hero-kicker">AI ENGINEERING</span>
                <h1>AI Engineering & Automation</h1>
                <p class="subtitle">From Harness Engineering to AI Agents \u2014 building systems that think, act, and improve</p>
                <div class="hero-tags">
                    <span>Harness Engineering</span>
                    <span>AI Agent</span>
                    <span>Prompt Engineering</span>
                    <span>Multi-Model</span>
                    <span>Automation</span>
                </div>
            </div>
        </div>
'''

    # Content blocks
    content = '''
        <div class="article-block">
            <h2>Harness Engineering</h2>
            <p>Harness engineering is the practice of orchestrating multiple AI models to work together in a coordinated system. Instead of relying on a single model, a harness architecture routes tasks to the most capable model, manages context windows, and handles fallback logic when a model underperforms.</p>
            <p>My approach to harness engineering emphasizes:</p>
            <ul>
                <li><strong>Multi-model orchestration</strong>: Routing subtasks to specialized models (code generation, reasoning, creative writing) based on their strengths.</li>
                <li><strong>Context management</strong>: Maintaining coherent long-running conversations by segmenting and summarizing context across model switches.</li>
                <li><strong>Fallback and retry logic</strong>: Building resilience into AI workflows so that failures in one model don\u2019t break the entire pipeline.</li>
                <li><strong>Performance monitoring</strong>: Tracking token usage, latency, and output quality across models to optimize cost and speed.</li>
            </ul>
            <div class="highlight-box">
                <p><strong>Key insight:</strong> The best AI system isn\u2019t built with the most powerful model\u2014it\u2019s built with the right combination of models, each doing what it does best.</p>
            </div>
        </div>

        <div class="article-block">
            <h2>AI Agent Development</h2>
            <p>AI agents are autonomous systems that perceive their environment, make decisions, and take actions to achieve specific goals. My work in this area spans from browser automation agents to custom tool-use workflows.</p>
            <ul>
                <li><strong>AutoApply series</strong>: A Selenium-to-Playwright migration project that automated job application workflows, demonstrating how agents can navigate complex web interfaces.</li>
                <li><strong>Custom agent pipelines</strong>: Building agents that combine LLM reasoning with API calls, file I/O, and structured data processing.</li>
                <li><strong>Tool-use patterns</strong>: Designing agents that can invoke external tools (search, calculators, databases) as part of their decision-making process.</li>
            </ul>
        </div>

        <div class="article-block">
            <h2>Prompt Engineering</h2>
            <p>Prompt engineering is the discipline of designing inputs that reliably produce desired outputs from language models. It\u2019s a blend of linguistics, logic, and experimentation.</p>
            <ul>
                <li><strong>Structured prompting</strong>: Using system prompts, role definitions, and output format specifications to constrain model behavior.</li>
                <li><strong>Chain-of-thought reasoning</strong>: Breaking complex tasks into step-by-step reasoning chains that improve accuracy and transparency.</li>
                <li><strong>Few-shot and zero-shot patterns</strong>: Selecting the right exemplars or crafting precise instructions for optimal results without excessive token usage.</li>
                <li><strong>Iterative refinement</strong>: A systematic approach to testing prompt variants, measuring output quality, and converging on the best formulation.</li>
            </ul>
        </div>

        <div class="article-block">
            <h2>AI-Driven Automation</h2>
            <p>The end goal of AI engineering is not just to build clever models\u2014it\u2019s to connect AI to real workflows that save time, reduce errors, and unlock new capabilities.</p>
            <ul>
                <li><strong>Workflow integration</strong>: Connecting AI pipelines to email, calendars, CRMs, and other everyday tools via APIs and webhooks.</li>
                <li><strong>Data processing pipelines</strong>: Using AI to extract, transform, and analyze data from unstructured sources like PDFs, emails, and web pages.</li>
                <li><strong>Human-in-the-loop patterns</strong>: Designing automation that knows when to ask for human approval, keeping the loop tight without sacrificing autonomy.</li>
            </ul>
            <div class="highlight-box">
                <p><strong>Bottom line:</strong> AI automation isn\u2019t about replacing humans\u2014it\u2019s about eliminating the repetitive parts so that humans can focus on judgment, creativity, and relationships.</p>
            </div>
        </div>
'''

    # Footer (from template)
    page_wrap_close = '    </div>\n\n    <!-- Easter egg placeholder -->\n    <div style="text-align:center; padding:60px 20px 40px;">\n        <img src="../assets/img/team/With Huang.jpg" alt="Photo with Jensen Huang" style="width:240px; max-width:70%; height:auto; border-radius:18px; box-shadow:0 12px 36px rgba(15,23,42,.12);">\n        <p style="margin-top:12px; color:#6b7280; font-size:.82rem; font-style:italic;">With Jensen Huang at HKUST \u2014 I\'m behind him.</p>\n    </div>\n\n    <div id="shared-site-footer"></div>\n    <script src="../assets/js/shared-site-footer.js"></script>'
    
    footer_scripts = html[html.find('<script src="../assets/js/jquery.min.js">'):]
    
    # Also add toc-related CSS from the template
    toc_css_match = re.search(r'/\\* === TOC.*?\\*/', html, re.DOTALL)
    toc_css = ''
    if toc_css_match:
        toc_css = toc_css_match.group(0)

    # Assemble
    result = head + '\n</head>\n<body>\n' + body_start + '\n' + hero + '\n' + content + '\n' + page_wrap_close + '\n' + footer_scripts

    with open('en/ai.html', 'w', encoding='utf-8') as f:
        f.write(result)
    print('Created en/ai.html')


def make_cloud_en():
    """Generate en/cloud.html from en/web3.html template"""
    with open('en/web3.html', 'r', encoding='utf-8') as f:
        html = f.read()

    head = html[:html.find('</head>') + 7]
    
    head = re.sub(r'<title>.*?</title>', '<title>Cloud Services Architecture & Practice | Fengyu WANG</title>', head)
    head = re.sub(r'<meta name="description" content=".*?">', '<meta name="description" content="A practical deep-dive into cloud services \u2014 Docker containerization, Cloudflare deployment, scalable infrastructure, reverse proxy, CI/CD, and cloud-native architecture.">', head)
    head = re.sub(r'<meta name="keywords" content=".*?">', '<meta name="keywords" content="cloud services, Docker, Cloudflare, cloud infrastructure, DevOps, CI/CD, Fengyu WANG">', head)
    head = re.sub(r'<link rel="canonical" href="/en/web3.html">', '<link rel="canonical" href="/en/cloud.html">', head)
    head = re.sub(r'hreflang="zh-CN" href="/zh-cn/web3.html"', 'hreflang="zh-CN" href="/zh-cn/cloud.html"', head)
    head = re.sub(r'hreflang="zh-HK" href="/zh-hk/web3.html"', 'hreflang="zh-HK" href="/zh-hk/cloud.html"', head)
    head = re.sub(r'<meta property="og:locale" content="zh_HK">', '<meta property="og:locale" content="en_US">', head)
    head = re.sub(r'<meta property="og:title" content=".*?">', '<meta property="og:title" content="Cloud Services Architecture & Practice | Fengyu WANG">', head)
    head = re.sub(r'<meta property="og:description" content=".*?">', '<meta property="og:description" content="Cloud services from Docker containerization to Cloudflare deployment \u2014 building scalable, high-availability cloud infrastructure.">', head)
    head = re.sub(r'<meta property="og:url" content="/en/web3.html">', '<meta property="og:url" content="/en/cloud.html">', head)
    head = re.sub(r'<meta name="twitter:title" content=".*?">', '<meta name="twitter:title" content="Cloud Services Architecture & Practice | Fengyu WANG">', head)
    head = re.sub(r'<meta name="twitter:description" content=".*?">', '<meta name="twitter:description" content="Cloud services from Docker to Cloudflare\u2014building scalable cloud infrastructure.">', head)
    head = re.sub(r'data-section="[^"]*"', 'data-section="portfolio"', head)

    body_start = '<body>\n    <div id="shared-subpage-navbar" data-section="portfolio"></div>\n    <script src="../assets/js/shared-subpage-navbar.js?v=26.07.02.01.24"></script>\n\n    <div class="page-wrap">'

    hero = '''
        <div class="container">
            <div class="article-hero" style="background:linear-gradient(135deg, #0f172a 0%, #0284c7 58%, #0ea5e9 100%)">
                <span class="hero-kicker">CLOUD SERVICES</span>
                <h1>Cloud Services Architecture & Practice</h1>
                <p class="subtitle">From Docker containerization to Cloudflare deployment \u2014 building scalable, high-availability cloud infrastructure</p>
                <div class="hero-tags">
                    <span>Docker</span>
                    <span>Cloudflare</span>
                    <span>Reverse Proxy</span>
                    <span>CI/CD</span>
                    <span>Infrastructure</span>
                </div>
            </div>
        </div>
'''

    content = '''
        <div class="article-block">
            <h2>Containerization & Docker</h2>
            <p>Docker containerization is the foundation of modern cloud deployment. It ensures that applications run consistently across environments, from a developer\u2019s laptop to a production server.</p>
            <ul>
                <li><strong>Multi-stage builds</strong>: Optimizing image size by separating build and runtime stages, reducing attack surface and deployment time.</li>
                <li><strong>Docker Compose</strong>: Orchestrating multi-container applications with service definitions, networks, and volumes in a single YAML file.</li>
                <li><strong>Image management</strong>: Tagging, versioning, and pushing images to registries (Docker Hub, GitHub Container Registry) for reproducible deployments.</li>
                <li><strong>Container security</strong>: Running with least-privilege users, read-only root filesystems, and regular image scanning for vulnerabilities.</li>
            </ul>
            <div class="highlight-box">
                <p><strong>Key principle:</strong> If it doesn\u2019t run in a container, it doesn\u2019t run in production. Containerization is the universal interface between code and infrastructure.</p>
            </div>
        </div>

        <div class="article-block">
            <h2>Cloudflare Deployment</h2>
            <p>Cloudflare provides a suite of services that span the entire delivery pipeline \u2014 from DNS to CDN to serverless compute. My deployment workflows leverage Cloudflare extensively.</p>
            <ul>
                <li><strong>Cloudflare Pages</strong>: Deploying static sites and frontend applications with automatic HTTPS, global CDN distribution, and instant cache purging.</li>
                <li><strong>DNS management</strong>: Configuring domain records, load balancing, and failover policies for high availability.</li>
                <li><strong>DDoS protection & WAF</strong>: Using Cloudflare\u2019s security layer to protect applications from common web threats.</li>
                <li><strong>Workers & KV</strong>: Building serverless functions that run at the edge for low-latency, globally distributed logic.</li>
            </ul>
        </div>

        <div class="article-block">
            <h2>Infrastructure Design</h2>
            <p>Good infrastructure design is invisible. When done right, developers deploy without friction and users experience no downtime.</p>
            <ul>
                <li><strong>Scalable architecture</strong>: Designing systems that can grow horizontally \u2014 adding more instances rather than vertically scaling a single server.</li>
                <li><strong>High availability</strong>: Eliminating single points of failure through redundancy, health checks, and auto-recovery mechanisms.</li>
                <li><strong>Reverse proxy & networking</strong>: Using Nginx or Caddy as reverse proxies for SSL termination, load balancing, and request routing.</li>
                <li><strong>Infrastructure as Code (IaC)</strong>: Managing servers, DNS, and deployments through version-controlled configuration files.</li>
            </ul>
        </div>

        <div class="article-block">
            <h2>DevOps & CI/CD</h2>
            <p>Automation is the bridge between code and production. A well-designed CI/CD pipeline turns a git push into a deployed feature with minimal manual intervention.</p>
            <ul>
                <li><strong>Pipeline design</strong>: Building stages for linting, testing, building, and deploying with clear failure points and rollback strategies.</li>
                <li><strong>Monitoring & observability</strong>: Setting up logging, metrics, and alerting to detect issues before users do.</li>
                <li><strong>Secret management</strong>: Handling API keys, tokens, and environment variables securely without hardcoding them into source code.</li>
            </ul>
            <div class="highlight-box">
                <p><strong>Bottom line:</strong> DevOps isn\u2019t a role \u2014 it\u2019s a practice. Everyone on the team should understand the deployment pipeline and be able to ship.</p>
            </div>
        </div>
'''

    page_wrap_close = '    </div>\n\n    <div style="text-align:center; padding:60px 20px 40px;">\n        <img src="../assets/img/team/With Huang.jpg" alt="Photo with Jensen Huang" style="width:240px; max-width:70%; height:auto; border-radius:18px; box-shadow:0 12px 36px rgba(15,23,42,.12);">\n        <p style="margin-top:12px; color:#6b7280; font-size:.82rem; font-style:italic;">With Jensen Huang at HKUST \u2014 I\'m behind him.</p>\n    </div>\n\n    <div id="shared-site-footer"></div>\n    <script src="../assets/js/shared-site-footer.js"></script>'
    
    footer_scripts = html[html.find('<script src="../assets/js/jquery.min.js">'):]

    result = head + '\n</head>\n<body>\n' + body_start + '\n' + hero + '\n' + content + '\n' + page_wrap_close + '\n' + footer_scripts

    with open('en/cloud.html', 'w', encoding='utf-8') as f:
        f.write(result)
    print('Created en/cloud.html')


# Now the Chinese versions
def make_zh_cn_ai():
    with open('zh-cn/web3.html', 'r', encoding='utf-8') as f:
        html = f.read()

    head = html[:html.find('</head>') + 7]
    
    head = re.sub(r'<title>.*?</title>', '<title>AI 工程与自动化 | 王丰羽 Fengyu WANG</title>', head)
    head = re.sub(r'<meta name="description" content=".*?">', '<meta name="description" content="AI 工程系统性梳理\u2014\u2014Harness Engineering、AI Agent 开发、Prompt Engineering、多模型协作与 AI 驱动的工作流自动化。">', head)
    head = re.sub(r'<meta name="keywords" content=".*?">', '<meta name="keywords" content="AI 工程, AI Agent, Harness Engineering, Prompt Engineering, AI 自动化, 多模型协作, 王丰羽">', head)
    head = re.sub(r'<link rel="canonical" href="/zh-cn/web3.html">', '<link rel="canonical" href="/zh-cn/ai.html">', head)
    head = re.sub(r'hreflang="en" href="/en/web3.html"', 'hreflang="en" href="/en/ai.html"', head)
    head = re.sub(r'hreflang="zh-HK" href="/zh-hk/web3.html"', 'hreflang="zh-HK" href="/zh-hk/ai.html"', head)
    head = re.sub(r'<meta property="og:locale" content="zh_HK">', '<meta property="og:locale" content="zh_CN">', head)
    head = re.sub(r'<meta property="og:title" content=".*?">', '<meta property="og:title" content="AI 工程与自动化 | 王丰羽 Fengyu WANG">', head)
    head = re.sub(r'<meta property="og:description" content=".*?">', '<meta property="og:description" content="AI 工程系统性梳理\u2014\u2014Harness Engineering、AI Agent 开发、Prompt Engineering、多模型协作与 AI 驱动的工作流自动化。">', head)
    head = re.sub(r'<meta property="og:url" content="/zh-cn/web3.html">', '<meta property="og:url" content="/zh-cn/ai.html">', head)
    head = re.sub(r'data-section="[^"]*"', 'data-section="portfolio"', head)

    body_start = '<body>\n    <div id="shared-subpage-navbar" data-section="portfolio"></div>\n    <script src="../assets/js/shared-subpage-navbar.js?v=26.07.02.01.24"></script>\n\n    <div class="page-wrap">'

    hero = '''
        <div class="container">
            <div class="article-hero" style="background:linear-gradient(135deg, #0f172a 0%, #3b82f6 58%, #6366f1 100%)">
                <span class="hero-kicker">AI 工程</span>
                <h1>AI 工程与自动化</h1>
                <p class="subtitle">从 Harness Engineering 到 AI Agent\u2014\u2014构建能够思考、行动、迭代的系统</p>
                <div class="hero-tags">
                    <span>Harness Engineering</span>
                    <span>AI Agent 开发</span>
                    <span>Prompt Engineering</span>
                    <span>多模型协作</span>
                    <span>自动化</span>
                </div>
            </div>
        </div>
'''

    content = '''
        <div class="article-block">
            <h2>Harness Engineering</h2>
            <p>Harness Engineering 是协调多个 AI 模型在统一系统中协同工作的实践。不再依赖单一模型，而是将任务路由到最擅长该任务的模型，管理上下文窗口，并在模型表现不佳时执行降级逻辑。</p>
            <ul>
                <li><strong>多模型编排</strong>：根据各模型的能力特长（代码生成、推理、创意写作），将子任务路由到最合适的模型。</li>
                <li><strong>上下文管理</strong>：通过在模型切换时分段和总结上下文，维护长时间对话的连贯性。</li>
                <li><strong>降级与重试</strong>：在 AI 工作流中内置容错机制，单个模型失败不会导致整个流程中断。</li>
                <li><strong>性能监控</strong>：追踪各模型的 Token 消耗、延迟和输出质量，优化成本与速度。</li>
            </ul>
            <div class="highlight-box">
                <p><strong>核心观点：</strong>最好的 AI 系统不是用最强的模型搭建的，而是用最合适的模型组合，各尽其能。</p>
            </div>
        </div>

        <div class="article-block">
            <h2>AI Agent 开发</h2>
            <p>AI Agent 是能够感知环境、做出决策并采取行动以实现特定目标的自主系统。我在这个领域的工作涵盖浏览器自动化 Agent 到自定义工具调用工作流。</p>
            <ul>
                <li><strong>AutoApply 系列</strong>：从 Selenium 迁移到 Playwright 的自动化项目，展示了 Agent 如何导航复杂网页界面。</li>
                <li><strong>自定义 Agent 流水线</strong>：构建结合 LLM 推理与 API 调用、文件 I/O、结构化数据处理的 Agent。</li>
                <li><strong>工具调用模式</strong>：设计 Agent 在决策过程中调用外部工具（搜索、计算器、数据库）的能力。</li>
            </ul>
        </div>

        <div class="article-block">
            <h2>Prompt Engineering</h2>
            <p>Prompt Engineering 是设计输入以从语言模型中获得可靠输出的一门技艺\u2014\u2014融合了语言学、逻辑学和实验方法。</p>
            <ul>
                <li><strong>结构化提示</strong>：使用系统提示词、角色定义和输出格式约束来规范模型行为。</li>
                <li><strong>思维链推理</strong>：将复杂任务分解为逐步推理链，提高准确性和可解释性。</li>
                <li><strong>少样本与零样本模式</strong>：选择合适的范例或编写精确指令，在不浪费 Token 的情况下获得最佳结果。</li>
                <li><strong>迭代优化</strong>：系统化测试提示词变体、衡量输出质量、收敛到最佳表述的方法。</li>
            </ul>
        </div>

        <div class="article-block">
            <h2>AI 驱动的自动化</h2>
            <p>AI 工程的最终目标不是构建聪明的模型，而是将 AI 接入真实工作流，节省时间、减少错误、解锁新能力。</p>
            <ul>
                <li><strong>工作流集成</strong>：通过 API 和 Webhook 将 AI 流水线连接到邮件、日历、CRM 等日常工具。</li>
                <li><strong>数据处理流水线</strong>：使用 AI 从非结构化来源（PDF、邮件、网页）中提取、转换和分析数据。</li>
                <li><strong>人在回路模式</strong>：设计自动化知道何时需要人工审批的机制，既保持自主性又保留控制权。</li>
            </ul>
            <div class="highlight-box">
                <p><strong>总结：</strong>AI 自动化不是取代人，而是消除重复性工作，让人专注于判断、创造和关系。</p>
            </div>
        </div>
'''

    page_wrap_close = '    </div>\n\n    <div style="text-align:center; padding:60px 20px 40px;">\n        <img src="../assets/img/team/With Huang.jpg" alt="与黄仁勋合影" style="width:240px; max-width:70%; height:auto; border-radius:18px; box-shadow:0 12px 36px rgba(15,23,42,.12);">\n        <p style="margin-top:12px; color:#6b7280; font-size:.82rem; font-style:italic;">与黄仁勋于 HKUST 合影\u2014\u2014我在他的后面。</p>\n    </div>\n\n    <div id="shared-site-footer"></div>\n    <script src="../assets/js/shared-site-footer.js"></script>'
    
    footer_scripts = html[html.find('<script src="../assets/js/jquery.min.js">'):]

    result = head + '\n</head>\n<body>\n' + body_start + '\n' + hero + '\n' + content + '\n' + page_wrap_close + '\n' + footer_scripts

    with open('zh-cn/ai.html', 'w', encoding='utf-8') as f:
        f.write(result)
    print('Created zh-cn/ai.html')


def make_zh_cn_cloud():
    with open('zh-cn/web3.html', 'r', encoding='utf-8') as f:
        html = f.read()

    head = html[:html.find('</head>') + 7]
    
    head = re.sub(r'<title>.*?</title>', '<title>云服务架构与实战 | 王丰羽 Fengyu WANG</title>', head)
    head = re.sub(r'<meta name="description" content=".*?">', '<meta name="description" content="云服务实战梳理\u2014\u2014Docker 容器化、Cloudflare 部署、可扩展基础设施、反向代理、CI/CD 与云原生架构。">', head)
    head = re.sub(r'<meta name="keywords" content=".*?">', '<meta name="keywords" content="云服务, Docker, Cloudflare, 云基础设施, DevOps, CI/CD, 王丰羽">', head)
    head = re.sub(r'<link rel="canonical" href="/zh-cn/web3.html">', '<link rel="canonical" href="/zh-cn/cloud.html">', head)
    head = re.sub(r'hreflang="en" href="/en/web3.html"', 'hreflang="en" href="/en/cloud.html"', head)
    head = re.sub(r'hreflang="zh-HK" href="/zh-hk/web3.html"', 'hreflang="zh-HK" href="/zh-hk/cloud.html"', head)
    head = re.sub(r'<meta property="og:locale" content="zh_HK">', '<meta property="og:locale" content="zh_CN">', head)
    head = re.sub(r'<meta property="og:title" content=".*?">', '<meta property="og:title" content="云服务架构与实战 | 王丰羽 Fengyu WANG">', head)
    head = re.sub(r'<meta property="og:description" content=".*?">', '<meta property="og:description" content="云服务实战梳理\u2014\u2014Docker 容器化、Cloudflare 部署、可扩展基础设施、反向代理、CI/CD 与云原生架构。">', head)
    head = re.sub(r'<meta property="og:url" content="/zh-cn/web3.html">', '<meta property="og:url" content="/zh-cn/cloud.html">', head)
    head = re.sub(r'data-section="[^"]*"', 'data-section="portfolio"', head)

    body_start = '<body>\n    <div id="shared-subpage-navbar" data-section="portfolio"></div>\n    <script src="../assets/js/shared-subpage-navbar.js?v=26.07.02.01.24"></script>\n\n    <div class="page-wrap">'

    hero = '''
        <div class="container">
            <div class="article-hero" style="background:linear-gradient(135deg, #0f172a 0%, #0284c7 58%, #0ea5e9 100%)">
                <span class="hero-kicker">云服务</span>
                <h1>云服务架构与实战</h1>
                <p class="subtitle">从 Docker 容器化到 Cloudflare 部署\u2014\u2014构建可扩展、高可用的云基础设施</p>
                <div class="hero-tags">
                    <span>Docker</span>
                    <span>Cloudflare</span>
                    <span>反向代理</span>
                    <span>CI/CD</span>
                    <span>基础设施</span>
                </div>
            </div>
        </div>
'''

    content = '''
        <div class="article-block">
            <h2>容器化与 Docker</h2>
            <p>Docker 容器化是现代云部署的基础。它确保应用在开发者的笔记本到生产服务器的各种环境中都能一致运行。</p>
            <ul>
                <li><strong>多阶段构建</strong>：通过分离构建阶段和运行阶段优化镜像大小，减少攻击面并缩短部署时间。</li>
                <li><strong>Docker Compose</strong>：在单个 YAML 文件中定义服务、网络和卷，编排多容器应用。</li>
                <li><strong>镜像管理</strong>：通过标签、版本控制和推送镜像到仓库（Docker Hub、GitHub Container Registry）实现可重复部署。</li>
                <li><strong>容器安全</strong>：以最小权限用户运行、只读根文件系统、定期镜像漏洞扫描。</li>
            </ul>
            <div class="highlight-box">
                <p><strong>核心原则：</strong>不能容器化的就不上生产。容器化是代码与基础设施之间的通用接口。</p>
            </div>
        </div>

        <div class="article-block">
            <h2>Cloudflare 部署</h2>
            <p>Cloudflare 提供覆盖整个交付链路的一系列服务\u2014\u2014从 DNS 到 CDN 到无服务器计算。我的部署工作流大量利用了 Cloudflare。</p>
            <ul>
                <li><strong>Cloudflare Pages</strong>：部署静态站点和前端应用，自动 HTTPS、全球 CDN 分发、即时缓存清除。</li>
                <li><strong>DNS 管理</strong>：配置域名记录、负载均衡和故障转移策略，实现高可用。</li>
                <li><strong>DDoS 防护与 WAF</strong>：利用 Cloudflare 的安全层保护应用免受常见 Web 威胁。</li>
                <li><strong>Workers 与 KV</strong>：构建运行在边缘节点的无服务器函数，实现低延迟的全球分布式逻辑。</li>
            </ul>
        </div>

        <div class="article-block">
            <h2>基础设施设计</h2>
            <p>好的基础设施设计是隐形的。做对了，开发者可无摩擦部署，用户感受不到停机。</p>
            <ul>
                <li><strong>可扩展架构</strong>：设计能够水平扩展的系统\u2014\u2014增加更多实例而非垂直扩容单一服务器。</li>
                <li><strong>高可用</strong>：通过冗余、健康检查和自动恢复机制消除单点故障。</li>
                <li><strong>反向代理与网络</strong>：使用 Nginx 或 Caddy 作为反向代理，进行 SSL 终止、负载均衡和请求路由。</li>
                <li><strong>基础设施即代码（IaC）</strong>：通过版本控制的配置文件管理服务器、DNS 和部署。</li>
            </ul>
        </div>

        <div class="article-block">
            <h2>DevOps 与 CI/CD</h2>
            <p>自动化是代码到生产的桥梁。设计良好的 CI/CD 流水线将一次 git push 变为已部署的功能，只需最少的人工介入。</p>
            <ul>
                <li><strong>流水线设计</strong>：构建包含 lint、测试、构建和部署阶段的流水线，具备清晰的失败点和回滚策略。</li>
                <li><strong>监控与可观测性</strong>：设置日志、指标和告警，在用户发现问题之前检测异常。</li>
                <li><strong>密钥管理</strong>：安全处理 API 密钥、Token 和环境变量，不硬编码到源码中。</li>
            </ul>
            <div class="highlight-box">
                <p><strong>总结：</strong>DevOps 不是一个岗位，而是一种实践。团队中的每个人都应该理解部署流水线，并且能够发布。</p>
            </div>
        </div>
'''

    page_wrap_close = '    </div>\n\n    <div style="text-align:center; padding:60px 20px 40px;">\n        <img src="../assets/img/team/With Huang.jpg" alt="与黄仁勋合影" style="width:240px; max-width:70%; height:auto; border-radius:18px; box-shadow:0 12px 36px rgba(15,23,42,.12);">\n        <p style="margin-top:12px; color:#6b7280; font-size:.82rem; font-style:italic;">与黄仁勋于 HKUST 合影\u2014\u2014我在他的后面。</p>\n    </div>\n\n    <div id="shared-site-footer"></div>\n    <script src="../assets/js/shared-site-footer.js"></script>'
    
    footer_scripts = html[html.find('<script src="../assets/js/jquery.min.js">'):]

    result = head + '\n</head>\n<body>\n' + body_start + '\n' + hero + '\n' + content + '\n' + page_wrap_close + '\n' + footer_scripts

    with open('zh-cn/cloud.html', 'w', encoding='utf-8') as f:
        f.write(result)
    print('Created zh-cn/cloud.html')


def make_zh_hk_ai():
    with open('zh-hk/web3.html', 'r', encoding='utf-8') as f:
        html = f.read()

    head = html[:html.find('</head>') + 7]
    
    head = re.sub(r'<title>.*?</title>', '<title>AI 工程與自動化 | 王豐羽 Fengyu WANG</title>', head)
    head = re.sub(r'<meta name="description" content=".*?">', '<meta name="description" content="AI 工程系統性梳理\u2014\u2014Harness Engineering、AI Agent 開發、Prompt Engineering、多模型協作與 AI 驅動的工作流自動化。">', head)
    head = re.sub(r'<meta name="keywords" content=".*?">', '<meta name="keywords" content="AI 工程, AI Agent, Harness Engineering, Prompt Engineering, AI 自動化, 多模型協作, 王豐羽">', head)
    head = re.sub(r'<link rel="canonical" href="/zh-hk/web3.html">', '<link rel="canonical" href="/zh-hk/ai.html">', head)
    head = re.sub(r'hreflang="en" href="/en/web3.html"', 'hreflang="en" href="/en/ai.html"', head)
    head = re.sub(r'hreflang="zh-CN" href="/zh-cn/web3.html"', 'hreflang="zh-CN" href="/zh-cn/ai.html"', head)
    head = re.sub(r'<meta property="og:title" content=".*?">', '<meta property="og:title" content="AI 工程與自動化 | 王豐羽 Fengyu WANG">', head)
    head = re.sub(r'<meta property="og:description" content=".*?">', '<meta property="og:description" content="AI 工程系統性梳理\u2014\u2014Harness Engineering、AI Agent 開發、Prompt Engineering、多模型協作與 AI 驅動的工作流自動化。">', head)
    head = re.sub(r'<meta property="og:url" content="/zh-hk/web3.html">', '<meta property="og:url" content="/zh-hk/ai.html">', head)
    head = re.sub(r'data-section="[^"]*"', 'data-section="portfolio"', head)

    body_start = '<body>\n    <div id="shared-subpage-navbar" data-section="portfolio"></div>\n    <script src="../assets/js/shared-subpage-navbar.js?v=26.07.02.01.24"></script>\n\n    <div class="page-wrap">'

    hero = '''
        <div class="container">
            <div class="article-hero" style="background:linear-gradient(135deg, #0f172a 0%, #3b82f6 58%, #6366f1 100%)">
                <span class="hero-kicker">AI 工程</span>
                <h1>AI 工程與自動化</h1>
                <p class="subtitle">從 Harness Engineering 到 AI Agent\u2014\u2014構建能夠思考、行動、迭代的系統</p>
                <div class="hero-tags">
                    <span>Harness Engineering</span>
                    <span>AI Agent 開發</span>
                    <span>Prompt Engineering</span>
                    <span>多模型協作</span>
                    <span>自動化</span>
                </div>
            </div>
        </div>
'''

    content = '''
        <div class="article-block">
            <h2>Harness Engineering</h2>
            <p>Harness Engineering 是協調多個 AI 模型在統一系統中協同工作的實踐。不再依賴單一模型，而是將任務路由到最擅長該任務的模型，管理上下文窗口，並在模型表現不佳時執行降級邏輯。</p>
            <ul>
                <li><strong>多模型編排</strong>：根據各模型的能力特長（代碼生成、推理、創意寫作），將子任務路由到最合適的模型。</li>
                <li><strong>上下文管理</strong>：通過在模型切換時分段和總結上下文，維護長時間對話的連貫性。</li>
                <li><strong>降級與重試</strong>：在 AI 工作流中內置容錯機制，單個模型失敗不會導致整個流程中斷。</li>
                <li><strong>性能監控</strong>：追蹤各模型的 Token 消耗、延遲和輸出質量，優化成本與速度。</li>
            </ul>
            <div class="highlight-box">
                <p><strong>核心觀點：</strong>最好的 AI 系統不是用最強的模型搭建的，而是用最合適的模型組合，各盡其能。</p>
            </div>
        </div>

        <div class="article-block">
            <h2>AI Agent 開發</h2>
            <p>AI Agent 是能夠感知環境、做出決策並採取行動以實現特定目標的自主系統。我在這個領域的工作涵蓋瀏覽器自動化 Agent 到自定義工具調用工作流。</p>
            <ul>
                <li><strong>AutoApply 系列</strong>：從 Selenium 遷移到 Playwright 的自動化項目，展示了 Agent 如何導航複雜網頁界面。</li>
                <li><strong>自定義 Agent 流水線</strong>：構建結合 LLM 推理與 API 調用、文件 I/O、結構化數據處理的 Agent。</li>
                <li><strong>工具調用模式</strong>：設計 Agent 在決策過程中調用外部工具（搜索、計算器、數據庫）的能力。</li>
            </ul>
        </div>

        <div class="article-block">
            <h2>Prompt Engineering</h2>
            <p>Prompt Engineering 是設計輸入以從語言模型中獲得可靠輸出的技藝\u2014\u2014融合了語言學、邏輯學和實驗方法。</p>
            <ul>
                <li><strong>結構化提示</strong>：使用系統提示詞、角色定義和輸出格式約束來規範模型行為。</li>
                <li><strong>思維鏈推理</strong>：將複雜任務分解為逐步推理鏈，提高準確性和可解釋性。</li>
                <li><strong>少樣本與零樣本模式</strong>：選擇合適的範例或編寫精確指令，在不浪費 Token 的情況下獲得最佳結果。</li>
                <li><strong>迭代優化</strong>：系統化測試提示詞變體、衡量輸出質量、收斂到最佳表述的方法。</li>
            </ul>
        </div>

        <div class="article-block">
            <h2>AI 驅動的自動化</h2>
            <p>AI 工程的最終目標不是構建聰明的模型，而是將 AI 接入真實工作流，節省時間、減少錯誤、解鎖新能力。</p>
            <ul>
                <li><strong>工作流集成</strong>：通過 API 和 Webhook 將 AI 流水線連接到郵件、日曆、CRM 等日常工具。</li>
                <li><strong>數據處理流水線</strong>：使用 AI 從非結構化來源（PDF、郵件、網頁）中提取、轉換和分析數據。</li>
                <li><strong>人在回路模式</strong>：設計自動化知道何時需要人工審批的機制，既保持自主性又保留控制權。</li>
            </ul>
            <div class="highlight-box">
                <p><strong>總結：</strong>AI 自動化不是取代人，而是消除重複性工作，讓人專注於判斷、創造和關係。</p>
            </div>
        </div>
'''

    page_wrap_close = '    </div>\n\n    <div style="text-align:center; padding:60px 20px 40px;">\n        <img src="../assets/img/team/With Huang.jpg" alt="與黃仁勳合影" style="width:240px; max-width:70%; height:auto; border-radius:18px; box-shadow:0 12px 36px rgba(15,23,42,.12);">\n        <p style="margin-top:12px; color:#6b7280; font-size:.82rem; font-style:italic;">與黃仁勳於 HKUST 合影\u2014\u2014我在他的後面。</p>\n    </div>\n\n    <div id="shared-site-footer"></div>\n    <script src="../assets/js/shared-site-footer.js"></script>'
    
    footer_scripts = html[html.find('<script src="../assets/js/jquery.min.js">'):]

    result = head + '\n</head>\n<body>\n' + body_start + '\n' + hero + '\n' + content + '\n' + page_wrap_close + '\n' + footer_scripts

    with open('zh-hk/ai.html', 'w', encoding='utf-8') as f:
        f.write(result)
    print('Created zh-hk/ai.html')


def make_zh_hk_cloud():
    with open('zh-hk/web3.html', 'r', encoding='utf-8') as f:
        html = f.read()

    head = html[:html.find('</head>') + 7]
    
    head = re.sub(r'<title>.*?</title>', '<title>雲服務架構與實戰 | 王豐羽 Fengyu WANG</title>', head)
    head = re.sub(r'<meta name="description" content=".*?">', '<meta name="description" content="雲服務實戰梳理\u2014\u2014Docker 容器化、Cloudflare 部署、可擴展基礎設施、反向代理、CI/CD 與雲原生架構。">', head)
    head = re.sub(r'<meta name="keywords" content=".*?">', '<meta name="keywords" content="雲服務, Docker, Cloudflare, 雲基礎設施, DevOps, CI/CD, 王豐羽">', head)
    head = re.sub(r'<link rel="canonical" href="/zh-hk/web3.html">', '<link rel="canonical" href="/zh-hk/cloud.html">', head)
    head = re.sub(r'hreflang="en" href="/en/web3.html"', 'hreflang="en" href="/en/cloud.html"', head)
    head = re.sub(r'hreflang="zh-CN" href="/zh-cn/web3.html"', 'hreflang="zh-CN" href="/zh-cn/cloud.html"', head)
    head = re.sub(r'<meta property="og:title" content=".*?">', '<meta property="og:title" content="雲服務架構與實戰 | 王豐羽 Fengyu WANG">', head)
    head = re.sub(r'<meta property="og:description" content=".*?">', '<meta property="og:description" content="雲服務實戰梳理\u2014\u2014Docker 容器化、Cloudflare 部署、可擴展基礎設施、反向代理、CI/CD 與雲原生架構。">', head)
    head = re.sub(r'<meta property="og:url" content="/zh-hk/web3.html">', '<meta property="og:url" content="/zh-hk/cloud.html">', head)
    head = re.sub(r'data-section="[^"]*"', 'data-section="portfolio"', head)

    body_start = '<body>\n    <div id="shared-subpage-navbar" data-section="portfolio"></div>\n    <script src="../assets/js/shared-subpage-navbar.js?v=26.07.02.01.24"></script>\n\n    <div class="page-wrap">'

    hero = '''
        <div class="container">
            <div class="article-hero" style="background:linear-gradient(135deg, #0f172a 0%, #0284c7 58%, #0ea5e9 100%)">
                <span class="hero-kicker">雲服務</span>
                <h1>雲服務架構與實戰</h1>
                <p class="subtitle">從 Docker 容器化到 Cloudflare 部署\u2014\u2014構建可擴展、高可用的雲基礎設施</p>
                <div class="hero-tags">
                    <span>Docker</span>
                    <span>Cloudflare</span>
                    <span>反向代理</span>
                    <span>CI/CD</span>
                    <span>基礎設施</span>
                </div>
            </div>
        </div>
'''

    content = '''
        <div class="article-block">
            <h2>容器化與 Docker</h2>
            <p>Docker 容器化是現代雲部署的基礎。它確保應用在開發者的筆記本到生產伺服器的各種環境中都能一致運行。</p>
            <ul>
                <li><strong>多階段構建</strong>：通過分離構建階段和運行階段優化鏡像大小，減少攻擊面並縮短部署時間。</li>
                <li><strong>Docker Compose</strong>：在單個 YAML 文件中定義服務、網絡和卷，編排多容器應用。</li>
                <li><strong>鏡像管理</strong>：通過標籤、版本控制和推送鏡像到倉庫（Docker Hub、GitHub Container Registry）實現可重複部署。</li>
                <li><strong>容器安全</strong>：以最小權限用戶運行、唯讀根文件系統、定期鏡像漏洞掃描。</li>
            </ul>
            <div class="highlight-box">
                <p><strong>核心原則：</strong>不能容器化的就不上生產。容器化是代碼與基礎設施之間的通用接口。</p>
            </div>
        </div>

        <div class="article-block">
            <h2>Cloudflare 部署</h2>
            <p>Cloudflare 提供覆蓋整個交付鏈路的一系列服務\u2014\u2014從 DNS 到 CDN 到無伺服器計算。我的部署工作流大量利用了 Cloudflare。</p>
            <ul>
                <li><strong>Cloudflare Pages</strong>：部署靜態站點和前端應用，自動 HTTPS、全球 CDN 分發、即時緩存清除。</li>
                <li><strong>DNS 管理</strong>：配置域名記錄、負載均衡和故障轉移策略，實現高可用。</li>
                <li><strong>DDoS 防護與 WAF</strong>：利用 Cloudflare 的安全層保護應用免受常見 Web 威脅。</li>
                <li><strong>Workers 與 KV</strong>：構建運行在邊緣節點的無伺服器函數，實現低延遲的全球分佈式邏輯。</li>
            </ul>
        </div>

        <div class="article-block">
            <h2>基礎設施設計</h2>
            <p>好的基礎設施設計是隱形的。做對了，開發者可無摩擦部署，用戶感受不到停機。</p>
            <ul>
                <li><strong>可擴展架構</strong>：設計能夠水平擴展的系統\u2014\u2014增加更多實例而非垂直擴容單一伺服器。</li>
                <li><strong>高可用</strong>：通過冗餘、健康檢查和自動恢復機制消除單點故障。</li>
                <li><strong>反向代理與網絡</strong>：使用 Nginx 或 Caddy 作為反向代理，進行 SSL 終止、負載均衡和請求路由。</li>
                <li><strong>基礎設施即代碼（IaC）</strong>：通過版本控制的配置文件管理伺服器、DNS 和部署。</li>
            </ul>
        </div>

        <div class="article-block">
            <h2>DevOps 與 CI/CD</h2>
            <p>自動化是代碼到生產的橋樑。設計良好的 CI/CD 流水線將一次 git push 變為已部署的功能，只需最少的人工介入。</p>
            <ul>
                <li><strong>流水線設計</strong>：構建包含 lint、測試、構建和部署階段的流水線，具備清晰的失敗點和回滾策略。</li>
                <li><strong>監控與可觀測性</strong>：設置日誌、指標和告警，在用戶發現問題之前檢測異常。</li>
                <li><strong>密鑰管理</strong>：安全處理 API 密鑰、Token 和環境變量，不硬編碼到源碼中。</li>
            </ul>
            <div class="highlight-box">
                <p><strong>總結：</strong>DevOps 不是一個崗位，而是一種實踐。團隊中的每個人都應該理解部署流水線，並且能夠發佈。</p>
            </div>
        </div>
'''

    page_wrap_close = '    </div>\n\n    <div style="text-align:center; padding:60px 20px 40px;">\n        <img src="../assets/img/team/With Huang.jpg" alt="與黃仁勳合影" style="width:240px; max-width:70%; height:auto; border-radius:18px; box-shadow:0 12px 36px rgba(15,23,42,.12);">\n        <p style="margin-top:12px; color:#6b7280; font-size:.82rem; font-style:italic;">與黃仁勳於 HKUST 合影\u2014\u2014我在他的後面。</p>\n    </div>\n\n    <div id="shared-site-footer"></div>\n    <script src="../assets/js/shared-site-footer.js"></script>'
    
    footer_scripts = html[html.find('<script src="../assets/js/jquery.min.js">'):]

    result = head + '\n</head>\n<body>\n' + body_start + '\n' + hero + '\n' + content + '\n' + page_wrap_close + '\n' + footer_scripts

    with open('zh-hk/cloud.html', 'w', encoding='utf-8') as f:
        f.write(result)
    print('Created zh-hk/cloud.html')


if __name__ == '__main__':
    make_ai_en()
    make_cloud_en()
    make_zh_cn_ai()
    make_zh_cn_cloud()
    make_zh_hk_ai()
    make_zh_hk_cloud()
    print('\nAll 6 pages created successfully.')

