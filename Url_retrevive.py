import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")
SEARCH_ENGINE_ID = os.getenv("GOOGLE_CSE_ID")

def search_google(query):
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "key": API_KEY,
        "cx": SEARCH_ENGINE_ID,
        "q": query
    }

    response = requests.get(url, params=params)
    results = response.json()


    if "items" not in results:
        print("No results found.")
        return

    for item in results["items"]:
        title = item.get("title", "").lower()
        link = item.get("link", "")
        snippet = item.get("snippet", "").lower()

        if "ad" in title or "sponsored" in title or "sponsored" in snippet:
            continue

        return link



 # Replace with your search query
# issues
    # certain providers lack domain name rights
    # security services may block the request
