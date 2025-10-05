# agents/arxiv_agent.py

import arxiv
from itertools import islice

def search_arxiv(query: str, max_results: int = 3) -> str:
    """
    Searches ArXiv for papers and returns a formatted string of results.

    Args:
        query: The search query.
        max_results: The maximum number of results to return.

    Returns:
        A formatted string of the top search results, or an error message.
    """
    print(f"-> ArXiv Agent: Searching for '{query}'...")
    try:
        # Construct the search query
        search = arxiv.Search(
            query=query,
            max_results=max_results,
            sort_by=arxiv.SortCriterion.Relevance
        )

        # Get the results
        client = arxiv.Client()
        results = list(islice(client.results(search), max_results))

        if not results:
            return "ArXiv Agent: No papers found."

        # Format the results
        formatted_results = []
        for i, result in enumerate(results):
            # Format authors to be a readable string
            author_names = ", ".join([author.name for author in result.authors])
            formatted_results.append(
                f"Paper {i+1}: {result.title}\n"
                f"Authors: {author_names}\n"
                f"Published: {result.published.strftime('%Y-%m-%d')}\n"
                f"URL: {result.pdf_url}"
            )

        print("-> ArXiv Agent: Found results.")
        return "\n\n".join(formatted_results)

    except Exception as e:
        print(f"-> ArXiv Agent: Error during search - {e}")
        return f"ArXiv Agent: An error occurred: {e}"

# Standalone test block
if __name__ == '__main__':
    test_query = "Transformer models in computer vision"
    print(f"--- Testing ArXiv Agent with query: '{test_query}' ---")
    search_results = search_arxiv(test_query)
    print("\n--- Results ---")
    print(search_results)
    print("\n--- Test Complete ---")