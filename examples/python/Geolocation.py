"""IP Geolocation Lookup: GET https://api.whoisfreaks.com/v1.0/geolocation

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python Geolocation.py
"""
import json
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.GeolocationApi(client)

    # geolocation parameters:
    #   ip (str, required)
    result = api.geolocation("8.8.8.8")
    print(json.dumps(result.to_dict(), indent=2))
