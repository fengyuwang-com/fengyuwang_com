---
title: "Disk Health Ratings Can't Be Trusted"
date: 2026-09-05
description: "A drive lies in only one way: reporting that it's fine."
slug: "disk-health-lies"
tags: ["Hardware", "Data"]
draft: false
translationKey: "disk-health-lies"
---

I have never seen a drive report health below 99 percent. Yet some drives die just like that — one sat at 100 percent, then dropped data mid-use, never to be recovered.

Not mysticism; two blind spots. First, the health rating is the drive reporting on itself: SMART attributes like C5 and C6 haven't tripped, but many deaths never pass through SMART — the circuit board fries, and the drive doesn't even leave last words. Second, the old drives circulating in the market labeled "brand new" are, nine times out of ten, refurbished or zeroed: drives produced a decade-plus ago routinely have thirty-to-fifty thousand power-on hours, scrubbed clean and resold. The buyer reads the health number; the seller bets the buyer doesn't know what it can't see.

The un-scrubbable record lives in FARM logs — enterprise drives' power-on hours, start-stop counts, remap history. That's the drive's medical chart, and zeroing tools can't reach it. Consumer tools don't show it by default.

Someone will say: checking health beats not checking. True — so don't discard the tool; demote it. Health is a necessary condition, not a sufficient one. For any data that matters, assume the drive dies tomorrow: backups, copies, off-site — skip none of them.

A drive lies in only one way: reporting that it's fine. Backing up isn't distrust of the drive. It's distrust of the number 99.
