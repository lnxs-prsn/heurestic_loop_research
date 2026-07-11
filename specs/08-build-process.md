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
  expensive thing to reconstruct.
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
  BUILDLOG (INV-1 spirit — rebuildable from them), and when they disagree,
  STATUS/BUILDLOG win. Purpose: no agent burns context re-confirming what a
  previous agent already confirmed with evidence.

## Session protocol (every agent, every session)

- **BP-8 — Start ritual:** read [00](00-overview.md) → [01](01-invariants.md) →
  STATUS.md → BUILDLOG tail (≥ last 3 entries). Then claim a pass (BP-3) and
  journal intent (BP-5). Four reads = complete onboarding; needing more context
  than the files provide is a bug in the files — fix the files. When
  HANDOFF.md (BP-14) is current, it substitutes for any wider re-reading or
  re-verification of the repo: trust its evidenced claims, re-check only what
  your pass touches.
- **BP-9 — End ritual:** tree clean (committed) or the exact dirty state
  journaled with reasons; STATUS updated; outcome entry written; HANDOFF.md
  rewritten (BP-14); push if remote configured. Rate-limited mid-pass: journal state immediately — the next agent
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
- No pass work without a STATUS claim commit (BP-3) when more than one agent
  may be active.
