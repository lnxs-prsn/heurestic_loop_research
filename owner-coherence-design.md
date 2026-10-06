# Human coherence structure using intent anchoring

*Keeping the human in charge coherent with a project that others keep changing.*

> **Status 2026-10-06:** design done; agent-facing spec + kit at
> incubating/human-coherence-intent-anchoring/; first trial completed (see
> coherence/reentry/RE-1.md). This document is the design record and is not
> updated further.

**Design draft 3.2 · 2026-10-05 · for the owner to shape · nothing here is built**
*(Pattern folder name: `human-coherence-intent-anchoring/`. All design
questions are answered; see the revision log at the end.)*

This is the *what / why / how* of a new, generic structure, written for the
human in charge to read and argue with before anyone writes the agent-facing
version. It is meant for any project; examples from the project that invented
it are marked **(origin example)**.

**How to take part:** section 8 holds what is still open. Answer in any form,
or challenge anything else in the document.

---

## 1. The problem in one paragraph

Agents stay coherent because every session reads the project's files before
acting. The human in charge has no equivalent. After a break (a hiatus, a busy
month, a funding gap), the owner no longer knows what stage the project is at.
The decisions waiting for them read as coherent to an agent but float free of
any story the owner remembers. Meanwhile the owner's own thinking kept moving
in other conversations, so it is no longer clear whether the idea in their head
and the idea the project records are still the same idea. As more agents work
on the project, the volume of change grows past what one person can follow,
and all of this gets worse.

**(origin example)** Project paused 2026-07-11 for funding reasons and resumed
2026-10-05. Meanwhile four documents from other conversations arrived,
reframing the project as "persona stacks" and "two tracks". The owner does not
remember what the intent was when the pause began; the project began from an
`idea/` folder. Four decisions are pending, each phrased in IDs
(`D-6: apply F-1..F-18`). The owner said: "I have no idea at what stage the
project is".

## 2. Why it happens — the core idea

There are **three** things that must agree, and today's tooling looks at only
part of one gap between them:

```
   THE OWNER'S HEAD          THE INTENT                   THE ACTUAL STATE
   (the idea as it is   ⟷   (what the project is    ⟷   (what exists: files,
    in your mind today)      for, and why)               code, decisions)

        gap A: drift of the idea           gap B: drift of the work
        nobody checks this                 agents check this partly, and
                                           only against last session's report
```

- **Gap A — the idea drifts.** The owner *forgets* the thread and *keeps
  thinking* elsewhere, both at once. Neither shows up in the files.
- **Gap B — the work drifts.** Agents change things step by step, each step
  checked against the previous one. A project can move a lot without moving
  toward its goal, and nobody notices.

Three facts about people shape the whole design:

1. **Good memory, bad recovery.** The owner has not lost the project; they
   have lost the way back into it. Given the right frame (*what* it is, *why*,
   *how*, *when*), they recall most of it, or they can ask precise questions
   about the rest. Re-orientation is cue-giving, not re-teaching.
2. **A disoriented person cannot be asked cold.** Questions come after the
   frame, never before.
3. **The intent is often not written down anywhere, even in the owner's
   head.** It has to be *reconstructed* from evidence: the material the
   project started from, what it had become by a given date, and the outside
   material that shows where the thinking went. The owner then confirms or
   corrects the reconstruction.

And one fact about projects: **progress means movement in the context of the
intent, not movement.** A project can be very busy and stand still. Everything
reaching the owner is therefore weighed by how much it moves the intent.

## 3. What goes wrong, concretely

| # | Failure | What it looks like | (origin example) |
|---|---|---|---|
| W1 | **Lost thread** | Owner can't say where the project stands | "no idea at what stage the project is" |
| W2 | **Orphaned decisions** | Owner asked to decide things without seeing what they do to the intent | D-6 "apply F-1..F-18" |
| W3 | **Silent idea drift** | The owner's idea moved elsewhere and the record never learned it, or the record moved while the owner didn't | 4 outside documents vs the specs |
| W4 | **Busy but not moving** | Lots of decisions and work, little of it moving the intent | not yet measurable; nothing classifies work by intent |
| W5 | **Agent-shaped orientation** | Files written for agents (IDs, evidence chains) the owner can't use | HANDOFF.md, decisions.md |
| W6 | **Lost intent** | Nobody, owner included, can state what the project was for at a given time | intent at the pause: unknown |

## 4. Design principles (the "why" behind each part)

- **P1 — Reconstruct the intent from evidence; the owner confirms it.** The
  intent is derived from what exists: origin material, the project's state at
  a given time, and outside material since. Every reconstructed statement
  cites its evidence and stays marked *derived* until the owner confirms or
  corrects it.
- **P2 — Give cues, not lectures.** Re-orientation hands the owner a frame
  (*what / why / how / when*) and lets them recall or ask. The owner's
  questions set the depth.
- **P3 — Frame before asking, neutrally.** The owner is asked nothing about
  the project before they have the frame. The old picture and each proposed
  direction are shown side by side as equals, with no recommendation until
  the owner has reacted, so the familiar version doesn't win by default.
- **P4 — One frame of reference.** Everything is described against two fixed
  points: the **intent** and **where the project stood relative to it**.
  New material is translated into the language of the intent, not presented
  in its own vocabulary.
- **P5 — Weigh everything by intent impact.** Every item reaching the owner
  says how much it moves the intent. Items are taken biggest-impact first.
  The aim is not many moves in the project; it is many moves in the context
  of the intent. Items that don't touch the intent don't compete for the
  owner's attention.
- **P6 — Process before presenting.** Raw changes are never handed to the
  owner. Each one is first digested into *what* it changes, *why*, and *how*
  it intends to move the project.
- **P7 — Build on, don't fork.** When a new idea outgrows the current intent,
  the first question is whether it is a layer that needs the current project
  underneath it. It then becomes a sub-project built on top, with its own
  intent, rather than a rival.
- **P8 — Records that serve more than one purpose.** The same records that
  re-orient the owner also let them reflect: is the project actually moving
  its intent, or is effort going into things that don't?

- **P9 — Check before asking.** Before putting any question to the owner,
  an agent checks whether the owner's earlier answers already decide it. If
  they do, the agent applies that answer, says which earlier answer settled
  it, and lets the owner object. Only questions the owner's past answers
  don't cover reach the owner.

## 5. What we would build — eight parts

Everything is plain files, like the agent side. No app.

**Part 1 — The intent timeline.** A dated series of intent statements: what
the project is for, for whom, what success looks like, and what it is
deliberately not. Three kinds of entry:
- **origin**: reconstructed from the material the project started from;
- **checkpoint**: reconstructed from what the project had become at a given
  date (e.g. when a pause began);
- **evolution**: what the outside material since then proposes.

Each entry cites its evidence and is marked *derived* or *confirmed by the
owner (date)*. Entries are appended, never edited. Sub-projects (P7) get their
own timeline, linked to the intent they build on.
**(origin example)** origin = `idea/` folder; checkpoint at the pause =
specs, BUILDLOG, decisions as of 2026-07-11; evolution = the four outside
documents.

**Part 2 — The story map.** The project's path from intent to done, as an
ordered list of stages in plain language (e.g. *understand the problem →
design → first working version → daily use → grows by itself*). Each stage
says what it contributes to the intent and is tagged **grasped / partial /
open**, with one line of evidence. A stage can also list the alternatives
still alive there, because an "open" stage is often crowded with undecided
options rather than empty. Like the intent, the stages are first derived from
evidence, then confirmed by the owner (Q6).

**Part 3 — Intent impact on every item.** Every owner-facing item (a
decision, an incoming idea, a piece of finished work) carries three
plain-language fields:
- **stage**: where it sits on the story map;
- **impact**: one of **changes the intent** / **advances toward the intent**
  / **changes only the route** / **does not touch the intent**;
- **why**: one line, in the language of the intent.

For example, not "D-6: apply F-1..F-18" but "Stage: design · advances toward
the intent · fixes 6 known flaws in the blueprint before building; deferring
turns them into rebuild costs."

**Part 4 — Re-entry.** The owner's counterpart of an agent's start ritual,
run when the owner asks or when coherence signals appear (Part 7).
1. **Process (agent, beforehand; P6).** Every change since the owner last
   engaged is digested into what / why / how and given its intent impact
   (Part 3). The intent timeline gets its checkpoint and evolution entries
   (Part 1).
2. **The frame (P2).** Short and cue-shaped: *what* the project is for,
   *why*, *how* it was going about it, and *when* things happened, from the
   origin through the pause to now. Then where the project stood relative to
   the intent at the pause (P4).
3. **Recall and ask.** The owner recalls, and asks directed questions. The
   agent answers each one from the files, citing them. This continues until
   the owner says they have the thread.
4. **The proposed moves.** New material is grouped into moves and shown in
   the frame (P4), biggest intent impact first (P5). Each move is shown
   against the intent (what it keeps, changes or drops; intent change or
   route change) and against the position at the pause (stages reopened or
   advanced, decisions affected). Moves are shown side by side, neutrally
   (P3).
5. **Restate.** Only now does the owner say what the project is and should
   become.
6. **Drift check.** The agent compares the restatement with the intent
   timeline and each move: **kept / evolved / adopted move / rejected move /
   new / dropped**.
7. **Resolve.** For each difference: update the intent, keep the old, park
   it as an open question, or make it a sub-project built on top (P7). The
   result is a confirmed intent entry, plus any decisions it creates; pending
   decisions are re-ordered by their impact on the resulting intent.

**Part 5 — Ordering by intent impact.** There is no cap on how many items
reach the owner. Instead, everything is ordered by how much it moves the
intent (P5):
1. items that **change the intent**: always the owner's call, first;
2. items that **advance toward the intent**, biggest first;
3. items that **change only the route**: grouped, decided together;
4. items that **do not touch the intent**: handled by agents under rules the
   owner approved; logged, never pushed at the owner.

When many items have the same effect, agents merge them before they reach the
owner.

**Part 6 — The inbox for outside thinking, and its processing.** The owner
will keep thinking about the project in other conversations, with other
agents, in notes. That is the main source of gap A, and also its best
evidence. There is one place to drop such material; every item is registered
on arrival, then processed (P6) and given its intent impact. Arriving is not
adopting: processed material is presented at the next re-entry as a proposed
move.
**(origin example)** `insights_from_other_conversations/` + its INDEX is the
agent-side half of this.

**Part 7 — Coherence signals.** Re-entry happens when the owner asks, or when
an agent sees signs that the owner may have lost the thread and offers it.
Signals (the agent offers; it never forces):
- the owner's instructions or questions contradict the confirmed intent, or
  reopen things already settled;
- the owner can't place a decision put to them;
- outside material has piled up that changes the intent and hasn't been
  through a re-entry;
- a long run of work or decisions with little intent impact (W4);
- the intent timeline holds competing unconfirmed versions;
- a long gap since the owner last engaged. A one-line log of each owner
  sitting makes this measurable.

**Part 8 — Reflection.** Each re-entry leaves a dated brief, and every item
carries its intent impact. Together they let the owner reflect at any time:
- how much of recent work and decision-making moved the intent, and how much
  didn't;
- which stages are advancing and which have stalled;
- how the intent itself has moved over time.

The trigger is the owner's suspicion ("this doesn't seem to be going
anywhere") or a W4 signal. No new records are needed; reflection is another
way of reading the same ones (P8).

## 6. How it feels — three walkthroughs

*(Illustrations of the intended experience. The numbers and outcomes are
invented to show the shape and are not predictions.)*

**A. Coming back after three months.** Before you sit down, an agent has
processed everything that changed since you last looked. It has also
reconstructed the intent: what it was at the start (from the material the
project began with), what it had become when you paused, and where the four
new documents want to take it. You open the project and it says: *"It's been
86 days. Here is the frame."* One screen: *what* the project was for, *why*
you started it, *how* it was going about it, and *when* each part happened.
Then where the project stood against that intent when you paused, stage by
stage.

Most of it comes back. You ask: *"Why did we decide to build it as a server?"*
The agent answers from the files and shows you where. You ask two more
questions, then say you have the thread.

Then: *"Since then, 4 documents from your other conversations arrived. They
pull the project in two directions. Here they are, biggest effect on the
intent first."* Side by side, in the intent's own words:
- *"Move 1 — personas as fixed stacks of heuristics. Keeps 'grow heuristics
  from experience'; changes 'retrieve the right heuristic by cue' into 'a
  dispatcher picks a stack'. **Changes the intent.** Reopens design; two of
  the four waiting decisions would no longer apply."*
- *"Move 2 — keep the library, use personas to organize it. Keeps the whole
  intent. **Changes only the route.** Adds one design step."*

Neither is recommended. Only now: *"What is this project, and what should it
become?"* You answer. The drift check shows what you kept, what you adopted,
and one idea that appears nowhere yet. You decide that personas are a layer
that needs the heuristic library underneath it: Move 1 becomes a
**sub-project built on top**, with its own intent, to start once the base
exists. The base intent is confirmed with one addition, and the four waiting
decisions are re-ordered by impact on it. Two turn out to be moot.

**B. A normal week with ten agents.** You receive no stream of messages. When
you sit down: *one* item changes the intent (yours to decide, first); *four*
advance toward it, biggest first; *six* route changes, grouped into one
decision; *112* actions that don't touch the intent, handled under rules you
approved and logged if you ever want them.

**C. Reflection.** A month later the project feels slow. You ask for a
reflection. It shows that most decisions in the last month changed only the
route or didn't touch the intent, and that the "first working version" stage
hasn't moved. The project was busy but not moving. You redirect.

## 7. How it fits with what exists

- **Handoff discipline** (in innovations/) keeps *agents* coherent; this keeps
  the *owner* coherent. They share the files.
- **Decision ledger** (in innovations/) gains the Part 3 fields; its entries
  become ordered by intent impact.
- **Two incubating ideas** in innovations/README are absorbed: "measure
  against the fixed intent" (P4, P5, Part 8) and "two reads for one workspace"
  (Part 2's tags plus alternatives). If this pattern is proven, both graduate
  with it.
- **(origin example)** The agent-side system built on 2026-10-05 (decision
  ledger, intake register, DIRECTION.md) supplies files Parts 3, 6 and 1 use.
  DIRECTION.md would be replaced by the intent timeline.

## 8. Settled questions

All nine questions are answered; the revision log records each answer and
what it changed. Two notes:
- **Name (Q1).** *Human coherence structure using intent anchoring*, folder
  `human-coherence-intent-anchoring/`. The name states the purpose (keep the
  human coherent) and the mechanism (anchor everything to the intent), so an
  agent reading only the name knows what the pattern is for.
- **Story map (Q6).** The stage list and its grasped / partial / open marks
  follow the same rule as the intent (P1): agents derive them from the files
  with evidence, and the owner confirms or corrects them at re-entry. Rough
  draft for the origin project: idea collected (grasped) → specs written
  (grasped) → specs sharpened (partial: 18 flaws found, none fixed) → first
  working version (open) → daily use (open) → grows by itself (open).

## 9. How we'll know it works (acceptance stories)

Walked live, never judged by reading the files (the project's M-15 rule).

**Owner**
- **OS-1** After a gap of any length, within one sitting, I can say what the
  project is for and where it stands relative to that, and the record agrees
  with me.
- **OS-2** I get a frame (what / why / how / when) that lets me recall, and
  every directed question I ask is answered from the files.
- **OS-3** I am never asked about the project before I have the frame. The
  old picture and the new directions are shown as equals.
- **OS-4** Every item put to me says how much it moves the intent, and the
  biggest movers come first. I never have to look up an ID.
- **OS-5** I never receive raw changes; each arrives digested into what / why
  / how.
- **OS-6** When I think about the project somewhere else, I have one place to
  put it, and it comes back to me at the next re-entry, in the frame.
- **OS-7** I can see the intent as it was at the start, at any checkpoint, and
  now, and what evidence each version rests on.
- **OS-8** I can ask "are we actually moving?" and get an answer measured
  against the intent.
- **OS-9** A big new idea can become a sub-project built on top of the
  current one instead of a rival to it.

**Agent**
- **AS-1** From files and the owner's behaviour, an agent can recognise
  coherence signals and offer a re-entry.
- **AS-2** From files alone, an agent can reconstruct the intent timeline,
  citing evidence, and prepare the frame. Only the restatement and the
  confirmation need the owner.
- **AS-3** An agent never presents a derived intent as confirmed.

**Adopting project** (the generic test)
- **AD-1** A brand-new project adopts this by copying a kit and filling
  placeholders, in under an hour, with no knowledge of the origin project.
- **AD-2** A project already under way can adopt it, starting from a
  reconstructed intent timeline.
- **AD-3** It works without the agent-side handoff system, though better with
  one.

## 10. Deliberately not building (now)

- No dashboard, web page or app: plain files first. A rendered view can come
  later as a *view* over the files.
- No automated drift check. It is a conversation by design.
- No notifications pushed at the owner. Agents offer re-entry when they see
  signals; the owner decides.
- No scoring of the owner.
- No derived intent presented as confirmed (P1).

## 11. What happens after you've shaped this

Scope is settled (Q9): all eight parts, run by hand first, tooling later.
The reason is defensive design: a coherent whole that can be fixed later
beats ad-hoc fixes that are locally good but generally bad.

1. Design questions are settled. You may still challenge anything.
2. I write the agent-facing version (numbered requirements, file formats) and
   the generic kit templates.
3. **Trial on this project's hiatus:** reconstruct the intent timeline
   (origin from `idea/`; checkpoint at the pause from specs, BUILDLOG and
   decisions; evolution from the four outside documents, read in full), then
   run re-entry with you.
4. What worked and what failed is written up as evidence. Then the pattern
   goes into `innovations/human-coherence-intent-anchoring/`, with its kit,
   per the toolbox's admission rule.

---

## Revision log

- **Draft 2 (2026-10-05), owner correction to §6.** Draft 1 had the owner
  restate the project *before* seeing anything ("ask before you show"), to
  keep the old text from overwriting the evolved idea. The owner rejected
  this: *"the user that is disorientated cannot answer anything related to
  the project — they barely remember anything meaningful; humans don't work
  like that."* Order reversed: process → give back the project at the pause →
  show proposed moves → then ask. The anchoring concern was kept as a
  presentation rule (neutral, side by side).
  Lesson worth keeping for the eventual pattern: **the first draft of an
  owner-facing design, written by an agent, assumed the owner works like an
  agent: answers from memory on demand. The owner caught it in one reading;
  that is why the design is human-facing first.**
- **Draft 2.1 (2026-10-05), owner addition to §6.** The pause picture is the
  intent plus where the project was *in the context of* that intent, not a
  list of stage states.
- **Draft 2.2 (2026-10-05), owner addition to §6.** Proposed directions are
  presented in the context of the original intent and of the position at the
  pause, in the language the project began with (now P4).
- **Draft 3 (2026-10-05), owner answers to Q1–Q9.**
  - Q1: name must be generic; options re-offered (still open).
  - Q2: the intent is *reconstructed* from evidence (origin material, state
    at the pause, outside material since), not written fresh: the owner does
    not remember it either. → P1, Part 1 is now an intent timeline.
  - Q3: "humans have good memory but a bad recovery system": give a
    what / why / how / when frame; the owner recalls or asks directed
    questions. → P2, Part 4 steps 2–3.
  - Q4: re-entry when the owner asks, or when what the agent sees suggests
    the owner may have lost coherence. Time/volume thresholds dropped as
    triggers; time gap kept as one signal. → Part 7.
  - Q5: no count cap; order by how much an item moves the intent, biggest
    first. "We don't want lots of moves in the project; we want lots of moves
    in context of the intent." → P5, Parts 3 and 5, new failure W4.
  - Q6: unclear; re-asked with an analogy (still open).
  - Q7: dated series, but usable for wider purposes such as project
    reflection (are we deciding things that don't move the intent?). → P8,
    Part 8, walkthrough C.
  - Q8: case by case, but the usual answer is a sub-project built on top of
    the current one (personas need the heuristic system first), not a new
    project. → P7.
  - Q9: all parts, run by hand first: something coherent to fix later
    instead of locally-good, generally-bad ad-hoc fixes.
- **Draft 3.1 (2026-10-05), owner answers to Q1 and Q6.**
  - Q1: option A, but phrased so the name says what it is for: *human
    coherence structure using intent anchoring*
    (`human-coherence-intent-anchoring/`).
  - Q6: the question was unclear to the owner ("who is the author of what
    has happened so far, or what context do I need, in relation to what?").
    Re-explained with this project's draft stage list; settled by applying
    the Q2 rule (derived by agents with evidence, confirmed by the owner).
    Lesson: a design question the owner can't parse is usually not a real
    owner decision. Apply the owner's existing rule and say so.
- **Draft 3.2 (2026-10-05).** Owner asked why Q6 existed at all. Answer: it
  was written in draft 1, when the owner was assumed to write the intent and
  stages; the owner's Q2 answer settled it, but draft 3 carried it forward
  without re-checking. Added P9 (check the owner's earlier answers before
  asking) so the structure itself prevents this.
