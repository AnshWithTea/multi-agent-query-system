Multi-Agent Query System
Live Demo: https://huggingface.co/spaces/AnshWithTech/multi-agent-query-system

Project Overview
This project is an intelligent Multi-Agent AI System designed to function as a dynamic and intelligent query router. The core purpose is to analyze a user's natural language query and determine the most effective information retrieval tool to answer it. Instead of relying on a single source, this system leverages a team of specialized agents to ensure the user receives the most relevant and accurate information, whether from a live web search, a scientific database, or a user-uploaded document.

Key Features
🧠 Dynamic Agent Routing: A central Controller Agent intelligently analyzes user queries and dispatches the task to the most appropriate agent.

📄 Retrieval-Augmented Generation (RAG): The system allows users to upload PDF documents and ask questions specifically about their content.

🌐 Multi-Tool Integration: Includes agents for real-time web searches, querying the ArXiv academic database, and performing RAG on local documents.

✨ LLM-Powered Answer Synthesis: After retrieving information, a fast LLM (via Groq API) generates a coherent, natural-language answer.

🔍 Transparent Reasoning: The system provides the final answer and shows which agent was used and why, ensuring transparency in its decision-making process.

Architecture & Approach
The system is built on a modern, modular architecture centered around a FastAPI backend. When a user submits a query, it follows a sophisticated workflow designed for both speed and accuracy.

Query Ingestion: The user interacts with a clean, modern UI to submit a query and optionally upload a PDF.

Controller Analysis: The request is sent to the FastAPI backend, where the Controller Agent takes over. It uses a hybrid routing strategy:

Rule-Based First: It quickly scans for keywords (e.g., "paper," "news," "document") to make an immediate, deterministic routing decision.

LLM-Based Fallback: If no keywords match, the query is sent to a fast Groq LLM, which is prompted to choose the most logical tool for the job.

Information Retrieval: The selected Worker Agent (Web Search, ArXiv, or PDF RAG) executes its task to gather the raw information.

Answer Synthesis & Response: The retrieved context is passed to the Groq LLM a second time. The LLM synthesizes this information into a concise, human-readable answer, which is sent back to the UI along with the controller's rationale.

Dataset and Expected Outputs
The project uses sample documents in the sample_pdfs/ directory to demonstrate the RAG agent's functionality. When you use the application, you can expect a clear, structured response for every query.

For example, after uploading a relevant PDF and asking a question about it, the output will look like this:

Answer
The primary export mentioned in the document is crystallized data fragments.

Agent Used: PDF_RAG

Rationale: A document has been uploaded and the query refers to it.
