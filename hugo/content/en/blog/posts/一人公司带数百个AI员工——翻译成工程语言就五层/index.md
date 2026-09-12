---
title: "One Person, Hundreds of AI Employees: Translated into Engineering, It's Five Layers"
date: 2026-09-10
description: "The one-person company is not a sentiment. It is an engineering problem: how to staff, approve, and correct hundreds of AI employees. The answer converges into five layers — intent, organization, talent, execution, safeguards."
slug: "opc-five-layers"
translationKey: "opc-five-layers"
tags: ["Tech", "Business"]
draft: false
---

The phrase "one-person company" sounds like a consolation prize — a dignified label for a startup that failed. My version is an engineering problem: a firm with exactly one human, running hundreds of AI employees, with AI leading AI. The chairman does two things only — sets targets, signs acceptances.

Slogans are cheap. The trouble is they have to land. Hundreds of employees: how are they staffed? Who approves when work goes wrong? How are lessons reviewed? Staffing, approval, review — all of them organizational problems, not intelligence problems. Org theory was written for people; software engineering was written for code. Hundreds of AI employees sit stuck in between: they need organizational discipline, yet can only be implemented as code.

## One sentence of vision, five layers of engineering

Break the vision down and the pain points fall into three: AI employees don't know how to organize themselves, don't know how to collaborate with humans, don't know where to look things up. Translate further and the answer converges into five layers. Skip any one and the structure falls:

- Intent: one target from the chairman, plus a signature;
- Organization: the brain that has AI lead AI — who works, how they are staffed, how work is handed over, how it is accepted;
- Talent: where qualified "people" for each specialty come from;
- Execution: the command-line engines that actually do the work;
- Safeguards: approval, memory, notification, knowledge.

## The waist is what goes missing first

The list reads backward too. The earliest mistake was treating a parts list as the architecture: picking approval tools, memory tools, notification tools one by one — dressing up layer-five patches as the whole design. Once that was seen clearly, the order fixed itself: patches are layer five's business; the main course is layer two.

Of the five layers, the organization layer is the one most often skipped. This pit was paid for: talent library and execution engine both in hand, work dispatched straight past staffing, batch-summoning the same generic "developer." Talent became a crowd of day laborers; strong execution made them no less headless. The organization layer is the waist of the whole structure.

The open-source organization manual found later had a command structure isomorphic to chairman → CEO → specialist AI, and staffing in three sizes: 5 to 10 roles for micro, 15 to 25 for a sprint, and full. How to staff hundreds of AI employees — those three sizes are the answer. No fourth needs inventing.

## 275 roles, 21 hired

The talent layer paid tuition in plainer numbers. A library of 275 specialist roles in Chinese, reviewed one by one: one third gems, two thirds empty shells. In the end 21 were hired — 25 slots in total inside the orchestrator. From 275 down to 21, with no mercy for the cut. "Rather none than mediocre" applies to AI employees as much as to people.

## Cost is a hard constraint

Execution closed the loop first: chosen from 40-plus candidate projects after source-level review; an official example run cost $0.0095 — under a cent. Cheap as it is, cost stays a hard constraint: API balances burned out, prepaid subscriptions burned out, and at the tightest moments free models served as the bypass for verification. A small-field exercise with three selected roles still hasn't been fought — it waits on one thing: a ruling on cost accounting. Every step the blueprint takes, an invoice follows.

## Safeguards: first, name what is being defended against

The collaboration pain point lands on the approval gate. In the vision the chairman only signs; in engineering, a signature means: before an AI takes a high-risk action — emailing a client, spending budget, dropping a database — it asks first, and the ask arrives as an approval card pushed to a phone. A policy engine auto-allows and auto-denies by rule; the rest goes to a human, with an audit log throughout.

A one-person company has no colleagues watching; internal control matters more, not less. Signing authority is an organizational problem, not a technical one. Fixed flows go through a manual approval gate in the pipeline; fluid scenarios go through runtime approval. Two legs, each covering half the ground.

The other four safeguards answer four kinds of failure. Memory, against AI forgetting when done — a stated reply preference should already be known to the next recruit on the first day. Notification, against work finished and no one knowing — a contract cleared at midnight should reach the chairman's phone for a signature. Knowledge supply, against blindness — ask a finance AI about last month's spending and it digs the ledger, instead of asking back where the data is. Acceptance benchmarks, against good-enough-by-whose-standard — the same task graded against an industry benchmark, role by role; only passing scores become permanent. The first three layers are offense; the safeguard layer is defense: able to work, and also unable to fail silently, run wasted, go unheard, or forget.

## Review: the shopping list cut to one line

The safeguard layer deserves the best review. At stocktaking, four layers were closed; the fifth was the gap. The first move was shopping to fill blanks — approval, memory, notification, knowledge, acceptance: five gaps, five open-source projects, a tidy list. The search was honest: current reality checked by search, not old memory, each project matched to its gap after reading.

The review flipped the conclusion. Four of the five exist natively in the platform — approval is the CEO asking directly before a high-risk action; memory is the project's memory files; notification is a written polling script; acceptance swaps in another agent to grade. One true gap remained: letting every AI employee read the company's documents.

A shopping list cut to one line. The lesson, on record: attitude is not review — the list has to be re-audited against the ground.

## Locked into one Skill

The organization layer finally hardened into a manual packed into a single Skill. Give it a target in one sentence — review this contract, produce a risk assessment — and it judges staffing on its own, summons a legal-review role that ships with acceptance criteria, splits the work across seven phases, gates each one, and aggregates reports up to a signature. The discipline is written hard: evidence outranks claims; fail the gate and the work goes back, three strikes at most; handovers must carry templates — a number in the org manual puts 73 percent of collaboration failures at the handover boundary. One iron rule presses on the bottom: the CEO never writes code. It orchestrates.

## Where this does not apply

The five layers have clear edges. They answer one question: how to staff hundreds of AI employees. One human with one AI doing scattered tasks needs one layer, not five — everything past the first is a sledgehammer on a chicken. Nor is this an automation utopia: the chairman's two jobs — setting targets, signing — are the only parts of the design not outsourced. The more automatic the five layers become, the heavier those two get.

One question is left: where does the human stand in the five layers? Not inside a layer — at every layer's door. The target enters at the intent layer; rejected work goes back at the gate; the signature happens at the approval door. Task-level human-AI collaboration already has a standard answer in the open-source world; the organization-level link is what remains — the structure is laid out on the site's [Feng Human-in-the-Loop](/en/human-in-the-loop.html) page.
