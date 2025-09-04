# Few-Shot Prompt Templates

These templates provide structured starting points for few-shot prompting.  
Refer to [Zero-Shot vs Few-Shot Guide](../readings/zero-shot-vs-few-shot-guide.md) for background.

---

## Sentiment Classification
```text
Task: Classify the sentiment of the following reviews.

Example 1:
Input: "I love this product!"
Output: Positive

Example 2:
Input: "This is the worst service ever."
Output: Negative

Now classify:
Input: "{{your_text_here}}"
Output:
````

---

## Text Summarization

```text
Task: Summarize each article in one sentence.

Example 1:
Text: "The stock market rose by 2% today as tech companies rallied."
Summary: "Tech stocks drive 2% market gain."

Example 2:
Text: "Scientists discovered a new exoplanet that may support life."
Summary: "New exoplanet found with potential habitability."

Now summarize:
Text: "{{your_text_here}}"
Summary:
```

---

## Style Transfer

```text
Task: Rewrite the given text in Shakespearean style.

Example 1:
Input: "I’m going to the store."
Output: "To market forth I go anon."

Example 2:
Input: "It is raining heavily."
Output: "Lo, the heavens do weep profusely."

Now rewrite:
Input: "{{your_text_here}}"
Output:
```

---

👉 Evaluate outputs using the [Reasoning Evaluation Rubric](../../assignments/reasoning-evaluation-rubric.md).

```
----------------------------
