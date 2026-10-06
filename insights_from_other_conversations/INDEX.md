# INDEX — intake register for material from other conversations

Protocol: [specs/08](../specs/08-build-process.md) BP-20 (intake), BP-17
(record format). Validated by `python3 scripts/preflight.py`.

Every file in this folder has exactly one `I-<n>` record here. A file without
a record is unregistered material — preflight flags it. Registering is not
adopting: what the project does with an input is an owner decision in
[decisions.md](../progress/decisions.md), linked via `affects:`.

`status` ∈ unread (registered, not yet analysed) | digested (analysed; summary
below) | applied (its content reached specs, via a D- entry) | rejected.
IDs are permanent and never reused. Append-only; status/links may be updated
in place as the input moves through the pipeline.

---

## I-1 — heuristic-stack-system-direction.md
status: digested
date: 2026-09-08
received: 2026-10-05
source: owner, design conversation outside this repo (file mtime 2026-09-08)
file: insights_from_other_conversations/heuristic-stack-system-direction.md
affects: D-7
evidence: BUILDLOG@2026-10-05T17:05+03:00, BUILDLOG@2026-10-05T22:00+03:00
stages: ST-2, ST-5, ST-6
impact: changes-intent

Persona = fixed invariant stacking order of heuristics (I/O contracts in
position), not a role label. Eligibility by contract match, not ranked
search; contract collision and position violation as design bugs; real choice
concentrated in one dispatcher. Two-phase roadmap: hand-authored stacks, then
self-compiled stacks from feedback.

Processed 2026-10-05 against INT-2 (HC-17); moves 1 and 5 in RE-1.
**What:** heuristics as an ordered stack with input/output contracts; a
persona = a fixed stacking order; one dispatcher picks a stack; a
deliberate → instinctive path for proven heuristics, with demotion.
**Why:** LLMs lose to a child on sample efficiency; humans crystallize
heuristics that build on each other in a fixed order; mismatched ones cause
friction.
**How:** first hand-authored stacks, then the agent compiles its own stack
from feedback; log (state-shape → heuristic → outcome) to drive promotion.

## I-2 — heuristic-direction-report.md (v3)
status: digested
date: 2026-09-09
received: 2026-10-05
source: owner, design conversation outside this repo (file mtime 2026-09-09)
file: insights_from_other_conversations/heuristic-direction-report.md
affects: D-7
evidence: BUILDLOG@2026-10-05T17:05+03:00, BUILDLOG@2026-10-05T22:00+03:00
stages: ST-2, ST-5, ST-6
impact: route-only

Declares itself the replacement of an earlier note: two INDEPENDENT tracks
sharing one thesis. Track A — growing corpus organized/limited by capacity-
bounded personas; reuse-vs-derive resolved empirically by spawning both;
parallel persona subagents. Track B — proceduralization (see file). Neither
constrains the other.

Processed 2026-10-05 against INT-2 (HC-17); moves 4 and 5 in RE-1.
**What:** two independent tracks. Track A: a growing corpus organized and
limited by personas. Track B: proceduralization (deliberate → instinctive).
**Why:** a growing corpus must not need a whole-corpus scan per decision;
heuristics need to earn fast use.
**How:** capacity-limited personas, reuse-vs-derive settled by spawning both
and keeping the better, parallel persona subagents; promotion/demotion by
frequency and reliability.

## I-3 — september2026.md
status: digested
date: 2026-10-05
received: 2026-10-05
source: owner, compiled from several design conversations (62 KB at intake, mtime 2026-10-05T16:54; ~~62 KB~~ STALE — shrank to 48 KB at 2026-10-05T17:14, the same minute I-4 appeared, so part was likely moved into I-4; the 48 KB version is what was processed)
file: insights_from_other_conversations/september2026.md
affects: D-7
evidence: BUILDLOG@2026-10-05T17:05+03:00, BUILDLOG@2026-10-05T22:00+03:00
stages: ST-2, ST-5, ST-6
impact: changes-intent

Raw clues/open questions, not a spec. Opening sections overlap I-1/I-2
(thesis, personas, hiring-analogy dispatch). Only the first ~40 lines read at
intake; full digest pending.

Processed 2026-10-05 against INT-2 (HC-17), read in full; moves 1, 2, 3,
4 and 6 in RE-1. Five "insights": two versions of an insight report, two
replies on drift detection, and a v2 report.
**What:** the system's target is the owner's architecture-level rule-making;
need = gap between a project's spirit and its state; a later persistent
"person" assistant; a drift/circuit-breaker design (human as outside check
for now, cheap self-check, periodic reflection); how specs are run in the
owner's other projects (single-cycle, contract hard-stop); a fast
decision-model product as a possible instinctive mode.
**Why:** agents have no heuristic for making rules; reinforcement alone
can't tell when a habit stopped paying off.
**How:** extract the owner's recognition heuristic by real-time
interrogation (not log review); surface usage patterns for the owner to
notice drift; the assistant's self-management grows later.

2026-10-06 update: the owner saved the rest of this file (48 KB → 69 KB,
mtime 2026-10-06T10:15). New **insight 6**, "updated version of insight 5"
(the Sep 22 v2 report), processed against INT-2. New relative to insight 5:
- **§6 [SAID]** the original question: "could I build a project of building a
  person out of heuristics, as personality is ultimately just a chain of
  heuristics in sequence of loops?" Then the owner's pushback (individuation
  from scarcity explains differences without anything outside the heuristic
  model) and resolution ("what it is like" is a question one layer *below*
  heuristics; not a blocker, not a milestone). Assistant: a person is a
  project whose spirit = disposition/values, state = current situation.
- **§9 [SAID]** later positions gathered in one place: wrong spirit, books
  and vocabulary, fit judgment as DSA-style, the directed-graph stop, ambiguity
  at a stop is acceptable (already in I-4; now confirmed as owner positions
  in this report too). Assistant: each graph node's fit check is a closed
  yes/no question suited to a fast decision model.
- §7 unchanged: still holds both "surfacing data to the owner is sufficient
  for now" and "the actual goal is self-management", with the compiler's
  bootstrap-vs-end-state reading.

## I-4 — october2026.md (was november2026.md)
status: digested
date: 2026-10-05
received: 2026-10-05
source: owner, handoff report from another conversation (file appeared 2026-10-05T17:14 during this session; flagged by preflight)
file: insights_from_other_conversations/october2026.md
affects: D-7
evidence: BUILDLOG@2026-10-05T18:40+03:00, BUILDLOG@2026-10-05T22:00+03:00
stages: ST-2, ST-5, ST-6
impact: changes-intent

Self-described "handoff report" for an agent taking charge of the
heuristic-stack project; marks owner positions [Said] vs [Proposed]. Opening
restates the stack thesis (I-1). Only the first ~15 lines read at intake.

Processed 2026-10-05 against INT-2 (HC-17), read in full; moves 1, 2, 4
in RE-1. A handoff report from another conversation; marks [Said] vs
[Proposed].
**What:** whether the heuristic system can close the gap between AI and
experts on open-ended work (recognizing what the real question is). Owner
positions: the corpus also comes from books; spirit is always the problem
being solved, and the failure is a *wrong* spirit; process a question
through the heuristics as a directed graph, and where it stops is the
diagnosis; ambiguity at the stop is acceptable.
**Why:** experts' recognition and framing are invisible to them and missing
in AI.
**How:** (proposed, not adopted) fit judgment with applicability conditions
and labeled cases; job posts that state their assumptions; log the stop
node and the fit evidence at every node passed.

~~file: insights_from_other_conversations/november2026.md~~ **STALE — on
2026-10-06 november2026.md no longer existed; its content is identical to
october2026.md insight 1, so the owner renamed and extended it. Caught by
preflight (gate: file does not exist).** october2026.md adds, processed
2026-10-06 against INT-2:
- **Insight 2 — Sep 28 report, "ecosystem + plan as a continuous process,
  applied to agentic loops"** (owner: "only parts of this might be
  relevant"). **What:** loops judged on the health of shared state, not only
  task success (from a war-origin idea); planning never stops: small
  executions, a "now-plan" re-derived from reality vs a "segment plan",
  commitments at seams, and a "success clause" that cheaply declares the
  goal unreachable when the two plans drift too far. **Why:** local task
  success can hide system damage; agents need an honest exit. **How:** a
  LoopSpec sketch; hybrid of subagents for tasks and loops for maintaining
  conditions; three open decisions (what distance is, what ends a segment,
  what a checkpoint may do). Mostly the assistant's elaboration of two owner
  ideas.
- **Insight 3 — Sep 29 report, "easy path as a choice"** (owner: "in some
  sense very relevant, in some sense not"). **What:** prefer the cheap valid
  path; at spawn time ask whether a simpler decomposition exists; at seams
  classify friction as intrinsic (commit) or extrinsic (replan). **Why:**
  difficulty is diagnostic, not proof of progress. **How:** a rule at every
  seam: did the difficulty change my model of the problem, or only cost
  more? Cost-capped to avoid thrashing.
- Ends in an empty "insight 4" (possibly unfinished).

## I-5 — insights_6_10_2026.md
status: digested
date: 2026-10-06
received: 2026-10-06
source: owner, fetched from earlier chats on request (completeness check in RE-1) plus one new owner statement
file: insights_from_other_conversations/insights_6_10_2026.md
affects: D-7
evidence: BUILDLOG@2026-10-06T10:20+03:00
stages: ST-2, ST-4, ST-5, ST-6
impact: changes-intent

Processed 2026-10-06 against INT-2.
- **Insight 1 — Sep 16, the owner's own words:** "these heuristics make the
  agent more efficient, but the biggest benefit is that they allow the agent
  to answer 'how can I be helpful to this specific human in the way they
  define helpful', and I think this is the biggest gain of the heuristics
  project." **What:** a purpose statement. **Impact:** changes or sharpens
  the intent's *For*; close to INT-2's user-fact heuristics and profile
  kernel, which already make the library specific to one owner.
- **Insight 2 — Sep 29 "ants" report** (assistant-written, built on the
  owner's insight that every project using the corpus sends it tuning
  signals for free, like pheromones). **What:** records for heuristics,
  stacks, personas and per-task traces; an outcome signal ranked by trust
  (owner's real-time corrections highest, usage alone never); reinforce whole
  stacks, scoped; decay by time-since-eligible with a protected floor for
  rare critical heuristics; dispatch = job post → cheap threshold gate →
  hierarchy tiebreak; instinctive vs intentional with promotion/demotion; a
  persona lifecycle (trial, keep or drop, retire, merge) with an exploration
  rate; two timescales (per task; weekly reflection); a three-phase bootstrap
  (hand-authored → assisted tuning → self-compiling); metrics; failure
  modes (popularity vs quality, credit, scope leaks, rare-heuristic decay).
  **Why:** the corpus tunes itself as a side effect of normal use.
  **How:** first steps start from logging traces in one existing project.
- **Insight 3 — NEW owner statement (2026-10-06):** "we need to figure out
  how to manage irrelevant information for the heuristics system; this I
  think is one of the most important parts of the heuristic system." Not in
  any earlier material. **Impact:** advances (an unaddressed requirement).
- Ends in an empty "insight 4" (possibly unfinished).


## I-6 — insights_about_projects_that_are_similar.md
status: held
date: 2026-10-06
received: 2026-10-06
source: owner, landscape survey made by web Claude on 2026-10-06 against the RE-1 move list (web searches + READMEs/abstracts; nothing installed or run)
file: insights_from_other_conversations/insights_about_projects_that_are_similar.md
affects: none
evidence: BUILDLOG@2026-10-06T11:50+03:00
stages: ST-2, ST-4, ST-5, ST-6
impact: route-only

**HELD 2026-10-06 (owner):** not hiatus material, so out of scope for
re-entry RE-1; not to be processed yet. The summary below is intake-only
(written before the owner's instruction) and has not been applied anywhere.

Owner's note: "this helps us to see if we need to build everything from zero
or could we trial out some parts from already existing parts".
**What:** places the project against existing work in six clusters (skill
libraries such as the SKILL.md format; libraries learned from experience;
human-corrected rules; ordered skill graphs; persona routing; persistent
assistants) plus ACT-R/Soar. Verdict: the infrastructure layers are
crowded; the purpose layer is not. Unclaimed: person-defined helpfulness;
need/spirit and rule-making; question fit; capacity-limited personas with
hierarchy; real-time interrogation. Lessons: playbooks bloat without
pruning; repeated graph reinforcement plateaus then degrades (SE-GoS);
unsupervised rules hallucinate; specific rules beat general ones; vector
retrieval misses prerequisite chains (supports stacks); ACT-R production
compilation as the model for promotion; personas help alignment but can
hurt accuracy.
**Why:** decide what to build versus reuse.
**How:** four [Proposed] options: A build everything; B build the purpose
layer on an existing base (SKILL.md format, Letta or cognee); C question-fit
check first; D person-defined helpfulness first (B combines with C or D);
seven open questions for the owner.
