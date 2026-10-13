"""Bulk Domain Availability Check: POST https://api.whoisfreaks.com/v2.0/domain/availability

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python BulkDomainAvailabilityV2.py
"""
import json
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DomainAvailabilityApi(client)

    # bulk_domain_availability_v2 parameters:
    #   bulk_domain_availability_request (BulkDomainAvailabilityRequest, required): request body
    #   domain (str, optional, keyword): Required for TLD-mode bulk check (base domain)
    #   format (str, optional, keyword): one of json, xml; default "json"
    body = whoisfreaks.BulkDomainAvailabilityRequest(domain_names=["whoisfreaks.com", "example.com"])
    result = api.bulk_domain_availability_v2(body)
    print(json.dumps(result.to_dict(), indent=2))
