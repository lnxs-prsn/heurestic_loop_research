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

## Process

- Handoff system (specs/08 BP-15..BP-21) — done (10ee803) — owner-approved commit 2026-10-06 (D-9, D-11; BUILDLOG@2026-10-05T17:05+03:00)
- Human coherence trial (incubating/human-coherence-intent-anchoring, coherence/) — in-progress (claude-opus-5-5, pi, 2026-10-06) — re-entry RE-1 closed, intent INT-4 confirmed (SIT-1); nine findings not yet folded into the pattern spec; pattern committed 46f2708 (BUILDLOG@2026-10-06T13:55+03:00)

## Open decisions (owner)

Owner decisions live in [decisions.md](decisions.md) (BP-15); this list only points.

- ~~Final location of the harness repo~~ — decided: D-5.
pending_decisions: D-6, D-8, D-10
- License choice (MIT vs Apache-2.0) — required only before first external contribution (FUT-1); not yet a ledger entry.
