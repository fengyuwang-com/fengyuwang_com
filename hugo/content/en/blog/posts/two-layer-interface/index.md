---
title: "The Two-Layer Interface Principle: Software Interaction Architecture in the AI Era"
date: 2026-09-13
description: "Any software system should keep only two interaction layers: a conversation layer that carries all daily operations, and a read-only viewing layer. Documents form the third interface — the governance plane for AI. Audited across five real production systems of a one-person company."
slug: "two-layer-interface"
translationKey: "two-layer-interface"
tags: ["Technology", "Business"]
draft: false
---

> This article keeps the full academic structure: abstract, seven sections, references. The original manuscript is archived as [The Two-Layer Interface Principle (GitHub)](https://github.com/fengyuwang-com/fengyuwang_com/blob/master/TWO-LAYER-INTERFACE.md).

## Abstract

Generative AI has pushed the forty-year-old paradigm of graphical interfaces for "operating software" to the point of replacement. Based on a complete audit and restructuring practice across a one-person software company — three real systems covering investment research, content production, and a private cloud product — this article proposes and tests the **Two-Layer Interface Principle (2LIP)**: any software system should keep only two interaction layers.

- **The conversation layer**: natural-language exchange between a human and AI (with Skills as its scripted form), carrying all daily operations;
- **The viewing layer**: a read-only graphical interface, existing solely to give "people who do not operate" visual confirmation.

Data always lives in local files; interaction output goes into a backup pipeline. The article aligns this principle with three parallel currents in the industry — YC's "chat is the interface", Generative UI, and the MCP-UI architecture of OpenAI's Apps SDK — and shows that all three structurally converge on the same proposition. It further argues that when AI becomes the primary operator, documents (AGENTS/MISSION/todo/logs) themselves constitute a **third interface** — a governance plane for AI — extending the concept of "interface" from the two ends of human and machine into a three-way structure: human, AI, document. The case section presents a conformity audit of five systems and the path that folds them back onto the principle, demonstrating that it works for personal production systems as well as commercial products.

## 1. The problem

The classic interaction model of software is client-centric: a user clicks and fills forms in a graphical interface, and the results settle into the client's database. The interface is both the entry point for operations and the container for data. That model rests on two premises that no longer hold in 2026:

1. **Operations must be initiated by a human.** Once an AI agent can be entrusted with the full pipeline — selecting topics, drafting, researching, publishing, diagnosing — "a human clicking buttons" drops from a necessity to an option.
2. **Results must stay in the client.** Once the source of truth is local files (Markdown/JSON/SQLite), the client degrades into a view; backup and migration become file-level operations rather than database engineering.

This leads to a rethinking of what software should be: **talk to the AI — most work was text exchange to begin with; a UI exists only for two moments, to make things understandable for those who don't know, and convenient for those who look.** This article formalizes that intuition into an auditable engineering principle and validates it against a real multi-system ecosystem.

## 2. The Two-Layer Interface Principle

**The principle (Two-Layer Interface Principle, 2LIP)**: an AI-era software system keeps only two layers on its interaction surface —

| Layer | Serves | Form | Duty | Anti-pattern |
|---|---|---|---|---|
| **Conversation layer (L1)** | Operator (human) and AI | Natural language + Skills (scripted commands) | All daily operations: CRUD, workflow triggers, exception handling | Burying operations in buttons the AI cannot reach |
| **Viewing layer (L2)** | Viewer (human, usually not operating) | Read-only web UI / dashboards | Show state and results for understanding, acceptance, and demonstration | Building write operations into the viewing layer |

Plus two resource constraints:

- **C1 (data local)**: the source of truth is always a local file or local database; any client or cloud service holds only a copy or a view.
- **C2 (output backupable)**: every artifact of interaction lands in a version-controlled, multi-replica synced pipeline (dual git push, multi-device sync).

To judge whether a system conforms to 2LIP, four questions suffice: Is the data local? Do daily operations go through conversation? Is the UI read-only? Can the output be backed up?

## 3. Industry alignment: three currents converging

### 3.1 Chat is the interface

In 2026, Y Combinator's Gary Tan and Jared Friedman publicly revised their earlier stance, confirming that "conversation as the interface" is the right form for AI applications (the Pete Koomen discussion spread widely). Product echoes followed: neww.ai's slogan, "Chat is the interface. The operating system is the product."; arg.ai dropped all feature pages and let the agent read and write files through chat; XBuild, built for contractors, made the conversation itself the estimating workflow. The L1 layer of 2LIP is now accepted as the main channel, not a bolted-on chatbot.

### 3.2 Generative UI: the viewing layer need not be pre-built

The next question: does L2 need to be "carefully developed"? Generative UI answers no — the interface is assembled on demand by the agent for the problem at hand (cards, charts, full-page HTML), rather than a fixed layout predefined by designers (the definitions from Google Cloud, CopilotKit, and Decagon converge). The argument: dashboards make a person dig through filters for an answer, while GenUI "turns the interface into a response, not a destination." Yet reflections from 2026 practice (such as the r/UXDesign community) point out that **a fixed "see everything at a glance" dashboard is irreplaceable in predictability and glanceability**. The two sides combine exactly into the 2LIP position: keep the viewing layer, but skip the fine decoration — fixed views handle "one glance at the day," generated views handle "a closer look on demand."

### 3.3 MCP Apps / OpenAI Apps SDK: giving the customer's Skill a face

The counterpart of 2LIP for external products is already a platform: OpenAI's Apps SDK lets an MCP server — a Skill for customers — return UI resources rendered as React components inside the chat stream (such as Zillow listing cards). This is the official form of "the web UI should grow a Skill": **the Skill is the subject; the UI is the visual attachment the Skill returns**, not a separate portal. The equivalent inference for a desktop or mobile own-product is that the customer's conversation entry lives inside the product, operations go through chat, and the panel retreats to display and fallback.

### 3.4 Local-first: industry consensus on the resource constraints

The C1/C2 constraints correspond to the local-first AI agent current: agents read and write local data first, syncing backups asynchronously (fast.io); local indexing with on-demand cloud tiering, where data placement follows sensitivity rather than a "local" dogma; a personal agent with runtime, memory, skills, and scheduled tasks fully local (r3zz.io's "boring architecture"). The consensus: full offline is unrealistic, and the key is **data tiering** — sensitive data never leaves the local machine. 2LIP adopts the same conclusion, and on a single-machine personal ecosystem goes further: the source of truth can be 100% local.

## 4. The third interface: documents as the governance plane for AI

2LIP answers "how does a human operate the software," but leaves a question: **how is the AI operated?** The answer has long since grown out of practice: not an API, not a config center, but **documents**.

A commonality analysis of 70 governance documents across my own multi-machine development ecosystem converged on a "supervision document paradigm": `AGENTS.md` (rules, single source of truth), `MISSION.md` (north-star goal and DoD), `todo.md` (task ledger), and `FENGMEM.md` (session log), with Skills (`SKILL.md`) as reusable operation wrappers. The mechanism: an AI starts work by reading documents to obtain identity, rules, and tasks; results of action are written back to the ledger and log; rule changes are written back to AGENTS. **Documents are the control plane** — the new role that emerges once Docs-as-Code and agent-native development merge: the reader of documents expands from "humans" to "humans and AI," and the AI is the stricter reader (it executes every word).

This yields the article's core extension: software interaction in the AI era is a **three-way structure** —

```
human ──natural language──> AI ──tool calls──> system
│                                  ↑
└── documents (rules/goals/ledger/log) ────────┘
        documents = interface for AI (governance plane)
```

- **The conversation layer** is the interface for "human operates AI";
- **The document layer** is the interface for "(human, via AI) governs the AI and the system";
- **The viewing layer** is the interface for "human confirms system state," visualizing the results of the first two.

The three layers are not parallel: the document layer constrains the conversation layer (a Skill must obey the AGENTS iron rules), the conversation layer drives the system, and the viewing layer only reflects their output. This structure explains why a 2LIP system needs no complex permission console — governance is already carried by the rules and ledger of the document layer.

## 5. Case study: audit and convergence of a real ecosystem

Below is the audit of my personal ecosystem — all real, local-first production systems — against the four questions of 2LIP:

| System | Domain | UI status | Verdict | Action |
|---|---|---|---|---|
| FengInvest | Investment research (62 tools, 2.7GB local market data) | Read-only report browser (fengweb) | ✅ Benchmark: data local and gitignored, operations via chat, purely read-only UI, output dual-pushed to git | Keep |
| FengMedia | Content production | Battle map + topic library / check-ins (has write operations) | ⚠️ UI mixed with operations | Fold writes into conversation ("log a topic" lands as JSON), UI becomes read-only |
| FlyGo | Private cloud product (commercial, external) | Panel + APK as the product itself | ➖ Special: the UI is the deliverable; L2's "retreat" clause does not apply, but a customer conversation layer is missing | Follow the MCP Apps pattern: embed a customer Skill, panel retreats to display |
| FengOS | Command center | 3D galaxy overview + system probes | ✅ The ecosystem-level viewing deck itself | Upgrade into the unified viewing entrance (aggregate read-only views per system, move no data) |
| Pure tools (TTS-UI etc.) | Desktop utilities | GUI as the interaction itself | ➖ Not applicable (no AI layer needed) | Keep |

The audit reveals a universal decision order: **first determine whether the system is a "personal production system" or an "external product."** The former follows 2LIP strictly; for the latter the UI is the product itself, and 2LIP is applied as "add a conversation layer inside the product, not remove the UI." Meanwhile, the ecosystem-level viewing deck (FengOS) should fold the per-system viewing entrances into one, but stick to "iframe/link aggregation, move no data," preserving C1's single source of truth.

## 6. Discussion: boundaries and costs

**2LIP is not "killing the UI."** The counter-evidence is real: glanceability scenarios — monitoring walls, cockpits, investor demos — favor fixed views over conversation; and unambiguous operations are more efficient without typing (volume should not be adjusted by chat). The correct reading of 2LIP is a **transfer of operating rights**, not the death of UI: operating rights go to the conversation layer, while the UI keeps confirmation rights.

**The reproducibility of conversation depends on the document layer.** The risk of pure conversational interaction is "said and gone." The document paradigm (tasks on the ledger, appended logs, DoD acceptance statements) completes it: every instruction and result of every round lands as machine-readable ledger entries, giving the conversation layer an auditability traditional GUI never had — the operation history is not a click-stream log but structured text.

**The change in cost structure.** 2LIP shifts the center of development from "frontend interface engineering" to "Skill engineering + document governance + on-demand generated views." For a one-person company this means the largest non-outsourceable asset (the interface) depreciates, while the hardest assets to copy (domain rule documents, persona, standards of judgment) appreciate.

## 7. Conclusion

The Two-Layer Interface Principle folds the shape of AI-era software into one sentence: **the conversation layer does, the viewing layer shows, the document layer governs; data stays local, output goes to backup.** Three industry currents (chat-first, Generative UI, MCP Apps) and local-first practice all structurally converge on this principle — which means it is not personal taste but an early position on where the paradigm is heading. For individuals and small organizations, 2LIP offers an immediately executable refactoring path: audit the write operations in existing UIs and fold them into conversation, aggregate the viewing entrances into a single deck, and embed a Skill-form conversation layer for external products — with the foundation of it all being to treat documents as first-class citizens built for AI.

## References (retrieved 2026-09)

1. YC's shift on "chat is the interface": reporting on the Pete Koomen interview, biggo.com
2. Google Cloud, *What is Generative UI?*
3. CopilotKit, *Generative UI*; Decagon, *What is Generative UI?*
4. Thesys, *From Static Dashboards to Generative UI*
5. Open Data Science, *Generative UI: When the Agent Builds the Interface for You*
6. OpenAI, *Apps SDK / Add UI to your MCP server* (developers.openai.com)
7. Render, *Building with the OpenAI Apps SDK: A Field Guide*
8. r3zz.io, *The Boring Architecture Behind a Useful Personal AI Agent*
9. fast.io, *How to Implement Local-First Storage for AI Agents*
10. Medium/Data Science Collective, *My Local-First AI Agent Stack*
11. Reddit r/UXDesign, *Generative UI feels like the next "voice will replace screens"*
12. Internal practice: governance-document paradigm research across a multi-machine development ecosystem (commonality analysis of 70 governance documents); the five-layer organizational framework of a one-person company and field notes from a desktop TTS tool fleet
