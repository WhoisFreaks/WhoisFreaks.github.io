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
