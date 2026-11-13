It was accidental. The template change came later in our conversation, when you asked whether main effort belongs in the top-level intent, and I never carried it back into the report. The report was also missing the other fixes we worked out: neutral examples, non-hierarchical layouts and the per-project table. Some things we learned while reviewing your two intents are also general enough to include. Here is the full updated report.

# Using Bungay's *Art of Action* Process in Agentic Workflows

## 1. The core problem: three gaps

Bungay (building on Clausewitz and von Moltke) argues that plans fail because of three gaps between plans, actions and outcomes. All three appear directly in agentic systems.

| Gap | Human organization | Agentic workflow |
|---|---|---|
| **Knowledge gap**: what we'd like to know vs. what we actually know | Leaders plan without full information | The work is briefed before anyone knows what the agent will find |
| **Alignment gap**: what we want people to do vs. what they actually do | Instructions get misread or followed too literally | The agent completes the literal task but misses its purpose, or optimizes the wrong thing |
| **Effects gap**: what we expect our actions to achieve vs. what they actually achieve | Actions have unexpected consequences | The output meets every check but misses the point, or fixing one thing breaks another |

**The usual response makes things worse.** People fill the knowledge gap with more information, the alignment gap with more detailed instructions, and the effects gap with more controls. In agentic terms that means longer prompts, more rigid step-by-step plans and more validation rules. The result is a brittle system that breaks the moment reality differs from the plan.

**Bungay's three principles:**

| Gap | Principle |
|---|---|
| Knowledge gap | **Limit direction to defining and communicating the essentials** (the intent) |
| Alignment gap | **Let each level work out how it will achieve the intent**, and explain that back (backbriefing) |
| Effects gap | **Give freedom to adjust actions within boundaries**, judged against the intent |

He calls the result **directed opportunism**: everyone knows where the effort is going, and everyone is free to take advantage of what they find on the way.

## 2. The key concept: intent

Intent is **what** must be achieved and **why**. It is never **how**.

- **What** is the end state or outcome.
- **Why** is the purpose, which comes from the intent one level up.

The *why* is the part people most often leave out, and it is the part that does the work. When a plan breaks, the *what* may stop making sense, but the *why* still tells the actor which way to adapt.

**Test of a good intent:** if every detailed plan turned out to be wrong, would this statement still tell someone what to do?

### Intent vs. main effort

Main effort is **not part of the intent**. In the doctrine Bungay draws on, intent is the *what* and *why*. The main effort is designated separately, as part of how effort is focused to achieve that intent. Bungay treats it as essential to strategy, because strategy means choosing, but it is a separate element.

The separation matters in practice:
- **Intent is stable.** It should hold even if every plan fails.
- **Main effort moves.** It shifts as the work progresses.

If they sit in the same block, every shift in main effort looks like a change of intent, or the main effort goes stale because nobody wants to edit the intent.

### Intent statement template

```
INTENT          (stable)
  Achieve:      <end state, observable>
  In order to:  <purpose — links to the intent above>
  Definition:   <any term the intent depends on that agents could read
                 differently — optional>

BOUNDARIES      (stable, or stated with how they loosen)
  Must:         <non-negotiables an agent could actually break>
  Must not:     <forbidden actions / out of scope — "(none confirmed)"
                 is a valid entry>

SUCCESS SIGN    (stable — a check, never the goal)
  <how we recognize the end state, including the quality it must keep
   and how the result is attributed to our work>

MAIN EFFORT     (current — revised as work progresses)
  <what wins trade-offs right now>

TRACE           (optional)
  <where each line came from — decisions, specs, the owner's statements>
```

Keep it short. If the intent needs a page, it has turned into a plan.

## 3. Nesting: intent flows down the layers

Each layer takes the intent from the layer above, adds its own *what*, and passes the result down. Every layer's *why* is the *what* of the layer above it.

```
Project intent:   Achieve A, in order to P
  Phase intent:   Achieve B, in order to A
    Task intent:  Achieve C, in order to B
      Step:       Do D,      in order to C
```

**Practical rule:** every brief should end in an "in order to…" chain that reaches the top-level purpose. If a task can't be completed honestly with that chain, it is drifting from the intent.

**Two levels up:** Bungay recommends that each actor understand the intent of the level above *and* the level above that. An actor that knows only its immediate task can't tell when completing the task literally would defeat the larger goal.

**Each layer sets its own main effort** under the shared intent. The intent passes down unchanged in meaning, while the main effort can differ from layer to layer.

### Layer structures

Intent has to travel along whatever structure the workflow has:

| Structure | What a "layer" is | Two levels up means | Backbrief goes to |
|---|---|---|---|
| **Hierarchy** (orchestrator → sub-agents) | A level of delegation | The parent's intent and the grandparent's | The parent agent or a human |
| **Single-agent loop** | A phase of the same agent's work | The current phase's intent and the overall goal's | Itself, as a written self-check before each phase |
| **Spawned loops** (loops that create or call other loops) | Each spawned loop | The intent of whatever spawned it, and what spawned that | The spawning loop |

## 4. The process loop

### Step 1: Plan (top level)

- State the intent: *what* and *why*.
- Set **boundaries**: what must and must not happen.
- Define the **success sign**, and how it could be gamed.
- Name the current **main effort**.
- Leave out the *how* unless a specific method is truly required.

### Step 2: Brief (handing work down)

The brief contains:
- the intent of this layer and the two layers above it
- the boundaries
- the current main effort
- the context the receiver needs and can't easily find on its own

The brief does **not** contain step-by-step instructions, unless the method is itself a boundary.

### Step 3: Backbrief (the receiver explains back before acting)

The receiver states:
- what it understands the intent to be, in its own words
- what it plans to do
- why that plan serves the intent
- what it would do if it finds X or Y (the main risks or unknowns)

Backbriefing is the main check on the alignment gap. It catches misunderstanding **before** effort is spent. Work above the project's review threshold gets its backbrief reviewed before execution. Below the threshold, the receiver writes the backbrief as a self-check.

**Red flag:** if the receiver's *why* doesn't mention the top-level purpose, the intent hasn't landed. Fix the brief, not the receiver.

### Step 4: Execute with freedom inside boundaries

- The receiver chooses its methods.
- When reality differs from expectations, it adapts toward the intent, not toward the original plan.
- If adapting would require crossing a boundary or changing the *what*, it escalates instead of improvising.

### Step 5: Check effects against intent, not against the plan

The question is "did we reach the intended end state, for the intended purpose?", not "did we do what we said?"

- Finished steps, passing checks and produced files are evidence, not success.
- Check the success sign directly, including its quality condition.
- Confirm that the result came from the work, not from something else that changed.
- Note any side effects that work against the higher intent.

### Step 6: Adjust and re-brief

Findings move up the layers.
- If the findings shift priorities, update the **main effort**. This is routine.
- If they show the intent is wrong at some level, that level revises the intent and re-briefs everything below it. This is rare, because intent is stable but not frozen.

## 5. Escalation rules

| Situation | Action |
|---|---|
| The plan doesn't work, but the intent is still reachable | Adapt the method and report it afterwards |
| The intent is reachable only by crossing a boundary | Stop and escalate |
| The intent itself looks wrong or impossible given new information | Stop, report the findings and propose a revised intent |
| Two parts of the work conflict | Follow the current main effort and flag the conflict |
| The action is irreversible and the right path is ambiguous | Prepare everything, lay out the decision and stop |

## 6. Failure modes and Bungay's remedies

The remedies come from the book. The agentic applications are adaptations, since Bungay didn't write about agents. Failure mode 3 isn't a named topic in the book; its remedy follows from his principles rather than from a specific technique he named.

| # | Failure mode | Bungay's remedy | Agentic application |
|---|---|---|---|
| 1 | **Instructions without intent**: long procedural prompts break on the first surprise | **Limit direction to defining and communicating intent.** Say what and why, not how. More detail doesn't close the knowledge gap; it makes plans brittle. | Replace procedural prompts with an intent statement. Keep a method only if it is truly a boundary. |
| 2 | **Intent without a *why***: the receiver games the success sign | **Intent always includes purpose.** The *why* lets subordinates adapt correctly when the situation changes. | Every brief ends with an "in order to…" chain up to the top purpose. Reject briefs without one. |
| 3 | **Success sign treated as the goal**: the check gets optimized instead of the end state | Follows from **judging action by intent, not by the plan.** A measure is evidence of the end state, not the end state itself. | Label the success sign as a check. Give it a quality condition and an attribution method. In review, ask "was the purpose served?", not only "did the check pass?" |
| 4 | **Too many priorities**: every trade-off becomes an arbitrary choice | **Main effort.** Name the one thing that matters most right now, so every trade-off has a default answer. Strategy means choosing. | Each layer names one current main effort. When work conflicts, follow it and flag the conflict. |
| 5 | **No backbrief**: misunderstandings are found only after the work is done | **Backbriefing.** The receiver explains the intent back in their own words, along with their plan. This closes the alignment gap before effort is spent. | Short backbrief: understood intent, plan, why the plan serves it, main risks. Reviewed before work above the threshold. |
| 6 | **Intent lost on the way down**: subtasks succeed locally and fail together | **Nested intent and the briefing cascade.** Each level states its own intent derived from the level above and knows the intent two levels up. | Every brief carries its own intent plus the two layers above it, whatever the layer structure. |
| 7 | **Plans frozen after facts change**: work continues on a plan that's no longer valid | **Freedom to adjust within boundaries,** together with the duty to report up. Plans are hypotheses; intent is what stays fixed. | Adapt the method toward the intent, report findings upward, update the main effort, and re-brief when the intent changes. |
| 8 | **Micro-control as a fix for the effects gap**: more validation layers make the system slower and more brittle without making it more aligned | Bungay's central warning: the instinctive fixes (more information, more detailed instructions, more control) **widen the gaps.** The cure is clearer intent and more freedom within boundaries. | When results drift, fix the intent and boundaries first. Add checks only for real boundaries, not as a stand-in for clarity. |

### The pattern behind the table

| Principle | Addresses |
|---|---|
| **Knowledge gap:** limit direction to essentials | Failure modes 1, 2, 4 |
| **Alignment gap:** each level works out the how and backbriefs it | Failure modes 5, 6 |
| **Effects gap:** freedom to adjust within boundaries, judged against intent | Failure modes 3, 7, 8 |

**Diagnosing a new failure mode:** find which of the three gaps it comes from. The matching principle is usually the remedy.

## 7. Reviewing an intent statement

These defects came up repeatedly when real intent statements were reviewed. Check for each one before using an intent.

| Defect | Symptom | Fix |
|---|---|---|
| **Scope in the *why*** | "In order to" contains where the work happens ("X is the first test case") | Move the scope to the Achieve or its own line. The *why* is purpose only. |
| **Belief posing as a boundary** | The Must states a view ("treat A as different from B") rather than something that can be broken | Rewrite it as a breakable rule ("never accept B as evidence of A") |
| **Boundary that contradicts the purpose** | A stable boundary rules out what the *why* is for (e.g. "owner approves everything" in an intent about needing the owner less) | Mark it as current, or state how it loosens and who decides |
| **Inferred boundary** | A boundary nobody with authority actually set | Confirm it or remove it. "(none confirmed)" is better than a guess. |
| **Uncheckable boundary** | The wording doesn't match anything a receiver does (e.g. a rule about "heuristics that run commands" when agents run commands) | Phrase it around actions the receiver can recognize |
| **Gameable success sign** | The sign can be met by failing (e.g. "involvement declines" when it declines because work quality dropped) | Add the quality the result must keep |
| **Unattributed success sign** | The sign shows the end state but not that the work caused it | Add an attribution method (before/after check, use→outcome record) |
| **Definition clashes with a boundary** | The definition's wording overlaps what a boundary excludes | Say which part is the thing being judged |
| **Undefined key term** | A term in the main effort or boundary only the writer understands | Define it, or use the words of the Achieve |
| **Repetition** | The same rule appears in several sections | Keep it in the one section where it belongs |
| **Clutter** | Provenance tags or notes inline make the intent hard to read | Move them to TRACE |
| **Method inside the Achieve** | The Achieve names both the end state and the means | Ask whether success by another means would count. If yes, move the means to Main effort or Boundaries. If proving the means is the point, keep it. |

## 8. What each project must define

The process is generic. These items are not, and each project fills them in:

| Item | Question to answer |
|---|---|
| Top-level intent | What are we achieving or proving, and in order to what? |
| Definitions | Which terms could agents read differently? |
| Boundaries | What must never happen? Which boundaries are permanent, and which loosen? |
| Success sign | How will we recognize the end state, what quality must it keep, how could it be gamed, and how is it attributed? |
| Current main effort | If two things conflict right now, which wins? |
| Layer structure | Hierarchy, phases of one agent, or spawned loops? |
| Review threshold | Which work needs its backbrief approved before it runs? |
| Escalation target | Who or what receives escalations: a human, an orchestrator or a parent loop? |

## 9. Minimal checklist per layer

**Before handing work down** (knowledge gap):
- [ ] Does the brief state *what* and *why*?
- [ ] Does the *why* connect to the intent two levels up?
- [ ] Are the boundaries explicit, breakable and confirmed?
- [ ] Does the success sign have a quality condition and an attribution method?
- [ ] Is the current main effort named?
- [ ] Have I left out the *how* where it isn't essential?

**Before executing** (alignment gap):
- [ ] Have I backbriefed (to the reviewer or to myself in writing)?
- [ ] Does my plan's *why* match the brief's *why*?
- [ ] Do I know when to escalate instead of adapting?

**After executing** (effects gap):
- [ ] Was the end state reached, rather than just the steps or the check?
- [ ] Can the result be attributed to this work?
- [ ] Do any side effects work against the higher intent?
- [ ] Does what I learned change the main effort, or the intent?

## 10. One-line summary

**Tell every layer what to achieve and why, let it decide how, have it explain its plan back before acting, and judge results against the purpose rather than the plan.**