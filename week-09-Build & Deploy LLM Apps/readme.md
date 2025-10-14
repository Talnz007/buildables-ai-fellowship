# Week 9 – Build & Deploy LLM Apps (FastAPI + Streamlit + Free Hosting)

## Overview
Turn your prompt-engineering hacks into **shareable web products**.  
You’ll containerise an LLM flow behind a FastAPI endpoint, wrap it in a **Streamlit chat UI**, and ship it to the internet on a **zero-rupee** plan (Railway, Render, Streamlit Cloud, Hugging Face Spaces, or any other free host).

## Resources
* [FastAPI Official Tutorial](https://fastapi.tiangolo.com/tutorial/)
* [Streamlit Docs – Chat Elements](https://docs.streamlit.io/develop/api-reference/chat)
* [Deploy FastAPI on Railway FREE](https://docs.railway.app/deploy/fastapi)
* [Hugging Face Spaces – Streamlit Docker](https://huggingface.co/docs/hub/spaces-sdks-streamlit)
* [Environment Secrets – keep your OpenAI key safe](https://docs.railway.app/guides/variables)
* [Urdu/English Bilingual Chat Template](https://github.com/haseeb-heaven/UrduChatGPT)

## Assignment
**DO NOT clone the class “hello-world” chatbot.**  
Identify a **real pain-point** around you and build a **micro-SaaS** that solves it in ≤ 2 clicks.  
Host it free, grab a public URL, and share with at least **three real users** for feedback.

Inspirational sparks:
* Hostel food rating: students type a dish name → LLM predicts “today’s taste score” → displays emoji meter.  
* Pakistani startup law helper: upload page-1 of an SECP form → LLM fills the rest in Roman-Urdu → download PDF.  
* Local cricket league: type ball-by-ball text commentary → LLM generates 30-second Urdu commentary audio (via free TTS) → play button.  
* Family grocery: photo of fridge → LLM lists what’s missing + cheapest nearby store (scraped from Carrefour IKEA website).  
* Hunza tourism: drop any landscape photo → LLM writes a 140-character Instagram caption in English + Urdu hashtags.  

Feel free to **invent your own** idea; anything that **calls an LLM** and is **usable via browser** counts.

**Submission Deadline:** DEADLINE_HERE

## Submission Guidelines
1. **Public URL** (must open without VPN).  
2. **GitHub repo** with:
   - README (problem, demo GIF, local setup)  
   - `requirements.txt` or `Dockerfile`  
   - `app.py` (Streamlit) + `api.py` (FastAPI) if hybrid  
3. **2-min Loom/video** showing:
   - User landing → interaction → LLM answer → happy user.  
4. **Feedback sheet** (Google Form) filled by ≥ 3 real users.

## Optional Challenges
* **Dockerise** the whole stack and push to Hugging Face Spaces (CPU free tier).  
* Add **caching (Redis or in-memory)** so repeated questions don’t burn tokens.  
* Implement **user login via Google** and store history in free Firebase.  
* Support **Urdu speech-to-text** (Whisper API) and return spoken answers.  
* Stress-test: handle 10 concurrent users with **async FastAPI** and report latency.
