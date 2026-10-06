## RE-1 — re-entry after the 2026 funding hiatus
kind: reentry
date: 2026-10-05
gap_start: 2026-07-11
intent_before: INT-2
intent_after: INT-4
evidence: INT-1, INT-2, INT-3, I-1, I-2, I-3, I-4

Rules: incubating/human-coherence-intent-anchoring/kit/SPEC.md HC-20..HC-27.
First trial of the pattern. Prepared by claude-opus-5-5; owner steps
(questions, restatement, drift check, resolutions) are filled in during the
sitting. Never rewritten afterwards.

### Frame

**What.** You set out to make AI reason better by keeping heuristics
*outside* the model, in a library an agent can draw on. By July this had
become something specific: a growing library of short heuristics for your
AI coding agents, which they look up at the start of a task (INT-1 → INT-2).

**Why.** Your premise: humans aren't more rational than AI. They carry large
libraries of heuristics and are good at reading cues to pick one. AI can
put a rule into words the moment it sees it work, but forgets everything
between sessions. So: *AI articulates, you recognize and pass it through.*

**How.** Each heuristic is a small markdown file with a few "cue" phrases. A
local server (MCP) lets any agent search them, read them, and log whether
they helped. Agents propose new heuristics into a staging area; only you
move them into the live library. Five phases hand you less work only where
the logs prove you were rubber-stamping.

**When.**
- Before 2026-07-09: four AI-written reports on the idea (`idea/`), each
  pushing it further: weak model helped → strong model made auditable →
  knowledge graph, memory layers, self-discovery → feasibility check.
- 2026-07-09: the full spec set, owner manual and user stories written. The
  ambition was deliberately narrowed to what one person's usage can support.
- 2026-07-10: specs checked: 18 flaws found, none fixed yet. A persona-voiced
  rewrite of the specs found flaws better than dry text, so personas were
  adopted as a way to *check* specs. A proposal to make heuristics themselves
  persona-shaped was parked as a later experiment. You chose a separate repo
  for the actual build.
- 2026-07-11: everything committed; pause.
- 2026-09-08 → 2026-10-05: four documents from your other conversations.

**Where the project stood against that intent at the pause:**
1. Idea collected: **grasped**.
2. Design written down: **grasped**.
3. Design checked and corrected: **partial**. 18 flaws known, none fixed.
4. First working version (agents can look heuristics up): **open**. Not
   started; waits on stage 3.
5. Library grows from experience: **open**.
6. You hand over routine work: **open**.

Decisions waiting at the pause, in terms of the intent:
- Which of the 18 design fixes to make before building. Serves stage 3; two
  of them touch names that freeze once built.
- (Raised later, after the pause:) whether the new documents change what
  the project is for. That's this re-entry.

### Questions asked
None. After the frame the owner said: "good now I have recalled lets
proceed" (2026-10-05). The frame alone was enough to recall; no directed
questions were needed. (Trial evidence for "good memory, bad recovery".)

After seeing the moves, the owner asked (2026-10-05): "what are downstreams
and what are upstreams; group them; I need to know if there are really
competing directions or simply needs chronological ordering." Answer given:
the moves layer, with the July library as foundation (L1), stacks/personas
as structure (L2: moves 1, 4), learning (L3: move 5 + corpus growth),
rule-making as purpose (L4: move 2; top as a reason, late to build), the
persistent assistant as end goal / sub-project (L5: move 3), and spec
process as a side question (move 6). Verdict: mostly chronological; four
real choices, all about *how*: C1 selection (cue search vs contract
eligibility; layerable: search picks the stack, contracts inside), C2 what a
persona is (stacking order vs capacity-limited bundle; possibly both),
C3 spec process (amended vs single-cycle; pick one), C4 capturing the
owner's judgment (log distillation vs real-time interrogation; mostly
different targets). Caution: the foundation's file format should leave room
for contracts, ordering and persona membership now (defensive design).
**Trial finding:** HC-23 describes each move against the intent and the
pause position but not against the other moves. The owner needed the moves'
dependency structure (upstream/downstream, competing vs ordering) before
restating. The spec should require it.

### Moves
*(prepared; shown to the owner after they have the thread; no
recommendation before the restatement)*

Ordered by impact on the intent, largest first. Each is described against
INT-2 (the intent at the pause) and the position at the pause.

**Move 1: heuristics stack in a fixed order; a persona *is* a stacking order.**
(I-1, I-3 §1, I-4 §1)
- *Against the intent:* keeps "heuristics live outside the model, authored
  and corrected with you". Changes "short, independent heuristics found by
  keyword" into "ordered stacks where each heuristic has an input/output
  contract and a single dispatcher picks a stack". Changes the *why*: from
  "tacit knowledge, AI articulates" to "LLMs lose to a child on sample
  efficiency because humans crystallize heuristics into stacks".
  **Changes the intent.**
- *Against the position:* reopens stage 2 (data model and server design).
  Several of the 18 waiting fixes are about the current design and may no
  longer apply.
- *Against the origin:* close to the "reasoning pipelines" and knowledge
  graph in idea/gpt.md that the July specs cut.

**Move 2: the system's real target is your own rule-making.**
(I-3 §3–5, I-4 §1–5)
- *Against the intent:* changes the *for*: from "guidance for coding agents"
  to "eventually take over the architecture-level rules you make for all
  your projects", because agents have no heuristic for making rules. Adds
  "need = the gap between a project's spirit and its current state", and a
  check for when a *question* doesn't fit. Capture method: real-time
  interrogation of you, explicitly *not* review of past logs, which is partly
  at odds with the July plan of distilling heuristics from logs.
  **Changes the intent.**
- *Against the position:* no current stage covers it; it would add stages
  after stage 6, or a parallel track.

**Move 3: a persistent "person"-like assistant built on the heuristic system.**
(I-3 §6–7, I-4 §1)
- *Against the intent:* a new end goal, explicitly later-stage in your own
  words. The same assistant runs on a weak local or strong cloud model. Brings
  a drift problem (habits that keep growing after they stop paying off).
  ~~a design answer: you as the outside check for now, self-management
  later.~~ **CORRECTED 2026-10-06:** the goal is that the assistant develops
  its own executive faculty (imperfect, but its own); heuristic self-checks
  only catch *large* drift, so gradual drift needs scheduled reflection,
  giving three tiers: cheap daily self-check ("who am I" vs the situation),
  periodic wide-window reflection, external reference check. I-3 §7 holds
  both "surfacing data to you is sufficient for now" and "the actual goal is
  self-management"; the original summary picked the compiler's
  bootstrap-vs-end-state reading, and the owner's cross-check says the
  self-management correction is the owner's position.
  **Changes the intent** (adds an end goal).
- *Against the position:* touches nothing now; everything here needs the
  heuristic system first.

**Move 4: personas organize a growing corpus.** (I-2 Track A, I-3 §2, I-4 §1)
- *Against the intent:* keeps "a growing library, corrected by you". Adds
  personas as capacity-limited bundles of heuristics, chosen like hiring
  ("job post" → best-fit persona), several personas run in parallel, and
  "spawn the old and a new persona, keep the better". The corpus also grows
  from books, not only your conversations (I-4 §3 item 2).
  **Changes only the route**, if the library stays the core.
- *Against the position:* the July persona experiment (decision D-3) is the
  existing hook in stage 5; retrieval design in stage 2 would change.

**Move 5: heuristics move from deliberate to instinctive as they prove themselves.**
(I-1 §5, I-2 Track B; a fast decision-model product, I-3 §8, as one
possible implementation)
- *Against the intent:* keeps "trust is earned from logged evidence", which is
  the July phase ladder, applied per heuristic. Often-used, reliable
  heuristics fire directly; failing ones drop back to deliberate use.
  **Changes only the route.**
- *Against the position:* fits stages 5–6; needs a log of (situation →
  heuristic → outcome), which the July design already mostly records.

**Move 6: how specs are run.** (I-3 §4, described as already operational in
your other projects)
- *Against the intent:* single-cycle specs, rewritten fresh each cycle
  rather than amended. Every interaction needs a contract before it exists
  (hard stop). Anomalies go upstream. This repo's specs are the opposite:
  long-lived and amended.
  **Changes only the route** (process).
- *Against the position:* would change how stages 2–3 are maintained.

None of the four documents mentions the July specs or the coding-agent
library, so none says whether it replaces or extends them.

### Completeness check (2026-10-06, before the restatement)

The owner cross-checked the moves against the source conversations using a
second assistant (web Claude, which has those chats). Verified item by item
against I-1..I-4:

**In our files but left out of the moves (summary too compressed):**
spirit is never undefined, and the real failure is a *wrong* spirit (I-4);
spirit grows as possibility grows (I-3 §5); "need" means something different
in each project (I-3 §5); fit judgment as a solvable DSA-style problem,
question processed as a directed graph, where it stops is the diagnosis,
an ambiguous stop is fine (I-4 §3); execution reduces to yes/no chains but
rule-making cannot, since generating the options is itself rule-making
(I-3 §8, assistant-tagged); anomalies go upstream, local calls allowed within
the spirit (I-3 §4); persona conflicts settled by hierarchy and proximity
expertise (I-3 §2); the book-to-fiction "shape" method for picking personas
(I-3 §2); why books matter: agents can't see the heuristics in books because
"heuristic" isn't in their vocabulary (I-4 §3); individuation from scarcity
and usage frequency (I-3 §6); your shrinking involvement as the success
measure (I-3 §2); the fast decision model (I-3 §8); a quick self-heuristic
"what kind of project/person am I now" (I-3 insight 4, assistant reply).
Also move 3, corrected above.

**Not in this repo at all (source conversations never exported):**
- Sep 16: the project's main value is helping an agent be helpful *in the
  way a specific person defines helpful*. A purpose statement, and none of
  the six moves states it.
- Sep 29 "ants": every project that uses the corpus sends it tuning signals
  for free (pheromone reinforcement) [owner]; proposals [assistant]: reinforce
  whole stacks, weight owner corrections highest, decay rarely used
  heuristics but protect rare critical ones, cheap threshold gates for
  dispatch; four open problems: usage mistaken for success, attribution
  across stacks, scope leaking between projects, rare heuristics decaying.
- Sep 22: personality as a chain of heuristics running in a sequence of
  loops (the basis for a "person" built from heuristics); wanting heuristics
  about what the project itself *is*, not only how to do things.
- Edges (agent-loop chats): easy path as a path-selection heuristic at spawn
  time and at seams (Sep 29); plan-origin and sub-loops (Sep 28).

**Already received:** the two tagged handoff reports the cross-check
mentions are I-4 (the Oct 5 report) and the tagged reports inside I-3.

**Unresolved:** the cross-check dates the stack and two-track ideas to a
Sep 10 chat, but I-1 and I-2 are dated Sep 8 and 9 on disk.

**Trial findings:** (1) Processing (HC-17) compressed the sources into
moves and dropped many of the owner's own positions; the spec should require
every owner-stated item to be carried into some move or listed as set
aside. (2) An outside vantage point with access to the original
conversations caught both the omissions and a misread owner position: a
working "external reference check" for the processing step itself.

### Material added 2026-10-06 (fetched by the owner)

Registered and processed as I-4 (now october2026.md) and I-5. Of the items
the completeness check found missing:
- **Fetched:** Sep 16 purpose statement (I-5 insight 1, the owner's own
  words); Sep 29 "ants" report (I-5 insight 2); Sep 28 plan/loops report
  (I-4 insight 2); Sep 29 easy-path report (I-4 insight 3).
- ~~**Still missing:** from Sep 22, "personality is a chain of heuristics
  running in a sequence of loops" and "heuristics about what the project
  itself is". Neither appears in any file.~~ **Updated 2026-10-06T10:15:**
  the owner saved the rest of september2026.md (insight 6, the updated Sep 22
  report). "Personality is a chain of heuristics in sequence of loops" is now
  present as the owner's own question (I-3 insight 6 §6). Still not present
  as an owner statement: wanting heuristics about *what the project itself
  is*. The closest is an assistant reply proposing a quick self-heuristic,
  "what kind of project/person am I now" (I-3 insight 4).
- **New, not in any earlier material:** the owner's statement that managing
  irrelevant information is "one of the most important parts of the
  heuristic system" (I-5 insight 3).

Effect on the moves and layers:
- **New candidate purpose (changes the intent, possibly unifies it):** "the
  biggest gain is that the agent can answer 'how can I be helpful to this
  specific human in the way they define helpful'" (Sep 16). It fits INT-2's
  personal library (user-fact heuristics, profile kernel) and gives layers
  2–5 a common *why*. It sits above everything as the purpose.
- **Layer 3 (learning) gets a concrete mechanism:** the ants report's
  self-tuning corpus (traces, outcome signals ranked by trust, stack
  reinforcement, eligibility-based decay, persona lifecycle). Its
  three-phase bootstrap (hand-authored → assisted tuning → self-compiling)
  lines up with the July phase ladder. Its data model (heuristic, stack,
  persona, trace records) is exactly the "leave room in the foundation"
  question from the layering answer.
- **New requirement across layers 1–3:** managing irrelevant information.
  It touches persona capacity limits, decay and dormancy, scarcity-based
  access, and what gets logged at all.
- **Edge material (agent-loop design):** the plan/loops and easy-path
  reports are about how agent loops plan and adapt, which the owner marked
  as only partly relevant. Candidate: a separate track or sub-project that
  *uses* heuristics (easy-path is itself a heuristic), not part of this
  project's core.

### Moves, revised 2026-10-06 (after the completeness check)

Supersedes the "Moves" list above for the restatement; that list stays as
first shown. Ordered by impact; layers as in the dependency answer; still
no recommendation.

Purpose (above all layers):
- **M0 helpful in the way this person defines helpful** (I-5 insight 1,
  Sep 16, owner's words). Changes the intent: sharpens *For*; coding becomes
  one domain of it.

Changes the intent:
- **M1 stacks with contracts; persona = stacking order** (I-1, I-3, I-4). L2.
- **M2 rule-making as the target** + spirit/need, wrong-spirit and
  question-fit graph, books + vocabulary (I-3 §4–5, §9; I-4). L4.
- **M3 a person built from heuristics**: personality as a chain of
  heuristics in loops; individuation from scarcity; "what it is like" is
  a layer below and not needed; drift in three tiers; the goal is the
  assistant's own executive faculty (I-3 insight 6 §6–7). L5, sub-project.

Advances (new requirement):
- **M7 managing irrelevant information**, "one of the most important parts"
  (I-5 insight 3, owner, 2026-10-06). Cuts across L1–L3.

Changes only the route:
- **M4 personas organize the library**: capacity limits, hiring-style
  dispatch, hierarchy + proximity, spawn-both trials, lifecycle (I-2, I-3,
  I-5 insight 2). L2.
- **M5 learning: deliberate → instinctive, and a self-tuning library**:
  traces, outcome signals ranked by trust, stack reinforcement, decay with a
  protected floor, exploration (I-1, I-2, I-5 insight 2). L3.
- **M6 how specs are run** (I-3 §4). Side question.

Separate track (uses heuristics, not part of the core):
- **M8 agent-loop planning**: plan as a continuous process, success clause,
  easy path at spawn and seams (I-4 insights 2–3; owner: partly relevant).

Real choices (all about *how*): C1 selection (cue search vs contract
eligibility), C2 what a persona is, C3 spec process, C4 capturing the
owner's judgment; plus C5 whether M8 belongs in this project or beside it.

### Presentation correction (2026-10-06)

The owner rejected the compressed revised-moves view and asked for
"something as clear as" the first dependency answer. Re-presented with:
the layer diagram including the purpose; a reason for each position; the
verdict (ordering, with drift-checking "you now / self-management later"
also shown as ordering); five choices with "what conflicts / can it be
layered" columns, each using evidence from the new material; the
foundation-format caution made concrete (stack, persona, trace records;
scope; signal type; relevance).
**Trial finding:** a revised picture must keep the full explanatory
structure (why each position, what conflicts), not just updated positions,
and must not use bare move codes (HC-15 applies to labels like "M0" too).

### ~~Landscape survey (I-6, arrived 2026-10-06T11:43)~~ WITHDRAWN

**WITHDRAWN 2026-10-06 (owner): "we are currently dealing with what I
produced in the period of hiatus; we do not process this yet; do not
confuse."** I-6 is post-resumption work, outside this re-entry's window
(gap_start 2026-07-11 → resumption 2026-10-05). The section below and the
"C6" choice shown to the owner do not apply to RE-1. The picture that stands
is the "Presentation correction" view (purpose + layers 1–5, choices C1–C5).
**Trial finding:** re-entry needs a defined input window: the material from
the gap. Material arriving *during* the re-entry is registered but held,
not folded into the moves.


Adds to the picture: layers 1–3 (store, structure, learning) and the
persistent assistant already exist elsewhere in some form; the purpose
(person-defined helpfulness), rule-making/need, question fit,
capacity-limited personas with hierarchy, and real-time interrogation were
found nowhere. New real choice C6: build the foundation in-house or reuse
an existing base and build only the unclaimed layers. Survey limits: one
morning of web search, READMEs and abstracts only.

### What actually competes (2026-10-06, owner: "some appear to be competing only superficially due to how it's worded")

Re-examined C1–C5 against the sources:
- C1 selection: superficial. A July cue (DM-4: "what the situation looks
  like") and a stack's input contract describe the same thing at different
  granularity; the stack thesis's single dispatcher is itself a match step.
- C2 persona: superficial. "Stacking order" (I-1) is contrasted with *role
  labels*, not with bundles; capacity (how many) and order (how arranged) are
  two properties of one thing.
- C3 specs: superficial, different levels. The owner's own model: architecture
  rules persist (owner-made), task specs are fresh per cycle (agent-made). The
  July set mixes both levels.
- C4 capture: superficial. July's main capture is already in the moment
  (AGT-7 log_lesson when the user corrects); the owner rejects reviewing
  *his past decisions* for *his* reasoning, which July never proposed.
  Interrogating the owner is an addition, not a rival.
- C5 agent-loop planning: not a direction; a scope placement.
- The purposes (helpfulness, child-level general intelligence, rule-making,
  a person) do not compete: why it matters / what it is for / a capability /
  the fullest form.
**The one real conflict:** what a heuristic *is*. July: an independent unit,
found by cue and dropped into any task (02, 03). Stack thesis: position-bound;
"one more good heuristic without regard for stack position causes conflict
rather than improvement" and a misplaced one is a "position violation" that
fails silently (I-1 §2–3). July's retrieval does exactly what I-1 warns
against. It is also what the foundation's file format must decide.
**Trial finding:** the dependency view listed "choices" by surface wording;
the owner had to push for the real ones. Moves should be compared at the
level of the underlying concept, not their phrasing.

### Result: nothing competes (2026-10-06, owner correction)

Owner, on the "one real conflict" (independent vs position-bound
heuristics): "these are not competing; the stack can only exist when there
are lots of individual heuristics; we cannot stack nothing on top of
nothing." Individual heuristics are the material stacks are built from:
layer 1 → layer 2, i.e. ordering.
**Conclusion of the comparison:** no competing directions in the hiatus
material. Everything is one system in layers under one candidate purpose;
the open points are sequencing (what is for now) and scope (where
agent-loop planning lives).
**Trial finding:** the agent kept finding "conflicts" that the owner
dissolved as ordering, three times over. An agent comparing moves should
first test every apparent conflict for "is one the material or
precondition of the other?" before presenting it as a choice.

### Restatement
**Replaced by a derived draft, INT-4 (2026-10-06).** The owner asked whether,
on the evidence, they needed to answer "what is this project and what should
it become" at all. Answer: no. Their Q2 rule (intent derived from evidence,
owner confirms) and P9 (check before asking) already settle it, and the
evidence covers each element. The agent drafted INT-4 for the owner to
confirm or correct. **Trial finding (major):** HC-24 "restate" contradicts
the design's own Q2 answer; the step must be "agent drafts the intent from
evidence; owner confirms or corrects", with the owner asked only what the
evidence leaves open.

*(Earlier: the quote below is an owner CORRECTION about one heuristic, not a
restatement; misread at first, see below.)*

> this is not an purpose "purpose: helpful the way you define helpful." its
> an heurestics we need to create current llm want to be helpful in the core
> but helpful in context of what? they heurestics system answers this just
> like when group of friends interact we humans create heurestics to know
> what each of the group things as helpful similarly we want to give agents
> capability to express their desire to be helpful in a way that is useful
> to the human

Correction to the picture: "helpful the way you define helpful" is not the
purpose above the layers; it is a kind of heuristic the system must create
(content), learned the way friends learn what each other finds helpful.

~~Owner asked (2026-10-06): does this differ from the founding goal in idea/?~~
**WITHDRAWN 2026-10-06 (owner): "what I said was only about 1 heuristic the
project will create … how are you comparing 1 heuristic to the founding
goal?"** The agent treated the owner's example of one heuristic as a
restatement of the project's goal, then compared it with the founding goal:
a category error. The text below is struck in substance; the founding goal
(INT-1) is untouched by the owner's remark. **Trial finding:** the agent
must not promote an owner's example or correction into an intent statement;
when unsure whether a remark is about the whole project or one part, ask.
Struck text follows:
Answer given: yes in *goal*, same in *mechanism*. Founding (idea/deepseek.md
§1): "elevate the reasoning and output quality of a weak base LLM"; kimi:
systematize and improve reasoning. Now: agents express their built-in
desire to help in a way useful to the human; heuristics supply the context.
Founding takes cues from the task ("the environment is the user query");
now cues also come from the person. Drift label: **evolved** (capability →
usefulness to a person), already begun in July (user-fact heuristics,
profile kernel). Open for the owner: founding goal stands with usefulness
added, or usefulness replaces it with better reasoning as a means.


### Drift check
Owner's test (2026-10-06): show evidence only if the intent changed
significantly, or if the hiatus insights deviate the road from the current
state to the intent; "currently this does not appear to be the case".
Checked against the records:
- **Intent:** kept. The founding goal (INT-1) is contradicted by nothing;
  July (INT-2) narrowed *where to start*; the hiatus material widens the same
  system by layers (all apparent conflicts were ordering, per owner). The
  only intent-level correction: person-defined helpfulness is one heuristic,
  not the goal. Label: **kept, grown by additions.**
- **Road:** unchanged. Current state: ST-3 partial, ST-4 open. Next stops:
  fix the design flaws (D-6), then the first working version. Hiatus
  material lands on ST-5/ST-6 and later layers (impact records I-1..I-5);
  the ants report's first step (log traces in one project) matches ST-4.
- **Touches the current step without redirecting it:** leave room in the
  foundation format for stacks, personas, traces, scope (owner's
  defensive-design rule); irrelevant-information management starts in
  layer 1 (I-5 insight 3).

### Resolutions
- Intent: INT-4 confirmed by the owner (SIT-1): intent kept, grown by
  additions, road unchanged. The owner's message is read as the
  confirmation; the owner may object.
- ~~Agent-loop planning: beside the project (inferred; not separately
  confirmed).~~ **Settled 2026-10-06, no decision needed:** the owner asked
  whether it is still an issue; by the owner's test it changes neither the
  intent nor the road. Its relevant parts (easy path; "did the difficulty
  teach anything or only cost more") are heuristics and enter the library
  as content; the rest is agent-loop work that would *use* the library.
  (INT-4's "Not / beside" line reads the same in effect; confirmed entries
  are not edited, HC-3.)
- No new owner decisions created. The two additions to the current step go
  into the design work of ST-3/ST-4 when it resumes.
- Pending decisions re-ordered by impact on INT-4: D-6 (design fixes) first,
  as the next stop on the road; D-7 (direction documents vs specs) is
  answered in substance by this re-entry; D-8 and D-10 are housekeeping,
  untouched by the intent.

### Trial outcome
First run of the pattern. Re-entry completed 2026-10-06. Findings for the
spec, in the order found: inter-move dependencies (HC-23); processing must
account for every owner-stated item (HC-17); an outside vantage point
checks processing; revisions keep their explanatory structure and avoid
bare codes; re-entry has an input window (gap material only); test
apparent conflicts for material/precondition relations before presenting
choices; never promote an owner's example into an intent; **restate
becomes "agent drafts from evidence, owner confirms" (HC-24, major)**; and
the owner's closing test: involve the owner only when evidence shows a
significant intent change or a deviated road.
