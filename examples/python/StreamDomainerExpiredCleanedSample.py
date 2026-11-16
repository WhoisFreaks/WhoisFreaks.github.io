"""Stream a sample of cleaned expiring domains (CSV): GET https://files.whoisfreaks.com/v3.3/stream/domainer/sample/expired/cleaned

Run it (public endpoint, no API key needed):
    python StreamDomainerExpiredCleanedSample.py
"""

import whoisfreaks

config = whoisfreaks.Configuration()
# Public endpoint: no API key needed.

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesStreamingApi(client)

    # stream_domainer_expired_cleaned_sample parameters:
    #   whois (bool, optional, keyword): true streams the full WHOIS record per domain with a CSV header row; false st...; default False
    #   offset (int, optional, keyword): Data rows to skip from the start of the file. The header row is never counted...
    #   limit (int, optional, keyword): Maximum data rows to return. Omit for the whole file. limit=0 returns the hea...
    new_key = api.stream_domainer_expired_cleaned_sample()  # use this key from now on
    print("New API key:", new_key)
