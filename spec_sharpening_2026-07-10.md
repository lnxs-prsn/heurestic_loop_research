# Spec Sharpening Pass — Findings & Proposed Amendments

Date: 2026-07-10 · Auditor: claude-fable-5 (fresh context, BP-8 ritual) ·
Scope: specs 00–10 + MANUAL.md, per BUILDLOG mandate 2026-07-09T20:00 ·
Status: **proposal for the gate (INV-10)** — nothing below is applied.

Verdict up front: the spec set is in very good shape — internally consistent
at the architecture level, honest about non-goals, and it substantially obeys
its own method (09). The findings below are five implementability gaps an
implementer would trip on at P1.x (F-1..F-5), four medium inconsistencies
(F-6..F-9), and minor polish (F-10..F-15). None require design changes; all
are resolvable by small amendments. Diffs are unified-format against current
files; apply with `git apply` or by hand.

---

## A. Major — an implementer trips on these (fix before P1.1)

### F-1 · No mechanism carries `agent`/`model` identity to the server

DM-13 makes `agent` and `model` mandatory on every log event; TOOL-5 needs the
model id for scope filtering ("model from agent context per AGT-2"). But no
tool signature carries them, and `~/.harness/config.yaml` (SRV-2) can't — the
same config file serves both Cline and Claude Code on one machine. AGT-2 says
adapters "state the agent's identity fields", but a rules snippet has no
channel into the server process. As written, every event logs
`agent: unknown, model: unknown` and model-patch filtering (DM-5/TOOL-5)
cannot work at all.

Proposed mechanism: identity via environment variables in each host's MCP
registration (one registration per agent host — the natural per-agent config
point). Known limit to journal at P1.8: if the owner switches models inside
Cline without updating the registration, `model` is stale; acceptable at
personal scale, revisit if per-model stats look wrong.

```diff
--- a/specs/03-mcp-server.md
+++ b/specs/03-mcp-server.md
@@ SRV section, after SRV-7
+- **SRV-8** Caller identity: the server reads `agent` and `model` from env
+  vars `HARNESS_AGENT` / `HARNESS_MODEL`, set in each host's MCP registration
+  (one registration per agent host). Missing → `"unknown"` (DM-13). The model
+  value feeds TOOL-5 scope filtering. Adapters MUST document their
+  registration line including these vars (AGT-2).
```

```diff
--- a/specs/04-agent-integration.md
+++ b/specs/04-agent-integration.md
@@ AGT-2
 - **AGT-2** Each adapter states the agent's identity fields (agent name, model id)
-  so tool calls and log events carry correct `agent` / `model` values.
+  so tool calls and log events carry correct `agent` / `model` values.
+  Identity travels via the MCP registration environment (SRV-8), never via
+  tool parameters; each adapter's install notes show the full registration
+  line with `HARNESS_AGENT` / `HARNESS_MODEL` set.
```

```diff
--- a/MANUAL.md
+++ b/MANUAL.md
@@ step 4
-   - **Cline**: MCP settings → add stdio server `heuristics` → command `python -m harness.server`. Then copy `adapters/cline-rules.md` into Cline's **global** rules directory.
-   - **Claude Code**: `claude mcp add --scope user heuristics -- python -m harness.server`. Then append `adapters/claude-md-snippet.md` to `~/.claude/CLAUDE.md`.
+   - **Cline**: MCP settings → add stdio server `heuristics` → command `python -m harness.server`, env `HARNESS_AGENT=cline`, `HARNESS_MODEL=<model id>`. Then copy `adapters/cline-rules.md` into Cline's **global** rules directory.
+   - **Claude Code**: `claude mcp add --scope user heuristics --env HARNESS_AGENT=claude-code --env HARNESS_MODEL=<model id> -- python -m harness.server`. Then append `adapters/claude-md-snippet.md` to `~/.claude/CLAUDE.md`.
+   - (If you switch the model an agent uses, update its registration env — logs and model-scoped heuristics key off it.)
```

### F-2 · `log_outcome` / `log_lesson` can't populate the mandatory `project` field

DM-13: every event carries `project`. `find_heuristics` takes `project` as an
argument precisely because "the server cannot infer it" (TOOL-1) — but TOOL-7
and TOOL-8 have no such parameter, so outcome/lesson events can only say
`"unknown"`, gutting per-project analytics (DM-19, WF-4 item 5 "recurring
across ≥2 projects"). The API is not yet published, so INV-6 permits this.

```diff
--- a/specs/03-mcp-server.md
+++ b/specs/03-mcp-server.md
@@
-### `log_outcome(heuristic_id: str, outcome: str, task_summary: str, notes: str = "")`
+### `log_outcome(heuristic_id: str, outcome: str, task_summary: str, notes: str = "", project: str = "")`
 - **TOOL-7** `outcome` MUST be one of `helped | hurt | not_applicable | unclear`
-  (DM schema). Writes `outcome` event.
+  (DM schema). Writes `outcome` event. `project` as in TOOL-1 (empty → "unknown").
 
-### `log_lesson(lesson: str, task_summary: str, context: str = "")`
+### `log_lesson(lesson: str, task_summary: str, context: str = "", project: str = "")`
 - **TOOL-8** Captures a correction/insight NOT tied to an existing heuristic.
-  Writes `lesson` event. This is the raw ore for distillation (WF-3).
+  Writes `lesson` event; `project` as in TOOL-1. This is the raw ore for
+  distillation (WF-3).
```

(Adapter template consequence at P1.8: AGT-6/AGT-7 instructions say to pass
the project name — no spec diff needed, AGT-3 already establishes the value.)

### F-3 · DM-17's retrieval↔outcome join is undefined

"A `retrieval` with no matching `outcome` within 7 days" — *matching* is never
defined, and stats scripts can't be written without it (M-5: a MUST without a
verifiable check). Cheapest deterministic rule, no API change:

```diff
--- a/specs/02-data-model.md
+++ b/specs/02-data-model.md
@@ DM-17
 - **DM-17** No-outcome accounting: a `retrieval` with no matching `outcome` within 7 days is COUNTED as "no outcome" (its own bucket) by all statistics scripts — never silently dropped (survivorship-bias rule).
+  *Matching rule:* an `outcome` matches a `retrieval` iff its `heuristic_id`
+  is in the retrieval's `served` list, the `task_summary` strings are equal,
+  and the outcome is 0–7 days after the retrieval; if several retrievals
+  qualify, the most recent wins. Stats scripts MUST implement exactly this rule.
```

### F-4 · `git mv` cannot promote an untracked staging file

WF-1 step 2 and the MANUAL's gate snippet promote via `git mv` — but staged
proposals are written by the server and are *untracked* until some sync
commits them; `git mv` errors on an untracked source. The owner's first-ever
review session fails at its second command (M-15: a manual promise the system
can't keep).

```diff
--- a/specs/05-workflows.md
+++ b/specs/05-workflows.md
@@ WF-1 step 2
-   - **promote**: `git mv` into `heuristics/`, adjusting id on collision (DM-3), commit;
+   - **promote**: move into `heuristics/` (`git mv` if tracked, else `mv` +
+     `git add` — server-written proposals are untracked until a sync commit),
+     adjusting id on collision (DM-3), commit;
```

```diff
--- a/MANUAL.md
+++ b/MANUAL.md
@@ gate snippet
-# for each proposal: read it, then
-git mv heuristics/staging/h-foo.md heuristics/   # promote
+# for each proposal: read it, then
+mv heuristics/staging/h-foo.md heuristics/ && git add -A heuristics/  # promote
```

### F-5 · US-24 cannot be walked at P1.11 — it needs `scripts/stats.py` (P2.5)

Spec 10's role-story header schedules the operator stories at P1.11, and 06's
P1.11 row includes US-21..25 — but US-24 explicitly requires
`scripts/stats.py`, which is delivered at P2.5. The acceptance walk as
specified is impossible. Also: 10's header says "operator at P1.11/P3.4" but
06's P3.4 row lists only US-15..16 — dangling cross-reference.

```diff
--- a/specs/10-user-stories.md
+++ b/specs/10-user-stories.md
@@
-## Role stories (M-17) — maintainer verified at P1.11, operator at P1.11/P3.4
+## Role stories (M-17) — maintainer verified at P1.11; operator: US-25 at P1.11, US-24 at P2.6 (needs scripts/stats.py, P2.5)
@@ US-24
 - **US-24** As an operator, I can diagnose a retrieval misbehavior from
   `scripts/stats.py` and the logs alone (candidates, scores, scope filters
-  applied) — no print statements, no code edits.
+  applied) — no print statements, no code edits. (Walked at P2.6.)
```

```diff
--- a/specs/06-phases.md
+++ b/specs/06-phases.md
@@ P1.11 row
-| P1.11 | acceptance run: every Phase-1 criterion in specs 02–05 AND Phase-1 user stories walked live ([10](10-user-stories.md) US-1..9 + role stories US-21..25, US-RULE-1), results → BUILDLOG | P1.10 | — |
+| P1.11 | acceptance run: every Phase-1 criterion in specs 02–05 AND Phase-1 user stories walked live ([10](10-user-stories.md) US-1..9 + role stories US-21..23, US-25 per US-RULE-1), results → BUILDLOG | P1.10 | — |
@@ P2.6 row
-| P2.6 | acceptance: first real proposals through WF-1; subagent flow observed end-to-end; Phase-2 user stories walked (US-10..14) | P2.1–P2.5 |
+| P2.6 | acceptance: first real proposals through WF-1; subagent flow observed end-to-end; Phase-2 user stories walked (US-10..14, US-24) | P2.1–P2.5 |
```

---

## B. Medium — inconsistencies that cause drift if left

### F-6 · Package layout `server/` vs `python -m harness.server`

DM-1's layout mandates a top-level `server/` directory; the MANUAL installs
with `pip install -e` and runs `python -m harness.server`, implying a package
named `harness`. An implementer at P1.1 must guess. Propose the layout names
the package:

```diff
--- a/specs/02-data-model.md
+++ b/specs/02-data-model.md
@@ layout
-├── server/                 # MCP server implementation
+├── harness/                # python package: MCP server + modules (`python -m harness.server`)
```

(Alternative if the gate prefers `server/` on disk: keep the dir and amend the
MANUAL to a console-script entry point instead. Either way, decide now — the
registration command in every host freezes on this name at P1.8.)

### F-7 · "expensive-later item #2/#3" reference a list that exists nowhere in specs/

03 (SRV-5), 04 (AGT-4), 05 (WF-8) cite numbered items of an "expensive-later"
sweep defined only in the planning conversation / idea docs — a violation of
BP-8's "needing more context than the files provide is a bug in the files."
Cheapest fix, no new file:

```diff
--- a/specs/03-mcp-server.md
+++ b/specs/03-mcp-server.md
@@ SRV-5
-  `"baseline mode"`. This creates the control-group data (expensive-later item #3).
+  `"baseline mode"`. This creates the control-group data (M-12 sweep: a
+  baseline that is not captured before go-live can never be reconstructed).
```

```diff
--- a/specs/04-agent-integration.md
+++ b/specs/04-agent-integration.md
@@ AGT-4
-  This line is the join key of the entire system (expensive-later item #2);
+  This line is the join key of the entire system (M-12 sweep: a free-text
+  join key that can't be re-described must be format-mandated on day one);
```

```diff
--- a/specs/05-workflows.md
+++ b/specs/05-workflows.md
@@ WF-8
-the permanent control group. Flip to `normal` afterwards. Skipping this is
-irreversible (expensive-later item #3).
+the permanent control group. Flip to `normal` afterwards. Skipping this is
+irreversible (M-12 sweep — see SRV-5 note).
```

### F-8 · PH-6 read literally forbids spec work — including this pass

"Any work not attributable to a pass ID … is out of scope" — but spec
amendments (all five BUILDLOG entries so far, and this pass) carry no pass ID,
and the BP-13 handoff/disaster drill plus US-19/20 are wired to no pass at
all. The process spec's own acceptance is unscheduled work (M-14 coherence
failure).

```diff
--- a/specs/06-phases.md
+++ b/specs/06-phases.md
@@ PH-6
 Any work not attributable to a pass ID in this file is out of scope until a
 spec change adds it (INV-10). "While I'm at it" is how specs die.
+Two standing exceptions, both journaled in BUILDLOG rather than claimed as
+passes: (a) spec changes themselves, governed by INV-10; (b) the BP-13
+process drill (US-19..20), which MUST be run at least once during Phase 1
+and its result journaled before Phase-1 graduation.
```

### F-9 · TOOL-3's minimum-score threshold has no home

Raw BM25 scores are corpus-dependent; "below a minimum-score threshold" gives
the implementer no number and the operator no knob. Propose a config key,
tuned during the baseline week (which logs all candidate scores — DM-14 —
exactly the data needed to set it):

```diff
--- a/specs/03-mcp-server.md
+++ b/specs/03-mcp-server.md
@@ SRV-2 config example
   serve_mode: normal                      # normal | log_only  (baseline week, WF-8)
+  min_score: 1.0                          # TOOL-3 serve threshold; tune from baseline-week candidate scores
@@ TOOL-3
 - **TOOL-3** Returns up to `k` results: `{id, title, matched_cue, score}` plus a
-  `note` field. Below a minimum-score threshold, return fewer or none —
+  `note` field. Below the configured `min_score` threshold, return fewer or none —
   an honest "no heuristics matched" beats a forced weak match.
```

---

## C. Minor — one-line fixes, no diffs needed

- **F-10** AGT-9 "includes/points at kernel" is host-dependent: Claude Code can
  `@`-import so kernel edits are live; a copied Cline global-rules file goes
  stale. Add one sentence to AGT-9: "where the host cannot reference a file
  live, the adapter install notes MUST say the copy is refreshed at each gate
  session (WF-1)." US-3 ("my edit is live on the very next task") is otherwise
  silently false on Cline for kernel edits.
- **F-11** STATUS "Specs" lines say `done (initial commit)` — BP-4 requires a
  commit hash. Replace with the actual hashes (`f850bdb`, `864d884`/`5703b39`).
- **F-12** DM-7 and DM-8 exist only as YAML comments inside the example; M-1
  wants auditable requirements — restate both as bullets alongside DM-3..DM-6.
- **F-13** TOOL-9 scope params default to `""` while frontmatter uses `null`;
  add "empty string maps to `null` in the written file" to TOOL-9.
- **F-14** SRV-3 writes to the flight recorder but BP-11 only names
  `build-<machine>.log`; name the server's file (`server-<machine>.log`) in 03
  or BP-11.
- **F-15** US-10 (lesson capture) is Phase-1 functionality (TOOL-8 at P1.7,
  AGT-7 at P1.8) yet is verified only at P2.6; it could be walked at P1.11.
  Optional re-wiring — leaving it is defensible (Phase 2 is where capture
  *matters*), so gate's call.

---

## D. Self-conformance scorecard (specs 00–10 vs. method 09, M-1..M-17)

| Principle | Verdict | Notes |
|---|---|---|
| M-1 numbered normative reqs | pass− | F-12 (reqs hiding in YAML comments) |
| M-2 one concern/file, reading order | pass | header deps + 00 reading order |
| M-3 constitution | pass | 01 is short, deferred-to, change-gated |
| M-4 non-goals everywhere | pass | every file has a Do-NOT section |
| M-5 acceptance criteria | pass− | F-3, F-9: two MUSTs lacked a checkable form |
| M-6 trust-ladder phases | pass | graduation signals defined, data-answerable |
| M-7 atomic passes | pass− | F-8: BP-13 drill + spec work unattributable |
| M-8 externalized build state | pass | this pass cold-started from files alone — the property demonstrably holds |
| M-9 outside record | pass− | F-14 naming gap |
| M-10/M-11 data shape | pass | INV-1/2/3 well threaded through DM |
| M-12 expensive-later sweep | pass− | F-7: sweep cited by numbers defined nowhere in specs |
| M-13 airlock/comparative advantage | pass | INV-4/INV-9 + WF-1 |
| M-14 coherence | pass− | F-8 is the one violation found |
| M-15 manual-first | pass− | manual exists & derived stories, but F-1, F-4, F-6 are manual promises the specs can't yet keep |
| M-16 manual delta | n/a | new project |
| M-17 role stories | pass− | F-5: operator story scheduled before its tooling exists |

09-checklist steps 1–8: all satisfied (progress/ scaffolded and VCS
initialized before implementation — step 8 — confirmed by git history).

---

## E. Recommended application order

F-1, F-2, F-6 before P1.1 (they shape the scaffold and the frozen-on-publish
names); F-3, F-9 before P1.5; F-4 before P1.9's first review; F-5, F-8 are
spec-text-only, any time. Minors batch into one commit. All amendments are
INV-10 spec changes: gate reviews this file, applies accepted diffs, commits
with rationale, journals in BUILDLOG.

---

## Addendum (2026-07-10, after persona A/B test runs)

Two genuine defects surfaced by the test's fresh readers (DeepSeek/Cline),
missed by the original audit — adopted here as findings:

### F-16 · Kernel-update proposals have no producer (found by dry-packet run)

DM-11 routes machine kernel changes through `staging/kernel-update-<date>.md`,
and the log schema (02) even defines `"kind":"kernel"` proposal events — but
no v1/v2 tool can write either: TOOL-9 writes DM-valid *heuristic* files,
TOOL-10 writes `update-<id>` revisions. Only the librarian (repo access,
AGT-13) can author kernel proposals; an in-session agent cannot. Propose the
cheap fix — scope the promise, don't add a tool:

```diff
--- a/specs/02-data-model.md
+++ b/specs/02-data-model.md
@@ DM-11
-- **DM-11** Kernel is human-edited only (it is "live" in the INV-4 sense). Machine changes go through staging as `staging/kernel-update-<date>.md` proposals.
+- **DM-11** Kernel is human-edited only (it is "live" in the INV-4 sense). Machine changes go through staging as `staging/kernel-update-<date>.md` proposals — authored by the librarian (WF-4/AGT-13, direct file access); no MCP tool writes them (the `"kind":"kernel"` proposal event is logged by the librarian's session, reserved for a future tool).
```

### F-17 · `status: candidate` (TOOL-12, P4.2) is not in DM-7's enum (found by persona-packet run)

DM-7 allows `live | deprecated`; Phase 4 serves `status: candidate` entries.
A DM-7-conformant validator rejects every candidate file, so Phase 4 as
specified cannot start. Fix now (cheap) rather than at P4.2 (surprising):

```diff
--- a/specs/02-data-model.md
+++ b/specs/02-data-model.md
@@ DM-7 (YAML comment line)
-status: live                     # DM-7: live | deprecated  (staging is expressed by folder)
+status: live                     # DM-7: live | deprecated | candidate (Phase 4 only, TOOL-12; staging is expressed by folder)
```

### F-18 (minor) · AGT-10's "within 15%" has no formula (found by BOTH runs)

Absolute vs relative, and of which denominator, is unstated. One line in
AGT-10: "relative: |a−b| / max(a,b) ≤ 0.15".

### F-19 · Adopt persona rendering as a method principle (owner decision, 2026-07-10) — APPLIED as M-18

Owner closed the A/B experiment after one round (B: 3/7 seeded vs A: 2/7,
plus the sharpest unseeded catch), corroborated by owner's persona-spec tests
in other projects. Proposed amendment — append-only M-18:

```diff
--- a/specs/09-how-to-write-specs.md
+++ b/specs/09-how-to-write-specs.md
@@ end of section A, after M-17
+- **M-18 — Persona rendering: a comprehension and audit layer, never the
+  normative text.** (Numbered append-only.) A spec set MAY be rendered as a
+  first-person story — the system narrating its own pipeline, citing its
+  requirement IDs at every step, stopping to confess wherever it does not
+  know what it is supposed to do. Evidence (this project, 2026-07-10):
+  fresh readers found more real defects in persona form than in dry form,
+  and writing the story surfaces gaps by itself (M-15's manual effect,
+  stronger). Uses: onboarding implementers; periodic self-audit whose
+  confessions become journaled findings (M-5, INV-10). Limits: the numbered
+  files stay the only normative text (auditability, surgical diffs, stable
+  references — M-1 is load-bearing); the story is derived and MUST be
+  regenerated or marked stale when specs change.
```
