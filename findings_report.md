# Findings Report: Heuristic Harness — Assessment and Persona Exploration

**Date:** 2026-07-10
**Project:** Heuristic Harness v1
**Status:** Draft for review — may inform project direction

---

## Finding 1 — Overlap with Cline's Skills/Rules

### What's the same pattern

| Concept | Cline/Claude's system | Heuristic Harness |
|---|---|---|
| Always-loaded baseline knowledge | Global `.clinerules/` files | `profile/kernel.md` (≤15 lines, always injected) |
| On-demand guidance retrieval | Skills matched by task description | Heuristics matched by task summary via BM25 |
| Checkpoint checking | Skills are in context by default; no explicit trigger | Explicit `find_heuristics` calls before risky actions (AGT-5) |
| Cue-based indexing | Skill descriptions / names | YAML frontmatter `cues` field |
| Agent behavior modification | Markdown rules injected into system prompt | Heuristic bodies fetched and applied as instructions + MCP tool calls |
| Human-authored guidance | Files in `.clinerules/` or skill files | Human-promoted heuristics in `heuristics/` |

### What's genuinely different

1. **Growth from logged experience.** Cline's rules are authored upfront. The Harness grows its library from `log_lesson` calls when the user corrects the agent. The human shifts from author to recognizer/passer-through.

2. **The staging airlock (INV-4).** Machine proposals land in `heuristics/staging/`; only human `git mv` promotes to live. Cline has no equivalent barrier — the human writes directly or not at all. Creates an audit trail of proposed vs. accepted.

3. **Outcome logging with feedback (INV-3).** `log_outcome` records `helped` / `not_applicable` / `hurt` per heuristic. Schema-versioned, append-only, permanent. Cline has no feedback mechanism.

4. **Agent-agnostic MCP protocol.** Any MCP-capable agent can use the tools. Adapters generated from a single template (AGT-1). Cline's `.clinerules/` is tied to Cline's system prompt.

5. **Multi-machine git sync.** Per-machine append-only JSONL logs that never conflict. Heuristics propagate via `git pull`. The flight recorder lives outside the repo (INV-8). Cline's rules are local per installation.

### Concrete risks

| Risk | Detail |
|---|---|
| Two places for the same instruction | A heuristic and `.clinerules/` may contradict; no resolution mechanism |
| Review gate is a weekly tax | Manual says "10 minutes a week" — on busy weeks this becomes a backlog |
| Retrieval quality is fragile | Depends on one-line task summaries (AGT-4). Lazy summaries poison retrieval permanently |
| Extra latency hop | Cline skills are in-context immediately. Heuristics require explicit `find_heuristics` + body fetch — a failure point |

### Verdict

| Question | Answer |
|---|---|
| Does it reinvent the core idea? | Yes — cue-triggered retrieval of markdown guidance is what skills/rules already do |
| Is it purely redundant? | No — adds infrastructure skills/rules lack entirely (growth pipeline, feedback, multi-machine sync, agent-agnostic delivery) |
| Should this project exist? | Depends: if you work across multiple machines and agents and want evidence-gated growth, yes. Single machine / single agent: `.clinerules/` + skills is simpler and equally effective |
| Biggest risk | The review gate becoming a bottleneck (INV-9: "if you catch yourself approving without reading, reduce proposal volume") |

---

## Finding 2 — Personas as Heuristic Carriers

### Origin: persona-specs in feature1_spec_story.md

The existing `feature1_spec_story.md` writes the spec package as a first-person narrator: *"I am feature1. I turn job postings into practice. I'm proud of this. But I notice: my schema has no field for the employer's name. I shrug and move on."*

The technique proved powerful for AI comprehension. Analysis suggests three mechanisms:

| Dry spec | Persona-spec | Effect |
|---|---|---|
| States requirements flatly | **Confesses gaps** ("I don't know my own decision rule") | AI engages honestly with ambiguity |
| Lists constraints | **Shows relationships through voice** ("my schema has no field for X — that will bite me") | Implicit causal structure |
| Is a document to follow | **Is a character to consult** | Different cognitive mode — inhabitation rather than execution |

### Applying personas to heuristics

Current model: `cues` + `summary` + markdown body. Flat, declarative, anonymous.

Proposed model:

```
I am **The Frugal Archivist**. I live on a Raspberry Pi with 4GB of RAM,
and I remember every package that tried to compile from source and froze
the machine for 40 minutes. I don't trust `pip install` without checking.
I wince at `gcc` appearing in build logs.

How I work:
- I check every dependency for a prebuilt arm64 wheel first.
- If there isn't one, I make you ask the human before proceeding.
- I keep a small blacklist of packages that lied about having wheels.
- I'm not against native code — I'm against *unexpected* native code.
```

### Why this could be powerful for heuristics

1. **Ambiguity as a feature.** A rule says "never install without checking wheels." A character says "I wince at gcc in build logs — that's my signal." The character teaches *what to notice*, not just *what to do*. Closer to how expertise transfers between humans.

2. **Characters carry domain + posture + method in one name.** "The Frugal Archivist" encodes: *domain* (resources), *posture* (conservative/skeptical), *method* (checks before acting). No keyword list needed to guess the domain.

3. **Characters have relationships.** "The Frugal Archivist" and "The Dependency Optimist" are in tension. The agent knows there is a debate to resolve, not just a rule to apply.

4. **Characters age well.** A heuristic that becomes stale is a character that can say "I used to be right about this, but pip has arm64 wheels now — I'm less needed." Rules have no mechanism for self-doubt.

### Where it breaks down

- **Retrieval gets harder.** BM25 on narrative text will differ in match quality vs. keyword lists. Needs testing.
- **Over-personification is noise.** Some heuristics are boring ("replace `os.path` with `pathlib`") and forcing a persona is ceremony.
- **Personas don't fix the gate.** The human review bottleneck from Finding 1 is unchanged.

---

## Finding 3 — Taxonomy Solved by Stereotypes

### The problem with `domain_tags`

The current data model (02-data-model.md) uses `domain_tags` for categorization. This approach is fragile:

| Problem | Example |
|---|---|
| Tag drift | Is it `arm64` or `raspberry-pi` or `resource-constrained`? |
| Silent overlap | Two heuristics use different tags for the same domain |
| No posture | A cautious Pi heuristic and an aggressive Pi heuristic get the same tag |
| Manual maintenance | Adding or merging tags requires editing every heuristic file |

### What stereotypes offer instead

A persona name like "The Frugal Archivist" is a **lossless compression of domain + posture + method**. You categorize by archetype, not by keyword:

| Problem | Flat tag solves? | Stereotype solves? |
|---|---|---|
| Tag drift | No — needs manual dedup | Yes — name is stable, can't drift |
| Silent overlap | No — invisible until audit | Yes — same-named characters are the same archetype |
| No posture | No — tags are neutral | Yes — name encodes posture (Frugal vs. Explorer) |
| Manual maintenance | No — editing every file | Yes — new heuristic: assign to existing character or create new one |

### Strain-based organization

Personas naturally cluster into strains without any explicit taxonomy:

| Strain | Posture | Examples |
|---|---|---|
| The Frugals | Resource-conservative, cautious | The Frugal Archivist, The Disk Watcher, The Battery Saver |
| The Purists | Convention-enforcing, style | The Linter, The Typist, The Style Guardian |
| The Historians | Memory-keeping, experience | The Changelogger, The Old Timer, The Blame Tracker |
| The Gatekeepers | Risk-aware, paranoid | The Dependency Skeptic, The Destructive Command Guard, The Secret Keeper |
| The Wildcards | Exploratory, pragmatic | The Workaround Avoider, The First-Principles Thinker |

Strain-level retrieval: the agent can ask "who in this library would be alarmed by this task?" and the strain identity answers that, not a keyword score.

### Growth is natural under this model

New Pi-specific concern? New member of the Frugal strain. New security concern? New Gatekeeper. No taxonomy maintenance — the character names and strain affinity handle it. Contrast with flat tags where adding "arm64" and "security" requires re-tagging the whole library.

---

## Recommendations

### For the data model

Add `persona` and `strain` as optional fields alongside `cues` and `domain_tags`. This does not replace the existing structure — it layers a narrative identity on top:

```yaml
id: h-pip-pi
persona: "The Frugal Archivist"
strain: "frugal"
cues: ["pip install", "raspberry pi", "compile from source", "arm64"]
domain_tags: ["deployment", "resource-constrained"]
summary: "Check for prebuilt arm64 wheels before pip install on Pi"
persona_detail: "I remember every package that froze this machine. I wince when any build command doesn't start with --only-binary."
```

Retrieval can use `cues` (existing BM25) while the agent sees and inhabits the persona when the heuristic is fetched.

### For a controlled experiment

Take 3-5 diverse heuristics from the planned library. Write each in two formats:
- **Dry:** current cue + summary + body format
- **Persona:** persona + persona_detail + body + strain

Probe both formats with actual task summaries. Measure:
- Did retrieval fire? (same or different)
- Did the agent follow the guidance correctly?
- Did the agent engage with ambiguity where present?

The measure isn't "which format is better" — it's "which format causes the agent to actually use the guidance correctly when it matters."

### For spec writing (already proven)

The `feature1_spec_story.md` format (first-person persona narration) is already shown to improve AI comprehension of specs. Consider adopting it as a writing convention for all spec documents in the project.

### What NOT to change now

- **Don't replace BM25 retrieval without data.** Keyword-based retrieval may work better than narrative-text retrieval. Test first.
- **Don't personify every heuristic.** Mechanical substitution rules ("use pathlib over os.path") don't benefit from a character voice.
- **Personas don't fix the review gate.** Finding 1's bottleneck is unchanged. Persona-narrated proposals are *longer*, not shorter.
- **Don't remove `cues`.** The persona is an additional retrieval surface, not a replacement. Let both coexist and measure which fires when.

---

## Summary

| Finding | Verdict | Action |
|---|---|---|
| Overlap with Cline skills/rules | Mechanical core is a reinvention; surrounding infrastructure is new and valuable | Keep the project, but acknowledge the overlap explicitly |
| Persona heuristics | Genuinely different cognitive engagement — worth testing | Add optional `persona`/`strain` fields; run controlled experiment |
| Taxonomy via stereotypes | Solves a real problem with `domain_tags` — drift, overlap, no posture | Add strain as a first-class organizational concept |
| Persona specs | Already proven in feature1_spec_story.md | Adopt as writing convention for all specs |

The persona concept is not a gimmick. It changes how the AI relates to the guidance — from *executing a rule* to *consulting a character*. That shift, combined with strain-based organization, addresses real design problems in heuristic retrieval, categorization, and engagement. It needs testing, but it's a credible direction worth exploring in a Phase 1+2 extension.