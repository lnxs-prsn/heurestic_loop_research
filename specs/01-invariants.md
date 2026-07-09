# 01 — Invariants (the constitution)

Status: settled · Deferred to by: every other spec file · Change policy: INV-10

These are the non-negotiables. Every implementer — human or AI — MUST have read
this file before touching the repository. When any other spec, log entry, or
instinct conflicts with this file, this file wins; if this file is wrong, change
it first (INV-10), then act.

Normative keywords MUST / MUST NOT / SHOULD / MAY are used as in RFC 2119.

- **INV-1 — Files + git are the canonical store.** All truth lives in plain-text
  files under version control. Databases, indexes, caches, embeddings and
  statistics are derived artifacts and MUST be rebuildable from the files and
  logs at any time. Migrations are loader scripts, never conversions of truth.

- **INV-2 — Stable IDs, never reused, never renamed.** Every heuristic has a
  permanent `id`. Improvement happens by superseding (new entry + `supersedes`/
  `superseded_by` links), not by renaming or deleting. This keeps all history
  joinable forever.

- **INV-3 — Logs are append-only, generous, and schema-versioned.** Every log
  event carries `schema_version`. Capture more than the current phase needs
  (all retrieval candidates with scores, raw task text, model, machine,
  project): data not recorded is the only thing no future phase can recover.
  Log files are per-machine; no two machines write the same file.

- **INV-4 — The staging airlock.** Machine-authored content (heuristics,
  updates, profile changes) MUST be written only to `heuristics/staging/`.
  The live library and the profile kernel are human-promoted until a phase
  graduation (per [06](06-phases.md)) explicitly delegates a scoped part of
  promotion. No exception for "obviously correct" changes.

- **INV-5 — Redaction before persistence.** Every string persisted to any log
  MUST first pass the redaction function (secret-shaped tokens, key material,
  credential assignments). A secret that reaches a synced file is unrecoverable
  (git history is forever); therefore redaction is at write time, not at sync time.

- **INV-6 — The tool API is frozen at first publication.** MCP tool names and
  existing parameter meanings MUST NOT change once written into any rules file.
  Evolution is additive only (new optional parameters, new tools). Reserved
  names are listed in [03](03-mcp-server.md) §Reserved.

- **INV-7 — No agent-native state.** Build progress, decisions, and system state
  MUST live in plain files in this repo (or the flight recorder). Agent memory
  systems, IDE checkpoints, and todo tools MAY be used as scratch but MUST NOT
  be the only place anything lives. No agent's context window, uptime, or rate
  limit may be load-bearing.

- **INV-8 — The flight recorder lives outside the repository.** A machine-local,
  append-only raw event log (`~/.harness/flightlog/`) records sessions, pass
  claims, git operations and errors. It is never synced, never edited, never
  inside the repo — because the record of failures must not live inside the
  thing that fails.

- **INV-9 — The human gate is kept honest by scarcity.** Machine proposals MUST
  be rare enough to actually be read (triggers: explicit correction or explicit
  request — not after every task). Rubber-stamping detected in review behavior
  is a signal to reduce proposal volume, not to widen autonomy.

- **INV-10 — The spec governs itself.** Changes to specs pass through the same
  review discipline as heuristic promotion: proposed as a diff, reviewed by the
  gate, committed with rationale. Implementation MUST NOT drift from spec
  silently; when reality disagrees with spec, the disagreement is journaled in
  BUILDLOG and resolved by changing one of them explicitly.

## Do NOT build (constitution-level non-goals)

- No database of record. No server other than the stdio MCP process. No network
  listener. No cloud dependency beyond git remotes and model APIs.
- No embeddings/vector store before Phase 5, and then only if BM25 misses are
  demonstrated from logs.
- No automatic write to the live library or kernel before Phase 4 graduation.
