"""Rotate API Key: GET https://api.whoisfreaks.com/v1.0/api-key/rotate

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python RotateApiKey.py
"""
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.AccountApi(client)

    # rotate_api_key takes no parameters.
    new_key = api.rotate_api_key()  # use this key from now on
    print("New API key:", new_key)
