"""Live DNS Lookup: GET https://api.whoisfreaks.com/v2.0/dns/live

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DnsLive.py
"""
import json
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DNSApi(client)

    # dns_live parameters:
    #   type (str, required): all or comma-separated: A,MX,NS,TXT,SOA,SPF,AAAA,CNAME; default "all"
    #   domain_name (str, optional, keyword)
    #   ip_address (str, optional, keyword): Use for PTR lookups
    #   format (str, optional, keyword): one of json, xml; default "json"
    result = api.dns_live("A,MX,TXT", domain_name="whoisfreaks.com")
    print(json.dumps(result.to_dict(), indent=2))
