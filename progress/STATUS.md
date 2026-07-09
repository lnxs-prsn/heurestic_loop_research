# STATUS

Format per BP-4. Phases/passes defined in [specs/06-phases.md](../specs/06-phases.md).

## Specs

- specs 00–09 — done (initial commit) — full spec set authored and reviewed in planning conversation
- MANUAL.md + specs/10-user-stories.md — done — manual-first artifact + story verification layer wired into 06 acceptance passes; 09 updated with M-15

## Phase 1 — Retrieval

- P1.1 — todo — repo scaffold, config loader, packaging
- P1.2 — todo — heuristic parser + validator
- P1.3 — todo — redaction module
- P1.4 — todo — event logger
- P1.5 — todo — BM25 ranker + scope filter
- P1.6 — todo — MCP server: find_heuristics, get_heuristic
- P1.7 — todo — MCP server: log_outcome, log_lesson
- P1.8 — todo — adapter template + Cline/Claude snippets + kernel injection
- P1.9 — todo — seed library + kernel v1 (librarian + owner thumb-through)
- P1.10 — todo — baseline week (log_only)
- P1.11 — todo — Phase 1 acceptance run

## Phase 2+ 

Not started. See specs/06-phases.md. Graduation from Phase 1 not yet possible (no usage data).

## Open decisions (owner)

- Final location of the harness repo (this repo vs. dedicated `~/heuristic-harness`) — decide at P1.1.
- License choice (MIT vs Apache-2.0) — required only before first external contribution (FUT-1).
