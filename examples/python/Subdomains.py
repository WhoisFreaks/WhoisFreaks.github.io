"""Subdomains Lookup: GET https://api.whoisfreaks.com/v1.0/subdomains

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python Subdomains.py
"""
import json
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.SubdomainsApi(client)

    # subdomains parameters:
    #   domain (str, required)
    #   after (datetime.date, optional, keyword)
    #   before (datetime.date, optional, keyword)
    #   status (str, optional, keyword): one of active, inactive
    #   page (int, optional, keyword): default 1
    #   format (str, optional, keyword): one of json, xml; default "json"
    result = api.subdomains("whoisfreaks.com", page=1)
    print(json.dumps(result.to_dict(), indent=2))
