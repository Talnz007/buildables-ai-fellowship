# Week 5 Resources - LLM Agents & Retrieval

## Essential Documentation

### LangChain
- **LangChain Official Docs** - [https://docs.langchain.com](https://docs.langchain.com)
- **Agent Types Documentation** - [https://docs.langchain.com/docs/modules/agents/](https://docs.langchain.com/docs/modules/agents/)
- **Tools Documentation** - [https://docs.langchain.com/docs/modules/agents/tools/](https://docs.langchain.com/docs/modules/agents/tools/)
- **Memory Documentation** - [https://docs.langchain.com/docs/modules/memory/](https://docs.langchain.com/docs/modules/memory/)

### LlamaIndex
- **LlamaIndex Official Docs** - [https://docs.llamaindex.ai](https://docs.llamaindex.ai)
- **Query Engines Guide** - [https://docs.llamaindex.ai/en/stable/module_guides/deploying/query_engine/](https://docs.llamaindex.ai/en/stable/module_guides/deploying/query_engine/)
- **Data Connectors** - [https://docs.llamaindex.ai/en/stable/module_guides/loading/](https://docs.llamaindex.ai/en/stable/module_guides/loading/)
- **Vector Stores Integration** - [https://docs.llamaindex.ai/en/stable/module_guides/storing/](https://docs.llamaindex.ai/en/stable/module_guides/storing/)

## Code Examples and Tutorials

### Agent Creation Tutorials
- **How to Create an Agent With Langchain, Llama Index and CrewAI** - [https://scrapegraphai.com/blog/how-to-create-agent-with-frameworks/](https://scrapegraphai.com/blog/how-to-create-agent-with-frameworks/)
- **LangChain Agents Tutorial** - Step-by-step agent building
- **Multi-Agent Systems** - Coordinating multiple agents

### Tool Integration Examples
- **Calculator Tool Implementation** - Mathematical operations
- **Web Search Tool Setup** - DuckDuckGo and Google Search integration
- **API Tool Creation** - Custom API integrations
- **File System Tools** - Document manipulation capabilities

## Required Python Packages

```bash
# Core packages
pip install langchain==0.1.0
pip install llamaindex==0.9.0
pip install openai>=1.0.0

# Vector stores
pip install faiss-cpu==1.7.4
pip install chromadb==0.4.0

# Document processing
pip install pypdf2==3.0.1
pip install python-docx==0.8.11
pip install beautifulsoup4==4.12.0

# Web tools
pip install duckduckgo-search==3.9.0
pip install requests==2.31.0

# Utilities
pip install python-dotenv==1.0.0
pip install streamlit==1.28.0
```

## Vector Database Options

### Local Solutions
- **FAISS** - Facebook AI Similarity Search (free, local)
- **Chroma** - Open-source embedding database
- **Qdrant** - Vector similarity search engine

### Cloud Solutions
- **Pinecone** - Managed vector database service
- **Weaviate** - Open-source vector search engine
- **Milvus** - Cloud-native vector database

## API Keys and Setup

### Required API Keys
```bash
# .env file setup
OPENAI_API_KEY=your_openai_key_here
ANTHROPIC_API_KEY=your_anthropic_key_here  # Optional
SERPAPI_KEY=your_serpapi_key_here  # For web search
```

### Environment Setup
```python
# config.py
import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
SERPAPI_KEY = os.getenv("SERPAPI_KEY")
```

## Common Tools for Agents

### Built-in Tools
- **Calculator** - Mathematical operations
- **Wikipedia** - Knowledge lookup
- **DuckDuckGo Search** - Web search capabilities
- **Shell Tool** - System commands (use carefully)

### Custom Tool Creation
```python
from langchain.tools import BaseTool
from typing import Optional

class CustomTool(BaseTool):
    name = "custom_tool"
    description = "Tool description here"
    
    def _run(self, query: str) -> str:
        # Tool implementation
        return "Tool response"
```

## Memory Types

### LangChain Memory
- **ConversationBufferMemory** - Simple conversation history
- **ConversationBufferWindowMemory** - Limited window memory
- **ConversationSummaryMemory** - Summarized conversation history
- **VectorStoreRetrieverMemory** - Vector-based memory retrieval

### Memory Implementation
```python
from langchain.memory import ConversationBufferMemory

memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)
```

## Best Practices

### Agent Design
1. **Clear Tool Descriptions** - Help the agent understand when to use each tool
2. **Error Handling** - Implement robust error handling for tool failures
3. **Output Parsing** - Structure agent outputs for consistency
4. **Cost Optimization** - Monitor token usage and API calls

### Document Processing
1. **Chunking Strategy** - Optimal chunk sizes (typically 500-1000 tokens)
2. **Overlap Management** - 10-20% overlap between chunks
3. **Metadata Preservation** - Keep source information and context
4. **Quality Control** - Validate document processing results

## Troubleshooting Guide

### Common Issues
- **API Rate Limits** - Implement retry logic and backoff
- **Memory Issues** - Optimize chunk sizes and vector storage
- **Tool Failures** - Add fallback mechanisms
- **Context Length** - Manage conversation history length

### Debug Tools
```python
import logging
logging.basicConfig(level=logging.DEBUG)

# Enable LangChain debugging
import langchain
langchain.debug = True
```

## Example Projects for Inspiration

### Business Applications
- **Customer Support Agent** - Automated ticket handling
- **Research Assistant** - Academic paper analysis
- **Document Q&A System** - Company knowledge base
- **Content Generation Pipeline** - Automated content creation

### Personal Use Cases
- **Personal Knowledge Manager** - Note organization and retrieval
- **Email Assistant** - Automated email processing
- **Learning Companion** - Educational content interaction
- **Task Automation** - Personal workflow optimization