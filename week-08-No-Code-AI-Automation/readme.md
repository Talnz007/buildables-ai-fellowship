# Week 8 – No-Code AI Automation (Zapier, Make, n8n, or ANY Free Tool)

## Overview
This week you’ll glue together **LLMs + everyday triggers**—emails, WhatsApp, cron, webhooks—using **ANY no-code platform you like**: Zapier, Make, Pabbly, IFTTT, Activepieces, self-hosted n8n, even Google AppSheet.  
Goal: **automate a real Pakistani headache** without writing backend code and without spending a rupee.

## Resources
* [Zapier ChatGPT Integration – Urdu walk-through](https://www.youtube.com/watch?v=3tGpC3b9Kik)
* [Make.com OpenAI Modules](https://www.make.com/en/help/app/openai)
* [n8n on Raspberry Pi – local & free](https://docs.n8n.io/hosting/installation/npm/)
* [Activepieces Cloud – 1 000 tasks/mo free](https://www.activepieces.com)
* [Pabbly Connect – lifetime free internal tasks](https://www.pabbly.com/connect)
* [Webhook vs Gmail Push – Pakistan 4G latency](https://propakistani.pk/how-to/webhook-vs-polling-pakistan/)

## Assignment
**Do NOT clone the class demo.**  
Pick **any no-code tool** (free tier or OSS) and build a **hands-off workflow** that solves a **local or personal problem** in Pakistan.  
Your flow must run **at least once automatically** (trigger → LLM → action) and cost **zero PKR** on the free plan.

Inspirational sparks (mix & match):
* Hostel mess: daily JPG menu photo → Gemini Vision → Urdu summary → WhatsApp group.  
* Load-shedding: scrape IESCO outage table → GPT-4 → SMS 30 min before your block.  
* Ramazan sasta bazaar: Punjab gov PDF price list → LLM → cheapest 5 items → Telegram channel.  
* Charity drive: handwritten donor sheet photo → LLM → Google Sheet + personalized Urdu thank-you SMS.  
* Cricket fever: PCB RSS → LLM 3-line Urdu summary → auto-post to Facebook page.  
* Family finances: screenshot of HBL debit alerts → LLM categorises → free Notion budget table updated.  

Feel free to **invent your own**; any trigger + any LLM + any action counts.

**Submission Deadline:** DEADLINE_HERE

## Submission Guidelines
1. **Public share-link** (or exported JSON / YAML) of your working flow.  
2. **One-pager** (Google Doc or Notion) containing:
   - Problem & target user  
   - Tool chosen + why free tier is enough  
   - Cost in PKR (show 0)  
3. **60-second vertical screen-recording** showing trigger firing and final Urdu/English output on a Pakistani network.

## Optional Challenges
* **Self-host n8n** on a Raspberry Pi behind PTCL router (port-forward or Cloudflare tunnel).  
* Add **error path**: if LLM fails, log to Airtable and send yourself a missed-call alert.  
* Chain **two different free LLMs** (e.g., GPT-4 for summary → local Urdu model for ghazal caption).  
* Expose an **Activepieces webhook** so classmates can trigger your flow with a simple POST.  
* Benchmark **execution time & cost** between Zapier free, Make free, and self-hosted n8n for 50 runs.
