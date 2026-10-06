# Heuristic Stack System — Direction Report

**Purpose of this document:** context for an agent working on the heuristics project. This is not a spec — it's the reasoning trail behind the design goal, so the agent understands *why* each constraint exists, not just what to build. Treat it as a supplement to whatever the project's current architecture already is.

---

## 1. Core Thesis

Current LLMs are already capable enough for most complex tasks a human can do. In raw output quality on tasks they've seen enough of, they're comparable to or exceed a single human. But they lose badly to a 10-year-old child on general intelligence — not because the child knows more, but because of **sample efficiency**. A child builds a working model of a new domain from a handful of examples and almost no explicit instruction. A model needs enormous exposure to reach equivalent coverage.

The working explanation: human intelligence isn't raw reasoning power, it's **crystallization of intelligence into heuristics and meta-heuristics**, most of which the person is not consciously aware of. The child isn't smarter in the sense of having more compute — they have a compiled, compositional stack of heuristics that structures how new information gets processed, and that stack is what's missing (or present only as a flat, uncompiled soup) in an LLM's learned patterns.

**Implication for this project:** the goal isn't to make a smarter model. It's to impose the missing compositional structure on an already-capable base model, so it gets more correct behavior per token instead of needing more scale.

---

## 2. Foundational Insight — Heuristics as an Invariant Stack

Heuristics are not interchangeable modules you can mix and match. They're more like compatible parts of a house: they build on top of each other, and if you drop in a part that doesn't match the layer below it, you get friction — not a new capability, just wasted effort resolving the mismatch.

This holds even in dysfunctional cases. Look at any person, however dysfunctional their heuristics are — the heuristics still build on top of each other in a consistent, fixed order. There is a forced dependency graph, not a random bag of tricks.

**Consequence for "persona" design:** a persona is not a role label (Auditor, Scribe, Teacher, Coach). **A persona is the fixed, invariant stacking order of heuristics** — the specific sequence of input/output contracts, in position. Two personas can't safely swap a heuristic between them unless that heuristic's input/output contract matches the receiving slot exactly. This is why giving an agent "one more good heuristic" without regard for stack position causes conflict rather than improvement: it creates a competing rule at the same slot, and the system wastes effort on *arbitration* instead of *execution*.

---

## 3. Design Principle — Contracts Define Eligibility, Not Competition

Because heuristics are position-bound, "choosing which heuristic to use" should almost never be a search over N candidates. If the stack is well-defined, only one heuristic is structurally eligible for the current state at any given moment — eligibility is a match check against an input/output contract, not a ranked comparison.

Two failure modes to design against:
- **Contract collision**: two heuristics both match the same input shape. This is a design bug in the stack, not something to resolve at runtime with arbitration logic.
- **Position violation**: a heuristic downstream receives an input shape meant for an earlier stage (e.g. raw, unprocessed data reaching a stage built for pre-filtered data). This produces silent failure or nonsense output, not an error — worth explicit validation.

Where real *choice* exists (as opposed to fixed traversal), it should be concentrated into as few explicit decision points as possible — e.g. a single dispatcher that decides which whole stack/persona activates, after which everything downstream is deterministic traversal, not further decision-making.

---

## 4. Two-Phase Roadmap

**Phase 1 (current / near-term): hand-authored, explicit stacks.**
Heuristics and their stage contracts are defined by hand — the same way the algorithm-learning framework's pipeline (problem → constraints → logic → steps → code → Big O) is explicit and ordered. This phase produces the intentional, deliberate mode of heuristic usage: slower, but auditable and correctable.

**Phase 2 (end goal): agent discovers/compiles its own stack from feedback.**
The agent builds and refines its own heuristic stack through interaction and outcomes, the way a child does — not by being handed contracts, but by having contracts emerge from what actually works. This phase is the long-term target and is not yet designed.

The system needs to end up supporting **both an instinctual (automatic) mode and an intentional (deliberate) mode of heuristic usage simultaneously** — not one replacing the other. How to build this transition is the open problem.

---

## 5. Candidate Mechanism for Phase 1 → Phase 2: Proceduralization

A relevant precedent exists in cognitive science (ACT-R, Anderson's cognitive architecture): the transition from explicit, rule-based, deliberate knowledge to fast, automatic, "instinctual" execution is called **proceduralization**, and it's driven by two measurable signals — **frequency** (how often a given rule fires) and **reliability** (how often it succeeds when it fires).

Proposed translation into this system:

- Every time a heuristic is selected (whether through a Dispatcher or explicit contract-matching), log the triple: **(state-shape → heuristic chosen → outcome)**.
- When a specific state-shape → heuristic mapping accumulates enough frequency and a high enough success rate, **promote it**: bypass the deliberate selection step for that shape and fire the heuristic directly. This is "instinct" — not a different kind of heuristic, but a cached, earned shortcut.
- Anything that hasn't earned promotion stays in the deliberate/intentional path: slower, but safer, and still building its track record.
- **Demotion matters as much as promotion.** If a promoted shortcut starts failing on new inputs (i.e. the input distribution shifted), it needs to fall back to deliberate dispatch — the same way a human habit breaks down in a novel context and forces conscious reasoning to resume.

This reframes the "efficiency vs. correctness" tension from earlier discussion: instinct isn't inherently faster because it's a lesser process, it's faster because it's a *proven* one. Intentional heuristics aren't slower because they're worse, they're slower because they haven't earned trust yet.

---

## 6. Open Questions (not yet resolved — flagged for the agent to reason about, not to silently assume an answer to)

- What threshold of frequency/reliability is sufficient to earn promotion from intentional to instinctual? Static threshold, or adaptive per heuristic/domain?
- What signal triggers demotion — an outright failure, a confidence drop, or a pattern of near-misses?
- How should contract collisions be surfaced and resolved during the hand-authored (Phase 1) stage, so they don't get carried forward into whatever gets compiled in Phase 2?
- What's the actual schema for logging (state-shape → heuristic → outcome) in a way that's cheap enough to not undermine the efficiency goal itself?
- Does "state-shape" need a formal definition/type system across all heuristics, or can it stay implicit per-project for now?

---

## 7. Cross-Project Relevance

This is meant to apply across all current and future projects, not just one:

- **Algorithm-learning framework** — already an explicit, ordered stack (problem → constraints → logic → steps → code → Big O); a candidate reference implementation of Phase 1 structure.
- **Problem-solving curriculum (Pólya-based)** — the existing Dispatcher persona is a natural candidate for the single explicit decision point described in Section 3; Teacher/Tutor/Coach/Problem Generator personas are candidate stacks with their own contracts.
- **5x-developer curriculum** — the seven tiers (See, Separate, Verify, Build, Meta, Incubate, Learn) are already a position-ordered stack; the 34 discrete cognitive processes are candidate heuristics scoped to specific tiers.
- **Structure-decomposition curriculum** — directly related to Section 3's contract-matching idea: making the "hidden structure" of an open-ended prompt explicit is equivalent to identifying which stack and which stage applies.
- **SliceKit** — the largest existing codebase; likely the first place a real (not toy) implementation of promotion/demotion logging would need to run.
