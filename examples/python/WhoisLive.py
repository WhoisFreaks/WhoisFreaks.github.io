"""Live WHOIS Lookup: GET https://api.whoisfreaks.com/v2.0/whois/live

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python WhoisLive.py
"""
import json
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.WHOISApi(client)

    # whois_live parameters:
    #   domain_name (str, required)
    #   format (str, optional, keyword): one of json, xml; default "json"
    result = api.whois_live("whoisfreaks.com")
    print(json.dumps(result.to_dict(), indent=2))
