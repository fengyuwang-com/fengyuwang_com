$path = "C:\Users\a8881\Desktop\fengyuwang_com\zh-hk\cloud.html"
Copy-Item "C:\Users\a8881\Desktop\fengyuwang_com\zh-cn\cloud.html" $path -Force
$content = Get-Content $path -Raw

# Meta - change lang
$content = $content.Replace('<html lang="zh-cn">', '<html lang="zh-hk">')
$content = $content.Replace('<meta property="og:locale" content="zh_CN">', '<meta property="og:locale" content="zh_HK">')

# Apply zh-cn to zh-hk conversions
$replacements = @{
  '云服务基础设施' = '雲端服務基礎設施'
  '云服务是什么、为什么不可替代、以及 AI 与 Web3 如何依赖云基础设施。' = '雲端服務係乜、點解不可替代、以及 AI 與 Web3 如何依賴雲端基礎設施。'
  '云服务, AI基础设施, Web3, 云计算' = '雲端服務, AI基礎設施, Web3, 雲端運算'
  '像用电一样用算力。过去十年最被低估的基础设施变革。' = '用電一樣用算力。過去十年最被低估嘅基礎設施變革。'
  '<h3>像用电一样用算力</h3>' = '<h3>用電一樣用算力</h3>'
  '<h3>有些门，本地推不开</h3>' = '<h3>有些門，本地推唔開</h3>'
  '<h3>试过了，所以知道</h3>' = '<h3>試過咗，所以知道</h3>'
  '<h3>本地跑 AI，天花板就在你的显卡上</h3>' = '<h3>本地跑 AI，天花板就喺你張卡上</h3>'
  '<h3>去中心化的梦，中心化的服务器</h3>' = '<h3>去中心化嘅夢，中心化嘅伺服器</h3>'
  '<h3>技术说话，账本做决定</h3>' = '<h3>技術說話，賬本做決定</h3>'
  '<h2>像用电一样用算力</h2>' = '<h2>用電一樣用算力</h2>'
  '<h2>有些门，本地推不开</h2>' = '<h2>有些門，本地推唔開</h2>'
  '<h2>试过了，所以知道</h2>' = '<h2>試過咗，所以知道</h2>'
  '<h2>本地跑 AI，天花板就在你的显卡上</h2>' = '<h2>本地跑 AI，天花板就喺你張卡上</h2>'
  '<h2>去中心化的梦，中心化的服务器</h2>' = '<h2>去中心化嘅夢，中心化嘅伺服器</h2>'
  '<h2>技术说话，账本做决定</h2>' = '<h2>技術說話，賬本做決定</h2>'
  '云服务的三种形态：SaaS、MaaS 和背后的基础设施逻辑' = '雲端服務三種形態：SaaS、MaaS 同背後嘅基礎設施邏輯'
  '云服务不可替代的四个维度' = '雲端服務不可替代嘅四個維度'
  '自己动手跑过一遍，才知云不可替代' = '自己動手跑過一次，先知雲不可替代'
  '从本地脚本到可调用的云端 AI 服务' = '從本地腳本到可調用嘅雲端 AI 服務'
  '区块链项目对云基础设施的真实依赖' = '區塊鏈項目對雲端基礎設施嘅真實依賴'
  '选择云服务背后的商业逻辑' = '選擇雲端服務背後嘅商業邏輯'
  '<p>SaaS、MaaS 和背后的基础设施逻辑</p>' = '<p>SaaS、MaaS 同背後嘅基礎設施邏輯</p>'
  '<p>云服务不可替代的四个维度</p>' = '<p>雲端服務不可替代嘅四個維度</p>'
  '<p>跨地域组网、容器编排、全栈开发、数据安全、AI 推理——全链路亲手验证</p>' = '<p>跨地域組網、容器編排、全棧開發、數據安全、AI 推理——全鏈路親手驗證</p>'
  '<p>从本地脚本到可调用的云端 AI 服务</p>' = '<p>從本地腳本到可調用嘅雲端 AI 服務</p>'
  '<p>区块链项目对云基础设施的真实依赖</p>' = '<p>區塊鏈項目對雲端基礎設施嘅真實依賴</p>'
  '<p>选择云服务背后的商业逻辑</p>' = '<p>選擇雲端服務背後嘅商業邏輯</p>'
  '<h4>跨地域算力组网</h4>' = '<h4>跨地域算力組網</h4>'
  '<h4>容器化平台</h4>' = '<h4>容器化平台</h4>'
  '<h4>全栈上线</h4>' = '<h4>全棧上線</h4>'
  '<h4>数据安全</h4>' = '<h4>數據安全</h4>'
  '<h4>AI 本地部署</h4>' = '<h4>AI 本地部署</h4>'
  '<h4>Web3 节点</h4>' = '<h4>Web3 節點</h4>'
  '惠州机房 × 香港办公。WireGuard 加密组网，DNS 智能分流。算力成本降 60%，7×24 稳定运行。' = '惠州機房 × 香港辦公。WireGuard 加密組網，DNS 智能分流。算力成本降 60%，7×24 穩定運行。'
  'Docker Compose 编排十余个服务。版本隔离、自动恢复、一键迁移——无单点故障。' = 'Docker Compose 編排十幾個服務。版本隔離、自動恢復、一鍵遷移——無單點故障。'
  'TypeScript + Node.js 项目，GitHub CI/CD。从域名到 SSL 到反向代理，上线全链路独立完成。' = 'TypeScript + Node.js 項目，GitHub CI/CD。從域名到 SSL 到反向代理，上線全鏈路獨立完成。'
  '自研文件加密工具。异地多副本备份 + 定期校验。端口收敛、最小权限、日志审计。' = '自研文件加密工具。異地多副本備份 + 定期校驗。端口收斂、最小權限、日誌審計。'
  '个人 GPU 跑过模型。显存、散热、算力——件件是瓶颈。云上 GPU 按需调用，性能差几个数量级。' = '個人 GPU 跑過模型。顯存、散熱、算力——樣樣係瓶頸。雲上 GPU 按需調用，性能差幾個數量級。'
  '以太坊全节点同步数天。1TB+ SSD、16GB 内存、稳定公网——本地扛不住。三分之一的节点在 AWS 上。' = '以太坊全節點同步數天。1TB+ SSD、16GB 記憶體、穩定公網——本地扛唔住。三分一嘅節點在 AWS 上。'
  '从能力到实践，看真实市场案例' = '從能力到實踐，睇真實市場案例'
  '探索市场学' = '探索市場學'
  '/zh-cn/mkt.html' = '/zh-hk/mkt.html'
  '/zh-cn/cloud.html' = '/zh-hk/cloud.html'
  '<meta name="author" content="王丰羽">' = '<meta name="author" content="王丰羽">'
  '王丰羽' = '王豐羽'
}

foreach ($old in $replacements.Keys) {
  $content = $content.Replace($old, $replacements[$old])
}

# Section 1 body
$content = $content.Replace('云服务的本质很简单：把计算、存储、网络变成像水电一样按需取用的资源。', '雲端服務嘅本質好簡單：將計算、存儲、網絡變成用水電一樣按需取用嘅資源。')
$content = $content.Replace('不需要买硬件、不需要等采购、不需要自己运维。', '唔需要買硬件、唔需要等採購、唔需要自己運維。')
$content = $content.Replace('这个模式催生了三种主要的服务形态：', '呢個模式催生咗三種主要嘅服務形態：')

$s1 = '<p><strong>SaaS（Software as a Service）</strong>——软件即服务。不需要安装，打开浏览器就用。Google Docs、Notion、Figma 都是 SaaS。背后的服务器、数据库、运维全部由提供商管理，用户只需关注业务本身。</p>'
$s1n = '<p><strong>SaaS（Software as a Service）</strong>——軟件即服務。唔使安裝，打開瀏覽器就用。Google Docs、Notion、Figma 都係 SaaS。背後嘅伺服器、數據庫、運維全部由提供商管理，用戶只需關注業務本身。</p>'
$content = $content.Replace($s1, $s1n)

$s2 = '<p><strong>MaaS（Model as a Service）</strong>——模型即服务。AI 模型以 API 的形式提供。调用 OpenAI 的 API 就是在用 MaaS。不需要买 GPU、不需要训练模型、不需要部署推理服务，几行代码就拿到世界顶尖的 AI 能力。</p>'
$s2n = '<p><strong>MaaS（Model as a Service）</strong>——模型即服務。AI 模型以 API 形式提供。調用 OpenAI 嘅 API 就係用 MaaS。唔使買 GPU、唔使訓練模型、唔使部署推理服務，幾行代碼就拎到世界頂尖嘅 AI 能力。</p>'
$content = $content.Replace($s2, $s2n)

$content = $content.Replace('这些服务形态有一个共同点：在本地几乎无法复现。', '呢啲服務形態有一個共同點：在本地幾乎無法複現。')

$content = $content.Replace('<li><strong>按需取用算力</strong>：需要一台服务器，几分钟内创建完成，用完后释放。采购周期从数月压缩到分钟级。</li>', '<li><strong>按需取用算力</strong>：需要一部伺服器，幾分鐘內創建完成，用完後釋放。採購週期從數月壓縮到分鐘級。</li>')
$content = $content.Replace('<li><strong>按量付费</strong>：用多少付多少，没有闲置浪费。入门门槛从数十万降到几块钱。</li>', '<li><strong>按量付費</strong>：用幾多付幾多，冇閒置浪費。入門門檻從數十萬降到幾蚊。</li>')
$content = $content.Replace('<li><strong>全球覆盖</strong>：服务可部署到全球数十个区域，用户从最近的数据中心获取数据。</li>', '<li><strong>全球覆蓋</strong>：服務可部署到全球幾十個區域，用戶從最近嘅數據中心獲取數據。</li>')
$content = $content.Replace('<li><strong>托管服务</strong>：数据库、消息队列、大数据分析——开箱即用，无需自行搭建维护。</li>', '<li><strong>託管服務</strong>：數據庫、消息隊列、大數據分析——開箱即用，無需自行搭建維護。</li>')

# Section 2
$content = $content.Replace('很多人以为云服务的核心优势是"省钱"。这种理解过于表面。', '好多人以為雲端服務嘅核心優勢係「慳錢」。呢種理解太過表面。')
$content = $content.Replace('云服务真正的不可替代性在于：有些事情本地和环境部署物理上就做不到。', '雲端服務真正嘅不可替代性在於：有啲嘢本地同環境部署物理上就做唔到。')

$content = $content.Replace('<li><strong>物理覆盖</strong>：在全球二十个区域同时部署服务，意味着在二十个地方建数据中心。这不是预算问题，是物理上不可能。云厂商的全球基础设施让开发者一次部署，全球可用。</li>', '<li><strong>物理覆蓋</strong>：在全球二十個區域同時部署服務，意味著在二十個地方建數據中心。呢個唔係預算問題，係物理上冇可能。雲端廠商嘅全球基礎設施讓開發者一次部署，全球可用。</li>')
$content = $content.Replace('<li><strong>规模算力</strong>：AI 模型训练需要数百到数千张 GPU 并行计算。自建同等规模的集群需要数月时间、数百万资金。云上将这一过程压缩到几分钟，用完即释放。</li>', '<li><strong>規模算力</strong>：AI 模型訓練需要數百到數千張 GPU 並行計算。自建同等規模嘅集群需要數月時間、數百萬資金。雲端將呢個過程壓縮到幾分鐘，用完即釋放。</li>')
$content = $content.Replace('<li><strong>弹性伸缩</strong>：流量在数秒内暴涨百倍并非罕见——产品上线、营销活动、病毒传播。自建服务器无法应对这种瞬时波动。云平台的自动扩缩可在秒级完成资源调整。</li>', '<li><strong>彈性伸縮</strong>：流量在數秒內暴漲百倍並非罕見——產品上線、營銷活動、病毒傳播。自建伺服器無法應對呢種瞬時波動。雲端平台嘅自動擴縮可在秒級完成資源調整。</li>')
$content = $content.Replace('<li><strong>合规认证</strong>：SOC 2、GDPR、HIPAA 等合规认证，企业自行获取需要数年时间和大量投入。云厂商已具备数百项认证，用户可直接继承。</li>', '<li><strong>合規認證</strong>：SOC 2、GDPR、HIPAA 等合規認證，企業自行獲取需要數年時間同大量投入。雲端廠商已具備數百項認證，用戶可直接繼承。</li>')

$s3 = '<p>SaaS 和 MaaS 天然是云原生的。SaaS 需要 24/7 在线、全球可访问；MaaS 背后是大规模 GPU 推理集群。这些模式在本地环境无法落地。</p>'
$s3n = '<p>SaaS 同 MaaS 天然係雲原生嘅。SaaS 需要 24/7 在線、全球可訪問；MaaS 背後係大規模 GPU 推理集群。呢啲模式在本地環境無法落地。</p>'
$content = $content.Replace($s3, $s3n)

# Link card
$content = $content.Replace('从能力到实践，看真实市场案例', '從能力到實踐，睇真實市場案例')
$content = $content.Replace('探索市场学', '探索市場學')

Set-Content -Path $path -Value $content -Encoding utf8NoBOM
Write-Host "zh-hk/cloud.html synced"

