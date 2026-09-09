---
title: "為 5DT-PD 立一塊墓碑：人機協作七十五年與一個組織級缺口"
date: 2026-09-10
description: "5DT-PD 退役，五層骨架改名 Feng Human-in-the-Loop 繼續服役。本文梳理人機協作的理論譜系與開源項目對照，指出任務級 HITL 已有標準答案、組織級仍是空位，並給出本站框架的站位與實測成本。"
slug: "tombstone-for-5dt-pd"
tags: ["技術", "商業"]
draft: false
translationKey: "tombstone-5dt-pd"
---

先立一塊碑，再指一塊空地。

> 5DT-PD
>
> 2026 — 2026
>
> 卒於命名：縮寫要先解碼才能懂。
>
> 五層骨架無恙，改名 Feng Human-in-the-Loop，繼續服役。

碑是真的，立在 zh-cn/5dt-pd.html 的問答區第一組，頁面照常開着。URL 不改——鏈接比名字長壽，斷鏈的代價，換不來改址的收益。遺址即 URL。

死因值得多寫一行。縮寫的成本按次收取：每一次轉述、每一回口頭提起，都得先交一遍解碼税；名字在被理解之前要先被翻譯，擋住的就不只是陌生人。退役手續也辦得體面：原稱呼僅存於 URL 與內部鍵，其餘場合一律讓位。碑上刻的退役原因，比多數項目的説明書寫得都誠實。

改名不是翻案，是一次糾錯。Feng Human-in-the-Loop，見詞明義：人在回路裏，由人把關。骨架五層、橫樑三根，一個沒動；動的只是稱呼。名字死了，判斷還活着。

## 任務級的考卷都交了

> 人機協作七十五年，攢出的答案全在同一量級。

2000 年，Parasuraman、Sheridan 與 Wickens 在 IEEE 的論文裏畫了一張至今通用的地圖：自動化到什麼程度，人退到什麼位置。行業沿用至今的是三分法——in-the-loop，人批准才能繼續；on-the-loop，人監控、可隨時叫停；out-of-the-loop，全自動，人只管例外。翻譯成大白話：副駕駛、教練、乘客。

地圖管分配，不管真假。HITL 這個詞，説的人多，過判據的少：人被放進回路，卻從不推翻機器的建議——部分領域人工推翻算法推薦的比例不足 5%，圖章蓋得很勤；到 2026 年，行業綜述還在重複這條批評。檢驗的辦法只有兩問：技術上，人能否決嗎？人否決時，有能力判斷好壞嗎？第二問更難，它有名字，叫自動化自滿（Parasuraman & Manzey 2010）。

23 年後，Lightman 等人補上質量那一半：80 萬步級人工標註證明，對推理的每一步給反饋，顯著優於只對最終結果給反饋（arXiv:2305.20050）。翻譯成大白話：別等期末考再算總賬，每次作業都要批改。階段門禁的學理出處就在這裏——證據高於口説，沒過不放行。

反饋還在下沉。RLHF 把人的判斷逐條餵進模型權重，人最累；Constitutional AI 把原則寫成憲章，AI 審 AI，人退到章程層。前者是逐條審批，後者是立法。憲章化的反饋搬到 agent 組織裏還有一層新意：反饋不進權重，進組織記憶，復盤修的是章程，不是模型。再往前翻，1999 年 Horvitz 已把理想説完：好的協作裏機器也該主動——不確定性高就開口請示，置信夠高再放膽推進。

四條脈絡擺在一起，是同一個落點：全部停在任務級。一個 agent、一次暫停、一次批准——判據、反饋、章程、請示，樣樣有人做。任務級的考卷交齊了；組織級那張，攤在桌上，還空着。

## 開源都擠在同一個量級

> interrupt 那一行，抄的人最多。

| 項目 | 管哪一段 |
|---|---|
| LangGraph | interrupt 暫停、checkpoint 存檔、resume 續跑，連回滾重放都有了名字（Time Travel），任務級 HITL 的事實標準原語 |
| AutoGen | 人以與會者身份進羣聊，走審批放行的工作流 |
| CrewAI | 一個 human_input 開關，任務完成時向人索取輸入 |
| Spec Kit | 規格先行：寫規格、人批准、拆任務、再實現 |

四家合起來，量級沒變：一個任務的暫停、插話、批准、規格。執行層早已飽和，任務級有標準答案可抄，抄的人也確實多。而把一支 agent 隊伍當組織來治理的部分——編制、匯報線、門禁、簽字留痕、復盤、轉正——檢索範圍內沒有現成的開源實現。所有人都在抄同一行代碼，恰好量出了另一層的空。

## 有人會説這是修廟

> 最強反駁：一個函數就夠的事，要什麼編制。

反駁有對的一半。單人單任務，interrupt 確實夠；無責可追的場合，審批單就是廢紙。廟不該亂修。

錯在另一半。interrupt 管暫停與恢復，不管誰有資格批、批了留什麼痕、批錯了誰復盤、下次怎麼不重犯。前者是工程問題，一個函數收尾；後者是組織問題，一個函數收不了。任務會結束，隊伍不會——不會結束的東西，才需要制度。

## 空位上放五個詞

> 編制、門禁、簽字、復盤、轉正。

本站框架的站位就在這五個詞：把 HITL 從任務級抬到組織級。

編制，誰在崗——匯報線是鐵律，supervisor 永不親自寫碼，只管分派與驗收；一人公司不豁免這一條，恰恰相反，一位真人帶數百個 AI 角色，編制與簽字一個都少不了。門禁，階段之間卡質量關，證據高於口説，不過不放行——in-the-loop，過判據的那種，不是圖章。簽字，審批單留痕：誰、何時、批准了什麼——meaningful human control 講的 tracing，事後能沿因果鏈追到具體的人。復盤，教訓寫回組織記憶，章程照此修訂。轉正，達標一個，轉正一個——AI 員工也有人事。

評價也定了四項：打回率、審批延遲、每份可接受交付物的成本、復盤採納率。四項全部從現成台賬回算，不另埋點。階段四的目標——AI 專業人士超過真人——要成立，先從這四項開始度量。

賬單也拿到了。一次完整流程實測：約 4 分鐘，79K 輸入 token 加 21K 輸出 token，$0.0095 一場，摺合人民幣不足一毛。HITL 文獻優化的是準確率與安全；這套框架把第一性指標換掉：每一份可接受的交付物，花多少錢。以成本作第一指標的 HITL 評測，檢索範圍內未見同類——九厘五美元，是目前唯一的實測錨點。

回到碑。名字死於解碼成本，葬在 URL 裏；骨架活下來，站位寫進正文：任務級的世界很滿，組織級空着一層，四條脈絡、四家開源，全繞開了它。

空地就在那裏。下一個把編制、門禁、簽字、復盤寫進開源代碼的，會是誰？

## 參考文獻

1. Parasuraman R., Sheridan T.B., Wickens C.D. (2000). A Model for Types and Levels of Human Interaction with Automation. IEEE Trans. SMC-A.
2. Parasuraman R., Manzey D.H. (2010). Complacency and Bias in Human Use of Automation. Human Factors.
3. Horvitz E. (1999). Principles of Mixed-Initiative User Interfaces. CHI '99.
4. Santoni de Sio F., van den Hoven J. (2018). Meaningful Human Control over Autonomous Systems. Frontiers in Robotics and AI.
5. Christiano P. et al. (2017). Deep RL from Human Preferences. arXiv:1706.03741.
6. Bai Y. et al. (2022). Constitutional AI: Harmlessness from AI Feedback. arXiv:2212.08073.
7. Lightman H. et al. (2023). Let's Verify Step by Step. arXiv:2305.20050.
8. LangChain Blog: Making it easier to build human-in-the-loop agents with interrupt. langchain.com/blog.
