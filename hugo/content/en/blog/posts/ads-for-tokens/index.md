---
title: "Ads for Tokens: Why Nobody Gets to Make AI Free"
date: 2026-09-23
description: "AI's marginal cost is a law of physics — it won't allow free at scale."
slug: "ads-for-tokens"
tags: ["AI", "Business Model"]
draft: true
translationKey: "ads-for-tokens"
---

## An obvious question

If AI chats cost this much, why hasn't anyone built a "watch ads, earn tokens" model? It worked for free-to-play games, free reading, free search — trade eyeballs for a subsidy, dead simple.

People have tried. Platforms like Whyl, Idlen, and OpenEarn hand out chat credits for a 15-second ad; infr.ad drops ASCII sponsor ads at the end of terminal output in exchange for a free API; ChatGPT itself is testing ads on its free tier.

None of them took off. The reason is a bit of arithmetic.

## The unit economics

- Cost of one AI chat: $0.01–0.15 (depending on the model and token count)
- Revenue from one ad: $0.001–0.01 (industry CPM average)
- Ads needed to break even per chat: 5–150

A developer running agents burns millions of tokens a day. Making them watch tens of thousands of ads to stay "free" isn't a business model — it's a punishment.

## Why this worked for SaaS but not for AI

In traditional SaaS, the marginal cost of user one and user ten thousand is basically the same. One more person watching an ads changes your server bill by roughly zero. So the flywheel spins: ad subsidy → user growth → economies of scale → profit.

AI isn't like that. Every extra chat burns GPU power again. Compute cost grows linearly with usage — no scale discount the way storage and bandwidth have. Ad revenue is a small fixed amount; chat cost is a straight line. The two lines never cross.

## Enterprise kills it outright

Imagine pasting a contract, a medical record, or internal code into an AI — and a banner pops up: "find a lawyer near you," "health check packages," "cloud storage coupon." Instant compliance breach, instant loss of trust.

The whole reason enterprises pay for AI is confidentiality. Ad models require profiling and tracking by their nature — utterly incompatible with privacy.

## The more likely endgame

Not "ads for tokens" but "mixed subsidy":

| Tier | Model | Who tolerates it |
|---|---|---|
| Free | Rate-limited + occasional ad to unlock 5 extra today | Light users |
| Subscription | No ads, long context, the strong model | Heavy individuals |
| Developer | Contextual tool ads in the terminal/IDE (databases, CI, cloud) | Developers |
| Enterprise | Pure paid, data isolation, zero ads | Companies |

The developer tier is the interesting one: you run a coding agent in your terminal, and it suggests a database or CI tool next to it. That's not really "watching an ad" — it's precision customer acquisition. Developer traffic is high-value and slow to decide, so advertisers pay a premium for it. Amp Free and Giga Dev are already doing this.

## Bottom line

"Ads for tokens" isn't impossible — it just can't fund a frontier model. AI's marginal cost is literal electricity, and physics doesn't permit "free" at scale. What actually works is the old playbook: use ads and subsidies to acquire users, then convert to paid to retain them. Same as every SaaS ever.
