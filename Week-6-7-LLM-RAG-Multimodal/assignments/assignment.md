# Week 6-7 Assignment: RAG & Multimodal AI Projects

**Submission Deadline:** Sunday, September 28th, 2025

---

## 📝 Assignment Overview

You will complete **TWO projects** this week:
1. **Mini RAG Application** - Build a document Q&A system
2. **Multimodal AI Application** - Create a vision-enabled AI tool

Both projects are required for full credit.

---

## 🎯 Project 1: Mini RAG Application

### Objective
Build a Retrieval-Augmented Generation system that can intelligently answer questions from PDF documents by retrieving relevant context.

### Requirements

#### Core Functionality
1. **PDF Text Extraction**
   - Extract text from at least one PDF document
   - Try BOTH PyPDF2 and pdfplumber
   - Document which works better for your PDF and why

2. **Text Processing**
   - Chunk the extracted text into manageable pieces
   - Experiment with at least 2 different chunk sizes
   - Document which size works better

3. **Vector Database**
   - Create embeddings for your text chunks
   - Store embeddings in FAISS (or similar vector DB)
   - Implement semantic search functionality

4. **RAG Pipeline**
   - Accept user questions
   - Retrieve top 3-5 relevant chunks
   - Send chunks + question to an LLM
   - Generate and return answer

5. **Comparison Analysis** (Critical!)
   - Test the SAME 5 questions with:
     - RAG (with retrieved context)
     - Non-RAG (just the question to LLM)
   - Document differences in answers
   - Analyze when RAG helps and when it doesn't

### Deliverables

1. **Code**
   - Jupyter notebook OR Python script
   - Well-commented and organized
   - Include error handling

2. **Test PDF**
   - The PDF you used for testing
   - Should be substantial (at least 10 pages)
   - Could be: research paper, technical doc, company report

3. **Comparison Document**
   - Table or document showing:
     - Questions asked
     - RAG answer
     - Non-RAG answer
     - Which was better and why
   - Your analysis of the results

4. **README Section**
   - Setup instructions
   - How to run your code
   - Libraries used
   - Challenges faced and solutions

### Evaluation Criteria (50 points)

| Criteria | Points |
|----------|--------|
| PDF extraction works correctly | 8 |
| Chunking and embeddings implemented | 8 |
| Vector database functioning | 8 |
| RAG pipeline works end-to-end | 10 |
| Comparison analysis (RAG vs non-RAG) | 10 |
| Code quality and documentation | 6 |

---

## 🎯 Project 2: Multimodal AI Application

### Objective
Create an application that uses vision-enabled LLMs (Gemini Pro Vision or GPT-4o) to analyze images and process long-context documents.

### Requirements

#### Core Functionality

1. **Image Analysis (Multiple Types)**
   - Test on at least 3 different image types:
     - **Photograph:** Describe and analyze a photo
     - **Document/Screenshot:** Extract and structure text (OCR)
     - **Chart/Diagram:** Interpret visual data or diagrams

2. **Long-Context Processing**
   - Process a document with 50,000+ tokens
   - Ask at least 3 multi-part questions
   - Test the model's context understanding

3. **Practical Use Case**
   - Demonstrate one real-world application, such as:
     - Document scanner + Q&A system
     - Image-based information extraction
     - Visual content moderation
     - Accessibility tool (describe images for visually impaired)
     - Any other creative use case

### Deliverables

1. **Code**
   - Jupyter notebook OR Python script
   - Clear organization and comments
   - Error handling included

2. **Test Images**
   - At least 3 images (one of each type)
   - Include in your submission

3. **Output Examples**
   - Screenshots or saved outputs showing:
     - Image analysis results
     - OCR extraction
     - Chart interpretation
     - Long-context Q&A

4. **Use Case Documentation**
   - Brief description (300-500 words) explaining:
     - What problem your use case solves
     - How it works
     - Potential real-world applications

5. **Long-Context Test Results**
   - Document showing:
     - Size of document processed
     - Questions asked
     - Model responses
     - Whether it handled the full context correctly

### Evaluation Criteria (50 points)

| Criteria | Points |
|----------|--------|
| Image analysis on 3 types | 12 |
| Long-context processing (50K+ tokens) | 10 |
| Practical use case demonstrated | 10 |
| Output examples clear and complete | 8 |
| Code quality and documentation | 6 |
| Creativity and thoughtfulness | 4 |

---

## 📦 Submission Format

### Option 1: GitHub Repository (Recommended)

Create a repository with this structure:

```
your-name-week6-7/
├── project1-rag/
│   ├── rag_system.ipynb (or .py)
│   ├── sample.pdf
│   ├── comparison_analysis.md
│   └── README.md
├── project2-multimodal/
│   ├── multimodal_app.ipynb (or .py)
│   ├── images/
│   │   ├── photo.jpg
│   │   ├── document.png
│   │   └── chart.png
│   ├── outputs/
│   │   └── example_outputs.md
│   ├── use_case_description.md
│   └── README.md
├── requirements.txt
└── README.md (main)
```

**Submit:** Post your GitHub repository link in the Discord submission channel

### Option 2: Zip File

If not using GitHub, create a zip file with the same structure:
- Name it: `Week6-7_YourName.zip`
- Upload to the shared folder (link in Discord)

---

## 📋 Required Files Checklist

### For Both Projects
- [ ] Main README.md explaining both projects
- [ ] requirements.txt with all dependencies
- [ ] Clear setup and run instructions

### Project 1 (RAG)
- [ ] Working code (notebook or script)
- [ ] Sample PDF document
- [ ] Comparison analysis document
- [ ] Project-specific README

### Project 2 (Multimodal)
- [ ] Working code (notebook or script)
- [ ] 3+ test images
- [ ] Output examples
- [ ] Use case description
- [ ] Long-context test results
- [ ] Project-specific README

---

## 💡 Tips for Success

### General Tips
1. **Start Early:** Don't wait until the last few days
2. **Test Incrementally:** Test each component before moving to the next
3. **Document As You Go:** Write down issues and solutions immediately
4. **Ask for Help:** Use Discord, pair programming, office hours
5. **Use Version Control:** Commit frequently if using Git

### RAG Project Tips
1. Choose a PDF you're genuinely interested in
2. Start with a simple, clean PDF (avoid heavily formatted ones)
3. Test your extraction before building the full pipeline
4. Keep your first version simple, then improve
5. The comparison analysis is KEY - put real thought into it

### Multimodal Project Tips
1. Start with Gemini (easier API) before trying GPT-4o
2. Test with simple images first
3. For long-context, use a text file initially (easier to test)
4. Save your API responses (they cost money/tokens)
5. Be creative with your use case - this is your portfolio piece!

---

## 🚫 Common Mistakes to Avoid

1. **Not testing PDF extraction separately** - Always verify text extraction quality first
2. **Using tiny chunks** - Too small = poor context; test different sizes
3. **Forgetting to compare RAG vs non-RAG** - This is required!
4. **Not handling API errors** - Always add try/except blocks
5. **Poor documentation** - Future you (and graders) need to understand your code
6. **Submitting without testing** - Run your code fresh before submission
7. **Missing requirements.txt** - We can't run code without dependencies

---

## ❓ Frequently Asked Questions

### General Questions

**Q: Can I work in pairs?**
A: You can discuss and debug together, but submit your own individual work.

**Q: What if I get stuck?**
A: Post in Discord, attend office hours, or schedule a 1-on-1 call.

**Q: Can I use different models/libraries than suggested?**
A: Yes! Just document what you used and why.

### Project 1 (RAG) Questions

**Q: What PDF should I use?**
A: Any substantial document (10+ pages). Research papers, technical docs, or company reports work well.

**Q: Do I have to use FAISS?**
A: FAISS is recommended, but you can use Pinecone, Chroma, or similar alternatives.

**Q: How many questions should I test?**
A: Minimum 5 questions for the comparison. More is better!

**Q: What if RAG doesn't improve answers?**
A: That's valuable! Document why and discuss possible reasons.

### Project 2 (Multimodal) Questions

**Q: Which API should I use?**
A: Gemini is easier to start with. GPT-4o is fine if you're comfortable with OpenAI API.

**Q: How do I get 50,000 tokens?**
A: A book chapter or long article works. You can use Project Gutenberg texts.

**Q: Can I use the same use case as someone else?**
A: Yes, but make it your own implementation and add unique insights.

**Q: What if I don't have API credits?**
A: Gemini has a free tier. Reach out if you need help with credits.

---

## 🎯 Grading Rubric Summary

| Component | Points | Weight |
|-----------|--------|--------|
| **Project 1: RAG System** | 50 | 50% |
| - Functionality | 34 | |
| - Comparison Analysis | 10 | |
| - Code Quality | 6 | |
| **Project 2: Multimodal** | 50 | 50% |
| - Core Features | 32 | |
| - Use Case | 10 | |
| - Documentation | 8 | |
| **TOTAL** | **100** | **100%** |

### Bonus Points (up to +10)
- Exceptional creativity in use cases
- Going beyond requirements (hybrid search, re-ranking, etc.)
- Excellent documentation and analysis
- Helping other students significantly

---

## 📅 Important Dates

- **September 5:** Week begins, resources released
- **September 12:** Midpoint - RAG should be mostly done
- **September 20:** Support call (check Discord for time)
- **September 28:** FINAL DEADLINE (11:59 PM)

---

## 🆘 Getting Help

1. **Discord Channel:** #week-6-7-questions (fastest response)
2. **Support Call:** Scheduled session (announced in Discord)
3. **Office Hours:** DM instructor to book a slot
4. **Pair Programming:** Find a partner in #find-partners channel

---

## 🌟 What Makes a Great Submission?

### Excellent submissions have:
- ✅ Clean, well-organized code
- ✅ Comprehensive documentation
- ✅ Thoughtful analysis and insights
- ✅ Creative use cases
- ✅ Evidence of testing and iteration
- ✅ Clear outputs and examples
- ✅ Proper error handling
- ✅ Works when someone else runs it

### They avoid:
- ❌ Messy, uncommented code
- ❌ Missing dependencies or broken setup
- ❌ Shallow comparison analysis
- ❌ Generic, uninteresting use cases
- ❌ No testing or examples
- ❌ Poor documentation
- ❌ Code that doesn't run

---

## 🎓 Learning Outcomes

After completing these projects, you will:

1. Understand how RAG systems work end-to-end
2. Know when to use RAG vs. simple prompting
3. Have experience with vector databases
4. Be able to work with vision-enabled AI models
5. Understand long-context processing
6. Have two portfolio-worthy projects
7. Be ready for advanced AI application development

---

## 📢 Final Notes

- **Quality over Speed:** Take time to do it well
- **Document Everything:** Your future self will thank you
- **Test Thoroughly:** Run your code multiple times
- **Be Creative:** Make it interesting and unique
- **Ask Questions:** No question is too small
- **Have Fun:** These are genuinely cool technologies!

---

**Good luck! We're excited to see what you build! 🚀**

**Questions? Post in Discord #week-6-7-questions**
