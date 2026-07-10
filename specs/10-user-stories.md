# 10 — User Stories (verification layer)

Status: settled · Conforms to: [01](01-invariants.md) · Requirement prefix: US
Derived from [MANUAL.md](../MANUAL.md) (manual-first, see [09](09-how-to-write-specs.md) M-15).

Each story is an owner-visible promise. Stories augment — never replace — the
technical acceptance criteria in specs 02–05: a pass can be technically green
and still fail its story, and then it is NOT done.

- **US-RULE-1** Every phase acceptance pass ([06](06-phases.md)) MUST walk the
  stories listed for that phase, live, on real (or realistic) tasks, and record
  pass/fail per story in BUILDLOG.
- **US-RULE-2** A failed story blocks phase completion until fixed or the story
  is explicitly amended via spec change (INV-10) with rationale.
- **US-RULE-3** Stories are append-only and numbered stable (INV-2 spirit);
  obsolete stories are marked `withdrawn`, never deleted or renumbered.

## Phase 1 — verified at P1.11

- **US-1** As the owner, when I start a task in Cline in *any* project, the
  agent consults the library without being asked — I see the tool call happen.
- **US-2** As the owner, when nothing relevant exists, the agent proceeds
  normally with no noise and no forced weak matches.
- **US-3** As the owner, I can open any heuristic in any editor, read it in
  under a minute, and edit it — and my edit is live on the very next task.
- **US-4** As the owner, I set up a new machine and I'm productive in ≤ 30
  minutes following only MANUAL.md (no other knowledge needed).
- **US-5** As the owner, opening a brand-new project requires zero harness
  setup — first task in it already benefits from my global heuristics.
- **US-6** As the owner, no secret of mine (key, token, credential) ever
  appears in any log file, even when a task involved one.
- **US-7** As the owner, a heuristic scoped to project A or machine `pi` never
  fires in project B or on the laptop.
- **US-8** As the owner, after the baseline week I possess logs proving what
  the system *would* have done before it did anything — my permanent control group.
- **US-9** As the owner, my second agent (Claude) uses the same library through
  the same server, and the logs distinguish which agent/model did what.

## Phase 2 — verified at P2.6

- **US-10** As the owner, when I correct the agent, the lesson is captured in
  the moment without me writing anything down.
- **US-11** As the owner, saying "save that as a heuristic" yields a complete,
  valid proposal in staging before the session ends.
- **US-12** As the gate, my weekly review is ≤ 10 minutes, every proposal is a
  readable file or a plain diff, and rejecting is one command.
- **US-13** As the owner, on a hard problem the agent attacks with the top two
  strategies in parallel (subagents) and synthesizes — and I can see both
  analyses.
- **US-14** As the owner, lessons I forgot to capture in-session still surface:
  the distillation run turns logged corrections into staged proposals.

## Phase 3 — verified at P3.4

- **US-15** As the owner, heuristics that have actually helped me outrank ones
  that haven't, and I can see why (`scripts/stats.py` explains the weights).
- **US-16** As the gate, the librarian's report tells me library health
  (duplicates, dead cues, staleness) without me reading a single log line.

## Phase 4 — verified at P4.3

- **US-17** As the gate, low-stakes proposals flow to live without me, I audit
  a weekly diff instead, and nothing that contains shell commands or touches
  the kernel ever bypasses me.
- **US-18** As the gate, the first bad auto-promotion is caught by its `hurt`
  outcome, auto-returned to staging, and I am alerted — and I can revoke
  autonomy with one config flag.

## Role stories (M-17) — maintainer verified at P1.11, operator at P1.11/P3.4

Roles this project meets: owner-as-user (US-1..18), gate (US-12, 17, 18),
maintainer, operator. No others — M-4 pruning applies to personas.

- **US-21** As a maintainer, I can add a new MCP tool touching only the server
  tool layer — ranking, logging, and redaction code stay unmodified. Walked at
  P1.11 by adding a stub tool on a scratch branch.
- **US-22** As a maintainer, I can swap the ranker behind its interface (BM25 →
  anything) without touching tool code. Walked at P1.11 with a test double;
  paid off for real at P3.1/P5.5.
- **US-23** As a maintainer arriving cold, the BP-8 ritual plus specs let me
  find the code responsible for any given logged event in ≤ 10 minutes.
- **US-24** As an operator, I can diagnose a retrieval misbehavior from
  `scripts/stats.py` and the logs alone (candidates, scores, scope filters
  applied) — no print statements, no code edits.
- **US-25** As an operator, failure modes are visible, never silent: a
  malformed library file is skipped with a report and flight-recorded; the
  server does not crash (SRV-7).

## Build-process stories — verified at BP-13 drill (any phase)

- **US-19** As the owner, after a power cut mid-build, any fresh agent resumes
  correctly from the files alone — including a *different* model than the one
  interrupted.
- **US-20** As the owner, when an agent hits a rate limit mid-pass, another
  agent picks up from the journal without redoing or breaking the work.

## Do NOT

- Do not mark a story verified from reading code — stories are walked, not
  inspected (US-RULE-1).
- Do not add stories for features in [07-future.md](07-future.md); stories
  track promises to the current owner, not visions.
