# Bedrock with CloudWatch
Model invocation logging: 
- you can send all invocation logs to CloudWatch and S3
- can include text, images, and embeddings 
- can analyze and build alerting with CloudWatch Logs Insights

## CloudWatch Metrics for Bedrock
`ContentFilteredCount` can help you see how your Guardrails are functioning 

So you could set up a CloudWatch Alarm to alert you if too much content is getting filtered