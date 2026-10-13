# Databases

Bulk data feeds and downloadable database snapshots for large-scale processing: newly registered, expiring/dropped, and full WHOIS/DNS/IP datasets.

**37 endpoints** across **10 categories**. Requests need your API key unless noted otherwise. See [Authentication](../authentication.md).

## Categories

### [Databases - Newly Registered](databases-newly-registered.md)

Newly registered domain downloads

7 endpoints:

- **Newly Registered gTLD (CSV)**: `GET /v3.1/download/domainer/gtld`
- **Newly Registered ccTLD (CSV)**: `GET /v3.1/download/domainer/cctld`
- **Newly Registered gTLD Cleaned WHOIS (CSV)**: `GET /v3.1/download/domainer/gtld/cleaned`
- **Newly Registered ccTLD Cleaned WHOIS (CSV)**: `GET /v3.1/download/domainer/cctld/cleaned`
- **Newly Registered gTLD (JSON)**: `GET /v3.1/domains/newly/gtld`
- **Newly Registered ccTLD (JSON)**: `GET /v3.1/domains/newly/cctld`
- **Newly Registered With DNS**: `GET /v3.1/download/domainer/newly/dns`

### [Databases - Expiring & Dropped](databases-expiring-dropped.md)

Expiring and dropped domain downloads

5 endpoints:

- **Expiring Domains**: `GET /v3.1/download/domainer/expired`
- **Expiring Cleaned WHOIS**: `GET /v3.1/download/domainer/expired/cleaned`
- **Dropped Domains**: `GET /v3.1/download/domainer/dropped`
- **Dropped Domains (JSON)**: `GET /v3.1/domains/dropped`
- **Dropped With Backlinks**: `GET /v3.3/download/domainer/dropped/backlinks`

### [Databases - WHOIS](databases-whois.md)

WHOIS database snapshots

3 endpoints:

- **WHOIS Database Daily**: `GET /v3.3/download/dbupdate/daily/domains/whois`
- **WHOIS Database Weekly**: `GET /v3.3/download/dbupdate/weekly/domains/whois`
- **WHOIS Database Monthly**: `GET /v3.3/download/dbupdate/monthly/domains/whois`

### [Databases - DNS](databases-dns.md)

DNS database snapshots

3 endpoints:

- **DNS Database Daily**: `GET /v3.2/download/dbupdate/daily/dns`
- **DNS Database Weekly**: `GET /v3.2/download/dbupdate/weekly/dns`
- **DNS Database Monthly**: `GET /v3.2/download/dbupdate/monthly/dns`

### [Databases - Subdomains](databases-subdomains.md)

Subdomain database snapshots

3 endpoints:

- **Subdomains Daily**: `GET /v3.2/download/dbupdate/daily/subdomains`
- **Subdomains Weekly**: `GET /v3.2/download/dbupdate/weekly/subdomains`
- **Subdomains Monthly**: `GET /v3.2/download/dbupdate/monthly/subdomains`

### [Databases - IP Geolocation](databases-ip-geolocation.md)

IP geolocation database snapshots

4 endpoints:

- **IP to Country Snapshot Status**: `GET /v3.3/status/snapshot/ip/country`
- **IP to Country Snapshot**: `GET /v3.3/download/snapshot/ip/country`
- **IP to City Snapshot Status**: `GET /v3.3/status/snapshot/ip/city`
- **IP to City Snapshot**: `GET /v3.3/download/snapshot/ip/city`

### [Databases - ASN WHOIS](databases-asn-whois.md)

ASN WHOIS database snapshots

2 endpoints:

- **ASN WHOIS Snapshot**: `GET /v3.3/download/snapshot/asn/whois`
- **ASN WHOIS Snapshot Status**: `GET /v3.3/status/snapshot/asn/whois`

### [Databases - IP WHOIS](databases-ip-whois.md)

IP WHOIS database snapshots

2 endpoints:

- **IP WHOIS Snapshot**: `GET /v3.3/download/snapshot/ip/whois`
- **IP WHOIS Snapshot Status**: `GET /v3.3/status/snapshot/ip/whois`

### [Databases - IP Security](databases-ip-security.md)

IP security database snapshots

2 endpoints:

- **IP Security Snapshot**: `GET /v3.3/download/snapshot/ip/security`
- **IP Security Snapshot Status**: `GET /v3.3/status/snapshot/ip/security`

### [Databases - Threat Feed](databases-threat-feed.md)

Daily phishing, malware and spam threat feeds

6 endpoints:

- **Download the daily phishing threat feed (CSV)**: `GET /v3.4/download/threat-feed/phishing`
- **Download a sample of the phishing threat feed (CSV)**: `GET /v3.4/download/threat-feed/phishing/sample`
- **Download the daily malware threat feed (CSV)**: `GET /v3.4/download/threat-feed/malware`
- **Download a sample of the malware threat feed (CSV)**: `GET /v3.4/download/threat-feed/malware/sample`
- **Download the daily spam threat feed (CSV)**: `GET /v3.4/download/threat-feed/spam`
- **Download a sample of the spam threat feed (CSV)**: `GET /v3.4/download/threat-feed/spam/sample`
