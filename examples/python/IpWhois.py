"""IP WHOIS Lookup: GET https://api.whoisfreaks.com/v1.0/ip-whois

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python IpWhois.py
"""
import json
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.IPWHOISApi(client)

    # ip_whois parameters:
    #   ip (str, required)
    #   format (str, optional, keyword): one of json, xml; default "json"
    result = api.ip_whois("8.8.8.8")
    print(json.dumps(result.to_dict(), indent=2))
