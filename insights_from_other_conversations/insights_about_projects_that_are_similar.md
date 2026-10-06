insight 1
this helps us to see if we need to build everything from zero or could we trial out some parts from already existing parts 
"
Heuristics project in the wider landscape
Oct 6, 2026 · @How Do You Compare With Gpt And Deepseek
Purpose
This report places Said's heuristics project against what already exists, so the project agent can reason about which direction to take. It is input for a decision, not the decision itself.
Two kinds of claims appear below, and they should not be mixed:
• [Said] marks positions Said stated in his own conversations. These are settled design decisions or beliefs.
• [Proposed] marks suggestions made by Claude. Said has not adopted them; treat them as options to test with him.
Everything about outside projects comes from READMEs, abstracts and blog posts read on 6 October 2026, not from running their code.
Bottom line
The infrastructure layer of the project is already crowded; the purpose layer is not. Building custom storage, logging or skill graphs would be reinventing the wheel. What nobody seems to have built is the part Said treats as the point.
Already exists (reuse or learn from):
• Heuristics stored outside the model and corrected by a human.
• Libraries that learn from use: logging, reinforcement, decay, pruning.
• Ordered skill graphs with contracts between skills (research stage).
• Routing a task to a persona, sometimes learning from performance.
• Persistent assistants with identity and memory.
• Deliberate-to-automatic conversion, in cognitive architectures such as ACT-R.
Not found anywhere (the project's own ground):
• Being helpful to one person in that person's own definition of helpful.
• Need as the gap between a project's spirit and its current state, and taking over architecture-level rule-making.
• Checking whether a question fits before answering it.
• Personas as small, capacity-limited bundles of heuristics, chosen like hiring and ordered by hierarchy.
• Capturing a person's judgment by real-time interrogation rather than log review.
[Proposed] stance: build the unclaimed layer on top of an existing base, and borrow the learning mechanics from published work rather than inventing them.
The landscape
Existing work falls into six clusters. Most of it is from 2025–2026, and the skill-file format (SKILL.md) has become a shared standard across agent tools.
Cluster
What it does
Key examples
Maturity
Hand-written skill libraries
Fixed workflows with triggers, steps, excuse rebuttals and verification
addyosmani/agent-skills (25 skills, 4 reviewer personas, routing evals)
Production, widely used
Libraries learned from experience
Extract heuristics from successful and failed runs, retrieve them for new tasks
ExpeL, ACE playbooks, Metacognitive Reuse, SkillRL
Research
Rules corrected by humans
Each accepted review comment becomes a versioned rule with scope and provenance
Microsoft behavioral rules paper; pro-workflow; self-improving-skills
Production in small deployments
Ordered skill graphs
Skills as nodes with interfaces; edges carry order, compatibility and fallbacks; weights learn from use
ASG-SI, SE-GoS, cognee-skills
Research plus one open-source library
Persona routing
Pick a persona per request; some learn which persona suits which work
Smythe, AgentHistoric (archived), WonderMr/Agents
Small open-source projects
Persistent person-like assistants
Long-lived agents with identity, memory, skill learning and periodic consolidation
Letta Code, Vellum assistant
Open source, actively developed
A seventh, older source sits outside AI tooling: cognitive architectures such as ACT-R and Soar. They modeled how deliberate rules become automatic decades ago (production compilation, chunking) and how rules compete by utility.
The six moves against existing work
Moves 1, 4, 5 and 6 overlap heavily with existing work; moves 2 and 3 are mostly open ground. The move numbers follow the project agent's own list.
Move
Closest existing work
Overlap
What existing work lacks
1. Ordered stacks with contracts, one dispatcher
ASG-SI, SE-GoS
High (research)
No tool to install; no persona layer above the graph
2. Real target is Said's rule-making; need = spirit gap; question-fit check
None found
Low
Everything: all tools assume the question is right and the rules are given
3. Persistent person-like assistant, weak or strong model
Letta Code, Vellum
Medium
Self-management and drift detection; identity built from heuristic stacks rather than memory blocks
4. Personas organize the library like hiring
Smythe, AgentHistoric
Medium
Capacity limits, hierarchy and proximity expertise, spawn-both trials, books as a source
5. Deliberate to instinctive as heuristics prove themselves
ACT-R, Metacognitive Reuse (distills to weights)
Medium
No agent tool promotes and demotes rules in a library
6. Specs written fresh each cycle, contract before every interaction
General spec-driven practice
Low relevance
This is Said's working method, not a market question
Two of Said's ideas the move list does not yet carry also map here:
• [Said] The project's biggest value is letting an agent answer how to be helpful to this specific person, in the way that person defines helpful. No project found targets this; tools remember preferences, which is narrower.
• [Said] Every project using the library sends it free tuning signals, like ant pheromones. SE-GoS and cognee-skills implement this kind of reinforcement, so it is buildable.
What remains unclaimed
Five ideas have no counterpart in anything found, and they share one trait: they are about what the heuristics are for, not how they are stored.
1. Person-defined helpfulness. [Said] The agent learns what helpful means to a specific person. Existing personal assistants store preferences and facts; none frames the goal as the person's own definition of helpful.
2. Need and rule-making. [Said] Need is the gap between a project's spirit and its current state; spirit grows as possibility grows; each project needs its own heuristics for what need means. The end goal is an agent that makes architecture-level rules. Every tool found takes the rules as given.
3. Question fit. [Said] A question is processed as a directed graph against the heuristic stack; where it stops is the diagnosis, and an ambiguous stop shows which part of the graph to improve. The real failure is a wrong spirit, not an undefined one. All tools found assume the question is well posed.
4. Capacity-limited personas with hierarchy. [Said] Personas are deliberately small because humans reach complexity with few heuristics. Conflicts resolve by hierarchy and proximity expertise. Existing persona routers have flat, fixed personas.
5. Real-time interrogation. [Said] Said's own recognition is captured as it happens, with corrections demanded in the moment, because after-the-fact review produces invented reasons. Every learning system found works from logs after the fact.
The Microsoft rules paper names unbounded growth and multi-team scope as open problems, needing hierarchy or namespaces. Idea 4 is a direct answer to a problem others have already hit.
Lessons and warnings
Existing work has already hit several problems the project will meet. Each row is a finding from outside work and what it implies here.
Finding
Source
Implication for the project
Append-only playbooks grow until they bloat the context; one study capped ACE at 100 entries
ACE as evaluated in 2603.16843
Supports capacity-limited personas; pruning or consolidation must be designed in from the start
Repeated graph-learning rounds plateau, then make retrieval worse
SE-GoS
Continuous reinforcement from every project may degrade the library; test for this early
Insights extracted without a human can include hallucinated generalizations, and a wrong rule loaded every session amplifies errors
Microsoft rules paper
Keeps Said's correction role essential in early phases
Specific rules were followed more reliably than general ones
Microsoft rules paper
Heuristic contracts should be concrete; vague heuristics may not fire
Plain vector retrieval misses prerequisite chains between skills
SE-GoS
Independent evidence for Said's stack thesis over keyword lookup
Two rules that fire one after another often merge into one faster rule
ACT-R production compilation
A tested model for move 5: promote whole stack segments, not single heuristics
Personas can improve alignment but hurt accuracy, depending on task type
PRISM, via Hugging Face papers
Persona choice should be tested per task type, not assumed beneficial
[Proposed] The ACT-R row is the strongest single reading recommendation before designing promotion and demotion.
Direction options
All four options below are [Proposed]; none has been chosen by Said. They differ mainly in how much is built versus reused, and which unclaimed idea goes first.
Option
What it means
Gains
Costs and risks
A. Build the full stack in-house
Own storage, logging, graph, personas, learning
Full control; fits Said's provider-agnostic preference
Months spent on solved problems before reaching the unclaimed layer
B. Purpose layer on an existing base
Use SKILL.md as the heuristic format; Letta or cognee for persistence and learning; build personas, need and fit-check on top
Fastest route to the unclaimed ideas; inherits a standard other tools read
Dependence on outside projects; their models may not match stacks with contracts
C. Question-fit check first
Build the directed-graph fit test against a small hand-written stack, with labeled cases
Narrow and testable; Said already treats it as a solvable DSA-style problem
Delays persona and learning work; needs a labeled case set
D. Person-defined helpfulness first
Start from the project's stated main value: learning one person's definition of helpful, through real-time interrogation
Targets the clearest gap in the market
Hardest to measure; success criteria not yet defined
Options B, C and D combine: B is about how to build, C and D about what to build first.
The July plan of distilling heuristics from logs sits close to what ExpeL and the skill repos already do. Said's later position favors real-time interrogation over log review, so the two need reconciling before any capture work starts.
Open questions for the project agent
These need Said's answer before a direction can be fixed.
[ ] Build or reuse: does provider-agnostic design rule out depending on Letta or cognee, or only on model providers?
[ ] Which goes first: question fit (option C) or person-defined helpfulness (option D)?
[ ] How is "helpful in the person's own definition" measured, so progress on it can be tested?
[ ] Does the July log-distillation plan stay, become secondary, or yield to real-time interrogation?
[ ] Should heuristics adopt the SKILL.md format, or does a stack with input/output contracts need its own format?
[ ] How will the library avoid the SE-GoS pattern, where repeated reinforcement first plateaus and then hurts?
[ ] Which outside items get read first: ACT-R production compilation, SE-GoS, the Microsoft rules paper, or Letta Code's skill learning?
Limits and sources
This survey covered roughly ten web searches and a few page reads on 6 October 2026. Projects were judged from READMEs, abstracts and blog posts; none was installed or run. Closed commercial products and non-English work were barely covered, so "not found" means not found in this search, not proven absent.
Said's positions come from his conversations of 10 September (heuristics as building blocks), 16 September (helpfulness as the main value), 22 September (context layer, need, persistent assistant), 29 September (ant mechanisms) and 5 October (question fit).
Sources
• addyosmani/agent-skills
• ExpeL: LLM Agents Are Experiential Learners
• Metacognitive Reuse
• SkillRL
• Internalizing Agency from Reflective Experience (ACE evaluation)
• Self-Improving AI Coding Agents Through Accumulated Behavioral Rules
• ASG-SI: Audited Skill-Graph Self-Improvement
• SE-GoS: Self-Evolving Graph-of-Skills
• Cognee: Building Self-Improving Skills for Agents
• unisone/self-improving-skills
• GitHub topic: claude-code-skills
• Smythe
• AgentHistoric
• WonderMr/Agents
• Letta Code
• Vellum assistant
• Production compilation in ACT-R (Taatgen)
• PRISM persona routing, via Hugging Face papers

"