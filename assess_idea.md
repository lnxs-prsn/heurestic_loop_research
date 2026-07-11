# Assessment: Is the Heuristic Harness Reinventing Cline's Skills/Rules?

**Date:** 2026-07-10
**Project:** Heuristic Harness v1
**Question:** Does this project duplicate what Cline/Claude already provides via `.clinerules/` and skills?

## TL;DR

The core insight is the same (cue-triggered retrieval beats bulk prompt injection), but the project builds **infrastructure around that insight** that Cline's system lacks: a growth pipeline from logged experience, a human-gated staging airlock, outcome logging with an evidence feedback loop, agent-agnostic design via MCP, and multi-machine git syncing. It is not redundant — it *externalizes* what agents currently do internally so it can be version-controlled, reviewed, grown systematically, and survive model/agent swaps. The risk is complexity and the overhead of the review gate, not duplication.

---

## 1. What's the same pattern

| Concept | Cline/Claude's system | Heuristic Harness |
|---|---|---|
| Always-loaded baseline knowledge | Global `.clinerules/` files | `profile/kernel.md` (≤15 lines, always injected) |
| On-demand guidance retrieval | Skills matched by task description | Heuristics matched by task summary via BM25 |
| Checkpoint checking | Skills are in context by default; no explicit trigger | Explicit `find_heuristics` calls before risky actions (AGT-5) |
| Cue-based indexing | Skill descriptions / names | YAML frontmatter `cues` field |
| Agent behavior modification | Markdown rules injected into system prompt | Heuristic bodies fetched and applied as instructions + MCP tool calls |
| Human-authored guidance | Files in `.clinerules/` or skill files | Human-promoted heuristics in `heuristics/` |

## 2. What's different (the new parts)

### 2.1 Growth from experience, not just authorship

Cline's rules/skills are authored by a human upfront. The Heuristic Harness grows its library from **logged corrections** (AGT-7: `log_lesson` when the user corrects the agent) and agent-discovered facts. The human's role shifts from *authoring* guidance to *recognizing and passing through* machine-drafted proposals — a comparative-advantage pairing (00-overview.md: "AI articulates, human recognizes").

**Implication:** The library grows from actual task friction, not from what the human remembers to pre-write. This is closer to the system learning than to configuration.

### 2.2 The staging airlock (INV-4)

Machine-authored content must land in `heuristics/staging/`. Promotion to the live library is a human act — `git mv` after review. Cline has no equivalent barrier between proposed rules and active rules; a human writes or edits directly, or not at all.

**Why it matters:** The airlock makes the human's attention the scarce resource (INV-9). This forces the system to be selective about what it proposes, and it creates a permanent audit trail of *what was proposed vs. what was accepted* — an evidence base for later autonomy decisions.

### 2.3 Outcome logging and feedback loop

Every applied heuristic gets a `log_outcome` verdict: `helped`, `not_applicable`, or `hurt`. This is permanent, schema-versioned evidence (INV-3). Cline's skills have no feedback mechanism — you cannot tell whether a skill actually improved outcomes without manually tracking it.

**Implication:** The logs let the system measure its own effectiveness, detect heuristics that hurt or don't apply, and justify autonomy graduation with data rather than intuition.

### 2.4 Agent-agnostic via MCP

The server exposes tools (`find_heuristics`, `get_heuristic`, `log_outcome`, `log_lesson`, `propose_heuristic`) over stdio MCP. Any MCP-capable agent can use it — Cline, Claude Code, or future agents. Adapters are generated from a single template (AGT-1) so they don't drift.

**Implication:** The heuristic library is decoupled from any specific agent's rules format. It survives model swaps and agent migrations. Cline's `.clinerules/` is tied to Cline's system prompt injection.

### 2.5 Multi-machine git sync

Logs are per-machine, append-only JSONL, and never conflict by design (INV-3). The library itself is a git repo — `git pull` on any machine gets the latest heuristics. The flight recorder (`~/.harness/flightlog/`) lives outside the repo (INV-8) so failure records survive repo corruption.

**Implication:** One reviewed heuristic propagates to all machines. Cline's rules are local per installation with no built-in sync mechanism.

## 3. Where it maps directly to skills/rules

Some Heuristic Harness features are genuinely just renaming:

| Heuristic Harness | Cline equivalent |
|---|---|
| `profile/kernel.md` | `clinerules/` — the always-loaded layer |
| Heuristic (cue-indexed markdown) | Skill file (description + instructions) |
| `find_heuristics` | Skill matching by task description |
| Human gate / weekly review | Human editing `.clinerules/` files |

These are not innovations — they're the same mechanism with different names. The value of the project lies in the parts **around** this core, not the core itself.

## 4. Concrete risks / downsides

1. **Two places for the same instruction.** If a heuristic says "no huge pip packages on Pi" but `.clinerules/also` says it, you get duplication, drift, or contradiction. The project acknowledges this via the adapter snippet that loads into Cline's global rules — but it doesn't solve the conflict problem.

2. **The review gate is a weekly tax.** The manual says "your ten minutes a week (the gate)." On a slow week this is trivial. On a busy week it becomes a backlog of un-promoted heuristics, which means the library is missing guidance the system itself identified as important.

3. **Retrieval quality is fragile.** The whole system depends on one-line task summaries (AGT-4: `<action> <object> <tech>`). Lazy summaries poison retrieval and analytics permanently, as the spec itself warns. Skills/rules don't depend on summary quality because they're always loaded or explicitly triggered.

4. **No embedded context.** Cline skills are loaded into the system prompt at task start — they're in-context immediately. The Heuristic Harness requires an explicit `find_heuristics` call and then a body fetch. This is an extra latency hop and a failure point (missing tool call = no heuristics).

## 5. Verdict

| Question | Answer |
|---|---|
| Does it reinvent the core idea? | Yes — cue-triggered retrieval of markdown guidance is what skills/rules already do |
| Is it purely redundant? | No — it adds infrastructure that skills/rules lack entirely (growth pipeline, feedback, multi-machine sync, agent-agnostic delivery) |
| Should this project exist? | It depends: if you work across multiple machines and agents, and want a growing evidence-gated library, yes. If you work on one machine with one agent, `.clinerules/` + skills is simpler and equally effective. |
| Biggest risk | The review gate becoming a bottleneck. The project's honesty itself says "if you catch yourself approving without reading, reduce proposal volume" (INV-9) — this is admitting the gate is hard to sustain. |

**Bottom line:** The Heuristic Harness is to Cline's skills what a package manager is to dropping `.so` files into `/usr/lib`. Same mechanism, but with version control, dependency tracking, provenance, and a growth pipeline. The mechanical core is a reinvention; the surrounding infrastructure is new and potentially valuable for specific workflows.