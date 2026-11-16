# JavaScript Runnable Examples

Install: see the [JavaScript guide](../../docs/languages/javascript.md). Set the `WHOISFREAKS_API_KEY` environment variable and run any file below.

## WHOIS
- [`WhoisLive.js`](WhoisLive.js): Live WHOIS Lookup (`GET /v2.0/whois/live`)
- [`BulkWhois.js`](BulkWhois.js): Bulk WHOIS Lookup (`POST /v2.0/bulkwhois/live`)
- [`WhoisHistory.js`](WhoisHistory.js): Historical WHOIS records for a domain (`GET /v2.0/whois/history`)
- [`WhoisReverse.js`](WhoisReverse.js): Reverse WHOIS lookup by keyword (`GET /v2.0/whois/reverse`)

## DNS
- [`DnsLive.js`](DnsLive.js): Live DNS Lookup (`GET /v2.0/dns/live`)
- [`DnsHistorical.js`](DnsHistorical.js): Historical DNS Lookup (`GET /v2.0/dns/historical`)
- [`DnsReverse.js`](DnsReverse.js): Reverse DNS Lookup (`GET /v2.1/dns/reverse`)
- [`DnsHistoricalV22.js`](DnsHistoricalV22.js): Historical DNS Lookup (v2.2) (`GET /v2.2/dns/historical`)
- [`DnsHistoricalV23.js`](DnsHistoricalV23.js): Historical DNS Lookup (v2.3) (`GET /v2.3/dns/historical`)
- [`DnsReverseV22.js`](DnsReverseV22.js): Reverse DNS Lookup (v2.2) (`GET /v2.2/dns/reverse`)
- [`DnsReverseV23.js`](DnsReverseV23.js): Reverse DNS Lookup (v2.3) (`GET /v2.3/dns/reverse`)
- [`DnsBulk.js`](DnsBulk.js): Bulk DNS Lookup (`POST /v2.0/dns/bulk/live`)

## Domain Availability
- [`DomainAvailabilityV2.js`](DomainAvailabilityV2.js): Domain Availability Check with Suggestions (`GET /v2.0/domain/availability`)
- [`BulkDomainAvailabilityV2.js`](BulkDomainAvailabilityV2.js): Bulk Domain Availability Check (`POST /v2.0/domain/availability`)

## Typosquatting
- [`Typosquatting.js`](Typosquatting.js): Typosquatting Lookup (`GET /v3.0/domain/typos`)

## SSL
- [`SslLookup.js`](SslLookup.js): SSL Certificate Lookup (`GET /v1.0/ssl/live`)

## Geolocation
- [`Geolocation.js`](Geolocation.js): IP Geolocation Lookup (`GET /v1.0/geolocation`)
- [`BulkGeolocation.js`](BulkGeolocation.js): Bulk IP Geolocation (`POST /v1.0/geolocation`)

## Subdomains
- [`Subdomains.js`](Subdomains.js): Subdomains Lookup (`GET /v1.0/subdomains`)

## IP Reputation
- [`IpReputation.js`](IpReputation.js): IP Reputation Lookup (`GET /v1.0/security`)
- [`BulkIpReputation.js`](BulkIpReputation.js): Bulk IP Reputation (`POST /v1.0/security`)
- [`IpReputationV2.js`](IpReputationV2.js): IP Reputation Lookup (v2.0) (`GET /v2.0/security`)
- [`BulkIpReputationV2.js`](BulkIpReputationV2.js): Bulk IP Reputation (v2.0) (`POST /v2.0/security`)

## Domain Reputation
- [`DomainReputation.js`](DomainReputation.js): Domain Reputation Lookup (`GET /v1/domain/security`)

## ASN WHOIS
- [`AsnWhois.js`](AsnWhois.js): ASN WHOIS Lookup (`GET /v2.0/asn-whois`)

## IP WHOIS
- [`IpWhois.js`](IpWhois.js): IP WHOIS Lookup (`GET /v1.0/ip-whois`)

## Account
- [`RotateApiKey.js`](RotateApiKey.js): Rotate API Key (`GET /v1.0/api-key/rotate`)
- [`AccountUsage.js`](AccountUsage.js): Account Usage (`GET /v1.0/whoisapi/usage`)
- [`DatabaseFileStatus.js`](DatabaseFileStatus.js): Database File Status (Public) (`GET /v3.4/status`)

## Databases - Newly Registered
- [`DbNewlyGtld.js`](DbNewlyGtld.js): Newly Registered gTLD (CSV) (`GET /v3.1/download/domainer/gtld`)
- [`DbNewlyCctld.js`](DbNewlyCctld.js): Newly Registered ccTLD (CSV) (`GET /v3.1/download/domainer/cctld`)
- [`DbNewlyGtldCleaned.js`](DbNewlyGtldCleaned.js): Newly Registered gTLD Cleaned WHOIS (CSV) (`GET /v3.1/download/domainer/gtld/cleaned`)
- [`DbNewlyCctldCleaned.js`](DbNewlyCctldCleaned.js): Newly Registered ccTLD Cleaned WHOIS (CSV) (`GET /v3.1/download/domainer/cctld/cleaned`)
- [`DbNewlyGtldJson.js`](DbNewlyGtldJson.js): Newly Registered gTLD (JSON) (`GET /v3.1/domains/newly/gtld`)
- [`DbNewlyCctldJson.js`](DbNewlyCctldJson.js): Newly Registered ccTLD (JSON) (`GET /v3.1/domains/newly/cctld`)
- [`DbNewlyDns.js`](DbNewlyDns.js): Newly Registered With DNS (`GET /v3.1/download/domainer/newly/dns`)

## Databases - Expiring & Dropped
- [`DbExpired.js`](DbExpired.js): Expiring Domains (`GET /v3.1/download/domainer/expired`)
- [`DbExpiredCleaned.js`](DbExpiredCleaned.js): Expiring Cleaned WHOIS (`GET /v3.1/download/domainer/expired/cleaned`)
- [`DbDropped.js`](DbDropped.js): Dropped Domains (`GET /v3.1/download/domainer/dropped`)
- [`DbDroppedJson.js`](DbDroppedJson.js): Dropped Domains (JSON) (`GET /v3.1/domains/dropped`)
- [`DbDroppedBacklinks.js`](DbDroppedBacklinks.js): Dropped With Backlinks (`GET /v3.3/download/domainer/dropped/backlinks`)

## Databases - WHOIS
- [`DbWhoisDaily.js`](DbWhoisDaily.js): WHOIS Database Daily (`GET /v3.3/download/dbupdate/daily/domains/whois`)
- [`DbWhoisWeekly.js`](DbWhoisWeekly.js): WHOIS Database Weekly (`GET /v3.3/download/dbupdate/weekly/domains/whois`)
- [`DbWhoisMonthly.js`](DbWhoisMonthly.js): WHOIS Database Monthly (`GET /v3.3/download/dbupdate/monthly/domains/whois`)

## Databases - DNS
- [`DbDnsDaily.js`](DbDnsDaily.js): DNS Database Daily (`GET /v3.2/download/dbupdate/daily/dns`)
- [`DbDnsWeekly.js`](DbDnsWeekly.js): DNS Database Weekly (`GET /v3.2/download/dbupdate/weekly/dns`)
- [`DbDnsMonthly.js`](DbDnsMonthly.js): DNS Database Monthly (`GET /v3.2/download/dbupdate/monthly/dns`)

## Databases - Subdomains
- [`DbSubdomainsDaily.js`](DbSubdomainsDaily.js): Subdomains Daily (`GET /v3.2/download/dbupdate/daily/subdomains`)
- [`DbSubdomainsWeekly.js`](DbSubdomainsWeekly.js): Subdomains Weekly (`GET /v3.2/download/dbupdate/weekly/subdomains`)
- [`DbSubdomainsMonthly.js`](DbSubdomainsMonthly.js): Subdomains Monthly (`GET /v3.2/download/dbupdate/monthly/subdomains`)

## Databases - IP Geolocation
- [`DbIpCountryStatus.js`](DbIpCountryStatus.js): IP to Country Snapshot Status (`GET /v3.3/status/snapshot/ip/country`)
- [`DbIpCountry.js`](DbIpCountry.js): IP to Country Snapshot (`GET /v3.3/download/snapshot/ip/country`)
- [`DbIpCityStatus.js`](DbIpCityStatus.js): IP to City Snapshot Status (`GET /v3.3/status/snapshot/ip/city`)
- [`DbIpCity.js`](DbIpCity.js): IP to City Snapshot (`GET /v3.3/download/snapshot/ip/city`)

## Databases - ASN WHOIS
- [`DbAsnWhois.js`](DbAsnWhois.js): ASN WHOIS Snapshot (`GET /v3.3/download/snapshot/asn/whois`)
- [`DbAsnWhoisStatus.js`](DbAsnWhoisStatus.js): ASN WHOIS Snapshot Status (`GET /v3.3/status/snapshot/asn/whois`)

## Databases - IP WHOIS
- [`DbIpWhois.js`](DbIpWhois.js): IP WHOIS Snapshot (`GET /v3.3/download/snapshot/ip/whois`)
- [`DbIpWhoisStatus.js`](DbIpWhoisStatus.js): IP WHOIS Snapshot Status (`GET /v3.3/status/snapshot/ip/whois`)

## Databases - IP Security
- [`DbIpSecurity.js`](DbIpSecurity.js): IP Security Snapshot (`GET /v3.3/download/snapshot/ip/security`)
- [`DbIpSecurityStatus.js`](DbIpSecurityStatus.js): IP Security Snapshot Status (`GET /v3.3/status/snapshot/ip/security`)

## Databases - Threat Feed
- [`DownloadThreatFeedPhishing.js`](DownloadThreatFeedPhishing.js): Download the daily phishing threat feed (CSV) (`GET /v3.4/download/threat-feed/phishing`)
- [`DownloadThreatFeedPhishingSample.js`](DownloadThreatFeedPhishingSample.js): Download a sample of the phishing threat feed (CSV) (`GET /v3.4/download/threat-feed/phishing/sample`)
- [`DownloadThreatFeedMalware.js`](DownloadThreatFeedMalware.js): Download the daily malware threat feed (CSV) (`GET /v3.4/download/threat-feed/malware`)
- [`DownloadThreatFeedMalwareSample.js`](DownloadThreatFeedMalwareSample.js): Download a sample of the malware threat feed (CSV) (`GET /v3.4/download/threat-feed/malware/sample`)
- [`DownloadThreatFeedSpam.js`](DownloadThreatFeedSpam.js): Download the daily spam threat feed (CSV) (`GET /v3.4/download/threat-feed/spam`)
- [`DownloadThreatFeedSpamSample.js`](DownloadThreatFeedSpamSample.js): Download a sample of the spam threat feed (CSV) (`GET /v3.4/download/threat-feed/spam/sample`)

## Databases - Streaming
- [`StreamThreatFeedPhishing.js`](StreamThreatFeedPhishing.js): Stream the daily phishing threat feed (CSV) (`GET /v3.4/stream/threat-feed/phishing`)
- [`StreamThreatFeedPhishingSample.js`](StreamThreatFeedPhishingSample.js): Stream a sample of the phishing threat feed (CSV) (`GET /v3.4/stream/threat-feed/phishing/sample`)
- [`StreamThreatFeedMalware.js`](StreamThreatFeedMalware.js): Stream the daily malware threat feed (CSV) (`GET /v3.4/stream/threat-feed/malware`)
- [`StreamThreatFeedMalwareSample.js`](StreamThreatFeedMalwareSample.js): Stream a sample of the malware threat feed (CSV) (`GET /v3.4/stream/threat-feed/malware/sample`)
- [`StreamThreatFeedSpam.js`](StreamThreatFeedSpam.js): Stream the daily spam threat feed (CSV) (`GET /v3.4/stream/threat-feed/spam`)
- [`StreamThreatFeedSpamSample.js`](StreamThreatFeedSpamSample.js): Stream a sample of the spam threat feed (CSV) (`GET /v3.4/stream/threat-feed/spam/sample`)
- [`StreamDomainerGtld.js`](StreamDomainerGtld.js): Stream newly registered gTLD domains (CSV) (`GET /v3.3/stream/domainer/gtld`)
- [`StreamDomainerGtldCleaned.js`](StreamDomainerGtldCleaned.js): Stream cleaned newly registered gTLD domains (CSV) (`GET /v3.3/stream/domainer/gtld/cleaned`)
- [`StreamDomainerGtldCleanedEmail.js`](StreamDomainerGtldCleanedEmail.js): Stream cleaned newly registered gTLD domains with an email (CSV) (`GET /v3.3/stream/domainer/gtld/cleaned/email`)
- [`StreamDomainerGtldCleanedPhone.js`](StreamDomainerGtldCleanedPhone.js): Stream cleaned newly registered gTLD domains with a phone (CSV) (`GET /v3.3/stream/domainer/gtld/cleaned/phone`)
- [`StreamDomainerCctld.js`](StreamDomainerCctld.js): Stream newly registered ccTLD domains (CSV) (`GET /v3.3/stream/domainer/cctld`)
- [`StreamDomainerCctldCleaned.js`](StreamDomainerCctldCleaned.js): Stream cleaned newly registered ccTLD domains (CSV) (`GET /v3.3/stream/domainer/cctld/cleaned`)
- [`StreamDomainerCctldCleanedEmail.js`](StreamDomainerCctldCleanedEmail.js): Stream cleaned newly registered ccTLD domains with an email (CSV) (`GET /v3.3/stream/domainer/cctld/cleaned/email`)
- [`StreamDomainerCctldCleanedPhone.js`](StreamDomainerCctldCleanedPhone.js): Stream cleaned newly registered ccTLD domains with a phone (CSV) (`GET /v3.3/stream/domainer/cctld/cleaned/phone`)
- [`StreamDomainerExpired.js`](StreamDomainerExpired.js): Stream expiring domains (CSV) (`GET /v3.3/stream/domainer/expired`)
- [`StreamDomainerExpiredCleaned.js`](StreamDomainerExpiredCleaned.js): Stream cleaned expiring domains (CSV) (`GET /v3.3/stream/domainer/expired/cleaned`)
- [`StreamDomainerExpiredCleanedEmail.js`](StreamDomainerExpiredCleanedEmail.js): Stream cleaned expiring domains with an email (CSV) (`GET /v3.3/stream/domainer/expired/cleaned/email`)
- [`StreamDomainerExpiredCleanedPhone.js`](StreamDomainerExpiredCleanedPhone.js): Stream cleaned expiring domains with a phone (CSV) (`GET /v3.3/stream/domainer/expired/cleaned/phone`)
- [`StreamDomainerDropped.js`](StreamDomainerDropped.js): Stream dropped domains (CSV) (`GET /v3.3/stream/domainer/dropped`)
- [`StreamDomainerDroppedBacklinks.js`](StreamDomainerDroppedBacklinks.js): Stream dropped domains with backlinks (CSV) (`GET /v3.3/stream/domainer/dropped/backlinks`)
- [`StreamDomainerGtldSample.js`](StreamDomainerGtldSample.js): Stream a sample of newly registered gTLD domains (CSV) (`GET /v3.3/stream/domainer/sample/gtld`)
- [`StreamDomainerGtldCleanedSample.js`](StreamDomainerGtldCleanedSample.js): Stream a sample of cleaned newly registered gTLD domains (CSV) (`GET /v3.3/stream/domainer/sample/gtld/cleaned`)
- [`StreamDomainerCctldSample.js`](StreamDomainerCctldSample.js): Stream a sample of newly registered ccTLD domains (CSV) (`GET /v3.3/stream/domainer/sample/cctld`)
- [`StreamDomainerCctldCleanedSample.js`](StreamDomainerCctldCleanedSample.js): Stream a sample of cleaned newly registered ccTLD domains (CSV) (`GET /v3.3/stream/domainer/sample/cctld/cleaned`)
- [`StreamDomainerExpiredSample.js`](StreamDomainerExpiredSample.js): Stream a sample of expiring domains (CSV) (`GET /v3.3/stream/domainer/sample/expired`)
- [`StreamDomainerExpiredCleanedSample.js`](StreamDomainerExpiredCleanedSample.js): Stream a sample of cleaned expiring domains (CSV) (`GET /v3.3/stream/domainer/sample/expired/cleaned`)
- [`StreamDomainerDroppedSample.js`](StreamDomainerDroppedSample.js): Stream a sample of dropped domains (CSV) (`GET /v3.3/stream/domainer/sample/dropped`)
- [`StreamDomainerDroppedBacklinksSample.js`](StreamDomainerDroppedBacklinksSample.js): Stream a sample of dropped domains with backlinks (CSV) (`GET /v3.3/stream/domainer/sample/dropped/backlinks`)
