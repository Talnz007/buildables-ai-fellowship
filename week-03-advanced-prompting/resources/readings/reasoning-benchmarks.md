# Reasoning Benchmarks

## Why Benchmarks Matter
To measure LLM reasoning, researchers evaluate models against standardized tasks.  
These benchmarks reveal strengths, weaknesses, and improvements with advanced prompting methods.

## Key Benchmarks

### 1. GSM8K
- **Focus:** Grade-school math word problems.  
- **Relevance:** Used widely to test CoT prompting.  
- **Insight:** Accuracy improves significantly when models are asked to “think step by step.”

### 2. BIG-Bench (Beyond the Imitation Game)
- **Focus:** Broad set of 200+ tasks (reasoning, common sense, linguistics).  
- **Relevance:** Evaluates diverse reasoning abilities.

### 3. MATH Dataset
- **Focus:** High school competition-level math problems.  
- **Relevance:** Requires multi-step symbolic reasoning.

### 4. Logic Puzzles & Synthetic Tasks
- **Focus:** Abstract reasoning and deduction.  
- **Relevance:** Useful for lab activities (provided in this repo’s datasets).

## Connection to Week 3
- Use provided JSON datasets (`logic-puzzles.json`, `math-problems.json`, `reasoning-tasks.json`) as mini-benchmarks.  
- Apply zero-shot, few-shot, and CoT prompting to compare results.

## References
- [Wei et al., 2022 – Chain-of-Thought Prompting](https://arxiv.org/abs/2201.11903)  
- [BIG-Bench Paper](https://arxiv.org/abs/2206.04615)  

