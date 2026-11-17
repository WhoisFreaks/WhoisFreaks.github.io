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
    #   domain_name (str, optional, keyword): Domain to look up
    #   ip_address (str, optional, keyword): Use for PTR lookups
    #   cname_depth (int, optional, keyword): How many CNAME links to follow before returning the records they point at. 0,...; default 0
    #   relative_records (bool, optional, keyword): Keeps the records picked up for other names along the way, such as a CNAME ta...; default True
    #   is_authoritative (bool, optional, keyword): Set true to read the records from the zone's own nameservers instead of a rec...; default False
    #   format (str, optional, keyword): Response format. JSON when the parameter is left out; one of json, xml; default "json"
    result = api.dns_live("A,MX,TXT", domain_name="whoisfreaks.com")
    print(json.dumps(result.to_dict(), indent=2))
