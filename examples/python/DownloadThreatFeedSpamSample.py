"""Download a sample of the spam threat feed (CSV): GET https://files.whoisfreaks.com/v3.4/download/threat-feed/spam/sample

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DownloadThreatFeedSpamSample.py
"""
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesThreatFeedApi(client)

    # download_threat_feed_spam_sample takes no parameters.
    data = api.download_threat_feed_spam_sample()  # the file's raw bytes
    path = "DownloadThreatFeedSpamSample.csv"
    with open(path, "wb") as f:
        f.write(data)
    print(f"Saved {len(data)} bytes to {os.path.abspath(path)}")
