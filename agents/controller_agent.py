# agents/controller_agent.py

import os
from groq import Groq
from dotenv import load_dotenv
from typing import Tuple

# Load environment variables
load_dotenv()

# Initialize the Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def route_query(query: str, collection_exists: bool) -> Tuple[str, str]:
    """
    Routes the user's query to the appropriate agent using a hybrid approach.
    Returns the chosen agent and the rationale for the choice.
    """
    # --- 1. Rule-Based Routing (Fast Path) ---
    query_lower = query.lower()

    if "arxiv" in query_lower or "paper" in query_lower or "research" in query_lower:
        rationale = "Query contains keywords like 'arxiv', 'paper', or 'research'."
        print(f"-> Controller: Routing to ArXiv Agent. Rationale: {rationale}")
        return "ARXIV", rationale

    if "news" in query_lower or "latest" in query_lower or "current events" in query_lower:
        rationale = "Query contains keywords like 'news', 'latest', or 'current events'."
        print(f"-> Controller: Routing to Web Search Agent. Rationale: {rationale}")
        return "WEB_SEARCH", rationale

    # If a PDF has been uploaded and the query refers to it
    if collection_exists and ("document" in query_lower or "pdf" in query_lower or "summarize" in query_lower):
        rationale = "A document has been uploaded and the query refers to it."
        print(f"-> Controller: Routing to PDF RAG Agent. Rationale: {rationale}")
        return "PDF_RAG", rationale

    # --- 2. LLM-Based Routing (Smart Path) ---
    print("-> Controller: No specific keywords found, using LLM to route.")
    try:
        system_prompt = """
        You are an intelligent routing agent. Your job is to analyze the user's query and decide which tool is best to use.
        The available tools are:
        - 'WEB_SEARCH': For general questions, current events, or real-time information.
        - 'ARXIV': For questions about scientific papers, research, or technical topics.
        - 'PDF_RAG': For questions specifically about the content of a document that the user has uploaded.

        Based on the user's query and whether a document has been provided, you must respond with ONLY the name of the tool to use (e.g., 'WEB_SEARCH'). Do not add any other text or explanation.
        """
        user_prompt = f"User query: '{query}'. Has a document been uploaded? {'Yes' if collection_exists else 'No'}."

        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            model="llama-3.1-8b-instant",
        )
        choice = chat_completion.choices[0].message.content.strip().upper()
        
        # Validate the choice
        valid_choices = ["WEB_SEARCH", "ARXIV", "PDF_RAG"]
        if choice in valid_choices:
            rationale = f"LLM decided the best tool for the query is {choice}."
            print(f"-> Controller: LLM routing to {choice}. Rationale: {rationale}")
            return choice, rationale
        else:
            # Fallback if the LLM gives an invalid response
            rationale = "LLM response was invalid, falling back to Web Search."
            print(f"-> Controller: LLM response invalid. {rationale}")
            return "WEB_SEARCH", rationale

    except Exception as e:
        rationale = f"An error occurred with the LLM router: {e}. Falling back to Web Search."
        print(f"-> Controller: {rationale}")
        return "WEB_SEARCH", rationale


def synthesize_answer(query: str, context: str) -> str:
    """

    Uses an LLM to generate a final, human-readable answer based on the retrieved context.
    """
    print("-> Controller: Synthesizing final answer...")
    system_prompt = "You are a helpful AI assistant. Based on the provided context, answer the user's query in a clear and concise way. If the context does not contain the answer, say that you couldn't find the information."
    user_prompt = f"Context:\n---\n{context}\n---\nUser Query: {query}"

    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            model="llama-3.1-8b-instant", # Using a smaller model for speed
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        print(f"-> Controller: Error during answer synthesis - {e}")
        return "An error occurred while generating the final answer."