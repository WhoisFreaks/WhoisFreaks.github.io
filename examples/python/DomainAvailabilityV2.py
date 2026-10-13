"""Domain Availability Check with Suggestions: GET https://api.whoisfreaks.com/v2.0/domain/availability

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DomainAvailabilityV2.py
"""
import json
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DomainAvailabilityApi(client)

    # domain_availability_v2 parameters:
    #   domain (str, required): The domain name to check
    #   sug (bool, optional, keyword): Whether to return TLD suggestions alongside the queried domain; default False
    #   count (int, optional, keyword): Number of TLD suggestions to return when sug=true. Maximum is 100; default 5
    #   format (str, optional, keyword): one of json, xml; default "json"
    result = api.domain_availability_v2("google.com", sug=True, count=5)
    print(json.dumps(result.to_dict(), indent=2))
