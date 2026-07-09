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
