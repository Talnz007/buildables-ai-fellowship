# Zero-Shot vs Few-Shot Prompting

## Zero-Shot Prompting
**Definition:** Ask the model to complete a task without providing examples.  
**Strengths:**
- Simple and fast.
- Works well for straightforward tasks (translation, summarization).
**Weaknesses:**
- Accuracy drops on complex reasoning.
- Ambiguity can confuse the model.

Example:
- Prompt: "Classify sentiment of: 'The food was terrible.'"
- Output: "Negative"

---

## Few-Shot Prompting
**Definition:** Provide a few worked-out examples before asking the question.  
**Strengths:**
- Calibrates the model by showing desired format and logic.
- Reduces ambiguity.
**Weaknesses:**
- Requires careful example selection.
- Input length may increase (token cost).

Example:
- Prompt:  
  "Review: 'I love ice cream' → Sentiment: Positive  
   Review: 'I hate traffic' → Sentiment: Negative  
   Review: 'The weather is beautiful' → Sentiment: ?"
- Output: "Positive"

---

## Comparison
| Aspect | Zero-Shot | Few-Shot |
|--------|-----------|----------|
| Setup | Minimal | Requires examples |
| Accuracy | Lower on reasoning tasks | Higher, especially with structured examples |
| Cost | Cheaper (fewer tokens) | More tokens needed |
| Best Use | Quick tasks | Classification, reasoning, style transfer |

---

## Practical Tip
- Start with **zero-shot** → if accuracy is low, add **few-shot** examples.  
- Combine with **Chain-of-Thought** for reasoning-heavy tasks.  

## References
- [OpenAI Prompting Guide](https://platform.openai.com/docs/guides/prompting)  

