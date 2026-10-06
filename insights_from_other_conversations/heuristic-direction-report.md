# Heuristic Project — Direction Report (v3)

**Purpose of this document:** context for an agent working on the heuristics project. This replaces the earlier note, which incorrectly framed the corpus/persona direction as a correction or successor to the proceduralization direction. **They are two separate, independent directions** — not sequential versions, not alternatives competing for the same slot, and neither depends on the other to make sense. They answer different questions. This document keeps them clearly separated so nothing about one gets read as a constraint on the other.

---

## 0. Shared Foundation (applies to both tracks)

Both directions grow out of the same starting thesis and insight — this part is common ground, everything after it forks.

**Core thesis:** Current LLMs are already capable enough for most complex tasks a human can do, and in raw output quality are comparable to or exceed a single human on tasks they've seen enough of — but they lose to a 10-year-old child on general intelligence, because the gap is sample efficiency, not scale. The working explanation: human intelligence is the crystallization of experience into heuristics and meta-heuristics, most of which the person is never consciously aware of.

**Foundational insight:** heuristics are not interchangeable modules. Like compatible parts of a house, they build on top of each other, and dropping in one that doesn't match the layer below it produces friction, not new capability. This holds true even in dysfunctional people — heuristics still stack in a consistent, fixed order.

Track A and Track B each take that shared foundation in a different direction. Read them as independent.

---

## Track A — Heuristic Corpus & Persona Organization

**The question this track answers:** given a large, continuously growing collection of heuristics, how do you know which one to use, without every decision requiring a scan of the whole collection?

**A1 — A growing corpus, not a fixed set.**
Heuristics accumulate continuously, sourced from Said's own interactions with many different agents. Agents compile heuristics themselves from inspiration gained while talking with him. The corpus has no target size or endpoint.

**A2 — Personas organize and limit, they don't just index.**
Personas exist so an agent facing a corpus full of many similar heuristics doesn't have to figure out which one applies from scratch. Personas are capacity-limited by design: humans achieve their complexity with very few heuristics, not many, so a persona holds a small, curated, complementary set drawn from the corpus rather than broad access to everything relevant.

**A3 — Corpus size never becomes a bottleneck, because nothing ever queries the whole corpus.**
Access is always mediated through a persona. When a new problem comes up, Said decides which existing personas (built for similar previous problems) already apply and reuses them. For a genuinely new kind of problem, a new persona gets derived. Growth in corpus size doesn't increase the cost of any single decision, because that decision only ever touches the small set of personas relevant right now.

**A4 — Assignment is corrected continuously, not solved upfront.**
A new heuristic doesn't need to be perfectly filed on arrival. Assignment can start arbitrary and get corrected through Said's own interaction with the agent over time, human in the loop. Sufficient for the current stage.

**A5 — Reuse-vs-derive is resolved empirically, not by upfront judgment.**
Rather than requiring a correct judgment call in advance about whether an existing persona fits well enough, the system spawns both: the existing persona(s) and a newly derived one. Whichever performs better is the one worth keeping.

**A6 — Parallelism across personas is a structural advantage over a single human.**
A human can only occupy one persona at a time and switches between them serially. This system can spawn subagents that take on different persona roles simultaneously, tackling the same problem from multiple persona-angles in parallel.

**Supplementary framings (precedent/vocabulary, not instruction):**
- *Mixture-of-Experts routing* — matches A2/A3's shape, but standard MoE gates are learned/dense and need retraining to update; these personas are symbolic and human-authored, which fits a continuously-growing, human-corrected corpus better.
- *Case-based reasoning* (Retrieve → Reuse → Revise → Retain) — the formal name for the matching pattern in A3. Its known weak point is the retrieve step; A5's answer (spawn both, test empirically) is a recognized, legitimate way around that weak point.
- *Society of Mind* (Minsky) — precedent for A6: intelligence as interaction of many simpler semi-independent agents. Difference: Minsky's agents are effectively serial/interacting within one system; these can run as genuinely concurrent processes.
- *Explore–exploit / evolutionary variation-selection* — the general pattern behind A5: generate a variation, test against the incumbent, retain whichever wins.

**Open dependencies for Track A (flagged, not resolved):**
- Human-in-the-loop is currently the evaluation function twice: for assignment correction (A4) and for "worth keeping" judgment (A5). Reasonable at current scale; a known dependency if the system ever needs to run without Said watching in real time.
- Correction throughput vs. corpus growth rate — not a problem now, worth monitoring if ingestion volume increases.
- Persona capacity limit is currently implicit — not yet specified how large "small" is.
- Reusability/transferability of a derived persona is undefined — if reused later by Said or another subagent, it likely needs an externalized standard form, not yet specified.
- Parallel-persona reconciliation (A6) — no defined merge/reconciliation step yet for when subagents running different personas disagree.

---

## Track B — Proceduralization (Instinct vs. Deliberate Execution)

**The question this track answers:** for any single heuristic, how does it move from being applied deliberately (explicit, checked, effortful) to being applied automatically (fast, compiled, unconscious) — and back, if it stops working?

**B1 — Two-phase bootstrap.**
Initial heuristics are hand-authored and explicit — contracts and stages defined directly, the way the algorithm-learning framework's pipeline (problem → constraints → logic → steps → code → Big O) already is. The end goal is for the agent to eventually discover/compile its own heuristics from feedback, the way a child does.

**B2 — The system needs both an instinctual and an intentional mode of heuristic usage at once**, not one replacing the other. How to achieve this was the open problem this track was created to solve.

**Supplementary framing (precedent/vocabulary, not instruction):**
- *Proceduralization (ACT-R, Anderson)* — explicit/deliberate rules compile into fast/automatic execution, driven by two tracked signals: frequency (how often a rule fires) and reliability (how often it succeeds when it fires). Proposed translation: log (state-shape → heuristic chosen → outcome) triples; promote a mapping to instinctual/direct-fire once it earns enough frequency and reliability; demote it back to deliberate if it starts failing on inputs it wasn't built for.

**Open dependencies for Track B (flagged, not resolved):**
- What threshold of frequency/reliability earns promotion — static or adaptive?
- What signal triggers demotion — outright failure, confidence drop, or a pattern of near-misses?
- What's the actual logging schema for (state-shape → heuristic → outcome), cheap enough not to undermine the efficiency goal itself?
- Does "state-shape" need a formal type system across all heuristics, or can it stay implicit per-project for now?

---

## Where the Two Tracks Could Compose (possibility, not a dependency)

Proceduralization (Track B) could, in principle, apply to individual heuristics living inside a persona (Track A) — a heuristic used often and reliably within a given persona could get promoted to instinctual execution within that persona's stack. This is a possible future composition, not something either track currently requires from the other. An agent should not assume this composition is already decided or in progress.

---

## Cross-Project Relevance (applies to both tracks)

- **Algorithm-learning framework** — an existing explicit, ordered pipeline; relevant to Track B (B1) as a working example of hand-authored stages, and to Track A as a candidate structure for what a single persona's internal contents could look like.
- **Problem-solving curriculum (Pólya-based)** — existing Teacher/Tutor/Coach/Problem Generator/Dispatcher personas are a live example of Track A's persona-as-organizing-unit idea; the Dispatcher is also a candidate site for Track B's promotion/demotion logic.
- **5x-developer curriculum** — the seven tiers and 34 processes are a candidate pre-existing corpus for Track A, already loosely organized.
- **Structure-decomposition curriculum** — related to Track A's persona-matching (A3): recognizing which persona/stage a new problem belongs to is the same move as decomposing an open-ended prompt into explicit structure.
- **SliceKit** — the largest existing codebase; the most likely place either track would actually get implemented.
