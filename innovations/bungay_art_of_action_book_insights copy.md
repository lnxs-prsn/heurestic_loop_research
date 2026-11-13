insight 
"
# Using Bungay's *Art of Action* Process in Agentic Workflows

## 1. The core problem: three gaps

Bungay (building on Clausewitz and von Moltke) argues that plans fail because of three gaps between plans, actions and outcomes. All three appear directly in agentic systems.

| Gap | Human organization | Agentic workflow |
|---|---|---|
| **Knowledge gap**: what we'd like to know vs. what we actually know | Leaders plan without full information | The orchestrator writes a task before it knows what the agent will find in the code, data or docs |
| **Alignment gap**: what we want people to do vs. what they actually do | Instructions get misread or followed too literally | The agent completes the literal task but misses its purpose, or optimizes the wrong thing |
| **Effects gap**: what we expect our actions to achieve vs. what they actually achieve | Actions have unexpected consequences | The tests pass but the feature doesn't work, or a fix breaks something else |

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

### Intent statement template

```
INTENT
  Achieve:      <end state, observable>
  In order to:  <purpose — links to the intent above>
  Main effort:  <the one thing that matters most if trade-offs arise>

BOUNDARIES
  Must:         <non-negotiables>
  Must not:     <forbidden actions / out of scope>

SUCCESS SIGN (a check, not the goal)
  <how we recognize the end state>
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

**Practical rule:** every agent prompt or task ticket should end in an "in order to…" chain that reaches the top-level purpose. If an agent's task can't be completed honestly with that chain, the task is drifting from the intent.

**Two levels up:** Bungay recommends that each actor understand the intent of the level above *and* the level above that. An agent that knows only its immediate task can't tell when completing the task literally would defeat the larger goal.

## 4. The process loop

### Step 1: Plan (orchestrator / top level)

- State the intent: *what* and *why*.
- Identify the **main effort**, the one thing that wins if trade-offs come up.
- Set **boundaries**: what must and must not happen.
- Leave out the *how* unless a specific method is truly required.

### Step 2: Brief (handing work to an agent)

The brief contains:
- the intent of this layer and the two layers above it
- the main effort
- the boundaries
- the context the agent needs and can't easily find on its own

The brief does **not** contain step-by-step instructions, unless the method is itself a boundary.

### Step 3: Backbrief (agent explains back before acting)

The agent states:
- what it understands the intent to be, in its own words
- what it plans to do
- why that plan serves the intent
- what it would do if it finds X or Y (the main risks or unknowns)

Backbriefing is the main check on the alignment gap. It catches misunderstanding **before** effort is spent. For expensive or irreversible work, the orchestrator reviews the backbrief before execution. For cheap work, the agent can backbrief to itself as a written self-check.

**Red flag:** if the agent's *why* doesn't mention the top-level purpose, the intent hasn't landed. Fix the brief, not the agent.

### Step 4: Execute with freedom inside boundaries

- The agent chooses its methods.
- When reality differs from expectations, the agent adapts toward the intent, not toward the original plan.
- If adapting would require crossing a boundary or changing the *what*, the agent escalates instead of improvising.

### Step 5: Check effects against intent, not against the plan

The question is "did we reach the intended end state, for the intended purpose?", not "did we do what we said?"

- Passing tests, finishing steps or producing a file is evidence, not success.
- Check the success sign directly.
- Note any side effects that work against the higher intent.

### Step 6: Adjust and re-brief

Findings move up the layers. If what was learned changes the intent at some level, that level re-briefs everything below it. Intent is stable but not frozen.

## 5. Escalation rules

| Situation | Agent action |
|---|---|
| The plan doesn't work, but the intent is still reachable | Adapt the method and report it afterwards |
| The intent is reachable only by crossing a boundary | Stop and escalate |
| The intent itself looks wrong or impossible given new information | Stop, report the findings and propose a revised intent |
| Two parts of the intent conflict | Follow the main effort and flag the conflict |
| The action is irreversible and the right path is ambiguous | Prepare everything, lay out the decision and stop |

## 6. Failure modes and Bungay's remedies

The remedies come from the book. The agentic applications are adaptations, since Bungay didn't write about agents. Failure mode 3 isn't a named topic in the book; its remedy follows from his principles rather than from a specific technique he named.

| # | Failure mode | Bungay's remedy | Agentic application |
|---|---|---|---|
| 1 | **Instructions without intent**: long procedural prompts break on the first surprise | **Limit direction to defining and communicating intent.** Say what and why, not how. More detail doesn't close the knowledge gap; it makes plans brittle. | Replace procedural prompts with an intent statement. Keep a method only if it is truly a boundary. |
| 2 | **Intent without a *why***: the agent games the success sign | **Intent always includes purpose.** The *why* lets subordinates adapt correctly when the situation changes. | Every brief ends with an "in order to…" chain up to the top purpose. Reject briefs without one. |
| 3 | **Success sign treated as the goal**: the check gets optimized instead of the end state | Follows from **judging action by intent, not by the plan.** A measure is evidence of the end state, not the end state itself. | State the success sign separately from the intent and label it as a check. In review, ask "was the purpose served?", not only "did the check pass?" |
| 4 | **Too many priorities**: every trade-off becomes an arbitrary choice | **Main effort.** Name the one thing that matters most, so every trade-off has a default answer. Strategy means choosing. | Each brief names one main effort. When parts of the intent conflict, the agent follows the main effort and flags the conflict. |
| 5 | **No backbrief**: misunderstandings are found only after the work is done | **Backbriefing.** The receiver explains the intent back in their own words, along with their plan. This closes the alignment gap before effort is spent. | Agent produces a short backbrief: understood intent, plan, why the plan serves it, and the main risks. The orchestrator reviews it before costly or irreversible work. |
| 6 | **Intent lost on the way down**: subtasks succeed locally and fail together | **Nested intent and the briefing cascade.** Each level states its own intent derived from the level above and knows the intent two levels up. | Sub-agent briefs carry their own intent plus the two layers above it, not just the local task. |
| 7 | **Plans frozen after facts change**: agents carry out a plan that's no longer valid | **Freedom to adjust within boundaries,** together with the duty to report up. Plans are hypotheses; intent is what stays fixed. | Agents adapt their method toward the intent, report findings upward, and the affected level re-briefs. If the intent itself looks wrong, the agent escalates. |
| 8 | **Micro-control as a fix for the effects gap**: more validation layers make the system slower and more brittle without making it more aligned | Bungay's central warning: the instinctive fixes (more information, more detailed instructions, more control) **widen the gaps.** The cure is clearer intent and more freedom within boundaries. | When results drift, fix the brief's intent and boundaries first. Add validation layers only for real boundaries, not as a stand-in for clarity. |

### The pattern behind the table

Every remedy comes from one of the three principles:

| Principle | Addresses |
|---|---|
| **Knowledge gap:** limit direction to essentials | Failure modes 1, 2, 4 |
| **Alignment gap:** each level works out the how and backbriefs it | Failure modes 5, 6 |
| **Effects gap:** freedom to adjust within boundaries, judged against intent | Failure modes 3, 7, 8 |

**Diagnosing a new failure mode:** find which of the three gaps it comes from. The matching principle is usually the remedy.

## 7. Minimal checklist per layer

**Before handing work down** (knowledge gap):
- [ ] Does the brief state *what* and *why*?
- [ ] Does the *why* connect to the intent two levels up?
- [ ] Is there one main effort?
- [ ] Are the boundaries explicit?
- [ ] Is the success sign labelled as a check, not the goal?
- [ ] Have I left out the *how* where it isn't essential?

**Before executing** (alignment gap):
- [ ] Have I backbriefed (to the orchestrator or to myself in writing)?
- [ ] Does my plan's *why* match the brief's *why*?
- [ ] Do I know when to escalate instead of adapting?

**After executing** (effects gap):
- [ ] Was the end state reached, rather than just the steps or the check?
- [ ] Do any side effects work against the higher intent?
- [ ] Does what I learned need to go up the layers and trigger a re-brief?

## 8. One-line summary

**Tell every layer what to achieve and why, let it decide how, have it explain its plan back before acting, and judge results against the purpose rather than the plan.**
"
