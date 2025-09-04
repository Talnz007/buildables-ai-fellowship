# Reasoning Prompt Templates

These templates help apply **Chain-of-Thought (CoT)** prompting strategies.  
Read [Chain-of-Thought Fundamentals](../readings/chain-of-thought-fundamentals.md) before using.

---

## Math Word Problem
```text
Solve this problem and explain your reasoning step by step.

Problem: A train travels 80 km in 2 hours. How far will it go in 5 hours?

Answer (show steps):
````

---

## Logic Puzzle

```text
Solve this puzzle step by step.

Puzzle: Alice is older than Bob. Bob is older than Charlie. Who is the youngest?

Answer (explain reasoning):
```

---

## Multi-Step Q\&A

```text
Answer the following question step by step, showing intermediate reasoning.

Question: If water freezes at 0°C and boils at 100°C, what is the temperature range of liquid water in Celsius?

Answer (step by step):
```

---

👉 Use with datasets: [logic-puzzles.json](../datasets/logic-puzzles.json) and [math-problems.json](../datasets/math-problems.json).
👉 Score results using the [Reasoning Evaluation Rubric](../../assignments/reasoning-evaluation-rubric.md).

````
