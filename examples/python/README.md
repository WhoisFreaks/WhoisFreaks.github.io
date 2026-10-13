# Python Runnable Examples

Install: see the [Python guide](../../docs/languages/python.md). Set the `WHOISFREAKS_API_KEY` environment variable and run any file below.

## WHOIS
- [`WhoisLive.py`](WhoisLive.py): Live WHOIS Lookup (`GET /v2.0/whois/live`)
- [`BulkWhois.py`](BulkWhois.py): Bulk WHOIS Lookup (`POST /v2.0/bulkwhois/live`)
- [`WhoisHistory.py`](WhoisHistory.py): Historical WHOIS records for a domain (`GET /v2.0/whois/history`)
- [`WhoisReverse.py`](WhoisReverse.py): Reverse WHOIS lookup by keyword (`GET /v2.0/whois/reverse`)

## DNS
- [`DnsLive.py`](DnsLive.py): Live DNS Lookup (`GET /v2.0/dns/live`)
- [`DnsHistorical.py`](DnsHistorical.py): Historical DNS Lookup (`GET /v2.0/dns/historical`)
- [`DnsReverse.py`](DnsReverse.py): Reverse DNS Lookup (`GET /v2.1/dns/reverse`)
- [`DnsBulk.py`](DnsBulk.py): Bulk DNS Lookup (`POST /v2.0/dns/bulk/live`)

## Domain Availability
- [`DomainAvailabilityV2.py`](DomainAvailabilityV2.py): Domain Availability Check with Suggestions (`GET /v2.0/domain/availability`)
- [`BulkDomainAvailabilityV2.py`](BulkDomainAvailabilityV2.py): Bulk Domain Availability Check (`POST /v2.0/domain/availability`)

## Typosquatting
- [`Typosquatting.py`](Typosquatting.py): Typosquatting Lookup (`GET /v3.0/domain/typos`)

## SSL
- [`SslLookup.py`](SslLookup.py): SSL Certificate Lookup (`GET /v1.0/ssl/live`)

## Geolocation
- [`Geolocation.py`](Geolocation.py): IP Geolocation Lookup (`GET /v1.0/geolocation`)
- [`BulkGeolocation.py`](BulkGeolocation.py): Bulk IP Geolocation (`POST /v1.0/geolocation`)

## Subdomains
- [`Subdomains.py`](Subdomains.py): Subdomains Lookup (`GET /v1.0/subdomains`)

## IP Reputation
- [`IpReputation.py`](IpReputation.py): IP Reputation Lookup (`GET /v1.0/security`)
- [`BulkIpReputation.py`](BulkIpReputation.py): Bulk IP Reputation (`POST /v1.0/security`)

## Domain Reputation
- [`DomainReputation.py`](DomainReputation.py): Domain Reputation Lookup (`GET /v1/domain/security`)

## ASN WHOIS
- [`AsnWhois.py`](AsnWhois.py): ASN WHOIS Lookup (`GET /v2.0/asn-whois`)

## IP WHOIS
- [`IpWhois.py`](IpWhois.py): IP WHOIS Lookup (`GET /v1.0/ip-whois`)

## Account
- [`RotateApiKey.py`](RotateApiKey.py): Rotate API Key (`GET /v1.0/api-key/rotate`)
- [`AccountUsage.py`](AccountUsage.py): Account Usage (`GET /v1.0/whoisapi/usage`)
- [`DatabaseFileStatus.py`](DatabaseFileStatus.py): Database File Status (Public) (`GET /v3.4/status`)

## Databases - Newly Registered
- [`DbNewlyGtld.py`](DbNewlyGtld.py): Newly Registered gTLD (CSV) (`GET /v3.1/download/domainer/gtld`)
- [`DbNewlyCctld.py`](DbNewlyCctld.py): Newly Registered ccTLD (CSV) (`GET /v3.1/download/domainer/cctld`)
- [`DbNewlyGtldCleaned.py`](DbNewlyGtldCleaned.py): Newly Registered gTLD Cleaned WHOIS (CSV) (`GET /v3.1/download/domainer/gtld/cleaned`)
- [`DbNewlyCctldCleaned.py`](DbNewlyCctldCleaned.py): Newly Registered ccTLD Cleaned WHOIS (CSV) (`GET /v3.1/download/domainer/cctld/cleaned`)
- [`DbNewlyGtldJson.py`](DbNewlyGtldJson.py): Newly Registered gTLD (JSON) (`GET /v3.1/domains/newly/gtld`)
- [`DbNewlyCctldJson.py`](DbNewlyCctldJson.py): Newly Registered ccTLD (JSON) (`GET /v3.1/domains/newly/cctld`)
- [`DbNewlyDns.py`](DbNewlyDns.py): Newly Registered With DNS (`GET /v3.1/download/domainer/newly/dns`)

## Databases - Expiring & Dropped
- [`DbExpired.py`](DbExpired.py): Expiring Domains (`GET /v3.1/download/domainer/expired`)
- [`DbExpiredCleaned.py`](DbExpiredCleaned.py): Expiring Cleaned WHOIS (`GET /v3.1/download/domainer/expired/cleaned`)
- [`DbDropped.py`](DbDropped.py): Dropped Domains (`GET /v3.1/download/domainer/dropped`)
- [`DbDroppedJson.py`](DbDroppedJson.py): Dropped Domains (JSON) (`GET /v3.1/domains/dropped`)
- [`DbDroppedBacklinks.py`](DbDroppedBacklinks.py): Dropped With Backlinks (`GET /v3.3/download/domainer/dropped/backlinks`)

## Databases - WHOIS
- [`DbWhoisDaily.py`](DbWhoisDaily.py): WHOIS Database Daily (`GET /v3.3/download/dbupdate/daily/domains/whois`)
- [`DbWhoisWeekly.py`](DbWhoisWeekly.py): WHOIS Database Weekly (`GET /v3.3/download/dbupdate/weekly/domains/whois`)
- [`DbWhoisMonthly.py`](DbWhoisMonthly.py): WHOIS Database Monthly (`GET /v3.3/download/dbupdate/monthly/domains/whois`)

## Databases - DNS
- [`DbDnsDaily.py`](DbDnsDaily.py): DNS Database Daily (`GET /v3.2/download/dbupdate/daily/dns`)
- [`DbDnsWeekly.py`](DbDnsWeekly.py): DNS Database Weekly (`GET /v3.2/download/dbupdate/weekly/dns`)
- [`DbDnsMonthly.py`](DbDnsMonthly.py): DNS Database Monthly (`GET /v3.2/download/dbupdate/monthly/dns`)

## Databases - Subdomains
- [`DbSubdomainsDaily.py`](DbSubdomainsDaily.py): Subdomains Daily (`GET /v3.2/download/dbupdate/daily/subdomains`)
- [`DbSubdomainsWeekly.py`](DbSubdomainsWeekly.py): Subdomains Weekly (`GET /v3.2/download/dbupdate/weekly/subdomains`)
- [`DbSubdomainsMonthly.py`](DbSubdomainsMonthly.py): Subdomains Monthly (`GET /v3.2/download/dbupdate/monthly/subdomains`)

## Databases - IP Geolocation
- [`DbIpCountryStatus.py`](DbIpCountryStatus.py): IP to Country Snapshot Status (`GET /v3.3/status/snapshot/ip/country`)
- [`DbIpCountry.py`](DbIpCountry.py): IP to Country Snapshot (`GET /v3.3/download/snapshot/ip/country`)
- [`DbIpCityStatus.py`](DbIpCityStatus.py): IP to City Snapshot Status (`GET /v3.3/status/snapshot/ip/city`)
- [`DbIpCity.py`](DbIpCity.py): IP to City Snapshot (`GET /v3.3/download/snapshot/ip/city`)

## Databases - ASN WHOIS
- [`DbAsnWhois.py`](DbAsnWhois.py): ASN WHOIS Snapshot (`GET /v3.3/download/snapshot/asn/whois`)
- [`DbAsnWhoisStatus.py`](DbAsnWhoisStatus.py): ASN WHOIS Snapshot Status (`GET /v3.3/status/snapshot/asn/whois`)

## Databases - IP WHOIS
- [`DbIpWhois.py`](DbIpWhois.py): IP WHOIS Snapshot (`GET /v3.3/download/snapshot/ip/whois`)
- [`DbIpWhoisStatus.py`](DbIpWhoisStatus.py): IP WHOIS Snapshot Status (`GET /v3.3/status/snapshot/ip/whois`)

## Databases - IP Security
- [`DbIpSecurity.py`](DbIpSecurity.py): IP Security Snapshot (`GET /v3.3/download/snapshot/ip/security`)
- [`DbIpSecurityStatus.py`](DbIpSecurityStatus.py): IP Security Snapshot Status (`GET /v3.3/status/snapshot/ip/security`)

## Databases - Threat Feed
- [`DownloadThreatFeedPhishing.py`](DownloadThreatFeedPhishing.py): Download the daily phishing threat feed (CSV) (`GET /v3.4/download/threat-feed/phishing`)
- [`DownloadThreatFeedPhishingSample.py`](DownloadThreatFeedPhishingSample.py): Download a sample of the phishing threat feed (CSV) (`GET /v3.4/download/threat-feed/phishing/sample`)
- [`DownloadThreatFeedMalware.py`](DownloadThreatFeedMalware.py): Download the daily malware threat feed (CSV) (`GET /v3.4/download/threat-feed/malware`)
- [`DownloadThreatFeedMalwareSample.py`](DownloadThreatFeedMalwareSample.py): Download a sample of the malware threat feed (CSV) (`GET /v3.4/download/threat-feed/malware/sample`)
- [`DownloadThreatFeedSpam.py`](DownloadThreatFeedSpam.py): Download the daily spam threat feed (CSV) (`GET /v3.4/download/threat-feed/spam`)
- [`DownloadThreatFeedSpamSample.py`](DownloadThreatFeedSpamSample.py): Download a sample of the spam threat feed (CSV) (`GET /v3.4/download/threat-feed/spam/sample`)
