# Kotlin Runnable Examples

Install: see the [Kotlin guide](../../docs/languages/kotlin.md). Set the `WHOISFREAKS_API_KEY` environment variable and run any file below.

## WHOIS
- [`WhoisLive.kt`](WhoisLive.kt): Live WHOIS Lookup (`GET /v2.0/whois/live`)
- [`BulkWhois.kt`](BulkWhois.kt): Bulk WHOIS Lookup (`POST /v2.0/bulkwhois/live`)
- [`WhoisHistory.kt`](WhoisHistory.kt): Historical WHOIS records for a domain (`GET /v2.0/whois/history`)
- [`WhoisReverse.kt`](WhoisReverse.kt): Reverse WHOIS lookup by keyword (`GET /v2.0/whois/reverse`)

## DNS
- [`DnsLive.kt`](DnsLive.kt): Live DNS Lookup (`GET /v2.0/dns/live`)
- [`DnsHistorical.kt`](DnsHistorical.kt): Historical DNS Lookup (`GET /v2.0/dns/historical`)
- [`DnsReverse.kt`](DnsReverse.kt): Reverse DNS Lookup (`GET /v2.1/dns/reverse`)
- [`DnsBulk.kt`](DnsBulk.kt): Bulk DNS Lookup (`POST /v2.0/dns/bulk/live`)

## Domain Availability
- [`DomainAvailabilityV2.kt`](DomainAvailabilityV2.kt): Domain Availability Check with Suggestions (`GET /v2.0/domain/availability`)
- [`BulkDomainAvailabilityV2.kt`](BulkDomainAvailabilityV2.kt): Bulk Domain Availability Check (`POST /v2.0/domain/availability`)

## Typosquatting
- [`Typosquatting.kt`](Typosquatting.kt): Typosquatting Lookup (`GET /v3.0/domain/typos`)

## SSL
- [`SslLookup.kt`](SslLookup.kt): SSL Certificate Lookup (`GET /v1.0/ssl/live`)

## Geolocation
- [`Geolocation.kt`](Geolocation.kt): IP Geolocation Lookup (`GET /v1.0/geolocation`)
- [`BulkGeolocation.kt`](BulkGeolocation.kt): Bulk IP Geolocation (`POST /v1.0/geolocation`)

## Subdomains
- [`Subdomains.kt`](Subdomains.kt): Subdomains Lookup (`GET /v1.0/subdomains`)

## IP Reputation
- [`IpReputation.kt`](IpReputation.kt): IP Reputation Lookup (`GET /v1.0/security`)
- [`BulkIpReputation.kt`](BulkIpReputation.kt): Bulk IP Reputation (`POST /v1.0/security`)

## Domain Reputation
- [`DomainReputation.kt`](DomainReputation.kt): Domain Reputation Lookup (`GET /v1/domain/security`)

## ASN WHOIS
- [`AsnWhois.kt`](AsnWhois.kt): ASN WHOIS Lookup (`GET /v2.0/asn-whois`)

## IP WHOIS
- [`IpWhois.kt`](IpWhois.kt): IP WHOIS Lookup (`GET /v1.0/ip-whois`)

## Account
- [`RotateApiKey.kt`](RotateApiKey.kt): Rotate API Key (`GET /v1.0/api-key/rotate`)
- [`AccountUsage.kt`](AccountUsage.kt): Account Usage (`GET /v1.0/whoisapi/usage`)
- [`DatabaseFileStatus.kt`](DatabaseFileStatus.kt): Database File Status (Public) (`GET /v3.4/status`)

## Databases - Newly Registered
- [`DbNewlyGtld.kt`](DbNewlyGtld.kt): Newly Registered gTLD (CSV) (`GET /v3.1/download/domainer/gtld`)
- [`DbNewlyCctld.kt`](DbNewlyCctld.kt): Newly Registered ccTLD (CSV) (`GET /v3.1/download/domainer/cctld`)
- [`DbNewlyGtldCleaned.kt`](DbNewlyGtldCleaned.kt): Newly Registered gTLD Cleaned WHOIS (CSV) (`GET /v3.1/download/domainer/gtld/cleaned`)
- [`DbNewlyCctldCleaned.kt`](DbNewlyCctldCleaned.kt): Newly Registered ccTLD Cleaned WHOIS (CSV) (`GET /v3.1/download/domainer/cctld/cleaned`)
- [`DbNewlyGtldJson.kt`](DbNewlyGtldJson.kt): Newly Registered gTLD (JSON) (`GET /v3.1/domains/newly/gtld`)
- [`DbNewlyCctldJson.kt`](DbNewlyCctldJson.kt): Newly Registered ccTLD (JSON) (`GET /v3.1/domains/newly/cctld`)
- [`DbNewlyDns.kt`](DbNewlyDns.kt): Newly Registered With DNS (`GET /v3.1/download/domainer/newly/dns`)

## Databases - Expiring & Dropped
- [`DbExpired.kt`](DbExpired.kt): Expiring Domains (`GET /v3.1/download/domainer/expired`)
- [`DbExpiredCleaned.kt`](DbExpiredCleaned.kt): Expiring Cleaned WHOIS (`GET /v3.1/download/domainer/expired/cleaned`)
- [`DbDropped.kt`](DbDropped.kt): Dropped Domains (`GET /v3.1/download/domainer/dropped`)
- [`DbDroppedJson.kt`](DbDroppedJson.kt): Dropped Domains (JSON) (`GET /v3.1/domains/dropped`)
- [`DbDroppedBacklinks.kt`](DbDroppedBacklinks.kt): Dropped With Backlinks (`GET /v3.3/download/domainer/dropped/backlinks`)

## Databases - WHOIS
- [`DbWhoisDaily.kt`](DbWhoisDaily.kt): WHOIS Database Daily (`GET /v3.3/download/dbupdate/daily/domains/whois`)
- [`DbWhoisWeekly.kt`](DbWhoisWeekly.kt): WHOIS Database Weekly (`GET /v3.3/download/dbupdate/weekly/domains/whois`)
- [`DbWhoisMonthly.kt`](DbWhoisMonthly.kt): WHOIS Database Monthly (`GET /v3.3/download/dbupdate/monthly/domains/whois`)

## Databases - DNS
- [`DbDnsDaily.kt`](DbDnsDaily.kt): DNS Database Daily (`GET /v3.2/download/dbupdate/daily/dns`)
- [`DbDnsWeekly.kt`](DbDnsWeekly.kt): DNS Database Weekly (`GET /v3.2/download/dbupdate/weekly/dns`)
- [`DbDnsMonthly.kt`](DbDnsMonthly.kt): DNS Database Monthly (`GET /v3.2/download/dbupdate/monthly/dns`)

## Databases - Subdomains
- [`DbSubdomainsDaily.kt`](DbSubdomainsDaily.kt): Subdomains Daily (`GET /v3.2/download/dbupdate/daily/subdomains`)
- [`DbSubdomainsWeekly.kt`](DbSubdomainsWeekly.kt): Subdomains Weekly (`GET /v3.2/download/dbupdate/weekly/subdomains`)
- [`DbSubdomainsMonthly.kt`](DbSubdomainsMonthly.kt): Subdomains Monthly (`GET /v3.2/download/dbupdate/monthly/subdomains`)

## Databases - IP Geolocation
- [`DbIpCountryStatus.kt`](DbIpCountryStatus.kt): IP to Country Snapshot Status (`GET /v3.3/status/snapshot/ip/country`)
- [`DbIpCountry.kt`](DbIpCountry.kt): IP to Country Snapshot (`GET /v3.3/download/snapshot/ip/country`)
- [`DbIpCityStatus.kt`](DbIpCityStatus.kt): IP to City Snapshot Status (`GET /v3.3/status/snapshot/ip/city`)
- [`DbIpCity.kt`](DbIpCity.kt): IP to City Snapshot (`GET /v3.3/download/snapshot/ip/city`)

## Databases - ASN WHOIS
- [`DbAsnWhois.kt`](DbAsnWhois.kt): ASN WHOIS Snapshot (`GET /v3.3/download/snapshot/asn/whois`)
- [`DbAsnWhoisStatus.kt`](DbAsnWhoisStatus.kt): ASN WHOIS Snapshot Status (`GET /v3.3/status/snapshot/asn/whois`)

## Databases - IP WHOIS
- [`DbIpWhois.kt`](DbIpWhois.kt): IP WHOIS Snapshot (`GET /v3.3/download/snapshot/ip/whois`)
- [`DbIpWhoisStatus.kt`](DbIpWhoisStatus.kt): IP WHOIS Snapshot Status (`GET /v3.3/status/snapshot/ip/whois`)

## Databases - IP Security
- [`DbIpSecurity.kt`](DbIpSecurity.kt): IP Security Snapshot (`GET /v3.3/download/snapshot/ip/security`)
- [`DbIpSecurityStatus.kt`](DbIpSecurityStatus.kt): IP Security Snapshot Status (`GET /v3.3/status/snapshot/ip/security`)

## Databases - Threat Feed
- [`DownloadThreatFeedPhishing.kt`](DownloadThreatFeedPhishing.kt): Download the daily phishing threat feed (CSV) (`GET /v3.4/download/threat-feed/phishing`)
- [`DownloadThreatFeedPhishingSample.kt`](DownloadThreatFeedPhishingSample.kt): Download a sample of the phishing threat feed (CSV) (`GET /v3.4/download/threat-feed/phishing/sample`)
- [`DownloadThreatFeedMalware.kt`](DownloadThreatFeedMalware.kt): Download the daily malware threat feed (CSV) (`GET /v3.4/download/threat-feed/malware`)
- [`DownloadThreatFeedMalwareSample.kt`](DownloadThreatFeedMalwareSample.kt): Download a sample of the malware threat feed (CSV) (`GET /v3.4/download/threat-feed/malware/sample`)
- [`DownloadThreatFeedSpam.kt`](DownloadThreatFeedSpam.kt): Download the daily spam threat feed (CSV) (`GET /v3.4/download/threat-feed/spam`)
- [`DownloadThreatFeedSpamSample.kt`](DownloadThreatFeedSpamSample.kt): Download a sample of the spam threat feed (CSV) (`GET /v3.4/download/threat-feed/spam/sample`)
