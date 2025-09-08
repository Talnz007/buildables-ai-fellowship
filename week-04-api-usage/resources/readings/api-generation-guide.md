# A Guide to Using Text Generation APIs

LLM APIs provide a simple yet powerful way to integrate AI into your applications. [cite_start]The core workflow involves sending a text prompt to an API endpoint and receiving a text completion in return[cite: 3].

## The Core Components of an API Call

1.  **API Key**: This is a secret token that authenticates you with the service provider (e.g., OpenAI, Google). **Never share your API key or commit it to public code repositories.** It's best practice to store it as an environment variable.

2.  **API Endpoint**: This is the URL you send your request to. [cite_start]Each provider has specific URLs for different models and tasks (e.g., OpenAI Completions API, Gemini Text Generation API)[cite: 3].

3.  **Model Identifier**: You must specify which model you want to use (e.g., `gpt-3.5-turbo`, `gemini-1.5-pro-latest`). Newer, more powerful models generally cost more per request.

4.  **The Payload (Request Body)**: This is a JSON object containing the data you send. The most important parts are:
    * **Prompt/Messages**: The text input for the model. For chat-based models, this is usually a list of messages with roles (`system`, `user`, `assistant`).
    * **Parameters**: Key-value pairs that control the generation process (e.g., `temperature`, `max_tokens`).

## Basic Workflow (Conceptual)

   Your Application                                  LLM Provider's Server
+-----------------+                                 +------------------------+
|                 | ------ 1. HTTP POST Request ---> |      API Endpoint      |
|  Python Script  |    (prompt, API key, etc.)       |    (e.g., OpenAI)      |
|                 |                                  +------------------------+
+-----------------+                                             |
      ^                                                         | 2. Process Request &
      |                                                         |    Generate Response
      |                                                         v
      |                                  +------------------------+
      |                                  |          LLM           |
      +----- 3. HTTP Response ----------- |     (e.g., GPT-4)      |
           (generated text)                +------------------------+

## Example: OpenAI `ChatCompletion`

OpenAI's newer models use a `ChatCompletion` endpoint, which expects a list of messages.

```json
{
  "model": "gpt-3.5-turbo",
  "messages": [
    {
      "role": "system",
      "content": "You are a helpful assistant."
    },
    {
      "role": "user",
      "content": "Who won the first Nobel Prize in Physics?"
    }
  ],
  "temperature": 0.7
}

The response you get back will also be a JSON object containing the model's reply. You will need to parse this JSON to extract the text content.
