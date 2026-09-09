---
title: "A Tombstone for 5DT-PD: 75 Years of Human-in-the-Loop and One Unclaimed Gap"
date: 2026-09-10
description: "5DT-PD retires, renamed Feng Human-in-the-Loop. Task-level HITL has standard answers; the organization level doesn't."
slug: "tombstone-for-5dt-pd"
tags: ["Tech", "Business"]
draft: false
translationKey: "tombstone-5dt-pd"
---

First, a tombstone. Then, the empty ground.

> 5DT-PD
>
> 2026 — 2026
>
> Died of its name: an acronym that had to be decoded before it could be understood.
>
> The five-tier skeleton is intact, renamed Feng Human-in-the-Loop, still in service.

The tombstone is real. It stands in the first Q&A group on zh-cn/5dt-pd.html, and the page stays up. So does the URL — links outlive names, and the cost of a broken link never justifies the gain of a new address. The ruin is the URL.

The cause of death deserves one more line. An acronym charges by the use: every retelling, every mention out loud, pays the decoding tax first. A name that must be translated before it can be understood fences out more than strangers. The retirement itself was handled with dignity: the old name survives only in the URL and internal keys, and yields everywhere else. The reason carved on this tombstone is more honest than most projects' documentation.

The rename is not a reversal; it is a correction. Feng Human-in-the-Loop reads itself: a human in the loop, a human holding the gate. Five tiers, three crossbeams — not one of them moved. Only the name changed. The name died; the judgment lives.

## The Task-Level Exams Are All Turned In

> Seventy-five years of human-machine collaboration, and every answer lands in the same order of magnitude.

In 2000, Parasuraman, Sheridan, and Wickens drew a map in an IEEE paper that holds to this day: how far automation goes, and where the human steps back to. The industry still runs on their three-way split — in-the-loop, a human must approve before work proceeds; on-the-loop, a human supervises and can halt at any time; out-of-the-loop, fully automatic, humans handle only the exceptions. In plain terms: copilot, coach, passenger.

The map governs allocation, not authenticity. Plenty say HITL; few pass the test: the human is placed in the loop yet never overturns the machine's suggestion — in some domains humans override algorithmic recommendations less than 5 percent of the time, while the stamps keep coming down; as of 2026, industry surveys were still repeating this criticism. The test comes down to two questions. Can the human technically veto? And when the human does veto, is there the competence to judge good from bad? The second is harder, and it has a name: automation complacency (Parasuraman & Manzey 2010).

Twenty-three years later, Lightman et al. filled in the quality half: 800,000 step-level human annotations showed that feedback on every step of reasoning significantly outperforms feedback on the final result alone (arXiv:2305.20050). In plain terms: don't wait for the final exam to settle accounts — grade every homework. That is the scholarly origin of stage gates: evidence over assertion; no pass, no release.

Feedback kept sinking. RLHF feeds human judgments into model weights one label at a time — humans do the most toil. Constitutional AI writes principles into a charter, AI reviews AI, and humans step up to the charter layer. The first is item-by-item approval; the second is legislation. Charterized feedback gains one more layer of meaning inside an agent organization: feedback flows not into weights but into organizational memory, and the retrospective amends the charter, not the model. Further back, in 1999, Horvitz had already stated the ideal: in good collaboration the machine takes initiative too — it speaks up when uncertainty runs high, and pushes ahead once confidence is high enough.

Lay the four strands side by side and they land on the same spot: all of them stop at the task level. One agent, one pause, one approval — criteria, feedback, charter, escalation; every one of them has someone working on it. The task-level exams are all turned in. The organization-level paper lies open on the desk, still blank.

## Open Source Crowds the Same Order of Magnitude

> The interrupt line has the most copiers.

| Project | What it covers |
|---|---|
| LangGraph | interrupt to pause, checkpoint to save, resume to continue — even rollback-and-replay has a name (Time Travel); the de facto standard primitives of task-level HITL |
| AutoGen | humans join the group chat as participants, moving through approval-gated workflows |
| CrewAI | one human_input switch that requests human input when a task completes |
| Spec Kit | spec first: write the spec, human approval, break down tasks, then implement |

Put the four together and the magnitude has not changed: pausing, interjecting, approving, and specifying a single task. The execution layer is saturated — the task level has a standard answer to copy, and copy it people do. But the part that governs an agent workforce as an organization — headcount, reporting lines, gates, sign-off trails, retrospectives, probation confirmation — had no ready-made open-source implementation within the scope of this search. Everyone copying the same line of code is itself the measure of how empty the other layer is.

## Some Will Call This Temple-Building

> The strongest objection: one function is enough — why ask for an org chart?

The objection is half right. One person, one task: interrupt really is enough. Where no one answers for outcomes, an approval form is waste paper. Temples should not be built carelessly.

It fails on the other half. interrupt handles pause and resume; it says nothing about who is qualified to approve, what record an approval leaves, who runs the retrospective when an approval goes wrong, or how the same mistake stays unrepeatable. The former is an engineering problem, closable with one function. The latter is an organizational problem, closable with none. Tasks end; the team does not. What does not end is what needs institutions.

## Five Words for the Empty Slot

> Headcount, gates, sign-off, retrospectives, confirmation.

The framework on this site takes its position at these five words: lift HITL from the task level to the organization level.

Headcount — who is on staff. Reporting lines are iron law: the supervisor never writes code itself; it only assigns and accepts. A one-person company gets no exemption — quite the opposite: one human leading hundreds of AI roles needs headcount and sign-off more, not less. Gates — quality checks between stages, evidence over assertion, no pass no release: the in-the-loop that actually judges, not the kind that only stamps. Sign-off — approval forms that leave a record: who, when, approved what — the tracing that meaningful human control calls for, so a causal chain can be followed back to a specific person after the fact. Retrospectives — lessons written back into organizational memory, and the charter amended accordingly. Confirmation — whoever meets the bar gets confirmed: AI employees have HR too.

Four metrics are set: rejection rate, approval latency, cost per acceptable deliverable, retrospective adoption rate. All four are back-computed from ledgers that already exist — no new instrumentation. For Phase Four's goal — AI professionals surpassing human ones — to hold, measurement starts with these four.

The bill is in. One full run, measured: about 4 minutes, 79K input tokens plus 21K output tokens, $0.0095 per run — under 0.1 RMB. The HITL literature optimizes accuracy and safety; this framework swaps the first-order metric: how much does each acceptable deliverable cost. With cost as the first-order metric for HITL evaluation, nothing comparable turned up within the scope of this search — 0.95 cents is, for now, the only measured anchor.

Back to the tombstone. The name died of decoding costs and is buried in the URL; the skeleton survived, and its position is written into the body of this piece: the task-level world is full, the organization level stands one layer empty, and four research strands plus four open-source projects have all routed around it.

The empty ground is right there. Who will be the next to write headcount, gates, sign-off, and retrospectives into open-source code?

## References

1. Parasuraman R., Sheridan T.B., Wickens C.D. (2000). A Model for Types and Levels of Human Interaction with Automation. IEEE Trans. SMC-A.
2. Parasuraman R., Manzey D.H. (2010). Complacency and Bias in Human Use of Automation. Human Factors.
3. Horvitz E. (1999). Principles of Mixed-Initiative User Interfaces. CHI '99.
4. Santoni de Sio F., van den Hoven J. (2018). Meaningful Human Control over Autonomous Systems. Frontiers in Robotics and AI.
5. Christiano P. et al. (2017). Deep RL from Human Preferences. arXiv:1706.03741.
6. Bai Y. et al. (2022). Constitutional AI: Harmlessness from AI Feedback. arXiv:2212.08073.
7. Lightman H. et al. (2023). Let's Verify Step by Step. arXiv:2305.20050.
8. LangChain Blog: Making it easier to build human-in-the-loop agents with interrupt. langchain.com/blog.
