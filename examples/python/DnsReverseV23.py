"""Reverse DNS Lookup (v2.3): GET https://api.whoisfreaks.com/v2.3/dns/reverse

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DnsReverseV23.py
"""
import json
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DNSApi(client)

    # dns_reverse_v23 parameters:
    #   value (str, required): IP, CIDR, or record value
    #   type (str, required): one of a, mx, cname, ns, aaaa, txt, soa
    #   exact (bool, optional, keyword): When false the value is matched as a substring, which is far slower than an e...; default True
    #   page (int, optional, keyword): default 1
    #   sort (str, optional, keyword): Sort direction. Omit to leave the results unsorted; one of asc, desc
    #   sort_by (str, optional, keyword): Field to sort on. Only applies when sort is given; one of firstSeen, lastSeen; default "lastSeen"
    #   format (str, optional, keyword): one of json, xml; default "json"
    result = api.dns_reverse_v23("8.8.8.8", "a", page=1)
    print(json.dumps(result.to_dict(), indent=2))
