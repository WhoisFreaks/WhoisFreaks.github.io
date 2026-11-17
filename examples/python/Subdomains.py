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
    #   domain (str, required): Domain whose subdomains you want
    #   after (datetime.date, optional, keyword): Only return records created after this date, in YYYY-MM-DD format. Defaults t...
    #   before (datetime.date, optional, keyword): Only return records created before this date, in YYYY-MM-DD format. Defaults ...
    #   status (str, optional, keyword): Limit results to active or inactive subdomains. Both are returned when the pa...; one of active, inactive
    #   page (int, optional, keyword): Page of results to return. Defaults to 1; default 1
    #   format (str, optional, keyword): Response format. JSON when the parameter is left out; one of json, xml; default "json"
    result = api.subdomains("whoisfreaks.com", page=1)
    print(json.dumps(result.to_dict(), indent=2))
