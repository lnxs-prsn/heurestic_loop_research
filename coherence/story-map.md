# Story map — heuristic loop research
map_for: INT-4

Rules: incubating/human-coherence-intent-anchoring/kit/SPEC.md HC-9..HC-11.
Stages derived 2026-10-05 from the project's own phase plan and records;
the owner confirms at re-entry. States are as of the pause (2026-07-11);
nothing inside the project changed during the hiatus, so they are also
today's states.

Carried to INT-4 at RE-1 (2026-10-06): used as the road in the drift check;
the owner accepted "road unchanged". Stages stay `derived` (not separately
confirmed). Layers 2–5 of INT-4 lie beyond ST-6 and are not yet staged.

---

## ST-1 — Idea collected
order: 1
contributes: the premise and the first architectures the intent came from
state: grasped
evidence: idea/deepseek.md, idea/kimi.md, idea/gpt.md, idea/manus.md
alternatives: none
status: derived

## ST-2 — Design written down (specs + owner manual)
order: 2
contributes: turns the intent into buildable, checkable requirements
state: grasped
evidence: specs/00-overview.md, MANUAL.md, specs/10-user-stories.md, 6a20659
alternatives: none
status: derived

## ST-3 — Design checked and corrected
order: 3
contributes: removes flaws before code makes them expensive
state: partial
evidence: spec_sharpening_2026-07-10.md, D-6
alternatives: apply all 18 fixes; apply the 6 major ones first; review one by one (D-6)
status: derived

18 flaws found; none applied. The persona audit method (D-2) came out of
this stage.

## ST-4 — First working version: agents can look up heuristics
order: 4
contributes: the library exists and agents actually use it (Phase 1)
state: open
evidence: specs/06-phases.md, progress/STATUS.md
alternatives: build here vs dedicated repo (decided: dedicated repo, D-5)
status: derived

Not started. Blocked on ST-3.

## ST-5 — The library grows from experience
order: 5
contributes: agents propose heuristics from real tasks; the owner promotes them (Phases 2–3)
state: open
evidence: specs/06-phases.md
alternatives: persona-shaped heuristics as an experiment (D-3)
status: derived

## ST-6 — The owner hands over work the logs show is routine
order: 6
contributes: autonomy earned from evidence (Phases 4–5)
state: open
evidence: specs/06-phases.md
alternatives: none
status: derived
