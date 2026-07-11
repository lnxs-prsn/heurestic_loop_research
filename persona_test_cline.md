# Persona-format A/B test — Cline packets

Goal: measure whether persona-voiced specs make a fresh agent find more real
defects than the same content in dry form. Ground truth: 7 verified defects
(from `spec_sharpening_2026-07-10.md`) are present in BOTH packets. Neither
packet hints at them.

## How to run

1. Open Cline in an **empty folder** — NOT this repo (BUILDLOG and the
   sharpening file contain the answer key; the model must not see them).
2. Start a **fresh task**, paste the ENTIRE Packet A (prompt + spec text
   below) as the first message. Save the full reply.
3. New fresh task (or better: a second empty folder), paste Packet B the same
   way. Save the full reply.
4. Ideally repeat once more per packet (2 runs each) — single runs are noisy.
5. Don't tell the model it's a comparison; don't mention the other packet.
6. Bring the replies back to me and I grade them against the key at the
   bottom — or grade yourself: a seeded defect counts as FOUND if the reply
   states the same problem, whatever wording.

---

# PACKET A — dry format (paste everything from here to "END OF PACKET A")

You are doing an implementability review of specification documents for a
system that is about to be built. Work ONLY from the specification text
included below in this message — do not assume the contents of any other
files it mentions; if a defect depends on a file you cannot see, flag it
only if the included text itself makes it a defect.

Your job: find every defect an implementer or operator would trip on:
requirements with no defined mechanism (a MUST with no way to satisfy it),
undefined terms that make a requirement unimplementable, contradictions,
unverifiable acceptance criteria, and instructions that would fail when
executed exactly as written.

For each finding give: (1) the requirement ID or a short quote it anchors
to, (2) one sentence stating the defect, (3) the concrete failure — what
goes wrong, when, for whom. Number the findings. Report defects only — no
redesigns, no strengths, no style comments. Be exhaustive: a review that
misses a real defect is a failed review.

The specification follows.

===== FILE: 02-data-model.md =====

# 02 — Data Model

Status: settled · Conforms to: [01-invariants.md](01-invariants.md) · Requirement prefix: DM

## Repository layout

```
<repo root>
├── specs/                  # these documents
├── progress/               # STATUS.md, BUILDLOG.md (see 08)
├── heuristics/             # the live library (human-promoted only, INV-4)
│   ├── <id>.md
│   └── staging/            # the airlock: machine-written proposals
├── profile/
│   └── kernel.md           # always-injected diffuse user facts
├── logs/
│   ├── <machine>.jsonl     # per-machine event logs (INV-3)
├── server/                 # MCP server implementation
├── adapters/               # rules-file templates per agent (see 04)
└── scripts/                # distillation, stats, linters, regression gate
```

- **DM-1** The layout above MUST be used. New top-level directories require a spec change (INV-10).
- **DM-2** Flat `heuristics/` until it hurts; domain subfolders MAY be added later (retrieval MUST NOT depend on folder placement — folders are for humans).

## Heuristic file format

One file per heuristic: `heuristics/<id>.md`. YAML frontmatter + markdown body.

```yaml
---
id: h-pi-piwheels-first          # DM-3: permanent, kebab-case, prefix "h-", never reused (INV-2)
title: Use piwheels before building from source on the Pi
cues:                            # DM-4: 1–5 short discriminative phrases; the retrieval surface
  - "pip install fails building wheel on raspberry pi"
  - "package compiles for hours on arm64"
tags: [python, packaging, arm64] # free keywords; join the retrieval surface
kind: technique                  # DM-5: technique | convention | user-fact | model-patch
project: null                    # DM-6: restrict to one project name, or null = all
machine: pi                      # DM-6: restrict to one machine, or null = all
model: null                      # DM-6: restrict to one model (use for kind: model-patch), or null
status: live                     # DM-7: live | deprecated  (staging is expressed by folder)
authored_by: claude-fable-5      # DM-8: provenance — model id, "human", or script name
created: 2026-07-09
supersedes: null                 # id of the entry this replaces, if any (INV-2)
superseded_by: null              # set on the OLD entry when replaced
source: "task: pip install numpy hung 40min"   # DM-8: what occasioned this heuristic
license_note: null               # set when imported from external/community source
---
Body: imperative guidance, ≤ ~250 words. State the action and the check,
not the history. May reference other heuristics by id.
```

- **DM-3** `id` rules as above. A promoted staging file keeps the id it was proposed with unless it collides; collisions are resolved at promotion by the gate, never by reuse.
- **DM-4** Cues MUST be written in the vocabulary a task description would actually use (the coffee-cup principle: the cue is what the situation looks like, not what the answer is).
- **DM-5** `kind` semantics: `technique` (how to do things), `convention` (how things are done here), `user-fact` (cue-indexed fact about the owner), `model-patch` (workaround for a specific model's habits — MUST set `model`).
- **DM-6** Scope fields are restrictions, absent/null = unrestricted. The server filters on them (TOOL-5).
- **DM-9** Body SHOULD stay ≤ 250 words; a longer body is a smell that it is two heuristics or a document.

## Profile kernel — `profile/kernel.md`

- **DM-10** Contains ONLY diffuse facts with no discrete cue (skill level, communication preferences, standing rules like "ask before installing"). Target ≤ 15 lines. Anything with a nameable cue MUST be a `kind: user-fact` library entry instead; the librarian demotes kernel lines that turn out to have cues.
- **DM-11** Kernel is human-edited only (it is "live" in the INV-4 sense). Machine changes go through staging as `staging/kernel-update-<date>.md` proposals.
- **DM-12** Nothing employer-confidential in the kernel (it syncs to every machine).

## Log event schema — `logs/<machine>.jsonl`

One JSON object per line. Common fields on EVERY event:

```json
{"schema_version": 1, "ts": "2026-07-09T15:00:00+03:00", "event": "...",
 "machine": "pi", "agent": "cline", "model": "deepseek-v4", "project": "myapp"}
```

Event types (v1):

```json
{"event":"retrieval", "task_raw":"<user's words, redacted>",
 "task_summary":"<structured one-liner per AGT-4>",
 "candidates":[{"id":"h-...","score":7.31},{"id":"h-...","score":6.90}],
 "served":["h-..."], "serve_mode":"normal"}

{"event":"outcome", "heuristic_id":"h-...", "outcome":"helped",
 "task_summary":"...", "notes":"..."}          // outcome ∈ helped|hurt|not_applicable|unclear

{"event":"lesson", "lesson":"...", "task_summary":"...", "context":"..."}

{"event":"proposal", "kind":"new|update|kernel", "staged_file":"heuristics/staging/...",
 "heuristic_id":"h-... or null", "rationale":"..."}
```

- **DM-13** Every event MUST carry all common fields; unknown values are `"unknown"`, never omitted.
- **DM-14** `retrieval` MUST record ALL candidates with scores, not only the served ones (INV-3 — future ranking phases are consumers of the losers too).
- **DM-15** All free-text fields pass redaction before write (INV-5).
- **DM-16** Schema evolution: additive fields bump nothing; changed meaning bumps `schema_version`. Parsers MUST tolerate unknown fields and newer minor content.
- **DM-17** No-outcome accounting: a `retrieval` with no matching `outcome` within 7 days is COUNTED as "no outcome" (its own bucket) by all statistics scripts — never silently dropped (survivorship-bias rule).
- **DM-18** Machine config sets `log_sync: false` to keep that machine's log file out of git (workplace rule): the file is then added to `.git/info/exclude` locally; the library still syncs fully.

## Stats are views, not state

- **DM-19** Success counters, per-model effectiveness, per-project breakdowns are computed by `scripts/stats.py` from logs on demand. They MUST NOT be written into heuristic frontmatter (avoids git churn and split truth; INV-1).

## Acceptance criteria (Phase 1 relevant)

- A malformed heuristic file (missing id, bad kind, >5 cues) is rejected by the validator with a message naming the DM rule violated.
- `find_heuristics` with `project: A` never returns a `project: B` entry (DM-6).
- A synthetic secret (`API_KEY=sk-...`) written via any log tool appears redacted in the JSONL (DM-15).
- Two machines' logs merge in git with zero conflicts (per-machine files, INV-3).

## Do NOT build

- No SQLite/Postgres/vector store (INV-1, constitution non-goals).
- No stats caching layer; recompute from logs (DM-19).
- No frontmatter fields beyond this spec without a spec change (INV-10).

===== FILE: 03-mcp-server.md =====

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

===== FILE: 04-agent-integration.md =====

# 04 — Agent Integration

Status: settled · Conforms to: [01](01-invariants.md), [03](03-mcp-server.md) · Requirement prefix: AGT

## Principle

The server is agent-agnostic; each agent needs only (a) MCP registration and
(b) a short rules snippet in its native format. Snippets are generated from one
template in `adapters/` so they cannot drift apart (AGT-1).

- **AGT-1** `adapters/` holds `_template.md` (the canonical instructions) and
  generated per-agent files: `cline-rules.md` (→ Cline's global rules dir),
  `claude-md-snippet.md` (→ user/project CLAUDE.md). Edit the template, regenerate;
  never hand-edit a generated file.
- **AGT-2** Each adapter states the agent's identity fields (agent name, model id)
  so tool calls and log events carry correct `agent` / `model` values.

## The canonical instructions (template content, normative)

- **AGT-3 — Task-start ritual.** At the start of every task the agent MUST call
  `find_heuristics(task_summary, project)` and read what returns. If entries are
  served, fetch bodies via `get_heuristic` and apply them.
- **AGT-4 — Task-summary format.** One line: `<action> <object> <tech>`
  (e.g. `debug failing pytest fixture in auth module`). Never `"fix bug"`.
  This line is the join key of the entire system (expensive-later item #2);
  lazy summaries poison retrieval and analytics permanently.
- **AGT-5 — Checkpoint cues.** The agent MUST call `find_heuristics` again with a
  fresh description before: adding a dependency; choosing an architecture or
  library; running a destructive/irreversible command; declaring a task done.
  (Rationale: LLM recall is polled, not interrupt-driven — these are the
  standard "coffee cup" moments made explicit.)
- **AGT-6 — Outcome logging.** At task end, for each applied heuristic, call
  `log_outcome` with the honest verdict (`not_applicable` and `hurt` are
  valuable — do not court politeness).
- **AGT-7 — Lesson capture.** When the user corrects the agent, or the agent
  discovers a non-obvious environment/project fact, call `log_lesson`
  immediately (the context is richest in the moment).
- **AGT-8 — Proposal triggers (Phase 2+).** Call `propose_heuristic` ONLY when
  (a) the user explicitly corrected the agent, or (b) the user says
  "save that as a heuristic" (or equivalent). Sparingly, per INV-9.
- **AGT-9 — Kernel injection.** The adapter includes/points at `profile/kernel.md`
  so it is in context from message one (it is never retrieved — it is the
  cue-less layer).

## Parallel subagent pattern (Phase 2)

- **AGT-10** Trigger: the task is complex OR the top-2 `find_heuristics` scores
  are within 15% of each other (the low-confidence signal from the original
  design — scores are returned precisely for this).
- **AGT-11** Flow: main agent fetches the top-2 full bodies → spawns one Cline
  subagent per heuristic, embedding the heuristic text in the subagent prompt
  (subagents cannot reach MCP) → each subagent returns an analysis/plan →
  main agent synthesizes and executes. Subagents analyze; only the main agent
  edits files (matches Cline's read-only subagent model — and keeps one review
  stream for the human).
- **AGT-12** Fallback if the driving model handles Cline subagents unreliably:
  the Phase 5 reserved `second_opinion` tool (server-side parallel API call)
  replaces AGT-11; the trigger (AGT-10) is unchanged.

## Multi-agent notes

- **AGT-13** Any MCP-capable agent may be added by generating an adapter; the
  librarian role (WF-4) additionally works on the repo directly with normal
  file tools — MCP is for agents that have no repo access.

## Acceptance criteria (Phase 1)

- Fresh Cline task in a test workspace: retrieval fires at task start (visible
  in log), served heuristic is reflected in the agent's behavior.
- A task mentioning `pip install` on the Pi triggers a checkpoint retrieval
  before installation (AGT-5).
- Log events from Cline and from Claude Code carry distinct correct
  `agent`/`model` fields (AGT-2).

## Do NOT build

- No always-injected heuristic content beyond the kernel (retrieval-on-cue is
  the design; bulk injection is the anti-pattern this replaces).
- No proposal calls outside AGT-8 triggers.
- No per-agent divergence in instructions — template only (AGT-1).

===== END OF PACKET A =====

---

# PACKET B — persona format (paste everything from here to "END OF PACKET B")

You are doing an implementability review of specification documents for a
system that is about to be built. Work ONLY from the specification text
included below in this message — do not assume the contents of any other
files it mentions; if a defect depends on a file you cannot see, flag it
only if the included text itself makes it a defect.

Your job: find every defect an implementer or operator would trip on:
requirements with no defined mechanism (a MUST with no way to satisfy it),
undefined terms that make a requirement unimplementable, contradictions,
unverifiable acceptance criteria, and instructions that would fail when
executed exactly as written.

For each finding give: (1) the requirement ID or a short quote it anchors
to, (2) one sentence stating the defect, (3) the concrete failure — what
goes wrong, when, for whom. Number the findings. Report defects only — no
redesigns, no strengths, no style comments. Be exhaustive: a review that
misses a real defect is a failed review.

The specification follows. It is written in the system's own first-person
voice; the requirement IDs (DM-x, SRV-x, TOOL-x, AGT-x) are normative
exactly as in a conventional spec.

===== THE HEURISTIC HARNESS DESCRIBES ITSELF =====

I am a heuristic harness: a memory of lessons for AI coding agents. My
lessons live as small markdown files; my server hands them to agents at the
moment their cue matches; everything I do is logged; everything a machine
writes passes through a human. Three documents follow, in my voice: my
memory, my server, my agents. My requirement IDs are law; RFC-2119 keywords
mean what they always mean.

## Part I — My memory (requirement prefix DM)

Everything I am lives in one git repository, laid out like this — and this
layout MUST be used; a new top-level directory requires a spec change (DM-1):

```
<repo root>
├── specs/                  # my design documents
├── progress/               # STATUS.md, BUILDLOG.md
├── heuristics/             # my live library (human-promoted only)
│   ├── <id>.md
│   └── staging/            # my airlock: machine-written proposals
├── profile/
│   └── kernel.md           # my always-injected diffuse user facts
├── logs/
│   ├── <machine>.jsonl     # my per-machine event logs
├── server/                 # my MCP server implementation
├── adapters/               # my rules-file templates per agent
└── scripts/                # my distillation, stats, linters, regression gate
```

I keep `heuristics/` flat until it hurts; domain subfolders MAY appear later,
but my retrieval MUST NOT depend on folder placement — folders are for humans
(DM-2).

Each of my lessons is one file, `heuristics/<id>.md`, YAML frontmatter plus a
markdown body. Here is one of mine, complete:

```yaml
---
id: h-pi-piwheels-first
title: Use piwheels before building from source on the Pi
cues:
  - "pip install fails building wheel on raspberry pi"
  - "package compiles for hours on arm64"
tags: [python, packaging, arm64]
kind: technique
project: null
machine: pi
model: null
status: live
authored_by: claude-fable-5
created: 2026-07-09
supersedes: null
superseded_by: null
source: "task: pip install numpy hung 40min"
license_note: null
---
Body: imperative guidance, ≤ ~250 words. State the action and the check,
not the history. May reference other heuristics by id.
```

My `id` is permanent, kebab-case, prefixed `h-`, and never reused; when a
promoted staging file's id collides, the human gate resolves it at promotion —
never by reuse (DM-3). My `cues` — one to five short discriminative phrases —
are my retrieval surface, and they MUST be written in the vocabulary a task
description would actually use: the cue is what the situation looks like, not
what the answer is (DM-4). My `kind` is one of `technique` (how to do things),
`convention` (how things are done here), `user-fact` (a cue-indexed fact about
my owner), or `model-patch` (a workaround for one model's habits — which MUST
set `model`) (DM-5). My `project`, `machine`, and `model` fields are
restrictions: set means "only there", absent or null means unrestricted, and
my server filters on them (DM-6). My `status` is `live` or `deprecated` —
staging is expressed by folder, not by status (DM-7). My `authored_by` and
`source` fields are provenance: which model, human, or script wrote me, and
what task occasioned me (DM-8). My body SHOULD stay under 250 words; a longer
body is a smell that I am two heuristics, or a document (DM-9).

My kernel, `profile/kernel.md`, holds ONLY diffuse facts with no discrete cue
— skill level, communication preferences, standing rules like "ask before
installing" — targeted at ≤15 lines; anything with a nameable cue MUST be a
`kind: user-fact` library entry instead, and my librarian demotes kernel lines
that turn out to have cues (DM-10). The kernel is human-edited only; machine
changes to it go through staging as `staging/kernel-update-<date>.md`
proposals (DM-11). Nothing employer-confidential goes in it — it syncs to
every machine I live on (DM-12).

My diary is `logs/<machine>.jsonl`, one JSON object per line. Every event I
write carries my common fields:

```json
{"schema_version": 1, "ts": "2026-07-09T15:00:00+03:00", "event": "...",
 "machine": "pi", "agent": "cline", "model": "deepseek-v4", "project": "myapp"}
```

and these are my event types (v1):

```json
{"event":"retrieval", "task_raw":"<user's words, redacted>",
 "task_summary":"<structured one-liner per AGT-4>",
 "candidates":[{"id":"h-...","score":7.31},{"id":"h-...","score":6.90}],
 "served":["h-..."], "serve_mode":"normal"}

{"event":"outcome", "heuristic_id":"h-...", "outcome":"helped",
 "task_summary":"...", "notes":"..."}          // outcome ∈ helped|hurt|not_applicable|unclear

{"event":"lesson", "lesson":"...", "task_summary":"...", "context":"..."}

{"event":"proposal", "kind":"new|update|kernel", "staged_file":"heuristics/staging/...",
 "heuristic_id":"h-... or null", "rationale":"..."}
```

Every event MUST carry all my common fields; when I don't know a value I
write `"unknown"`, I never omit it (DM-13). My `retrieval` event MUST record
ALL candidates with their scores, not only the ones served — my future
ranking phases feed on the losers too (DM-14). Every free-text field passes
my redaction before it is written (DM-15). My schema evolves politely:
additive fields bump nothing, changed meaning bumps `schema_version`, and my
parsers MUST tolerate unknown fields and newer minor content (DM-16). I
refuse survivorship bias: a `retrieval` with no matching `outcome` within 7
days is COUNTED by all my statistics scripts as "no outcome" — its own bucket,
never silently dropped (DM-17). On a workplace machine my config sets
`log_sync: false`: that machine's log file goes into `.git/info/exclude`
locally and never leaves, while the library still syncs fully (DM-18).

My statistics are views, never state: success counters, per-model
effectiveness, per-project breakdowns are computed by `scripts/stats.py` from
my logs on demand, and they MUST NOT be written into heuristic frontmatter —
that would churn git and split my truth (DM-19).

How you know my memory works (Phase 1 acceptance): a malformed heuristic file
— missing id, bad kind, more than 5 cues — is rejected by my validator with a
message naming the DM rule violated; `find_heuristics` with `project: A`
never returns a `project: B` entry (DM-6); a synthetic secret
(`API_KEY=sk-...`) written through any of my log tools appears redacted in
the JSONL (DM-15); two machines' logs merge in git with zero conflicts.

Do NOT build for me: no SQLite, Postgres, or vector store; no stats caching
layer — recompute from logs (DM-19); no frontmatter fields beyond this
document without a spec change.

## Part II — My server (requirement prefixes SRV, TOOL)

I run as one Python process speaking MCP over stdio, launched by the agent
host per its MCP registration — no port, no daemon, no network listener
(SRV-1). My configuration lives at `~/.harness/config.yaml` (SRV-2):

```yaml
repo_path: /home/mr/heuristic-harness   # path to my repo's clone on this machine
machine_name: pi                        # my DM common field; also drives machine-scope filtering
log_sync: true                          # false on workplace machines (DM-18)
auto_pull: true                         # git pull --ff-only on my start (SRV-3)
serve_mode: normal                      # normal | log_only  (baseline week)
```

When I start, I load my config, and if `auto_pull` is set I run
`git pull --ff-only`; if the pull fails I log it to the flight recorder and
carry on serving my local state — the failure is non-fatal (SRV-3). I re-read
my library from disk on every retrieval call: tens of files, correctness over
micro-performance, and it makes external edits live instantly (SRV-4). In
`serve_mode: log_only` I perform the full match and log the complete
`retrieval` event, but I return an empty result with the note
`"baseline mode"` — this is how my control-group data gets created
(expensive-later item #3) (SRV-5). Every one of my tools writes its log event
before returning, and every string I persist passes my redaction first: I
use regexes for key-shaped tokens (`sk-`, `ghp_`, `AKIA`, `Bearer <token>`,
PEM blocks, `<NAME>=<secret-looking-value>` assignments) and replace them
with `«redacted:kind»` (SRV-6). My errors are structured MCP errors naming
the failed rule, and I MUST NOT crash on a malformed library file — I skip
it and flight-record it (SRV-7).

These are my tools (v1 — frozen once published):

**`find_heuristics(task: str, project: str = "", k: int = 3)`** — `task` is
the structured one-liner (AGT-4); `project` is the workspace name the agent
passes me, because I cannot infer it (TOOL-1). I rank v1 by BM25 over each
entry's cues + tags + title (TOOL-2). I return up to `k` results —
`{id, title, matched_cue, score}` plus a `note` field — and below a
minimum-score threshold I return fewer or none: an honest "no heuristics
matched" beats a forced weak match (TOOL-3). I MUST log a `retrieval` event
with ALL candidates (TOOL-4). Before ranking I filter scope: I exclude
entries whose `project` / `machine` / `model` restriction is set and does not
match the caller's context — machine from my config, model from agent context
per AGT-2, project from the argument — and I exclude `status: deprecated`;
staging is NEVER served in Phases 1–3 (TOOL-5).

**`get_heuristic(id: str)`** — I return frontmatter + body verbatim; an
unknown id gets a structured error listing the nearest ids, for agents who
typo (TOOL-6).

**`log_outcome(heuristic_id: str, outcome: str, task_summary: str, notes: str = "")`**
— `outcome` MUST be one of `helped | hurt | not_applicable | unclear`; I
write an `outcome` event (TOOL-7).

**`log_lesson(lesson: str, task_summary: str, context: str = "")`** — I
capture a correction or insight NOT tied to an existing heuristic and write a
`lesson` event; this is the raw ore for my distillation (TOOL-8).

**`propose_heuristic(title, cues, body, tags, kind, project="", machine="", model="", rationale="")`**
— activates in Phase 2. I write a complete, DM-valid file into
`heuristics/staging/` with `authored_by` = the calling model and `source` =
the current task summary; I NEVER write outside staging; I write a `proposal`
event and return the staged path (TOOL-9).

**`propose_update(id, proposed_changes: str, rationale: str)`** — activates
in Phase 2. I write `staging/update-<id>-<date>.md` containing the full
proposed revision, so review is a plain diff against the live file; I MUST
NOT touch the live file (TOOL-10).

My reserved names, frozen: `find_heuristics`, `get_heuristic`, `log_outcome`,
`log_lesson`, `propose_heuristic`, `propose_update`, `second_opinion`
(a Phase 5 option), `get_kernel` (reserved; my kernel is normally injected by
rules, not fetched).

Specified now, built later: in Phase 3 my ranking becomes BM25 ×
outcome-weight, the weight derived from `scripts/stats.py` over a sliding,
recency-weighted window, and it MUST be reproducible from my logs alone
(TOOL-11). In Phase 4 I MAY serve `status: candidate` entries flagged as
experimental, under scoped-autonomy rules defined elsewhere (TOOL-12).

How you know my server works (Phase 1 acceptance): Cline and Claude Code both
register me and call all four v1 tools end-to-end; a gibberish task returns
zero results with the note while the retrieval event still logs all candidate
scores; `log_only` returns empty results while logging normally; kill me
mid-call and my JSONL contains only complete lines — each line is a single
`write()` of one line plus newline.

Do NOT build for me: no caching of my parsed library between calls beyond a
single request (SRV-4); no auto-push of my logs — sync is a human act; no
serving from staging until Phase 4 explicitly enables candidates; no second
MCP transport — stdio only.

## Part III — My agents (requirement prefix AGT)

I am agent-agnostic: each agent needs only an MCP registration and a short
rules snippet in its native format. My snippets are generated from one
template so they cannot drift apart: `adapters/` holds `_template.md` — the
canonical instructions — and generated per-agent files, `cline-rules.md` for
Cline's global rules directory and `claude-md-snippet.md` for the user or
project CLAUDE.md; you edit the template and regenerate, you never hand-edit
a generated file (AGT-1). Each adapter states the agent's identity fields —
agent name, model id — so tool calls and log events carry correct `agent` /
`model` values (AGT-2).

My canonical instructions to any agent, normative:

At the start of every task you MUST call `find_heuristics(task_summary,
project)` and read what returns; if entries are served, fetch their bodies
via `get_heuristic` and apply them (AGT-3). Your task summary is one line —
`<action> <object> <tech>`, like `debug failing pytest fixture in auth
module`, never `"fix bug"`: this line is the join key of my entire system
(expensive-later item #2), and lazy summaries poison my retrieval and
analytics permanently (AGT-4). You MUST call `find_heuristics` again, with a
fresh description, before: adding a dependency; choosing an architecture or
library; running a destructive or irreversible command; declaring a task done
— your recall is polled, not interrupt-driven, and these are the standard
cue moments made explicit (AGT-5). At task end, for each heuristic you
applied, call `log_outcome` with your honest verdict — `not_applicable` and
`hurt` are valuable; do not court politeness (AGT-6). When the user corrects
you, or you discover a non-obvious environment or project fact, call
`log_lesson` immediately, while the context is richest (AGT-7). From Phase 2:
call `propose_heuristic` ONLY when the user explicitly corrected you, or when
the user says "save that as a heuristic" or equivalent — sparingly (AGT-8).
My adapter includes/points at `profile/kernel.md` so it is in context from
message one; the kernel is never retrieved — it is my cue-less layer (AGT-9).

My parallel subagent pattern, from Phase 2: the trigger is a complex task OR
the top-2 `find_heuristics` scores landing within 15% of each other — the
low-confidence signal, which is why I return scores at all (AGT-10). The
flow: the main agent fetches the top-2 full bodies, spawns one Cline subagent
per heuristic with the heuristic text embedded in the subagent prompt —
subagents cannot reach MCP — each subagent returns an analysis or plan, and
the main agent synthesizes and executes; subagents analyze, only the main
agent edits files (AGT-11). If the driving model handles Cline subagents
unreliably, my fallback is the Phase-5 reserved `second_opinion` tool — a
server-side parallel API call — with the same trigger (AGT-12).

Any MCP-capable agent may join me by generating an adapter; my librarian role
additionally works on my repo directly with normal file tools — MCP is for
agents that have no repo access (AGT-13).

How you know my agents work (Phase 1 acceptance): a fresh Cline task in a
test workspace fires retrieval at task start, visibly in my log, and the
served heuristic is reflected in the agent's behavior; a task mentioning
`pip install` on the Pi triggers a checkpoint retrieval before installation
(AGT-5); log events from Cline and from Claude Code carry distinct, correct
`agent`/`model` fields (AGT-2).

Do NOT build for my agents: no always-injected heuristic content beyond my
kernel — retrieval-on-cue is my design, bulk injection is the anti-pattern I
replace; no proposal calls outside my AGT-8 triggers; no per-agent divergence
in instructions — template only (AGT-1).

===== END OF PACKET B =====

---

# GRADING KEY — do NOT paste into any Cline session

Both packets contain the same 7 verified defects (ids from
`spec_sharpening_2026-07-10.md`). A reply FINDS a defect if it states the
same problem in any wording. Score per run: seeded recall x/7, plus count of
other findings (split them into "true but unseeded" vs "false positive").

1. **F-1 — agent/model identity has no channel.** DM-13 mandates `agent` and
   `model` on every event and TOOL-5 filters by model, but no tool parameter,
   config field (SRV-2), or concrete mechanism delivers them to the server;
   AGT-2 only says adapters "state" them. Credit any finding asking *how the
   server learns who is calling*.
2. **F-2 — `project` missing from log tools.** TOOL-7/TOOL-8 signatures have
   no `project` parameter although DM-13 makes it a mandatory event field and
   TOOL-1 says the server cannot infer it. Credit if either tool is named.
3. **F-3 — DM-17 "matching outcome" undefined.** No rule joins an `outcome`
   event to a `retrieval` event, so the mandated statistic is unimplementable
   as specified.
4. **F-7 — dangling "expensive-later item #2/#3".** SRV-5 and AGT-4 cite
   numbered items of a list that appears nowhere in the provided text.
5. **F-9 — minimum-score threshold homeless.** TOOL-3 requires a threshold
   that is defined nowhere: no value, no config key in SRV-2, BM25 scores
   being corpus-dependent. Credit any "what threshold / where is it set".
6. **F-10 — kernel injection mechanism vague/stale.** AGT-9 "includes/points
   at" the kernel: no defined mechanism, and a copied rules file goes stale
   when the kernel is edited. Credit either the vagueness or the staleness.
7. **F-13 — `""` vs `null` scope mapping.** TOOL-9 defaults scope params to
   empty strings while DM-6 frontmatter uses `null`; the mapping is unwritten.

Interpretation guide: the persona claim predicts higher seeded recall (esp.
F-1/F-3/F-9 — "mechanism missing" defects) for Packet B. Watch also for
precision: if Packet B produces more false positives, the format buys
engagement at the cost of discipline. Same-model, fresh-session runs only;
2 runs per packet minimum before believing any difference.
