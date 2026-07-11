# I am the Heuristic Harness — my life, told honestly (2026-07-10)

I am `specs/00-10` plus `MANUAL.md`. I am a memory of lessons for AI coding
agents: I keep what the owner already taught once, and I hand it back at the
moment it matters. Below I narrate my own pipeline as if I were running it,
and I stop at every place where I don't actually know what I'm supposed to do.
Markers like **[H-1]** point into my issue register at the bottom. I quote my
own requirement IDs so every stumble is checkable against my text, not against
vibes. (My register aligns with `spec_sharpening_2026-07-10.md`, finding for
finding — the dry audit and I are telling the same story in two voices.)

---

## Scene 1: A task begins

The owner types a task into Cline. My adapter rules fire before anything else:
the agent MUST call `find_heuristics(task_summary, project)` at task start
(AGT-3), and the summary MUST be one disciplined line — `<action> <object>
<tech>`, never `"fix bug"` (AGT-4). I am strict about this line because it is
the join key of my entire existence; my own text says a lazy summary poisons
retrieval and analytics *permanently*. To justify that severity I cite
"(expensive-later item #2)" — and then I reach for the numbered list I'm
citing and find it isn't in any of my files. It lived in a planning
conversation I can no longer attend. I cite evidence I don't carry. **[H-9]**

The call reaches my server: one Python process over stdio, no port, no daemon
(SRV-1). I re-read my library from disk — tens of files, correctness over
micro-performance (SRV-4) — filter out anything scoped to a different project,
machine, or model, and anything deprecated (TOOL-5), then rank what survives
by BM25 over cues + tags + title (TOOL-2). I return at most `k` results, and
below a minimum score I return none at all, because an honest "nothing
matched" beats a forced weak match (TOOL-3). I am proud of that honesty. But —
*which* minimum? My config file has five keys (SRV-2): path, machine, sync,
pull, serve mode. No threshold among them, and no default in my text. I hold a
strong opinion about silence and I have nowhere to keep the number that
triggers it. My implementer will invent one; my operator won't find it.
**[H-5]**

If something matches, the agent fetches the full body (`get_heuristic`,
TOOL-6) and applies it. The owner sees the tool call happen (US-1); when
nothing matches, no noise (US-2); a brand-new project needs zero setup and
already benefits (US-5); a heuristic scoped to project A never fires in
project B (US-7). The kernel — my ≤15 lines of cue-less facts about the owner
(DM-10) — was already in context from message one, injected by the adapter,
never retrieved (AGT-9).

## Scene 2: What I write down, and the pockets I pat

Before returning anything, I log (SRV-6, INV-3). My `retrieval` event records
ALL candidates with scores, not just winners — future phases feed on the
losers too (DM-14). Every string passes redaction *before* it is persisted:
key-shaped tokens, PEM blocks, credential assignments become `«redacted:kind»`
(INV-5, SRV-6). No secret of the owner's ever reaches a synced file (US-6);
git history is forever, which is exactly why I redact at write time, not sync
time.

Now the part I'm ashamed of. Every event I write MUST carry the common fields:
`machine`, `agent`, `model`, `project` — unknown values written as `"unknown"`,
never omitted (DM-13). Machine I know from my config. Agent and model… I pat
my pockets. No tool signature carries them. My config file can't hold them —
Cline and Claude Code launch me from the *same* `~/.harness/config.yaml`
(SRV-2), so one static value would lie for the other. My spec waves toward
"model from agent context per AGT-2" (TOOL-5) — and AGT-2 says adapters "state
the agent's identity fields" — but a rules snippet is words shown to an agent;
it is not a channel into my process. I am *required* to say who is calling,
my model-patch filtering (DM-5, TOOL-5) *depends* on knowing, and I have no
way to know. As written, I stamp `"unknown"` on everything and my per-model
memory is stillborn. **[H-1]**

`project` is worse in a smaller way. My retrieval tool takes it as a parameter
precisely because "the server cannot infer it" (TOOL-1). Then the task ends
and the agent calls `log_outcome(heuristic_id, outcome, task_summary, notes)`
(TOOL-7) — count the parameters. The agent knows the project; my signature
gives it no slot to tell me. Same for `log_lesson` (TOOL-8). So my outcome and
lesson events — the evidence base for every trust decision I will ever make —
say `project: "unknown"` forever, and my librarian's instruction to generalize
lessons "recurring across ≥2 projects" (WF-4 item 5) reads a field I never
filled. **[H-2]**

And when the statistics come due: a `retrieval` with no *matching* `outcome`
within 7 days is counted as "no outcome", its own bucket, never silently
dropped — my survivorship-bias rule, and a good one (DM-17). Matching. By
what? Heuristic id? Task summary? Nearest in time? I never say. Two honest
implementers of `scripts/stats.py` will produce two different truths from the
same log, and neither will have violated me. **[H-3]**

## Scene 3: The owner corrects the agent

Mid-task, the owner says "no — on this machine, check piwheels first." The
agent calls `log_lesson` immediately, while the context is richest (AGT-7);
nothing is asked of the owner (US-10). That lesson is raw ore. It becomes a
heuristic in one of two ways: in the moment — **[Phase 2]** the owner says
"save that as a heuristic" and the agent calls `propose_heuristic` (AGT-8,
TOOL-9), which writes a complete, valid file — or later, when distillation
(WF-3) or a librarian session (WF-4) mines the logs for what was missed
(US-14).

Wherever it comes from, the proposal lands in exactly one place:
`heuristics/staging/` — my airlock. Machine-authored content goes there and
nowhere else, no exception for "obviously correct" (INV-4). I notice one small
lie in my own paperwork as the file is written: `propose_heuristic` receives
`project=""` as its default, and my file format wants `project: null` (DM-6).
Empty string, null — someone maps one to the other; nobody wrote down that
they should. A linter and a proposer can disagree about it without either
being wrong. **[H-6]**

## Scene 4: The gate's ten minutes

Weekly, or at five proposals, whichever first (WF-2), the owner opens staging.
My manual promises this is ten minutes: read each proposal, lint it, then
promote, edit-then-promote, or reject with a one-line reason (WF-1). Scarcity
keeps the gate honest — proposals rare enough to actually be read; detected
rubber-stamping means *reduce volume*, never *widen autonomy* (INV-9, US-12).

I walk the owner through their very first review. `ls heuristics/staging/` —
there it is. Read it — good. Now promote: my manual says `git mv
heuristics/staging/h-foo.md heuristics/`. The shell answers:
*fatal: not under version control*. Of course — my server wrote that file; no
one has committed it; `git mv` refuses untracked sources. My owner's first
review session, the ritual my whole trust ladder is built on, dies at its
second command, and both WF-1 and my MANUAL gave that command with a straight
face. **[H-4]**

## Scene 5: The librarian visits

Monthly-ish, a capable agent opens me whole: logs, library, staging, kernel
(WF-4). It distills unprocessed lessons, dedupes near-identicals into
`supersedes` chains (never renames — ids are permanent, INV-2), sharpens cues
that never fire or over-fire, proposes deprecations, and files a report the
owner can read instead of reading logs (US-16). Everything it writes lands in
staging — the librarian is a proposer with better taste, not a second gate
(WF-4a). It also authored my first 10–20 entries by inspecting the machines
and drafting for the owner's thumb-through — "yes / no / almost" — because the
owner recognizes expertise on sight but cannot enumerate it on request; that
asymmetry is my founding philosophy (WF-5, 00-overview).

## Scene 6: Growing up, and the witness who isn't born yet

I earn autonomy on a ladder, never a calendar: each phase automates only what
the logs prove the human was rubber-stamping (06, M-6). Phase acceptance is
not an impression — my user stories are walked live, on real tasks, pass/fail
recorded in BUILDLOG; a technically-green pass that fails its story is not
done (US-RULE-1, specs/10).

At P1.11 I walk my Phase-1 stories: US-1..9, and my role stories US-21..25.
US-24 promises my operator can diagnose retrieval misbehavior "from
`scripts/stats.py` and the logs alone." I check my own ledger:
`scripts/stats.py` is delivered by pass P2.5 — a phase *after* the walk. I
have scheduled a witness who hasn't been born. **[H-7]**

And one more thing I notice about my own law book. PH-6, my standing rule:
"Any work not attributable to a pass ID in this file is out of scope." I
admire its severity — "while I'm at it" is how specs die. Then I look at my
own BUILDLOG: five entries of spec amendments, and the sharpening pass that
audited me — none carries a pass ID, because spec work has no pass. Read
literally, I forbid my own maintenance, and the BP-13 disaster drill that
proves my build process (US-19, US-20) is likewise assigned to no pass at all.
My constitution's INV-10 permits what my phase file forbids. **[H-8]**

## Scene 7: How I survive the people who build me

I am built the way I work (M-14). No agent's context window, uptime, or rate
limit is load-bearing (INV-7, BP-8): any fresh agent reads four files —
overview, constitution, STATUS, BUILDLOG tail — and continues correctly after
a power cut, a rate limit, or a model swap (US-19, US-20). Intent is journaled
*before* acting, outcome after (BP-5), so a crash leaves a readable "was doing
X" instead of a mystery tree. And one record lives outside me entirely: the
flight recorder in `~/.harness/flightlog/`, never synced, never edited,
because the record of failures must not live inside the thing that fails
(INV-8). When my repo itself is the casualty, the flight recorder still
remembers.

## The promises I make (my story layer, in one breath)

To my owner: retrieval without asking (US-1), silence over noise (US-2),
every file human-readable and editable with edits live next task (US-3), a new
machine productive in ≤30 minutes from the manual alone (US-4), new projects
free (US-5), secrets never persisted (US-6), scopes respected (US-7), a
permanent control-group week before I change anything (US-8, WF-8), and every
agent sharing one library with attributed logs (US-9). To my gate: ten honest
minutes (US-12), and — much later, if earned — low-stakes promotions flowing
without them but never anything with shell commands or kernel reach (US-17),
with the first bad auto-promotion caught, reverted, and revocable by one flag
(US-18). To my maintainer: seams — a new tool without touching ranking
(US-21), a swapped ranker without touching tools (US-22), any logged event
traced to code in ≤10 minutes cold (US-23). To my operator: diagnosis from
logs alone (US-24 — see [H-7]), failures visible, never silent (US-25, SRV-7).
Stories are append-only, numbered stable, walked live, never verified by
reading code (US-RULE-1..3).

---

## My issue register

Every marker above, mapped to the dry audit (`spec_sharpening_2026-07-10.md`):

- **[H-1]** = F-1 — I must log `agent`/`model` (DM-13) and filter by model
  (TOOL-5), but no parameter, config field, or adapter mechanism delivers them
  to my process. Proposed fix: identity env vars in each host's MCP registration.
- **[H-2]** = F-2 — `log_outcome`/`log_lesson` (TOOL-7/8) have no `project`
  slot; the mandatory field (DM-13) logs `"unknown"` forever. Fix: optional param.
- **[H-3]** = F-3 — DM-17's "matching outcome" is undefined; stats are
  unimplementable-as-specified. Fix: explicit join rule.
- **[H-4]** = F-4 — WF-1 and MANUAL promote with `git mv`, which fails on
  untracked staging files. Fix: `mv` + `git add`.
- **[H-5]** = F-9 — TOOL-3's minimum score has no home and no default. Fix:
  `min_score` config key, tuned from baseline-week data.
- **[H-6]** = F-13 — TOOL-9's `""` defaults vs frontmatter `null` (DM-6):
  unwritten mapping. Fix: one sentence.
- **[H-7]** = F-5 — US-24 walked at P1.11 needs `scripts/stats.py` (P2.5).
  Fix: move its walk to P2.6.
- **[H-8]** = F-8 — PH-6 read literally forbids spec work and the BP-13 drill.
  Fix: two journaled standing exceptions.
- **[H-9]** = F-7 — "expensive-later item #2/#3" cite a list absent from my
  files (violates BP-8's own standard). Fix: replace with self-contained M-12
  references.

*(The dry audit found six further findings — F-6, F-10, F-11, F-12, F-14,
F-15 — that live in files this story only brushes past; they are not
re-narrated here.)*

---

*Written per the spirit of M-15: if a behavior is hard to narrate to its user,
the design is wrong — fix the spec before the code. Where this story
disagrees with specs/00-10, one of the two is wrong; journal it (INV-10) and
change one explicitly. This file is untracked working material for the gate,
not a spec.*
