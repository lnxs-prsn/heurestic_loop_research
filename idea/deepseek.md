# Report: Heuristic-Driven Subagent Harness for Enhancing Weak LLM Performance

**Prepared:** Based on the philosophical premise and architectural specifications provided.

## 1. Executive Summary

This report formalizes a proposed architecture designed to elevate the reasoning and output quality of a weak base LLM to a level significantly exceeding its native zero-shot capabilities. The core innovation is a **decoupled harness system** that externalizes heuristic selection and execution into static data structures (JSON/YAML) and indexed retrieval mechanisms. By drawing a direct parallel to human cognitive biases—where rapid cue-reading triggers pre-learned heuristics—the system offloads the burden of meta-cognition from the weak model, relying instead on curated knowledge bases and brute-force subagent parallelism.

---

## 2. Philosophical Foundation

The architecture is grounded in the premise that humans are not fundamentally more rational than LLMs. Instead:

- Humans possess vast libraries of heuristics accumulated over long periods.
- Their primary meta-skill is reading environmental cues to select which heuristic to deploy.
- The downside of this process is **cognitive bias**: once a cue is learned, the associated heuristic is often followed blindly.

The proposed harness mirrors this structure: the "environment" is the user query; the "cues" are indexed summary phrases; and the "blind execution" is the subagent spawning process. This design reframes rationality not as inherent model intelligence, but as the quality of the heuristic library and the precision of the selection mechanism.

---

## 3. Core Technical Architecture

The harness is structured into four distinct layers:

### 3.1. The Heuristic Repository (Static Data Layer)
- **Format:** JSON or YAML files.
- **Content:** For each heuristic, the repository stores:
  - `summary`: A few short, highly discriminative phrases (e.g., "Reverse engineering from end state," "Analogical reasoning to physical systems").
  - `full_prompt_path`: A file path or a large prompt template designed to guide the subagent through that specific reasoning process.
- **Rationale:** The weak base LLM never sees or generates the full, complex prompts. It only interacts with the short summaries, preventing its generative flaws from corrupting the heuristic content.

### 3.2. The Indexing & Matching Engine (Selection Layer)
- **Mechanism:** Pre-computed vector embeddings, keyword tags, or semantic indexes for the `summary` fields.
- **Process:** Upon receiving a user query, the system computes a similarity score between the query and all available heuristic summaries.
- **Output:** The engine identifies the **top 2 most viable heuristic matches**.

### 3.3. The Router (Orchestration Layer)
- The system passes the original user query and the top 2 matched summary phrases to the weak base LLM.
- *Crucially:* The weak model is not asked to reason deeply. It is only asked to perform a final lightweight verification (e.g., "Choose A or B" based on the brief summaries) or the routing can simply be deterministic, taking the top 2 by index score.

### 3.4. The Subagent Parallel Execution Layer
- Two (or more) subagents—which can be instances of the *same* weak base LLM—are spawned.
- **Subagent A** receives the user query + the full prompt file linked to Heuristic 1.
- **Subagent B** receives the user query + the full prompt file linked to Heuristic 2.
- Each subagent generates a complete output independently. These outputs are then aggregated (e.g., best-of-N selection, weighted voting, or concatenation/synthesis) to produce the final answer.

---

## 4. Resolution of the Critical Bottleneck

A significant architectural challenge was identified: relying on the *weak base LLM* to select the top 2 heuristics would reintroduce the very flaw the system aims to bypass—asking a limited model to perform complex meta-cognition.

**The user's proposed solution (implemented in the architecture above) resolves this perfectly:**

1.  **Summarization:** The weak LLM only handles ultra-short summary phrases, making the matching task a surface-level retrieval problem rather than a deep reasoning one.
2.  **External Indexes:** By building pre-computed indexes (e.g., vector databases) to assess heuristic-problem compatibility, the system shifts precision from *inference-time reasoning* to *pre-computed retrieval*. The selection accuracy scales with the quality of the index and the curatorial precision of the summaries, not with the parameter count of the base model.

---

## 5. Implications & Advantages

- **Parameter Efficiency:** Allows small, cheap, and fast models to punch well above their weight class without fine-tuning.
- **Predictability:** Since heuristics are static and curated, the system's behavior is more predictable and less prone to hallucination in the *strategy* phase.
- **Exploitability of Human Bias:** By embracing the "blindness" described in the philosophical premise (the system follows the cue without second-guessing), the harness avoids the paralysis-by-analysis that often plagues larger models trying to solve everything end-to-end.

---

## 6. Recommendations & Further Suggestions

Based on the logical extensions of the idea, the following refinements are recommended:

1.  **Curation Over Generation:** The success of the system hinges entirely on the quality and distinctiveness of the `summary` phrases. Invest heavily in manually writing or rigorously validating these summaries to ensure they are orthogonal enough to avoid index ambiguity.

2.  **Hybrid Selection for Safety:** Instead of solely relying on the weak LLM to choose between the top 2, consider a deterministic fallback: if the index similarity scores for the top 2 are too close (low confidence), spawn *three* subagents (top 3) and use a majority-vote or meta-synthesis layer.

3.  **Feedback-Weighted Indexing:** Implement a logging mechanism that tracks which heuristic subagent won the final aggregation round for specific query types. Periodically rebuild or adjust the index weights to boost historically successful heuristics for similar incoming queries, effectively allowing the harness to "accumulate experience" externally.

4.  **Semantic Caching for Subagents:** Since subagents share the same context but different prompts, ensure the system caches the common parts of the context window to reduce API/compute overhead.

5.  **Prompt Engineering for Subagents:** Ensure the full prompt files do not just state the heuristic, but explicitly instruct the weak subagent to avoid degenerating into its default behavior. Impose strict structural constraints on the output format (e.g., JSON, bullet points) to maintain reliability.

---

## 7. Conclusion

The proposed heuristic-subagent harness is a philosophically coherent and technically viable method for supercharging weak LLMs. By externalizing heuristics into static files, relying on robust indexes for cue-reading, and offloading execution to parallel subagents, the system effectively bypasses the inherent limitations of the base model's parameter count. The architecture stands as a practical proof-of-concept that replicating human heuristic-reliance—including its mechanical, sometimes "blind" execution—is not a bug in AI design, but a powerful, low-cost feature. The bottleneck of heuristic selection has been successfully addressed through data curation and index-driven retrieval, leaving a clear path for implementation.