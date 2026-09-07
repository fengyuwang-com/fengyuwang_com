---
title: "我给 Docker 报了一个级联 bug"
date: 2026-09-05
description: "一个 0 字节的文件让引擎起不来，修掉一个，露出下一个。"
slug: "docker-cascade-bug"
tags: ["技术"]
draft: false
translationKey: "docker-cascade-bug"
---

报 bug 这件事，多数人做到"重启就好了"就停了。我停不下来，我想知道是哪一层烂了。

现象很简单：Docker Desktop 从 4.71 起在 Windows Insider Build 26200 上启动就崩，无限循环，到 4.82 还没修。

我扒下去，找到那颗钉子。新加的推理管理器要在 NTFS 上建一个 AF_UNIX socket 文件，Windows 对这种 socket 的实现是借 NTFS 的 reparse point 挂上去的。一旦 Docker 非正常退出——崩溃、强杀、断电——这个 0 字节的文件就留在盘上，带着一个没人认领的标记。下次启动，程序想删它，Windows 报 error 1920，拒绝。程序一看：删不掉，我不活了。崩溃循环。

这不算完，真正的戏在后面。我把这个文件清掉，程序起来又崩在第二个 socket 上：engine.sock。再清，第三个：userAnalyticsOtlpHttp.sock。Cleaning one corrupted socket exposes the next——修掉一个，露出下一个。这不是一个 bug，这是同一根筋烂了三处。

为什么三处都过不去？因为代码里写的是同一条规矩：启动前先清场，清不掉就退出。对必选组件，这条规矩没错。可推理管理器是个可选功能，AI 不用，引擎照样该跑。一个可选服务的遗物，拖死了整台引擎。

我试出来的路子：把父目录改名。文件动不了，目录的名字动得了——改名之后程序找不到旧路径，自己建新的，活了。设置里把 AI 关掉？某些版本里那个开关是摆设，后台照建。最干净的是降级 4.69.0，那个年代关掉 Beta 功能就真的不装推理管理器。

issue 提到 docker/desktop-feedback（#527），我附了三条建议：socket 删不掉不该 fatal；可选服务故障不该拖垮引擎；与其只给一个 Reset to factory defaults，不如告诉用户是哪个文件删不掉。三条都不贵，都是把"我不活了"改成"我绕过去"。

后来我回头审自己的诊断，发现我第一版也有毛病。issue 里我写 MFT 条目损坏，复核下来更像 reparse point 孤儿化：文件的记录还在，指向的内核上下文没了。报 bug 也要自我回测，不然自己就是下一个想当然的人。

一个 0 字节的文件，放倒一台引擎，还连着三处。可靠是底线：不能出错的地方不能出错；会出错的地方，要留活门。
