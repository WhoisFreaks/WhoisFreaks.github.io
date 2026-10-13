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
- [`DnsBulk.swift`](DnsBulk.swift): Bulk DNS Lookup (`POST /v2.0/dns/bulk/live`)

## Domain Availability
- [`DomainAvailabilityV2.swift`](DomainAvailabilityV2.swift): Domain Availability Check with Suggestions (`GET /v2.0/domain/availability`)
- [`BulkDomainAvailabilityV2.swift`](BulkDomainAvailabilityV2.swift): Bulk Domain Availability Check (`POST /v2.0/domain/availability`)

## Typosquatting
- [`Typosquatting.swift`](Typosquatting.swift): Typosquatting Lookup (`GET /v3.0/domain/typos`)

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
