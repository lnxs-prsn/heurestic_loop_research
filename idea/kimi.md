# Report: Adaptive Heuristic Exoskeleton for Strong LLM Systems

**Prepared:** Based on architectural evolution from static heuristic harness to dynamic, self-modifying reasoning infrastructure.

---

## 1. Executive Summary

This report formalizes a modified architecture that repositions the heuristic-subagent harness from a **compensatory prosthetic** (for weak models) to a **cognitive exoskeleton** (for strong models). The critical innovation is the introduction of a **dynamic heuristic lifecycle**: strong base models not only select and execute from a curated heuristic library, but also critique, modify, and evolve that library based on execution outcomes.

The value proposition shifts from *enabling reasoning* to *systematizing, inspecting, and continuously improving reasoning*. The architecture treats heuristics not as static crutches, but as version-controlled, testable, and self-optimizing reasoning primitives.

---

## 2. The Pivot: From Prosthetic to Exoskeleton

### 2.1. Why the Original Design Misaligns with Strong Models

The static harness described in the foundational report was architected to solve a specific problem: weak models cannot reliably perform meta-cognition (heuristic selection, strategy formulation). For strong models, this is not the binding constraint. Asking a capable model to route between pre-written heuristics adds latency and overhead without addressing a genuine bottleneck.

**The mismatch:** The original system asks the model to do *less* than it can. The modified system asks the model to do *more*—but in a structured, externalized, and improvable way.

### 2.2. The New Value Proposition

For strong models, the harness provides:

| Capability | Description |
|------------|-------------|
| **Reproducibility** | Named heuristics create deterministic reasoning topologies. The same query + heuristic yields inspectably similar reasoning paths. |
| **Auditability** | Every output carries a reasoning genealogy: *"Heuristic #7 (Analogical Decomposition) was selected with confidence 0.91; execution flagged summary ambiguity in step 3."* |
| **Continuous Improvement** | Execution failures and critiques feed back into the heuristic library, creating a living knowledge base. |
| **Load Distribution** | Complex reasoning is decomposed into discrete, parallel heuristic executions that can be validated independently before synthesis. |

---

## 3. Core Architecture: The Adaptive Harness

The system retains the four-layer structure but redefines each layer's role and introduces a fifth: the **Meta-Cognition & Evolution Layer**.

### 3.1. The Heuristic Repository (Dynamic Data Layer)

- **Format:** Version-controlled JSON/YAML with embedded metadata.
- **Content per heuristic:**
  - `id`: Unique identifier
  - `summary`: Short, discriminative phrases for indexing
  - `full_prompt_template`: The detailed reasoning scaffold
  - `metadata`:
    - `success_rate`: Float, updated via feedback loop
    - `last_modified`: Timestamp
    - `version`: Semantic versioning
    - `domain_tags`: Applicable problem categories
    - `failure_modes`: Logged patterns where this heuristic underperforms

- **Rationale:** The library is no longer static. It is a **reasoning codebase** that evolves.

### 3.2. The Indexing & Matching Engine (Selection Layer)

- **Mechanism:** Hybrid retrieval combining vector embeddings, keyword tags, and historical success weighting.
- **Process:** Queries are matched against heuristic summaries, but ranking incorporates `success_rate` and `domain_tags`.
- **Output:** Top-N viable heuristics, ranked by composite score (similarity × historical performance).

### 3.3. The Router (Orchestration Layer)

- The strong model receives the query and the top-N heuristic summaries.
- **Unlike the original design:** The model is *not* restricted to lightweight selection. It performs active meta-reasoning: *"Given these summaries and the query structure, Heuristic A is primary; Heuristic B is a useful cross-check; Heuristic C is irrelevant because..."*
- **Output:** A ranked execution plan with explicit rationale.

### 3.4. The Subagent Parallel Execution Layer

- Multiple subagents (which may be instances of the same strong model or specialized variants) execute in parallel.
- Each subagent receives: the user query + the full prompt template + a constraint on output structure.
- **Critical addition:** Each subagent is instructed to generate not only an answer, but a **confidence-and-critique** block assessing whether the heuristic was appropriate for this specific query.

### 3.5. The Meta-Cognition & Evolution Layer (New)

This is the architectural differentiator. After execution:

1. **Outcome Evaluation:** The system scores each subagent output (via programmatic evaluation, human feedback, or a stronger judge model).
2. **Heuristic Critique Generation:** The base model (or a dedicated meta-model) generates a structured critique:
   - Was the heuristic selection correct?
   - Did the full prompt template contain redundant or misleading instructions?
   - Was the summary phrase ambiguous or overly broad?
3. **Modification Proposals:** If a heuristic underperforms, the system proposes:
   - `summary` refinement (sharper discriminative phrases)
   - `full_prompt_template` edits (removing noise, adding constraints)
   - `domain_tags` expansion or restriction
   - New heuristic creation (if the query falls into a gap)
4. **Validation Gate:** Proposed modifications are held in a **staging area**. They must pass:
   - Regression testing against a holdout set of historical queries
   - A/B comparison against the current heuristic version
   - Optional human review for high-stakes domains
5. **Deployment:** Validated modifications are merged into the live library with version increment.

---

## 4. The Dynamic Heuristic Lifecycle

```
┌─────────────────────────────────────────────────────────────┐
│  USER QUERY                                                 │
└──────────────┬──────────────────────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────────────────────┐
│  INDEX RETRIEVAL (Hybrid: embedding + performance history)   │
└──────────────┬──────────────────────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────────────────────┐
│  META-ROUTING (Strong model selects + justifies choice)     │
└──────────────┬──────────────────────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────────────────────┐
│  PARALLEL SUBAGENT EXECUTION (Query + Heuristic Template)    │
│  Each returns: [Answer] + [Confidence] + [Critique]         │
└──────────────┬──────────────────────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────────────────────┐
│  AGGREGATION (Best-of-N, synthesis, or structured voting)     │
└──────────────┬──────────────────────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────────────────────┐
│  FEEDBACK LOOP                                                │
│  ├─ Outcome scoring                                           │
│  ├─ Heuristic critique generation                             │
│  ├─ Modification proposal (staging)                           │
│  ├─ Regression validation                                     │
│  └─ Merge to live library (versioned)                         │
└─────────────────────────────────────────────────────────────┘
```

---

## 5. Risk Architecture & Safeguards

Dynamic self-modification introduces failure modes that static systems avoid. The architecture must contain these risks explicitly.

### 5.1. Heuristic Drift

**Risk:** Over time, heuristics evolve to become overly narrow, overfit to recent query distributions, or "gamed" by the model to favor aesthetically pleasing but less effective reasoning paths.

**Mitigation:**
- **Temporal regularization:** Success rates are computed over sliding windows, not cumulative history.
- **Diversity enforcement:** The system tracks embedding-space coverage. If heuristics cluster too tightly, a "exploration" mode triggers, forcing selection of underutilized heuristics.
- **Separation of concerns:** The model that *proposes* heuristic modifications is distinct from the model that *uses* them (or at minimum, operates under different system prompts).

### 5.2. The Validation Bottleneck

**Risk:** A strong model can generate plausible-sounding modifications that fail in practice. Without a ground-truth evaluator, the system optimizes for *verbal coherence* rather than *task correctness*.

**Mitigation:**
- **Programmatic evaluation where possible:** For math, code, or structured data tasks, use deterministic evaluators.
- **Human-in-the-loop for high-stakes changes:** Modifications to heuristics with >100 historical invocations require human approval.
- **Canary deployment:** New heuristic versions are rolled out to 10% of traffic before full deployment.

### 5.3. Summary Ambiguity Amplification

**Risk:** If the `summary` phrases become too abstract or metaphorical, the index retrieval degrades.

**Mitigation:**
- **Summary orthogonality audits:** Periodic automated checks for cosine similarity between summary embeddings. If any pair exceeds a threshold, the system flags them for disambiguation.
- **Human-curated seed summaries:** The initial library is written by humans; the model only *refines*, never *invents from scratch* without validation.

---

## 6. Comparison: Static vs. Adaptive Harness

| Dimension | Static Harness (Weak Model) | Adaptive Exoskeleton (Strong Model) |
|-----------|----------------------------|-------------------------------------|
| **Primary function** | Compensate for poor meta-reasoning | Systematize and improve strong reasoning |
| **Heuristic library** | Static, curated once | Dynamic, version-controlled, self-optimizing |
| **Model's role** | Surface-level selector | Active meta-reasoner + critic + editor |
| **Failure mode** | Wrong heuristic selected | Heuristic drift, overfitting, validation gaps |
| **Best use case** | Narrow, bounded domains | Complex, high-stakes, evolving problem spaces |
| **Cost structure** | N× inference per query | N× inference + periodic meta-processing |
| **Key metric** | Accuracy vs. zero-shot | Reproducibility + rate of heuristic improvement |

---

## 7. Implementation Recommendations

### 7.1. Phase 1: Foundation (Weeks 1-2)
- Build the static heuristic library for your target domain.
- Implement the indexing engine and parallel subagent execution.
- Add structured logging: every query, selected heuristic, subagent output, and final aggregation must be recorded.

### 7.2. Phase 2: Critique (Weeks 3-4)
- Add the confidence-and-critique block to subagent outputs.
- Build a manual review dashboard where human operators can flag heuristic misfires.
- Do not yet allow automatic modification—only logging and flagging.

### 7.3. Phase 3: Evolution (Weeks 5-8)
- Implement the modification proposal pipeline.
- Build the regression test harness (holdout set of 50-100 queries per heuristic).
- Enable automatic modification for low-stakes heuristics (<50 historical uses); require human approval for mature heuristics.

### 7.4. Phase 4: Autonomy (Ongoing)
- Introduce the "new heuristic creation" pathway for query gaps.
- Implement the diversity enforcement and temporal regularization safeguards.
- Deploy canary testing for all heuristic version updates.

---

## 8. Conclusion

The adaptive heuristic exoskeleton is not a workaround for model weakness. It is an infrastructure layer that treats reasoning as **versioned, testable, and continuously improvable software** rather than as a transient, opaque inference.

For strong models, the architecture does not ask *"Can you reason?"*—it asks *"Can you reason reproducibly, explain your strategy, and get better over time?"* The answer to the latter, with proper scaffolding, is yes.

The system trades some of the zero-shot flexibility of end-to-end reasoning for the predictability of structured reasoning primitives. In domains where debugging failures, auditing decisions, or accumulating institutional knowledge matters, this is a trade worth making.

The original harness externalized heuristics to bypass a weak model's limitations. The adaptive exoskeleton externalizes heuristics to make a strong model's reasoning **legible, accountable, and self-improving.**

---

*End of Report*