# Databases

Bulk data feeds and downloadable database snapshots for large-scale processing: newly registered, expiring/dropped, and full WHOIS/DNS/IP datasets.

**65 endpoints** across **11 categories**. Requests need your API key unless noted otherwise. See [Authentication](../authentication.md).

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

### [Databases - Streaming](databases-streaming.md)

Stream database files and threat feeds as plain CSV text instead of downloading a gzip file

28 endpoints:

- **Stream the daily phishing threat feed (CSV)**: `GET /v3.4/stream/threat-feed/phishing`
- **Stream a sample of the phishing threat feed (CSV)**: `GET /v3.4/stream/threat-feed/phishing/sample`
- **Stream the daily malware threat feed (CSV)**: `GET /v3.4/stream/threat-feed/malware`
- **Stream a sample of the malware threat feed (CSV)**: `GET /v3.4/stream/threat-feed/malware/sample`
- **Stream the daily spam threat feed (CSV)**: `GET /v3.4/stream/threat-feed/spam`
- **Stream a sample of the spam threat feed (CSV)**: `GET /v3.4/stream/threat-feed/spam/sample`
- **Stream newly registered gTLD domains (CSV)**: `GET /v3.3/stream/domainer/gtld`
- **Stream cleaned newly registered gTLD domains (CSV)**: `GET /v3.3/stream/domainer/gtld/cleaned`
- **Stream cleaned newly registered gTLD domains with an email (CSV)**: `GET /v3.3/stream/domainer/gtld/cleaned/email`
- **Stream cleaned newly registered gTLD domains with a phone (CSV)**: `GET /v3.3/stream/domainer/gtld/cleaned/phone`
- **Stream newly registered ccTLD domains (CSV)**: `GET /v3.3/stream/domainer/cctld`
- **Stream cleaned newly registered ccTLD domains (CSV)**: `GET /v3.3/stream/domainer/cctld/cleaned`
- **Stream cleaned newly registered ccTLD domains with an email (CSV)**: `GET /v3.3/stream/domainer/cctld/cleaned/email`
- **Stream cleaned newly registered ccTLD domains with a phone (CSV)**: `GET /v3.3/stream/domainer/cctld/cleaned/phone`
- **Stream expiring domains (CSV)**: `GET /v3.3/stream/domainer/expired`
- **Stream cleaned expiring domains (CSV)**: `GET /v3.3/stream/domainer/expired/cleaned`
- **Stream cleaned expiring domains with an email (CSV)**: `GET /v3.3/stream/domainer/expired/cleaned/email`
- **Stream cleaned expiring domains with a phone (CSV)**: `GET /v3.3/stream/domainer/expired/cleaned/phone`
- **Stream dropped domains (CSV)**: `GET /v3.3/stream/domainer/dropped`
- **Stream dropped domains with backlinks (CSV)**: `GET /v3.3/stream/domainer/dropped/backlinks`
- **Stream a sample of newly registered gTLD domains (CSV)**: `GET /v3.3/stream/domainer/sample/gtld`
- **Stream a sample of cleaned newly registered gTLD domains (CSV)**: `GET /v3.3/stream/domainer/sample/gtld/cleaned`
- **Stream a sample of newly registered ccTLD domains (CSV)**: `GET /v3.3/stream/domainer/sample/cctld`
- **Stream a sample of cleaned newly registered ccTLD domains (CSV)**: `GET /v3.3/stream/domainer/sample/cctld/cleaned`
- **Stream a sample of expiring domains (CSV)**: `GET /v3.3/stream/domainer/sample/expired`
- **Stream a sample of cleaned expiring domains (CSV)**: `GET /v3.3/stream/domainer/sample/expired/cleaned`
- **Stream a sample of dropped domains (CSV)**: `GET /v3.3/stream/domainer/sample/dropped`
- **Stream a sample of dropped domains with backlinks (CSV)**: `GET /v3.3/stream/domainer/sample/dropped/backlinks`
