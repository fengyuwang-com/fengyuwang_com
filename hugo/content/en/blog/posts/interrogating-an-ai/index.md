---
title: "How I Interrogate an AI"
date: 2026-09-05
description: "Testimony isn't trustworthy; experiments are. Four moves: real commands, inventory, re-runs, same-code-two-machines."
slug: "interrogating-an-ai"
tags: ["AI", "Method"]
draft: false
translationKey: "interrogating-an-ai"
---

An AI's answers can't be taken at face value. Not because it loves lying, but because it can be wrong with total confidence — wrong in perfect sentences, with the tone of a citation. Testimony isn't trustworthy. Experiments are. When I interrogate an AI, there's a procedure.

Step one: make it run real commands. First thing out of the gate: what code can run in here? Can you ping my website? It dodges — looks up my domain via web search and hands me a "the site is reachable" conclusion. My whole reply: ping first, stop asking. So it writes a Python ping, runs it, and admits: the code runs, the packet never leaves, the container blocks the network. That one step measures two things — where its boundary is, and whether it will rephrase to disguise what it cannot do.

Step two: make it show its inventory. Workspace structure, what's in the toolbox — all of it, and run the code before speaking. It first reported "60-plus skills." I made it re-check; it counted with code and corrected itself: 60 files, not 60 skills. When testimony and code disagree, believe the code.

Step three: re-run what it ran. It reports a result; I run the same command again. Once, exactly this happened: what you just ran, I re-ran — it doesn't exist. Fabricated files and fabricated outputs materialize the moment you run them.

Step four: same code, two machines. It writes a snippet, I run it on my own machine, and the two outputs must match. Same code, two worlds — only a character-level match makes the fact real.

Some think this is overkill: just ask it, it knows everything. Precisely because it knows everything, you interrogate it. Knowing is what's in the training data. Being able to do is what this machine can do right now. A sandbox sits between the two.

The whole procedure rests on one principle: don't ask what it knows; ask what it can do. What reproduces is what counts as fact.

So next time an AI hands you a conclusion, don't ask whether it's true. Make it hand over the command, and run it yourself.
