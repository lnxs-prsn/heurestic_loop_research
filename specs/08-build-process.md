# 08 — Build Process (fault-tolerant, multi-agent-continuable)

Status: settled · Conforms to: [01](01-invariants.md) · Requirement prefix: BP

The build must satisfy the same property as the system it produces:
**no agent's context window, uptime, or rate limit is load-bearing** (INV-7).
Any agent, cold-starting from files alone, continues as intended after a power
cut, a rate limit, or a model swap.

## Passes — the atomic unit

- **BP-1** A pass is the smallest unit of work that is independently
  completable, independently verifiable, and leaves the tree clean.
  **If it cannot be finished in one sitting, it is not one pass — split it**
  (and record the split as a spec change to [06](06-phases.md), INV-10).
- **BP-2** Every pass is declared in [06](06-phases.md) with: ID, deliverable,
  requirement IDs covered, dependencies, parallel-safety. Work not attributable
  to a declared pass ID does not happen (PH-6).
- **BP-3** Parallel work: two passes may run concurrently (different agents,
  different machines) iff no dependency path connects them AND their file
  footprints are disjoint. A pass is claimed by committing a STATUS.md change
  (`in-progress`, with agent + machine) BEFORE work starts — the commit is the
  lock; a push race loser rebases and picks another pass.

## progress/STATUS.md — where are we

- **BP-4** One line per pass: `P1.4 — done (a1b2c3d) — event logger` /
  `P1.6 — in-progress (claude, pi, 2026-07-09)` / `P1.7 — todo` /
  `P2.4 — blocked: DeepSeek subagent reliability unknown`.
  `done` MUST point at a commit hash (evidence, not claim). Phase graduation
  decisions are recorded here too, with a BUILDLOG reference.

## progress/BUILDLOG.md — what happened and why

- **BP-5 — Write-ahead rule.** An agent MUST append an *intent* entry BEFORE
  acting, and an *outcome* entry after. A power cut then leaves a readable
  "was doing X, expected to touch A,B" instead of a mystery tree.
- **BP-6** Entry template (append-only, newest last):
  ```
  ## 2026-07-09T16:40+03:00 · claude-fable-5 · pi · P1.4
  INTENT: implement event logger; will touch server/logging.py, tests/test_logging.py
  ...
  OUTCOME: done, commit a1b2c3d. Decision: one write() per line for atomicity
  (kill-test passed). Next: P1.6 or P1.5 free for parallel pickup.
  ```
  Decisions and their *reasons* are mandatory content — decisions are the
  expensive thing to reconstruct. This covers implementation-level decisions
  (how a pass was done). Owner-level decisions live in the ledger (BP-15);
  the BUILDLOG entry cites their `D-<n>` and serves as their evidence.
- **BP-7** Spec/reality conflicts are journaled here and resolved explicitly
  (INV-10), never patched around silently.

## progress/HANDOFF.md — the trust cache (don't re-derive the verified)

- **BP-14** `progress/HANDOFF.md` is a bounded snapshot (≤ ~40 lines),
  REWRITTEN — not appended — at every session end. Contents: current state in
  ≤3 lines; a "verified — do not re-check" list where every claim carries its
  evidence (commit hash, BUILDLOG timestamp, or acceptance-run reference);
  the 2–3 files the next task actually needs to read; open questions. Rules:
  a claim whose evidence predates a later change to the files it covers is
  stale and void; a fresh agent re-verifies only what its own pass touches
  plus one spot-check of the list; HANDOFF is a derived view over STATUS +
  BUILDLOG + decisions.md (INV-1 spirit — rebuildable from them), and when
  they disagree, those files win, each for what it owns: STATUS for pass
  state, BUILDLOG for what happened, decisions.md for owner decisions
  (BP-15). Purpose: no agent burns context re-confirming what a
  previous agent already confirmed with evidence.

## Records, decisions, intake — the defensive layer

Owner directive (D-9): design the handoff layer so that a later RAG/graph
layer is a *derived view* over it (INV-1), never a migration of it. The cheap
moment to give records stable IDs and typed links is before there are many.

- **BP-15 — Decision ledger.** `progress/decisions.md` is the single home of
  owner-level decisions (taste, money, autonomy, scope, hard-to-reverse),
  IDs `D-<n>`, append-only. An agent whose work triggers one writes a
  `proposed` entry (essence / analogy / impact + reversibility / what the
  architecture points at / lettered options with a default) and STOPS; only
  an explicit owner answer unblocks. A decision recorded only in BUILDLOG
  prose is not yet a decision of record — the BUILDLOG entry is its evidence.
  STATUS and HANDOFF cite decisions by `D-<n>`, never restate them.
- **BP-16 — Agent entry pointers.** `AGENTS.md` at the repo root is the one
  canonical entry file; per-tool auto-loaded files (`CLAUDE.md`, …) are thin
  pointers to it and MUST NOT carry their own rules. Its content is the start
  ritual (BP-8), nothing project-descriptive.
- **BP-17 — Record format and reference grammar.** A *record* is a markdown
  heading carrying a stable ID, immediately followed by `key: value` field
  lines, then free prose. Record types today: decisions `D-<n>`, intake
  `I-<n>`, BUILDLOG entries (ID = `BUILDLOG@<heading timestamp>`).
  References anywhere in records use one grammar: requirement IDs
  (`INV-n`, `BP-n`, `DM-n`, `M-n`, `US-n`, `WF-5a`, …), passes (`P1.4`),
  decisions (`D-n`), intake (`I-n`), sharpening findings (`F-n`), BUILDLOG
  entries (`BUILDLOG@<ts>`), commits (≥7 hex), and repo-relative paths.
  Reference fields are typed edges (`supersedes`, `superseded_by`, `affects`,
  `evidence`); every reference MUST resolve. New record types are added by
  declaration only (one entry in preflight's type registry + this
  requirement's list) — if a new type needs parser changes beyond that, the
  format leaked. `scripts/preflight.py --export` emits the derived
  nodes/edges JSON; it is never committed as truth.
- **BP-18 — Handoff truthfulness** (extends BP-14). Update triggers:
  (a) you changed state a cold session needs; (b) you FOUND a stale or false
  claim in HANDOFF or any doc it points to — record it even if you changed
  nothing else. Verify-before-repeat: every claim carried into HANDOFF is
  re-checked against its authoritative file at that moment and cites it in
  BP-17 grammar. HANDOFF's first lines carry `as_of:` (ISO ts) and
  `verified_at:` (commit hash) fields.
- **BP-19 — Machine enforcement.** `scripts/preflight.py` (stdlib) runs at
  session start and before session end. GATES (exit 1): any record fails to
  parse, a reference does not resolve, a decision's fields are inconsistent.
  WARNS (exit 0): dirty tree (listing paths — BP-9 permits journaled dirty
  state), files unregistered under BP-20, HANDOFF `as_of` older than the
  newest BUILDLOG entry, commits since `verified_at` touching specs/ or
  progress/, pending `proposed` decisions, commit hook inactive. Also GATES:
  STATUS and HANDOFF each carry one `pending_decisions:` line (comma-
  separated `D-<n>`, or `none`), and it must equal the ledger's `proposed`
  set exactly. That catches both a stale "still pending" claim about an
  answered decision (the failure BP-18 exists to prevent) and a pending
  decision nobody mentions. Prose elsewhere cites decisions but does not
  claim their status. Every
  failure prints a REMEDY. Its self-tests (`scripts/test_preflight.py`) plant
  each defect and require it be caught. `.githooks/commit-msg` enforces the
  BP-10 format; activation is D-10. Enforcers change in the same sitting as
  the rule they enforce.
- **BP-20 — Intake of outside material.** Material from other conversations
  or projects lands in `insights_from_other_conversations/` and gets an `I-<n>`
  record in its `INDEX.md` the session it is first seen. Registering is not
  adopting: adoption is a `D-<n>` decision linked via `affects:`.
- **BP-21 — Direction file.** `DIRECTION.md` at the root owns one fact: what
  this project is building right now and which inputs are under
  consideration. It carries no status and no history (STATUS, BUILDLOG and
  decisions own those); it changes only alongside a `D-<n>` entry. Rationale
  (handoff-discipline evidence from other projects): a fact with no owning
  file migrates into the handoff and regrows it indefinitely — before
  compacting anything, ask what fact has no home.

## Session protocol (every agent, every session)

- **BP-8 — Start ritual:** run `python3 scripts/preflight.py` (BP-19; a gate
  failure is fixed or journaled before anything else) → read
  [00](00-overview.md) → [01](01-invariants.md) → DIRECTION.md (BP-21) →
  STATUS.md → BUILDLOG tail (≥ last 3 entries). Then claim a pass (BP-3) and
  journal intent (BP-5). Preflight plus these five reads = complete
  onboarding; needing more context
  than the files provide is a bug in the files — fix the files. When
  HANDOFF.md (BP-14) is current, it substitutes for any wider re-reading or
  re-verification of the repo: trust its evidenced claims, re-check only what
  your pass touches.
- **BP-9 — End ritual:** tree clean (committed) or the exact dirty state
  journaled with reasons; STATUS updated; outcome entry written; new owner
  decisions in the ledger (BP-15), new outside material registered (BP-20);
  HANDOFF.md rewritten (BP-14, BP-18); preflight run, gates green;
  push if remote configured. Rate-limited mid-pass: journal state immediately — the next agent
  (or model) resumes from the journal, not from memory.

## Commits

- **BP-10** Small and frequent; each message references pass + requirement IDs
  (`P1.4: event logger (DM-13..16, INV-3)`). Git history is the third log.
  A power cut costs at most the current step.

## Flight recorder (INV-8)

- **BP-11** Location `~/.harness/flightlog/build-<machine>.log`, append-only,
  never synced, never edited, OUTSIDE the repo. Written by a session wrapper
  and/or explicit calls: session start/stop (agent, model), pass claims,
  every git command attempted + result, every error/exception encountered.
  Raw telemetry, not narrative.
- **BP-12** Recovery order when things break: STATUS → BUILDLOG → `git log`/
  `git fsck` → flight recorder. The flight recorder is the truth about events
  when the repo itself is the casualty (bad rebase, clean -fd, corrupted
  commit) — this is WHY it lives outside git.

## Verification of the process itself

- **BP-13** Acceptance for this spec: simulate a handoff — agent A journals
  intent on a pass and stops mid-way (no outcome entry); agent B (fresh
  session, start ritual only) correctly identifies and completes the pass.
  Simulate a repo disaster — delete `.git/` in a scratch clone; the flight
  recorder still tells what the last session did.

## Do NOT

- No progress tracking in agent memory, IDE state, or todo tools as sole store (INV-7).
- No BUILDLOG editing — corrections are new entries.
- No editing an answered decision — supersede it with a new `D-<n>` (BP-15).
- No derived index, embedding store, or graph file committed as truth — they
  are rebuilt from records on demand (BP-17, INV-1; vectors still gated by 01).
- No pass work without a STATUS claim commit (BP-3) when more than one agent
  may be active.
