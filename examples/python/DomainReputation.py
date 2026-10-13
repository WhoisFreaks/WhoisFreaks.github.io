"""Domain Reputation Lookup: GET https://api.whoisfreaks.com/v1/domain/security

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DomainReputation.py
"""
import json
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DomainReputationApi(client)

    # domain_reputation parameters:
    #   domain_name (str, required): The domain name to assess
    #   format (str, optional, keyword): one of json, xml; default "json"
    result = api.domain_reputation("amazon.com")
    print(json.dumps(result.to_dict(), indent=2))
