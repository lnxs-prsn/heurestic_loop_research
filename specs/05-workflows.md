# 05 — Workflows (human + librarian operations)

Status: settled · Conforms to: [01](01-invariants.md) · Requirement prefix: WF

## WF-1 — Review & promotion (the gate's core loop)

1. Open `heuristics/staging/` (or `git status` — staged files are untracked/new).
2. For each proposal: read it; check DM validity (`scripts/lint.py` runs the
   validator + cue-overlap check); then one of:
   - **promote**: `git mv` into `heuristics/`, adjusting id on collision (DM-3), commit;
   - **edit-then-promote**: fix, then as above (the edit is signal — note it);
   - **reject**: delete the file, one-line reason in the commit message.
3. For `update-*` proposals: `diff` against the live file; apply or reject.
- Promotion commits SHOULD note unedited/edited/rejected — this is the
  graduation evidence for Phase 4 ([06](06-phases.md)).

## WF-2 — Cadence

Review staging weekly or when ≥5 proposals accumulate, whichever first.
Ten minutes; if it regularly takes longer, proposal volume is too high (INV-9).

## WF-3 — Batch distillation (safety net)

`scripts/distill.py`: reads `lesson` events and `hurt`/`unclear` outcomes since
its last run (tracked in the script's state file under `~/.harness/`), clusters
them, and drafts candidate heuristic files into staging via a model call
(configurable endpoint; DeepSeek by default, any OpenAI-compatible URL).
Offline mode: `--manual` prints the prompt for pasting anywhere. Runs weekly or
on demand. It catches what in-the-moment proposals (AGT-8) missed.

## WF-4 — Librarian session (capable agent, e.g. Claude)

Inputs: full logs, live library, staging, kernel. Tasks, in order:
1. Distill unprocessed lessons into proposals (as WF-3, but with judgment).
2. Dedupe/merge near-identical entries (propose `supersedes` chains, INV-2).
3. Sharpen cues that never match or over-match (evidence: retrieval events).
4. Propose deprecations (stale tech, superseded practice, `hurt`-dominant stats).
5. Route misplaced knowledge: user-facts posing as techniques → `kind: user-fact`;
   kernel lines that turn out to have discrete cues → demote to library entries;
   project-scoped lessons recurring across ≥2 projects/machines → generalize scope.
6. Write `staging/librarian-report-<date>.md`: what was done and why, plus
   library health notes (entry count, orphaned cues, no-outcome rate per DM-17).
- **WF-4a** All librarian output lands in staging (INV-4) — the librarian is a
  proposer with better taste, not a second gate.
- **WF-4b** Cadence: monthly, or when staging review (WF-1) starts feeling noisy.

## WF-5 — Seeding (one-time, Phase 1 pass P1.9)

The librarian authors the initial 10–20 heuristics from: (a) direct inspection
of the machine and repos, (b) known failure patterns of the target model as
`kind: model-patch`, (c) the owner's recognition — drafts are reviewed by
thumb-through ("yes / no / almost"), NOT by asking the owner to enumerate pain
points (tacit-knowledge principle, [00](00-overview.md)). Kernel v1 is drafted
the same way (≤15 lines, DM-10).

- **WF-5a — Format experiment embedded in the seed (no new machinery).** The
  seed library carries two comparisons the normal logs will answer as a side
  effect of use: (a) *personification* — 2–4 seed entries get persona-voiced
  bodies ("I wince at gcc in build logs…"), the rest stay dry; `outcome`
  events per entry accumulate the comparison; (b) *stereotyping* — every seed
  entry includes its archetype/strain as an ordinary tag (e.g.
  `tags: [frugal, …]`), which joins the BM25 surface (TOOL-2); retrieval
  events (DM-14, all candidates with scores) show whether strain tokens ever
  contribute to matches or the cues do all the work. Librarian sessions
  (WF-4 item 6) report on both; judged at Phase-2 graduation. Existing
  schema only — no new frontmatter fields (DM Do-NOT-build stands).

## WF-6 — Multi-machine sync

- New machine: clone repo, install server (pip), write `~/.harness/config.yaml`
  with its `machine_name`, register MCP + adapter snippets. Done.
- Daily use: `auto_pull` on server start covers inbound; push after gate
  sessions (WF-1) and periodically (`scripts/sync.sh` = pull --ff-only, add
  logs+staging, commit, push). Logs never conflict (per-machine files, INV-3).
- Workplace machine: `log_sync: false` (DM-18) — consumes the library fully,
  contributes no logs. Never author kernel/heuristic content containing
  employer-confidential specifics from it (see [07](07-future.md) §privacy).

## WF-7 — Recovery drill

State is reconstructable in this order: STATUS.md → BUILDLOG tail → git log →
flight recorder (`~/.harness/flightlog/`). If repo and flight recorder disagree,
the flight recorder is the raw truth about *events*; the repo is the truth about
*content*. Rebuild derived artifacts from files (INV-1); never hand-edit logs.

## WF-8 — Baseline week (before go-live)

Run the full stack with `serve_mode: log_only` for ~1 week of normal work.
This records what *would* have been retrieved while changing nothing —
the permanent control group. Flip to `normal` afterwards. Skipping this is
irreversible (expensive-later item #3).

## Acceptance criteria

- A dry-run WF-1 session on synthetic staging files completes with lint passing
  and correct git history (promote/edit/reject each exercised).
- WF-3 in `--manual` mode produces a well-formed prompt from synthetic lessons.
- A second machine reaches working state via WF-6 in ≤ 30 minutes.

## Do NOT build

- No auto-promotion of any kind before Phase 4 (INV-4).
- No dashboard/web UI — the terminal, git, and markdown are the interface.
- No scheduled unattended distillation with API spend before Phase 3 (manual
  or explicit runs only until value is proven).
