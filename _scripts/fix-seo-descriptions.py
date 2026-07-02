import os, re

root = r'C:\Users\a8881\Desktop\fengyuwang_com'

zh_cn_desc = {
    'index.html': '王丰羽的个人网站：市场策略、价值投资与软件工程——三个领域，一套底层逻辑。从数据洞察到工程交付，从企业估值到代码实现，用实践连接每一个环节。',
    'mkt.html': '市场学的本质是识别真需求并创造价值连接。本页涵盖数据驱动研究、4P/STP框架、AI时代的营销沟通、SEO策略与全球化市场理解。',
    'portfolio.html': '技术是为了交付。GitHub项目展示：Web应用、跨平台开发、自动化系统、CI/CD流程与AI工程——想得到，做得出的技术能力。',
    'invest.html': '买公司不是买彩票。巴菲特式价值投资框架：企业价值分析、安全边际、概率思维、经济学视角与AI辅助研究，帮你做出更理性的投资决策。',
    'capabilities.html': '三条线，一个根——市场理解力、技术实现力、商业判断力。三种能力互相增强，超越三者之和的价值。查看完整能力树与技能图谱。',
    'web3.html': 'Web3深度研究：核心本质与底层逻辑、全球监管体系对比、商业价值与落地案例、传统企业入局路径，以及五大专题深度分析。',
    'cloud.html': '云服务为什么不可替代？从AI计算力、Web3节点到企业基础设施，解析云原生的真正价值。附真实部署经验与技术对比。',
    'ai.html': 'AI工程不是调API。从Harness Engineering到AI Agent开发，覆盖提示工程、RAG架构、模型部署与自动化工作流的实战记录。',
    '5dt-pd.html': '5DT-PD方法框架：五层x双轨x双循环x三横梁——一套覆盖盈利性内容制造的完整方法与软件工程架构。含极简问答与框架图。'
}

zh_hk_desc = {
    'index.html': '王豐羽的個人網站：市場策略、價值投資與軟件工程——三個領域，一套底層邏輯。從數據洞察到工程交付，從企業估值到代碼實現，用實踐連接每個環節。',
    'mkt.html': '市場學的本質是識別真需求並創造價值連接。本頁涵蓋數據驅動研究、4P/STP框架、AI時代的營銷溝通、SEO策略與全球化市場理解。',
    'portfolio.html': '技術是為了交付。GitHub項目展示：Web應用、跨平台開發、自動化系統、CI/CD流程與AI工程——想得到，做得出的技術能力。',
    'invest.html': '買公司不是買彩票。巴菲特式價值投資框架：企業價值分析、安全邊際、概率思維、經濟學視角與AI輔助研究。',
    'capabilities.html': '三條線，一個根——市場理解力、技術實現力、商業判斷力。三種能力互相增強，超越三者之和的價值。查看完整能力樹。',
    'web3.html': 'Web3深度研究：核心本質與底層邏輯、全球監管體系對比、商業價值與落地案例、傳統企業入局路徑，以及五大專題深度分析。',
    'cloud.html': '雲服務為什麼不可替代？從AI計算力、Web3節點到企業基礎設施，解析雲原生的真正價值。附真實部署經驗與技術對比。',
    'ai.html': 'AI工程不是調API。從Harness Engineering到AI Agent開發，覆蓋提示工程、RAG架構、模型部署與自動化工作流的實戰記錄。',
    '5dt-pd.html': '5DT-PD方法架構：五層x雙軌x雙循環x三橫梁——一套覆蓋盈利性內容製造的完整方法與軟件工程架構。含極簡問答與框架圖。'
}

count = 0
for lang, descs in [('zh-cn', zh_cn_desc), ('zh-hk', zh_hk_desc)]:
    for fname, new_desc in descs.items():
        path = os.path.join(root, lang, fname)
        with open(path, 'r', encoding='utf-8') as f:
            html = f.read()
        html = re.sub(
            r'name="description" content="[^"]*"',
            'name="description" content="' + new_desc + '"',
            html
        )
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        count += 1
        print(f'Updated {lang}/{fname} ({len(new_desc)} chars)')

print(f'\nTotal: {count} descriptions updated')

