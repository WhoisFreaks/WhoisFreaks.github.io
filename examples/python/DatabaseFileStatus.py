"""Database File Status (Public): GET https://files.whoisfreaks.com/v3.4/status

Run it (public endpoint, no API key needed):
    python DatabaseFileStatus.py
"""
import json

import whoisfreaks

config = whoisfreaks.Configuration()
# Public endpoint: no API key needed.

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.AccountApi(client)

    # database_file_status takes no parameters.
    result = api.database_file_status()
    print(json.dumps(result.to_dict(), indent=2))
