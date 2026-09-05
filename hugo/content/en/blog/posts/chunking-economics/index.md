---
title: "Feeding a Million Characters at Once Is Expensive and Bad"
date: 2026-09-05
description: "However large the context window, chunking still wins — and the reason is arithmetic, not feeling."
slug: "chunking-economics"
tags: ["AI", "Cost"]
draft: false
translationKey: "chunking-economics"
---

Context windows now hold a million characters. Is chunking still necessary? My answer: yes. Not as a feeling — as arithmetic.

First, the money. A million characters in one shot, versus ten thousand segments of a hundred characters each — which is cheaper? Intuition says one shot: doesn't segmenting mean paying for ten thousand extra prompt headers? Here's the physical fact that settles it: as long as the prefix matches, the prompt hits the KV cache, and cache hits are nearly free. I estimated a few percent at most. Re-priced later with current numbers: 0.83% — indeed under 1%. There was even a detour where the AI priced it off years-old rates, and I told it: it's the May Fourth era now, and you're quoting emperor-era prices. The re-run changed nothing: feeding in segments costs barely more than one shot.

Now quality — the bigger ledger. Push a million characters in at once and attention gets thinner and thinner. Not forgetting — dilution: the earlier the content, the less weight it carries over the current output. Worse is interference: Dream of the Red Chamber and Water Margin have nothing to do with each other; throw them into one model together and, window or no window, they contaminate each other and the output drifts.

So the two-sided ledger reads: one shot saves money — barely — and loses quality. Ten thousand segments cost about the same, and each segment gets the model's full attention, undiluted and unmixed.

This isn't a universal rule. Hunting foreshadowing across a whole novel is exactly what long context is for. I'm talking about batch work: ten thousand independent tasks shouldn't share one room, whispering over each other.

Window size is the model's business. How you feed it is yours.
