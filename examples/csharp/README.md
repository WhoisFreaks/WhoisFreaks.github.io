# C# / .NET Runnable Examples

Install: see the [C# / .NET guide](../../docs/languages/csharp.md). Set the `WHOISFREAKS_API_KEY` environment variable and run any file below.

## WHOIS
- [`WhoisLive.cs`](WhoisLive.cs): Live WHOIS Lookup (`GET /v2.0/whois/live`)
- [`BulkWhois.cs`](BulkWhois.cs): Bulk WHOIS Lookup (`POST /v2.0/bulkwhois/live`)
- [`WhoisHistory.cs`](WhoisHistory.cs): Historical WHOIS records for a domain (`GET /v2.0/whois/history`)
- [`WhoisReverse.cs`](WhoisReverse.cs): Reverse WHOIS lookup by keyword (`GET /v2.0/whois/reverse`)

## DNS
- [`DnsLive.cs`](DnsLive.cs): Live DNS Lookup (`GET /v2.0/dns/live`)
- [`DnsHistorical.cs`](DnsHistorical.cs): Historical DNS Lookup (`GET /v2.0/dns/historical`)
- [`DnsReverse.cs`](DnsReverse.cs): Reverse DNS Lookup (`GET /v2.1/dns/reverse`)
- [`DnsHistoricalV22.cs`](DnsHistoricalV22.cs): Historical DNS Lookup (v2.2) (`GET /v2.2/dns/historical`)
- [`DnsHistoricalV23.cs`](DnsHistoricalV23.cs): Historical DNS Lookup (v2.3) (`GET /v2.3/dns/historical`)
- [`DnsReverseV22.cs`](DnsReverseV22.cs): Reverse DNS Lookup (v2.2) (`GET /v2.2/dns/reverse`)
- [`DnsReverseV23.cs`](DnsReverseV23.cs): Reverse DNS Lookup (v2.3) (`GET /v2.3/dns/reverse`)
- [`DnsBulk.cs`](DnsBulk.cs): Bulk DNS Lookup (`POST /v2.0/dns/bulk/live`)

## Domain Availability
- [`DomainAvailabilityV2.cs`](DomainAvailabilityV2.cs): Domain Availability Check with Suggestions (`GET /v2.0/domain/availability`)
- [`BulkDomainAvailabilityV2.cs`](BulkDomainAvailabilityV2.cs): Bulk Domain Availability Check (`POST /v2.0/domain/availability`)

## Typosquatting
- [`Typosquatting.cs`](Typosquatting.cs): Typosquatting Lookup (`GET /v3.0/domain/typos`)

## SSL
- [`SslLookup.cs`](SslLookup.cs): SSL Certificate Lookup (`GET /v1.0/ssl/live`)

## Geolocation
- [`Geolocation.cs`](Geolocation.cs): IP Geolocation Lookup (`GET /v1.0/geolocation`)
- [`BulkGeolocation.cs`](BulkGeolocation.cs): Bulk IP Geolocation (`POST /v1.0/geolocation`)

## Subdomains
- [`Subdomains.cs`](Subdomains.cs): Subdomains Lookup (`GET /v1.0/subdomains`)

## IP Reputation
- [`IpReputation.cs`](IpReputation.cs): IP Reputation Lookup (`GET /v1.0/security`)
- [`BulkIpReputation.cs`](BulkIpReputation.cs): Bulk IP Reputation (`POST /v1.0/security`)
- [`IpReputationV2.cs`](IpReputationV2.cs): IP Reputation Lookup (v2.0) (`GET /v2.0/security`)
- [`BulkIpReputationV2.cs`](BulkIpReputationV2.cs): Bulk IP Reputation (v2.0) (`POST /v2.0/security`)

## Domain Reputation
- [`DomainReputation.cs`](DomainReputation.cs): Domain Reputation Lookup (`GET /v1/domain/security`)

## ASN WHOIS
- [`AsnWhois.cs`](AsnWhois.cs): ASN WHOIS Lookup (`GET /v2.0/asn-whois`)

## IP WHOIS
- [`IpWhois.cs`](IpWhois.cs): IP WHOIS Lookup (`GET /v1.0/ip-whois`)

## Account
- [`RotateApiKey.cs`](RotateApiKey.cs): Rotate API Key (`GET /v1.0/api-key/rotate`)
- [`AccountUsage.cs`](AccountUsage.cs): Account Usage (`GET /v1.0/whoisapi/usage`)
- [`DatabaseFileStatus.cs`](DatabaseFileStatus.cs): Database File Status (Public) (`GET /v3.4/status`)

## Databases - Newly Registered
- [`DbNewlyGtld.cs`](DbNewlyGtld.cs): Newly Registered gTLD (CSV) (`GET /v3.1/download/domainer/gtld`)
- [`DbNewlyCctld.cs`](DbNewlyCctld.cs): Newly Registered ccTLD (CSV) (`GET /v3.1/download/domainer/cctld`)
- [`DbNewlyGtldCleaned.cs`](DbNewlyGtldCleaned.cs): Newly Registered gTLD Cleaned WHOIS (CSV) (`GET /v3.1/download/domainer/gtld/cleaned`)
- [`DbNewlyCctldCleaned.cs`](DbNewlyCctldCleaned.cs): Newly Registered ccTLD Cleaned WHOIS (CSV) (`GET /v3.1/download/domainer/cctld/cleaned`)
- [`DbNewlyGtldJson.cs`](DbNewlyGtldJson.cs): Newly Registered gTLD (JSON) (`GET /v3.1/domains/newly/gtld`)
- [`DbNewlyCctldJson.cs`](DbNewlyCctldJson.cs): Newly Registered ccTLD (JSON) (`GET /v3.1/domains/newly/cctld`)
- [`DbNewlyDns.cs`](DbNewlyDns.cs): Newly Registered With DNS (`GET /v3.1/download/domainer/newly/dns`)

## Databases - Expiring & Dropped
- [`DbExpired.cs`](DbExpired.cs): Expiring Domains (`GET /v3.1/download/domainer/expired`)
- [`DbExpiredCleaned.cs`](DbExpiredCleaned.cs): Expiring Cleaned WHOIS (`GET /v3.1/download/domainer/expired/cleaned`)
- [`DbDropped.cs`](DbDropped.cs): Dropped Domains (`GET /v3.1/download/domainer/dropped`)
- [`DbDroppedJson.cs`](DbDroppedJson.cs): Dropped Domains (JSON) (`GET /v3.1/domains/dropped`)
- [`DbDroppedBacklinks.cs`](DbDroppedBacklinks.cs): Dropped With Backlinks (`GET /v3.3/download/domainer/dropped/backlinks`)

## Databases - WHOIS
- [`DbWhoisDaily.cs`](DbWhoisDaily.cs): WHOIS Database Daily (`GET /v3.3/download/dbupdate/daily/domains/whois`)
- [`DbWhoisWeekly.cs`](DbWhoisWeekly.cs): WHOIS Database Weekly (`GET /v3.3/download/dbupdate/weekly/domains/whois`)
- [`DbWhoisMonthly.cs`](DbWhoisMonthly.cs): WHOIS Database Monthly (`GET /v3.3/download/dbupdate/monthly/domains/whois`)

## Databases - DNS
- [`DbDnsDaily.cs`](DbDnsDaily.cs): DNS Database Daily (`GET /v3.2/download/dbupdate/daily/dns`)
- [`DbDnsWeekly.cs`](DbDnsWeekly.cs): DNS Database Weekly (`GET /v3.2/download/dbupdate/weekly/dns`)
- [`DbDnsMonthly.cs`](DbDnsMonthly.cs): DNS Database Monthly (`GET /v3.2/download/dbupdate/monthly/dns`)

## Databases - Subdomains
- [`DbSubdomainsDaily.cs`](DbSubdomainsDaily.cs): Subdomains Daily (`GET /v3.2/download/dbupdate/daily/subdomains`)
- [`DbSubdomainsWeekly.cs`](DbSubdomainsWeekly.cs): Subdomains Weekly (`GET /v3.2/download/dbupdate/weekly/subdomains`)
- [`DbSubdomainsMonthly.cs`](DbSubdomainsMonthly.cs): Subdomains Monthly (`GET /v3.2/download/dbupdate/monthly/subdomains`)

## Databases - IP Geolocation
- [`DbIpCountryStatus.cs`](DbIpCountryStatus.cs): IP to Country Snapshot Status (`GET /v3.3/status/snapshot/ip/country`)
- [`DbIpCountry.cs`](DbIpCountry.cs): IP to Country Snapshot (`GET /v3.3/download/snapshot/ip/country`)
- [`DbIpCityStatus.cs`](DbIpCityStatus.cs): IP to City Snapshot Status (`GET /v3.3/status/snapshot/ip/city`)
- [`DbIpCity.cs`](DbIpCity.cs): IP to City Snapshot (`GET /v3.3/download/snapshot/ip/city`)

## Databases - ASN WHOIS
- [`DbAsnWhois.cs`](DbAsnWhois.cs): ASN WHOIS Snapshot (`GET /v3.3/download/snapshot/asn/whois`)
- [`DbAsnWhoisStatus.cs`](DbAsnWhoisStatus.cs): ASN WHOIS Snapshot Status (`GET /v3.3/status/snapshot/asn/whois`)

## Databases - IP WHOIS
- [`DbIpWhois.cs`](DbIpWhois.cs): IP WHOIS Snapshot (`GET /v3.3/download/snapshot/ip/whois`)
- [`DbIpWhoisStatus.cs`](DbIpWhoisStatus.cs): IP WHOIS Snapshot Status (`GET /v3.3/status/snapshot/ip/whois`)

## Databases - IP Security
- [`DbIpSecurity.cs`](DbIpSecurity.cs): IP Security Snapshot (`GET /v3.3/download/snapshot/ip/security`)
- [`DbIpSecurityStatus.cs`](DbIpSecurityStatus.cs): IP Security Snapshot Status (`GET /v3.3/status/snapshot/ip/security`)

## Databases - Threat Feed
- [`DownloadThreatFeedPhishing.cs`](DownloadThreatFeedPhishing.cs): Download the daily phishing threat feed (CSV) (`GET /v3.4/download/threat-feed/phishing`)
- [`DownloadThreatFeedPhishingSample.cs`](DownloadThreatFeedPhishingSample.cs): Download a sample of the phishing threat feed (CSV) (`GET /v3.4/download/threat-feed/phishing/sample`)
- [`DownloadThreatFeedMalware.cs`](DownloadThreatFeedMalware.cs): Download the daily malware threat feed (CSV) (`GET /v3.4/download/threat-feed/malware`)
- [`DownloadThreatFeedMalwareSample.cs`](DownloadThreatFeedMalwareSample.cs): Download a sample of the malware threat feed (CSV) (`GET /v3.4/download/threat-feed/malware/sample`)
- [`DownloadThreatFeedSpam.cs`](DownloadThreatFeedSpam.cs): Download the daily spam threat feed (CSV) (`GET /v3.4/download/threat-feed/spam`)
- [`DownloadThreatFeedSpamSample.cs`](DownloadThreatFeedSpamSample.cs): Download a sample of the spam threat feed (CSV) (`GET /v3.4/download/threat-feed/spam/sample`)

## Databases - Streaming
- [`StreamThreatFeedPhishing.cs`](StreamThreatFeedPhishing.cs): Stream the daily phishing threat feed (CSV) (`GET /v3.4/stream/threat-feed/phishing`)
- [`StreamThreatFeedPhishingSample.cs`](StreamThreatFeedPhishingSample.cs): Stream a sample of the phishing threat feed (CSV) (`GET /v3.4/stream/threat-feed/phishing/sample`)
- [`StreamThreatFeedMalware.cs`](StreamThreatFeedMalware.cs): Stream the daily malware threat feed (CSV) (`GET /v3.4/stream/threat-feed/malware`)
- [`StreamThreatFeedMalwareSample.cs`](StreamThreatFeedMalwareSample.cs): Stream a sample of the malware threat feed (CSV) (`GET /v3.4/stream/threat-feed/malware/sample`)
- [`StreamThreatFeedSpam.cs`](StreamThreatFeedSpam.cs): Stream the daily spam threat feed (CSV) (`GET /v3.4/stream/threat-feed/spam`)
- [`StreamThreatFeedSpamSample.cs`](StreamThreatFeedSpamSample.cs): Stream a sample of the spam threat feed (CSV) (`GET /v3.4/stream/threat-feed/spam/sample`)
- [`StreamDomainerGtld.cs`](StreamDomainerGtld.cs): Stream newly registered gTLD domains (CSV) (`GET /v3.3/stream/domainer/gtld`)
- [`StreamDomainerGtldCleaned.cs`](StreamDomainerGtldCleaned.cs): Stream cleaned newly registered gTLD domains (CSV) (`GET /v3.3/stream/domainer/gtld/cleaned`)
- [`StreamDomainerGtldCleanedEmail.cs`](StreamDomainerGtldCleanedEmail.cs): Stream cleaned newly registered gTLD domains with an email (CSV) (`GET /v3.3/stream/domainer/gtld/cleaned/email`)
- [`StreamDomainerGtldCleanedPhone.cs`](StreamDomainerGtldCleanedPhone.cs): Stream cleaned newly registered gTLD domains with a phone (CSV) (`GET /v3.3/stream/domainer/gtld/cleaned/phone`)
- [`StreamDomainerCctld.cs`](StreamDomainerCctld.cs): Stream newly registered ccTLD domains (CSV) (`GET /v3.3/stream/domainer/cctld`)
- [`StreamDomainerCctldCleaned.cs`](StreamDomainerCctldCleaned.cs): Stream cleaned newly registered ccTLD domains (CSV) (`GET /v3.3/stream/domainer/cctld/cleaned`)
- [`StreamDomainerCctldCleanedEmail.cs`](StreamDomainerCctldCleanedEmail.cs): Stream cleaned newly registered ccTLD domains with an email (CSV) (`GET /v3.3/stream/domainer/cctld/cleaned/email`)
- [`StreamDomainerCctldCleanedPhone.cs`](StreamDomainerCctldCleanedPhone.cs): Stream cleaned newly registered ccTLD domains with a phone (CSV) (`GET /v3.3/stream/domainer/cctld/cleaned/phone`)
- [`StreamDomainerExpired.cs`](StreamDomainerExpired.cs): Stream expiring domains (CSV) (`GET /v3.3/stream/domainer/expired`)
- [`StreamDomainerExpiredCleaned.cs`](StreamDomainerExpiredCleaned.cs): Stream cleaned expiring domains (CSV) (`GET /v3.3/stream/domainer/expired/cleaned`)
- [`StreamDomainerExpiredCleanedEmail.cs`](StreamDomainerExpiredCleanedEmail.cs): Stream cleaned expiring domains with an email (CSV) (`GET /v3.3/stream/domainer/expired/cleaned/email`)
- [`StreamDomainerExpiredCleanedPhone.cs`](StreamDomainerExpiredCleanedPhone.cs): Stream cleaned expiring domains with a phone (CSV) (`GET /v3.3/stream/domainer/expired/cleaned/phone`)
- [`StreamDomainerDropped.cs`](StreamDomainerDropped.cs): Stream dropped domains (CSV) (`GET /v3.3/stream/domainer/dropped`)
- [`StreamDomainerDroppedBacklinks.cs`](StreamDomainerDroppedBacklinks.cs): Stream dropped domains with backlinks (CSV) (`GET /v3.3/stream/domainer/dropped/backlinks`)
- [`StreamDomainerGtldSample.cs`](StreamDomainerGtldSample.cs): Stream a sample of newly registered gTLD domains (CSV) (`GET /v3.3/stream/domainer/sample/gtld`)
- [`StreamDomainerGtldCleanedSample.cs`](StreamDomainerGtldCleanedSample.cs): Stream a sample of cleaned newly registered gTLD domains (CSV) (`GET /v3.3/stream/domainer/sample/gtld/cleaned`)
- [`StreamDomainerCctldSample.cs`](StreamDomainerCctldSample.cs): Stream a sample of newly registered ccTLD domains (CSV) (`GET /v3.3/stream/domainer/sample/cctld`)
- [`StreamDomainerCctldCleanedSample.cs`](StreamDomainerCctldCleanedSample.cs): Stream a sample of cleaned newly registered ccTLD domains (CSV) (`GET /v3.3/stream/domainer/sample/cctld/cleaned`)
- [`StreamDomainerExpiredSample.cs`](StreamDomainerExpiredSample.cs): Stream a sample of expiring domains (CSV) (`GET /v3.3/stream/domainer/sample/expired`)
- [`StreamDomainerExpiredCleanedSample.cs`](StreamDomainerExpiredCleanedSample.cs): Stream a sample of cleaned expiring domains (CSV) (`GET /v3.3/stream/domainer/sample/expired/cleaned`)
- [`StreamDomainerDroppedSample.cs`](StreamDomainerDroppedSample.cs): Stream a sample of dropped domains (CSV) (`GET /v3.3/stream/domainer/sample/dropped`)
- [`StreamDomainerDroppedBacklinksSample.cs`](StreamDomainerDroppedBacklinksSample.cs): Stream a sample of dropped domains with backlinks (CSV) (`GET /v3.3/stream/domainer/sample/dropped/backlinks`)
