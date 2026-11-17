# Endpoint Reference

The WhoisFreaks API exposes **95 endpoints** across **23 categories**, organized into 3 sections. Every endpoint is available in all 10 SDKs.

## API Solutions

Real-time and on-demand lookup APIs. Query a single domain, IP, or ASN and get structured JSON (or XML) back immediately.

27 endpoints across 11 categories. See the [API Solutions overview](api-solutions.md).

- [WHOIS](whois.md): 4 endpoints
- [DNS](dns.md): 8 endpoints
- [Domain Availability](domain-availability.md): 2 endpoints
- [Typosquatting](typosquatting.md): 2 endpoints
- [SSL](ssl.md): 1 endpoint
- [Geolocation](geolocation.md): 2 endpoints
- [Subdomains](subdomains.md): 1 endpoint
- [IP Reputation](ip-reputation.md): 4 endpoints
- [Domain Reputation](domain-reputation.md): 1 endpoint
- [ASN WHOIS](asn-whois.md): 1 endpoint
- [IP WHOIS](ip-whois.md): 1 endpoint

## Databases

Bulk data feeds and downloadable database snapshots for large-scale processing: newly registered, expiring/dropped, and full WHOIS/DNS/IP datasets.

65 endpoints across 11 categories. See the [Databases overview](databases.md).

- [Databases - Newly Registered](databases-newly-registered.md): 7 endpoints
- [Databases - Expiring & Dropped](databases-expiring-dropped.md): 5 endpoints
- [Databases - WHOIS](databases-whois.md): 3 endpoints
- [Databases - DNS](databases-dns.md): 3 endpoints
- [Databases - Subdomains](databases-subdomains.md): 3 endpoints
- [Databases - IP Geolocation](databases-ip-geolocation.md): 4 endpoints
- [Databases - ASN WHOIS](databases-asn-whois.md): 2 endpoints
- [Databases - IP WHOIS](databases-ip-whois.md): 2 endpoints
- [Databases - IP Security](databases-ip-security.md): 2 endpoints
- [Databases - Threat Feed](databases-threat-feed.md): 6 endpoints
- [Databases - Streaming](databases-streaming.md): 28 endpoints

## Account & Utilities

Manage your account, monitor API usage and credits, and rotate your API key.

3 endpoints across 1 category. See the [Account & Utilities overview](account-utilities.md).

- [Account](account.md): 3 endpoints

## Full endpoint list

| Section | Category | Method | Path | Operation |
|---------|----------|--------|------|-----------|
| API Solutions | WHOIS | GET | `/v2.0/whois/live` | `whoisLive` |
| API Solutions | WHOIS | POST | `/v2.0/bulkwhois/live` | `bulkWhois` |
| API Solutions | WHOIS | GET | `/v2.0/whois/history` | `whoisHistory` |
| API Solutions | WHOIS | GET | `/v2.0/whois/reverse` | `whoisReverse` |
| API Solutions | DNS | GET | `/v2.0/dns/live` | `dnsLive` |
| API Solutions | DNS | GET | `/v2.0/dns/historical` | `dnsHistorical` |
| API Solutions | DNS | GET | `/v2.1/dns/reverse` | `dnsReverse` |
| API Solutions | DNS | GET | `/v2.2/dns/historical` | `dnsHistoricalV22` |
| API Solutions | DNS | GET | `/v2.3/dns/historical` | `dnsHistoricalV23` |
| API Solutions | DNS | GET | `/v2.2/dns/reverse` | `dnsReverseV22` |
| API Solutions | DNS | GET | `/v2.3/dns/reverse` | `dnsReverseV23` |
| API Solutions | DNS | POST | `/v2.0/dns/bulk/live` | `dnsBulk` |
| API Solutions | Domain Availability | GET | `/v2.0/domain/availability` | `domainAvailabilityV2` |
| API Solutions | Domain Availability | POST | `/v2.0/domain/availability` | `bulkDomainAvailabilityV2` |
| API Solutions | Typosquatting | GET | `/v3.0/domain/typos` | `typosquatting` |
| API Solutions | Typosquatting | GET | `/v3.0/subdomains/typos` | `subdomainTyposquatting` |
| API Solutions | SSL | GET | `/v1.0/ssl/live` | `sslLookup` |
| API Solutions | Geolocation | GET | `/v1.0/geolocation` | `geolocation` |
| API Solutions | Geolocation | POST | `/v1.0/geolocation` | `bulkGeolocation` |
| API Solutions | Subdomains | GET | `/v1.0/subdomains` | `subdomains` |
| API Solutions | IP Reputation | GET | `/v1.0/security` | `ipReputation` |
| API Solutions | IP Reputation | POST | `/v1.0/security` | `bulkIpReputation` |
| API Solutions | IP Reputation | GET | `/v2.0/security` | `ipReputationV2` |
| API Solutions | IP Reputation | POST | `/v2.0/security` | `bulkIpReputationV2` |
| API Solutions | Domain Reputation | GET | `/v1/domain/security` | `domainReputation` |
| API Solutions | ASN WHOIS | GET | `/v2.0/asn-whois` | `asnWhois` |
| API Solutions | IP WHOIS | GET | `/v1.0/ip-whois` | `ipWhois` |
| Account & Utilities | Account | GET | `/v1.0/api-key/rotate` | `rotateApiKey` |
| Account & Utilities | Account | GET | `/v1.0/whoisapi/usage` | `accountUsage` |
| Account & Utilities | Account | GET | `/v3.4/status` | `databaseFileStatus` |
| Databases | Databases - Newly Registered | GET | `/v3.1/download/domainer/gtld` | `dbNewlyGtld` |
| Databases | Databases - Newly Registered | GET | `/v3.1/download/domainer/cctld` | `dbNewlyCctld` |
| Databases | Databases - Newly Registered | GET | `/v3.1/download/domainer/gtld/cleaned` | `dbNewlyGtldCleaned` |
| Databases | Databases - Newly Registered | GET | `/v3.1/download/domainer/cctld/cleaned` | `dbNewlyCctldCleaned` |
| Databases | Databases - Newly Registered | GET | `/v3.1/domains/newly/gtld` | `dbNewlyGtldJson` |
| Databases | Databases - Newly Registered | GET | `/v3.1/domains/newly/cctld` | `dbNewlyCctldJson` |
| Databases | Databases - Newly Registered | GET | `/v3.1/download/domainer/newly/dns` | `dbNewlyDns` |
| Databases | Databases - Expiring & Dropped | GET | `/v3.1/download/domainer/expired` | `dbExpired` |
| Databases | Databases - Expiring & Dropped | GET | `/v3.1/download/domainer/expired/cleaned` | `dbExpiredCleaned` |
| Databases | Databases - Expiring & Dropped | GET | `/v3.1/download/domainer/dropped` | `dbDropped` |
| Databases | Databases - Expiring & Dropped | GET | `/v3.1/domains/dropped` | `dbDroppedJson` |
| Databases | Databases - Expiring & Dropped | GET | `/v3.3/download/domainer/dropped/backlinks` | `dbDroppedBacklinks` |
| Databases | Databases - WHOIS | GET | `/v3.3/download/dbupdate/daily/domains/whois` | `dbWhoisDaily` |
| Databases | Databases - WHOIS | GET | `/v3.3/download/dbupdate/weekly/domains/whois` | `dbWhoisWeekly` |
| Databases | Databases - WHOIS | GET | `/v3.3/download/dbupdate/monthly/domains/whois` | `dbWhoisMonthly` |
| Databases | Databases - DNS | GET | `/v3.2/download/dbupdate/daily/dns` | `dbDnsDaily` |
| Databases | Databases - DNS | GET | `/v3.2/download/dbupdate/weekly/dns` | `dbDnsWeekly` |
| Databases | Databases - DNS | GET | `/v3.2/download/dbupdate/monthly/dns` | `dbDnsMonthly` |
| Databases | Databases - Subdomains | GET | `/v3.2/download/dbupdate/daily/subdomains` | `dbSubdomainsDaily` |
| Databases | Databases - Subdomains | GET | `/v3.2/download/dbupdate/weekly/subdomains` | `dbSubdomainsWeekly` |
| Databases | Databases - Subdomains | GET | `/v3.2/download/dbupdate/monthly/subdomains` | `dbSubdomainsMonthly` |
| Databases | Databases - IP Geolocation | GET | `/v3.3/status/snapshot/ip/country` | `dbIpCountryStatus` |
| Databases | Databases - IP Geolocation | GET | `/v3.3/download/snapshot/ip/country` | `dbIpCountry` |
| Databases | Databases - IP Geolocation | GET | `/v3.3/status/snapshot/ip/city` | `dbIpCityStatus` |
| Databases | Databases - IP Geolocation | GET | `/v3.3/download/snapshot/ip/city` | `dbIpCity` |
| Databases | Databases - ASN WHOIS | GET | `/v3.3/download/snapshot/asn/whois` | `dbAsnWhois` |
| Databases | Databases - ASN WHOIS | GET | `/v3.3/status/snapshot/asn/whois` | `dbAsnWhoisStatus` |
| Databases | Databases - IP WHOIS | GET | `/v3.3/download/snapshot/ip/whois` | `dbIpWhois` |
| Databases | Databases - IP WHOIS | GET | `/v3.3/status/snapshot/ip/whois` | `dbIpWhoisStatus` |
| Databases | Databases - IP Security | GET | `/v3.3/download/snapshot/ip/security` | `dbIpSecurity` |
| Databases | Databases - IP Security | GET | `/v3.3/status/snapshot/ip/security` | `dbIpSecurityStatus` |
| Databases | Databases - Threat Feed | GET | `/v3.4/download/threat-feed/phishing` | `downloadThreatFeedPhishing` |
| Databases | Databases - Threat Feed | GET | `/v3.4/download/threat-feed/phishing/sample` | `downloadThreatFeedPhishingSample` |
| Databases | Databases - Threat Feed | GET | `/v3.4/download/threat-feed/malware` | `downloadThreatFeedMalware` |
| Databases | Databases - Threat Feed | GET | `/v3.4/download/threat-feed/malware/sample` | `downloadThreatFeedMalwareSample` |
| Databases | Databases - Threat Feed | GET | `/v3.4/download/threat-feed/spam` | `downloadThreatFeedSpam` |
| Databases | Databases - Threat Feed | GET | `/v3.4/download/threat-feed/spam/sample` | `downloadThreatFeedSpamSample` |
| Databases | Databases - Streaming | GET | `/v3.4/stream/threat-feed/phishing` | `streamThreatFeedPhishing` |
| Databases | Databases - Streaming | GET | `/v3.4/stream/threat-feed/phishing/sample` | `streamThreatFeedPhishingSample` |
| Databases | Databases - Streaming | GET | `/v3.4/stream/threat-feed/malware` | `streamThreatFeedMalware` |
| Databases | Databases - Streaming | GET | `/v3.4/stream/threat-feed/malware/sample` | `streamThreatFeedMalwareSample` |
| Databases | Databases - Streaming | GET | `/v3.4/stream/threat-feed/spam` | `streamThreatFeedSpam` |
| Databases | Databases - Streaming | GET | `/v3.4/stream/threat-feed/spam/sample` | `streamThreatFeedSpamSample` |
| Databases | Databases - Streaming | GET | `/v3.3/stream/domainer/gtld` | `streamDomainerGtld` |
| Databases | Databases - Streaming | GET | `/v3.3/stream/domainer/gtld/cleaned` | `streamDomainerGtldCleaned` |
| Databases | Databases - Streaming | GET | `/v3.3/stream/domainer/gtld/cleaned/email` | `streamDomainerGtldCleanedEmail` |
| Databases | Databases - Streaming | GET | `/v3.3/stream/domainer/gtld/cleaned/phone` | `streamDomainerGtldCleanedPhone` |
| Databases | Databases - Streaming | GET | `/v3.3/stream/domainer/cctld` | `streamDomainerCctld` |
| Databases | Databases - Streaming | GET | `/v3.3/stream/domainer/cctld/cleaned` | `streamDomainerCctldCleaned` |
| Databases | Databases - Streaming | GET | `/v3.3/stream/domainer/cctld/cleaned/email` | `streamDomainerCctldCleanedEmail` |
| Databases | Databases - Streaming | GET | `/v3.3/stream/domainer/cctld/cleaned/phone` | `streamDomainerCctldCleanedPhone` |
| Databases | Databases - Streaming | GET | `/v3.3/stream/domainer/expired` | `streamDomainerExpired` |
| Databases | Databases - Streaming | GET | `/v3.3/stream/domainer/expired/cleaned` | `streamDomainerExpiredCleaned` |
| Databases | Databases - Streaming | GET | `/v3.3/stream/domainer/expired/cleaned/email` | `streamDomainerExpiredCleanedEmail` |
| Databases | Databases - Streaming | GET | `/v3.3/stream/domainer/expired/cleaned/phone` | `streamDomainerExpiredCleanedPhone` |
| Databases | Databases - Streaming | GET | `/v3.3/stream/domainer/dropped` | `streamDomainerDropped` |
| Databases | Databases - Streaming | GET | `/v3.3/stream/domainer/dropped/backlinks` | `streamDomainerDroppedBacklinks` |
| Databases | Databases - Streaming | GET | `/v3.3/stream/domainer/sample/gtld` | `streamDomainerGtldSample` |
| Databases | Databases - Streaming | GET | `/v3.3/stream/domainer/sample/gtld/cleaned` | `streamDomainerGtldCleanedSample` |
| Databases | Databases - Streaming | GET | `/v3.3/stream/domainer/sample/cctld` | `streamDomainerCctldSample` |
| Databases | Databases - Streaming | GET | `/v3.3/stream/domainer/sample/cctld/cleaned` | `streamDomainerCctldCleanedSample` |
| Databases | Databases - Streaming | GET | `/v3.3/stream/domainer/sample/expired` | `streamDomainerExpiredSample` |
| Databases | Databases - Streaming | GET | `/v3.3/stream/domainer/sample/expired/cleaned` | `streamDomainerExpiredCleanedSample` |
| Databases | Databases - Streaming | GET | `/v3.3/stream/domainer/sample/dropped` | `streamDomainerDroppedSample` |
| Databases | Databases - Streaming | GET | `/v3.3/stream/domainer/sample/dropped/backlinks` | `streamDomainerDroppedBacklinksSample` |
