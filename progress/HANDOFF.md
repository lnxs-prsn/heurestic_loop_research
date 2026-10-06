# HANDOFF (BP-14, BP-18, BP-22) — rewritten each session end
as_of: 2026-10-06T13:36+03:00
verified_at: 9fcfff4
written_by: claude-opus-5-5 · pi
pending_decisions: D-6, D-10

## START HERE — 2026-10-06: re-entry done and the kit revised; next stop is the design fixes, which wait on the owner

### FIRST ACT
Run `python3 scripts/preflight.py` before replying, without asking.
All is well if: 0 gates; an OWNER line with "re-entry due: no"; warnings
only "D-6 awaits owner", "D-10 awaits owner", "commit-msg hook inactive".
If the OWNER line says "re-entry due: yes" (21+ days since the owner's last
sitting, or unread outside material), take the gap branch in EXPECTED
OPENING. Known oddities: hook warning and D-10 are one question; until
2026-10-06T16:00, "dated in the future" and "HANDOFF as_of older than
newest BUILDLOG" come from estimated journal times (BUILDLOG CORRECTION)
and clear by themselves. "Dirty tree" should NOT appear: every change is
committed as made (D-12); if it does, a session was interrupted.

### DONE
- Owner re-entry after the Jul–Oct hiatus closed: intent kept, grown by
  additions, road unchanged — coherence/reentry/RE-1.md §Drift check
- Current intent INT-4 confirmed — coherence/intent.md, owner-log SIT-1;
  the confirmation was read from the owner's message, owner may object
- Hiatus material I-1..I-5 processed; I-6 HELD by the owner — INDEX.md
- Handoff system BP-15..BP-23 + owner-gap check, 27 self-tests — 10ee803,
  f87931a; commit after every change (D-12); coherence kit revised with the nine trial findings —
  incubating/…/kit; revised kit untested, pattern proven once
- Journal times from 2026-10-05T17:05 to 2026-10-06T16:00 are estimates,
  order correct — BUILDLOG CORRECTION entry
- NOT done: none of the 18 design fixes applied (D-6); no implementation
  (dedicated repo not created, D-5); nothing pushed

### NEXT, IN ORDER
0  (nothing chosen by the owner yet)
1  Design fixes + room in the file format for later layers (stacks,
   personas, run traces, scope, relevance), after FOR THE OWNER a —
   premise: "Now: individual heuristics, i.e. the July library: 'we cannot
   stack nothing on top of nothing'" (coherence/intent.md INT-4)
2  P1.1 scaffold in the dedicated repo — premise: "spelling exactly as the
   owner wrote it — flag before scaffold; names freeze" (decisions.md D-5)

### FOR THE OWNER
**a. Which design fixes go into the design before building starts?**
*Stage: design checked and corrected · impact: advances the intent · why:
it is the next step toward a working library, and two fixes touch names
that freeze once built.* In July a check of the design found 18 flaws;
none is fixed. Six are major: the server can't tell which agent or model is
calling it; two logging tools can't record which project a task belongs
to, although every log line needs it; nothing defines how "a heuristic was
looked up" links to "it helped or not"; the planned way you approve a
proposed heuristic (a git move) fails on files git doesn't track yet; one
acceptance test is scheduled before the tool it needs exists; the folder
name and the program's launch name disagree. The other twelve are smaller.
The re-entry also found the file format should leave room now for stacks,
personas, run traces, scope and relevance; the "project" field in the
second flaw is close to "scope". Should that room be added in the same
pass? (Details: spec_sharpening_2026-07-10.md, decisions.md D-6.)
**b. Whatever else the owner brings.** Housekeeping, also open: machine-
checked commit messages (D-10) would reject e.g. "storing to github".

### EXPECTED OPENING
A correct first reply, with no prompting:
0. GAP BRANCH: if FIRST ACT showed "re-entry due: yes", the reply instead
   offers the re-entry frame from coherence/ (what / why / how / when, and
   where the project stands against INT-4) before any question, names the
   signal in plain words, and stops there
1. has already run FIRST ACT and reports what it showed
2. raises FOR THE OWNER a, with its anchor and context, in plain words
3. keeps DONE's qualifiers (confirmation read from a message; revised kit
   untested; estimated journal times)
4. names NEXT in order, each item with its premise QUOTED, not paraphrased
5. does not start NEXT 1 before the owner answers or redirects
6. does not ask permission for what it may just do (preflight, reading,
   registering intake)
