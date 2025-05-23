# RAG with Bedrock
RAG with Bedrock works like this: for any given prompt, Bedrock searches for relevant information in a "Knowledge Base". The Knowledge Base is backed by a Vector Database. To create the data in the vector database:
  - Bedrock takes care of eerything. Bedrock takes care of creating Vector Embeddings in the database of your choice based on your data
## Can you use a google cloud database for generating vector embeddings for amazon bedrock?
You can use a Google Cloud database (such as BigQuery, Firestore, or AlloyDB) to store and manage your data, but generating vector embeddings for Amazon Bedrock typically involves using Bedrock’s own models or other embedding models (like those from AWS SageMaker or open-source libraries).

How it could work:

Store Data in Google Cloud: Your raw data (text, images, etc.) is stored in a Google Cloud database.
Extract Data: You extract the data from Google Cloud to your application.
Generate Embeddings:
If you want to use Amazon Bedrock for embeddings, you send the extracted data to Bedrock’s embedding model via API.
Alternatively, you can use Google’s Vertex AI or open-source models to generate embeddings.
Store Embeddings: You can store the resulting embeddings back in Google Cloud, or in another vector database (like Pinecone, Weaviate, or Amazon OpenSearch).
Key Points:

Amazon Bedrock does not natively connect to Google Cloud databases; you need to handle data transfer in your application code.
Bedrock provides the embedding models, not the database.
You can use any database to store embeddings, as long as your application can read/write to it.
Summary:
Yes, you can use a Google Cloud database to store data and embeddings, but you must handle the integration between Google Cloud and Amazon Bedrock in your application logic. Bedrock itself does not directly connect to Google Cloud databases.

Vector embeddings tend to be smaller to store than the size of the original text
## AWS Services That Can Be Used as Your Vector Dabase to Store Vector Embedings
- OpenSearch service (default if you don't specify a database)
- Amazon Aurora
- Other options: MongoDB, Redis, Pinecone
## Embedding Models
Embedding models - determine how data is put into vector stores
Options: Amazon Titon OR Cohere (even though these are also names of foundation models, the embedding model and foundation model can be different)

RAG files are broken into document chunks by the embedding model then stored in a vector database 
## Where RAG files can be stored
RAG files can be stored in S3

### With amazon bedrock can i store my RAG files on-prem instead of in S3? Link to relevant docs
No, Amazon Bedrock currently requires your Retrieval-Augmented Generation (RAG) data to be stored in Amazon S3. Bedrock’s Knowledge Bases feature is designed to connect to data in S3 buckets, and there is no built-in support for directly accessing on-premises file storage.

Relevant documentation:
- [Amazon Bedrock Knowledge Bases – Supported Data Sources](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-data-source.html)
- [Create a knowledge base in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-create.html)

Amazon Bedrock Knowledge Bases – Supported Data Sources
Create a knowledge base in Amazon Bedrock
If you need to use on-premises data, you would have to sync or upload your files to S3 first.