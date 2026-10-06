# Human coherence structure using intent anchoring — keep the human in charge in step with a project others keep changing

> **STATUS: INCUBATING — not yet admitted to innovations/.** Designed
> 2026-10-05; first trial completed 2026-10-06; its nine findings were
> folded into the kit the same day. The revised kit is not yet tested. Per innovations/CONTRIBUTING.md §1 it moves
> into innovations/ only after real use with dated evidence. See "Proven in".

## What it is
The owner's counterpart of agent handoff. Agents stay coherent by re-reading
files; the human in charge cannot. This pattern keeps the owner coherent by
anchoring everything that reaches them to the project's **intent** (what it
is for):
- an **intent timeline** reconstructed from evidence and confirmed by the
  owner;
- a **story map** of stages, each marked against the intent;
- an **impact** label on every owner-facing item (changes the intent /
  advances / route only / untouched), which orders what the owner sees;
- a **re-entry** procedure after a gap: process changes → give a
  what / why / how / when frame → owner recalls and asks → show new
  directions in the intent's own terms → only then ask the owner → drift
  check → resolve;
- an **inbox** for the owner's thinking elsewhere, **coherence signals**
  that prompt agents to offer re-entry, and **reflection** over the same
  records ("are we actually moving?").

## Problem it solves
After a gap (hiatus, busy month, funding pause), the owner no longer knows
where the project stands. Pending decisions are coherent to agents but float
free of any story the owner remembers. The owner's own idea has moved in
other conversations, and nobody can say whether it still matches what the
project records. As agents multiply, change outruns the owner's attention,
and a project can be very busy without moving toward its goal. Agent-side
handoff docs don't help: they are written for agents and compare against the
last session, not against the intent.

## How to use it
1. Copy `kit/templates/*` to `<cdir>/` (default `coherence/`) and paste
   `kit/AGENT_POINTER.md` into the agent entry file.
2. New project: write the origin intent entry from whatever started the
   project. Project under way: have an agent reconstruct the timeline (origin
   from the starting material, checkpoint for now) and the story map, all
   marked *derived*, then run a first re-entry with the owner to confirm
   them (`kit/SPEC.md` HC-36, HC-37).
3. From then on, agents give every owner-facing item its stage / impact /
   why, order by impact, register outside material in the inbox, and offer a
   re-entry when they see coherence signals.
4. The owner reads `kit/OWNER_GUIDE.md` once. Re-entry and reflection run on
   request.
5. Run it by hand first. Build machine checks (HC-35) only when doing it by
   hand starts to hurt.

## Fits projects like
Any project where the person in charge is not in it every day: owner + AI
agents, side projects with long gaps, funded work with pauses, projects that
many agents feed. The more agents, and the longer the gaps, the more it
carries. Less useful for a short project the owner works on continuously.

## Proven in
**First trial done; findings folded into the kit 2026-10-06 (the revised
kit is untested).** Trial
2026-10-05/06, origin project: re-entry after a ~3-month hiatus. Step 1
reconstructed the intent timeline (origin, checkpoint at the pause,
evolution) and processed five documents of the owner's hiatus thinking;
the owner recalled the project from the frame alone, with no questions
needed. The re-entry closed with the intent confirmed as kept, grown by
additions, road unchanged. It also produced nine findings, all owner-forced
corrections. The major one: the "restate" step contradicted the owner's own
rule; it must be "agent drafts the intent from evidence, owner confirms",
and the owner is involved only when evidence shows a significant intent
change or a deviated road. Others: describe moves against each other
(upstream/downstream); account for every owner-stated item when processing;
an outside vantage point (a second assistant with the source chats) caught
omissions; keep revised views fully explained, with no bare codes; re-entry
has an input window (gap material only); test apparent conflicts for
material/precondition relations first; never promote an owner's example
into an intent. Full record: the origin project's coherence/reentry/RE-1.md.
Folded as: HC-17 (account for every owner statement), HC-17a (outside
check), HC-23 (moves against each other; conflict test), HC-24 (draft,
don't ask to restate), HC-25 (two verdicts), HC-38 (input window), HC-39
(when to involve the owner), and, from the same day's follow-up, HC-40
(times read from the clock: the agent's estimated timestamps drifted ~3 h
and the gap check exposed it) and HC-41 (the session opening branches to
the frame on a long gap).

Design evidence, from the origin project (a spec
repo for a heuristic harness for AI coding agents; owner + AI agents; 2026):
- Trigger: the project resumed 2026-10-05 after a ~3-month funding hiatus.
  The owner reported having "no idea at what stage the project is"; four
  documents from the owner's other conversations had arrived during the
  pause; the intent at the time of the pause was recorded nowhere the owner
  could use. An agent-side handoff system, built the same day, kept *agents*
  coherent and did nothing for the owner.
- The design was shaped by the owner in a human-facing draft before any
  agent-facing text was written. Four owner corrections changed it
  materially. The most important: an agent-written first draft asked the
  owner to restate the project *before* seeing anything; the owner rejected
  it ("a disoriented user cannot answer anything related to the project;
  humans don't work like that"). That produced the frame-first order and the
  "good memory, bad recovery" principle. Also: the intent is reconstructed
  from evidence, not written fresh; no count cap, order by intent impact;
  sub-projects built on top instead of forks; check the owner's earlier
  answers before asking.
- Planned first trial: re-entry on the origin project's own hiatus (origin
  intent from its idea folder, checkpoint at the pause, evolution from the
  four outside documents). Admission to innovations/ follows that trial's
  written evidence, including what failed.

Absorbs two ideas from innovations/README's Incubating list: "measure
against the fixed intent" (impact labels, reflection) and "two reads for one
workspace" (story map states plus alternatives). If this pattern is admitted,
both graduate with it.

## Kit (deployable files in `kit/`)
- `kit/SPEC.md` — agent-facing requirements HC-1..HC-37, acceptance stories,
  do-not-build list.
- `kit/OWNER_GUIDE.md` — the plain-language guide for the human in charge.
- `kit/AGENT_POINTER.md` — snippet for the agent entry file.
- `kit/templates/` — `intent.md`, `story-map.md`, `inbox-INDEX.md`,
  `reentry-brief.md`, `owner-log.md`.

Pairs with: handoff-discipline (agent side; shares files), decision-ledger
(gains stage / impact / why fields), root-cause-laddering (a W4 "busy but not
moving" reflection is a natural place to start a ladder).
