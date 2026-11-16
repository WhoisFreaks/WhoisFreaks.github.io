"""Stream a sample of the spam threat feed (CSV): GET https://files.whoisfreaks.com/v3.4/stream/threat-feed/spam/sample

Run it (public endpoint, no API key needed):
    python StreamThreatFeedSpamSample.py
"""

import whoisfreaks

config = whoisfreaks.Configuration()
# Public endpoint: no API key needed.

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesStreamingApi(client)

    # stream_threat_feed_spam_sample parameters:
    #   offset (int, optional, keyword): Data rows to skip from the start of the file. The header row is never counted...
    #   limit (int, optional, keyword): Maximum data rows to return. Omit for the whole file. limit=0 returns the hea...
    csv_text = api.stream_threat_feed_spam_sample()  # plain CSV text, already decompressed
    print(csv_text)
