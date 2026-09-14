---
title: "The Two-Layer Interface Principle: Software Interaction Architecture for the AI Era"
date: 2026-09-13
description: "The conversation layer becomes the main human-machine channel and the graphical layer retreats to a viewing deck — any software system keeps exactly two interaction layers, and documents form a third interface that faces the AI. Proven by a full audit and consolidation of a real multi-system ecosystem."
slug: "two-layer-interface"
translationKey: "two-layer-interface"
tags: ["Tech", "Business"]
draft: false
---

## Abstract

Generative AI has pushed the graphical-interface paradigm of "operating software," unchanged for four decades, to the point of paradigm replacement. Based on a complete audit and refactoring practice across a one-person software company (the FengProj ecosystem: investment research, content production, and private-cloud products — three real systems), this paper proposes and tests the **Two-Layer Interface Principle (2LIP)**: any software system should keep only two interaction layers — (1) the **conversation layer**, natural-language exchange between human and AI (with Skills as its scripted form), carrying all daily operations; (2) the **viewing layer**, a read-only graphical interface that exists only for "people who do not operate." Data always lives in local files, and interaction output flows into a backup-able pipeline. The paper places this principle against three parallel industry currents — YC's "Chat is the interface," Generative UI, and the MCP-UI architecture of the OpenAI Apps SDK — and shows that all three converge structurally on the same proposition. It further argues that when AI becomes the first operator, documents (AGENTS/MISSION/todo/logs) themselves constitute a **third interface** — a governance interface facing the AI — extending "interface" from two ends, human and machine, into a triadic structure of human–AI–document. The case section presents a compliance audit of five systems and their consolidation paths, showing that the principle lands on both personal production systems and external commercial products.

## 1. The Problem

The classic software interaction model is client-centric: users click and fill forms in a graphical interface, and results settle into the client's database; the interface is both the operating entrance and the data container. Two premises implicit in this model no longer hold in 2026:

1. **Operations must be initiated by humans.** Once an AI Agent can be entrusted with the full pipeline — topic selection, drafting, research, publishing, diagnostics — "humans press buttons" is demoted from necessity to option.
2. **Results must stay in the client.** Once data has a local-file source of truth (Markdown/JSON/SQLite), the client degrades into a view, and backup and migration become file-level operations rather than database engineering.

From this the author re-conceived the whole shape of software: **I only need to talk to the AI — because most of the work was textual exchange to begin with; UI exists for two kinds of moments: letting people who don't understand see it, and making it convenient for those who look.** This paper formalizes that intuition into an auditable engineering principle and validates it on a real multi-system ecosystem.

## 2. The Two-Layer Interface Principle

**Principle (Two-Layer Interface Principle, 2LIP)**: a software system built for the AI era keeps only two interaction layers —

| Layer | Serves | Form | Duty | Anti-pattern |
|---|---|---|---|---|
| **Conversation (L1)** | Operators (human) and AI | Natural language + Skills (scripted instructions) | All daily operations: CRUD, workflow triggers, exception handling | Burying operations in buttons the AI cannot reach |
| **Viewing (L2)** | Watchers (human, usually non-operating) | Read-only Web UI / dashboards | Displaying state and results for understanding, acceptance, and external demo | Building write operations into the viewing layer |

Plus two resource constraints:

- **C1 (data local)**: the source of truth is always a local file or local database; any client or cloud service holds only copies or views.
- **C2 (output backup-able)**: all interaction output lands in a versionable, multi-replica sync pipeline (git dual-push, multi-device sync).

Whether a system complies with 2LIP takes four questions: Is the data local? Do daily operations go through conversation? Is the UI read-only? Can the output be backed up?

## 3. Industry Alignment: Three Currents Converging

### 3.1 "Chat is the interface"

In 2026, Y Combinator's Gary Tan and Jared publicly revised their earlier stance, confirming that "conversation as the interface" is the correct form for AI applications (the Pete Koomen discussion spread widely). Products echo it: neww.ai's slogan "Chat is the interface. The operating system is the product."; arg.ai simply cancelled all feature pages, with the Agent reading and writing files directly through chat; XBuild, for contractors, made conversation the estimating flow itself. This shows 2LIP's L1 layer has been accepted by the industry as the main channel, not a bolted-on chatbot.

### 3.2 Generative UI: the viewing layer need not be pre-built

The further question: does L2 require "careful development"? Generative UI answers no — the interface is assembled on demand by the Agent for the problem at hand (cards, charts, whole pages of HTML), not a fixed layout predefined by designers (definitions from Google Cloud, CopilotKit, and Decagon converge). Its argument: dashboards make people dig through filters for answers, while GenUI "turns the interface into a response, not a destination." Yet 2026 practice reflection (e.g., the r/UXDesign community) points out equally: **fixed dashboards that show everything at a glance are irreplaceable in predictability and glanceability**. The two combine into 2LIP's position: keep the viewing layer, but skip the fine finish — fixed views cover "one glance a day," generated views cover "details right now."

### 3.3 MCP Apps / OpenAI Apps SDK: growing a visualization onto the customer's Skill

2LIP's counterpart in external products has been platformized: the OpenAI Apps SDK lets an MCP server (that is, "a Skill given to the customer") return UI resources rendered as React components inside the chat flow (such as Zillow listing cards). This is the official form of "a Skill inside the Web UI": **the Skill is the body; the UI is a visualization attachment returned by the Skill**, not an independent portal. For desktop/mobile native products the equivalent corollary: embed the customer conversation entrance in the product; operations go through conversation; panels retreat to display and fallback.

### 3.4 Local-first: industry consensus on the resource constraints

Constraints C1/C2 correspond to the local-first AI Agent current: agents read and write local data first, with asynchronous sync for backup (fast.io); local indexing plus on-demand cloud as a tiered data strategy (data placement decided by sensitivity, not by a "local" dogma); the runtime, memory, skills, and scheduled tasks of a personal agent fully localized (r3zz.io's "boring architecture"). The consensus: full offline is unrealistic; the key is **data tiering** — sensitive data never leaves the local machine. 2LIP adopts the same conclusion and goes further in a single-machine personal ecosystem: the source of truth can be 100% local.

## 4. The Third Interface: Documents as the AI's Governance Plane

2LIP answers "how do humans operate the software," but leaves one question: **how is the AI operated?** The answer grew out of practice long ago: not APIs, not a config center, but **documents**.

The author's multi-machine development ecosystem (FengASNI) ran a commonality analysis over 70 governance documents and converged on a "supervising-document paradigm": a four-piece set of `AGENTS.md` (rules, single source), `MISSION.md` (north-star goal and DoD), `todo.md` (task ledger), and `FENGMEM.md` (session logs), supplemented by Skills (`SKILL.md`) as reusable operation wrappers. Its mechanism: the AI reads documents before work to obtain identity, rules, and tasks; action results are written back to the ledger and logs; rule changes are written back to AGENTS. **The document is the control plane** — the new role of Docs-as-Code after its confluence with agent-native development: documents' readers expanded from "humans" to "humans and AI," and the AI is the stricter reader (it executes word for word).

The core extended proposition follows: software interaction in the AI era is a **triadic structure** —

```
human ──natural language──> AI ──tool calls──> system
│                                ↑
└──documents (rules/goals/ledger/logs)──────┘
        documents = the interface facing the AI (governance plane)
```

- The **conversation layer** is the interface for "humans operating the AI";
- The **document layer** is the interface for "(humans, through the AI) governing the AI and the system";
- The **viewing layer** is the interface for "humans confirming system state," visualizing the results of the first two.

The three layers are not parallel: the document layer constrains the conversation layer (Skills must obey the AGENTS iron rules), the conversation layer drives the system, and the viewing layer only reflects the output of the first two. This structure explains why a 2LIP system needs no complex permission backend — governance is already carried by the rules and ledgers of the document layer.

## 5. Case Study: Audit and Consolidation of a Real Ecosystem

The following is an audit of the author's personal ecosystem (all local-first real production systems) against the four 2LIP questions:

| System | Domain | UI status | Verdict | Action |
|---|---|---|---|---|
| FengInvest | Investment research (62 tools, 2.7 GB local market-data library) | Read-only report browser (fengweb) | ✅ Benchmark: data local and gitignored, all operations through conversation, UI purely viewing, output git dual-pushed | Leave as is |
| FengMedia | Content production | Battle map + topic library / check-ins (has write operations) | ⚠️ UI mixed with operations | Move write operations into conversation ("record a topic" writes JSON directly); UI retreats to read-only |
| FlyGo | Private-cloud product (external, commercial) | Panel + APK as the product itself | ➖ Special: the UI is the deliverable; L2's "retreat" clause does not apply; but lacks a customer conversation layer | Embed a "customer Skill" following the MCP Apps pattern; panel retreats to display |
| FengOS | Project command center | 3D galaxy overview + system probes | ✅ The ecosystem-level "viewing deck" itself | Upgrade to the unified viewing entrance (aggregate read-only views of each system, move no data) |
| Pure tools (TTS-UI etc.) | Desktop utilities | GUI as the interaction itself | ➖ Not applicable (no AI layer needed) | Leave as is |

The audit reveals a universal decision order: **first decide whether the system is a "self-use production system" or an "external product."** The former strictly applies 2LIP; for the latter the UI is the product itself, and 2LIP's application becomes "add a conversation layer inside the product, not cancel the UI." Meanwhile, the ecosystem-level viewing deck (FengOS) should consolidate the viewing entrances of all systems while holding to "iframe/link aggregation, move no data," guarding C1's single source of truth.

## 6. Discussion: Boundaries and Costs

**2LIP is not "abolishing the UI."** Counter-evidence is real: glanceability scenarios — monitoring walls, cockpits, demoing to investors — favor fixed views over conversation; efficiency for unambiguous operations (volume should not be adjusted by typing). The correct reading of 2LIP is **transfer of operating rights**, not the death of UI: operating rights go to the conversation layer; the UI keeps the right of confirmation.

**The reproducibility of the conversation layer depends on the document layer.** The risk of pure conversation is "said and lost." The document paradigm (tasks into the ledger, logs appended, DoD acceptance statements) is exactly the completion: every round of conversation's instructions and results lands as machine-readable ledger entries, giving the conversation layer an auditability traditional GUI never had — the operation history is not a clickstream log but structured text.

**The change in cost structure.** 2LIP shifts the development center of gravity from "front-end interface engineering" to "Skill engineering + document governance + on-demand generation of viewing pages." For a one-person company, this means the largest non-outsourceable asset (the interface) is depreciating, while the hardest-to-copy assets (domain-rules documents, personas, judgment standards) are appreciating.

## 7. Conclusion

The Two-Layer Interface Principle condenses the shape of software in the AI era into one sentence: **the conversation layer does, the viewing layer shows, the document layer governs; data stays local, output goes to backup.** That three industry currents (chat-first, Generative UI, MCP Apps) and local-first practice converge structurally on this principle suggests it is not a personal preference but an early position on a paradigm direction. For individuals and small organizations, 2LIP offers an immediately executable refactoring path: audit existing systems' UI write operations and move them into conversation, aggregate viewing entrances into a single viewing deck, and embed a Skill-form customer conversation layer into external products — and the foundation of all of it is treating documents as first-class citizens facing the AI.

## References (retrieved 2026-09)

1. YC "chat is the interface" stance shift: Pete Koomen interview coverage, biggo.com
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
12. Internal practice: FengASNI DocsParadigm (commonality analysis of 70 governance documents and paradigm proposal); FengOrchestrator five-layer architecture master plan and TTS-UI fleet battle retrospective
