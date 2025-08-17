# Week 1 Assignment: LLM Basics

## 🎯 Assignment Overview

Welcome to the Buildables AI Fellowship! For your first assignment, you will create a **Text Analysis Tool** that demonstrates your understanding of LLM basics, tokenization, and API usage. Your tool should analyze text inputs and provide insights using different LLM capabilities.

---

## 📋 Requirements

### Core Features (Required)
1.  **Text Summarization** using Gemini, Mistral, ChatGPT API (We suggest using Gemini as it is powerful and has a generous free tier, but feel free to explore others like Mistral or any other LLM you prefer).
2.  **Tokenization Analysis** using Hugging Face tokenizers.
3.  **Multi-model Comparison** (compare at least 2 different models to see how they perform).
4.  **Token Usage Tracking** and cost estimation.

### Advanced Features (Choose 2)
5.  **Language Detection** and analysis.
6.  **Sentiment Analysis** using LLM.
7.  **Writing Style Analysis** (formal/informal, complexity, etc.).
8.  **Text Statistics** (readability scores, word frequency).
9.  **Batch Processing** for multiple texts.
10. **Export Results** (JSON, CSV, or PDF).

---

## 🛠 Technical Specifications

### Required Technology Stack
-   Python 3.9+
-   LLM API
-   Hugging Face Transformers
-   At least one additional library of your choice

### Project Structure

### Project Structure
```
your-project-name/
├── README.md
├── main.py
├── requirements.txt
├── config.py
├── utils/
│   ├── __init__.py
│   ├── llm_helpers.py
│   └── tokenizer_helpers.py
├── data/
│   ├── sample_texts/
│   └── results/
├── tests/
│   └── test_main.py
└── docs/
    └── usage_examples.md
```

## 📝 Specific Tasks

### Task 1: API Integration (25 points)
-   Set up your LLM API client.
-   Implement error handling and rate limiting.
-   Create reusable functions for API calls.
-   Document your API usage patterns.

### Task 2: Tokenization Explorer (25 points)
-   Compare tokenization across different models (e.g., GPT, BERT).
-   Visualize token boundaries.
-   Calculate and display token statistics.
-   Handle edge cases (empty strings, special characters).

### Task 3: Analysis Features (30 points)
-   Implement the core summarization feature.
-   Add your chosen advanced features.
-   Ensure robust error handling.
-   Optimize for performance.

### Task 4: User Interface (20 points)
-   Create an intuitive command-line interface OR
-   Build a simple web interface using Streamlit/Gradio.
-   Include help documentation.
-   Handle user input validation.

---

## 📊 Sample Inputs for Testing

Test your tool with these diverse text types:

1.  **News Article** (300-500 words)
2.  **Academic Abstract** (150-200 words)
3.  **Social Media Post** (50-100 words)
4.  **Technical Documentation** (400-600 words)
5.  **Creative Writing** (200-300 words)

---

## 🏆 Evaluation Rubric

### Technical Implementation (40%)
-   Code quality and organization.
-   Proper API usage.
-   Error handling.
-   Performance considerations.

### Feature Completeness (30%)
-   All required features implemented.
-   Advanced features working correctly.
-   Edge case handling.

### Documentation (20%)
-   Clear `README` with setup instructions.
-   Code comments and docstrings.
-   Usage examples.
-   API documentation.

### Innovation & Creativity (10%)
-   Unique approach or features.
-   User experience improvements.
-   Additional insights or visualizations.

---

## 📅 Submission Guidelines

### Deadline
**Sunday, August 24th, 11:59 PM**

### Submission Format
1.  **GitHub Repository**: Create a public repo with your project.
2.  **Demo Video**: Create a 3-5 minute walkthrough (upload to YouTube/Loom).
3.  **Google Classroom**: Submit both your repository link and your demo video link as part of your assignment submission.

### Submission Checklist
-   [ ] All required files in proper structure.
-   [ ] `README.md` with setup and usage instructions.
-   [ ] `requirements.txt` with all dependencies.
-   [ ] Working code that runs without errors.
-   [ ] Demo video showcasing key features.
-   [ ] At least 3 meaningful git commits.

---

## 📈 Building in Public: A Quick Guide

We highly encourage you to **build in public** throughout this fellowship. This means sharing your work, progress, and key learnings on platforms like **LinkedIn**.

**Why should you do this?**
-   **Showcase your skills:** This creates a living portfolio that demonstrates your technical abilities to potential employers and collaborators.
-   **Build a professional network:** Engaging with the AI community on LinkedIn can lead to new connections and opportunities.
-   **Gain traction:** Sharing your projects can attract attention and feedback, helping you refine your work and get noticed.

**What to share on LinkedIn:**
-   **Your progress:** Post updates about the features you've implemented and the challenges you've overcome.
-   **Your code:** Share a link to your GitHub repository.
-   **Your demo video:** Post your walkthrough video to visually showcase your project.

---

## 🎓 Learning Objectives Assessment

By completing this assignment, you should be able to:
-   [ ] Make API calls to an LLM with proper error handling.
-   [ ] Compare tokenization strategies across different models.
-   [ ] Understand token limits and cost implications.
-   [ ] Build a complete Python application with good structure.
-   [ ] Document and present your technical work.

---

## 💡 Getting Started Tips

1.  **Start Early**: Begin with environment setup on Day 1.
2.  **Test Incrementally**: Build one feature at a time.
3.  **Ask Questions**: Use our dedicated Discord channel and office hours.
4.  **Review Examples**: Check our sample project for inspiration.
5.  **Plan Your Demo**: Think about what you want to showcase.

---

## 🆘 Common Issues & Solutions

### API Key Issues
-   Ensure your `.env` file is properly configured.
-   Check API key permissions and billing.
-   Review rate limiting documentation.

### Tokenization Confusion
-   Start with simple examples.
-   Use online tokenizer tools for comparison.
-   Understand model-specific tokenization.

### Code Organization
-   Follow the suggested project structure.
-   Use meaningful function names.
-   Keep functions small and focused.

---

## 🏅 Bonus Challenges

For extra credit consideration:
1.  **Performance Benchmark**: Compare response times across models.
2.  **Cost Analysis**: Build detailed cost tracking.
3.  **Multilingual Support**: Handle non-English text.
4.  **Interactive Visualization**: Create charts/graphs of analysis results.

---

## 📞 Getting Help

-   **Office Hours**: I am generally available after 8 PM, but I'll try to assist whenever I have the time. These are dedicated periods for one-on-one help and to ask questions about the assignments or course material. Check the Google Classroom calendar for more specific times.
-   **Discord**: If you have any issues, feel free to ping me or post your problem in the Discord channel. I will try to assist you as soon as I am available. You should also feel free to help other fellows if you see a problem you can fix. This is a collaborative environment, and helping each other is a great way to learn.
-   **Peer Review**: Partner with another fellow to try out their project, test it, and do a review. This is an excellent way to get feedback on your work and learn from your peers.
-   **Documentation**: Always remember to review the official API documentation. It is the most reliable source of information for troubleshooting and understanding how to use a service.

Good luck, and remember: the goal is learning, not perfection! 
