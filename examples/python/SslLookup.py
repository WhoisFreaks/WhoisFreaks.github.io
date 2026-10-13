"""SSL Certificate Lookup: GET https://api.whoisfreaks.com/v1.0/ssl/live

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python SslLookup.py
"""
import json
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.SSLApi(client)

    # ssl_lookup parameters:
    #   domain_name (str, required)
    #   chain (bool, optional, keyword): default False
    #   ssl_raw (bool, optional, keyword): default False
    #   format (str, optional, keyword): one of json, xml; default "json"
    result = api.ssl_lookup("whoisfreaks.com")
    print(json.dumps(result.to_dict(), indent=2))
