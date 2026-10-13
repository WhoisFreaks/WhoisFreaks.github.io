"""IP Reputation Lookup: GET https://api.whoisfreaks.com/v1.0/security

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python IpReputation.py
"""
import json
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.IPReputationApi(client)

    # ip_reputation parameters:
    #   ip (str, required)
    result = api.ip_reputation("8.8.8.8")
    print(json.dumps(result.to_dict(), indent=2))
