"""Subdomains Monthly: GET https://files.whoisfreaks.com/v3.2/download/dbupdate/monthly/subdomains

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DbSubdomainsMonthly.py
"""
import os
from datetime import date

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesSubdomainsApi(client)

    # db_subdomains_monthly parameters:
    #   var_date (datetime.date, optional, keyword): yyyy-MM-dd; omit for latest
    data = api.db_subdomains_monthly(var_date=date(2026, 10, 1))  # the file's raw bytes
    path = "DbSubdomainsMonthly.csv"
    with open(path, "wb") as f:
        f.write(data)
    print(f"Saved {len(data)} bytes to {os.path.abspath(path)}")
