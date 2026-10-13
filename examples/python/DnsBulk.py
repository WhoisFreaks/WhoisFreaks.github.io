"""Bulk DNS Lookup: POST https://api.whoisfreaks.com/v2.0/dns/bulk/live

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DnsBulk.py
"""
import json
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DNSApi(client)

    # dns_bulk parameters:
    #   type (str, required): default "all"
    #   dns_bulk_request (DnsBulkRequest, required): request body
    #   format (str, optional, keyword): one of json, xml; default "json"
    body = whoisfreaks.DnsBulkRequest(domain_names=["whoisfreaks.com", "example.com"])
    result = api.dns_bulk("A,MX,TXT", body)
    print(json.dumps(result.to_dict(), indent=2))
