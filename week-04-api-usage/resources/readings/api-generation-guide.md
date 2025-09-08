
---

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
```

The response you get back will also be a JSON object containing the model's reply.
You will need to parse this JSON to extract the text content.
