"""ASN WHOIS Snapshot: GET https://files.whoisfreaks.com/v3.3/download/snapshot/asn/whois

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DbAsnWhois.py
"""
import os
from datetime import date

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesASNWHOISApi(client)

    # db_asn_whois parameters:
    #   var_date (datetime.date, required)
    data = api.db_asn_whois(date(2026, 10, 1))  # the file's raw bytes
    path = "DbAsnWhois.json.gz"
    with open(path, "wb") as f:
        f.write(data)
    print(f"Saved {len(data)} bytes to {os.path.abspath(path)}")
