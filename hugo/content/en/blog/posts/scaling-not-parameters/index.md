---
title: "Scaling Is No Longer a Bigger Number"
date: 2026-09-11
description: "The AI industry spent five years treating parameter count as progress itself, then patiently proved the accounting wrong. Scaling never stopped — only its objective function changed."
slug: "scaling-not-parameters"
tags: ["Technology"]
draft: false
translationKey: "scaling-not-parameters"
---

Ask anyone about a large language model and the first question is still: how many parameters? The question itself deserves a challenge. What does parameter count actually tell you, on its own? Over the past few years the industry spent real money testing the answer, and the answer is: almost nothing. Parameter count only means something next to three other facts — how much data the model saw, where the compute went, and under what conditions it runs.

## Three Editions of the Ledger, Each Closer to the Truth

The evolution of Scaling Law over the last few years is really a story of the ledger being rewritten three times. In 2020, Kaplan and colleagues computed a ratio: parameters should grow much faster than data, roughly 2.7 to 1. The industry followed instructions, models ballooned, and a trillion parameters was briefly treated as the mandatory road to progress. In 2022, Hoffmann and colleagues reran the experiments with over four hundred models and reversed the conclusion: compute-optimal allocation sits near 20 tokens per parameter, and as compute grows, parameters and data should grow at roughly the same rate. That is Chinchilla Scaling Law. Look back at the largest models of that first era and you find precisely the most misallocated ones — parameters stacked too fast, data left behind, money spent, results missing.

The third rewrite happened after deployment. Chinchilla priced a model that is trained once and then benchmarked. But a frontier model today is called billions of times a day, and inference costs dwarf that single training run. Fold that bill into the ledger and the optimum moves toward smaller models trained longer — pay more upfront, save real money on every answer.

By the MoE era, simple ratios gave out entirely. New research split two things that had been conflated: total parameters determine how much knowledge, fact, and long-tail information a model can hold; active parameters and the effective depth of each forward pass determine long-range reasoning. Memory-heavy tasks feed on parameters; reasoning-heavy tasks feed on data. The counterintuitive finding goes further: at a fixed tokens-per-parameter ratio, adding total parameters can actually degrade reasoning, while activating more experts steadily improves it.

## A Controlled Experiment in the Wild

The logic comes with a ready-made case. GLM-5.3 shares its entire base with the previous GLM-5.2: 753B total parameters, 40B active — the hardware untouched, line by line. Yet the AA index rose from 53 to 60, and its coding performance is widely ranked at the front of the domestic field. Where did the points come from? Higher-quality data and a better training recipe. This is a controlled experiment in the wild: with parameters and activation locked, any score increase must come from the data side — and it did.

Which is the real conclusion: how smart a model is can no longer be summarized by one parameter count. Scaling has not stopped. It has changed from piling up an ever-larger number into a game of finding the optimum. The money is no longer spent making the number bigger; it is spent getting the accounting right. Where compute is allocated matters more than how high the pile stands.
