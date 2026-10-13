"""Bulk IP Reputation: POST https://api.whoisfreaks.com/v1.0/security

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python BulkIpReputation.py
"""
import json
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.IPReputationApi(client)

    # bulk_ip_reputation parameters:
    #   bulk_geolocation_request (BulkGeolocationRequest, required): request body
    body = whoisfreaks.BulkGeolocationRequest(ips=["8.8.8.8", "1.1.1.1"])
    results = api.bulk_ip_reputation(body)
    print(json.dumps([item.to_dict() for item in results], indent=2))
