# BUILDLOG

Append-only. Protocol per [specs/08-build-process.md](../specs/08-build-process.md) (BP-5, BP-6).
Corrections are new entries, never edits.

## 2026-07-09T17:30+03:00 · claude-fable-5 · pi · specs
INTENT: author the complete spec set (00–09) + progress scaffolding from the
settled planning conversation; initialize git.

OUTCOME: done (see initial commit). Key decisions carried from planning, with reasons:
- Full endgame specced as an autonomy ladder (trust earned from logged evidence),
  not built up front — evaluation signal at personal scale comes from the human
  gate + verifiable coding domain.
- Parallel subagents restored (Cline native, AGT-10..12) after confirming Cline
  supports read-only parallel subagents; MCP-side `second_opinion` reserved as
  fallback (P5.4).
- Profile split: cue-less kernel (always injected, ≤15 lines) + cue-indexed
  `user-fact` library entries — owner's cue-based-recall argument ("coffee cup →
  honey"); a cue-recalled user fact is architecturally identical to a heuristic.
- Cut permanently: reasoning scorecards, canary/A-B, meta-memory layer (need
  volume that doesn't exist at n=1); data model future-proofed instead
  (model/machine/project fields, DM-14 all-candidates logging).
- Expensive-later survivors put in INV/DM: write-time redaction (INV-5),
  structured task summaries (AGT-4), baseline week (WF-8), no-outcome bucket
  (DM-17), frozen tool API (INV-6), license-before-contributors (FUT-1).
- Flight recorder outside git (INV-8): the record of failures must not live
  inside the thing that fails (owner's intuition, formalized).
- 09-how-to-write-specs written portable/self-contained per owner request; it is
  itself a heuristic (cue + body) and should be ingested once the harness runs.

Source material: idea/ (deepseek, kimi, gpt, manus documents) — manus.md
citations partly unverifiable; treated as vision, not evidence.

NEXT: P1.1 (repo scaffold) — but first the owner decides: build here or in a
dedicated repo (see STATUS open decisions). Any agent resuming: BP-8 ritual.

## 2026-07-09T18:20+03:00 · claude-fable-5 · pi · specs (amendment)
INTENT: add manual-first verification layer per owner request — user manual,
user stories wired into acceptance, method update.

OUTCOME: done. MANUAL.md written from specs alone (owner-facing, phase-tagged);
specs/10-user-stories.md added (US-1..20 + US-RULE-1..3: stories walked live at
each phase acceptance pass, failure blocks phase completion); 06-phases.md
acceptance rows P1.11/P2.6/P3.4/P4.3 now reference their stories; 09 gained
M-15 (manual-before-implementation, stories as acceptance) — appended, no
renumbering of M-ids. Decision: stories are append-only/stable-numbered and
verified by walking, never by code reading — keeps the story layer honest as
a check independent of the implementer's self-report.
NEXT: unchanged — owner decision on repo location, then P1.1.

## 2026-07-09T19:05+03:00 · claude-fable-5 · pi · specs (amendment)
INTENT: merge owner-provided update of 09 (root copy 09-how-to-write-specs.md)
into specs/09 after review.

OUTCOME: done. Adopted M-16 (manual delta classifies change on existing
systems: extension grows / migration rewords-not-promises / refactor delta
empty as acceptance criterion) and M-17 (role stories beyond end user;
maintainer stories never optional; M-4 pruning applies to personas) — both
judged consistent with the method's voice and M-14. Editorial fixes during
merge: intro range M-1…M-14 → M-1…M-17 (was stale since M-15), stray blank
line removed. Checklist step 4 extended per the update. Root copy left in
place untracked (owner's working copy — owner may delete).
NEXT: unchanged — owner decision on repo location, then P1.1. Optional
follow-up: apply M-17 to specs/10 (maintainer/operator story sets).

## 2026-07-09T19:40+03:00 · claude-fable-5 · pi · specs (amendment) + SESSION HANDOFF
INTENT: apply M-17 to specs/10 (role stories), then hand off — planning
session context exhausted.

OUTCOME: done. specs/10 gained role stories US-21..25 (maintainer ×3,
operator ×2; persona cast pruned per M-17/M-4); 06 P1.11 acceptance row now
includes them.

HANDOFF STATE (complete — any fresh agent resumes from files alone, BP-8):
- Specs 00–10 + MANUAL.md: complete and internally consistent. Method file
  09 at M-17 (synced with owner's spec-driven-ai-projects skill).
- Implementation: NOT STARTED. Next work = P1.1 (repo scaffold), blocked only
  on owner decision: build in this repo vs dedicated ~/heuristic-harness
  (see STATUS open decisions; this session recommended: this repo).
- Untracked root file 09-how-to-write-specs.md is the owner's working copy,
  redundant with specs/09 — owner may delete, agents leave it alone.
- No code exists; no ~/.harness/ exists yet; nothing registered in Cline.
- Resume ritual: read README.md → specs/00 → specs/01 → progress/STATUS.md →
  this file's tail. Then claim P1.1 in STATUS (BP-3), journal intent, build.

## 2026-07-09T20:00+03:00 · claude-fable-5 · pi · handoff correction
INTENT: correct the previous handoff's NEXT — owner clarified the next session
is to SHARPEN the specs, not implement.

OUTCOME: NEXT is now a spec-sharpening pass by a fresh-context agent, BEFORE
any P1.x work. Scope of that pass: (1) full read of specs 00-10 + MANUAL.md
with fresh eyes; (2) consistency audit — cross-references, requirement IDs,
contradictions between files, spec-vs-manual promise mismatches (M-15/M-16);
(3) implementability audit — ambiguities an implementer would trip on, MUSTs
without a verifiable check (M-1/M-5), acceptance criteria that can't actually
be walked; (4) self-conformance audit — score this spec set against its own
method 09 M-1..M-17 and the 09 checklist; (5) output = findings + proposed
amendments as diffs for the gate, journaled here (INV-10). Implementation
remains blocked until the owner closes the sharpening pass and the repo-
location decision.

## 2026-07-10T14:55+03:00 · claude-fable-5 · pi · spec-sharpening pass (INV-10, per 2026-07-09T20:00 mandate)
INTENT: execute the sharpening pass — full fresh read of specs 00-10 +
MANUAL.md done; now writing findings + proposed amendments as diffs to
spec_sharpening_2026-07-10.md (repo root, untracked — gate review material,
INV-10). No spec file will be modified; no implementation. Will also assess
owner-provided findings_report.md (persona-heuristics proposal) at owner
request; assessment delivered in-session, summary journaled here.

## 2026-07-10T15:05+03:00 · claude-fable-5 · pi · spec-sharpening pass — OUTCOME
OUTCOME: done. Findings + proposed diffs in spec_sharpening_2026-07-10.md
(repo root, untracked — gate review material per INV-10; no spec file was
modified). 15 findings: 5 major implementability gaps (F-1 agent/model
identity has no channel to the server; F-2 log_outcome/log_lesson lack the
mandatory `project` field; F-3 DM-17 retrieval↔outcome join undefined; F-4
`git mv` cannot promote untracked staging files — WF-1/MANUAL both broken;
F-5 US-24 needs stats.py (P2.5) but is scheduled at P1.11), 4 medium (F-6
server/ vs harness package name; F-7 "expensive-later item #N" cites a list
absent from specs; F-8 PH-6 literally forbids spec work + BP-13 drill is
pass-less; F-9 TOOL-3 threshold homeless), 6 minor. Self-conformance vs 09:
strong — M-8 demonstrably holds (this pass cold-started from files alone);
sole M-14 violation is F-8. Recommended order: F-1/F-2/F-6 before P1.1.

Also assessed owner-provided findings_report.md (persona-heuristics
proposal) at owner request: recommend NOT adopting as-is — Finding 3
misreads the data model (attacks `domain_tags`/`summary` fields that don't
exist in 02); persona/strain frontmatter now would violate 02 Do-NOT-build
and the trust-ladder method. Salvage: (a) short prior-art note in 00
(overlap with Cline rules/skills — fair point, matches assess_idea.md),
(b) persona-voiced BODIES for 2-3 of the P1.9 seed heuristics as a free
experiment inside the existing schema, judged later from outcome logs.
Full reasoning delivered to owner in-session.

DIRTY STATE (BP-9, intentional): spec_sharpening_2026-07-10.md untracked
(awaiting gate); BUILDLOG modified (these two entries); owner files
assess_idea.md, feature1_spec_story.md, findings_report.md untracked
(owner's, agents leave alone). Nothing committed — owner did not request
commits; gate commits accepted amendments with rationale per INV-10.
NEXT: gate reviews sharpening findings + repo-location decision; then P1.1.

## 2026-07-10T15:40+03:00 · claude-fable-5 · pi · persona-spec experiment (owner-directed)
INTENT: owner directs (a) a persona rendering of the spec set in the style of
feature1_spec_story.md incl. user-story layer → specs_persona_story.md, and
(b) an A/B test of dry vs persona format run by the owner in fresh Cline
sessions → persona_test_cline.md (two paste-ready packets over specs 02+03+04:
dry verbatim vs persona voice-only transform WITHOUT gap confessions, plus a
grading key of 7 seeded defects from spec_sharpening_2026-07-10.md). Both
files repo root, untracked — experiment material, not spec changes (INV-10
untouched). Rationale journaled: the confessional story cannot double as test
material (it contains the answer key), hence two artifacts.

## 2026-07-10T16:05+03:00 · claude-fable-5 · pi · persona-spec experiment — OUTCOME
OUTCOME: done. Two artifacts, repo root, untracked (experiment material, no
spec touched): specs_persona_story.md — full spec set narrated first-person
per the feature1_spec_story.md format, user-story layer woven in, confessions
[H-1..H-9] mapped 1:1 to sharpening findings F-1..F-9; persona_test_cline.md
— A/B packets for owner-run test in fresh Cline sessions (Packet A: dry specs
02+03+04 verbatim; Packet B: same content voice-transformed, all IDs kept,
NO confessions; identical audit prompt; grading key = 7 seeded defects F-1,
F-2, F-3, F-7, F-9, F-10, F-13). Decision: story and test material split into
two artifacts because a confessional story contains the answer key.
Known bias journaled: packet B was written by the same agent that found the
seeded defects; mitigation = voice-only transform rule + owner may diff-read.
DIRTY STATE (BP-9): both new files + spec_sharpening_2026-07-10.md untracked;
BUILDLOG modified. Nothing committed (owner has not requested commits).
NEXT: owner runs packets in Cline (2×A, 2×B, empty folder, NOT this repo),
returns outputs for grading; separately: gate review of sharpening findings
+ repo-location decision still open.

## 2026-07-10T17:30+03:00 · claude-fable-5 · pi · persona A/B test — first results graded
OUTCOME: owner ran one Cline session per packet (n=1 each; second runs still
recommended). Seeded-defect recall (key of 7): dry packet A = 2/7 (F-3, F-13);
persona packet B = 3/7 (F-3, F-9, F-13). Both missed F-1, F-2, F-7, F-10.
Finding volume: A = 11, B = 19; precision comparable (B chattier, not
noisier). Meta-result: runs surfaced two REAL defects the sharpening audit
missed — F-16 (kernel-update proposals have no producing tool despite
"kind":"kernel" event in schema; dry run) and F-17 (status: candidate not in
DM-7 enum; persona run), plus minor F-18 (AGT-10 15% formula) — appended to
spec_sharpening_2026-07-10.md addendum with diffs. Interpretation journaled:
directional support for persona format (more seeded + more true unseeded
findings incl. best single catch), NOT conclusive — single run, and B's
higher volume confounds recall. Result files: defects_report.md (A),
defects_packet_B.md (B), owner-provided, untracked.
NEXT: optional runs A2/B2 for variance; gate review of sharpening findings
(now F-1..F-18) + repo location still open.

## 2026-07-10T18:00+03:00 · claude-fable-5 · pi · persona experiment closed (owner decision)
OUTCOME: owner accepts persona format on round-1 evidence + external
corroboration (own tests in other projects, incl. a Fable session reaching
the same conclusion); no further test runs — token budget. Proposed M-18
(persona rendering = comprehension/audit layer over numbered specs, never
normative) appended to spec_sharpening_2026-07-10.md as F-19, awaiting gate
with F-1..F-18. specs_persona_story.md stands as the first M-18 artifact;
it must be regenerated/marked stale when specs change.
NEXT: gate review of F-1..F-19 diffs + repo-location decision; then P1.1.

## 2026-07-10T18:30+03:00 · claude-fable-5 · pi · specs/09 amendment (INV-10, owner-directed)
M-18 added to specs/09 (persona rendering as defect-finding audit layer,
never normative text); intro range M-1…M-17 → M-1…M-18. F-19 in the
sharpening file marked applied. Evidence base: this project's A/B run +
owner's external tests. Uncommitted (owner commits per gate discipline).

## 2026-07-10T18:50+03:00 · claude-fable-5 · pi · specs/05 amendment (INV-10, owner-directed)
WF-5a added: seed library embeds persona-vs-dry body comparison and
strain-as-tag retrieval comparison; answered by normal outcome/retrieval
logs, reported by librarian, judged at Phase-2 graduation. No schema change.
Uncommitted.

## 2026-07-10T19:15+03:00 · claude-fable-5 · pi · specs/08+09 amendment (INV-10, owner-directed)
BP-14 (progress/HANDOFF.md trust cache: bounded, rewritten, evidenced
"do-not-re-check" list; stale-on-change; STATUS/BUILDLOG win conflicts) +
BP-8/BP-9 wired to it; M-19 added to 09 (method-level). First HANDOFF.md
written for current state. Uncommitted.

## 2026-07-10T20:00+03:00 · claude-fable-5 · pi · owner decisions
Repo location DECIDED: ~/Desktop/python/portfolio_projects/heurestic_harness
(dedicated repo; spelling as owner wrote it — flag before scaffold, names
freeze). F-1..F-18 application pending: owner requested plain-language
impact walkthrough before choosing; delivered in-session.
