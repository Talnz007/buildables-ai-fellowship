# Week 8 – Multimodal LLMs: Vision & Long-Context

## Overview
This week you’ll learn how to feed **images and long documents** into large language models (Gemini Pro Vision, GPT-4o, etc.) and extract insights that combine text + visual reasoning. You’ll also experiment with **very long context windows** to see how models handle multi-part questions across hundreds of pages.

## Resources
* [Gemini Vision API Quickstart](https://ai.google.dev/tutorials/web_quickstart#multi_modal )
* [GPT-4o Vision Guide – OpenAI Cookbook](https://github.com/openai/openai-cookbook/blob/main/examples/GPT_with_vision_for_video_understanding.ipynb )
* [Long-Context Best Practices – Anthropic](https://www.anthropic.com/index/long-context-tips )
* [Video: “Seeing with Language” – Google DeepMind](https://youtu.be/7pQ1c7fHN2k )
* [PyPI: `pdf2image` & `Pillow` for image prep](https://pypi.org/project/pdf2image/ )

## Assignment
**Do NOT rebuild the class demo.**  
Instead, look around you—home, campus, workplace, community—and spot a **real-world pain-point** that can be solved by **combining images (or very long text) with an LLM**. Build a tiny, working prototype that proves the idea.

Need sparks?  
* Snap photos of nutrition labels and ask the model to flag allergens for your roommate.  
* Feed the model a 100-page municipal report and create a 3-question chatbot for citizens.  
* Photograph handwritten meeting notes, then let the model answer action-item questions.  
* Upload a long group-chat export and generate a visual timeline of who promised what.  
* Take pictures of birds on your feeder; ask the model to log species + count per day.

**Submission Deadline:** 12/10/2025
## Submission Guidelines
1. GitHub repo (public or private link shared) containing:
   - README with problem statement, setup steps, and demo GIF/screenshots  
   - `requirements.txt` or `pyproject.toml`  
   - Core script/notebook that runs end-to-end  
2. 2-min Loom/video walkthrough (unlisted YouTube or direct MP4 link)  
3. Short reflection (≤ 200 words) on biggest challenge & next improvement  

## Optional Challenges
* Support **multiple images in one query** (e.g., before/after, front/back).  
* Add **caching** so repeated questions on the same long doc don’t re-cost tokens.  
* Build a **Slack/Discord bot** that answers questions about uploaded images or PDFs.  
* Compare **cost & latency** between Gemini Pro Vision and GPT-4o on identical inputs.  
* Fine-tune **chunking strategy** to beat the model’s “lost-in-the-middle” recall issue.
