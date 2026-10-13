# Ruby Runnable Examples

Install: see the [Ruby guide](../../docs/languages/ruby.md). Set the `WHOISFREAKS_API_KEY` environment variable and run any file below.

## WHOIS
- [`WhoisLive.rb`](WhoisLive.rb): Live WHOIS Lookup (`GET /v2.0/whois/live`)
- [`BulkWhois.rb`](BulkWhois.rb): Bulk WHOIS Lookup (`POST /v2.0/bulkwhois/live`)
- [`WhoisHistory.rb`](WhoisHistory.rb): Historical WHOIS records for a domain (`GET /v2.0/whois/history`)
- [`WhoisReverse.rb`](WhoisReverse.rb): Reverse WHOIS lookup by keyword (`GET /v2.0/whois/reverse`)

## DNS
- [`DnsLive.rb`](DnsLive.rb): Live DNS Lookup (`GET /v2.0/dns/live`)
- [`DnsHistorical.rb`](DnsHistorical.rb): Historical DNS Lookup (`GET /v2.0/dns/historical`)
- [`DnsReverse.rb`](DnsReverse.rb): Reverse DNS Lookup (`GET /v2.1/dns/reverse`)
- [`DnsBulk.rb`](DnsBulk.rb): Bulk DNS Lookup (`POST /v2.0/dns/bulk/live`)

## Domain Availability
- [`DomainAvailabilityV2.rb`](DomainAvailabilityV2.rb): Domain Availability Check with Suggestions (`GET /v2.0/domain/availability`)
- [`BulkDomainAvailabilityV2.rb`](BulkDomainAvailabilityV2.rb): Bulk Domain Availability Check (`POST /v2.0/domain/availability`)

## Typosquatting
- [`Typosquatting.rb`](Typosquatting.rb): Typosquatting Lookup (`GET /v3.0/domain/typos`)

## SSL
- [`SslLookup.rb`](SslLookup.rb): SSL Certificate Lookup (`GET /v1.0/ssl/live`)

## Geolocation
- [`Geolocation.rb`](Geolocation.rb): IP Geolocation Lookup (`GET /v1.0/geolocation`)
- [`BulkGeolocation.rb`](BulkGeolocation.rb): Bulk IP Geolocation (`POST /v1.0/geolocation`)

## Subdomains
- [`Subdomains.rb`](Subdomains.rb): Subdomains Lookup (`GET /v1.0/subdomains`)

## IP Reputation
- [`IpReputation.rb`](IpReputation.rb): IP Reputation Lookup (`GET /v1.0/security`)
- [`BulkIpReputation.rb`](BulkIpReputation.rb): Bulk IP Reputation (`POST /v1.0/security`)

## Domain Reputation
- [`DomainReputation.rb`](DomainReputation.rb): Domain Reputation Lookup (`GET /v1/domain/security`)

## ASN WHOIS
- [`AsnWhois.rb`](AsnWhois.rb): ASN WHOIS Lookup (`GET /v2.0/asn-whois`)

## IP WHOIS
- [`IpWhois.rb`](IpWhois.rb): IP WHOIS Lookup (`GET /v1.0/ip-whois`)

## Account
- [`RotateApiKey.rb`](RotateApiKey.rb): Rotate API Key (`GET /v1.0/api-key/rotate`)
- [`AccountUsage.rb`](AccountUsage.rb): Account Usage (`GET /v1.0/whoisapi/usage`)
- [`DatabaseFileStatus.rb`](DatabaseFileStatus.rb): Database File Status (Public) (`GET /v3.4/status`)

## Databases - Newly Registered
- [`DbNewlyGtld.rb`](DbNewlyGtld.rb): Newly Registered gTLD (CSV) (`GET /v3.1/download/domainer/gtld`)
- [`DbNewlyCctld.rb`](DbNewlyCctld.rb): Newly Registered ccTLD (CSV) (`GET /v3.1/download/domainer/cctld`)
- [`DbNewlyGtldCleaned.rb`](DbNewlyGtldCleaned.rb): Newly Registered gTLD Cleaned WHOIS (CSV) (`GET /v3.1/download/domainer/gtld/cleaned`)
- [`DbNewlyCctldCleaned.rb`](DbNewlyCctldCleaned.rb): Newly Registered ccTLD Cleaned WHOIS (CSV) (`GET /v3.1/download/domainer/cctld/cleaned`)
- [`DbNewlyGtldJson.rb`](DbNewlyGtldJson.rb): Newly Registered gTLD (JSON) (`GET /v3.1/domains/newly/gtld`)
- [`DbNewlyCctldJson.rb`](DbNewlyCctldJson.rb): Newly Registered ccTLD (JSON) (`GET /v3.1/domains/newly/cctld`)
- [`DbNewlyDns.rb`](DbNewlyDns.rb): Newly Registered With DNS (`GET /v3.1/download/domainer/newly/dns`)

## Databases - Expiring & Dropped
- [`DbExpired.rb`](DbExpired.rb): Expiring Domains (`GET /v3.1/download/domainer/expired`)
- [`DbExpiredCleaned.rb`](DbExpiredCleaned.rb): Expiring Cleaned WHOIS (`GET /v3.1/download/domainer/expired/cleaned`)
- [`DbDropped.rb`](DbDropped.rb): Dropped Domains (`GET /v3.1/download/domainer/dropped`)
- [`DbDroppedJson.rb`](DbDroppedJson.rb): Dropped Domains (JSON) (`GET /v3.1/domains/dropped`)
- [`DbDroppedBacklinks.rb`](DbDroppedBacklinks.rb): Dropped With Backlinks (`GET /v3.3/download/domainer/dropped/backlinks`)

## Databases - WHOIS
- [`DbWhoisDaily.rb`](DbWhoisDaily.rb): WHOIS Database Daily (`GET /v3.3/download/dbupdate/daily/domains/whois`)
- [`DbWhoisWeekly.rb`](DbWhoisWeekly.rb): WHOIS Database Weekly (`GET /v3.3/download/dbupdate/weekly/domains/whois`)
- [`DbWhoisMonthly.rb`](DbWhoisMonthly.rb): WHOIS Database Monthly (`GET /v3.3/download/dbupdate/monthly/domains/whois`)

## Databases - DNS
- [`DbDnsDaily.rb`](DbDnsDaily.rb): DNS Database Daily (`GET /v3.2/download/dbupdate/daily/dns`)
- [`DbDnsWeekly.rb`](DbDnsWeekly.rb): DNS Database Weekly (`GET /v3.2/download/dbupdate/weekly/dns`)
- [`DbDnsMonthly.rb`](DbDnsMonthly.rb): DNS Database Monthly (`GET /v3.2/download/dbupdate/monthly/dns`)

## Databases - Subdomains
- [`DbSubdomainsDaily.rb`](DbSubdomainsDaily.rb): Subdomains Daily (`GET /v3.2/download/dbupdate/daily/subdomains`)
- [`DbSubdomainsWeekly.rb`](DbSubdomainsWeekly.rb): Subdomains Weekly (`GET /v3.2/download/dbupdate/weekly/subdomains`)
- [`DbSubdomainsMonthly.rb`](DbSubdomainsMonthly.rb): Subdomains Monthly (`GET /v3.2/download/dbupdate/monthly/subdomains`)

## Databases - IP Geolocation
- [`DbIpCountryStatus.rb`](DbIpCountryStatus.rb): IP to Country Snapshot Status (`GET /v3.3/status/snapshot/ip/country`)
- [`DbIpCountry.rb`](DbIpCountry.rb): IP to Country Snapshot (`GET /v3.3/download/snapshot/ip/country`)
- [`DbIpCityStatus.rb`](DbIpCityStatus.rb): IP to City Snapshot Status (`GET /v3.3/status/snapshot/ip/city`)
- [`DbIpCity.rb`](DbIpCity.rb): IP to City Snapshot (`GET /v3.3/download/snapshot/ip/city`)

## Databases - ASN WHOIS
- [`DbAsnWhois.rb`](DbAsnWhois.rb): ASN WHOIS Snapshot (`GET /v3.3/download/snapshot/asn/whois`)
- [`DbAsnWhoisStatus.rb`](DbAsnWhoisStatus.rb): ASN WHOIS Snapshot Status (`GET /v3.3/status/snapshot/asn/whois`)

## Databases - IP WHOIS
- [`DbIpWhois.rb`](DbIpWhois.rb): IP WHOIS Snapshot (`GET /v3.3/download/snapshot/ip/whois`)
- [`DbIpWhoisStatus.rb`](DbIpWhoisStatus.rb): IP WHOIS Snapshot Status (`GET /v3.3/status/snapshot/ip/whois`)

## Databases - IP Security
- [`DbIpSecurity.rb`](DbIpSecurity.rb): IP Security Snapshot (`GET /v3.3/download/snapshot/ip/security`)
- [`DbIpSecurityStatus.rb`](DbIpSecurityStatus.rb): IP Security Snapshot Status (`GET /v3.3/status/snapshot/ip/security`)

## Databases - Threat Feed
- [`DownloadThreatFeedPhishing.rb`](DownloadThreatFeedPhishing.rb): Download the daily phishing threat feed (CSV) (`GET /v3.4/download/threat-feed/phishing`)
- [`DownloadThreatFeedPhishingSample.rb`](DownloadThreatFeedPhishingSample.rb): Download a sample of the phishing threat feed (CSV) (`GET /v3.4/download/threat-feed/phishing/sample`)
- [`DownloadThreatFeedMalware.rb`](DownloadThreatFeedMalware.rb): Download the daily malware threat feed (CSV) (`GET /v3.4/download/threat-feed/malware`)
- [`DownloadThreatFeedMalwareSample.rb`](DownloadThreatFeedMalwareSample.rb): Download a sample of the malware threat feed (CSV) (`GET /v3.4/download/threat-feed/malware/sample`)
- [`DownloadThreatFeedSpam.rb`](DownloadThreatFeedSpam.rb): Download the daily spam threat feed (CSV) (`GET /v3.4/download/threat-feed/spam`)
- [`DownloadThreatFeedSpamSample.rb`](DownloadThreatFeedSpamSample.rb): Download a sample of the spam threat feed (CSV) (`GET /v3.4/download/threat-feed/spam/sample`)
