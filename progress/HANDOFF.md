# HANDOFF (BP-14) — rewritten each session end · this version: 2026-07-10, claude-fable-5

STATE: specs 00-10 + MANUAL sharpened and amended (M-18, M-19, WF-5a, BP-14);
implementation NOT started; P1.1 blocked on owner's repo-location decision
and gate review of spec_sharpening_2026-07-10.md (F-1..F-18 diffs pending).

VERIFIED — do not re-check (evidence in parentheses):
- Specs 00-10 + MANUAL fully audited for consistency/implementability/
  self-conformance; all known defects are F-1..F-18 in
  spec_sharpening_2026-07-10.md (BUILDLOG 2026-07-10T15:05 + 17:30).
- Persona format beats dry for defect-finding on these specs, 3/7 vs 2/7
  seeded; adopted as M-18 (BUILDLOG 2026-07-10T17:30, 18:30).
- specs_persona_story.md matches specs as of 2026-07-10; stale after any
  spec change (M-18).
- Owner decisions on record: persona adopted; heuristic-level persona/strain
  deferred to WF-5a seed experiment, judged at Phase-2 graduation
  (BUILDLOG 18:00, 18:50).

READ FOR NEXT TASK (P1.1, once unblocked): specs/02 (layout — note F-6
harness/ vs server/ naming, undecided), specs/03 (SRV-2 config), MANUAL
setup section. Nothing else needed beyond BP-8's four reads.

OPEN QUESTIONS (owner): repo location (here vs ~/heuristic-harness);
F-1..F-18 diffs approve/reject; whether to commit current amendments +
delete disposable test files (persona_test_cline.md, test_packet_*.txt,
defects_*.md).
