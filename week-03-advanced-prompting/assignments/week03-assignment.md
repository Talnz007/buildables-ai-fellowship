# Week 3 Assignment: Advanced Prompt Engineering Techniques

## 🎯 Assignment Overview
[cite_start]Master advanced prompting techniques by implementing and comparing zero-shot, few-shot, and chain-of-thought prompting strategies across different reasoning tasks. 

## 📋 Part 1: Prompt Technique Implementation (50 points)

### Task 1.1: Zero-Shot Baseline (15 points)
[cite_start]Create prompts that ask the LLM to solve problems without any examples or reasoning guidance. 

**Requirements:**
- Test on 3 different types of problems:
  1. **Logic Puzzles**: "Who sits where?" type problems
  2. **Math Word Problems**: Multi-step arithmetic reasoning
  3. **Pattern Recognition**: Sequence completion tasks

**Example Zero-Shot Prompt:**

Solve this logic puzzle:
Three friends - Alice, Bob, and Carol - are sitting in a row.
Alice is not sitting next to Bob. Carol is sitting to the right of Alice.
Who is sitting in the middle?

### Task 1.2: Few-Shot Learning (20 points)
Enhance your prompts by providing 2-3 examples of solved problems. 

**Requirements:**
- Use the same problem types as Task 1.1
- Provide clear, well-structured examples
- Test how example quality affects performance
- Document which examples work best

**Template:**

Here are some examples:

Example 1:
Problem: [example problem]
Solution: [step-by-step solution]

Example 2:
Problem: [example problem]
Solution: [step-by-step solution]

Now solve this:
Problem: [target problem]
Solution:

### Task 1.3: Chain-of-Thought Reasoning (15 points)
Guide the model to show its reasoning process explicitly. 

**Requirements:**
- Add "Let's think step by step" or similar reasoning triggers 
- Test different CoT instruction variations
- Combine CoT with few-shot examples
- Evaluate reasoning quality, not just final answers

**Chain-of-Thought Template:**
Let's work through this step by step:

    First, identify what we know

    Then, determine what we need to find

    Next, work through the logical steps

    Finally, state the conclusion

Problem: [your problem here]


## 📊 Part 2: Comparative Analysis (30 points)

### Accuracy Testing
Test each prompt type on 10 problems of each category (30 total problems). 

**Scoring Criteria:**
- **Correct Answer + Good Reasoning**: 2 points
- **Correct Answer + Poor/No Reasoning**: 1 point  
- **Incorrect Answer**: 0 points

### Performance Metrics
Calculate and report:
- Success rate for each prompting technique
- Average reasoning quality score (1-5 scale)
- Types of errors most common in each approach
- Time/token efficiency analysis

**Analysis Template:**

Technique	Logic Puzzles	Math Problems	Pattern Recognition	Overall
Zero-Shot	X/10 (X%)	X/10 (X%)	X/10 (X%)	X/30
Few-Shot	X/10 (X%)	X/10 (X%)	X/10 (X%)	X/30
CoT	X/10 (X%)	X/10 (X%)	X/10 (X%)	X/30

## 🔧 Part 3: Interactive Tool Development (20 points)

### Build a Prompt Comparison Tool
Create a Python script or Streamlit app that:

**Core Features:**
- Input field for problem entry
- Buttons to test all three prompt types
- Side-by-side response comparison
- Accuracy scoring interface
- Export results to CSV/JSON

**Advanced Features (Bonus):**
- Batch problem testing
- Automatic accuracy evaluation for math problems
- Reasoning quality assessment
- Performance visualization charts

**Example Interface Layout:**

Problem Input: [text box]
[Zero-Shot Test] [Few-Shot Test] [CoT Test]

Results:
┌─────────────┬─────────────┬─────────────┐
│ Zero-Shot   │ Few-Shot    │ Chain-of-   │
│             │             │ Thought     │
├─────────────┼─────────────┼─────────────┤
│ Response 1  │ Response 2  │ Response 3  │
│ Accuracy: ? │ Accuracy: ? │ Accuracy: ? │
└─────────────┴─────────────┴─────────────┘
## 📝 Deliverables

1. **Code Files:**
   - `prompt_tester.py` - Main comparison tool
   - `problem_datasets.py` - Your test problems
   - `evaluation_utils.py` - Scoring and analysis functions

2. **Analysis Report** (1000-1500 words):
   - Methodology explanation
   - Results summary with statistics
   - Key insights and patterns discovered
   - Recommendations for when to use each technique

3. **Problem Dataset:**
   - 30 original test problems (10 per category)
   - Answer key with explanations
   - Difficulty ratings (1-5 scale)

4. **Demo Video** (3-5 minutes):
   - Show your tool in action
   - Highlight most interesting findings
   - Demonstrate best and worst prompt examples

## 🏆 Evaluation Criteria

### Technical Implementation (40%)
- Tool functionality and reliability
- Code quality and organization
- Error handling and user experience
- Integration of all prompt techniques

### Experimental Design (35%)
- Quality and variety of test problems
- Systematic comparison methodology
- Statistical rigor in analysis
- Objective evaluation criteria

### Analysis and Insights (25%)
- Depth of findings and conclusions
- Clear communication of results
- Practical recommendations
- Understanding of underlying concepts

## 🎯 Bonus Opportunities (+10 points each)

1. **Advanced CoT Variants:**
   - Test Tree-of-Thought or Graph-of-Thought prompting
   - Compare different reasoning instruction styles
   - Implement self-consistency decoding

2. **Automated Evaluation:**
   - Build automatic accuracy checking for math problems
   - Implement reasoning quality scoring using another LLM
   - Create performance benchmarking suite

3. **Real-World Application:**
   - Apply techniques to a practical use case (tutoring, customer service, etc.)
   - Demonstrate measurable improvement in a real scenario
   - Include user feedback and iteration

## 📅 Submission Timeline

- **Day 3**: Submit problem dataset and initial tool prototype
- **Day 5**: Complete testing and begin analysis report
- **Day 7**: Final submission with all deliverables

## 🆘 Getting Help

### Common Challenges
1. **Poor Example Selection**: Examples should be representative and clear
2. **Inconsistent Evaluation**: Use objective criteria, not subjective judgment
3. **Token Limit Issues**: Manage prompt length vs context needs
4. **Statistical Significance**: Ensure sufficient test cases for meaningful results

### Resources for Support
- **Office Hours**: Monday/Wednesday 2-4 PM for technical help
- **Peer Review Sessions**: Friday 1-2 PM for feedback exchange
- **Online Forum**: 24/7 peer and instructor support
- **Example Solutions**: Available after submission deadline

## 🎓 Learning Outcomes

Upon completion, you will:
- Master the three fundamental prompting approaches
- Understand when and why to use each technique
- Build tools for systematic prompt evaluation
- Develop scientific thinking about AI performance
- Gain practical experience with reasoning enhancement

**This assignment bridges theoretical understanding with practical application - focus on building something you'd actually use in real projects!**

