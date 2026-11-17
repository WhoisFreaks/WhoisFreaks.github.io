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
    #   domain_name (str, required): Domain to look up
    #   type (str, required): Comma separated DNS record types to return, for example A,MX,TXT. Defaults to...; default "all"
    #   page (int, optional, keyword): Page of results to return. Defaults to 1; default 1
    #   format (str, optional, keyword): Response format. JSON when the parameter is left out; one of json, xml; default "json"
    result = api.dns_historical("whoisfreaks.com", "A,MX,TXT", page=1)
    print(json.dumps(result.to_dict(), indent=2))
