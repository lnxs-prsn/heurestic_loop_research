# 00 — Overview: The Heuristic Harness

Status: settled · Conforms to: [01-invariants.md](01-invariants.md) · Audience: everyone, read first

## What this is

An external heuristic system for AI coding agents. Heuristics — short, cue-indexed
units of guidance — live as markdown files in this git repository, are served to
agents on demand by a local MCP server, and grow over time from logged experience,
through a human-gated review process.

First deployment target: Cline + DeepSeek on the owner's machines. The design is
model-agnostic and agent-agnostic by construction.

## Why (the philosophy, in four sentences)

Humans hold their expertise as **tacit knowledge**: acquired implicitly, fired by
environmental cues, nearly impossible to enumerate on request (Polanyi: "we know
more than we can tell"). AI agents have the opposite profile: they can articulate
a rule fluently the moment they see it work, but forget everything between
sessions. This system pairs the two by comparative advantage: **AI articulates,
human recognizes and passes through.** Recall is cue-based, like human memory:
facts are not all held in working context — they are retrieved when the situation
matches their cue (the "coffee cup → honey, not sugar" principle).

## The three roles

| Role | Held by | Does |
|---|---|---|
| **Worker** | cheap frontline agent (DeepSeek in Cline) | uses heuristics on every task; logs outcomes; proposes new heuristics in the moment |
| **Librarian** | capable agent (Claude) | authors the seed library; periodically distills logs, dedupes, sharpens, proposes deprecations |
| **Gate** | the human owner | reviews staged proposals and promotes them; the only writer to the live library until Phase 4 graduation |

## System summary

- **Library**: `heuristics/` — one markdown file per heuristic, YAML frontmatter
  (cues, scopes, provenance), body ≤ ~250 words. Canonical store. See [02](02-data-model.md).
- **Server**: one local Python MCP server (stdio) exposing retrieval, logging and
  proposal tools to any MCP-capable agent. See [03](03-mcp-server.md).
- **Profile kernel**: a tiny always-injected file of diffuse (cue-less) user facts;
  everything with a discrete cue is a normal library entry with `kind: user-fact`.
- **Logs**: append-only per-machine JSONL, redacted at write time. The episodic
  memory of the system and the evidence base for every trust decision.
- **Staging airlock**: `heuristics/staging/` — the only place machine-authored
  content may be written. Promotion to live is a human act (git mv + review).
- **Autonomy ladder**: five phases; each automates only what the logs prove the
  human has been rubber-stamping. See [06](06-phases.md).

## Reading order

1. This file
2. [01-invariants.md](01-invariants.md) — the constitution (mandatory before any work)
3. Then the file(s) for your task:
   - implementing the server → [02](02-data-model.md), [03](03-mcp-server.md)
   - wiring an agent → [04](04-agent-integration.md)
   - operating the system → [05](05-workflows.md)
   - planning/executing build work → [06](06-phases.md), [08](08-build-process.md)
   - writing specs for anything else → [09](09-how-to-write-specs.md)

## Resuming the build (any agent, cold start)

Read, in order: this file → [01](01-invariants.md) → [progress/STATUS.md](../progress/STATUS.md)
→ tail of [progress/BUILDLOG.md](../progress/BUILDLOG.md). Then follow the
session protocol in [08-build-process.md](08-build-process.md). That is the whole
onboarding; no prior agent's memory is needed or permitted as a dependency.

## Glossary

- **Heuristic**: a cue-indexed unit of guidance (technique, convention, user-fact, or model-patch).
- **Cue**: short discriminative phrase(s) a task description is matched against.
- **Kernel**: the tiny always-loaded profile of cue-less user facts.
- **Staging / airlock**: machine-writable proposal area; nothing live comes from machines directly.
- **Pass**: the atomic unit of build work (see [08](08-build-process.md)).
- **Graduation signal**: logged evidence that unlocks the next autonomy phase.
- **Librarian session**: a periodic curation run by a capable agent over logs + library.
- **Flight recorder**: the machine-local, outside-git raw event log.

## Non-goals of the whole project

- Making a weak model as capable as a frontier model (impossible via scaffolding; see idea/ analysis).
- Multi-dimensional "reasoning scorecards", canary traffic-splitting, meta-memory layers (cut: need volume that does not exist at personal scale).
- Any always-on service, database, or cloud dependency.
