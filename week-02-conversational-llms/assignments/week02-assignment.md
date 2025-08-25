# Week 2 Assignment: Building Your First Conversational LLM Interface

## Objective
Create a functional chat interface that demonstrates understanding of conversational LLMs and prompt engineering fundamentals.

## Tasks

### Part 1: Basic Chat Implementation (40 points)
1. Build a command-line chat loop that:
   - Takes user input
   - Sends it to OpenAI's API using proper chat format
   - Displays the response
   - Continues until user types 'exit'

2. Requirements:
   - Use the chat completions API (not the older completions API)
   - Implement proper error handling
   - Maintain conversation history for context

### Part 2: System Prompt Experimentation (35 points)
Create 3 different chat experiences by varying the system prompt:
1. **Professional Assistant**: Formal, business-like responses
2. **Creative Companion**: Imaginative, artistic responses  
3. **Technical Expert**: Detailed, technical explanations

Compare and document how responses differ for the same user questions.

### Part 3: Streamlit Interface (25 points)
Convert your CLI chat into a web interface using Streamlit:
- Clean, user-friendly design
- Message history display
- System prompt selector
- Optional: Message export functionality

## Submission Requirements
- Working code files
- Screenshots of different system prompt behaviors
- Brief reflection (200-300 words) on what you learned about prompt engineering

## Evaluation Criteria
- **Functionality**: Does the chat interface work correctly?
- **Code Quality**: Clean, commented, error-handled code
- **Prompt Engineering**: Effective use of system prompts
- **Documentation**: Clear explanations and comparisons

## Bonus Points (5 points)
Implement conversation memory that persists across sessions using local file storage.
