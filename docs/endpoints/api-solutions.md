# API Solutions

Real-time and on-demand lookup APIs. Query a single domain, IP, or ASN and get structured JSON (or XML) back immediately.

**20 endpoints** across **11 categories**. Requests need your API key unless noted otherwise. See [Authentication](../authentication.md).

## Categories

### [WHOIS](whois.md)

WHOIS lookup APIs (live, historical, reverse, bulk)

4 endpoints:

- **Live WHOIS Lookup**: `GET /v2.0/whois/live`
- **Bulk WHOIS Lookup**: `POST /v2.0/bulkwhois/live`
- **Historical WHOIS records for a domain**: `GET /v2.0/whois/history`
- **Reverse WHOIS lookup by keyword**: `GET /v2.0/whois/reverse`

### [DNS](dns.md)

DNS lookup APIs (live, historical, reverse, bulk)

4 endpoints:

- **Live DNS Lookup**: `GET /v2.0/dns/live`
- **Historical DNS Lookup**: `GET /v2.0/dns/historical`
- **Reverse DNS Lookup**: `GET /v2.1/dns/reverse`
- **Bulk DNS Lookup**: `POST /v2.0/dns/bulk/live`

### [Domain Availability](domain-availability.md)

Check domain availability

2 endpoints:

- **Domain Availability Check with Suggestions**: `GET /v2.0/domain/availability`
- **Bulk Domain Availability Check**: `POST /v2.0/domain/availability`

### [Typosquatting](typosquatting.md)

Detect typo variants of brand domains

1 endpoint:

- **Typosquatting Lookup**: `GET /v3.0/domain/typos`

### [SSL](ssl.md)

SSL certificate lookup

1 endpoint:

- **SSL Certificate Lookup**: `GET /v1.0/ssl/live`

### [Geolocation](geolocation.md)

IP geolocation lookup

2 endpoints:

- **IP Geolocation Lookup**: `GET /v1.0/geolocation`
- **Bulk IP Geolocation**: `POST /v1.0/geolocation`

### [Subdomains](subdomains.md)

Subdomain enumeration

1 endpoint:

- **Subdomains Lookup**: `GET /v1.0/subdomains`

### [IP Reputation](ip-reputation.md)

IP threat intelligence

2 endpoints:

- **IP Reputation Lookup**: `GET /v1.0/security`
- **Bulk IP Reputation**: `POST /v1.0/security`

### [Domain Reputation](domain-reputation.md)

Real-time domain threat assessment and trust scoring

1 endpoint:

- **Domain Reputation Lookup**: `GET /v1/domain/security`

### [ASN WHOIS](asn-whois.md)

Autonomous System Number WHOIS

1 endpoint:

- **ASN WHOIS Lookup**: `GET /v2.0/asn-whois`

### [IP WHOIS](ip-whois.md)

IP address WHOIS

1 endpoint:

- **IP WHOIS Lookup**: `GET /v1.0/ip-whois`
