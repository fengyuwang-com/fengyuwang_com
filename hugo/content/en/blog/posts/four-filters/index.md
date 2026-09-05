---
title: "Be Greedy When Others Are Fearful, Written as Code"
date: 2026-09-06
description: "Fear isn't a day; it's a structure."
slug: "four-filters"
tags: ["Investing", "Quant"]
draft: false
translationKey: "four-filters"
---

Everyone has memorized "be greedy when others are fearful." Plenty of memorizers, plenty of losers — because the sentence is missing half of itself: how do you know that today is fear?

My method is clumsy: no definition, no trading. And the definition can't be an adjective; it has to be a rule a machine can judge right or wrong too. When the machine rules against it, revise the rule. This strategy was forced into existence by verdicts.

## Claim #11

The first version lived in a script called verify-011, with one claim: buy during panic periods, when VIX is above 30, and you beat calm periods.

The verdict was ugly. On the Chinese market, the 1-month, 6-month, and 12-month holding periods all fail; the 3-month one holds, and only after stripping out overlapping samples does it stay significant. In other words, buying on panic days usually buys you nothing.

## The Appeal

I refused the verdict and added a premise: the line only holds when asset quality comes first — be greedy when others are fearful, but greedy for the best stocks. Test the best stock, then. In A-shares, which is best? ICBC. Re-run.

The verdict got uglier. Buying ICBC during panic periods lost an average of 5.6% over a one-year hold; buying on a random day and holding a year earned 16.1%; the one-month win rate was 36.6% — six losses out of every ten. The conclusion is one sentence: a panic period is not a golden pit for good stocks; a panic period is precisely where the good stock starts to lag.

Both verdicts pointed the same way: the problem wasn't me, it was the word panic — the original sentence never defined it.

## Defining Fear

So I said again what fear actually is: the market has already fallen for three to five months straight, and then one day it drops another 5% or more — that is fear reaching its extreme. March–April 2022, the reopening day after the 2020 pandemic shutdown — that is fear, real fear. A random one-day drop doesn't deserve the name.

Once the definition landed, the statistics followed: from 2006 to 2026, the Shanghai index fell more than 5% in a single day 48 times; half a year later, the probability of a positive return was only 41.7%, with a median of -4.11%. But slice the market by regime: in a choppy market, buying such dips pays off 87.5% of the time; in a bear market, only 22.6%. The numbers say what I said — a crash by itself isn't an opportunity. The structure a crash sits inside is the opportunity.

## The Four Filters

So the strategy ended up looking like this:

```python
# verify-011-final.py · four-filter fear-extreme strategy
DROP_THRESHOLD = 3.0    # single-day drop ≥3%
LOOKBACK_DAYS  = 63     # close below its 63-trading-day-ago close: three months down
PE_ABS_MAX     = 15.0   # PE ≤15
PE_PCT_MAX     = 20.0   # PE in the lowest 20% of its five-year range
TAKE_PROFIT    = 8.0    # take profit at +8%
STOP_LOSS      = -3.0   # stop loss at -3%
EXIT_WINDOW    = 120    # 120 trading days with no exit = timeout
TC             = 0.0003 * 2   # both sides, 6 bps — never understated
```

Four filters: three months of decline removes what has only just started falling; the single-day plunge removes the slow bleed; PE at 15 or below removes expensive; the bottom-quintile-of-five-years removes what fell a lot but is still expensive. The pool is 15 A-share blue chips, ICBC and Kweichow Moutai among them. The data costs nothing: daily bars stitched in segments from Tencent's API, PE scraped from Eastmoney. Exits are hard-coded too — take 8% and leave, lose 3% and leave, 120 quiet days and it's a timeout.

## Right of Verdict

Not one sentence in this strategy is my feeling. The four filters were paid for by two falsifications; the exit lines were computed from costs; even the fees live in the code. It hangs there now, waiting for the next panic to hand in its exam.

Buffett's line was never wrong. What's wrong is treating panic as a day. Fear is a structure — and a structure can be written as code. Only what can be written as code can be right or wrong.
