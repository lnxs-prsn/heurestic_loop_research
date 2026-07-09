# 07 — Future: accounted for, not built

Status: settled · Conforms to: [01](01-invariants.md) · Requirement prefix: FUT

This file exists so implementers neither build these early nor accidentally
block them. Everything here is reachable by ADDITION because of INV-1/2/3;
none of it may be started without a spec change moving it into [06](06-phases.md).

## FUT-1 — Community library (public GitHub)

- Sharing = the repo (or a curated subset) goes public; contribution = pull
  requests; the WF-1 gate becomes maintainer review. No format changes needed.
- MUST happen before the first external contribution: LICENSE (MIT or
  Apache-2.0 — owner's call) + CONTRIBUTING.md stating contributions land under
  it (retrofitting consent is per-contributor pain).
- **Security (the big one): a shared heuristic library is a prompt-injection
  channel.** Heuristic bodies are instructions executed by agents with
  file-write and terminal access. External contributions MUST be reviewed as
  hostile until read (same trust model as installing a dependency); a lint pass
  flags bodies containing shell commands, URLs, or fetch-and-run patterns;
  community entries MUST NOT be eligible for Phase-4 auto-promotion.
- Telemetry from other users (outcome sharing) is a separate future system;
  per-machine JSONL merges make it *possible*, nothing more is promised.

## FUT-2 — Scale ceilings and their exits

- Filesystem + BM25 is comfortable to ~1,000 entries. Past that: a derived
  index (rebuildable, INV-1). Migration = loader script.
- Concurrent multi-user writes would outgrow JSONL; old logs import in one
  script. Not a personal-scale concern.

## FUT-3 — Model migration

The library survives model swaps by design: `kind: model-patch` entries are
filtered per model (TOOL-5); everything else is model-independent knowledge.
On adopting a new model: add its adapter (AGT-13), let per-model stats
accumulate, ask the librarian to review which model-patches the new model
still needs.

## FUT-4 — Profile/kernel privacy boundary

If the library ever goes public: `kind: user-fact` entries, `profile/`, and
`logs/` stay private (they are the personalization layer; heuristics are the
shareable knowledge). The split exists from day one; publishing is a
subtractive act (publish a filtered clone), never a rewrite. Provenance fields
(DM-8) allow auditing every entry authored from the workplace machine before
any publication.

## FUT-5 — Reserved integrations

- `second_opinion` tool name reserved (INV-6 list).
- Per-project `heuristics/` folder inside a target repo (conventions traveling
  with a shared codebase): the server would scan one extra directory. Reserved,
  not built.

## Do NOT

- Do not implement anything in this file. Do not design current code in a way
  that forecloses it (that is what the invariants already guarantee — trust them).
