"""Bulk IP Geolocation: POST https://api.whoisfreaks.com/v1.0/geolocation

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python BulkGeolocation.py
"""
import json
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.GeolocationApi(client)

    # bulk_geolocation parameters:
    #   bulk_geolocation_request (BulkGeolocationRequest, required): request body
    body = whoisfreaks.BulkGeolocationRequest(ips=["8.8.8.8", "1.1.1.1"])
    results = api.bulk_geolocation(body)
    print(json.dumps([item.to_dict() for item in results], indent=2))
