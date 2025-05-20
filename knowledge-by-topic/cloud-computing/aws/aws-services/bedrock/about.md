# Amazon Bedrock

## Foundation Models
- You have to set IAM permissions to get access to a foundation model
- "Amazon Nova" is the cheapest foundation model 
- Some models accept attachments, others do not 
### Choosing a Foundation Model
- Diff FMs have different context windows, latencies, etc
- Some models are "multimodal models" meaning types of input and output can vary. Eg a model that can accept both text and image as input 
- Smaller models tend to be more cost-effective, yet know less
### Specific Foundation Models
- Amazon Titan - most high-performing FM from AWS
  - Image, text, multimodal choices via fully-managed APIs (same API as used with Bedrock)
  - Can be customized with your own data 
  - "Titan Text Express" is part of the "Titan Text" family of models, is text-only (not multimodal) and tends to be cheap 
## Custom models - Customization Methods for FMs
### Fine-tuning (Fine-tuning will be a big part of the AIF-C01 exam)
- "Fine-tuning" - provide labeled data in order to train a model to improve performance on specific tasks
- Data can be placed in S3
### Distillation
- "Distillation" - Generate synthetic data from a large foundation model (teacher) and use the synthetic data to fine-tune a smaller model (student) for your specific use case
### Continued pre-training
- "Continued pre-training" - Provide unlabeled data to pre-train a foundation model by familiarizing it with certain types of inputs 
#### Hyperparameters (knowing these in detail is beyond the scope of the AIF-C01 cert)
- Hyperparameters allow you to customize training
- "Epochs" - total numver of iterations of all the training data in one cycle for the training model 
- "Learning rate" - the rate at which model parameters are updated after each batch of training data
- "Learning rate warmup steps" - number of iterations over which learning rate is gradually increased to the initial rate specified
## Modes
- "Single prompt" mode - tells you input and output tokens, does NOT keep track of chat history
- "Chat" mode - keeps track of chat history. Tells you input and output tokens

## Pricing
- "Input tokens" & "output tokens" generated affect pricing

## RAG
- [Knowledge Bases](https://aws.amazon.com/bedrock/knowledge-bases/ ) allow RAG with Amazon Bedrock

## Prompt Management
- Bedrock offers [prompt management](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html) and [prompt templates](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-create.html)
- Bedrock allows you to version prompts
- Bedrock has a [prompt optimization tool](https://www.youtube.com/watch?v=WlD2i6gT9Js)
- Bedrock allows you to create a [prompt flow](https://aws.amazon.com/awstv/watch/f555df58129/ ), sort of like a langchain chain