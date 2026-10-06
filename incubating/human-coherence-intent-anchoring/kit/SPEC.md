# SPEC — human coherence structure using intent anchoring (agent-facing)

> **Known delta (2026-10-06):** first-trial findings are not yet applied
> here. Most important: HC-24 "restate" is to become "agent drafts the intent
> from evidence; owner confirms or corrects". See PATTERN.md "Proven in".

Requirement prefix: **HC**. Normative keywords MUST / MUST NOT / SHOULD / MAY
as in RFC 2119. The owner-facing explanation of the same structure is
`OWNER_GUIDE.md`; when they disagree, fix one explicitly, never silently.

**Purpose.** Agents stay coherent by reading files. The human in charge (the
*owner*) cannot: after a gap they have lost the way back into the project,
their idea has moved in conversations elsewhere, and agents keep changing the
project faster than one person can follow. This spec keeps the owner coherent
by anchoring everything that reaches them to the project's **intent**: what
the project is for.

**Three facts the design rests on** (do not design against them):
1. *Good memory, bad recovery.* Given a frame (what / why / how / when), the
   owner recalls most of the project or can ask precise questions about the
   rest. Re-orientation is cue-giving, not re-teaching.
2. *A disoriented owner cannot be asked cold.* Questions come after the frame.
3. *The intent is often written down nowhere, not even in the owner's head.*
   It is reconstructed from evidence, then confirmed by the owner.

Placeholders: `<cdir>` = this structure's directory (default `coherence/`);
`<ledger>` = the project's decision ledger, if any; `<agent entry>` = the file
agents auto-load (e.g. `AGENTS.md`).

---

## 1. Files

- **HC-1** The structure lives in plain files under `<cdir>/`:
  `intent.md` (intent timeline), `story-map.md`, `inbox/` + `inbox/INDEX.md`,
  `reentry/RE-<n>.md` (re-entry and reflection briefs), `owner-log.md`.
  No database, no app; any rendered view is derived from these files.
- **HC-2 — Record format.** Every record is a markdown heading carrying a
  permanent ID (`## <ID> — <title>`), immediately followed by `key: value`
  field lines, then free prose. IDs are never reused or renamed. References
  between records use IDs in reference fields (`evidence`, `affects`,
  `builds_on`, `supersedes`, `superseded_by`), comma-separated, or `none`.
  This keeps every record machine-parseable and every link a typed edge, so
  search, retrieval or a graph can later be built as a *derived* view.
- **HC-3 — Append-only.** Records are appended. A record's prose is never
  rewritten after the owner has confirmed it; corrections are new records
  that `supersede` old ones, and the old record only gains `superseded_by`.
  Status fields MAY change as a record moves through its lifecycle.

## 2. The intent timeline — `<cdir>/intent.md`

- **HC-4** Entries `INT-<n>` with fields:
  `kind` ∈ origin | checkpoint | evolution | restated ·
  `describes` (ISO date the intent is *as of*) ·
  `status` ∈ derived | confirmed | superseded ·
  `confirmed` (`<date>, owner` or `none`) ·
  `evidence` · `builds_on` (parent project's INT id for a sub-project, or
  `none`) · `supersedes` · `superseded_by`.
  Body has four sections: **For** (what the project is for), **For whom**,
  **Success looks like**, **Not** (what it deliberately isn't).
- **HC-5 — Kinds.** *origin*: reconstructed from the material the project
  started from. *checkpoint*: reconstructed from what the project had become
  at a date (e.g. when a pause began). *evolution*: what outside material
  since a checkpoint proposes. *restated*: the owner's own restatement from a
  re-entry, in their words.
- **HC-6 — Evidence per claim.** A *derived* entry MUST cite evidence for
  each statement it makes (file paths, record IDs, commits). A statement with
  no evidence MUST be marked `(inferred)`.
- **HC-7 — Owner confirms.** Only the owner confirms an entry. An agent MUST
  NOT set `status: confirmed` without the owner's explicit confirmation in a
  sitting recorded in `owner-log.md` (HC-30). An agent MUST NOT present a
  derived entry as confirmed, in any file or message.
- **HC-8 — Current intent.** The current intent is the newest *confirmed*
  entry not superseded. If none is confirmed, every owner-facing artifact
  MUST say the intent is unconfirmed.

## 3. The story map — `<cdir>/story-map.md`

- **HC-9** The map belongs to one intent entry (`map_for: INT-<n>` at the
  top). Stages `ST-<n>` with fields:
  `order` · `contributes` (one line: what this stage contributes to the
  intent) · `state` ∈ grasped | partial | open · `evidence` ·
  `alternatives` (options still alive at this stage, or `none`) ·
  `status` ∈ derived | confirmed.
- **HC-10** Stages and states are derived by agents from evidence and
  confirmed by the owner at re-entry (same rule as HC-7). Agents MAY update
  `state` between re-entries, citing evidence; the change is shown at the
  next re-entry.
- **HC-11** "open" with live alternatives and "open" with nothing considered
  are different findings and MUST be distinguishable (the `alternatives`
  field). An open stage crowded with undecided options is an absent
  decision, not an absent idea.

## 4. Intent impact — on every owner-facing item

- **HC-12** Every item that asks for or reaches the owner's attention (a
  decision, an inbox item, a finished piece of work, a digest line) MUST
  carry three plain-language fields:
  `stage` (a stage name, with its ST id) ·
  `impact` ∈ changes-intent | advances | route-only | untouched ·
  `why` (one line, in the language of the intent).
  In a decision ledger these are added as extra fields on each entry.
- **HC-13 — Impact meanings.** *changes-intent*: alters For / For whom /
  Success / Not. *advances*: moves a stage toward done under the unchanged
  intent. *route-only*: changes how a stage is reached, not what the project
  is for. *untouched*: neither.
- **HC-14 — Ordering, not capping.** Items reach the owner ordered by impact:
  changes-intent first (always the owner's call), then advances (largest
  first), then route-only (grouped and decided together). *Untouched* items
  are handled by agents under rules the owner already approved, logged, and
  never pushed at the owner. There is no count cap. Items with the same
  effect MUST be merged before they reach the owner.
- **HC-15 — Plain language.** Owner-facing text MUST say what an item is in
  words. IDs MAY follow as references; a bare ID is never the description.

## 5. The inbox — `<cdir>/inbox/`

- **HC-16** Material from outside the project (the owner's conversations
  elsewhere, documents from other agents or projects, notes) is dropped into
  `inbox/` and registered in `inbox/INDEX.md` as `IN-<n>` the session it is
  first seen, with fields: `file` · `received` · `source` ·
  `status` ∈ registered | processed | presented | resolved ·
  `stages` · `impact` · `evidence`.
- **HC-17 — Processing.** Before it reaches the owner, each item is
  processed: its body gains **What** (what it changes), **Why** (the reason
  it gives), **How** (how it intends to move the project), written against
  the current intent (HC-8) and the story map. Raw material MUST NOT be
  handed to the owner unprocessed.
- **HC-18** Registering and processing are not adopting. An inbox item
  changes the intent only through a re-entry resolution (HC-26).

## 6. Re-entry — the owner's way back in

- **HC-19 — When.** A re-entry runs when the owner asks, or when an agent
  sees coherence signals (HC-28) and the owner accepts its offer.
- **HC-20 — Step 1, process (before the owner sits down).** Every change
  since the owner's last sitting (HC-30) is processed (HC-17) and given its
  impact (HC-12). The intent timeline gains any missing *checkpoint* entry
  for where the project stood at the start of the gap, and *evolution*
  entries for what has arrived since, all `derived`.
- **HC-21 — Step 2, the frame.** The agent presents, in a short first view:
  *what* the project is for, *why*, *how* it was going about it, and *when*
  things happened, from origin to the start of the gap to now. Then where
  the project stood **relative to the intent** at the start of the gap: each
  stage with what it contributes to the intent and how far it had got, and
  each waiting decision with which part of the intent it serves. Never a
  bare list of states.
- **HC-22 — Step 3, recall and ask.** The owner recalls and asks directed
  questions; the agent answers each from the files, citing them, at whatever
  depth is asked. This continues until the owner says they have the thread.
  The owner's questions set the depth; the agent MUST NOT push a full
  read-through.
- **HC-23 — Step 4, proposed moves.** Processed material is grouped into
  *moves* (items that push the project the same way). Each move is described
  in the language of the intent, against two fixed points:
  (a) the intent: what it keeps, changes, drops, and whether it changes the
  intent itself or only the route;
  (b) the position at the start of the gap: stages it reopens or advances,
  decisions it affects or makes moot.
  Moves are ordered by impact (HC-14) and shown side by side. The agent MUST
  NOT recommend any move before the owner has restated (HC-24).
- **HC-24 — Step 5, restate.** Only now is the owner asked what the project
  is and should become, in any form. The answer is recorded as a `restated`
  INT entry, in the owner's words.
- **HC-25 — Step 6, drift check.** The agent compares the restatement with
  the timeline and each move and labels each point:
  kept | evolved | adopted-move | rejected-move | new | dropped.
- **HC-26 — Step 7, resolve.** For each difference, the owner chooses:
  update the intent · keep the old · park as an open question ·
  **sub-project built on top** (a new idea that needs the current project
  underneath it gets its own intent timeline with `builds_on`, and starts
  when its base allows). Outputs: a confirmed INT entry (or the existing one
  re-confirmed with today's date), any new decisions, and pending decisions
  re-ordered by impact on the resulting intent.
- **HC-27 — The brief.** Each re-entry leaves `reentry/RE-<n>.md` with
  fields `kind: reentry` · `date` · `gap_start` · `intent_before` ·
  `intent_after` · `evidence`, and sections: Frame · Questions asked ·
  Moves · Restatement · Drift check · Resolutions. Briefs form a series and
  are never rewritten.

## 7. Coherence signals

- **HC-28** An agent SHOULD offer a re-entry (never force one) when it sees
  any of:
  - the owner's instructions or questions contradict the current intent, or
    reopen something already settled;
  - the owner cannot place a decision put to them;
  - inbox items with impact changes-intent are waiting and no re-entry has
    happened since they arrived;
  - a long run of work or decisions with impact route-only or untouched
    (the project is busy but not moving);
  - the intent timeline has competing unconfirmed entries;
  - a long gap since the last owner sitting (project sets the length).
  The offer names the signal in plain words.
- **HC-29 — Check before asking.** Before putting any question to the owner,
  an agent MUST check whether the owner's earlier answers (confirmed intent,
  decision ledger, owner log, re-entry briefs) already decide it. If they do,
  the agent applies that answer, tells the owner which earlier answer settled
  it, and lets them object.

## 8. The owner log — `<cdir>/owner-log.md`

- **HC-30** One record `SIT-<n>` per owner sitting, with fields `date` ·
  `kind` ∈ reentry | decisions | reflection | other · `confirmed` (IDs the
  owner confirmed, or `none`) · `decided` (IDs, or `none`) · `brief` (RE id,
  or `none`). Written by the agent the owner worked with, at the end of the
  sitting. It is the evidence for HC-7 and the clock for HC-28.

## 9. Reflection

- **HC-31** On the owner's request, or on the "busy but not moving" signal,
  an agent produces a reflection brief (`reentry/RE-<n>.md`, `kind:
  reflection`) for a stated period, computed from impact fields:
  how much work and decision-making had each impact; which stages advanced
  and which stalled; how the intent itself moved. Reflection reads the same
  records; it MUST NOT require new ones.

## 10. Integration

- **HC-32** `<agent entry>` MUST tell every agent: check coherence signals
  (HC-28) and check before asking (HC-29). Snippet: `AGENT_POINTER.md`.
- **HC-33** If the project has a decision ledger, its entries gain the HC-12
  fields, and pending decisions are listed to the owner in HC-14 order.
- **HC-34** If the project has an agent handoff system, it stays as is. This
  structure is the owner's counterpart and shares files with it. It MUST
  also work with no agent handoff system present.
- **HC-35 — Machine checks (SHOULD, once volume makes them pay).** A
  preflight script verifies: every record parses (HC-2); every reference
  resolves; no `confirmed` INT or ST without a matching SIT record (HC-7);
  every inbox file has an IN record (HC-16); every pending owner-facing item
  has the HC-12 fields; and it reports HC-28 signals it can compute (gap
  length, unprocessed changes-intent items, impact mix since last sitting).

## 11. Adopting

- **HC-36 — New project.** Copy the templates to `<cdir>/`, write the origin
  INT entry from whatever started the project (a brief, an idea folder, the
  first conversation), add the pointer snippet, start.
- **HC-37 — Project already under way.** Reconstruct the timeline first:
  origin entry from the starting material; checkpoint entry for "now"; story
  map from the current state. All `derived`. Then run a first re-entry with
  the owner to confirm them.

## Acceptance (walked live, not judged by reading files)

Owner:
- **OS-1** After a gap of any length, within one sitting, I can say what the
  project is for and where it stands relative to that, and the record agrees.
- **OS-2** I get a frame (what / why / how / when) that lets me recall, and
  every directed question I ask is answered from the files.
- **OS-3** I am never asked about the project before I have the frame; the
  old picture and new directions are shown as equals.
- **OS-4** Every item put to me says how much it moves the intent; the
  biggest movers come first; I never have to look up an ID.
- **OS-5** I never receive raw changes.
- **OS-6** Thinking I do elsewhere has one place to land and comes back to me
  at the next re-entry, in the frame.
- **OS-7** I can see the intent at the start, at any checkpoint, and now,
  with the evidence each rests on.
- **OS-8** I can ask "are we actually moving?" and get an answer measured
  against the intent.
- **OS-9** A big new idea can become a sub-project built on top instead of a
  rival.

Agent:
- **AS-1** An agent recognises coherence signals and offers a re-entry.
- **AS-2** From files alone, an agent reconstructs the timeline with evidence
  and prepares the frame; only restatement and confirmation need the owner.
- **AS-3** No derived intent is ever presented as confirmed.
- **AS-4** No question reaches the owner that their earlier answers decide.

Adopting project:
- **AD-1** A new project adopts this from the kit in under an hour, with no
  knowledge of the origin project.
- **AD-2** A project under way adopts it starting from a reconstructed
  timeline.
- **AD-3** It works without an agent-side handoff system.

## Do NOT build

- No dashboard, app or web page of record; rendered views are derived.
- No automated drift check: it is a conversation by design.
- No notifications pushed at the owner; agents offer, the owner decides.
- No scoring of the owner.
- No derived intent presented as confirmed.
- No count cap on owner items; order by impact instead (HC-14).
