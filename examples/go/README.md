# Go Runnable Examples

Install: see the [Go guide](../../docs/languages/go.md). Set the `WHOISFREAKS_API_KEY` environment variable and run any file below.

## WHOIS
- [`WhoisLive.go`](WhoisLive.go): Live WHOIS Lookup (`GET /v2.0/whois/live`)
- [`BulkWhois.go`](BulkWhois.go): Bulk WHOIS Lookup (`POST /v2.0/bulkwhois/live`)
- [`WhoisHistory.go`](WhoisHistory.go): Historical WHOIS records for a domain (`GET /v2.0/whois/history`)
- [`WhoisReverse.go`](WhoisReverse.go): Reverse WHOIS lookup by keyword (`GET /v2.0/whois/reverse`)

## DNS
- [`DnsLive.go`](DnsLive.go): Live DNS Lookup (`GET /v2.0/dns/live`)
- [`DnsHistorical.go`](DnsHistorical.go): Historical DNS Lookup (`GET /v2.0/dns/historical`)
- [`DnsReverse.go`](DnsReverse.go): Reverse DNS Lookup (`GET /v2.1/dns/reverse`)
- [`DnsBulk.go`](DnsBulk.go): Bulk DNS Lookup (`POST /v2.0/dns/bulk/live`)

## Domain Availability
- [`DomainAvailabilityV2.go`](DomainAvailabilityV2.go): Domain Availability Check with Suggestions (`GET /v2.0/domain/availability`)
- [`BulkDomainAvailabilityV2.go`](BulkDomainAvailabilityV2.go): Bulk Domain Availability Check (`POST /v2.0/domain/availability`)

## Typosquatting
- [`Typosquatting.go`](Typosquatting.go): Typosquatting Lookup (`GET /v3.0/domain/typos`)

## SSL
- [`SslLookup.go`](SslLookup.go): SSL Certificate Lookup (`GET /v1.0/ssl/live`)

## Geolocation
- [`Geolocation.go`](Geolocation.go): IP Geolocation Lookup (`GET /v1.0/geolocation`)
- [`BulkGeolocation.go`](BulkGeolocation.go): Bulk IP Geolocation (`POST /v1.0/geolocation`)

## Subdomains
- [`Subdomains.go`](Subdomains.go): Subdomains Lookup (`GET /v1.0/subdomains`)

## IP Reputation
- [`IpReputation.go`](IpReputation.go): IP Reputation Lookup (`GET /v1.0/security`)
- [`BulkIpReputation.go`](BulkIpReputation.go): Bulk IP Reputation (`POST /v1.0/security`)

## Domain Reputation
- [`DomainReputation.go`](DomainReputation.go): Domain Reputation Lookup (`GET /v1/domain/security`)

## ASN WHOIS
- [`AsnWhois.go`](AsnWhois.go): ASN WHOIS Lookup (`GET /v2.0/asn-whois`)

## IP WHOIS
- [`IpWhois.go`](IpWhois.go): IP WHOIS Lookup (`GET /v1.0/ip-whois`)

## Account
- [`RotateApiKey.go`](RotateApiKey.go): Rotate API Key (`GET /v1.0/api-key/rotate`)
- [`AccountUsage.go`](AccountUsage.go): Account Usage (`GET /v1.0/whoisapi/usage`)
- [`DatabaseFileStatus.go`](DatabaseFileStatus.go): Database File Status (Public) (`GET /v3.4/status`)

## Databases - Newly Registered
- [`DbNewlyGtld.go`](DbNewlyGtld.go): Newly Registered gTLD (CSV) (`GET /v3.1/download/domainer/gtld`)
- [`DbNewlyCctld.go`](DbNewlyCctld.go): Newly Registered ccTLD (CSV) (`GET /v3.1/download/domainer/cctld`)
- [`DbNewlyGtldCleaned.go`](DbNewlyGtldCleaned.go): Newly Registered gTLD Cleaned WHOIS (CSV) (`GET /v3.1/download/domainer/gtld/cleaned`)
- [`DbNewlyCctldCleaned.go`](DbNewlyCctldCleaned.go): Newly Registered ccTLD Cleaned WHOIS (CSV) (`GET /v3.1/download/domainer/cctld/cleaned`)
- [`DbNewlyGtldJson.go`](DbNewlyGtldJson.go): Newly Registered gTLD (JSON) (`GET /v3.1/domains/newly/gtld`)
- [`DbNewlyCctldJson.go`](DbNewlyCctldJson.go): Newly Registered ccTLD (JSON) (`GET /v3.1/domains/newly/cctld`)
- [`DbNewlyDns.go`](DbNewlyDns.go): Newly Registered With DNS (`GET /v3.1/download/domainer/newly/dns`)

## Databases - Expiring & Dropped
- [`DbExpired.go`](DbExpired.go): Expiring Domains (`GET /v3.1/download/domainer/expired`)
- [`DbExpiredCleaned.go`](DbExpiredCleaned.go): Expiring Cleaned WHOIS (`GET /v3.1/download/domainer/expired/cleaned`)
- [`DbDropped.go`](DbDropped.go): Dropped Domains (`GET /v3.1/download/domainer/dropped`)
- [`DbDroppedJson.go`](DbDroppedJson.go): Dropped Domains (JSON) (`GET /v3.1/domains/dropped`)
- [`DbDroppedBacklinks.go`](DbDroppedBacklinks.go): Dropped With Backlinks (`GET /v3.3/download/domainer/dropped/backlinks`)

## Databases - WHOIS
- [`DbWhoisDaily.go`](DbWhoisDaily.go): WHOIS Database Daily (`GET /v3.3/download/dbupdate/daily/domains/whois`)
- [`DbWhoisWeekly.go`](DbWhoisWeekly.go): WHOIS Database Weekly (`GET /v3.3/download/dbupdate/weekly/domains/whois`)
- [`DbWhoisMonthly.go`](DbWhoisMonthly.go): WHOIS Database Monthly (`GET /v3.3/download/dbupdate/monthly/domains/whois`)

## Databases - DNS
- [`DbDnsDaily.go`](DbDnsDaily.go): DNS Database Daily (`GET /v3.2/download/dbupdate/daily/dns`)
- [`DbDnsWeekly.go`](DbDnsWeekly.go): DNS Database Weekly (`GET /v3.2/download/dbupdate/weekly/dns`)
- [`DbDnsMonthly.go`](DbDnsMonthly.go): DNS Database Monthly (`GET /v3.2/download/dbupdate/monthly/dns`)

## Databases - Subdomains
- [`DbSubdomainsDaily.go`](DbSubdomainsDaily.go): Subdomains Daily (`GET /v3.2/download/dbupdate/daily/subdomains`)
- [`DbSubdomainsWeekly.go`](DbSubdomainsWeekly.go): Subdomains Weekly (`GET /v3.2/download/dbupdate/weekly/subdomains`)
- [`DbSubdomainsMonthly.go`](DbSubdomainsMonthly.go): Subdomains Monthly (`GET /v3.2/download/dbupdate/monthly/subdomains`)

## Databases - IP Geolocation
- [`DbIpCountryStatus.go`](DbIpCountryStatus.go): IP to Country Snapshot Status (`GET /v3.3/status/snapshot/ip/country`)
- [`DbIpCountry.go`](DbIpCountry.go): IP to Country Snapshot (`GET /v3.3/download/snapshot/ip/country`)
- [`DbIpCityStatus.go`](DbIpCityStatus.go): IP to City Snapshot Status (`GET /v3.3/status/snapshot/ip/city`)
- [`DbIpCity.go`](DbIpCity.go): IP to City Snapshot (`GET /v3.3/download/snapshot/ip/city`)

## Databases - ASN WHOIS
- [`DbAsnWhois.go`](DbAsnWhois.go): ASN WHOIS Snapshot (`GET /v3.3/download/snapshot/asn/whois`)
- [`DbAsnWhoisStatus.go`](DbAsnWhoisStatus.go): ASN WHOIS Snapshot Status (`GET /v3.3/status/snapshot/asn/whois`)

## Databases - IP WHOIS
- [`DbIpWhois.go`](DbIpWhois.go): IP WHOIS Snapshot (`GET /v3.3/download/snapshot/ip/whois`)
- [`DbIpWhoisStatus.go`](DbIpWhoisStatus.go): IP WHOIS Snapshot Status (`GET /v3.3/status/snapshot/ip/whois`)

## Databases - IP Security
- [`DbIpSecurity.go`](DbIpSecurity.go): IP Security Snapshot (`GET /v3.3/download/snapshot/ip/security`)
- [`DbIpSecurityStatus.go`](DbIpSecurityStatus.go): IP Security Snapshot Status (`GET /v3.3/status/snapshot/ip/security`)

## Databases - Threat Feed
- [`DownloadThreatFeedPhishing.go`](DownloadThreatFeedPhishing.go): Download the daily phishing threat feed (CSV) (`GET /v3.4/download/threat-feed/phishing`)
- [`DownloadThreatFeedPhishingSample.go`](DownloadThreatFeedPhishingSample.go): Download a sample of the phishing threat feed (CSV) (`GET /v3.4/download/threat-feed/phishing/sample`)
- [`DownloadThreatFeedMalware.go`](DownloadThreatFeedMalware.go): Download the daily malware threat feed (CSV) (`GET /v3.4/download/threat-feed/malware`)
- [`DownloadThreatFeedMalwareSample.go`](DownloadThreatFeedMalwareSample.go): Download a sample of the malware threat feed (CSV) (`GET /v3.4/download/threat-feed/malware/sample`)
- [`DownloadThreatFeedSpam.go`](DownloadThreatFeedSpam.go): Download the daily spam threat feed (CSV) (`GET /v3.4/download/threat-feed/spam`)
- [`DownloadThreatFeedSpamSample.go`](DownloadThreatFeedSpamSample.go): Download a sample of the spam threat feed (CSV) (`GET /v3.4/download/threat-feed/spam/sample`)
