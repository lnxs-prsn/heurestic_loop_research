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
