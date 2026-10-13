# TypeScript Runnable Examples

Install: see the [TypeScript guide](../../docs/languages/typescript.md). Set the `WHOISFREAKS_API_KEY` environment variable and run any file below.

## WHOIS
- [`WhoisLive.ts`](WhoisLive.ts): Live WHOIS Lookup (`GET /v2.0/whois/live`)
- [`BulkWhois.ts`](BulkWhois.ts): Bulk WHOIS Lookup (`POST /v2.0/bulkwhois/live`)
- [`WhoisHistory.ts`](WhoisHistory.ts): Historical WHOIS records for a domain (`GET /v2.0/whois/history`)
- [`WhoisReverse.ts`](WhoisReverse.ts): Reverse WHOIS lookup by keyword (`GET /v2.0/whois/reverse`)

## DNS
- [`DnsLive.ts`](DnsLive.ts): Live DNS Lookup (`GET /v2.0/dns/live`)
- [`DnsHistorical.ts`](DnsHistorical.ts): Historical DNS Lookup (`GET /v2.0/dns/historical`)
- [`DnsReverse.ts`](DnsReverse.ts): Reverse DNS Lookup (`GET /v2.1/dns/reverse`)
- [`DnsBulk.ts`](DnsBulk.ts): Bulk DNS Lookup (`POST /v2.0/dns/bulk/live`)

## Domain Availability
- [`DomainAvailabilityV2.ts`](DomainAvailabilityV2.ts): Domain Availability Check with Suggestions (`GET /v2.0/domain/availability`)
- [`BulkDomainAvailabilityV2.ts`](BulkDomainAvailabilityV2.ts): Bulk Domain Availability Check (`POST /v2.0/domain/availability`)

## Typosquatting
- [`Typosquatting.ts`](Typosquatting.ts): Typosquatting Lookup (`GET /v3.0/domain/typos`)

## SSL
- [`SslLookup.ts`](SslLookup.ts): SSL Certificate Lookup (`GET /v1.0/ssl/live`)

## Geolocation
- [`Geolocation.ts`](Geolocation.ts): IP Geolocation Lookup (`GET /v1.0/geolocation`)
- [`BulkGeolocation.ts`](BulkGeolocation.ts): Bulk IP Geolocation (`POST /v1.0/geolocation`)

## Subdomains
- [`Subdomains.ts`](Subdomains.ts): Subdomains Lookup (`GET /v1.0/subdomains`)

## IP Reputation
- [`IpReputation.ts`](IpReputation.ts): IP Reputation Lookup (`GET /v1.0/security`)
- [`BulkIpReputation.ts`](BulkIpReputation.ts): Bulk IP Reputation (`POST /v1.0/security`)

## Domain Reputation
- [`DomainReputation.ts`](DomainReputation.ts): Domain Reputation Lookup (`GET /v1/domain/security`)

## ASN WHOIS
- [`AsnWhois.ts`](AsnWhois.ts): ASN WHOIS Lookup (`GET /v2.0/asn-whois`)

## IP WHOIS
- [`IpWhois.ts`](IpWhois.ts): IP WHOIS Lookup (`GET /v1.0/ip-whois`)

## Account
- [`RotateApiKey.ts`](RotateApiKey.ts): Rotate API Key (`GET /v1.0/api-key/rotate`)
- [`AccountUsage.ts`](AccountUsage.ts): Account Usage (`GET /v1.0/whoisapi/usage`)
- [`DatabaseFileStatus.ts`](DatabaseFileStatus.ts): Database File Status (Public) (`GET /v3.4/status`)

## Databases - Newly Registered
- [`DbNewlyGtld.ts`](DbNewlyGtld.ts): Newly Registered gTLD (CSV) (`GET /v3.1/download/domainer/gtld`)
- [`DbNewlyCctld.ts`](DbNewlyCctld.ts): Newly Registered ccTLD (CSV) (`GET /v3.1/download/domainer/cctld`)
- [`DbNewlyGtldCleaned.ts`](DbNewlyGtldCleaned.ts): Newly Registered gTLD Cleaned WHOIS (CSV) (`GET /v3.1/download/domainer/gtld/cleaned`)
- [`DbNewlyCctldCleaned.ts`](DbNewlyCctldCleaned.ts): Newly Registered ccTLD Cleaned WHOIS (CSV) (`GET /v3.1/download/domainer/cctld/cleaned`)
- [`DbNewlyGtldJson.ts`](DbNewlyGtldJson.ts): Newly Registered gTLD (JSON) (`GET /v3.1/domains/newly/gtld`)
- [`DbNewlyCctldJson.ts`](DbNewlyCctldJson.ts): Newly Registered ccTLD (JSON) (`GET /v3.1/domains/newly/cctld`)
- [`DbNewlyDns.ts`](DbNewlyDns.ts): Newly Registered With DNS (`GET /v3.1/download/domainer/newly/dns`)

## Databases - Expiring & Dropped
- [`DbExpired.ts`](DbExpired.ts): Expiring Domains (`GET /v3.1/download/domainer/expired`)
- [`DbExpiredCleaned.ts`](DbExpiredCleaned.ts): Expiring Cleaned WHOIS (`GET /v3.1/download/domainer/expired/cleaned`)
- [`DbDropped.ts`](DbDropped.ts): Dropped Domains (`GET /v3.1/download/domainer/dropped`)
- [`DbDroppedJson.ts`](DbDroppedJson.ts): Dropped Domains (JSON) (`GET /v3.1/domains/dropped`)
- [`DbDroppedBacklinks.ts`](DbDroppedBacklinks.ts): Dropped With Backlinks (`GET /v3.3/download/domainer/dropped/backlinks`)

## Databases - WHOIS
- [`DbWhoisDaily.ts`](DbWhoisDaily.ts): WHOIS Database Daily (`GET /v3.3/download/dbupdate/daily/domains/whois`)
- [`DbWhoisWeekly.ts`](DbWhoisWeekly.ts): WHOIS Database Weekly (`GET /v3.3/download/dbupdate/weekly/domains/whois`)
- [`DbWhoisMonthly.ts`](DbWhoisMonthly.ts): WHOIS Database Monthly (`GET /v3.3/download/dbupdate/monthly/domains/whois`)

## Databases - DNS
- [`DbDnsDaily.ts`](DbDnsDaily.ts): DNS Database Daily (`GET /v3.2/download/dbupdate/daily/dns`)
- [`DbDnsWeekly.ts`](DbDnsWeekly.ts): DNS Database Weekly (`GET /v3.2/download/dbupdate/weekly/dns`)
- [`DbDnsMonthly.ts`](DbDnsMonthly.ts): DNS Database Monthly (`GET /v3.2/download/dbupdate/monthly/dns`)

## Databases - Subdomains
- [`DbSubdomainsDaily.ts`](DbSubdomainsDaily.ts): Subdomains Daily (`GET /v3.2/download/dbupdate/daily/subdomains`)
- [`DbSubdomainsWeekly.ts`](DbSubdomainsWeekly.ts): Subdomains Weekly (`GET /v3.2/download/dbupdate/weekly/subdomains`)
- [`DbSubdomainsMonthly.ts`](DbSubdomainsMonthly.ts): Subdomains Monthly (`GET /v3.2/download/dbupdate/monthly/subdomains`)

## Databases - IP Geolocation
- [`DbIpCountryStatus.ts`](DbIpCountryStatus.ts): IP to Country Snapshot Status (`GET /v3.3/status/snapshot/ip/country`)
- [`DbIpCountry.ts`](DbIpCountry.ts): IP to Country Snapshot (`GET /v3.3/download/snapshot/ip/country`)
- [`DbIpCityStatus.ts`](DbIpCityStatus.ts): IP to City Snapshot Status (`GET /v3.3/status/snapshot/ip/city`)
- [`DbIpCity.ts`](DbIpCity.ts): IP to City Snapshot (`GET /v3.3/download/snapshot/ip/city`)

## Databases - ASN WHOIS
- [`DbAsnWhois.ts`](DbAsnWhois.ts): ASN WHOIS Snapshot (`GET /v3.3/download/snapshot/asn/whois`)
- [`DbAsnWhoisStatus.ts`](DbAsnWhoisStatus.ts): ASN WHOIS Snapshot Status (`GET /v3.3/status/snapshot/asn/whois`)

## Databases - IP WHOIS
- [`DbIpWhois.ts`](DbIpWhois.ts): IP WHOIS Snapshot (`GET /v3.3/download/snapshot/ip/whois`)
- [`DbIpWhoisStatus.ts`](DbIpWhoisStatus.ts): IP WHOIS Snapshot Status (`GET /v3.3/status/snapshot/ip/whois`)

## Databases - IP Security
- [`DbIpSecurity.ts`](DbIpSecurity.ts): IP Security Snapshot (`GET /v3.3/download/snapshot/ip/security`)
- [`DbIpSecurityStatus.ts`](DbIpSecurityStatus.ts): IP Security Snapshot Status (`GET /v3.3/status/snapshot/ip/security`)

## Databases - Threat Feed
- [`DownloadThreatFeedPhishing.ts`](DownloadThreatFeedPhishing.ts): Download the daily phishing threat feed (CSV) (`GET /v3.4/download/threat-feed/phishing`)
- [`DownloadThreatFeedPhishingSample.ts`](DownloadThreatFeedPhishingSample.ts): Download a sample of the phishing threat feed (CSV) (`GET /v3.4/download/threat-feed/phishing/sample`)
- [`DownloadThreatFeedMalware.ts`](DownloadThreatFeedMalware.ts): Download the daily malware threat feed (CSV) (`GET /v3.4/download/threat-feed/malware`)
- [`DownloadThreatFeedMalwareSample.ts`](DownloadThreatFeedMalwareSample.ts): Download a sample of the malware threat feed (CSV) (`GET /v3.4/download/threat-feed/malware/sample`)
- [`DownloadThreatFeedSpam.ts`](DownloadThreatFeedSpam.ts): Download the daily spam threat feed (CSV) (`GET /v3.4/download/threat-feed/spam`)
- [`DownloadThreatFeedSpamSample.ts`](DownloadThreatFeedSpamSample.ts): Download a sample of the spam threat feed (CSV) (`GET /v3.4/download/threat-feed/spam/sample`)
