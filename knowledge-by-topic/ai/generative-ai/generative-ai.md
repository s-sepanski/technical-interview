# Generative AI

# Tokenization
Tokenization - converting raw text into a sequence of tokens

Types of tokenization:
- word-based tokenization: text is split into individual words
- subword tokenization: some words can be split, too (helpful for long words)

Can visually tokenize a string at: https://platform.openai.com/tokenizer

Tokens are embedded using embedding models

# Context Window
Context window - the number of tokens an LLM can consider when generating text

The larger the context window, the more information and coherence 

Large context windows require more memory and processing 

# Vectors vs Embeddings
In generative AI and machine learning:

Embedding: An embedding is a learned representation of data (like words, images, or items) in a continuous vector space. Embeddings are created by neural networks to capture semantic or structural relationships in the data.

Vector: A vector is simply an array of numbers. In this context, it is the numerical output (the coordinates) of the embedding.

Summary:
An embedding is the concept or meaningful representation; a vector is the actual array of numbers that represents that embedding. All embeddings are vectors, but not all vectors are embeddings.

Example: Embedding vs. Vector
Suppose you have the word "cat".
A neural network learns to represent "cat" as an embedding—a point in a high-dimensional space.

The embedding vector for "cat" might look like this (with just 5 dimensions for simplicity):
```
# Example embedding vector for the word "cat"
embedding_cat = [0.12, -0.34, 0.56, 0.78, -0.91]
```

The embedding is the concept: "cat" represented in a way that captures its meaning and relationships.
The vector is the actual list of numbers: `[0.12, -0.34, 0.56, 0.78, -0.91]`.
In practice, embeddings often have hundreds of dimensions.

# Embeddings
Words that have a semantic relationship have similar embeddings 

## Visualizing Embeddings
To visualize embeddings, we can do something called "dimensionality reduction" to reduce, for example, word embeddings to 2D

Another way to visualize high-dimensionality embeddings is to use colors (so for each dimension, represent it with a color instead of with a number)