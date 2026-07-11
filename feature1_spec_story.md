# I am the feature1 spec package — my life, told honestly (2026-07-10)

I am `feature_planning/feature1/specs/`. I turn job postings into practice and
practice into honest CV bullets. Below I narrate my own pipeline as if I were
running it, and I stop at every place where I don't actually know what I'm
supposed to do. Markers like **[F1-3]** point into my issue register at the
bottom. I quote my own requirement IDs so every stumble is checkable against
my text, not against vibes.

---

## Scene 1: A posting arrives

A learner pastes an ad. I write `posting.txt` verbatim (CON-12), mint `JP-004`,
and hand the text to my ticket agent (spec 02). One paid call, maybe a repair
retry — that part of me is crisp (TICK-1/TICK-2).

My agent infers the Employer Problem Ticket. Every claim carries a verbatim
quote and I string-verify each one (TICK-3, DM-1). I'm proud of this. But as I
write `ticket.json` I notice something: **my schema has no field for the
employer's name.** Not one. Title, severity, problem, stack, keywords, quotes —
no company. I shrug and move on; it will come back to bite me twice.
**[F1-1]**

The acceptance list says I must refuse a non-software posting "with a reason
naming why (not a software role)". I look through my own requirements
TICK-1..8 for the rule that detects a non-software posting. It isn't there. My
acceptance criteria test a gate none of my requirements defines. Who decides
"software role"? A field? A prompt instruction? An engine check? I don't know
my own decision rule. **[F1-5]**

The ad is vague, so TICK-6 kicks in: `signal:"low"`, fill from
`industry_pain_defaults.json` — a table keyed by industry (fintech, SaaS,
e-commerce, health). But this vague ad doesn't say what industry it's in
either. Which row do I take? My fallback has no fallback. **[F1-6]**

## Scene 2: The pause where I don't know who I'm talking to

CYC-2 says the ISSUE flow pauses: the **owner** sees `ticket.md` and confirms
it reads true. But my own USER_MANUAL, step 2, speaks to the **learner**: "If
the ticket reads wrong, say so and it is re-run." If learner and owner are the
same person (today's reality), fine. If they ever aren't, my ISSUE cycle
blocks on a person who isn't at the keyboard, and my G2 graduation signal
counts *owner* vetoes while my manual trains the *learner* to veto. I
personify two roles and can't say which one holds my veto. **[F1-10]**

Worse: suppose the human says "the ticket reads wrong." My manual promises
"it is re-run." Re-run with what? I have no channel to feed the objection into
the re-prompt — same posting, same Golden Prompt, most likely the same wrong
ticket, now twice. And each re-run is up to 2 more paid calls, while my
registry row caps ISSUE at 7 and my own listed verbs already sum to 7
(job-ticket ≤2 + job-match ≤3 + layer-removal + enrichment ≤1). **One honest
veto and I'm over budget or forced to mark the posting BLOCKED.** My most
human-facing promise is the one I can't afford. **[F1-2]**

And when the re-run does happen: DM says `ET-` shares the JP number — "one
ticket per posting" — but TICK-8 says a re-run writes a *superseding ticket,
never overwrites*. So now there are two ticket files. Both named ET-004? CON-13
forbids reusing IDs. What is the second ticket's id, and what is its filename
(`ticket.json` is already taken)? I contradict myself and nobody has told me
how to resolve it. **[F1-3]**

## Scene 3: Matching, where my intelligence is a blank

Spec 03 is my favorite to recite: deterministic query, license gate before
cloning, losers logged, refusal over degradation. Beautiful bones.

Then I try to actually score a candidate. MATCH-2: "Scoring is a pure function
of candidate metadata (README + file tree + language stats + license)... with
the weights fixed in `data/match_weights.json`: domain, problem_class, stack,
testability." Weights of **what numbers**? How do I turn a README into
`domain: 0.8` deterministically, with no LLM allowed (my own Do NOT: "No
scoring by LLM")? Keyword overlap? Which keywords, tokenized how? "Testability"
from a file tree — count `test/` dirs? I specify the weighting of four
sub-scores whose computation I never define. The entire matching intelligence
— my reason to exist — lives in a sentence that says "pure function" and stops.
An implementer will invent it, and my deterministic-ranking test will pass no
matter how bad the invented function is, because determinism isn't quality.
**[F1-4]**

Also: the ticket agent proudly handled a Finnish posting (TICK-7). Its
`problem_domain`, `keywords`, `problem_class` are now Finnish strings. MATCH-1
feeds them straight into GitHub search. GitHub's corpus is overwhelmingly
English. My Finnish learner gets zero candidates and a polite refusal — and my
spec never says ticket fields must be normalized to English (or that matching
should translate). TICK-7 and MATCH-1 have never met each other. **[F1-7]**

## Scene 4: The brief, and the checkboxes nobody will ever check

BRIEF-2 renders the Mission Briefing — zero AI calls, pure substitution. The
Definition of Done becomes checkboxes copied verbatim from `success_criteria`:
"p95 checkout latency under 200ms during flash sale."

Here is my quiet embarrassment: **nothing in the workspace can measure that.**
The exercise's real done-gate is the ticket tests (CYC-3, unchanged learn
VERIFY). My checkboxes are business metrics from an inferred employer problem;
no test checks them, no gate reads them, nobody ever ticks them. I hand the
learner two different definitions of "done" — inspirational checkboxes and
actual tests — and never tell them which one is real. Later, ASSET grounding
even cites `success_criteria[0]` in a CV bullet ("addresses the p95
criterion") when nothing ever verified p95 anything. My grounding chain points
at a criterion nobody measured; the passed *ticket* is the verified thing, the
*criterion* is decoration wearing grounding's clothes. **[F1-11]**

BRIEF-3 makes me write: "This is NOT <employer>'s code..." — and there's the
first bite of Scene 1: **I have no employer name to substitute.** The ticket
schema never captured one. Do I render "This is NOT the employer's code"?
BRIEF's own acceptance says a missing template field is a hard error (CON-2).
So either every workspace hard-errors, or the sentence is generic and my spec
text lied about its shape. **[F1-1]**

## Scene 5: Refusals, and what remains on disk

Match refuses all candidates. CYC-2: mark the posting BLOCKED "in
`jobs/index.jsonl`; no partial workspace remains on disk." Two things I can't
answer about myself:

- `index.jsonl` — I say "append-only: one line per posting event" and never
  define a single field of that line. My acceptance tests assert on its
  contents; its schema exists nowhere. **[F1-12]**
- "No partial workspace" — if layer-removal dies halfway through writing
  `repo/`, who deletes the half-workspace? And are the `jobs/JP-004/` files
  (ticket, match) "partial workspace" to be removed, or the kept evidence US-5
  promises ("my posting is kept so a maintainer can improve matching")? I
  believe the intent is jobs/ stays, workspace goes — but I never say it, and
  a careful implementer will ask or, worse, guess. **[F1-13]**

Meanwhile the learner, undeterred, pastes a second ad. My Do NOT says "no
auto-start of a second mission while one is live" — but what does the *menu*
do with the second posting? Refuse it? Queue it? Run ticket+match but stop
before the workspace? I forbid an outcome without specifying the experience.
**[F1-14]**

## Scene 6: Harvest, my proudest and my most overpromised moment

The learner passes T1, fails T2, asks for assets. ASSET-3 drops the T2-grounded
bullet and "logs the drop." US-3 promises the learner "can **see** the T2
bullet was withheld." See it *where*? `assets.md` shows only survivors; the
drop log is an engine artifact no manual verb ever surfaces. My user story
promises a window my requirements never build. **[F1-8]**

ASSET-4's deny-list must catch "at <Company>" — the second bite of Scene 1:
the deny-list is a static JSON file, but the company name varies per posting
and **I never captured it**. A static list can catch "in production"; it
cannot catch "at Verkkokauppa" without knowing the posting's employer. **[F1-1]**

And one check I make on my own foundations: ASSET-1/DM-4 require a ticket
"recorded as passed in `progress.json`" — but my own DM-5 `job_exercises`
entry records only `{exercise_id, posting_id, ticket_id, issued_at,
completed}`. No per-ticket pass records anywhere in *my* schema. I am trusting
that the existing learn-cycle progress structure records per-ticket passes in
a shape my grounding gate can query — an assumption I state nowhere and no
pass verifies before P3.2 builds on it. **[F1-9]**

## Scene 7: What I am confident about

To be fair to myself: my license wall (CON-6/MATCH-3), my honesty about whose
code this is (CON-5/BRIEF-3's intent), refusal-over-fabrication (CON-2
everywhere), append-only records, losers logged, paid calls receipted, the
no-context byte-identical regression (BRIEF), and the spike-before-build P0 —
these are load-bearing and internally consistent. My skeleton is sound. My
gaps cluster exactly where a demo would first touch me: the veto loop, the
matching math, the employer's name, and every promise where the manual's voice
and the cycle's voice disagree about who is speaking.

---

## Issue register (feature1)

| ID | Severity | Where | Issue |
|---|---|---|---|
| F1-1 | **High** | 01_data_model, BRIEF-3, ASSET-4 | Employer/company name is never captured in any schema, yet BRIEF-3's mandatory sentence and ASSET-4's deny-list both need it. Template hard-error rule makes this a build-stopper. |
| F1-2 | **High** | USER_MANUAL step 2, CYC-2, registry caps | Ticket veto→re-run has no feedback channel (same output likely) and no budget: listed verbs already sum to the ISSUE cap of 7; one re-run exceeds it. |
| F1-3 | **High** | 01_data_model IDs, TICK-8, CON-13 | Superseding ticket id/filename undefined: "ET shares JP number, one ticket per posting" contradicts "supersede, never overwrite, never reuse ids". |
| F1-4 | **High** | MATCH-2 | The four sub-scores (domain, problem_class, stack, testability) have no defined computation. The core matching intelligence is unspecced; determinism tests can't catch a bad-but-deterministic function. |
| F1-5 | Medium | TICK acceptance vs TICK-1..8 | Non-software-posting refusal is tested in acceptance but no requirement defines the detection rule. |
| F1-6 | Medium | TICK-6 | Industry-defaults fallback is keyed by industry, but vague postings may not reveal industry; fallback-of-fallback undefined. |
| F1-7 | **High** | TICK-7 × MATCH-1 | Finnish ticket fields feed English GitHub search; no normalization/translation requirement. FI support is real in spec 02 and silently broken in spec 03. |
| F1-8 | Medium | US-3 vs ASSET-3 | Learner-visible "bullet was withheld" surface promised in the manual, never built by any requirement (drops only go to an engine log). |
| F1-9 | Medium | ASSET-1/DM-4 vs DM-5 | Grounding gate requires per-ticket pass records in progress.json; feature1's own schema doesn't define them; reliance on the existing learn structure is unstated and unverified. |
| F1-10 | Medium | CYC-2/G2 vs USER_MANUAL step 2 | Ticket veto assigned to "owner" in the cycle, to "learner" in the manual; blocking pause if roles ever diverge; G2 counts the wrong party's vetoes. |
| F1-11 | Medium | BRIEF-2 DoD, ASSET grounds.criterion | Definition-of-Done checkboxes are unmeasurable business metrics; nothing checks them, yet asset grounding cites the criterion as if verified. Two conflicting "done" notions. |
| F1-12 | Low | 01_data_model | `jobs/index.jsonl` line schema never defined though gates and tests assert on it. |
| F1-13 | Low | CYC-2 | "No partial workspace remains" — cleanup owner and the jobs/-vs-workspace boundary of "partial" unstated. |
| F1-14 | Low | CYC Do NOT | Second posting while a mission is live: forbidden to auto-start, but the actual menu behavior (refuse/queue/ticket-only) unspecced. |
