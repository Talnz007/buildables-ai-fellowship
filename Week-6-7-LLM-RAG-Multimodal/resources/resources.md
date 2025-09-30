# Week 6-7 Resources: Readings & Documentation

Essential reading materials, documentation, and articles for RAG and Multimodal AI projects.

---

## 📚 Week 6: RAG & PDF Processing

### PDF Text Extraction

#### PyPDF2
- **Official Documentation:** https://pypdf2.readthedocs.io/
- **Getting Started Guide:** https://pypdf2.readthedocs.io/en/3.x/user/extract-text.html
- **Installation:** `pip install PyPDF2`
- **Best For:** Simple, text-based PDFs

#### pdfplumber
- **Official Documentation:** https://github.com/jsvine/pdfplumber
- **Usage Examples:** https://github.com/jsvine/pdfplumber#usage
- **Installation:** `pip install pdfplumber`
- **Best For:** Complex layouts, tables, structured documents

#### Comparison Article
- **PyPDF2 vs pdfplumber:** https://towardsdatascience.com/pdf-text-extraction-in-python-5b6ab9e92dd
- Discusses pros/cons of different libraries

---

### Embeddings & Vector Databases

#### Understanding Embeddings
- **What are Embeddings?** https://platform.openai.com/docs/guides/embeddings
  - OpenAI's clear explanation of embeddings
- **Sentence Transformers Documentation:** https://www.sbert.net/
  - Library for generating embeddings
- **Embedding Models Comparison:** https://www.sbert.net/docs/pretrained_models.html

#### FAISS (Facebook AI Similarity Search)
- **Official Documentation:** https://faiss.ai/
- **Getting Started:** https://github.com/facebookresearch/faiss/wiki/Getting-started
- **Tutorial:** https://www.pinecone.io/learn/faiss-tutorial/
- **Installation:** `pip install faiss-cpu` (or `faiss-gpu` for GPU support)

#### Alternative Vector Databases
- **Pinecone:** https://www.pinecone.io/ (cloud-based, easy to use)
- **Chroma:** https://www.trychroma.com/ (lightweight, open-source)
- **Weaviate:** https://weaviate.io/ (open-source, feature-rich)
- **pgvector:** https://github.com/pgvector/pgvector (PostgreSQL extension)

---

### RAG (Retrieval-Augmented Generation)

#### Core Concepts
- **Introduction to RAG:** https://www.pinecone.io/learn/retrieval-augmented-generation/
  - Comprehensive overview of RAG concepts
- **RAG Explained (Papers with Code):** https://paperswithcode.com/method/rag
  - Technical deep dive
- **LangChain RAG Tutorial:** https://python.langchain.com/docs/use_cases/question_answering/
  - Practical implementation guide

#### Best Practices
- **RAG Best Practices:** https://docs.llamaindex.ai/en/stable/optimizing/production_rag.html
  - Production-ready RAG systems
- **Chunking Strategies:** https://www.pinecone.io/learn/chunking-strategies/
  - How to split documents effectively
- **Improving RAG:** https://towardsdatascience.com/10-ways-to-improve-the-performance-of-retrieval-augmented-generation-systems-5fa2cee7cd5c

#### Advanced Topics
- **Hybrid Search:** https://www.pinecone.io/learn/hybrid-search-intro/
  - Combining semantic and keyword search
- **Re-ranking:** https://www.sbert.net/examples/applications/cross-encoder/README.html
  - Improving retrieval quality
- **Query Expansion:** https://arxiv.org/abs/2305.03653
  - Research paper on query transformation

---

### LangChain Framework
- **Official Documentation:** https://python.langchain.com/
- **RAG Use Cases:** https://python.langchain.com/docs/use_cases/question_answering/
- **Vector Stores:** https://python.langchain.com/docs/modules/data_connection/vectorstores/
- **Document Loaders:** https://python.langchain.com/docs/modules/data_connection/document_loaders/

---

## 📚 Week 7: Multimodal AI

### Google Gemini Vision

#### Official Documentation
- **Gemini API Docs:** https://ai.google.dev/gemini-api/docs
- **Vision Capabilities:** https://ai.google.dev/gemini-api/docs/vision
- **Quickstart Guide:** https://ai.google.dev/gemini-api/docs/get-started/tutorial?lang=python
- **API Reference:** https://ai.google.dev/api/python/google/generativeai

#### Getting Started
- **Google AI Studio:** https://aistudio.google.com/
  - Test Gemini in browser before coding
- **Python SDK:** `pip install google-generativeai`
- **Authentication:** https://ai.google.dev/gemini-api/docs/api-key

#### Capabilities
- **Long Context:** https://ai.google.dev/gemini-api/docs/long-context
  - Up to 1M tokens!
- **Multimodal Prompting:** https://ai.google.dev/gemini-api/docs/vision?lang=python
- **Best Practices:** https://ai.google.dev/gemini-api/docs/prompting-strategies

---

### OpenAI GPT-4o Vision

#### Official Documentation
- **Vision Guide:** https://platform.openai.com/docs/guides/vision
- **API Reference:** https://platform.openai.com/docs/api-reference/chat/create
- **Quickstart:** https://platform.openai.com/docs/quickstart
- **Python SDK:** `pip install openai`

#### Features & Limits
- **Supported Formats:** https://platform.openai.com/docs/guides/vision#what-type-of-files-can-i-upload
  - PNG, JPEG, WEBP, GIF
- **Limitations:** https://platform.openai.com/docs/guides/vision#limitations
- **Pricing:** https://openai.com/api/pricing/

---

### Multimodal AI Concepts

#### Understanding Multimodal Models
- **Multimodal AI Overview:** https://cloud.google.com/use-cases/multimodal-ai
- **Vision-Language Models:** https://huggingface.co/blog/vision-language-pretraining
- **How GPT-4o Works:** https://openai.com/index/hello-gpt-4o/

#### Use Cases & Applications
- **Multimodal Use Cases:** https://cloud.google.com/blog/products/ai-machine-learning/multimodal-generative-ai-search
- **OCR + Q&A Workflows:** https://ai.google.dev/gemini-api/docs/vision#technical-details-image
- **Document Understanding:** https://platform.openai.com/docs/guides/vision#uploading-base-64-encoded-images

---

### Long-Context Processing

#### Understanding Context Windows
- **What is Context Window?** https://www.anthropic.com/index/claude-2-1-prompting
- **Gemini 1.5 Context:** https://blog.google/technology/ai/google-gemini-next-generation-model-february-2024/
  - Breakthrough 1M token context
- **Managing Long Context:** https://ai.google.dev/gemini-api/docs/long-context

#### Best Practices
- **Prompting for Long Context:** https://ai.google.dev/gemini-api/docs/prompting-strategies
- **Optimizing Costs:** Consider RAG vs full context for your use case
- **Testing Limits:** Always verify what your model actually processes

---

## 🔧 Tools & Libraries

### Essential Python Libraries
```bash
# PDF Processing
pip install PyPDF2 pdfplumber

# Embeddings
pip install sentence-transformers

# Vector Database
pip install faiss-cpu

# LLM APIs
pip install google-generativeai openai anthropic

# Utilities
pip install python-dotenv pillow requests

# Optional: LangChain
pip install langchain
```

### Development Tools
- **Jupyter Notebooks:** https://jupyter.org/
- **VS Code Python Extension:** https://code.visualstudio.com/docs/languages/python
- **Google Colab:** https://colab.research.google.com/ (free GPU access)

---

## 📖 Recommended Reading

### Beginner-Friendly
1. **"What is RAG?"** - Pinecone Learn (15 min read)
2. **"Getting Started with FAISS"** - GitHub Wiki (20 min)
3. **"Gemini Vision Tutorial"** - Google AI Docs (30 min)

### Intermediate
1. **"Building Production RAG"** - LlamaIndex Docs (45 min)
2. **"Chunking Strategies Explained"** - Pinecone (30 min)
3. **"Multimodal AI Use Cases"** - Google Cloud (40 min)

### Advanced
1. **"Improving RAG Performance"** - TowardsDataScience (1 hour)
2. **"Hybrid Search Deep Dive"** - Pinecone (45 min)
3. **"Long-Context Strategies"** - Anthropic (1 hour)

---

## 📊 Research Papers (Optional)

### RAG
- **Original RAG Paper:** https://arxiv.org/abs/2005.11401
  - Lewis et al., 2020
- **Dense Passage Retrieval:** https://arxiv.org/abs/2004.04906
  - Foundation for modern retrieval

### Multimodal
- **Flamingo Paper:** https://arxiv.org/abs/2204.14198
  - Visual language models
- **CLIP Paper:** https://arxiv.org/abs/2103.00020
  - Vision-language pretraining

---

## 🎥 Supplementary Videos

See `videos_md.md` for curated video tutorials and walkthroughs.

---

## 💡 Pro Tips

### For RAG
1. **Start with documentation:** Read FAISS and Sentence Transformers docs first
2. **Test extraction quality:** Don't assume your PDF extracts cleanly
3. **Understand embeddings:** Know what your vectors represent
4. **Experiment with chunks:** Size matters for retrieval quality

### For Multimodal
1. **Try it in the browser first:** Use Google AI Studio before coding
2. **Read error messages:** API errors tell you exactly what's wrong
3. **Start small:** Test with simple images before complex ones
4. **Monitor usage:** Vision API calls can add up quickly

---

## 🔗 Quick Reference Links

### APIs & Keys
- **Google AI Studio:** https://aistudio.google.com/
- **OpenAI Platform:** https://platform.openai.com/
- **Anthropic Console:** https://console.anthropic.com/

### Community & Support
- **LangChain Discord:** https://discord.gg/langchain
- **OpenAI Forum:** https://community.openai.com/
- **Pinecone Community:** https://community.pinecone.io/

### Sample Datasets
- **Academic Papers:** https://arxiv.org/
- **Project Gutenberg:** https://www.gutenberg.org/ (for long-context testing)
- **Sample Images:** https://unsplash.com/ (free high-quality photos)

---

## 📝 Notes

- **Bookmark this page:** You'll reference it throughout the week
- **Links updated:** September 2025 - report broken links in Discord
- **API changes:** Check official docs for latest features
- **Cost awareness:** Some APIs have free tiers with limits

---

**Need more resources? Ask in Discord #week-6-7-questions!**
