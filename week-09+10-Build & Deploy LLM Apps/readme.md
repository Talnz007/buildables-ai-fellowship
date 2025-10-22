# Week 9–10 – Build & Deploy AI Agents (LangGraph + MCP + FastAPI + Streamlit)

## Overview
We’re taking the leap from “LLM apps” to **autonomous, context-aware AI agents**.  
This two-week sprint combines Week 9 and 10 into one powerful build phase where you’ll create an agent that can **reason, retrieve, and act** using the **Model Context Protocol (MCP)** and **LangGraph**.  
You’ll connect it to a **FastAPI backend**, wrap it in a **Streamlit (or any web)** interface, and **deploy it live** — because if it’s not deployed, it doesn’t exist.

## Resources
* [MCP Docs – Model Context Protocol](https://modelcontextprotocol.io/)
* [LangGraph Guide – Build Reactive AI Agents](https://langchain-ai.github.io/langgraph/)
* [FastAPI Official Tutorial](https://fastapi.tiangolo.com/tutorial/)
* [Streamlit Docs – Chat Elements](https://docs.streamlit.io/develop/api-reference/chat)
* [Deploy FastAPI on Render (Free)](https://render.com/docs/deploy-fastapi)
* [Streamlit Cloud Deployment Guide](https://docs.streamlit.io/streamlit-cloud/get-started)
* [Unsloth AI Fine-Tuning Notebook (Optional)](https://unsloth.ai/)
* [Environment Secrets – keep your API keys safe](https://docs.railway.app/guides/variables)

## Assignment
**DO NOT clone the class “hello-world” chatbot.**  
Build a **context-driven AI agent** that uses **MCP** to fetch or interact with external data (APIs, files, or tools).  
Your system must:
- Use **LangGraph** for reasoning flow.  
- Expose a **FastAPI backend** to handle MCP context or API calls.  
- Include a **Streamlit** or **Next.js + Vercel** frontend.  
- Be **publicly deployed** on a free tier (Render, Streamlit Cloud, Hugging Face Spaces, or Vercel).  

You may optionally:
- Fine-tune a small model with **Unsloth AI** or use context-based tuning.  
- Integrate your previous no-code automation (n8n/Zapier) through MCP.  

**Submission Deadline:** November 2, 2025

## Submission Guidelines
1. **Public URL** (must open without VPN).  
2. **GitHub repo** with:
   - README (problem statement, architecture, demo GIF, local setup).  
   - `requirements.txt` or `Dockerfile`.  
   - `app.py` (Streamlit UI) + `api.py` (FastAPI backend).  
3. **2-min demo video** showing:
   - User landing → interaction → agent reasoning → output.  
4. **Reflection section** in README describing how MCP improved your agent’s context awareness.

## Optional Challenges
* **Dockerise** the whole stack and host on Hugging Face Spaces (CPU free tier).  
* Add **caching (Redis / in-memory)** for repeated queries.  
* Implement **Google Login** and save chat history in Firebase/Supabase.  
* Add **speech interface** using Whisper STT + Coqui TTS (Urdu/English).  
* Perform a **stress test** with 10 concurrent users via async FastAPI and report latency.  
