"""IP WHOIS Snapshot Status: GET https://files.whoisfreaks.com/v3.3/status/snapshot/ip/whois

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DbIpWhoisStatus.py
"""
import json
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesIPWHOISApi(client)

    # db_ip_whois_status takes no parameters.
    result = api.db_ip_whois_status()
    print(json.dumps(result.to_dict(), indent=2))
