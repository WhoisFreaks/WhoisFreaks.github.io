"""IP Security Snapshot Status: GET https://files.whoisfreaks.com/v3.3/status/snapshot/ip/security

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DbIpSecurityStatus.py
"""
import json
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesIPSecurityApi(client)

    # db_ip_security_status takes no parameters.
    result = api.db_ip_security_status()
    print(json.dumps(result.to_dict(), indent=2))
