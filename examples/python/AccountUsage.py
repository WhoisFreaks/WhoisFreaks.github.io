"""Account Usage: GET https://api.whoisfreaks.com/v1.0/whoisapi/usage

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python AccountUsage.py
"""
import json
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.AccountApi(client)

    # account_usage takes no parameters.
    result = api.account_usage()
    print(json.dumps(result.to_dict(), indent=2))
