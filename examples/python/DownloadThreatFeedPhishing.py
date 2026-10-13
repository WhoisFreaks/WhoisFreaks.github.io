"""Download the daily phishing threat feed (CSV): GET https://files.whoisfreaks.com/v3.4/download/threat-feed/phishing

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DownloadThreatFeedPhishing.py
"""
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesThreatFeedApi(client)

    # download_threat_feed_phishing parameters:
    #   var_date (str, optional, keyword): Feed date (yyyy-MM-dd); omit for the full dump of the feed
    data = api.download_threat_feed_phishing(var_date="2026-10-01")  # the file's raw bytes
    path = "DownloadThreatFeedPhishing.csv"
    with open(path, "wb") as f:
        f.write(data)
    print(f"Saved {len(data)} bytes to {os.path.abspath(path)}")
