# Week 4 Assignment: Build Your Own AI News Summarizer & Q&A Tool 🚀

## 🎯 Objective

This week, you’ll build a Python project that uses a Large Language Model (LLM) API (OpenAI or Google Gemini) to:
1. Summarize a news article of your choice.  
2. Answer questions about that article.  
3. Experiment with model parameters to see how output changes.  

Pick articles from a topic you actually enjoy (tech, sports, entertainment, etc.) so this feels fun and not just homework.

---

## 🛠️ Project Requirements

### Part 1: Summarization Engine
1. **Choose an Article**  
   Select a news article (BBC, Reuters, TechCrunch, ESPN, etc.) and copy its text into your script.  

2. **Create the Script**  
   Write a Python script called `summarizer.py`.  

3. **API Call**  
   Send the article text to an LLM API and ask for a 3–4 sentence summary.  

4. **Output**  
   Print both:  
   - Original article length (words or characters)  
   - The generated summary  

---

### Part 2: Interactive Q&A
1. **Extend Your Script**  
   After summarizing, allow the user to ask at least **3 questions** about the article.  

2. **Craft Prompts**  
   Each Q&A should include both the question and the article text.  
   Example:  
```

Based on the article below, \[QUESTION]?
Article: \[ARTICLE TEXT HERE]

```

3. **Display Results**  
Print each question followed by the model’s answer.  

---

### Part 3: Experiment with Parameters 🎛️
1. **Run with Different Temperatures**  
Generate summaries three times on the same article:  
- `0.1` (deterministic, robotic)  
- `0.7` (balanced)  
- `1.0` (creative, maybe chaotic)  

2. **Record Observations**  
In a file called `observations.md`, describe how the summaries changed.  
Note which temperature gave the most useful/fun results.  

---

## 💡 Bonus Challenge (Optional)
- Turn your script into a **CLI tool** where the user pastes an article URL and chats with it.  
- Add a **fun mode** where the summary comes in the style of a pirate, comedian, or sports commentator.  
- Wrap it in a simple Flask/Streamlit app.  

---

## 📦 Submission
Submit the following:  
- `summarizer.py` (your Python script)  
- `observations.md` (your notes on parameter tuning)  
