"""Historical DNS Lookup: GET https://api.whoisfreaks.com/v2.0/dns/historical

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DnsHistorical.py
"""
import json
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DNSApi(client)

    # dns_historical parameters:
    #   domain_name (str, required)
    #   type (str, required): default "all"
    #   page (int, optional, keyword): default 1
    #   format (str, optional, keyword): one of json, xml; default "json"
    result = api.dns_historical("whoisfreaks.com", "A,MX,TXT", page=1)
    print(json.dumps(result.to_dict(), indent=2))
