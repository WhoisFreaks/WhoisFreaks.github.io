"""Bulk WHOIS Lookup: POST https://api.whoisfreaks.com/v2.0/bulkwhois/live

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python BulkWhois.py
"""
import json
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.WHOISApi(client)

    # bulk_whois parameters:
    #   bulk_whois_request (BulkWhoisRequest, required): request body
    #   format (str, optional, keyword): one of json, xml; default "json"
    body = whoisfreaks.BulkWhoisRequest(domain_names=["whoisfreaks.com", "jfreaks.com"])
    result = api.bulk_whois(body)
    print(json.dumps(result.to_dict(), indent=2))
