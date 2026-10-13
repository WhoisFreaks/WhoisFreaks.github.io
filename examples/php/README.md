# PHP Runnable Examples

Install: see the [PHP guide](../../docs/languages/php.md). Set the `WHOISFREAKS_API_KEY` environment variable and run any file below.

## WHOIS
- [`WhoisLive.php`](WhoisLive.php): Live WHOIS Lookup (`GET /v2.0/whois/live`)
- [`BulkWhois.php`](BulkWhois.php): Bulk WHOIS Lookup (`POST /v2.0/bulkwhois/live`)
- [`WhoisHistory.php`](WhoisHistory.php): Historical WHOIS records for a domain (`GET /v2.0/whois/history`)
- [`WhoisReverse.php`](WhoisReverse.php): Reverse WHOIS lookup by keyword (`GET /v2.0/whois/reverse`)

## DNS
- [`DnsLive.php`](DnsLive.php): Live DNS Lookup (`GET /v2.0/dns/live`)
- [`DnsHistorical.php`](DnsHistorical.php): Historical DNS Lookup (`GET /v2.0/dns/historical`)
- [`DnsReverse.php`](DnsReverse.php): Reverse DNS Lookup (`GET /v2.1/dns/reverse`)
- [`DnsBulk.php`](DnsBulk.php): Bulk DNS Lookup (`POST /v2.0/dns/bulk/live`)

## Domain Availability
- [`DomainAvailabilityV2.php`](DomainAvailabilityV2.php): Domain Availability Check with Suggestions (`GET /v2.0/domain/availability`)
- [`BulkDomainAvailabilityV2.php`](BulkDomainAvailabilityV2.php): Bulk Domain Availability Check (`POST /v2.0/domain/availability`)

## Typosquatting
- [`Typosquatting.php`](Typosquatting.php): Typosquatting Lookup (`GET /v3.0/domain/typos`)

## SSL
- [`SslLookup.php`](SslLookup.php): SSL Certificate Lookup (`GET /v1.0/ssl/live`)

## Geolocation
- [`Geolocation.php`](Geolocation.php): IP Geolocation Lookup (`GET /v1.0/geolocation`)
- [`BulkGeolocation.php`](BulkGeolocation.php): Bulk IP Geolocation (`POST /v1.0/geolocation`)

## Subdomains
- [`Subdomains.php`](Subdomains.php): Subdomains Lookup (`GET /v1.0/subdomains`)

## IP Reputation
- [`IpReputation.php`](IpReputation.php): IP Reputation Lookup (`GET /v1.0/security`)
- [`BulkIpReputation.php`](BulkIpReputation.php): Bulk IP Reputation (`POST /v1.0/security`)

## Domain Reputation
- [`DomainReputation.php`](DomainReputation.php): Domain Reputation Lookup (`GET /v1/domain/security`)

## ASN WHOIS
- [`AsnWhois.php`](AsnWhois.php): ASN WHOIS Lookup (`GET /v2.0/asn-whois`)

## IP WHOIS
- [`IpWhois.php`](IpWhois.php): IP WHOIS Lookup (`GET /v1.0/ip-whois`)

## Account
- [`RotateApiKey.php`](RotateApiKey.php): Rotate API Key (`GET /v1.0/api-key/rotate`)
- [`AccountUsage.php`](AccountUsage.php): Account Usage (`GET /v1.0/whoisapi/usage`)
- [`DatabaseFileStatus.php`](DatabaseFileStatus.php): Database File Status (Public) (`GET /v3.4/status`)

## Databases - Newly Registered
- [`DbNewlyGtld.php`](DbNewlyGtld.php): Newly Registered gTLD (CSV) (`GET /v3.1/download/domainer/gtld`)
- [`DbNewlyCctld.php`](DbNewlyCctld.php): Newly Registered ccTLD (CSV) (`GET /v3.1/download/domainer/cctld`)
- [`DbNewlyGtldCleaned.php`](DbNewlyGtldCleaned.php): Newly Registered gTLD Cleaned WHOIS (CSV) (`GET /v3.1/download/domainer/gtld/cleaned`)
- [`DbNewlyCctldCleaned.php`](DbNewlyCctldCleaned.php): Newly Registered ccTLD Cleaned WHOIS (CSV) (`GET /v3.1/download/domainer/cctld/cleaned`)
- [`DbNewlyGtldJson.php`](DbNewlyGtldJson.php): Newly Registered gTLD (JSON) (`GET /v3.1/domains/newly/gtld`)
- [`DbNewlyCctldJson.php`](DbNewlyCctldJson.php): Newly Registered ccTLD (JSON) (`GET /v3.1/domains/newly/cctld`)
- [`DbNewlyDns.php`](DbNewlyDns.php): Newly Registered With DNS (`GET /v3.1/download/domainer/newly/dns`)

## Databases - Expiring & Dropped
- [`DbExpired.php`](DbExpired.php): Expiring Domains (`GET /v3.1/download/domainer/expired`)
- [`DbExpiredCleaned.php`](DbExpiredCleaned.php): Expiring Cleaned WHOIS (`GET /v3.1/download/domainer/expired/cleaned`)
- [`DbDropped.php`](DbDropped.php): Dropped Domains (`GET /v3.1/download/domainer/dropped`)
- [`DbDroppedJson.php`](DbDroppedJson.php): Dropped Domains (JSON) (`GET /v3.1/domains/dropped`)
- [`DbDroppedBacklinks.php`](DbDroppedBacklinks.php): Dropped With Backlinks (`GET /v3.3/download/domainer/dropped/backlinks`)

## Databases - WHOIS
- [`DbWhoisDaily.php`](DbWhoisDaily.php): WHOIS Database Daily (`GET /v3.3/download/dbupdate/daily/domains/whois`)
- [`DbWhoisWeekly.php`](DbWhoisWeekly.php): WHOIS Database Weekly (`GET /v3.3/download/dbupdate/weekly/domains/whois`)
- [`DbWhoisMonthly.php`](DbWhoisMonthly.php): WHOIS Database Monthly (`GET /v3.3/download/dbupdate/monthly/domains/whois`)

## Databases - DNS
- [`DbDnsDaily.php`](DbDnsDaily.php): DNS Database Daily (`GET /v3.2/download/dbupdate/daily/dns`)
- [`DbDnsWeekly.php`](DbDnsWeekly.php): DNS Database Weekly (`GET /v3.2/download/dbupdate/weekly/dns`)
- [`DbDnsMonthly.php`](DbDnsMonthly.php): DNS Database Monthly (`GET /v3.2/download/dbupdate/monthly/dns`)

## Databases - Subdomains
- [`DbSubdomainsDaily.php`](DbSubdomainsDaily.php): Subdomains Daily (`GET /v3.2/download/dbupdate/daily/subdomains`)
- [`DbSubdomainsWeekly.php`](DbSubdomainsWeekly.php): Subdomains Weekly (`GET /v3.2/download/dbupdate/weekly/subdomains`)
- [`DbSubdomainsMonthly.php`](DbSubdomainsMonthly.php): Subdomains Monthly (`GET /v3.2/download/dbupdate/monthly/subdomains`)

## Databases - IP Geolocation
- [`DbIpCountryStatus.php`](DbIpCountryStatus.php): IP to Country Snapshot Status (`GET /v3.3/status/snapshot/ip/country`)
- [`DbIpCountry.php`](DbIpCountry.php): IP to Country Snapshot (`GET /v3.3/download/snapshot/ip/country`)
- [`DbIpCityStatus.php`](DbIpCityStatus.php): IP to City Snapshot Status (`GET /v3.3/status/snapshot/ip/city`)
- [`DbIpCity.php`](DbIpCity.php): IP to City Snapshot (`GET /v3.3/download/snapshot/ip/city`)

## Databases - ASN WHOIS
- [`DbAsnWhois.php`](DbAsnWhois.php): ASN WHOIS Snapshot (`GET /v3.3/download/snapshot/asn/whois`)
- [`DbAsnWhoisStatus.php`](DbAsnWhoisStatus.php): ASN WHOIS Snapshot Status (`GET /v3.3/status/snapshot/asn/whois`)

## Databases - IP WHOIS
- [`DbIpWhois.php`](DbIpWhois.php): IP WHOIS Snapshot (`GET /v3.3/download/snapshot/ip/whois`)
- [`DbIpWhoisStatus.php`](DbIpWhoisStatus.php): IP WHOIS Snapshot Status (`GET /v3.3/status/snapshot/ip/whois`)

## Databases - IP Security
- [`DbIpSecurity.php`](DbIpSecurity.php): IP Security Snapshot (`GET /v3.3/download/snapshot/ip/security`)
- [`DbIpSecurityStatus.php`](DbIpSecurityStatus.php): IP Security Snapshot Status (`GET /v3.3/status/snapshot/ip/security`)

## Databases - Threat Feed
- [`DownloadThreatFeedPhishing.php`](DownloadThreatFeedPhishing.php): Download the daily phishing threat feed (CSV) (`GET /v3.4/download/threat-feed/phishing`)
- [`DownloadThreatFeedPhishingSample.php`](DownloadThreatFeedPhishingSample.php): Download a sample of the phishing threat feed (CSV) (`GET /v3.4/download/threat-feed/phishing/sample`)
- [`DownloadThreatFeedMalware.php`](DownloadThreatFeedMalware.php): Download the daily malware threat feed (CSV) (`GET /v3.4/download/threat-feed/malware`)
- [`DownloadThreatFeedMalwareSample.php`](DownloadThreatFeedMalwareSample.php): Download a sample of the malware threat feed (CSV) (`GET /v3.4/download/threat-feed/malware/sample`)
- [`DownloadThreatFeedSpam.php`](DownloadThreatFeedSpam.php): Download the daily spam threat feed (CSV) (`GET /v3.4/download/threat-feed/spam`)
- [`DownloadThreatFeedSpamSample.php`](DownloadThreatFeedSpamSample.php): Download a sample of the spam threat feed (CSV) (`GET /v3.4/download/threat-feed/spam/sample`)
