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
    #   domain_name (str, required): Domain to look up
    #   chain (bool, optional, keyword): Set true to return the full certificate chain, ordered from the end-user cert...; default False
    #   ssl_raw (bool, optional, keyword): Set true to include the raw OpenSSL response for the domain. Defaults to false; default False
    #   format (str, optional, keyword): Response format. JSON when the parameter is left out; one of json, xml; default "json"
    result = api.ssl_lookup("whoisfreaks.com")
    print(json.dumps(result.to_dict(), indent=2))
