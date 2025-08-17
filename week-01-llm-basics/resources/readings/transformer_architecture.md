# Understanding Transformer Architecture

## What is a Transformer?

The Transformer is a neural network architecture introduced in the paper "Attention is All You Need" (2017). It revolutionized natural language processing by using self-attention mechanisms instead of recurrent layers.

## Key Components

### 1. Self-Attention Mechanism
- **Purpose**: Allows the model to focus on different parts of the input sequence
- **How it works**: Each token can attend to all other tokens in the sequence
- **Formula**: `Attention(Q,K,V) = softmax(QK^T/√d_k)V`

### 2. Multi-Head Attention
- Uses multiple attention heads in parallel
- Each head learns different types of relationships
- Outputs are concatenated and projected

### 3. Feed-Forward Networks
- Simple neural networks applied to each position
- Two linear transformations with ReLU activation
- Same across all positions but different parameters

### 4. Positional Encoding
- Since Transformers don't have inherent sequence order
- Adds information about token positions
- Uses sine and cosine functions of different frequencies

## Architecture Flow

1. **Input Embedding**: Convert tokens to dense vectors
2. **Positional Encoding**: Add position information
3. **Encoder Layers**: Stack of attention + feed-forward
4. **Decoder Layers**: Similar to encoder but with masked attention
5. **Output Layer**: Linear projection + softmax

## Why Transformers Work

- **Parallelization**: Unlike RNNs, can process all positions simultaneously
- **Long-range Dependencies**: Self-attention connects distant tokens
- **Scalability**: Performance improves with more data and parameters

## Modern Variations

### GPT (Generative Pre-trained Transformer)
- Decoder-only architecture
- Autoregressive generation
- Pre-trained on next-token prediction

### BERT (Bidirectional Encoder Representations)
- Encoder-only architecture
- Bidirectional context
- Pre-trained on masked language modeling

### T5 (Text-to-Text Transfer Transformer)
- Encoder-decoder architecture
- All tasks as text-to-text
- Unified framework

## Key Insights for Fellows

1. **Attention is Key**: Understanding attention helps in prompt engineering
2. **Context Window**: Limited by computational constraints
3. **Training Objective**: Influences model capabilities
4. **Scale Matters**: Larger models often perform better

## Further Reading
- [Attention is All You Need](https://arxiv.org/abs/1706.03762)
- [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/)
- [GPT-1 Paper](https://s3-us-west-2.amazonaws.com/openai-assets/research-covers/language-unsupervised/language_understanding_paper.pdf)
