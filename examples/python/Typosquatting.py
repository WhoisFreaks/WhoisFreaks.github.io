"""Typosquatting Lookup: GET https://api.whoisfreaks.com/v3.0/domain/typos

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python Typosquatting.py
"""
import json
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.TyposquattingApi(client)

    # typosquatting parameters:
    #   keyword (str, optional, keyword): Brand or label to find typo variants for. Pass either keyword or pattern, not...
    #   pattern (str, optional, keyword): Wildcard search string, where '*' matches any characters. Pass either keyword...
    #   page_token (str, optional, keyword): Token from nextPageToken in the previous response, needed from page 2 onward....
    result = api.typosquatting(keyword="whoisfreaks")
    print(json.dumps(result.to_dict(), indent=2))
