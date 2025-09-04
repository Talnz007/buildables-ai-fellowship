# Evaluation Frameworks for Prompting

A structured way to compare **Zero-Shot, Few-Shot, and Chain-of-Thought (CoT)** prompting methods.  
Supports Week 3 assignments ([Prompt Comparison Lab](../../assignments/prompt-comparison-lab.md)).

---

## Step 1: Select a Task
Choose from the [datasets](../datasets), such as:
- `logic-puzzles.json`
- `math-problems.json`
- `reasoning-tasks.json`

---

## Step 2: Run Different Prompts
- **Zero-Shot:** direct question with no examples.  
- **Few-Shot:** include 2–3 examples.  
- **CoT:** explicitly ask the model to “think step by step.”  

---

## Step 3: Record Outputs
```markdown
| Task              | Zero-Shot Output | Few-Shot Output | CoT Output                         |
|-------------------|------------------|-----------------|-------------------------------------|
| Logic Puzzle #1   | "Bob"            | "Charlie"       | "Step 1… Step 2… Answer: Charlie"  |
````

---

## Step 4: Evaluate

Apply the [Reasoning Evaluation Rubric](../../assignments/reasoning-evaluation-rubric.md).

```markdown
| Criterion     | Zero-Shot | Few-Shot | CoT |
|---------------|-----------|----------|-----|
| Correctness   | 1         | 2        | 3   |
| Clarity       | 0         | 2        | 3   |
| Completeness  | 1         | 2        | 3   |
| Conciseness   | 2         | 2        | 2   |
```

---

## Step 5: Reflect

* Which prompting style consistently performs better?
* Where does CoT help the most?
* Do examples improve reasoning or just formatting?

---

👉 For sample prompting patterns, see [Prompt Patterns Library](../readings/prompt-patterns-library.md).

```
