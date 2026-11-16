# Java Runnable Examples

Install: see the [Java guide](../../docs/languages/java.md). Set the `WHOISFREAKS_API_KEY` environment variable and run any file below.

## WHOIS
- [`WhoisLive.java`](WhoisLive.java): Live WHOIS Lookup (`GET /v2.0/whois/live`)
- [`BulkWhois.java`](BulkWhois.java): Bulk WHOIS Lookup (`POST /v2.0/bulkwhois/live`)
- [`WhoisHistory.java`](WhoisHistory.java): Historical WHOIS records for a domain (`GET /v2.0/whois/history`)
- [`WhoisReverse.java`](WhoisReverse.java): Reverse WHOIS lookup by keyword (`GET /v2.0/whois/reverse`)

## DNS
- [`DnsLive.java`](DnsLive.java): Live DNS Lookup (`GET /v2.0/dns/live`)
- [`DnsHistorical.java`](DnsHistorical.java): Historical DNS Lookup (`GET /v2.0/dns/historical`)
- [`DnsReverse.java`](DnsReverse.java): Reverse DNS Lookup (`GET /v2.1/dns/reverse`)
- [`DnsHistoricalV22.java`](DnsHistoricalV22.java): Historical DNS Lookup (v2.2) (`GET /v2.2/dns/historical`)
- [`DnsHistoricalV23.java`](DnsHistoricalV23.java): Historical DNS Lookup (v2.3) (`GET /v2.3/dns/historical`)
- [`DnsReverseV22.java`](DnsReverseV22.java): Reverse DNS Lookup (v2.2) (`GET /v2.2/dns/reverse`)
- [`DnsReverseV23.java`](DnsReverseV23.java): Reverse DNS Lookup (v2.3) (`GET /v2.3/dns/reverse`)
- [`DnsBulk.java`](DnsBulk.java): Bulk DNS Lookup (`POST /v2.0/dns/bulk/live`)

## Domain Availability
- [`DomainAvailabilityV2.java`](DomainAvailabilityV2.java): Domain Availability Check with Suggestions (`GET /v2.0/domain/availability`)
- [`BulkDomainAvailabilityV2.java`](BulkDomainAvailabilityV2.java): Bulk Domain Availability Check (`POST /v2.0/domain/availability`)

## Typosquatting
- [`Typosquatting.java`](Typosquatting.java): Typosquatting Lookup (`GET /v3.0/domain/typos`)

## SSL
- [`SslLookup.java`](SslLookup.java): SSL Certificate Lookup (`GET /v1.0/ssl/live`)

## Geolocation
- [`Geolocation.java`](Geolocation.java): IP Geolocation Lookup (`GET /v1.0/geolocation`)
- [`BulkGeolocation.java`](BulkGeolocation.java): Bulk IP Geolocation (`POST /v1.0/geolocation`)

## Subdomains
- [`Subdomains.java`](Subdomains.java): Subdomains Lookup (`GET /v1.0/subdomains`)

## IP Reputation
- [`IpReputation.java`](IpReputation.java): IP Reputation Lookup (`GET /v1.0/security`)
- [`BulkIpReputation.java`](BulkIpReputation.java): Bulk IP Reputation (`POST /v1.0/security`)
- [`IpReputationV2.java`](IpReputationV2.java): IP Reputation Lookup (v2.0) (`GET /v2.0/security`)
- [`BulkIpReputationV2.java`](BulkIpReputationV2.java): Bulk IP Reputation (v2.0) (`POST /v2.0/security`)

## Domain Reputation
- [`DomainReputation.java`](DomainReputation.java): Domain Reputation Lookup (`GET /v1/domain/security`)

## ASN WHOIS
- [`AsnWhois.java`](AsnWhois.java): ASN WHOIS Lookup (`GET /v2.0/asn-whois`)

## IP WHOIS
- [`IpWhois.java`](IpWhois.java): IP WHOIS Lookup (`GET /v1.0/ip-whois`)

## Account
- [`RotateApiKey.java`](RotateApiKey.java): Rotate API Key (`GET /v1.0/api-key/rotate`)
- [`AccountUsage.java`](AccountUsage.java): Account Usage (`GET /v1.0/whoisapi/usage`)
- [`DatabaseFileStatus.java`](DatabaseFileStatus.java): Database File Status (Public) (`GET /v3.4/status`)

## Databases - Newly Registered
- [`DbNewlyGtld.java`](DbNewlyGtld.java): Newly Registered gTLD (CSV) (`GET /v3.1/download/domainer/gtld`)
- [`DbNewlyCctld.java`](DbNewlyCctld.java): Newly Registered ccTLD (CSV) (`GET /v3.1/download/domainer/cctld`)
- [`DbNewlyGtldCleaned.java`](DbNewlyGtldCleaned.java): Newly Registered gTLD Cleaned WHOIS (CSV) (`GET /v3.1/download/domainer/gtld/cleaned`)
- [`DbNewlyCctldCleaned.java`](DbNewlyCctldCleaned.java): Newly Registered ccTLD Cleaned WHOIS (CSV) (`GET /v3.1/download/domainer/cctld/cleaned`)
- [`DbNewlyGtldJson.java`](DbNewlyGtldJson.java): Newly Registered gTLD (JSON) (`GET /v3.1/domains/newly/gtld`)
- [`DbNewlyCctldJson.java`](DbNewlyCctldJson.java): Newly Registered ccTLD (JSON) (`GET /v3.1/domains/newly/cctld`)
- [`DbNewlyDns.java`](DbNewlyDns.java): Newly Registered With DNS (`GET /v3.1/download/domainer/newly/dns`)

## Databases - Expiring & Dropped
- [`DbExpired.java`](DbExpired.java): Expiring Domains (`GET /v3.1/download/domainer/expired`)
- [`DbExpiredCleaned.java`](DbExpiredCleaned.java): Expiring Cleaned WHOIS (`GET /v3.1/download/domainer/expired/cleaned`)
- [`DbDropped.java`](DbDropped.java): Dropped Domains (`GET /v3.1/download/domainer/dropped`)
- [`DbDroppedJson.java`](DbDroppedJson.java): Dropped Domains (JSON) (`GET /v3.1/domains/dropped`)
- [`DbDroppedBacklinks.java`](DbDroppedBacklinks.java): Dropped With Backlinks (`GET /v3.3/download/domainer/dropped/backlinks`)

## Databases - WHOIS
- [`DbWhoisDaily.java`](DbWhoisDaily.java): WHOIS Database Daily (`GET /v3.3/download/dbupdate/daily/domains/whois`)
- [`DbWhoisWeekly.java`](DbWhoisWeekly.java): WHOIS Database Weekly (`GET /v3.3/download/dbupdate/weekly/domains/whois`)
- [`DbWhoisMonthly.java`](DbWhoisMonthly.java): WHOIS Database Monthly (`GET /v3.3/download/dbupdate/monthly/domains/whois`)

## Databases - DNS
- [`DbDnsDaily.java`](DbDnsDaily.java): DNS Database Daily (`GET /v3.2/download/dbupdate/daily/dns`)
- [`DbDnsWeekly.java`](DbDnsWeekly.java): DNS Database Weekly (`GET /v3.2/download/dbupdate/weekly/dns`)
- [`DbDnsMonthly.java`](DbDnsMonthly.java): DNS Database Monthly (`GET /v3.2/download/dbupdate/monthly/dns`)

## Databases - Subdomains
- [`DbSubdomainsDaily.java`](DbSubdomainsDaily.java): Subdomains Daily (`GET /v3.2/download/dbupdate/daily/subdomains`)
- [`DbSubdomainsWeekly.java`](DbSubdomainsWeekly.java): Subdomains Weekly (`GET /v3.2/download/dbupdate/weekly/subdomains`)
- [`DbSubdomainsMonthly.java`](DbSubdomainsMonthly.java): Subdomains Monthly (`GET /v3.2/download/dbupdate/monthly/subdomains`)

## Databases - IP Geolocation
- [`DbIpCountryStatus.java`](DbIpCountryStatus.java): IP to Country Snapshot Status (`GET /v3.3/status/snapshot/ip/country`)
- [`DbIpCountry.java`](DbIpCountry.java): IP to Country Snapshot (`GET /v3.3/download/snapshot/ip/country`)
- [`DbIpCityStatus.java`](DbIpCityStatus.java): IP to City Snapshot Status (`GET /v3.3/status/snapshot/ip/city`)
- [`DbIpCity.java`](DbIpCity.java): IP to City Snapshot (`GET /v3.3/download/snapshot/ip/city`)

## Databases - ASN WHOIS
- [`DbAsnWhois.java`](DbAsnWhois.java): ASN WHOIS Snapshot (`GET /v3.3/download/snapshot/asn/whois`)
- [`DbAsnWhoisStatus.java`](DbAsnWhoisStatus.java): ASN WHOIS Snapshot Status (`GET /v3.3/status/snapshot/asn/whois`)

## Databases - IP WHOIS
- [`DbIpWhois.java`](DbIpWhois.java): IP WHOIS Snapshot (`GET /v3.3/download/snapshot/ip/whois`)
- [`DbIpWhoisStatus.java`](DbIpWhoisStatus.java): IP WHOIS Snapshot Status (`GET /v3.3/status/snapshot/ip/whois`)

## Databases - IP Security
- [`DbIpSecurity.java`](DbIpSecurity.java): IP Security Snapshot (`GET /v3.3/download/snapshot/ip/security`)
- [`DbIpSecurityStatus.java`](DbIpSecurityStatus.java): IP Security Snapshot Status (`GET /v3.3/status/snapshot/ip/security`)

## Databases - Threat Feed
- [`DownloadThreatFeedPhishing.java`](DownloadThreatFeedPhishing.java): Download the daily phishing threat feed (CSV) (`GET /v3.4/download/threat-feed/phishing`)
- [`DownloadThreatFeedPhishingSample.java`](DownloadThreatFeedPhishingSample.java): Download a sample of the phishing threat feed (CSV) (`GET /v3.4/download/threat-feed/phishing/sample`)
- [`DownloadThreatFeedMalware.java`](DownloadThreatFeedMalware.java): Download the daily malware threat feed (CSV) (`GET /v3.4/download/threat-feed/malware`)
- [`DownloadThreatFeedMalwareSample.java`](DownloadThreatFeedMalwareSample.java): Download a sample of the malware threat feed (CSV) (`GET /v3.4/download/threat-feed/malware/sample`)
- [`DownloadThreatFeedSpam.java`](DownloadThreatFeedSpam.java): Download the daily spam threat feed (CSV) (`GET /v3.4/download/threat-feed/spam`)
- [`DownloadThreatFeedSpamSample.java`](DownloadThreatFeedSpamSample.java): Download a sample of the spam threat feed (CSV) (`GET /v3.4/download/threat-feed/spam/sample`)

## Databases - Streaming
- [`StreamThreatFeedPhishing.java`](StreamThreatFeedPhishing.java): Stream the daily phishing threat feed (CSV) (`GET /v3.4/stream/threat-feed/phishing`)
- [`StreamThreatFeedPhishingSample.java`](StreamThreatFeedPhishingSample.java): Stream a sample of the phishing threat feed (CSV) (`GET /v3.4/stream/threat-feed/phishing/sample`)
- [`StreamThreatFeedMalware.java`](StreamThreatFeedMalware.java): Stream the daily malware threat feed (CSV) (`GET /v3.4/stream/threat-feed/malware`)
- [`StreamThreatFeedMalwareSample.java`](StreamThreatFeedMalwareSample.java): Stream a sample of the malware threat feed (CSV) (`GET /v3.4/stream/threat-feed/malware/sample`)
- [`StreamThreatFeedSpam.java`](StreamThreatFeedSpam.java): Stream the daily spam threat feed (CSV) (`GET /v3.4/stream/threat-feed/spam`)
- [`StreamThreatFeedSpamSample.java`](StreamThreatFeedSpamSample.java): Stream a sample of the spam threat feed (CSV) (`GET /v3.4/stream/threat-feed/spam/sample`)
- [`StreamDomainerGtld.java`](StreamDomainerGtld.java): Stream newly registered gTLD domains (CSV) (`GET /v3.3/stream/domainer/gtld`)
- [`StreamDomainerGtldCleaned.java`](StreamDomainerGtldCleaned.java): Stream cleaned newly registered gTLD domains (CSV) (`GET /v3.3/stream/domainer/gtld/cleaned`)
- [`StreamDomainerGtldCleanedEmail.java`](StreamDomainerGtldCleanedEmail.java): Stream cleaned newly registered gTLD domains with an email (CSV) (`GET /v3.3/stream/domainer/gtld/cleaned/email`)
- [`StreamDomainerGtldCleanedPhone.java`](StreamDomainerGtldCleanedPhone.java): Stream cleaned newly registered gTLD domains with a phone (CSV) (`GET /v3.3/stream/domainer/gtld/cleaned/phone`)
- [`StreamDomainerCctld.java`](StreamDomainerCctld.java): Stream newly registered ccTLD domains (CSV) (`GET /v3.3/stream/domainer/cctld`)
- [`StreamDomainerCctldCleaned.java`](StreamDomainerCctldCleaned.java): Stream cleaned newly registered ccTLD domains (CSV) (`GET /v3.3/stream/domainer/cctld/cleaned`)
- [`StreamDomainerCctldCleanedEmail.java`](StreamDomainerCctldCleanedEmail.java): Stream cleaned newly registered ccTLD domains with an email (CSV) (`GET /v3.3/stream/domainer/cctld/cleaned/email`)
- [`StreamDomainerCctldCleanedPhone.java`](StreamDomainerCctldCleanedPhone.java): Stream cleaned newly registered ccTLD domains with a phone (CSV) (`GET /v3.3/stream/domainer/cctld/cleaned/phone`)
- [`StreamDomainerExpired.java`](StreamDomainerExpired.java): Stream expiring domains (CSV) (`GET /v3.3/stream/domainer/expired`)
- [`StreamDomainerExpiredCleaned.java`](StreamDomainerExpiredCleaned.java): Stream cleaned expiring domains (CSV) (`GET /v3.3/stream/domainer/expired/cleaned`)
- [`StreamDomainerExpiredCleanedEmail.java`](StreamDomainerExpiredCleanedEmail.java): Stream cleaned expiring domains with an email (CSV) (`GET /v3.3/stream/domainer/expired/cleaned/email`)
- [`StreamDomainerExpiredCleanedPhone.java`](StreamDomainerExpiredCleanedPhone.java): Stream cleaned expiring domains with a phone (CSV) (`GET /v3.3/stream/domainer/expired/cleaned/phone`)
- [`StreamDomainerDropped.java`](StreamDomainerDropped.java): Stream dropped domains (CSV) (`GET /v3.3/stream/domainer/dropped`)
- [`StreamDomainerDroppedBacklinks.java`](StreamDomainerDroppedBacklinks.java): Stream dropped domains with backlinks (CSV) (`GET /v3.3/stream/domainer/dropped/backlinks`)
- [`StreamDomainerGtldSample.java`](StreamDomainerGtldSample.java): Stream a sample of newly registered gTLD domains (CSV) (`GET /v3.3/stream/domainer/sample/gtld`)
- [`StreamDomainerGtldCleanedSample.java`](StreamDomainerGtldCleanedSample.java): Stream a sample of cleaned newly registered gTLD domains (CSV) (`GET /v3.3/stream/domainer/sample/gtld/cleaned`)
- [`StreamDomainerCctldSample.java`](StreamDomainerCctldSample.java): Stream a sample of newly registered ccTLD domains (CSV) (`GET /v3.3/stream/domainer/sample/cctld`)
- [`StreamDomainerCctldCleanedSample.java`](StreamDomainerCctldCleanedSample.java): Stream a sample of cleaned newly registered ccTLD domains (CSV) (`GET /v3.3/stream/domainer/sample/cctld/cleaned`)
- [`StreamDomainerExpiredSample.java`](StreamDomainerExpiredSample.java): Stream a sample of expiring domains (CSV) (`GET /v3.3/stream/domainer/sample/expired`)
- [`StreamDomainerExpiredCleanedSample.java`](StreamDomainerExpiredCleanedSample.java): Stream a sample of cleaned expiring domains (CSV) (`GET /v3.3/stream/domainer/sample/expired/cleaned`)
- [`StreamDomainerDroppedSample.java`](StreamDomainerDroppedSample.java): Stream a sample of dropped domains (CSV) (`GET /v3.3/stream/domainer/sample/dropped`)
- [`StreamDomainerDroppedBacklinksSample.java`](StreamDomainerDroppedBacklinksSample.java): Stream a sample of dropped domains with backlinks (CSV) (`GET /v3.3/stream/domainer/sample/dropped/backlinks`)
