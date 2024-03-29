import json
import os
import requests
from langchain.tools import tool

class SearchTools():

    @tool("Search the internet")
    def search_internet(query):
        """
        Searches the internet using a specified query and returns the top results.
        """
        top_result_to_return = 4
        url = "https://google.serper.dev/search"
        payload = json.dumps({"q": query})
        headers = {
            'X-API-KEY': os.environ['SERPER_API_KEY'],  # Fixed: Use square brackets for accessing environment variables
            'content-type': 'application/json'  # Fixed typo: 'conetent-type' to 'content-type'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        if 'organic' not in response.json():
            return "Sorry, I couldn't find anything about that, there could be an error with your SERPER API key."
        else:
            results = response.json()['organic']
            string = []
            for result in results[:top_result_to_return]:
                try:
                    string.append('\n'.join([
                        f"Title: {result['title']}", f"Link: {result['link']}",
                        f"Snippet: {result['snippet']}", "\n-----------------"
                    ]))
                except KeyError:
                    continue  # Use 'continue' instead of 'next'

            return '\n'.join(string)
