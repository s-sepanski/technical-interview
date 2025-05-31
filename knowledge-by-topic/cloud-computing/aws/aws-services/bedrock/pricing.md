# Pricing
Pricing modes:
- on-demand - pay as you go, no committment. works on "Base Models" only. charged based on:
  - for text models: every input/output token processed 
  - for embedding models: charged for every input token processed 
  - for image models: charged for every image generated 
- batch:
  - multiple predictions at a time (output is a single file in Amazon S3)
  - responses can be a little slower
  - can provide discounts of up to 50%
- provisioned throughput:
  - purchase model units for a certain time (e.g. 1 month, 6 months)
  - guaranteed throughput with maximum number of input/output tokens processed per minute
  - works with base AND fine-tuned AND custom models

## Model Improvement Techniques from Cheapest to Most Expensive
1. prompt engineering
2. RAG 
3. Instruction-based fine-tuning (FM is fine-tuned with specific instructions, requiring additional computation)
4. domain adaptation fine-tuning (model is trained on a domain-specific dataset, requiring intensive computation

## Other
Modifying temperature, top K, or top P has no impact on pricing

Number of input and output tokens tends to be main driver of cost