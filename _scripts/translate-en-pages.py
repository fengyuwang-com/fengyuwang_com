#!/usr/bin/env python3
"""Translate remaining Chinese text in en/cloud.html and en/ai.html to English."""
import re, pathlib

BASE = pathlib.Path(r'C:\Users\a8881\Desktop\fengyuwang_com')

# ─── Common chip translations ───
CHIP_MAP = {
    'Docker 容器化': 'Docker Containerization',
    'SSH 远程管理': 'SSH Remote Management',
    '命令行': 'Command Line',
    '网络诊断': 'Network Diagnostics',
    '算力管理': 'Compute Management',
    '跨平台系统精通': 'Cross-Platform Systems',
    '自动化脚本': 'Automation Scripts',
    'AI 本地部署实战': 'Local AI Deployment',
    'Git 版本管理': 'Git Version Control',
    'AI Agent 开发': 'AI Agent Development',
    '品牌策略': 'Brand Strategy',
    '客户洞察': 'Customer Insight',
    '数字化转型落地': 'Digital Transformation',
    '商业判断力': 'Business Judgment',
    '市场策略': 'Market Strategy',
    'AI Harness Engineering': 'AI Harness Engineering',  # already English
}

# ─── Fix en/cloud.html ───
cloud_path = BASE / 'en' / 'cloud.html'
cloud = cloud_path.read_text('utf-8')

# 1. Card buttons: 了解详情 → Learn More
cloud = cloud.replace('>了解详情<', '>Learn More<')

# 2. Stack chips
for cn, en in CHIP_MAP.items():
    cloud = cloud.replace(f'>{cn}<', f'>{en}<')

# 3. cloud-ai section: full Chinese paragraphs → English
cloud = cloud.replace(
    '<p>AI 自动化工具的开发是典型的从本地到云端的迁移路径。</p>',
    '<p>AI automation tools follow a classic local-to-cloud migration path.</p>'
)
cloud = cloud.replace(
    '<p>AutoApply 系列是基于 Playwright 和 Selenium 开发的 AI Agent，用于自动化信息筛选与投递。当前运行在本地环境，意味着需要持续开机、保持网络稳定、无法并发运行。当一个脚本一天只能处理有限数量的任务时，它的上限就是本地硬件的上限。</p>',
    '<p>The AutoApply series is an AI Agent built on Playwright and Selenium for automated information filtering and submission. Currently running locally, it requires the machine to stay on, the network to stay stable, and cannot run concurrently. When a script can only process a limited number of tasks per day, its ceiling is the ceiling of local hardware.</p>'
)
cloud = cloud.replace(
    '<p>AI Harness Engineering 的工作方式是多模型协作——同时调用 Claude、GPT、DeepSeek 等模型，通过提示工程编排任务逻辑。这套流程目前在本地终端中运行，本质上仍是单机工具。</p>',
    '<p>AI Harness Engineering works through multi-model collaboration — calling Claude, GPT, DeepSeek and others simultaneously, orchestrating task logic through prompt engineering. This workflow currently runs in a local terminal, still essentially a single-machine tool.</p>'
)
cloud = cloud.replace(
    '<p><strong>迁移到云上之后，变化是结构性的：</strong></p>',
    '<p><strong>Migrating to the cloud brings structural changes:</strong></p>'
)

# Cloud-AI list items
cloud = cloud.replace(
    '<li>AutoApply 可打包为 Docker 镜像，部署到云服务器上 24/7 运行，不受本地设备状态影响</li>',
    '<li>AutoApply packaged as a Docker image, deployed to a cloud server running 24/7, unaffected by local device status</li>'
)
cloud = cloud.replace(
    '<li>可同时启动多个实例并行处理，任务量提升一个数量级</li>',
    '<li>Multiple instances run in parallel, increasing throughput by an order of magnitude</li>'
)
cloud = cloud.replace(
    '<li>AI 推理网关统一调度多模型，实现自动路由、容错重试、用量统计</li>',
    '<li>AI inference gateway schedules multiple models, enabling auto-routing, fault-tolerant retries, and usage tracking</li>'
)
cloud = cloud.replace(
    '<li>从"自己用的脚本"变成"可调用的 API 服务"——这是向 MaaS 方向迈进的路径</li>',
    '<li>From "a script for personal use" to "a callable API service" — a step toward MaaS</li>'
)
cloud = cloud.replace(
    '<p>SaaS 和 MaaS 的商业模式本质上是云原生的。要做订阅制的 AI 服务，云是唯一的选项。</p>',
    '<p>SaaS and MaaS business models are inherently cloud-native. To build a subscription-based AI service, the cloud is the only option.</p>'
)

# 4. cloud-web3 section: full Chinese paragraphs → English
cloud = cloud.replace(
    '<p>区块链项目在理念上是去中心化的，在基础设施层面却高度依赖中心化的云服务。这不是矛盾，是物理限制下的最优解。</p>',
    '<p>Blockchain projects are decentralized in concept but heavily depend on centralized cloud infrastructure. This is not a contradiction — it is the optimal solution under physical constraints.</p>'
)
cloud = cloud.replace(
    '<p>本地运行全节点的体验可以说明这一点：一台家用电脑同步以太坊账本需要数天，持续运行后对带宽和存储的占用超出多数个人环境的承受范围。行业数据显示，约三分之一的以太坊节点托管在 AWS 上——这不是项目方偷懒，是个人网络和硬件条件根本扛不住。</p>',
    '<p>Running a full node locally proves this point: a home PC takes days to sync the Ethereum ledger, and sustained operation consumes bandwidth and storage beyond most personal environments. Industry data shows about one-third of all Ethereum nodes are hosted on AWS — not because projects cut corners, but because personal network and hardware simply cannot handle it.</p>'
)
cloud = cloud.replace(
    '<p><strong>Web3 项目对云服务的依赖不止于跑节点：</strong></p>',
    '<p><strong>Web3 reliance on cloud goes beyond running nodes:</strong></p>'
)

# Web3 list items
cloud = cloud.replace(
    '<li><strong>NFT 铸造</strong>：开盘瞬间流量从零暴涨至数万并发，本地服务器无法响应这种瞬时压力</li>',
    '<li><strong>NFT Minting</strong>: traffic spikes from zero to tens of thousands of concurrent requests at launch. Local servers cannot handle that instantaneous pressure</li>'
)
cloud = cloud.replace(
    '<li><strong>DeFi 协议</strong>：需要 24/7 高可用架构和跨区域灾备</li>',
    '<li><strong>DeFi Protocols</strong>: require 24/7 high-availability architecture and cross-region disaster recovery</li>'
)
cloud = cloud.replace(
    '<li><strong>链上数据分析</strong>：区块链数据以 TB 级增长，分析处理必须在云端完成</li>',
    '<li><strong>On-Chain Data Analysis</strong>: blockchain data grows by terabytes, analysis must be done in the cloud</li>'
)
cloud = cloud.replace(
    '<li><strong>交易所</strong>：全球用户需要低延迟访问，必须依赖多区域部署</li>',
    '<li><strong>Exchanges</strong>: global users need low-latency access, requiring multi-region deployment</li>'
)
cloud = cloud.replace(
    '<p><strong>发展方向：</strong>将 Web3 基础设施部署标准化，用 Docker 和自动化脚本实现区块链节点的一键部署、自动监控与故障恢复。同时搭建从节点同步到数据清洗、入库、可视化的完整数据管道。</p>',
    '<p><strong>Direction:</strong> standardize Web3 infrastructure deployment — one-click blockchain node setup, auto-monitoring, and fault recovery using Docker and automation scripts. Meanwhile, build a complete data pipeline from node sync to data cleaning, storage, and visualization.</p>'
)

# 5. business-case section
cloud = cloud.replace(
    '<p>从商业角度审视云服务，价值比技术层面更清晰：</p>',
    '<p>Looking at cloud from a business perspective makes the value clearer than from the technical side:</p>'
)

# Business case list items
cloud = cloud.replace(
    '<li><strong>改变成本结构</strong>：固定资产投入转为按需运营支出。资金配置更灵活，现金流压力更小。</li>',
    '<li><strong>Change Cost Structure</strong>: fixed asset investment becomes on-demand operational expense. More flexible capital allocation, less cash flow pressure.</li>'
)
cloud = cloud.replace(
    '<li><strong>压缩交付周期</strong>：基础设施不再成为交付瓶颈。从新服务上线到全球部署，时间单位从月缩短到天。</li>',
    '<li><strong>Compress Delivery Cycles</strong>: infrastructure is no longer a delivery bottleneck. From new service launch to global deployment, time goes from months to days.</li>'
)
cloud = cloud.replace(
    '<li><strong>释放团队产能</strong>：运维基础设施的人力成本往往是隐性却最高的。将这部分工作外包给云厂商，团队可专注于构建核心业务。</li>',
    '<li><strong>Free Up Team Capacity</strong>: infrastructure ops is often the highest hidden cost. Outsource it to cloud providers so the team can focus on core business.</li>'
)
cloud = cloud.replace(
    '<li><strong>打开市场范围</strong>：全球部署能力让小团队也能服务全球用户。市场边界不再受基础设施限制。</li>',
    '<li><strong>Expand Market Reach</strong>: global deployment lets small teams serve users worldwide. Market boundaries are no longer limited by infrastructure.</li>'
)
cloud = cloud.replace(
    '<li><strong>SaaS/MaaS 的商业模式</strong>：订阅制服务、按量计费的模型天然依赖云基础设施。如果业务方向是提供可调用的服务，云是唯一的可行路径。</li>',
    '<li><strong>SaaS/MaaS Business Model</strong>: subscription services and usage-based pricing naturally depend on cloud infrastructure. If the business direction is to provide callable services, cloud is the only viable path.</li>'
)
cloud = cloud.replace(
    '<p>技术能力、商业判断、市场理解——三个方向相互支撑。云服务的落地既需要技术理解，也需要商业语言将其转化为决策依据。</p>',
    '<p>Technical capability, business judgment, market understanding — three directions that reinforce each other. Making cloud work requires both technical understanding and business language to translate it into decisions.</p>'
)

# 6. Fix og:url (was pointing to zh-cn)
cloud = cloud.replace(
    '<meta property="og:url" content="https://fengyuwang.com/zh-cn/cloud.html">',
    '<meta property="og:url" content="https://fengyuwang.com/en/cloud.html">'
)
# Fix hreflang zh-CN (was pointing to en)
cloud = cloud.replace(
    '<link rel="alternate" hreflang="zh-CN" href="/en/cloud.html">',
    '<link rel="alternate" hreflang="zh-CN" href="/zh-cn/cloud.html">'
)

# Remove Cloudflare beacon from en/cloud.html (if present)
cloud = re.sub(
    r'<script defer src="https://static\.cloudflareinsights\.com/beacon\.min\.js"[^>]*></script>\s*',
    '', cloud
)

cloud_path.write_text(cloud, 'utf-8')
print(f'en/cloud.html: translated {CHIP_MAP.keys()} chips, 6 buttons, AI/Web3/Biz sections')

# ─── Fix en/ai.html ───
ai_path = BASE / 'en' / 'ai.html'
ai = ai_path.read_text('utf-8')

# 1. Card buttons
ai = ai.replace('>了解详情<', '>Learn More<')

# 2. Harness section
ai = ai.replace(
    '<li><strong>多模型编排</strong>：根据各模型的能力特长，将子任务路由到最合适的模型。</li>',
    '<li><strong>Multi-Model Orchestration</strong>: route subtasks to the most suitable model based on each model\'s strengths.</li>'
)
ai = ai.replace(
    '<li><strong>上下文管理</strong>：在模型切换时分段和总结上下文，维护长时间对话的连贯性。</li>',
    '<li><strong>Context Management</strong>: segment and summarize context during model switching to maintain coherence across long conversations.</li>'
)
ai = ai.replace(
    '<li><strong>降级与重试</strong>：在 AI 工作流中内置容错机制，单个模型失败不会导致整个流程中断。</li>',
    '<li><strong>Degradation & Retry</strong>: built-in fault tolerance in AI workflows so a single model failure won\'t interrupt the entire flow.</li>'
)
ai = ai.replace(
    '<li><strong>性能监控</strong>：追踪各模型的 Token 消耗、延迟和输出质量，优化成本与速度。</li>',
    '<li><strong>Performance Monitoring</strong>: track token consumption, latency, and output quality across models to optimize cost and speed.</li>'
)

# 3. Agent section
ai = ai.replace(
    '<li><strong>浏览器自动化 Agent</strong>：从 Selenium 迁移到 Playwright，展示 Agent 如何导航复杂网页界面。</li>',
    '<li><strong>Browser Automation Agent</strong>: migrated from Selenium to Playwright, demonstrating how Agents navigate complex web interfaces.</li>'
)
ai = ai.replace(
    '<li><strong>自定义 Agent 流水线</strong>：构建结合 LLM 推理与 API 调用、文件 I/O、结构化数据处理的 Agent。</li>',
    '<li><strong>Custom Agent Pipeline</strong>: build Agents that combine LLM reasoning with API calls, file I/O, and structured data processing.</li>'
)
ai = ai.replace(
    '<li><strong>工具调用模式</strong>：设计 Agent 在决策过程中调用外部工具的能力。</li>',
    '<li><strong>Tool Calling Pattern</strong>: design the Agent\'s ability to call external tools during decision-making.</li>'
)

# 4. Prompt section
ai = ai.replace(
    '<li><strong>结构化提示</strong>：使用系统提示词、角色定义和输出格式约束来规范模型行为。</li>',
    '<li><strong>Structured Prompting</strong>: use system prompts, role definitions, and output format constraints to regulate model behavior.</li>'
)
ai = ai.replace(
    '<li><strong>思维链推理</strong>：将复杂任务分解为逐步推理链，提高准确性和可解释性。</li>',
    '<li><strong>Chain-of-Thought Reasoning</strong>: break complex tasks into step-by-step reasoning chains for improved accuracy and interpretability.</li>'
)
ai = ai.replace(
    '<li><strong>少样本与零样本模式</strong>：选择合适的范例或编写精确指令，在不浪费 Token 的情况下获得最佳结果。</li>',
    '<li><strong>Few-Shot & Zero-Shot</strong>: choose appropriate examples or write precise instructions to get the best results without wasting tokens.</li>'
)
ai = ai.replace(
    '<li><strong>迭代优化</strong>：系统化测试提示词变体、衡量输出质量、收敛到最佳表述。</li>',
    '<li><strong>Iterative Optimization</strong>: systematically test prompt variants, measure output quality, and converge on the best expression.</li>'
)

# 5. Automation section
ai = ai.replace(
    '<li><strong>工作流集成</strong>：通过 API 和 Webhook 将 AI 流水线连接到邮件、日历、CRM 等日常工具。</li>',
    '<li><strong>Workflow Integration</strong>: connect AI pipelines to email, calendar, CRM, and other daily tools via API and Webhook.</li>'
)
ai = ai.replace(
    '<li><strong>数据处理流水线</strong>：使用 AI 从非结构化来源中提取、转换和分析数据。</li>',
    '<li><strong>Data Processing Pipeline</strong>: use AI to extract, transform, and analyze data from unstructured sources.</li>'
)
ai = ai.replace(
    '<li><strong>人在回路模式</strong>：设计自动化知道何时需要人工审批的机制。</li>',
    '<li><strong>Human-in-the-Loop</strong>: design mechanisms where automation knows when human approval is needed.</li>'
)

# 6. Remove Cloudflare beacon from en/ai.html
ai = re.sub(
    r'<script defer src="https://static\.cloudflareinsights\.com/beacon\.min\.js"[^>]*></script>\s*',
    '', ai
)

# 7. Fix og:url for en/ai.html (check if pointing correctly)
# Currently: <meta property="og:url" content="https://fengyuwang.com/en/ai.html"> — seems correct already

ai_path.write_text(ai, 'utf-8')
print('en/ai.html: translated 4 buttons, Harness/Agent/Prompt/Automation sections, removed CF beacon')
print('Done')

