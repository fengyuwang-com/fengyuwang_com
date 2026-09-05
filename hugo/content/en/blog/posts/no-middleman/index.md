---
title: "My Server Uploads, My Phone Downloads"
date: 2026-09-05
description: "The middleman isn't a technical necessity. It's the rent on scarce addresses."
slug: "no-middleman"
tags: ["Tech", "Networking"]
draft: false
translationKey: "no-middleman"
---

From first principles: my server can upload, my phone can download — there shouldn't be any middleman in between.

Reality: your home broadband probably has no public IP, so data has to exit through a node that owns one. It was the carrier's carrier-grade NAT that decided "direct" doesn't exist for you.

Three roads to directness. Enable IPv6 with DDNS — closest to no-middleman, fastest, cost zero. Use an overlay network like Tailscale — the relay only makes introductions; once direct connection succeeds, your data never passes through it. Self-host a tunnel like FRP — total control, at the price of a public VPS, a few dozen yuan a month. Notice: even "no middleman" itself has a middleman's price.

Someone will say Tailscale is a middleman too. Not when the direct path is up. It's a matchmaker — it introduces the two ends and steps aside. A real middleman stands in the middle of the road collecting rent. The difference isn't whether a third party exists; it's whether the third party can choke your road.

So the middleman's existence isn't a technical necessity. It's the rent on scarce addresses. The day IPv6 becomes universal is the day a class of cloud services is exposed for what they sell: not technology, but a public address.

Next time you pay a cloud subscription, think about which one you're paying for: compute, or road tolls.
