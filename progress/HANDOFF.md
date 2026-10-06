# HANDOFF (BP-14, BP-18) — rewritten each session end
as_of: 2026-10-06T14:45+03:00
verified_at: 3bbbe36
written_by: claude-opus-5-5 · pi
pending_decisions: D-6, D-8, D-10

STATE: project resumed after the Jul–Oct hiatus. Owner re-entry done
(coherence/reentry/RE-1.md): intent INT-4 confirmed (SIT-1) — kept, grown by
additions, road unchanged. Next stop on the road: D-6 design fixes, then
P1.1 in the dedicated repo (D-5). Implementation NOT started. Work of
2026-10-05/06 committed on owner's order (10ee803, 46f2708, + re-entry
commit 3bbbe36); not pushed. innovations/ left untracked (D-8).

VERIFIED — do not re-check (evidence in parentheses):
- Current intent: heuristics outside the model, grown in layers (individual
  heuristics → stacks/personas → learning → rule-making → person); now =
  layer 1, the July Harness design (coherence/intent.md INT-4; D-7).
- Hiatus material I-1..I-5 read in full, processed; nothing competes with
  the specs; it describes later layers (RE-1; D-7). I-6 (post-hiatus
  landscape survey) registered and HELD by owner: do not process yet.
- Two additions for layer-1 design work: leave room in the file format for
  stacks, personas, run traces, scope; irrelevant-information management
  starts in layer 1 (RE-1 §Drift check).
- Handoff system BP-15..BP-21 built, preflight 17 self-tests green (D-9,
  D-11). Agent-loop planning: no decision needed (RE-1 §Resolutions).
- Repo location decided (D-5); target dir not yet created. F-1..F-18 exist
  with diffs, none applied (spec_sharpening_2026-07-10.md; D-6).

OWNER-SIDE PATTERN: incubating/human-coherence-intent-anchoring/ (PATTERN +
kit). First trial complete; its nine findings are recorded in RE-1 §Trial
outcome and PATTERN.md "Proven in" but NOT yet folded into kit/SPEC.md
(banner says so). Major: HC-24 restate → "agent drafts, owner confirms";
involve the owner only on significant intent change or road deviation.

READ FOR NEXT TASK: run scripts/preflight.py. Then either (a) fold the
trial findings into kit/SPEC.md (+ OWNER_GUIDE, design record untouched), or
(b) D-6 with the owner: spec_sharpening_2026-07-10.md, specs/02, specs/03,
keeping INT-4's layer-1 additions in view. Owner chooses.

OPEN QUESTIONS (owner): the pending_decisions line above; license (FUT-1)
not yet a ledger entry; whether to push.
