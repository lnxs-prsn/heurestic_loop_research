# 03 — MCP Server

Status: settled · Conforms to: [01](01-invariants.md), [02](02-data-model.md) · Requirement prefix: TOOL / SRV

## Runtime

- **SRV-1** One Python process, MCP over **stdio**, launched by the agent host
  (Cline / Claude Code) per its MCP registration. No port, no daemon, no network
  listener (constitution non-goal).
- **SRV-2** Config file `~/.harness/config.yaml`:
  ```yaml
  repo_path: /home/mr/heuristic-harness   # path to this repo's clone on this machine
  machine_name: pi                        # DM common field; also drives machine-scope filtering
  log_sync: true                          # false on workplace machines (DM-18)
  auto_pull: true                         # git pull --ff-only on server start (SRV-3)
  serve_mode: normal                      # normal | log_only  (baseline week, WF-8)
  ```
- **SRV-3** On start: load config; if `auto_pull`, run `git pull --ff-only`
  (failure is logged to flight recorder and NON-fatal — serve the local state).
- **SRV-4** Library is re-read from disk on each retrieval call (tens of files;
  correctness over micro-performance; also makes external edits live instantly).
- **SRV-5** `serve_mode: log_only`: `find_heuristics` performs matching and logs
  the full `retrieval` event but returns an empty result with note
  `"baseline mode"`. This creates the control-group data (expensive-later item #3).
- **SRV-6** Every tool writes its log event before returning (INV-3); every
  persisted string passes redaction first (INV-5). Redaction: regexes for
  key-shaped tokens (`sk-`, `ghp_`, `AKIA`, `Bearer <token>`, PEM blocks,
  `<NAME>=<secret-looking-value>` assignments), replaced with `«redacted:kind»`.
- **SRV-7** Errors return structured MCP errors with the failed rule named;
  the server MUST NOT crash on malformed library files (skip + flight-record).

## Tools (v1 — frozen per INV-6)

### `find_heuristics(task: str, project: str = "", k: int = 3)`
- **TOOL-1** `task` is the structured one-liner (AGT-4); `project` is the
  workspace name passed by the agent (the server cannot infer it).
- **TOOL-2** Ranking v1: BM25 over each entry's `cues + tags + title`.
- **TOOL-3** Returns up to `k` results: `{id, title, matched_cue, score}` plus a
  `note` field. Below a minimum-score threshold, return fewer or none —
  an honest "no heuristics matched" beats a forced weak match.
- **TOOL-4** MUST log a `retrieval` event with ALL candidates (DM-14).
- **TOOL-5** Scope filtering before ranking: exclude entries whose `project` /
  `machine` / `model` restriction is set and does not match the caller's context
  (machine from config; model from agent context per AGT-2; project from arg).
  Exclude `status: deprecated`. Staging is NEVER served in Phase 1–3.

### `get_heuristic(id: str)`
- **TOOL-6** Returns frontmatter + body verbatim. Unknown id → structured error
  listing nearest ids (typo tolerance for agents).

### `log_outcome(heuristic_id: str, outcome: str, task_summary: str, notes: str = "")`
- **TOOL-7** `outcome` MUST be one of `helped | hurt | not_applicable | unclear`
  (DM schema). Writes `outcome` event.

### `log_lesson(lesson: str, task_summary: str, context: str = "")`
- **TOOL-8** Captures a correction/insight NOT tied to an existing heuristic.
  Writes `lesson` event. This is the raw ore for distillation (WF-3).

### `propose_heuristic(title, cues, body, tags, kind, project="", machine="", model="", rationale="")`  — *activates Phase 2*
- **TOOL-9** Writes a complete, DM-valid file into `heuristics/staging/` with
  `authored_by` = calling model, `source` = current task summary. NEVER writes
  outside staging (INV-4). Writes `proposal` event. Returns the staged path.

### `propose_update(id, proposed_changes: str, rationale: str)` — *activates Phase 2*
- **TOOL-10** Writes `staging/update-<id>-<date>.md` containing the full
  proposed revision (so review is a plain diff against the live file). MUST NOT
  touch the live file.

## Reserved (INV-6 freeze list)

`find_heuristics`, `get_heuristic`, `log_outcome`, `log_lesson`,
`propose_heuristic`, `propose_update`, `second_opinion` (Phase 5 option),
`get_kernel` (reserved; kernel is normally injected by rules, not fetched).

## Phase 3+ additions (specified now, built later)

- **TOOL-11** (Phase 3) Ranking becomes `BM25 × outcome-weight`, where
  outcome-weight derives from `scripts/stats.py` over a sliding window
  (recency-weighted; kimi.md's temporal regularization). Weighting MUST be
  reproducible from logs alone (INV-1).
- **TOOL-12** (Phase 4) `find_heuristics` MAY serve `status: candidate` entries
  flagged as experimental, per the scoped-autonomy rules in [06](06-phases.md).

## Acceptance criteria (Phase 1)

- Cline and Claude Code both register the server and successfully call all four
  v1 tools end-to-end on this machine.
- Threshold behavior: a gibberish task returns zero results with the note, and
  the retrieval event still logs all candidate scores.
- `serve_mode: log_only` returns empty results while logging normally.
- Kill the server mid-call; JSONL file contains only complete lines (write =
  single `write()` of one line + newline).

## Do NOT build

- No caching of parsed library between calls beyond a single request (SRV-4).
- No auto-push of logs (sync is a human/workflow act, WF-6).
- No serving from staging (until [06] Phase 4 explicitly enables candidates).
- No second MCP transport (SSE/HTTP) — stdio only.
