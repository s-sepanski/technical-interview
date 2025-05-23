# Model Context Protocol (MCP)
A protocol to connect LLMs to external data sources and tools 

The MCP client connects to MCP servers. MCP typically works over HTTPS

MCP supports TWO-WAY connection between the server and the client. So the server can request the client (eg Claude) to generate completions (the "sampling" primitive). Similarly, the client can request tool execution on the server, then request a result.

## Clarification: Is MCP an Abstraction on Top of HTTP?
Yes, MCP (Model Context Protocol) is effectively an abstraction layer on top of HTTP—but it’s more accurate to say that it’s a data protocol or interface specification that is typically transmitted over HTTP(S).


Here’s how it breaks down:

✅ What MCP is:
A structured format (usually JSON) for how to represent model inputs, outputs, metadata, and capabilities.

A standard schema that allows clients to interact with different models in a uniform way, regardless of provider.

An application-layer protocol, similar in spirit to REST or GraphQL—but focused on model invocation and metadata.

📡 How it’s used:
Typically sent over HTTP(S) via standard POST requests (e.g., to /v1/chat/completions).

MCP defines the payload structure, not the transport mechanism.

That means you could theoretically send MCP-structured requests over other transport mechanisms (e.g., WebSocket or gRPC), but HTTP is the most common.

🧠 Analogy:
If HTTP is the mail truck, MCP is the form inside the envelope that tells the recipient what the request is about, how to process it, and how to respond.

Summary:
MCP is an abstraction over how model interactions are structured.

It is usually used over HTTP(S), but not inherently tied to it.

## MCP Clients
LLM-powered apps eg Claude, IDEs

MCP clients provide 2 primitives:
1. Routes: Interfaces or entrypoints through which the client connects to the MCP servers 
2. Sampling: Strangely, the SERVER can request the CLIENT to generate text based on specific inputs or context

## MCP Servers
Can optionally connect to some data store or API

MCP servers provide 3 primitives: 
1. Resources: File-like data that can be read by clients (like API responses or file contents)
2. Tools: Functions that can be called by the LLM (with user approval)
3. Prompts: Pre-written templates that help users accomplish specific tasks