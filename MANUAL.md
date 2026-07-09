# Heuristic Harness — User Manual

**Read this if you are the owner/operator.** (Agents: your entry point is
[specs/00-overview.md](specs/00-overview.md), not this file.)

> **Manual-first notice:** this manual was written from the specs *before* the
> implementation (see [specs/09](specs/09-how-to-write-specs.md), M-15). It
> describes the system as it must behave when built. Where built behavior
> disagrees with this manual, one of the two is wrong — journal it in
> BUILDLOG and fix one explicitly. Features not available until later phases
> are tagged like **[Phase 2]**.

## What this is, in one paragraph

A memory of lessons for your AI coding agents. Every lesson lives as a small
markdown file (a *heuristic*) with cue phrases; when an agent starts a task,
it asks the local server "anything relevant?", gets the matching lessons, and
applies them. When you correct an agent, that correction can become a new
heuristic — but nothing enters the live library without passing through your
hands. Over months, your agents stop repeating mistakes you've already fixed
once, in every project, on every machine.

## Setting up a machine (once per machine, ~15–30 min)

1. Clone the repo: `git clone <your-remote> ~/heuristic-harness`
2. Install: `pip install -e ~/heuristic-harness` (installs `mcp`, `rank-bm25`, `pyyaml`)
3. Create `~/.harness/config.yaml`:
   ```yaml
   repo_path: /home/you/heuristic-harness
   machine_name: laptop          # unique per machine
   log_sync: true                # false on a workplace machine — see below
   auto_pull: true
   serve_mode: normal            # log_only during the baseline week
   ```
4. Register the MCP server:
   - **Cline**: MCP settings → add stdio server `heuristics` → command `python -m harness.server`. Then copy `adapters/cline-rules.md` into Cline's **global** rules directory.
   - **Claude Code**: `claude mcp add --scope user heuristics -- python -m harness.server`. Then append `adapters/claude-md-snippet.md` to `~/.claude/CLAUDE.md`.
5. Open any project and start a task. You're done — **new projects never need setup.**

**Workplace machine:** set `log_sync: false`. That machine gets the full
library but its logs never leave it. Don't author heuristics containing
employer-confidential specifics from it.

## Daily use — what you'll see

You mostly do nothing. At task start the agent calls `find_heuristics` (you'll
see the tool call in Cline); if something matches, it fetches and applies it.
It checks again before risky moments: adding a dependency, picking an
architecture, running destructive commands, declaring done.

Your two verbal habits, both optional but valuable:

- **Correct the agent normally.** When you do, it logs the lesson
  (`log_lesson`) — that's the raw ore for new heuristics.
- **Say "save that as a heuristic."** **[Phase 2]** The agent drafts a
  complete heuristic into staging on the spot.

On hard problems **[Phase 2]**, when the top two matches score close together,
the agent spawns two read-only subagents — one per strategy — and synthesizes
their reports before touching your code.

## Your ten minutes a week (the gate)

This is your only recurring duty, and the whole system's quality control:

```bash
cd ~/heuristic-harness && git pull
ls heuristics/staging/          # what's waiting
python scripts/lint.py          # validity + cue-overlap check
# for each proposal: read it, then
git mv heuristics/staging/h-foo.md heuristics/   # promote
# ...or edit first, or delete it (one-line reason in the commit)
git commit -m "review: promoted h-foo, rejected h-bar (duplicate)" && git push
```

Honesty rule: if you catch yourself approving without reading, don't speed up
— tell the agents to propose less (that's a config/rules change, and it's in
the specs as INV-9). Your genuine attention is what the later autonomy phases
are trained on.

## The baseline week (before first real use)

Set `serve_mode: log_only` and work normally for a week. The system logs what
it *would* have served without changing anything — your permanent
before-picture. Then set `normal`. Don't skip this; it can never be
reconstructed later.

## Working with the librarian

Monthly-ish, open the repo with a capable agent (Claude) and say:
*"Run a librarian session per WF-4."* It distills unprocessed lessons, dedupes,
sharpens cues, proposes deprecations — everything lands in staging with a
report (`staging/librarian-report-<date>.md`). Review as usual.

The librarian also writes the initial library: at setup it inspects your
machine and drafts 10–20 heuristics plus your profile kernel; you thumb
through with "yes / no / almost" — you never have to enumerate your
preferences from memory.

## Where everything lives

| Path | What | You may edit? |
|---|---|---|
| `heuristics/*.md` | live library | yes, freely (it's yours) |
| `heuristics/staging/` | machine proposals | your review queue |
| `profile/kernel.md` | always-loaded facts about you (≤15 lines) | yes — keep it tiny |
| `logs/<machine>.jsonl` | event logs | never edit; read via `scripts/stats.py` |
| `adapters/` | agent rules snippets | edit `_template.md` only, regenerate |
| `specs/`, `progress/` | design + build state | via review discipline |

## Troubleshooting

- **Agent never calls the tools** → the rules snippet isn't loading. Check it's
  in the *global* rules location; re-read `adapters/` install notes. This is
  the #1 failure mode — verify it on day one, not eventually.
- **"No heuristics matched" constantly** → cues are written in answer-vocabulary
  instead of task-vocabulary. Ask the librarian to sharpen cues (it has the
  retrieval logs to see what was asked).
- **Weird/irrelevant heuristic served** → log it: tell the agent "that
  heuristic didn't apply" (it calls `log_outcome: not_applicable`). Enough of
  those and ranking/cues get fixed with evidence.
- **Empty results + note "baseline mode"** → `serve_mode` is still `log_only`.
- **Two machines out of sync** → `git pull` in the repo; logs never conflict by
  design. If git itself is broken, the flight recorder
  (`~/.harness/flightlog/`) has the raw event history.
- **Check health anytime** → `python scripts/stats.py` — retrieval rate,
  outcomes, no-outcome share, per-model breakdowns.

## What this will NOT do (honest expectations)

It will not make a cheap model as smart as a frontier model. It makes your
agents stop fumbling what you already taught them: fewer repeated mistakes,
your conventions respected, better strategy on hard tasks. The payoff
compounds over months and survives model swaps — the library is yours, not
the model's.
