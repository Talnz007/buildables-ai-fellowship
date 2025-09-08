# Understanding Key API Parameters

When you make an API call to an LLM, you can include several parameters to influence how the model generates a response. <!--cite: 3--> Mastering these parameters is key to getting the high-quality, consistent output you need.

Here are the most common ones:

### `temperature`

This parameter controls the randomness of the model's output. <!--cite: 3--> It is usually a float value between 0.0 and 2.0.

* **Low Temperature (e.g., `0.0` - `0.3`)**: The model becomes more deterministic and focused. It will almost always pick the most likely next word.
    * **Use Case**: Best for tasks that require factual, concise, and predictable answers, like summarization, classification, or fact-based Q&A.

* **High Temperature (e.g., `0.8` - `1.2`)**: The model becomes more creative and random. It's more likely to pick less common words, leading to more diverse, interesting, and sometimes unexpected outputs.
    * **Use Case**: Ideal for creative tasks like writing stories, brainstorming ideas, or creating varied marketing copy. A high temperature increases the risk of "hallucinations" (making up facts).

### `max_tokens` or `max_output_tokens`

This sets a hard limit on the length of the generated text, measured in tokens. A token is roughly equivalent to 4 characters of common English text.

* **Why it's important**: This is a primary tool for controlling costs and preventing runaway, overly long responses. If the model's output is cut off, it's often because it hit the `max_tokens` limit.
* **Example**: If you set `max_tokens: 150`, the model will stop generating text once it reaches 150 tokens, even if it's in the middle of a sentence.

### `top_p` (Top-P Sampling)

This is an alternative to `temperature` for controlling randomness. It tells the model to consider only the most probable words that make up a certain cumulative probability mass.

* **How it works**: A `top_p` of `0.9` means the model considers the smallest set of most likely words whose combined probability is at least 90%.
* **General Advice**: It is recommended to alter either `temperature` or `top_p`, but not both at the same time.

### `stop` (Stop Sequences)

You can provide a list of character sequences that, if generated, will cause the model to immediately stop.

* **Use Case**: This is useful for preventing the model from generating irrelevant text or for forcing it to stop at a natural endpoint, like a newline character or a specific phrase.

