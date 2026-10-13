"""Historical WHOIS records for a domain: GET https://api.whoisfreaks.com/v2.0/whois/history

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python WhoisHistory.py
"""
import json
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.WHOISApi(client)

    # whois_history parameters:
    #   domain_name (str, required): Domain to fetch historical WHOIS records for
    #   format (str, optional, keyword): one of json, xml
    result = api.whois_history("whoisfreaks.com")
    print(json.dumps(result.to_dict(), indent=2))
