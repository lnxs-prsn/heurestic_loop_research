# Intent timeline — heuristic loop research

Rules: incubating/human-coherence-intent-anchoring/kit/SPEC.md HC-4..HC-8.
Append-only. Agents reconstruct entries from evidence (`status: derived`);
only the owner confirms (recorded in owner-log.md). The current intent is
the newest confirmed, unsuperseded entry. **As of 2026-10-06 the current intent is INT-4,
confirmed by the owner at re-entry RE-1 (SIT-1).**

---

## INT-1 — Origin: heuristics outside the model make an AI reason better
kind: origin
describes: 2026-07-09
status: derived
confirmed: none
evidence: idea/deepseek.md, idea/kimi.md, idea/gpt.md, idea/manus.md, progress/BUILDLOG.md
builds_on: none
supersedes: none
superseded_by: none

**For:** improving how an AI reasons by moving heuristics *out of the model*
into a curated, external library: read the cue in a problem, pick the
matching heuristic, run it. The owner's premise: humans are not more rational
than LLMs; they have large heuristic libraries and are good at reading cues
to choose one (idea/deepseek.md §2). "Rationality" lives in the quality of
the library and the selection, not in model size.
The origin material is a sequence, and the aim grew along it:
1. a weak model punches above its weight (idea/deepseek.md §1, §7);
2. a strong model's reasoning becomes reproducible, auditable and
   self-improving: the "exoskeleton" (idea/kimi.md §1, §2.2, §8);
3. heuristics as a knowledge graph, layered memory, automatic discovery of
   new heuristics, governance (idea/gpt.md);
4. feasibility check: largely buildable (idea/manus.md, second half).

**For whom:** LLM-based systems in general; no specific user named (inferred).
**Success looks like:** reasoning that is versioned, testable and improves
over time, without changing model weights (idea/kimi.md §8; idea/gpt.md §8).
**Not:** fine-tuning or replacing the model (idea/gpt.md §8; idea/kimi.md §2).
The ordering 1→4 is inferred from cross-references (kimi.md cites "the
foundational report"; gpt.md says "your original report") (inferred).

## INT-2 — Checkpoint at the pause: a growing, evidence-gated heuristic library for the owner's coding agents
kind: checkpoint
describes: 2026-07-11
status: derived
confirmed: none
evidence: specs/00-overview.md, specs/06-phases.md, specs/01-invariants.md, MANUAL.md, progress/BUILDLOG.md, progress/STATUS.md, progress/decisions.md
builds_on: none
supersedes: none
superseded_by: none

**For:** an external, growing library of short, cue-indexed heuristics for
AI coding agents, served on demand by a local MCP server, grown from logged
experience through a human-gated staging airlock, with autonomy earned in
phases from logged evidence (specs/00 "What this is", "System summary").
Philosophy: humans hold expertise as tacit, cue-fired knowledge; AI can
articulate rules but forgets between sessions, so "AI articulates, human
recognizes and passes through" (specs/00 "Why").
**For whom:** the owner, on their own machines and projects; first target
Cline + DeepSeek, agent- and model-agnostic by design (specs/00).
**Success looks like:** agents retrieve and visibly apply heuristics on most
tasks; the library grows from real task friction; the owner's gate work is
gradually automated only where logs prove it was rubber-stamping
(specs/06 phases 1–5, graduation signals).
**Not:** making a weak model frontier-capable; reasoning scorecards, canary
traffic, meta-memory layers; any always-on service, database or cloud
dependency (specs/00 "Non-goals"; specs/01 "Do NOT build").

How it relates to INT-1: a deliberate **narrowing**. It kept "external
heuristics + human gate + growth from experience", moved the target from
reasoning in general to coding agents, and cut much of INT-1 item 3 as
needing volume a single person doesn't have (BUILDLOG@2026-07-09T17:30+03:00).
Persona ideas existed at the pause but were held at arm's length: personas
adopted only as a way to *audit specs* (D-2); personas at the heuristic level
deferred to an experiment (D-3, findings_report.md).

## INT-3 — Evolution: what the outside material (Sep–Oct 2026) proposes
kind: evolution
describes: 2026-10-05
status: derived
confirmed: none
evidence: I-1, I-2, I-3, I-4
builds_on: none
supersedes: none
superseded_by: none

This entry records what the four outside documents *propose*; it is not
adopted. The documents mark the owner's own statements ([SAID]) apart from
assistant suggestions; only [SAID] material is used below unless noted.

**For:** closing the gap between LLMs and human general intelligence, which
is attributed to *sample efficiency*: humans crystallize experience into
heuristics that **stack in a fixed order**, mostly unconsciously (I-1 §1–2;
I-3 §1). Concretely, a heuristic system that eventually takes over the
owner's own job of **making architecture-level rules** for their projects,
since agents have no heuristics for rule-making (I-3 §4 correction trail;
I-4 §1).
**For whom:** the owner, across all current and future projects (I-1 §7;
I-2 "Cross-Project Relevance"); later a persistent "person"-like assistant
that runs on a weak local model or a strong cloud model (I-3 §6; I-4 §1).
**Success looks like:** the owner's participation in projects declines over
time (I-3 §2); the system can tell when a question doesn't fit, not just
answer it (I-4 §3 items 5–8).
**Not:** settled. The documents leave open: thresholds for instinctive use,
persona capacity, reconciliation between personas, what "fits" means
(I-1 §6; I-2 open dependencies).

How it relates to INT-2 (detail per move in coherence/reentry/RE-1.md):
several parts return to INT-1 ambitions that INT-2 cut (graph structure,
parallel subagents, reasoning beyond coding, self-discovery), and some are
new (fixed stacking order, rule-making as the target, persistent assistant).

## INT-4 — Current intent as derived at re-entry RE-1 (for owner confirmation)
kind: checkpoint
describes: 2026-10-06
status: confirmed
confirmed: 2026-10-06, owner (SIT-1)
evidence: INT-1, INT-3, I-3, I-5, BUILDLOG@2026-10-06T12:45+03:00, BUILDLOG@2026-10-06T13:25+03:00
builds_on: none
supersedes: none
superseded_by: none

Drafted by the agent from the owner's own statements (the owner's Q2 rule:
intent is derived from evidence, the owner confirms), instead of asking the
owner to restate it.

**For:** making AI agents better at their work by giving them what the model
lacks: crystallized, cue-triggered heuristics that build on each other, kept
outside the model and grown over time (idea/deepseek.md §1–2; I-1 §1–2).
**For whom:** the owner, across all their projects (I-3 [SAID]); "what this
person finds helpful" is one kind of heuristic it learns (owner, 2026-10-06).
**How it grows:** individual heuristics → stacks and personas → learning from
use → rule-making → a person as a sub-project; all ordering, nothing
competing (RE-1, owner corrections 2026-10-06).
**Now:** individual heuristics, i.e. the July library: "we cannot stack
nothing on top of nothing" (owner, 2026-10-06).
**Success looks like:** the owner's involvement in projects declining (I-3
[SAID]).
**Not / beside:** agent-loop planning (inferred from the owner's "partly
relevant", I-4 insights 2–3).
