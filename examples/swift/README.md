# Swift Runnable Examples

Install: see the [Swift guide](../../docs/languages/swift.md). Set the `WHOISFREAKS_API_KEY` environment variable and run any file below.

## WHOIS
- [`WhoisLive.swift`](WhoisLive.swift): Live WHOIS Lookup (`GET /v2.0/whois/live`)
- [`BulkWhois.swift`](BulkWhois.swift): Bulk WHOIS Lookup (`POST /v2.0/bulkwhois/live`)
- [`WhoisHistory.swift`](WhoisHistory.swift): Historical WHOIS records for a domain (`GET /v2.0/whois/history`)
- [`WhoisReverse.swift`](WhoisReverse.swift): Reverse WHOIS lookup by keyword (`GET /v2.0/whois/reverse`)

## DNS
- [`DnsLive.swift`](DnsLive.swift): Live DNS Lookup (`GET /v2.0/dns/live`)
- [`DnsHistorical.swift`](DnsHistorical.swift): Historical DNS Lookup (`GET /v2.0/dns/historical`)
- [`DnsReverse.swift`](DnsReverse.swift): Reverse DNS Lookup (`GET /v2.1/dns/reverse`)
- [`DnsHistoricalV22.swift`](DnsHistoricalV22.swift): Historical DNS Lookup (v2.2) (`GET /v2.2/dns/historical`)
- [`DnsHistoricalV23.swift`](DnsHistoricalV23.swift): Historical DNS Lookup (v2.3) (`GET /v2.3/dns/historical`)
- [`DnsReverseV22.swift`](DnsReverseV22.swift): Reverse DNS Lookup (v2.2) (`GET /v2.2/dns/reverse`)
- [`DnsReverseV23.swift`](DnsReverseV23.swift): Reverse DNS Lookup (v2.3) (`GET /v2.3/dns/reverse`)
- [`DnsBulk.swift`](DnsBulk.swift): Bulk DNS Lookup (`POST /v2.0/dns/bulk/live`)

## Domain Availability
- [`DomainAvailabilityV2.swift`](DomainAvailabilityV2.swift): Domain Availability Check with Suggestions (`GET /v2.0/domain/availability`)
- [`BulkDomainAvailabilityV2.swift`](BulkDomainAvailabilityV2.swift): Bulk Domain Availability Check (`POST /v2.0/domain/availability`)

## Typosquatting
- [`Typosquatting.swift`](Typosquatting.swift): Typosquatting Lookup (`GET /v3.0/domain/typos`)
- [`SubdomainTyposquatting.swift`](SubdomainTyposquatting.swift): Subdomain Typosquatting Lookup (`GET /v3.0/subdomains/typos`)

## SSL
- [`SslLookup.swift`](SslLookup.swift): SSL Certificate Lookup (`GET /v1.0/ssl/live`)

## Geolocation
- [`Geolocation.swift`](Geolocation.swift): IP Geolocation Lookup (`GET /v1.0/geolocation`)
- [`BulkGeolocation.swift`](BulkGeolocation.swift): Bulk IP Geolocation (`POST /v1.0/geolocation`)

## Subdomains
- [`Subdomains.swift`](Subdomains.swift): Subdomains Lookup (`GET /v1.0/subdomains`)

## IP Reputation
- [`IpReputation.swift`](IpReputation.swift): IP Reputation Lookup (`GET /v1.0/security`)
- [`BulkIpReputation.swift`](BulkIpReputation.swift): Bulk IP Reputation (`POST /v1.0/security`)
- [`IpReputationV2.swift`](IpReputationV2.swift): IP Reputation Lookup (v2.0) (`GET /v2.0/security`)
- [`BulkIpReputationV2.swift`](BulkIpReputationV2.swift): Bulk IP Reputation (v2.0) (`POST /v2.0/security`)

## Domain Reputation
- [`DomainReputation.swift`](DomainReputation.swift): Domain Reputation Lookup (`GET /v1/domain/security`)

## ASN WHOIS
- [`AsnWhois.swift`](AsnWhois.swift): ASN WHOIS Lookup (`GET /v2.0/asn-whois`)

## IP WHOIS
- [`IpWhois.swift`](IpWhois.swift): IP WHOIS Lookup (`GET /v1.0/ip-whois`)

## Account
- [`RotateApiKey.swift`](RotateApiKey.swift): Rotate API Key (`GET /v1.0/api-key/rotate`)
- [`AccountUsage.swift`](AccountUsage.swift): Account Usage (`GET /v1.0/whoisapi/usage`)
- [`DatabaseFileStatus.swift`](DatabaseFileStatus.swift): Database File Status (Public) (`GET /v3.4/status`)

## Databases - Newly Registered
- [`DbNewlyGtld.swift`](DbNewlyGtld.swift): Newly Registered gTLD (CSV) (`GET /v3.1/download/domainer/gtld`)
- [`DbNewlyCctld.swift`](DbNewlyCctld.swift): Newly Registered ccTLD (CSV) (`GET /v3.1/download/domainer/cctld`)
- [`DbNewlyGtldCleaned.swift`](DbNewlyGtldCleaned.swift): Newly Registered gTLD Cleaned WHOIS (CSV) (`GET /v3.1/download/domainer/gtld/cleaned`)
- [`DbNewlyCctldCleaned.swift`](DbNewlyCctldCleaned.swift): Newly Registered ccTLD Cleaned WHOIS (CSV) (`GET /v3.1/download/domainer/cctld/cleaned`)
- [`DbNewlyGtldJson.swift`](DbNewlyGtldJson.swift): Newly Registered gTLD (JSON) (`GET /v3.1/domains/newly/gtld`)
- [`DbNewlyCctldJson.swift`](DbNewlyCctldJson.swift): Newly Registered ccTLD (JSON) (`GET /v3.1/domains/newly/cctld`)
- [`DbNewlyDns.swift`](DbNewlyDns.swift): Newly Registered With DNS (`GET /v3.1/download/domainer/newly/dns`)

## Databases - Expiring & Dropped
- [`DbExpired.swift`](DbExpired.swift): Expiring Domains (`GET /v3.1/download/domainer/expired`)
- [`DbExpiredCleaned.swift`](DbExpiredCleaned.swift): Expiring Cleaned WHOIS (`GET /v3.1/download/domainer/expired/cleaned`)
- [`DbDropped.swift`](DbDropped.swift): Dropped Domains (`GET /v3.1/download/domainer/dropped`)
- [`DbDroppedJson.swift`](DbDroppedJson.swift): Dropped Domains (JSON) (`GET /v3.1/domains/dropped`)
- [`DbDroppedBacklinks.swift`](DbDroppedBacklinks.swift): Dropped With Backlinks (`GET /v3.3/download/domainer/dropped/backlinks`)

## Databases - WHOIS
- [`DbWhoisDaily.swift`](DbWhoisDaily.swift): WHOIS Database Daily (`GET /v3.3/download/dbupdate/daily/domains/whois`)
- [`DbWhoisWeekly.swift`](DbWhoisWeekly.swift): WHOIS Database Weekly (`GET /v3.3/download/dbupdate/weekly/domains/whois`)
- [`DbWhoisMonthly.swift`](DbWhoisMonthly.swift): WHOIS Database Monthly (`GET /v3.3/download/dbupdate/monthly/domains/whois`)

## Databases - DNS
- [`DbDnsDaily.swift`](DbDnsDaily.swift): DNS Database Daily (`GET /v3.2/download/dbupdate/daily/dns`)
- [`DbDnsWeekly.swift`](DbDnsWeekly.swift): DNS Database Weekly (`GET /v3.2/download/dbupdate/weekly/dns`)
- [`DbDnsMonthly.swift`](DbDnsMonthly.swift): DNS Database Monthly (`GET /v3.2/download/dbupdate/monthly/dns`)

## Databases - Subdomains
- [`DbSubdomainsDaily.swift`](DbSubdomainsDaily.swift): Subdomains Daily (`GET /v3.2/download/dbupdate/daily/subdomains`)
- [`DbSubdomainsWeekly.swift`](DbSubdomainsWeekly.swift): Subdomains Weekly (`GET /v3.2/download/dbupdate/weekly/subdomains`)
- [`DbSubdomainsMonthly.swift`](DbSubdomainsMonthly.swift): Subdomains Monthly (`GET /v3.2/download/dbupdate/monthly/subdomains`)

## Databases - IP Geolocation
- [`DbIpCountryStatus.swift`](DbIpCountryStatus.swift): IP to Country Snapshot Status (`GET /v3.3/status/snapshot/ip/country`)
- [`DbIpCountry.swift`](DbIpCountry.swift): IP to Country Snapshot (`GET /v3.3/download/snapshot/ip/country`)
- [`DbIpCityStatus.swift`](DbIpCityStatus.swift): IP to City Snapshot Status (`GET /v3.3/status/snapshot/ip/city`)
- [`DbIpCity.swift`](DbIpCity.swift): IP to City Snapshot (`GET /v3.3/download/snapshot/ip/city`)

## Databases - ASN WHOIS
- [`DbAsnWhois.swift`](DbAsnWhois.swift): ASN WHOIS Snapshot (`GET /v3.3/download/snapshot/asn/whois`)
- [`DbAsnWhoisStatus.swift`](DbAsnWhoisStatus.swift): ASN WHOIS Snapshot Status (`GET /v3.3/status/snapshot/asn/whois`)

## Databases - IP WHOIS
- [`DbIpWhois.swift`](DbIpWhois.swift): IP WHOIS Snapshot (`GET /v3.3/download/snapshot/ip/whois`)
- [`DbIpWhoisStatus.swift`](DbIpWhoisStatus.swift): IP WHOIS Snapshot Status (`GET /v3.3/status/snapshot/ip/whois`)

## Databases - IP Security
- [`DbIpSecurity.swift`](DbIpSecurity.swift): IP Security Snapshot (`GET /v3.3/download/snapshot/ip/security`)
- [`DbIpSecurityStatus.swift`](DbIpSecurityStatus.swift): IP Security Snapshot Status (`GET /v3.3/status/snapshot/ip/security`)

## Databases - Threat Feed
- [`DownloadThreatFeedPhishing.swift`](DownloadThreatFeedPhishing.swift): Download the daily phishing threat feed (CSV) (`GET /v3.4/download/threat-feed/phishing`)
- [`DownloadThreatFeedPhishingSample.swift`](DownloadThreatFeedPhishingSample.swift): Download a sample of the phishing threat feed (CSV) (`GET /v3.4/download/threat-feed/phishing/sample`)
- [`DownloadThreatFeedMalware.swift`](DownloadThreatFeedMalware.swift): Download the daily malware threat feed (CSV) (`GET /v3.4/download/threat-feed/malware`)
- [`DownloadThreatFeedMalwareSample.swift`](DownloadThreatFeedMalwareSample.swift): Download a sample of the malware threat feed (CSV) (`GET /v3.4/download/threat-feed/malware/sample`)
- [`DownloadThreatFeedSpam.swift`](DownloadThreatFeedSpam.swift): Download the daily spam threat feed (CSV) (`GET /v3.4/download/threat-feed/spam`)
- [`DownloadThreatFeedSpamSample.swift`](DownloadThreatFeedSpamSample.swift): Download a sample of the spam threat feed (CSV) (`GET /v3.4/download/threat-feed/spam/sample`)

## Databases - Streaming
- [`StreamThreatFeedPhishing.swift`](StreamThreatFeedPhishing.swift): Stream the daily phishing threat feed (CSV) (`GET /v3.4/stream/threat-feed/phishing`)
- [`StreamThreatFeedPhishingSample.swift`](StreamThreatFeedPhishingSample.swift): Stream a sample of the phishing threat feed (CSV) (`GET /v3.4/stream/threat-feed/phishing/sample`)
- [`StreamThreatFeedMalware.swift`](StreamThreatFeedMalware.swift): Stream the daily malware threat feed (CSV) (`GET /v3.4/stream/threat-feed/malware`)
- [`StreamThreatFeedMalwareSample.swift`](StreamThreatFeedMalwareSample.swift): Stream a sample of the malware threat feed (CSV) (`GET /v3.4/stream/threat-feed/malware/sample`)
- [`StreamThreatFeedSpam.swift`](StreamThreatFeedSpam.swift): Stream the daily spam threat feed (CSV) (`GET /v3.4/stream/threat-feed/spam`)
- [`StreamThreatFeedSpamSample.swift`](StreamThreatFeedSpamSample.swift): Stream a sample of the spam threat feed (CSV) (`GET /v3.4/stream/threat-feed/spam/sample`)
- [`StreamDomainerGtld.swift`](StreamDomainerGtld.swift): Stream newly registered gTLD domains (CSV) (`GET /v3.3/stream/domainer/gtld`)
- [`StreamDomainerGtldCleaned.swift`](StreamDomainerGtldCleaned.swift): Stream cleaned newly registered gTLD domains (CSV) (`GET /v3.3/stream/domainer/gtld/cleaned`)
- [`StreamDomainerGtldCleanedEmail.swift`](StreamDomainerGtldCleanedEmail.swift): Stream cleaned newly registered gTLD domains with an email (CSV) (`GET /v3.3/stream/domainer/gtld/cleaned/email`)
- [`StreamDomainerGtldCleanedPhone.swift`](StreamDomainerGtldCleanedPhone.swift): Stream cleaned newly registered gTLD domains with a phone (CSV) (`GET /v3.3/stream/domainer/gtld/cleaned/phone`)
- [`StreamDomainerCctld.swift`](StreamDomainerCctld.swift): Stream newly registered ccTLD domains (CSV) (`GET /v3.3/stream/domainer/cctld`)
- [`StreamDomainerCctldCleaned.swift`](StreamDomainerCctldCleaned.swift): Stream cleaned newly registered ccTLD domains (CSV) (`GET /v3.3/stream/domainer/cctld/cleaned`)
- [`StreamDomainerCctldCleanedEmail.swift`](StreamDomainerCctldCleanedEmail.swift): Stream cleaned newly registered ccTLD domains with an email (CSV) (`GET /v3.3/stream/domainer/cctld/cleaned/email`)
- [`StreamDomainerCctldCleanedPhone.swift`](StreamDomainerCctldCleanedPhone.swift): Stream cleaned newly registered ccTLD domains with a phone (CSV) (`GET /v3.3/stream/domainer/cctld/cleaned/phone`)
- [`StreamDomainerExpired.swift`](StreamDomainerExpired.swift): Stream expiring domains (CSV) (`GET /v3.3/stream/domainer/expired`)
- [`StreamDomainerExpiredCleaned.swift`](StreamDomainerExpiredCleaned.swift): Stream cleaned expiring domains (CSV) (`GET /v3.3/stream/domainer/expired/cleaned`)
- [`StreamDomainerExpiredCleanedEmail.swift`](StreamDomainerExpiredCleanedEmail.swift): Stream cleaned expiring domains with an email (CSV) (`GET /v3.3/stream/domainer/expired/cleaned/email`)
- [`StreamDomainerExpiredCleanedPhone.swift`](StreamDomainerExpiredCleanedPhone.swift): Stream cleaned expiring domains with a phone (CSV) (`GET /v3.3/stream/domainer/expired/cleaned/phone`)
- [`StreamDomainerDropped.swift`](StreamDomainerDropped.swift): Stream dropped domains (CSV) (`GET /v3.3/stream/domainer/dropped`)
- [`StreamDomainerDroppedBacklinks.swift`](StreamDomainerDroppedBacklinks.swift): Stream dropped domains with backlinks (CSV) (`GET /v3.3/stream/domainer/dropped/backlinks`)
- [`StreamDomainerGtldSample.swift`](StreamDomainerGtldSample.swift): Stream a sample of newly registered gTLD domains (CSV) (`GET /v3.3/stream/domainer/sample/gtld`)
- [`StreamDomainerGtldCleanedSample.swift`](StreamDomainerGtldCleanedSample.swift): Stream a sample of cleaned newly registered gTLD domains (CSV) (`GET /v3.3/stream/domainer/sample/gtld/cleaned`)
- [`StreamDomainerCctldSample.swift`](StreamDomainerCctldSample.swift): Stream a sample of newly registered ccTLD domains (CSV) (`GET /v3.3/stream/domainer/sample/cctld`)
- [`StreamDomainerCctldCleanedSample.swift`](StreamDomainerCctldCleanedSample.swift): Stream a sample of cleaned newly registered ccTLD domains (CSV) (`GET /v3.3/stream/domainer/sample/cctld/cleaned`)
- [`StreamDomainerExpiredSample.swift`](StreamDomainerExpiredSample.swift): Stream a sample of expiring domains (CSV) (`GET /v3.3/stream/domainer/sample/expired`)
- [`StreamDomainerExpiredCleanedSample.swift`](StreamDomainerExpiredCleanedSample.swift): Stream a sample of cleaned expiring domains (CSV) (`GET /v3.3/stream/domainer/sample/expired/cleaned`)
- [`StreamDomainerDroppedSample.swift`](StreamDomainerDroppedSample.swift): Stream a sample of dropped domains (CSV) (`GET /v3.3/stream/domainer/sample/dropped`)
- [`StreamDomainerDroppedBacklinksSample.swift`](StreamDomainerDroppedBacklinksSample.swift): Stream a sample of dropped domains with backlinks (CSV) (`GET /v3.3/stream/domainer/sample/dropped/backlinks`)
