$path = "C:\Users\a8881\Desktop\fengyuwang_com\en\cloud.html"
Copy-Item "C:\Users\a8881\Desktop\fengyuwang_com\zh-cn\cloud.html" $path -Force
$content = Get-Content $path -Raw

# Meta
$content = $content.Replace('<html lang="zh-cn">', '<html lang="en">')
$content = $content.Replace('<title>云服务基础设施', '<title>Cloud Infrastructure')
$content = $content.Replace('云服务是什么、为什么不可替代、以及 AI 与 Web3 如何依赖云基础设施。', 'What cloud is, why it is irreplaceable, and how AI and Web3 depend on it.')
$content = $content.Replace('云服务, AI基础设施, Web3, 云计算', 'Cloud Infrastructure, AI, Web3, Cloud Computing')
$content = $content.Replace('<meta name="author" content="王丰羽">', '<meta name="author" content="Fengyu WANG">')
$content = $content.Replace('<meta property="og:locale" content="zh_CN">', '<meta property="og:locale" content="en_US">')
$content = $content.Replace('<meta property="og:title" content="云服务基础设施', '<meta property="og:title" content="Cloud Infrastructure')
$content = $content.Replace('<meta name="twitter:title" content="云服务基础设施', '<meta name="twitter:title" content="Cloud Infrastructure')

# Hero
$content = $content.Replace('云服务基础设施', 'Cloud Infrastructure')
$content = $content.Replace('像用电一样用算力。过去十年最被低估的基础设施变革。', 'Computing power like electricity. The most underestimated infrastructure shift of the past decade.')

# Card h3
$content = $content.Replace('<h3>像用电一样用算力</h3>', '<h3>Computing Like Electricity</h3>')
$content = $content.Replace('<h3>有些门，本地推不开</h3>', '<h3>Doors That Won@q@t Open Locally</h3>')
$content = $content.Replace('<h3>试过了，所以知道</h3>', '<h3>Tried It, So I Know</h3>')
$content = $content.Replace('<h3>本地跑 AI，天花板就在你的显卡上</h3>', '<h3>Local AI Hits Your GPU Ceiling</h3>')
$content = $content.Replace('<h3>去中心化的梦，中心化的服务器</h3>', '<h3>Decentralized Dream, Centralized Servers</h3>')
$content = $content.Replace('<h3>技术说话，账本做决定</h3>', '<h3>Tech Talks, Books Decide</h3>')

# Fix the temporary marker
$content = $content.Replace("Won@q@t", "Won't")

# Card p
$content = $content.Replace('<p>SaaS、MaaS 和背后的基础设施逻辑</p>', '<p>SaaS, MaaS, and the infrastructure logic behind them</p>')
$content = $content.Replace('<p>云服务不可替代的四个维度</p>', '<p>Four dimensions where on-premises cannot compete</p>')
$content = $content.Replace('<p>跨地域组网、容器编排、全栈开发、数据安全、AI 推理——全链路亲手验证</p>', '<p>Cross-region networking, container orchestration, full-stack dev, data security, AI inference</p>')
$content = $content.Replace('<p>从本地脚本到可调用的云端 AI 服务</p>', '<p>From local scripts to callable cloud AI services</p>')
$content = $content.Replace('<p>区块链项目对云基础设施的真实依赖</p>', '<p>How blockchain projects truly depend on cloud infrastructure</p>')
$content = $content.Replace('<p>选择云服务背后的商业逻辑</p>', '<p>The business logic behind choosing cloud services</p>')

# Section h2 (same as card h3 but these were already replaced above)
# Just to be safe, use the remaining ones
$content = $content.Replace('<h2>像用电一样用算力</h2>', '<h2>Computing Like Electricity</h2>')
$content = $content.Replace('<h2>有些门，本地推不开</h2>', '<h2>Doors That Won@q@t Open Locally</h2>')
$content = $content.Replace('<h2>试过了，所以知道</h2>', '<h2>Tried It, So I Know</h2>')
$content = $content.Replace('<h2>本地跑 AI，天花板就在你的显卡上</h2>', '<h2>Local AI Hits Your GPU Ceiling</h2>')
$content = $content.Replace('<h2>去中心化的梦，中心化的服务器</h2>', '<h2>Decentralized Dream, Centralized Servers</h2>')
$content = $content.Replace('<h2>技术说话，账本做决定</h2>', '<h2>Tech Talks, Books Decide</h2>')
$content = $content.Replace("Won@q@t", "Won't")

# Section subtitles
$content = $content.Replace('云服务的三种形态：SaaS、MaaS 和背后的基础设施逻辑', 'SaaS, MaaS, and the infrastructure logic behind them')
$content = $content.Replace('云服务不可替代的四个维度', 'Four dimensions where on-premises cannot compete')
$content = $content.Replace('自己动手跑过一遍，才知云不可替代', 'Run it yourself once, and cloud becomes undeniable')
$content = $content.Replace('从本地脚本到可调用的云端 AI 服务', 'From local scripts to callable cloud AI services')
$content = $content.Replace('区块链项目对云基础设施的真实依赖', 'How blockchain projects truly depend on cloud infrastructure')
$content = $content.Replace('选择云服务背后的商业逻辑', 'The business logic behind choosing cloud services')

# Section 1 body key paragraphs
$content = $content.Replace('云服务的本质很简单：把计算、存储、网络变成像水电一样按需取用的资源。', 'The essence of cloud is simple: turn compute, storage, and network into utilities you consume on demand.')
$content = $content.Replace('不需要买硬件、不需要等采购、不需要自己运维。', 'No hardware to buy, no procurement delays, no self-managed ops.')
$content = $content.Replace('这个模式催生了三种主要的服务形态：', 'This model created three main service forms:')

$saasOld = '<p><strong>SaaS（Software as a Service）</strong>——软件即服务。不需要安装，打开浏览器就用。Google Docs、Notion、Figma 都是 SaaS。背后的服务器、数据库、运维全部由提供商管理，用户只需关注业务本身。</p>'
$saasNew = '<p><strong>SaaS (Software as a Service)</strong> - no installation, just open the browser. Google Docs, Notion, Figma. Servers, databases, ops are all managed by the provider. Users focus on the business.</p>'
$content = $content.Replace($saasOld, $saasNew)

$maasOld = '<p><strong>MaaS（Model as a Service）</strong>——模型即服务。AI 模型以 API 的形式提供。调用 OpenAI 的 API 就是在用 MaaS。不需要买 GPU、不需要训练模型、不需要部署推理服务，几行代码就拿到世界顶尖的 AI 能力。</p>'
$maasNew = '<p><strong>MaaS (Model as a Service)</strong> - AI models delivered as APIs. Calling the OpenAI API is using MaaS. No GPU, no training, no inference deployment - world-class AI with a few lines of code.</p>'
$content = $content.Replace($maasOld, $maasNew)

$content = $content.Replace('这些服务形态有一个共同点：在本地几乎无法复现。', 'These services share one thing: they are nearly impossible to replicate locally.')

$content = $content.Replace('<li><strong>按需取用算力</strong>：需要一台服务器，几分钟内创建完成，用完后释放。采购周期从数月压缩到分钟级。</li>', '<li><strong>On-demand compute</strong>: spin up a server in minutes, release when done. Procurement from months to minutes.</li>')
$content = $content.Replace('<li><strong>按量付费</strong>：用多少付多少，没有闲置浪费。入门门槛从数十万降到几块钱。</li>', '<li><strong>Pay-as-you-go</strong>: pay for what you use, no idle waste. Entry barrier from thousands to pennies.</li>')
$content = $content.Replace('<li><strong>全球覆盖</strong>：服务可部署到全球数十个区域，用户从最近的数据中心获取数据。</li>', '<li><strong>Global reach</strong>: deploy across dozens of regions worldwide. Users served from the nearest datacenter.</li>')
$content = $content.Replace('<li><strong>托管服务</strong>：数据库、消息队列、大数据分析——开箱即用，无需自行搭建维护。</li>', '<li><strong>Managed services</strong>: databases, message queues, big data analytics - ready out of the box, no self-hosting.</li>')

# Section 2 key paragraphs
$content = $content.Replace('很多人以为云服务的核心优势是"省钱"。这种理解过于表面。', 'Many think cloud is about saving money. That view is too shallow.')
$content = $content.Replace('云服务真正的不可替代性在于：有些事情本地和环境部署物理上就做不到。', 'What makes cloud truly irreplaceable: some things are physically impossible on-premises.')
$content = $content.Replace('<li><strong>物理覆盖</strong>：在全球二十个区域同时部署服务，意味着在二十个地方建数据中心。这不是预算问题，是物理上不可能。云厂商的全球基础设施让开发者一次部署，全球可用。</li>', '<li><strong>Physical coverage</strong>: deploying in 20 regions means 20 datacenters. Not a budget issue - physically impossible. Cloud makes one deployment globally available.</li>')
$content = $content.Replace('<li><strong>规模算力</strong>：AI 模型训练需要数百到数千张 GPU 并行计算。自建同等规模的集群需要数月时间、数百万资金。云上将这一过程压缩到几分钟，用完即释放。</li>', '<li><strong>Scale compute</strong>: AI training needs hundreds to thousands of GPUs. Building that on-prem takes months and millions. Cloud compresses it to minutes.</li>')
$content = $content.Replace('<li><strong>弹性伸缩</strong>：流量在数秒内暴涨百倍并非罕见——产品上线、营销活动、病毒传播。自建服务器无法应对这种瞬时波动。云平台的自动扩缩可在秒级完成资源调整。</li>', '<li><strong>Elastic scaling</strong>: traffic can spike 100x in seconds - product launch, campaign, viral spread. On-prem cannot handle that. Cloud auto-scales in seconds.</li>')
$content = $content.Replace('<li><strong>合规认证</strong>：SOC 2、GDPR、HIPAA 等合规认证，企业自行获取需要数年时间和大量投入。云厂商已具备数百项认证，用户可直接继承。</li>', '<li><strong>Compliance</strong>: SOC 2, GDPR, HIPAA - earning these takes years and huge investment. Cloud providers already have hundreds of certifications customers inherit.</li>')

$saaSaaS = '<p>SaaS 和 MaaS 天然是云原生的。SaaS 需要 24/7 在线、全球可访问；MaaS 背后是大规模 GPU 推理集群。这些模式在本地环境无法落地。</p>'
$saaSaaSNew = '<p>SaaS and MaaS are cloud-native by nature. SaaS needs 24/7 global availability; MaaS runs on massive GPU inference clusters. Neither works on-premises.</p>'
$content = $content.Replace($saaSaaS, $saaSaaSNew)

# Section 3 - exp cards
$content = $content.Replace('<h4>跨地域算力组网</h4>', '<h4>Cross-Region Compute</h4>')
$content = $content.Replace('<h4>容器化平台</h4>', '<h4>Container Platform</h4>')
$content = $content.Replace('<h4>全栈上线</h4>', '<h4>Full-Stack Ship</h4>')
$content = $content.Replace('<h4>数据安全</h4>', '<h4>Data Security</h4>')
$content = $content.Replace('<h4>AI 本地部署</h4>', '<h4>Local AI</h4>')
$content = $content.Replace('<h4>Web3 节点</h4>', '<h4>Web3 Nodes</h4>')

$content = $content.Replace('惠州机房 × 香港办公。WireGuard 加密组网，DNS 智能分流。算力成本降 60%，7×24 稳定运行。', 'Huizhou server x Hong Kong office. WireGuard encrypted mesh, smart DNS routing. 60% cost reduction, 7x24 stable operation.')
$content = $content.Replace('Docker Compose 编排十余个服务。版本隔离、自动恢复、一键迁移——无单点故障。', 'Docker Compose orchestrating a dozen services. Version isolation, auto-recovery, one-click migration. No single point of failure.')
$content = $content.Replace('TypeScript + Node.js 项目，GitHub CI/CD。从域名到 SSL 到反向代理，上线全链路独立完成。', 'TypeScript + Node.js projects, GitHub CI/CD. From domain to SSL to reverse proxy - full deployment chain handled independently.')
$content = $content.Replace('自研文件加密工具。异地多副本备份 + 定期校验。端口收敛、最小权限、日志审计。', 'Self-built file encryption. Multi-site backup + periodic verification. Port hardening, least-privilege, audit logging.')
$content = $content.Replace('个人 GPU 跑过模型。显存、散热、算力——件件是瓶颈。云上 GPU 按需调用，性能差几个数量级。', 'Ran models on personal GPUs. VRAM, cooling, compute - every piece a bottleneck. Cloud GPUs on demand, orders of magnitude faster.')
$content = $content.Replace('以太坊全节点同步数天。1TB+ SSD、16GB 内存、稳定公网——本地扛不住。三分之一的节点在 AWS 上。', 'Ethereum full node sync takes days. 1TB+ SSD, 16GB RAM, stable public IP - local cannot handle it. A third of all nodes on AWS.')

# Exp chips
$content = $content.Replace('<span>混合云架构</span><span>成本优化</span><span>跨境网络</span>', '<span>Hybrid Cloud</span><span>Cost Optimization</span><span>Cross-Border Network</span>')
$content = $content.Replace('<span>容器编排</span><span>运维自动化</span><span>高可用设计</span>', '<span>Container Orchestration</span><span>Ops Automation</span><span>High Availability</span>')
$content = $content.Replace('<span>全栈开发</span><span>DevOps</span><span>CI/CD</span>', '<span>Full-Stack Dev</span><span>DevOps</span><span>CI/CD</span>')
$content = $content.Replace('<span>数据安全</span><span>合规设计</span><span>风险防控</span>', '<span>Data Security</span><span>Compliance</span><span>Risk Management</span>')
$content = $content.Replace('<span>AI 基础设施</span><span>算力评估</span>', '<span>AI Infrastructure</span><span>Compute Assessment</span>')
$content = $content.Replace('<span>区块链基础设施</span><span>节点运维</span>', '<span>Blockchain Infrastructure</span><span>Node Ops</span>')

# Link card
$content = $content.Replace('从能力到实践，看真实市场案例', 'From capability to practice - see real market cases')
$content = $content.Replace('探索市场学', 'Explore Marketing')
$content = $content.Replace('/zh-cn/mkt.html', '/en/mkt.html')

# Canonical
$content = $content.Replace('href="/zh-cn/cloud.html"', 'href="/en/cloud.html"')

Set-Content -Path $path -Value $content -Encoding utf8NoBOM
Write-Host "en/cloud.html synced"

