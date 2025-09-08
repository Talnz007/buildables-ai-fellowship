# Week 4 Assignment: News Article Summarizer & Q&A Tool

## Objective

Your goal is to build a Python script that uses a Large Language Model (LLM) API (either OpenAI or Google Gemini) to perform two key tasks:
1.  [cite_start]Summarize a given news article[cite: 3].
2.  [cite_start]Answer specific questions about the content of that article[cite: 3].

[cite_start]This project will give you hands-on experience with making API calls, processing text, and manipulating model parameters to change the output[cite: 3].

## Project Requirements

### Part 1: Article Summarization

1.  **Choose an Article**: Find a news article online (e.g., from BBC News, Reuters, TechCrunch).
2.  **Write a Script**: Create a Python script (`summarizer.py`).
3.  **API Call**: In your script, make an API call to an LLM. [cite_start]Your prompt should instruct the model to summarize the article you chose[cite: 3].
    * **Prompt Example**: "Please summarize the following news article in three concise sentences: [Paste article text here]"
4.  **Print the Output**: Display the original article length (in characters or words) and the generated summary.

### Part 2: Question Answering

1.  **Extend Your Script**: Add functionality to ask at least three questions about the article.
2.  **Craft Q&A Prompts**: For each question, create a new prompt that includes both the question and the full article text.
    * [cite_start]**Prompt Example**: "Based on the article provided, what are the key points? [Paste article text here]" [cite: 3]
3.  **Display Results**: Print each question followed by the model's answer.

### Part 3: Experiment with Parameters

1.  **Vary Temperature**: Run your summarization script on the same article three times with different `temperature` settings:
    * `temperature = 0.1` (Very deterministic, factual)
    * `temperature = 0.7` (Balanced, creative)
    * `temperature = 1.0` (Highly creative, potentially less accurate)
2.  [cite_start]**Record Observations**: In a separate markdown file named `observations.md`, write a few sentences describing how the summary changed with each temperature setting[cite: 3]. Which one produced the best result?

## Submission

Please submit the following files:
* `summarizer.py` (your completed Python script)
* `observations.md` (your notes on parameter tuning)
