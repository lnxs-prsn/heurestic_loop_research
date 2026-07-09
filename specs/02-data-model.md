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
