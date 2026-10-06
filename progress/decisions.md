# decisions — owner decision ledger (APPEND-ONLY)

Protocol: [specs/08](../specs/08-build-process.md) BP-15 (ledger), BP-17
(record format). Validated by `python3 scripts/preflight.py`.

Rules: an entry is never edited after the owner answers — corrections are NEW
entries that name the old one in `supersedes:` (the old entry gets only its
`superseded_by:` field filled, nothing else). An agent whose work triggers an
owner-level decision (taste, money, autonomy, scope, hard-to-reverse) writes a
`proposed` entry and STOPS; only an explicit owner answer unblocks. A session
may surface a pending proposal but must not act on it. IDs `D-<n>` are
permanent and never reused (INV-2 spirit).

Record format (BP-17): heading `## D-<n> — <title>`, then `key: value` field
lines, then free prose. `status` ∈ proposed | accepted | rejected | superseded.
Reference fields (`supersedes`, `superseded_by`, `affects`, `evidence`) hold
comma-separated references in the BP-17 grammar, or `none`.

D-1..D-5 are BACKFILLED on 2026-10-05 from BUILDLOG entries that recorded owner
decisions in prose before this ledger existed; their evidence field is the
authority, the summary here is a pointer.

---

## D-1 — Next session sharpens specs, does not implement
status: accepted
date: 2026-07-09T20:00+03:00
decided_by: owner
supersedes: none
superseded_by: none
affects: P1.1, F-1
evidence: BUILDLOG@2026-07-09T20:00+03:00, spec_sharpening_2026-07-10.md

Executed: the sharpening pass ran 2026-07-10 and produced F-1..F-18. Its
application is D-6.

## D-2 — Persona format adopted as defect-finding audit layer (M-18)
status: accepted
date: 2026-07-10T18:00+03:00
decided_by: owner
supersedes: none
superseded_by: none
affects: M-18
evidence: BUILDLOG@2026-07-10T18:00+03:00, BUILDLOG@2026-07-10T18:30+03:00, specs_persona_story.md

Accepted on round-1 A/B evidence + owner's external tests; no further runs
(token budget). Persona rendering is never normative text.

## D-3 — Heuristic-level persona/strain deferred to WF-5a seed experiment
status: accepted
date: 2026-07-10T18:50+03:00
decided_by: owner
supersedes: none
superseded_by: none
affects: WF-5a
evidence: BUILDLOG@2026-07-10T18:50+03:00

Judged at Phase-2 graduation from normal outcome/retrieval logs. No schema
change.

## D-4 — HANDOFF.md trust cache adopted (BP-14, M-19)
status: accepted
date: 2026-07-10T19:15+03:00
decided_by: owner
supersedes: none
superseded_by: none
affects: BP-14, BP-8, BP-9, M-19
evidence: BUILDLOG@2026-07-10T19:15+03:00

## D-5 — Harness implementation repo location
status: accepted
date: 2026-07-10T20:00+03:00
decided_by: owner
supersedes: none
superseded_by: none
affects: P1.1, F-6
evidence: BUILDLOG@2026-07-10T20:00+03:00

Dedicated repo at `~/Desktop/python/portfolio_projects/heurestic_harness`
(spelling exactly as the owner wrote it — flag before scaffold; names freeze).
Verified 2026-10-05: directory does not exist yet (P1.1 not started).

## D-6 — Apply spec-sharpening findings F-1..F-18
status: proposed
date: 2026-07-10T15:05+03:00
decided_by: pending
supersedes: none
superseded_by: none
affects: F-1, F-2, F-3, F-4, F-5, F-6, P1.1
evidence: spec_sharpening_2026-07-10.md, BUILDLOG@2026-07-10T15:05+03:00, BUILDLOG@2026-07-10T20:00+03:00
stage: ST-3 design checked and corrected
impact: advances
why: the next stop on the road to INT-4; two fixes touch names that freeze once built

Essence: which of the 18 proposed spec diffs become spec text before any code
is written.
Analogy: correcting the blueprint before the foundation is poured.
Impact + reversibility: cheap now (text diffs); after P1.1 each unapplied
major finding becomes a code/schema migration. F-2 (missing `project` field)
and F-6 (package naming) touch names that freeze at first publication
(INV-6) — those are the one-way doors.
Architecture points at: B — the sharpening pass itself ranked F-1/F-2/F-6 as
"before P1.1"; INV-6 makes naming findings the only time-critical ones.
Context: owner asked for a plain-language impact walkthrough first; delivered
in-session 2026-07-10, no answer recorded since.
Options:
  A) apply all F-1..F-18 as proposed
  B) apply majors F-1..F-5 + F-6 now; minors F-7..F-18 reviewed later   ← DEFAULT
  C) walk through each finding individually with the owner
Decision: pending

## D-7 — How the Sept 2026 direction documents relate to the specs
status: accepted
date: 2026-10-05T17:05+03:00
decided_by: owner (via confirmation of INT-4, SIT-1)
supersedes: none
superseded_by: none
affects: DIRECTION.md, I-1, I-2, I-3
evidence: insights_from_other_conversations/INDEX.md, coherence/reentry/RE-1.md, coherence/intent.md

Essence: the specs describe a cue-indexed heuristic library served over MCP;
I-1/I-2 frame the project as two tracks (persona-organized corpus; contract-
bound heuristic stacks with a dispatcher). Which one is "what we are
building"?
Analogy: a second architect's sketch arrived after the blueprint was
approved — extension, replacement, or a separate building?
Impact + reversibility: decides whether specs 00–10 are revised, extended, or
left alone. Fully reversible while no code exists; becomes expensive once
P1.x schemas freeze (INV-6).
Architecture points at: A for now — INV-10 requires spec change by explicit
diff, and DM-2/02 Do-NOT-build already forbid persona fields in the schema
without evidence; recording the documents as inputs keeps every option open.
Options:
  A) record as inputs; specs unchanged until owner states the relation  ← DEFAULT
  B) revise specs/00 + data model to adopt Track A/B framing
  C) separate spec set (or repo) for the direction work; harness specs stay
Decision: A in substance, settled 2026-10-06 by the owner's confirmation of
  INT-4 at re-entry RE-1 (SIT-1): the documents describe later layers of the
  same system (intent kept, grown by additions, road unchanged); specs stay
  as they are until those layers are reached. Applied under HC-29 (the
  owner's earlier answer decides it); the owner may object.

## D-8 — Where the innovations/ toolbox lives
status: accepted
date: 2026-10-05T17:05+03:00
decided_by: owner
supersedes: none
superseded_by: none
affects: innovations/
evidence: innovations/CONTRIBUTING.md
stage: none (housekeeping)
impact: untouched
why: where a borrowed toolbox lives; no effect on the intent

Essence: innovations/ (14 patterns from other projects) is untracked here.
Commit it, ignore it, or move it out?
Analogy: a borrowed toolbox — keep a copy in this workshop, or fetch it from
its owner's shed each time.
Impact + reversibility: committing a copy makes it drift from its origin
(its own CONTRIBUTING §4 evolve-sync rule); ignoring it means a fresh clone
lacks it — but the kits actually adopted are already copied into this repo's
own files, so nothing load-bearing depends on it. Reversible either way.
Architecture points at: B — INV-1 wants canonical truth in one place; the
toolbox's canonical place is its origin project.
Options:
  A) commit as a vendored snapshot with a source/date note
  B) add to .gitignore; keep as local reference                        ← DEFAULT
  C) move it out of this repo entirely
Decision: A, as this project's OWN copy, not a vendored snapshot. Owner,
  2026-10-06: "local innovations/ belongs to this project so it too gets
  committed." It will later be moved to another project folder that future
  projects inherit (owner, 2026-10-05). The default (B) is rejected.

## D-9 — Adopt the handoff system (BP-15..BP-21)
status: accepted
date: 2026-10-05T17:00+03:00
decided_by: owner
supersedes: none
superseded_by: none
affects: BP-15, BP-16, BP-17, BP-18, BP-19, BP-20, BP-21
evidence: BUILDLOG@2026-10-05T17:05+03:00

Owner directive in-session: use the innovations/ kits; "defensive design …
even if the system won't need it yet … where it's cheapest, which is here",
because the handoff layer may later grow into full RAG + graph structure.
Spec text still passes the gate (INV-10): uncommitted until owner review.

## D-10 — Activate the commit-msg hook
status: proposed
date: 2026-10-05T17:05+03:00
decided_by: pending
supersedes: none
superseded_by: none
affects: BP-10, BP-19
evidence: .githooks/commit-msg
stage: none (housekeeping)
impact: untouched
why: whether commit messages are machine-checked; no effect on the intent

Essence: turn on machine enforcement of the BP-10 commit format for every
commit in this clone — including the owner's own.
Analogy: a lock that also locks out the landlord unless they use the spare
key (`--no-verify`).
Impact + reversibility: owner commits like "storing to github" would be
rejected. One command to enable, one to disable
(`git config --unset core.hooksPath`).
Architecture points at: A — machine-enforced-laws; but it changes the
owner's own workflow, hence a proposal.
Options:
  A) activate: `git config core.hooksPath .githooks`                    ← DEFAULT
  B) keep the hook file, leave it inactive (preflight keeps warning)
Decision: pending

## D-11 — Corrections to the handoff system as first built
status: accepted
date: 2026-10-05T20:15+03:00
decided_by: owner
supersedes: none
superseded_by: none
affects: BP-4, BP-6, BP-8, BP-9, BP-14, BP-19, D-9
evidence: BUILDLOG@2026-10-05T20:20+03:00

Owner approved ("yes") six fixes found after D-9's system was built:
BP-14's conflict rule now names decisions.md; BP-6 limited to
implementation-level decisions; BP-8's "four reads" corrected; STATUS no
longer claims "done" without a commit (BP-4); preflight now gates stale
"pending" claims about answered decisions (BP-19); and this entry carries the
links D-9 omitted. D-9 itself had BP-8, BP-9 and BP-14 missing from its
`affects:` field, but it is not edited, because answered entries are
append-only (BP-15).
