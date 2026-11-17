"""Reverse DNS Lookup: GET https://api.whoisfreaks.com/v2.1/dns/reverse

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DnsReverse.py
"""
import json
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DNSApi(client)

    # dns_reverse parameters:
    #   value (str, required): IP, CIDR, or record value
    #   type (str, required): DNS record type to search by; one of a, mx, cname, ns, aaaa, txt, soa
    #   exact (bool, optional, keyword): Set true to match value exactly. Defaults to false, where value is treated as...; default False
    #   page (int, optional, keyword): Page of results to return. Defaults to 1; default 1
    #   format (str, optional, keyword): Response format. JSON when the parameter is left out; one of json, xml; default "json"
    result = api.dns_reverse("8.8.8.8", "a", page=1)
    print(json.dumps(result.to_dict(), indent=2))
