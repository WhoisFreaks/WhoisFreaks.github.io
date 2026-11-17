"""Subdomain Typosquatting Lookup: GET https://api.whoisfreaks.com/v3.0/subdomains/typos

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python SubdomainTyposquatting.py
"""
import json
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.TyposquattingApi(client)

    # subdomain_typosquatting parameters:
    #   keyword (str, optional, keyword): Brand or label to find typo variants for. 3 to 63 characters, letters, digits...
    #   pattern (str, optional, keyword): Wildcard search string, where '*' matches any characters and '?' matches one....
    #   page_token (str, optional, keyword): Token from nextPageToken in the previous response, needed from page 2 onward....
    #   fetch_size (int, optional, keyword): Subdomains per page. 100 when the parameter is left out, and values above 100...; default 100
    result = api.subdomain_typosquatting()
    print(json.dumps(result.to_dict(), indent=2))
