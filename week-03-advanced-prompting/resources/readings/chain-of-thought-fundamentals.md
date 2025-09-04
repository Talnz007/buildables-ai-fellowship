# Chain-of-Thought (CoT) Fundamentals

## What is CoT Prompting?
Chain-of-Thought (CoT) prompting is a technique where the model is explicitly asked to "think step by step."  
Instead of jumping straight to an answer, the LLM outlines its reasoning process in multiple steps.

Example:
**Prompt:** What is 23 × 17? Think step by step.  
**Response:**  
1. 23 × 10 = 230  
2. 23 × 7 = 161  
3. 230 + 161 = 391  
**Answer: 391**

## Why It Works
- Large models internally perform reasoning-like processes.  
- CoT helps “externalize” this reasoning, making the model’s thinking transparent.  
- Research (Wei et al., 2022) shows that CoT significantly improves performance on math word problems, logic puzzles, and multi-step reasoning tasks.

## Limitations
- Smaller models (<10B parameters) often fail with CoT prompts.  
- CoT can introduce “hallucinated steps” even when the final answer is correct.  
- Overly verbose reasoning may obscure clarity.

## Key Paper
- [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models (Wei et al., ICLR 2022)](https://arxiv.org/abs/2201.11903)

