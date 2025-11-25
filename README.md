# 🤖 Multi-Agent Query System

<div align="center">
  <strong>An intelligent query system leveraging multiple specialized agents for comprehensive answers</strong>
</div>

<div align="center">
  
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.118.0-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![LangChain](https://img.shields.io/badge/LangChain-0.3.27-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)](https://www.langchain.com/)
[![Groq](https://img.shields.io/badge/Groq-LLM-orange?style=for-the-badge)](https://groq.com/)
[![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)

</div>

## 🌟 Project Vision

The **Multi-Agent Query System** is designed to overcome the limitations of single-source information retrieval. By orchestrating a team of specialized agents—including a Web Search Agent, an Arxiv Research Agent, and a PDF RAG Agent—this system provides accurate, context-aware, and synthesized answers to complex user queries. It intelligently routes questions to the most appropriate agent, ensuring efficiency and depth.

## ✨ Features

- **🧠 Intelligent Query Routing**: A Controller Agent analyzes the user's query and routes it to the best-suited specialist.
- **📄 PDF RAG (Retrieval-Augmented Generation)**: Upload and query your own PDF documents with context-aware retrieval.
- **🌐 Web Search Integration**: Real-time web search capabilities using DuckDuckGo for up-to-date information.
- **📚 Arxiv Research**: Dedicated agent for searching and summarizing academic papers from Arxiv.
- **💬 Answer Synthesis**: Combines retrieved context into a coherent, natural language response.
- **🖥️ Clean UI**: A simple and responsive web interface for interacting with the system.

## 🏗️ Architecture

The system is built on a modular architecture:

1.  **Frontend**: HTML/CSS/JS (Jinja2 Templates) for user interaction.
2.  **Backend**: FastAPI server handling API requests and agent orchestration.
3.  **Agents**:
    *   **Controller Agent**: The "brain" that decides which tool to use.
    *   **Web Agent**: Fetches data from the internet.
    *   **Arxiv Agent**: Fetches academic papers.
    *   **PDF RAG Agent**: Handles document embedding (ChromaDB) and retrieval.

## 🚀 Getting Started

### Prerequisites

-   **Python 3.10+**
-   **Groq API Key**: You need an API key from [Groq](https://console.groq.com/) to power the LLM.

### Installation

1.  **Clone the repository**

    ```bash
    git clone https://github.com/AnshWithTea/multi-agent-query-system.git
    cd multi-agent-query-system
    ```

2.  **Set up environment variables**

    Create a `.env` file in the root directory and add your Groq API key:

    ```bash
    GROQ_API_KEY=your_groq_api_key_here
    ```

3.  **Install dependencies**

    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

You can run the application using Python directly:

```bash
python main.py
```

Or using Uvicorn:

```bash
uvicorn main:app --reload
```

The application will be available at `http://localhost:8000`.

## 🤝 Contributing

We welcome contributions! If you have ideas for new agents or improvements, please feel free to open an issue or submit a pull request.

## 📝 License

This project is open-source and available under the MIT License.

---

<div align="center">
  <p>Built with ❤️ using FastAPI and LangChain</p>
</div>
