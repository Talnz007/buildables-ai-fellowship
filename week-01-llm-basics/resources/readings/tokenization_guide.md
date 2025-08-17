# Tokenization in Large Language Models

## What is Tokenization?

Tokenization is the process of breaking down text into smaller units called tokens, which are then converted to numerical representations that neural networks can process.

## Why Tokenization Matters

1. **Model Input**: LLMs work with numbers, not text
2. **Vocabulary Management**: Handles out-of-vocabulary words
3. **Efficiency**: Balances vocabulary size with representation quality
4. **Multilingual Support**: Enables processing of multiple languages

## Types of Tokenization

### 1. Word-Level Tokenization
```
"Hello world!" → ["Hello", "world", "!"]
```
- **Pros**: Intuitive, preserves word boundaries
- **Cons**: Large vocabulary, poor handling of rare words

### 2. Character-Level Tokenization
```
"Hello" → ["H", "e", "l", "l", "o"]
```
- **Pros**: Small vocabulary, handles any text
- **Cons**: Long sequences, loses semantic meaning

### 3. Subword Tokenization
```
"unhappiness" → ["un", "happiness"]
```
- **Pros**: Balances vocabulary size and meaning
- **Cons**: More complex implementation

## Popular Tokenization Algorithms

### Byte Pair Encoding (BPE)
1. Start with character vocabulary
2. Iteratively merge most frequent pairs
3. Build vocabulary of subwords

### WordPiece
- Similar to BPE but uses likelihood-based merging
- Used by BERT and similar models

### SentencePiece
- Language-agnostic tokenization
- Treats input as raw byte stream
- Used by T5, GPT models

## Tokenization in Practice

### OpenAI Models
```python
import tiktoken

# GPT-4 tokenizer
enc = tiktoken.get_encoding("cl100k_base")
tokens = enc.encode("Hello, world!")
print(tokens)  # [9906, 11, 1917, 0]
print(enc.decode(tokens))  # "Hello, world!"
```

### Hugging Face Models
```python
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("gpt2")
tokens = tokenizer.encode("Hello, world!")
print(tokens)  # [15496, 11, 995, 0]
```

## Key Concepts

### Token Limits
- GPT-3.5-turbo: 4,096 tokens
- GPT-4: 8,192 or 32,768 tokens
- Claude: 100,000+ tokens

### Token Counting
```python
def count_tokens(text, model="gpt-3.5-turbo"):
    encoding = tiktoken.encoding_for_model(model)
    return len(encoding.encode(text))

text = "The quick brown fox jumps over the lazy dog."
print(f"Token count: {count_tokens(text)}")
```

### Special Tokens
- `<|endoftext|>`: End of document
- `<|im_start|>`: Start of message
- `<|im_end|>`: End of message

## Best Practices

### 1. Token Efficiency
- Shorter prompts = lower costs
- Monitor token usage in applications
- Use appropriate models for task complexity

### 2. Multilingual Considerations
- Different languages have different token densities
- English: ~4 characters per token
- Other languages: May vary significantly

### 3. Code Tokenization
- Code tokens differently than natural language
- Consider specialized models for code tasks

## Common Issues and Solutions

### Issue: Unexpected Token Splits
```python
# Problem: "GPT-4" might tokenize as ["G", "PT", "-", "4"]
# Solution: Use consistent formatting
text = "The model GPT-4 is powerful"
tokens = tokenizer.encode(text)
```

### Issue: Token Limit Exceeded
```python
# Solution: Implement chunking
def chunk_text(text, max_tokens=1000):
    tokens = tokenizer.encode(text)
    chunks = []
    for i in range(0, len(tokens), max_tokens):
        chunk_tokens = tokens[i:i+max_tokens]
        chunks.append(tokenizer.decode(chunk_tokens))
    return chunks
```

## Hands-On Exercise

Try tokenizing these examples and observe the differences:

1. `"Hello world"`
2. `"hello world"`
3. `"HelloWorld"`
4. `"Hello  world"` (two spaces)
5. `"🌟 Hello world 🌟"`
6. `"print('Hello world!')"`

## Tools for Exploration

1. [OpenAI Tokenizer](https://platform.openai.com/tokenizer)
2. [Hugging Face Tokenizers](https://huggingface.co/docs/tokenizers/)
3. [tiktoken Library](https://github.com/openai/tiktoken)

Understanding tokenization is crucial for effective prompt engineering and cost optimization in LLM applications!
