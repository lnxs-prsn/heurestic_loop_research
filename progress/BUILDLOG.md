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
