---
title: "我給 Docker 報了一個級聯 bug"
date: 2026-09-05
description: "一個 0 字節的文件讓引擎起不來，修掉一個，露出下一個。"
slug: "docker-cascade-bug"
tags: ["Docker", "調試"]
draft: false
translationKey: "docker-cascade-bug"
---

報 bug 這件事，多數人做到"重啓就好了"就停了。我停不下來，我想知道是哪一層爛了。

現象很簡單：Docker Desktop 從 4.71 起在 Windows Insider Build 26200 上啓動就崩，無限循環，到 4.82 還沒修。

我扒下去，找到那顆釘子。新加的推理管理器要在 NTFS 上建一個 AF_UNIX socket 文件，Windows 對這種 socket 的實現是借 NTFS 的 reparse point 掛上去的。一旦 Docker 非正常退出——崩潰、強殺、斷電——這個 0 字節的文件就留在盤上，帶着一個沒人認領的標記。下次啓動，程序想刪它，Windows 報 error 1920，拒絕。程序一看：刪不掉，我不活了。崩潰循環。

這不算完，真正的戲在後面。我把這個文件清掉，程序起來又崩在第二個 socket 上：engine.sock。再清，第三個：userAnalyticsOtlpHttp.sock。Cleaning one corrupted socket exposes the next——修掉一個，露出下一個。這不是一個 bug，這是同一根筋爛了三處。

為什麼三處都過不去？因為代碼裏寫的是同一條規矩：啓動前先清場，清不掉就退出。對必選組件，這條規矩沒錯。可推理管理器是個可選功能，AI 不用，引擎照樣該跑。一個可選服務的遺物，拖死了整台引擎。

我試出來的路子：把父目錄改名。文件動不了，目錄的名字動得了——改名之後程序找不到舊路徑，自己建新的，活了。設置裏把 AI 關掉？某些版本里那個開關是擺設，後台照建。最乾淨的是降級 4.69.0，那個年代關掉 Beta 功能就真的不裝推理管理器。

issue 提到 docker/desktop-feedback（#527），我附了三條建議：socket 刪不掉不該 fatal；可選服務故障不該拖垮引擎；與其只給一個 Reset to factory defaults，不如告訴用户是哪個文件刪不掉。三條都不貴，都是把"我不活了"改成"我繞過去"。

後來我回頭審自己的診斷，發現我第一版也有毛病。issue 裏我寫 MFT 條目損壞，複核下來更像 reparse point 孤兒化：文件的記錄還在，指向的內核上下文沒了。報 bug 也要自我回測，不然自己就是下一個想當然的人。

一個 0 字節的文件，放倒一台引擎，還連着三處。可靠是底線：不能出錯的地方不能出錯；會出錯的地方，要留活門。
