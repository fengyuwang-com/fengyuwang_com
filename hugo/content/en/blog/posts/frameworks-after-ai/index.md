---
title: "AI Writes Everything Now. What's Left for Frameworks?"
date: 2026-09-05
description: "AI eats the flesh and can't eat the skeleton."
slug: "frameworks-after-ai"
tags: ["AI", "Programming"]
draft: false
translationKey: "frameworks-after-ai"
---

A question surfaced while discussing runtimes: if AI can now write everything, are frameworks still necessary? Vue, say — maybe not so necessary anymore?

First, what does a framework actually sell? The runtime is the engine; the framework is the body and the manual. But the needle is inversion of control: you don't call it — it calls you. You fill routes into its slots; when a request arrives, it calls back. A framework sells a complete set of pre-made architecture decisions: where directories go, how requests flow, where code lives.

Can AI make those decisions itself, now that it writes code? Half of them. Implementation is flesh, and flesh just got cheap. Structure is skeleton, and skeleton just got expensive. My first rule of writing code has always been: draw the structure first, then write — once the skeleton is right, flesh attaches naturally. AI turned filling in flesh into a few seconds' work; all remaining time goes into drawing the skeleton.

So frameworks won't die, but the reason for using them changed. You used to use a framework to skip boilerplate — the part AI now writes anyway. Going forward, you use a framework to lay a track for AI: the clearer the conventions, the less the generation drifts. A framework turns from the thing doing your work into the thing that keeps the worker in line.

The cautionary tale already exists. Inside Oracle, inside Microsoft, not one person fully understands their own systems — forty years of accumulated weight, nobody knows how it all works, so all you can do is test. A system sold for a thousand yuan, with testing outsourced to its users through the Insider program. Isn't that funny?

When complexity has no owner, humanity falls back on conventions and tests as the safety net. Now, for the first time, there's an assistant who can carry it.

Whether a framework lives or dies depends on which side of that line it stands on.
