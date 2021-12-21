import os
from serpapi import GoogleSearch
from google_scholar_organic_results import organic_results


def cite_results():

    print("extracting cite results..")

    citation_results = []

    for citation in organic_results():
        params = {
            "api_key": os.getenv("API_KEY"),
            "engine": "google_scholar_cite",
            "q": citation["result_id"]
        }

        search = GoogleSearch(params)
        results = search.get_dict()

        print(f"Currently extracting {citation['result_id']} citation ID.")

        for result in results["citations"]:
            cite_title = result["title"]
            cite_snippet = result["snippet"]

            citation_results.append({
                "organic_result_title": citation["title"],
                "organic_result_link": citation["link"],
                "citation_title": cite_title,
                "citation_snippet": cite_snippet
            })

    return citation_results
