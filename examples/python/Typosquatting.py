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
    #   keyword (str, optional, keyword)
    #   pattern (str, optional, keyword)
    #   page_token (str, optional, keyword)
    result = api.typosquatting(keyword="whoisfreaks")
    print(json.dumps(result.to_dict(), indent=2))
