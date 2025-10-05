# agents/web_agent.py

from duckduckgo_search import DDGS

def search_web(query: str, max_results: int = 3) -> str:
    """
    Performs a web search using DuckDuckGo and returns formatted results.

    Args:
        query: The search query.
        max_results: The maximum number of search results to return.

    Returns:
        A formatted string containing the search results, or an error message.
    """
    print(f"-> Web Agent: Searching for '{query}'...")
    try:
        with DDGS() as ddgs:
            # Perform the search
            results = list(ddgs.text(query, max_results=max_results))

            if not results:
                return "Web Agent: No results found."

            # Format the results into a single string
            formatted_results = []
            for i, result in enumerate(results):
                formatted_results.append(f"Source {i+1}: {result['title']}\nURL: {result['href']}\nSnippet: {result['body']}")

            print("-> Web Agent: Found results.")
            return "\n\n".join(formatted_results)

    except Exception as e:
        print(f"-> Web Agent: Error during search - {e}")
        return f"Web Agent: An error occurred during the search: {e}"

# This allows you to test the agent directly
if __name__ == '__main__':
    test_query = "latest news on generative AI"
    print(f"--- Testing Web Agent with query: '{test_query}' ---")
    search_results = search_web(test_query)
    print("\n--- Results ---")
    print(search_results)
    print("\n--- Test Complete ---")