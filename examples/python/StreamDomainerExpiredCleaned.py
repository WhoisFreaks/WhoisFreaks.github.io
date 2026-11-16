"""Stream cleaned expiring domains (CSV): GET https://files.whoisfreaks.com/v3.3/stream/domainer/expired/cleaned

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python StreamDomainerExpiredCleaned.py
"""
import os
from datetime import date

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesStreamingApi(client)

    # stream_domainer_expired_cleaned parameters:
    #   var_date (datetime.date, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints
    #   whois (bool, optional, keyword): true streams the full WHOIS record per domain with a CSV header row; false st...; default False
    #   offset (int, optional, keyword): Data rows to skip from the start of the file. The header row is never counted...
    #   limit (int, optional, keyword): Maximum data rows to return. Omit for the whole file. limit=0 returns the hea...
    new_key = api.stream_domainer_expired_cleaned(date(2026, 10, 1))  # use this key from now on
    print("New API key:", new_key)
