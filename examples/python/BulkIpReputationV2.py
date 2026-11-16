"""Bulk IP Reputation (v2.0): POST https://api.whoisfreaks.com/v2.0/security

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python BulkIpReputationV2.py
"""
import json
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.IPReputationApi(client)

    # bulk_ip_reputation_v2 parameters:
    #   bulk_geolocation_request (BulkGeolocationRequest, required): request body
    body = whoisfreaks.BulkGeolocationRequest(ips=["1.1.1.1", "2.2.2.2", "8.8.8.8"])
    results = api.bulk_ip_reputation_v2(body)
    print(json.dumps([item.to_dict() for item in results], indent=2))
