"""Reverse WHOIS lookup by keyword: GET https://api.whoisfreaks.com/v2.0/whois/reverse

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python WhoisReverse.py
"""
import json
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.WHOISApi(client)

    # whois_reverse parameters:
    #   keyword (str, required): Keyword to search across WHOIS records
    #   page (int, optional, keyword): Page number
    #   format (str, optional, keyword): one of json, xml
    result = api.whois_reverse("whoisfreaks", page=1)
    print(json.dumps(result.to_dict(), indent=2))
