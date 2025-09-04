# Prompt Patterns Library

## Overview
Prompt patterns are reusable strategies for structuring inputs to get better responses from LLMs.  
Think of them like "design patterns" in software engineering.

## Common Prompt Patterns

### 1. Zero-Shot
- **Definition:** Ask the question with no examples.
- **Use Case:** Quick tasks like definitions, summaries.
- **Example:**  
  "Translate 'good morning' to French."

### 2. Few-Shot
- **Definition:** Provide a few worked examples before the task.
- **Use Case:** Classification, style imitation.
- **Example:**  
  "Example: Input: 'I love pizza' → Sentiment: Positive  
   Input: 'I hate rain' → Sentiment: Negative  
   Input: 'This movie is amazing' → Sentiment: ?"

### 3. Chain-of-Thought (CoT)
- **Definition:** Ask the model to explain reasoning step by step.
- **Use Case:** Math, logic, reasoning.
- **Example:**  
  "If a train travels 60 km in 1 hour, how far in 4 hours? Think step by step."

### 4. Role/Persona Prompts
- **Definition:** Instruct the model to act as a persona.
- **Example:**  
  "You are an expert math tutor. Explain quadratic equations simply."

### 5. Instruction Refinement
- **Definition:** Specify formatting, style, or constraints.
- **Example:**  
  "Summarize this article in 3 bullet points, each under 10 words."

## References
- [OpenAI Prompting Guide](https://platform.openai.com/docs/guides/prompting)  
- [Prompt Engineering Best Practices](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api)  

