"""IP to Country Snapshot Status: GET https://files.whoisfreaks.com/v3.3/status/snapshot/ip/country

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DbIpCountryStatus.py
"""
import json
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesIPGeolocationApi(client)

    # db_ip_country_status takes no parameters.
    result = api.db_ip_country_status()
    print(json.dumps(result.to_dict(), indent=2))
