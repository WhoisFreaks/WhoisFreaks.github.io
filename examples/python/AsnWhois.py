"""ASN WHOIS Lookup: GET https://api.whoisfreaks.com/v2.0/asn-whois

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python AsnWhois.py
"""
import json
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.ASNWHOISApi(client)

    # asn_whois parameters:
    #   asn (str, required)
    #   format (str, optional, keyword): one of json, xml; default "json"
    result = api.asn_whois("as15169")
    print(json.dumps(result.to_dict(), indent=2))
