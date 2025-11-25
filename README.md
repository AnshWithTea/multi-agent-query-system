# Multi-Query AI Agent 🤖

An intelligent orchestration engine built with **Python** and **FastAPI**. This system acts as a smart central brain that analyzes user queries and dynamically routes them to the most effective information retrieval tool—whether that's live web data, academic research, or internal documents.

## 🚀 Features

* **Intelligent Query Routing:** Uses an LLM to analyze intent and determine the best source of information.
* **Multi-Tool Integration:**
    * **🌐 Live Web Search:** Fetches real-time information for current events and general queries.
    * **📄 RAG Pipeline:** Custom Retrieval-Augmented Generation system for querying uploaded PDF documents.
    * **🎓 ArXiv API:** Direct access to scientific papers and academic research.
* **High Performance:** Built on **FastAPI** for asynchronous, high-speed request handling.
* **Scalable Architecture:** Designed to easily add more tools (e.g., Wikipedia, Database queries) in the future.

## 🛠️ Tech Stack

* **Backend:** Python 3.x
* **API Framework:** FastAPI
* **AI/LLM:** (Specify your model here, e.g., OpenAI GPT-4, Google Gemini, local Llama)
* **Vector Database:** (Specify if used, e.g., FAISS, ChromaDB, Pinecone)
* **Search Integration:** (Specify provider, e.g., Serper, Google Custom Search)

## 📂 Project Structure

```bash
multi-agent-query-system/
├── app/
│   ├── main.py            # Application entry point
│   ├── agents/            # Logic for the orchestrator agent
│   ├── tools/
│   │   ├── web_search.py  # Web search tool implementation
│   │   ├── arxiv_tool.py  # ArXiv API wrapper
│   │   └── rag_pipeline.py# PDF processing and retrieval logic
│   ├── models/            # Pydantic models for request/response
│   └── utils/             # Helper functions (text processing, etc.)
├── data/                  # Storage for uploaded PDFs (if local)
├── .env                   # Environment variables (API Keys)
├── requirements.txt       # Python dependencies
└── README.md
