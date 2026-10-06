# Agent entry point — read before doing anything in this repo

Canonical entry file (specs/08 BP-16). Tool-specific files (CLAUDE.md, …)
only point here.

1. Run `python3 scripts/preflight.py`. Gate failure → fix it or journal it in
   progress/BUILDLOG.md before any other work. Read its WARN lines: they list
   pending owner decisions, unregistered files, and a stale handoff.
2. Read progress/HANDOFF.md and do its FIRST ACT before replying. Your first
   reply must match its EXPECTED OPENING (BP-22). Its DONE claims are the
   trust cache: no re-verifying unless your work touches them (BP-14,
   BP-18).
3. Start ritual per specs/08 BP-8: specs/00 → specs/01 → DIRECTION.md →
   progress/STATUS.md → BUILDLOG tail (≥ 3 entries).
4. Journal INTENT in BUILDLOG before acting, OUTCOME after (BP-5). Read
   every timestamp from `date`; never estimate it (BP-6).
5. Owner-level decision (taste, money, autonomy, scope, hard-to-reverse)?
   Write a `proposed` entry in progress/decisions.md and STOP (BP-15).
6. New files from outside (other conversations/projects)? Register them in
   insights_from_other_conversations/INDEX.md (BP-20). Registering ≠ adopting.
7. Found a stale or false claim anywhere? Record it in HANDOFF, even if you
   changed nothing else (BP-18).
8. Git: explicit staging only (`git add <paths>`, never `-A`/`.`/`commit -a`);
   commit format per BP-10. COMMIT AFTER EVERY CHANGE to any file, handoff
   included, without asking (D-12). Push only when the owner says so.
9. End ritual per BP-9, finishing with preflight green.

**Human coherence (`coherence/`; rules in
incubating/human-coherence-intent-anchoring/kit/SPEC.md, on trial here).**
The owner is not a file you can re-read; keep them in step with the intent.
- Everything you put to the owner carries `stage`, `impact`
  (changes-intent / advances / route-only / untouched) and a one-line `why`
  in plain words, biggest impact first (HC-12..HC-15).
- Before asking the owner anything, check whether their earlier answers
  already decide it; if so, apply it and say which answer settled it (HC-29).
- Watch for coherence signals and offer a re-entry; never force one (HC-28).
- Never present a derived intent as confirmed (HC-7). Current intent:
  coherence/intent.md INT-4, confirmed 2026-10-06 (RE-1, SIT-1).
- Involve the owner only when evidence shows a significant intent change or
  a road deviated from the current state to the intent; otherwise derive,
  apply the owner's earlier answers, and report (RE-1 trial outcome).
