# Prompt Comparison Lab: Scientific Approach to Prompt Engineering

## 🔬 Lab Objective
Conduct controlled experiments comparing prompt engineering techniques using scientific methodology.

## 🧪 Experimental Design

### Hypothesis Formation
Before testing, formulate hypotheses:
1. **Zero-Shot Hypothesis**: "Zero-shot prompts will perform worst on complex reasoning tasks"
2. **Few-Shot Hypothesis**: "Few-shot prompts will show improvement but inconsistent reasoning"
3. [cite_start]**CoT Hypothesis**: "Chain-of-thought prompts will achieve highest accuracy on multi-step problems" 

### Variables to Control
- **Model**: Use same model (e.g., gpt, gemini ... etc) throughout
- **Temperature**: Keep consistent (recommend 0.1 for reasoning tasks)
- **Max Tokens**: Set appropriate limit (500-1000)
- **Problem Difficulty**: Ensure problems are equivalent difficulty within categories

### Test Categories

#### [cite_start]Category A: Logic Puzzles (Deductive Reasoning) 
**Example Problems:**
1. Seating arrangements with constraints
2. "Who owns what?" puzzles  
3. Scheduling conflicts resolution
4. Relationship mapping problems

**Success Criteria:**
- Correct final answer (2 points)
- Valid logical reasoning (1 point)
- Clear explanation (1 point)
**Total**: 4 points per problem

#### Category B: Mathematical Word Problems (Arithmetic Reasoning)
**Example Problems:**
1. Multi-step percentage calculations
2. Time and distance problems
3. Financial planning scenarios
4. Measurement conversions

**Success Criteria:**
- Correct numerical answer (3 points)
- Proper mathematical steps shown (2 points)
**Total**: 5 points per problem

#### Category C: Pattern Recognition (Inductive Reasoning)
**Example Problems:**
1. Number sequence completion
2. Analogical reasoning tasks
3. Classification with rules
4. Trend identification

**Success Criteria:**
- Correct pattern identified (2 points)
- Explanation of pattern logic (2 points)
- Generalization ability (1 point)
**Total**: 5 points per problem

## 📊 Data Collection Protocol

### Response Recording Template
```python
{
    "problem_id": "logic_001",
    "category": "logic_puzzles", 
    "difficulty": 3,
    "prompt_type": "zero_shot",
    "prompt_text": "...",
    "response": "...",
    "accuracy_score": 2,
    "reasoning_score": 1,
    "tokens_used": 156,
    "response_time": 2.3,
    "notes": "Got answer right but reasoning was unclear"
}
