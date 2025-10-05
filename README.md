Multi-Agent Query System
This project is an intelligent multi-agent AI system that dynamically routes user queries to the most appropriate information retrieval tool. It's designed to understand the user's intent and choose between a real-time web search, a scientific paper database, or a user-uploaded PDF to find the most relevant answer.

Core Features
🧠 Dynamic Agent Routing: A central Controller Agent analyzes user queries to select the best tool for the job: Web Search, ArXiv, or a PDF RAG agent.

⚙️ Hybrid Decision Logic: Utilizes a fast, rule-based approach for specific keywords (e.g., "paper," "news") and falls back to an LLM-based router for ambiguous queries.

📄 Retrieval-Augmented Generation (RAG): Allows users to upload a PDF and ask questions directly about its content. The system extracts text, creates embeddings, and retrieves the most relevant passages to answer the query.

🌐 Multi-Tool Integration:

Web Agent: Performs real-time web searches for current events and general knowledge.

ArXiv Agent: Queries the ArXiv database for scientific papers and research.

PDF RAG Agent: Analyzes the content of user-provided documents.

✨ LLM-Powered Answer Synthesis: After retrieving information, the system uses a fast LLM via the Groq API to generate a coherent, natural-language answer for the user.

Tech Stack
Backend: FastAPI

LLM & Embeddings: Groq API, Sentence-Transformers

Vector Store: ChromaDB

Core Libraries: LangChain, arxiv, duckduckgo-search

Deployment: Docker, Hugging Face Spaces


Multi-Agent Query System - https://huggingface.co/spaces/AnshWithTea/multi-query-ai-agent
