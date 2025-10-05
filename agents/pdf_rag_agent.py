# --- CORRECTED VERSION FOR DEPLOYMENT ---
# agents/pdf_rag_agent.py

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFLoader
from langchain.embeddings import HuggingFaceEmbeddings
import chromadb
import os

# --- Constants ---
EMBEDDING_MODEL = "all-MiniLM-L6-v2"

# --- ChromaDB Client (In-Memory) ---
# For deployment stability on read-only filesystems, we use an in-memory client.
client = chromadb.Client()
embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
# This collection will be created in memory when the first PDF is processed.
collection = None

def process_pdf_and_store(file_path: str, collection_name: str):
    """
    Loads a PDF, splits it into chunks, embeds them, and stores them in an in-memory ChromaDB collection.
    """
    global collection
    print(f"-> PDF RAG Agent: Processing {file_path} for collection '{collection_name}'...")
    if not os.path.exists(file_path):
        print(f"-> PDF RAG Agent: Error - File not found at {file_path}")
        return

    loader = PyPDFLoader(file_path)
    documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = text_splitter.split_documents(documents)
    print(f"-> PDF RAG Agent: Created {len(chunks)} chunks.")

    # Get or create the in-memory collection
    collection = client.get_or_create_collection(
        name=collection_name,
        embedding_function=chromadb.utils.embedding_functions.SentenceTransformerEmbeddingFunction(model_name=EMBEDDING_MODEL)
    )

    collection.add(
        ids=[f"chunk_{i}" for i in range(len(chunks))],
        documents=[chunk.page_content for chunk in chunks]
    )
    print(f"-> PDF RAG Agent: Successfully stored embeddings in in-memory collection '{collection_name}'.")


def query_rag_store(query: str, collection_name: str, n_results: int = 3) -> str:
    """
    Queries the in-memory ChromaDB store for relevant document chunks.
    """
    global collection
    print(f"-> PDF RAG Agent: Querying '{query}' in collection '{collection_name}'...")
    
    if collection is None or collection.name != collection_name:
         return f"PDF RAG Agent: Could not find the document '{collection_name}'. Please upload it first."

    try:
        results = collection.query(
            query_texts=[query],
            n_results=n_results
        )

        retrieved_docs = results['documents'][0]
        if not retrieved_docs:
            return "PDF RAG Agent: No relevant information found in the document."

        formatted_results = "\n\n".join(retrieved_docs)
        print("-> PDF RAG Agent: Found relevant context.")
        return formatted_results

    except Exception as e:
        print(f"-> PDF RAG Agent: Error querying collection - {e}")
        return f"PDF RAG Agent: An error occurred while querying the document."