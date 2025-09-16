# Week 5: LLM Agents & Retrieval Solutions

**Duration**: August 29 - September 4  
**Track**: Buildables AI Fellowship  
**Topics**: LangChain, LlamaIndex, Agent Development, RAG Systems

## 🎯 Week Overview

This week focuses on building intelligent agents and retrieval systems using LangChain and LlamaIndex. You'll learn to create agents that can use external tools and build systems that can intelligently retrieve and process documents to answer questions.

## 📋 Learning Objectives

By the end of this week, you will be able to:
- Build LLM agents using LangChain framework
- Integrate external tools (calculator, web search, APIs) into agents
- Create document retrieval systems using LlamaIndex
- Implement vector storage and semantic search
- Design memory systems for conversational agents
- Deploy agent-based solutions for real-world problems

## 📚 Resources

### 📹 Video Resources
- [week5-videos.md](./week5-videos.md) - Curated video tutorials and demonstrations
- Core topics: LangChain agents, LlamaIndex implementation, memory management

### 📖 Documentation & Links  
- [week5-resources.md](./week5-resources.md) - Essential documentation and code examples
- API references, Python packages, and troubleshooting guides

### 🎯 Assignment Details
- [week5-assignment.md](./week5-assignment.md) - Complete assignment requirements and evaluation criteria
- **New Format**: Real-world problem solving with video demos and live presentations

## 🚀 Quick Start Guide

### Prerequisites
- Python 3.8+
- OpenAI API key
- Basic understanding of LLMs from previous weeks

### Environment Setup
```bash
# Clone the repository
git clone https://github.com/Talnz007/buildables-ai-fellowship.git
cd buildables-ai-fellowship/week-05-agents-retrieval

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Add your API keys to .env file
```

### Required Dependencies
```bash
# Core packages
pip install langchain==0.1.0
pip install llamaindex==0.9.0
pip install openai>=1.0.0

# Vector stores and utilities
pip install faiss-cpu==1.7.4
pip install chromadb==0.4.0
pip install python-dotenv==1.0.0
pip install streamlit==1.28.0
```

## 🛠️ Week Structure

### Day 1-2: Foundation
- **Setup**: Development environment and API configurations
- **LangChain Basics**: Agent types and tool integration
- **First Agent**: Simple calculator or web search agent

### Day 3-4: Document Processing
- **LlamaIndex**: Document indexing and vector storage
- **RAG Systems**: Building retrieval-augmented generation
- **Integration**: Combining agents with document retrieval

### Day 5-6: Real-World Application
- **Problem Identification**: Find a real problem to solve
- **Solution Development**: Build working prototype
- **Testing & Documentation**: Validate with real data

### Day 7: Presentation
- **Video Demo**: 5-7 minute demonstration
- **Live Q&A**: Present during follow-up call

## 🎯 Assignment: Real-World Problem Solving

### **New Assignment Format** 
Starting Week 5, you'll identify real problems and build solutions rather than complete generic exercises.

### Deliverables
1. **Working Solution**: LangChain/LlamaIndex application solving a real problem
2. **Video Demo**: 5-7 minute explanation of problem, solution, and impact
3. **Live Presentation**: Q&A session during follow-up call
4. **Code Repository**: Complete, documented, and deployable solution

### Technical Requirements
- ✅ Use LangChain OR LlamaIndex (or both)
- ✅ Integrate at least one external tool (calculator, web search, API)
- ✅ Include proper error handling and user feedback
- ✅ Test with real documents/data
- ✅ Deploy working demo (local acceptable)

## 📁 Repository Structure

```
week-05-agents-retrieval/
├── README.md                 # This file
├── week5-videos.md          # Video resources
├── week5-resources.md       # Documentation and links
├── week5-assignment.md      # Assignment details
├── requirements.txt         # Python dependencies
├── .env.example            # Environment variable template
├── examples/               # Code examples and templates
│   ├── langchain-agent/
│   ├── llamaindex-rag/
│   └── combined-solution/
├── templates/              # Project templates
└── docs/                   # Additional documentation
```

## 💡 Project Ideas (Find Your Own!)

### Business Applications
- **Customer Support Agent**: Automated ticket handling for specific industry
- **Document Analysis**: Legal contracts, medical records, financial reports
- **Research Assistant**: Academic or business research automation
- **Compliance Checker**: Automated document compliance verification

### Personal Productivity
- **Knowledge Manager**: Personal note organization and retrieval  
- **Email Assistant**: Intelligent email processing and responses
- **Learning Companion**: Educational content interaction
- **Task Automation**: Personal workflow optimization

## 🏆 Success Criteria

### What Makes a Great Project
1. **Real Problem**: Solves actual pain points for real users
2. **Measurable Impact**: Quantified time savings or quality improvements
3. **Technical Depth**: Sophisticated use of agent capabilities  
4. **User Validation**: Feedback from actual users
5. **Professional Quality**: Clean code, documentation, and presentation

### Example Success Metrics
- "Reduced contract review time by 3 hours per document"
- "Improved research efficiency by 70%"
- "Automated 40% of customer support tickets"
- "Organized 1000+ personal notes with 95% retrieval accuracy"

## 🆘 Getting Help

### Support Channels
- **Office Hours**: Daily 7-9 PM PKT
- **Discord**: #week5-agents-help
- **Documentation**: Check resources folder for troubleshooting

### Common Issues
- **API Rate Limits**: Implement exponential backoff
- **Memory Issues**: Use conversation summarization  
- **Tool Integration**: Check framework documentation
- **Performance**: Optimize chunk sizes and vector storage

## 🎬 Submission Guidelines

### Video Demo Requirements (5-7 minutes)
1. **Problem** (1 min): What problem are you solving?
2. **Solution** (2 mins): Technical approach and architecture
3. **Demo** (2-3 mins): Working system with real data
4. **Impact** (1 min): Results and measurements
5. **Challenges** (1 min): Technical problems solved

### Repository Requirements
- Complete source code with documentation
- README with setup instructions
- Video link in repository
- Working deployment (local or cloud)

## 🚀 Ready to Start?

1. Review the [assignment details](./week5-assignment.md)
2. Check out [video resources](./week5-videos.md) for tutorials
3. Use [resources.md](./week5-resources.md) for documentation
4. Set up your development environment
5. Identify a real problem to solve
6. Start building! 

**Remember**: The goal is to build something genuinely useful, not just complete a technical exercise. Think like an entrepreneur solving real problems!

---

*Part of the Buildables AI Fellowship Program*
