# 06 — Phases & Passes (the autonomy ladder)

Status: settled · Conforms to: [01](01-invariants.md), [08](08-build-process.md) · Requirement prefix: PH

Phases are a **trust ladder**: each phase automates only what the previous
phase's logs prove the human has been rubber-stamping. Graduation signals are
suggested evidence, judged by the gate — numbers below are defaults, not law.

Pass rules (atomicity, claiming, journaling) are defined in [08](08-build-process.md).
Pass IDs here are the canonical work breakdown. "∥" = parallel-safe with
(disjoint files, no dependency edge).

---

## Phase 1 — Retrieval (the harness exists and serves)

Scope: everything marked Phase 1 in specs 02–05. Agents retrieve and log;
all authoring is human/librarian; no proposal tools yet.

| Pass | Delivers | Depends on | ∥ with |
|---|---|---|---|
| P1.1 | repo scaffold, config loader, `.gitignore`, pip packaging | — | — |
| P1.2 | heuristic parser + validator (`scripts/lint.py` core) [DM-3..9] | P1.1 | P1.3 |
| P1.3 | redaction module + tests [SRV-6, INV-5] | P1.1 | P1.2 |
| P1.4 | event logger (JSONL, per-machine, atomic lines) [DM-13..16] | P1.3 | P1.5 |
| P1.5 | BM25 ranker + scope filter [TOOL-2, TOOL-5] | P1.2 | P1.4 |
| P1.6 | MCP server with `find_heuristics` + `get_heuristic` [TOOL-1..6, SRV-1..5] | P1.4, P1.5 | P1.9 |
| P1.7 | `log_outcome` + `log_lesson` tools [TOOL-7..8] | P1.6 (same file — NOT parallel with P1.6) | — |
| P1.8 | adapter template + Cline/Claude snippets + kernel injection [AGT-1..7, AGT-9] | P1.6 | P1.9 |
| P1.9 | seed library (10–20 entries) + kernel v1, owner thumb-through [WF-5] | P1.2 | P1.6, P1.8 |
| P1.10 | baseline week in `log_only` [WF-8] | P1.6–P1.9 | — |
| P1.11 | acceptance run: every Phase-1 criterion in specs 02–05, results → BUILDLOG | P1.10 | — |

- **PH-1** Phase 1 do-NOT-build: proposal tools, distillation, subagent pattern,
  stats weighting, anything from Phase ≥2. (Signatures for TOOL-9/10 are
  reserved, not implemented.)

**Graduation → Phase 2** (read from logs after ≥2 weeks of `normal` use):
retrieval fires at task start in ≥80% of tasks; served heuristics are visibly
applied (spot-check transcripts); zero unredacted secrets in logs; baseline
captured. Decision journaled in BUILDLOG.

---

## Phase 2 — Capture & parallelism (the library starts growing)

| Pass | Delivers | Depends on |
|---|---|---|
| P2.1 | `propose_heuristic` + `propose_update` [TOOL-9..10] | Phase 1 |
| P2.2 | proposal triggers in adapter template [AGT-8] + WF-1 lint integration | P2.1 |
| P2.3 | `scripts/distill.py` incl. `--manual` [WF-3] | Phase 1 |
| P2.4 | subagent orchestration in adapter [AGT-10..12] + reliability test with DeepSeek | Phase 1 |
| P2.5 | `scripts/stats.py` v1: retrieval/outcome/no-outcome reporting [DM-17, DM-19] | Phase 1 |
| P2.6 | acceptance: first real proposals through WF-1; subagent flow observed end-to-end | P2.1–P2.5 |

P2.1, P2.3, P2.4, P2.5 are mutually ∥ (disjoint files).

- **PH-2** Do-NOT-build: outcome-weighted ranking, auto-promotion, regression gate.

**Graduation → Phase 3**: ≥20 proposals reviewed; ≥70% promoted with no or
trivial edits; distillation demonstrably catches lessons missed in-session;
review time per WF-2 stays ≤ ~10 min.

---

## Phase 3 — Feedback-weighted evolution (the system prioritizes)

| Pass | Delivers | Depends on |
|---|---|---|
| P3.1 | outcome-weight in ranking, sliding window [TOOL-11] | P2.5 |
| P3.2 | librarian tooling: cue-overlap linter, dedupe report, staleness report [WF-4 items 2–4] | P2.5 |
| P3.3 | first full librarian session by capable agent, report in staging [WF-4] | P3.2 |
| P3.4 | acceptance: weighted ranking beats plain BM25 on spot-checks from logged history | P3.1 |

- **PH-3** Do-NOT-build: any machine write outside staging; candidate serving.

**Graduation → Phase 4**: ≥4 further weeks; librarian/update proposals accepted
≥85% unedited; weighted ranking confirmed better (P3.4); gate reports the
review loop feels like rubber-stamping for low-stakes items — that boredom IS
the signal, but it must agree with the logged numbers.

---

## Phase 4 — Scoped autonomy (promotion is partially delegated)

| Pass | Delivers | Depends on |
|---|---|---|
| P4.1 | regression gate: `scripts/regress.py` replays logged task summaries with/without candidate via API, diffs retrieval fit + model behavior on a golden set | P3.x |
| P4.2 | scoped auto-promotion: `kind: technique|user-fact` entries, non-destructive content, passing P4.1 → status `candidate`, served flagged [TOOL-12]; auto-`live` after N clean outcomes; `hurt` → auto-return to staging + gate alert | P4.1 |
| P4.3 | audit workflow: gate reviews weekly *diff of changes* instead of each item | P4.2 |

- **PH-4** Hard limits: kernel changes, `model-patch` entries, and anything whose
  body contains shell commands ALWAYS require the human gate. Auto-promotion is
  revoked (config flag) the first time a rollback was needed and the cause was
  judgment rather than bad luck.

**Graduation → Phase 5**: ≥4 weeks of auto-promotions with zero judgment-fault
rollbacks; library ≥ ~50 live entries (below that, Phase 5 machinery has
nothing to work on).

---

## Phase 5 — Composition, discovery, reach (build only what logs demand)

Menu, each item gated on demonstrated need from logs (PH-5):

- P5.1 composition files: named pipelines referencing heuristic ids (new file
  type, same staging path).
- P5.2 relationship links in frontmatter (`related`, `conflicts_with`) + linter
  enforcement of referential integrity.
- P5.3 gap detection: cluster `lesson`/`hurt` events lexically; recurring
  clusters with no matching heuristic → librarian queue.
- P5.4 `second_opinion` MCP tool (server-side parallel API call) if AGT-12
  fallback was needed.
- P5.5 embeddings ranker behind the same interface, ONLY if logged misses show
  BM25 vocabulary gaps (INV do-NOT-build lifts here).
- P5.6 community preparation: LICENSE + CONTRIBUTING (BEFORE first external
  contributor), external-contribution review policy incl. prompt-injection
  screening — see [07](07-future.md).

---

## PH-6 — Standing rule

Any work not attributable to a pass ID in this file is out of scope until a
spec change adds it (INV-10). "While I'm at it" is how specs die.
