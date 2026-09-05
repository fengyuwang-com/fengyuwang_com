---
title: "The Crime of Forward-Adjusted Prices"
date: 2026-09-06
description: "It takes no villain to rewrite history — just a default parameter."
slug: "adjusted-price"
tags: ["Investing", "Data"]
draft: false
translationKey: "adjusted-price"
---

The crime scene was in my own database: a stock's historical price was negative. No crash, no delisting — just negative. A price can fall from 100 to 1, but no kind of falling ends below zero — unless the historical price was rewritten by someone.

## The First Scene

The confession comes first: one major bias in my system — the share prices I scraped off the web, are they forward-adjusted? And here's the thing: forward adjustment means knowing every future year's dividends. That ruins everything. Did I scrape all this for nothing?

Forward adjustment works by taking every future dividend and folding it backward into historical prices. The 1995 candle has been rewritten by dividends declared in 2024 — information no investor in 1995 could have had. Anyone backtesting on such data has already peeked at the answer sheet. The trade has a name: look-ahead bias; this particular variant, dividend look-ahead. The scraped data wasn't wasted — the raw prices are fine. What was broken was my method for computing returns: the calculation was stealing glances at the future.

## Three Calibrations, Three Contaminations

Then the fatal problem surfaced on its own: forward adjustment has one big flaw — prices can be adjusted into negative numbers. A high-dividend old stock, decades of dividends deducted backward, can push its historical price below zero. That's not a trend-research inconvenience — the whole dataset is mathematically unsound.

So switch calibrations? Does unadjusted contaminate the database too? Back-adjusted? The interrogation found every option guilty of something. Unadjusted: the price series breaks at every ex-dividend date, and phantom gaps manufacture fake chart signals — but its PE is real, because people back then really did price the stock where it traded. Back-adjusted: the series is continuous and computed only from the past, no future information — but prices get pushed to absurd heights and valuation percentiles go haywire. Forward-adjusted: the prettiest charts, the worst mathematics.

Verdict: no ready-made calibration is clean. The clean design is one thing only — store unadjusted prices plus a dividend-event table, and compute whichever calibration you need at query time. Prices are facts; events are facts; calibration is a decision that belongs to the moment of use.

## An Accomplice

Case nearly closed — and then I caught the index doing the same thing. The Hang Seng Index is not adjusted for dividends at all: roughly 4% a year in dividends, thrown away. Telling a thirty-year story with a price index amputates the real return, systematically understating it by about 4 points a year.

How can investors around the world be this stupid? The bias is enormous — look at the difference between 6% and 10%: that's a 50% gap. In a market yielding 6%, a dividend-free index told over thirty years swallows half the real return. Newspapers use it, funds use it, your long-term performance benchmark uses it. Global investors aren't stupid — they're all reading the same doctored table.

## Closing the Case

Data is not fact. Data is fact wearing a calibration. Behind every candlestick chart hides a question that must be interrogated: this historical price — computed by whom, from what was knowable at that time? Data that can't answer doesn't get into a backtest.

My database now lives under new law: unadjusted prices, forward-adjusted, back-adjusted, dividend events — all four stored, plus a knowable-at-the-time flag. The cost is a few tables; what they buy is a history that the future cannot rewrite. Rewriting history takes no villain — a default parameter is enough.
