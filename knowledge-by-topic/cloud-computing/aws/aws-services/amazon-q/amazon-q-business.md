# Amazon Q Business
- Fully managed Gen-AI assistant for your employees
- Based on your company's knowledge and data:
  - Answer questions, provide summaries, generate content, automate tasks

## Data Connectors (fully managed RAG) 
can connect to 40+ popular enterprise data sources. Including:
- S3
- RDS
- Aurora
- WorkDocs
- Microsoft 365
- Salesforce
- GDrive
- Gmail
- Slack
- Sharepoint

## Plugins
allows you to interact with third party services. Includes:
- Jira
- ServiceNow
- Zendesk
- Salesforce

## How to Access Amazon Q Business?
- users can be authenticated thru IAM Identity Center (users authenticate)
  - can be configured with external Identity Providers
- users receive responses generated only from the documents they have access to 

## Admin Controls
Pretty much the same as Guardrails in Bedrock. Lets you:
- block specific words or topics
- respond only with internal information (vs using external knowledge)
- create global controls and topic-level controls (more granular rules)

# Amazon Q Apps (part of Amazon Q Business)
Lets you create Gen-AI powered apps without coding by using natural language. Leverages your company's internal data