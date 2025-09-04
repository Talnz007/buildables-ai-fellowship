# Week 3 Assignment

## Title
Advanced Prompting: Zero-Shot, Few-Shot, and Chain-of-Thought (CoT)

---

## Overview
This week focuses on experimenting with **different prompting strategies** to see how they impact model reasoning and accuracy.  
You’ll use the datasets provided in [`resources/datasets`](../resources/datasets) and apply three key approaches:
- **Zero-Shot** (direct question, no examples)
- **Few-Shot** (include examples → see [`few-shot-templates.md`](../resources/templates/few-shot-templates.md))
- **Chain-of-Thought (CoT)** (step-by-step reasoning → see [`reasoning-prompt-templates.md`](../resources/templates/reasoning-prompt-templates.md))

By the end, you’ll have a **comparative evaluation** of how these methods perform on reasoning tasks.

---

## Instructions
1. Select at least 3 reasoning tasks from the provided datasets:  
   - [`logic-puzzles.json`](../resources/datasets/logic-puzzles.json)  
   - [`math-problems.json`](../resources/datasets/math-problems.json)  
   - [`reasoning-tasks.json`](../resources/datasets/reasoning-tasks.json)  
   - (Optional: [`benchmark-questions.json`](../resources/datasets/benchmark-questions.json))  

2. For each task, apply three prompting strategies:  
   - **Zero-Shot** → no examples, direct instruction.  
   - **Few-Shot** → use at least 2 examples from [`few-shot-templates.md`](../resources/templates/few-shot-templates.md).  
   - **CoT** → explicitly ask the model to *“think step by step”* using [`reasoning-prompt-templates.md`](../resources/templates/reasoning-prompt-templates.md).  

3. Record the outputs in a table format (see [`evaluation-frameworks.md`](../resources/templates/evaluation-frameworks.md) for guidance).  

4. Evaluate each response using the [Reasoning Evaluation Rubric](reasoning-evaluation-rubric.md).  

---

## Deliverables
Submit a report (Markdown or Jupyter Notebook) containing:
- **Prompts used** (clearly separated for Zero-Shot, Few-Shot, and CoT).  
- **Model outputs** (paste exact responses).  
- **Rubric-based evaluation** (use [reasoning-evaluation-rubric.md](reasoning-evaluation-rubric.md)).  
- **Comparative insights**: Which strategy worked best? Why?  

---

## Bonus Challenges
- **Peer Review**: Swap prompts with a fellow participant and evaluate their outputs.  
- **Prompt Tweaks**: Document how *small wording changes* (e.g., “explain clearly” vs. “think step by step”) affect reasoning.  
- **Dataset Extension**: Add your own puzzle/problem into one of the JSON files in [`datasets`](../resources/datasets) and test prompts on it.  

---

## Suggested Workflow
1. Review the background materials in [`resources/readings`](../resources/readings) (especially [Zero-Shot vs Few-Shot Guide](../resources/readings/zero-shot-vs-few-shot-guide.md) and [Chain-of-Thought Fundamentals](../resources/readings/chain-of-thought-fundamentals.md)).  
2. Use templates from [`resources/templates`](../resources/templates) to structure your prompts.  
3. Collect results in a table (see [`evaluation-frameworks.md`](../resources/templates/evaluation-frameworks.md)).  
4. Score outputs with the [Reasoning Evaluation Rubric](reasoning-evaluation-rubric.md).  
5. Reflect: Which approach was most reliable? Where did the model struggle?  

---
