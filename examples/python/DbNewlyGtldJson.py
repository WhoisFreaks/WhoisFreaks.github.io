"""Newly Registered gTLD (JSON): GET https://files.whoisfreaks.com/v3.1/domains/newly/gtld

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DbNewlyGtldJson.py
"""
import os
from datetime import date

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesNewlyRegisteredApi(client)

    # db_newly_gtld_json parameters:
    #   var_date (datetime.date, optional, keyword): yyyy-MM-dd; omit for latest
    #   tlds (str, optional, keyword)
    domains = api.db_newly_gtld_json(var_date=date(2026, 10, 1))
    print(f"{len(domains)} domains")
    print("\n".join(domains[:10]))
