"""Reverse DNS Lookup (v2.2): GET https://api.whoisfreaks.com/v2.2/dns/reverse

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DnsReverseV22.py
"""
import json
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DNSApi(client)

    # dns_reverse_v22 parameters:
    #   value (str, required): IP, CIDR, or record value
    #   type (str, required): DNS record type to search by; one of a, mx, cname, ns, aaaa, txt, soa
    #   exact (bool, optional, keyword): When false the value is matched as a substring, which is far slower than an e...; default True
    #   page (int, optional, keyword): Page of results to return. Defaults to 1; default 1
    #   sort (str, optional, keyword): Sort direction. Omit to leave the results unsorted; one of asc, desc
    #   sort_by (str, optional, keyword): Field to sort on. Only applies when sort is given; one of firstSeen, lastSeen; default "lastSeen"
    #   format (str, optional, keyword): Response format. JSON when the parameter is left out; one of json, xml; default "json"
    result = api.dns_reverse_v22("8.8.8.8", "a", page=1)
    print(json.dumps(result.to_dict(), indent=2))
