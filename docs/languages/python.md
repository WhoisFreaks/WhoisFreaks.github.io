# Python SDK

## About

The official **WhoisFreaks Python SDK**: a complete client for WHOIS, DNS, SSL, domain availability, subdomain, IP geolocation, IP reputation, ASN, typosquatting, and domain reputation lookups, plus bulk database downloads. Query real-time and historical domain data, reverse WHOIS, and threat intelligence from Python with a single API key. Generated from the WhoisFreaks OpenAPI specification and published to PyPI.

**Keywords:** python whois api, python whois sdk, whoisfreaks python, python domain lookup, python dns api, whois api, whois lookup, domain api, dns api, dns lookup, reverse whois, historical whois, domain availability api, ssl certificate api, ip geolocation api, ip reputation api, asn lookup, subdomain finder, typosquatting api, domain reputation, threat intelligence api, domain data api, whois sdk, domain monitoring, brand protection api

- **Registry:** PyPI
- **Package:** `whoisfreaks`

## Install

```bash
pip install whoisfreaks
```

## Build from Source

Prefer to build the SDK yourself instead of installing from PyPI? Clone the Python SDK repository and build it locally:

```bash
git clone https://github.com/WhoisFreaks/whoisfreaks-python
cd whoisfreaks-python
pip install -e .   # editable local install
```

## Getting Started

A complete walkthrough from an empty directory to a running program:

1. Create a project folder with a virtual environment and install the SDK:

```bash
mkdir whoisfreaks-test && cd whoisfreaks-test
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install whoisfreaks
```

2. Create `main.py`:

```python
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    record = whoisfreaks.WHOISApi(client).whois_live("whoisfreaks.com")
    print("Domain: ", record.domain_name)
    print("Created:", record.create_date)
    print("Expires:", record.expiry_date)
```

3. Set your API key and run it:

```bash
export WHOISFREAKS_API_KEY="your_api_key"   # PowerShell: $env:WHOISFREAKS_API_KEY="your_api_key"
python main.py
```

## Configure

See [Authentication](../authentication.md) for how to obtain a key. Minimal setup:

```python
"""Live WHOIS Lookup: GET https://api.whoisfreaks.com/v2.0/whois/live

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python WhoisLive.py
"""
import json
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.WHOISApi(client)

    # whois_live parameters:
    #   domain_name (str, required)
    #   format (str, optional, keyword): one of json, xml; default "json"
    result = api.whois_live("whoisfreaks.com")
    print(json.dumps(result.to_dict(), indent=2))
```

## Endpoints

All 60 endpoints are shown below, grouped by category. Each includes its method, path, parameters, and a runnable example. See the [full endpoint reference](../endpoints/README.md) for response shapes and field details.

### WHOIS

#### Live WHOIS Lookup

`GET /v2.0/whois/live`

```python
"""Live WHOIS Lookup: GET https://api.whoisfreaks.com/v2.0/whois/live

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python WhoisLive.py
"""
import json
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.WHOISApi(client)

    # whois_live parameters:
    #   domain_name (str, required)
    #   format (str, optional, keyword): one of json, xml; default "json"
    result = api.whois_live("whoisfreaks.com")
    print(json.dumps(result.to_dict(), indent=2))
```

#### Bulk WHOIS Lookup

`POST /v2.0/bulkwhois/live`

```python
"""Bulk WHOIS Lookup: POST https://api.whoisfreaks.com/v2.0/bulkwhois/live

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python BulkWhois.py
"""
import json
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.WHOISApi(client)

    # bulk_whois parameters:
    #   bulk_whois_request (BulkWhoisRequest, required): request body
    #   format (str, optional, keyword): one of json, xml; default "json"
    body = whoisfreaks.BulkWhoisRequest(domain_names=["whoisfreaks.com", "jfreaks.com"])
    result = api.bulk_whois(body)
    print(json.dumps(result.to_dict(), indent=2))
```

#### Historical WHOIS records for a domain

`GET /v2.0/whois/history`

```python
"""Historical WHOIS records for a domain: GET https://api.whoisfreaks.com/v2.0/whois/history

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python WhoisHistory.py
"""
import json
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.WHOISApi(client)

    # whois_history parameters:
    #   domain_name (str, required): Domain to fetch historical WHOIS records for
    #   format (str, optional, keyword): one of json, xml
    result = api.whois_history("whoisfreaks.com")
    print(json.dumps(result.to_dict(), indent=2))
```

#### Reverse WHOIS lookup by keyword

`GET /v2.0/whois/reverse`

```python
"""Reverse WHOIS lookup by keyword: GET https://api.whoisfreaks.com/v2.0/whois/reverse

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python WhoisReverse.py
"""
import json
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.WHOISApi(client)

    # whois_reverse parameters:
    #   keyword (str, required): Keyword to search across WHOIS records
    #   page (int, optional, keyword): Page number
    #   format (str, optional, keyword): one of json, xml
    result = api.whois_reverse("whoisfreaks", page=1)
    print(json.dumps(result.to_dict(), indent=2))
```

### DNS

#### Live DNS Lookup

`GET /v2.0/dns/live`

```python
"""Live DNS Lookup: GET https://api.whoisfreaks.com/v2.0/dns/live

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DnsLive.py
"""
import json
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DNSApi(client)

    # dns_live parameters:
    #   type (str, required): all or comma-separated: A,MX,NS,TXT,SOA,SPF,AAAA,CNAME; default "all"
    #   domain_name (str, optional, keyword)
    #   ip_address (str, optional, keyword): Use for PTR lookups
    #   format (str, optional, keyword): one of json, xml; default "json"
    result = api.dns_live("A,MX,TXT", domain_name="whoisfreaks.com")
    print(json.dumps(result.to_dict(), indent=2))
```

#### Historical DNS Lookup

`GET /v2.0/dns/historical`

```python
"""Historical DNS Lookup: GET https://api.whoisfreaks.com/v2.0/dns/historical

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DnsHistorical.py
"""
import json
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DNSApi(client)

    # dns_historical parameters:
    #   domain_name (str, required)
    #   type (str, required): default "all"
    #   page (int, optional, keyword): default 1
    #   format (str, optional, keyword): one of json, xml; default "json"
    result = api.dns_historical("whoisfreaks.com", "A,MX,TXT", page=1)
    print(json.dumps(result.to_dict(), indent=2))
```

#### Reverse DNS Lookup

`GET /v2.1/dns/reverse`

```python
"""Reverse DNS Lookup: GET https://api.whoisfreaks.com/v2.1/dns/reverse

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DnsReverse.py
"""
import json
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DNSApi(client)

    # dns_reverse parameters:
    #   value (str, required): IP, CIDR, or record value
    #   type (str, required): one of a, mx, cname, ns, aaaa, txt, soa
    #   exact (bool, optional, keyword): default True
    #   page (int, optional, keyword): default 1
    #   format (str, optional, keyword): one of json, xml; default "json"
    result = api.dns_reverse("8.8.8.8", "a", page=1)
    print(json.dumps(result.to_dict(), indent=2))
```

#### Bulk DNS Lookup

`POST /v2.0/dns/bulk/live`

```python
"""Bulk DNS Lookup: POST https://api.whoisfreaks.com/v2.0/dns/bulk/live

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DnsBulk.py
"""
import json
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DNSApi(client)

    # dns_bulk parameters:
    #   type (str, required): default "all"
    #   dns_bulk_request (DnsBulkRequest, required): request body
    #   format (str, optional, keyword): one of json, xml; default "json"
    body = whoisfreaks.DnsBulkRequest(domain_names=["whoisfreaks.com", "example.com"])
    result = api.dns_bulk("A,MX,TXT", body)
    print(json.dumps(result.to_dict(), indent=2))
```

### Domain Availability

#### Domain Availability Check with Suggestions

`GET /v2.0/domain/availability`

```python
"""Domain Availability Check with Suggestions: GET https://api.whoisfreaks.com/v2.0/domain/availability

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DomainAvailabilityV2.py
"""
import json
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DomainAvailabilityApi(client)

    # domain_availability_v2 parameters:
    #   domain (str, required): The domain name to check
    #   sug (bool, optional, keyword): Whether to return TLD suggestions alongside the queried domain; default False
    #   count (int, optional, keyword): Number of TLD suggestions to return when sug=true. Maximum is 100; default 5
    #   format (str, optional, keyword): one of json, xml; default "json"
    result = api.domain_availability_v2("google.com", sug=True, count=5)
    print(json.dumps(result.to_dict(), indent=2))
```

#### Bulk Domain Availability Check

`POST /v2.0/domain/availability`

```python
"""Bulk Domain Availability Check: POST https://api.whoisfreaks.com/v2.0/domain/availability

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python BulkDomainAvailabilityV2.py
"""
import json
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DomainAvailabilityApi(client)

    # bulk_domain_availability_v2 parameters:
    #   bulk_domain_availability_request (BulkDomainAvailabilityRequest, required): request body
    #   domain (str, optional, keyword): Required for TLD-mode bulk check (base domain)
    #   format (str, optional, keyword): one of json, xml; default "json"
    body = whoisfreaks.BulkDomainAvailabilityRequest(domain_names=["whoisfreaks.com", "example.com"])
    result = api.bulk_domain_availability_v2(body)
    print(json.dumps(result.to_dict(), indent=2))
```

### Typosquatting

#### Typosquatting Lookup

`GET /v3.0/domain/typos`

```python
"""Typosquatting Lookup: GET https://api.whoisfreaks.com/v3.0/domain/typos

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python Typosquatting.py
"""
import json
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.TyposquattingApi(client)

    # typosquatting parameters:
    #   keyword (str, optional, keyword)
    #   pattern (str, optional, keyword)
    #   page_token (str, optional, keyword)
    result = api.typosquatting(keyword="whoisfreaks")
    print(json.dumps(result.to_dict(), indent=2))
```

### SSL

#### SSL Certificate Lookup

`GET /v1.0/ssl/live`

```python
"""SSL Certificate Lookup: GET https://api.whoisfreaks.com/v1.0/ssl/live

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python SslLookup.py
"""
import json
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.SSLApi(client)

    # ssl_lookup parameters:
    #   domain_name (str, required)
    #   chain (bool, optional, keyword): default False
    #   ssl_raw (bool, optional, keyword): default False
    #   format (str, optional, keyword): one of json, xml; default "json"
    result = api.ssl_lookup("whoisfreaks.com")
    print(json.dumps(result.to_dict(), indent=2))
```

### Geolocation

#### IP Geolocation Lookup

`GET /v1.0/geolocation`

```python
"""IP Geolocation Lookup: GET https://api.whoisfreaks.com/v1.0/geolocation

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python Geolocation.py
"""
import json
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.GeolocationApi(client)

    # geolocation parameters:
    #   ip (str, required)
    result = api.geolocation("8.8.8.8")
    print(json.dumps(result.to_dict(), indent=2))
```

#### Bulk IP Geolocation

`POST /v1.0/geolocation`

```python
"""Bulk IP Geolocation: POST https://api.whoisfreaks.com/v1.0/geolocation

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python BulkGeolocation.py
"""
import json
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.GeolocationApi(client)

    # bulk_geolocation parameters:
    #   bulk_geolocation_request (BulkGeolocationRequest, required): request body
    body = whoisfreaks.BulkGeolocationRequest(ips=["8.8.8.8", "1.1.1.1"])
    results = api.bulk_geolocation(body)
    print(json.dumps([item.to_dict() for item in results], indent=2))
```

### Subdomains

#### Subdomains Lookup

`GET /v1.0/subdomains`

```python
"""Subdomains Lookup: GET https://api.whoisfreaks.com/v1.0/subdomains

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python Subdomains.py
"""
import json
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.SubdomainsApi(client)

    # subdomains parameters:
    #   domain (str, required)
    #   after (datetime.date, optional, keyword)
    #   before (datetime.date, optional, keyword)
    #   status (str, optional, keyword): one of active, inactive
    #   page (int, optional, keyword): default 1
    #   format (str, optional, keyword): one of json, xml; default "json"
    result = api.subdomains("whoisfreaks.com", page=1)
    print(json.dumps(result.to_dict(), indent=2))
```

### IP Reputation

#### IP Reputation Lookup

`GET /v1.0/security`

```python
"""IP Reputation Lookup: GET https://api.whoisfreaks.com/v1.0/security

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python IpReputation.py
"""
import json
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.IPReputationApi(client)

    # ip_reputation parameters:
    #   ip (str, required)
    result = api.ip_reputation("8.8.8.8")
    print(json.dumps(result.to_dict(), indent=2))
```

#### Bulk IP Reputation

`POST /v1.0/security`

```python
"""Bulk IP Reputation: POST https://api.whoisfreaks.com/v1.0/security

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python BulkIpReputation.py
"""
import json
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.IPReputationApi(client)

    # bulk_ip_reputation parameters:
    #   bulk_geolocation_request (BulkGeolocationRequest, required): request body
    body = whoisfreaks.BulkGeolocationRequest(ips=["8.8.8.8", "1.1.1.1"])
    results = api.bulk_ip_reputation(body)
    print(json.dumps([item.to_dict() for item in results], indent=2))
```

### Domain Reputation

#### Domain Reputation Lookup

`GET /v1/domain/security`

```python
"""Domain Reputation Lookup: GET https://api.whoisfreaks.com/v1/domain/security

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DomainReputation.py
"""
import json
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DomainReputationApi(client)

    # domain_reputation parameters:
    #   domain_name (str, required): The domain name to assess
    #   format (str, optional, keyword): one of json, xml; default "json"
    result = api.domain_reputation("amazon.com")
    print(json.dumps(result.to_dict(), indent=2))
```

### ASN WHOIS

#### ASN WHOIS Lookup

`GET /v2.0/asn-whois`

```python
"""ASN WHOIS Lookup: GET https://api.whoisfreaks.com/v2.0/asn-whois

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python AsnWhois.py
"""
import json
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.ASNWHOISApi(client)

    # asn_whois parameters:
    #   asn (str, required)
    #   format (str, optional, keyword): one of json, xml; default "json"
    result = api.asn_whois("as15169")
    print(json.dumps(result.to_dict(), indent=2))
```

### IP WHOIS

#### IP WHOIS Lookup

`GET /v1.0/ip-whois`

```python
"""IP WHOIS Lookup: GET https://api.whoisfreaks.com/v1.0/ip-whois

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python IpWhois.py
"""
import json
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.IPWHOISApi(client)

    # ip_whois parameters:
    #   ip (str, required)
    #   format (str, optional, keyword): one of json, xml; default "json"
    result = api.ip_whois("8.8.8.8")
    print(json.dumps(result.to_dict(), indent=2))
```

### Account

#### Rotate API Key

`GET /v1.0/api-key/rotate`

```python
"""Rotate API Key: GET https://api.whoisfreaks.com/v1.0/api-key/rotate

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python RotateApiKey.py
"""
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.AccountApi(client)

    # rotate_api_key takes no parameters.
    new_key = api.rotate_api_key()  # use this key from now on
    print("New API key:", new_key)
```

#### Account Usage

`GET /v1.0/whoisapi/usage`

```python
"""Account Usage: GET https://api.whoisfreaks.com/v1.0/whoisapi/usage

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python AccountUsage.py
"""
import json
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.AccountApi(client)

    # account_usage takes no parameters.
    result = api.account_usage()
    print(json.dumps(result.to_dict(), indent=2))
```

#### Database File Status (Public)

`GET /v3.4/status`

```python
"""Database File Status (Public): GET https://files.whoisfreaks.com/v3.4/status

Run it (public endpoint, no API key needed):
    python DatabaseFileStatus.py
"""
import json

import whoisfreaks

config = whoisfreaks.Configuration()
# Public endpoint: no API key needed.

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.AccountApi(client)

    # database_file_status takes no parameters.
    result = api.database_file_status()
    print(json.dumps(result.to_dict(), indent=2))
```

### Databases - Newly Registered

#### Newly Registered gTLD (CSV)

`GET /v3.1/download/domainer/gtld`

```python
"""Newly Registered gTLD (CSV): GET https://files.whoisfreaks.com/v3.1/download/domainer/gtld

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DbNewlyGtld.py
"""
import os
from datetime import date

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesNewlyRegisteredApi(client)

    # db_newly_gtld parameters:
    #   whois (bool, required)
    #   var_date (datetime.date, optional, keyword): yyyy-MM-dd; omit for latest
    #   tlds (str, optional, keyword)
    data = api.db_newly_gtld(True, var_date=date(2026, 10, 1))  # the file's raw bytes
    path = "DbNewlyGtld.csv"
    with open(path, "wb") as f:
        f.write(data)
    print(f"Saved {len(data)} bytes to {os.path.abspath(path)}")
```

#### Newly Registered ccTLD (CSV)

`GET /v3.1/download/domainer/cctld`

```python
"""Newly Registered ccTLD (CSV): GET https://files.whoisfreaks.com/v3.1/download/domainer/cctld

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DbNewlyCctld.py
"""
import os
from datetime import date

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesNewlyRegisteredApi(client)

    # db_newly_cctld parameters:
    #   whois (bool, required)
    #   var_date (datetime.date, optional, keyword): yyyy-MM-dd; omit for latest
    #   tlds (str, optional, keyword)
    data = api.db_newly_cctld(True, var_date=date(2026, 10, 1))  # the file's raw bytes
    path = "DbNewlyCctld.csv"
    with open(path, "wb") as f:
        f.write(data)
    print(f"Saved {len(data)} bytes to {os.path.abspath(path)}")
```

#### Newly Registered gTLD Cleaned WHOIS (CSV)

`GET /v3.1/download/domainer/gtld/cleaned`

```python
"""Newly Registered gTLD Cleaned WHOIS (CSV): GET https://files.whoisfreaks.com/v3.1/download/domainer/gtld/cleaned

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DbNewlyGtldCleaned.py
"""
import os
from datetime import date

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesNewlyRegisteredApi(client)

    # db_newly_gtld_cleaned parameters:
    #   var_date (datetime.date, optional, keyword): yyyy-MM-dd; omit for latest
    data = api.db_newly_gtld_cleaned(var_date=date(2026, 10, 1))  # the file's raw bytes
    path = "DbNewlyGtldCleaned.csv"
    with open(path, "wb") as f:
        f.write(data)
    print(f"Saved {len(data)} bytes to {os.path.abspath(path)}")
```

#### Newly Registered ccTLD Cleaned WHOIS (CSV)

`GET /v3.1/download/domainer/cctld/cleaned`

```python
"""Newly Registered ccTLD Cleaned WHOIS (CSV): GET https://files.whoisfreaks.com/v3.1/download/domainer/cctld/cleaned

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DbNewlyCctldCleaned.py
"""
import os
from datetime import date

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesNewlyRegisteredApi(client)

    # db_newly_cctld_cleaned parameters:
    #   var_date (datetime.date, optional, keyword): yyyy-MM-dd; omit for latest
    data = api.db_newly_cctld_cleaned(var_date=date(2026, 10, 1))  # the file's raw bytes
    path = "DbNewlyCctldCleaned.csv"
    with open(path, "wb") as f:
        f.write(data)
    print(f"Saved {len(data)} bytes to {os.path.abspath(path)}")
```

#### Newly Registered gTLD (JSON)

`GET /v3.1/domains/newly/gtld`

```python
"""Newly Registered gTLD (JSON): GET https://files.whoisfreaks.com/v3.1/domains/newly/gtld

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DbNewlyGtldJson.py
"""
import os
from datetime import date

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesNewlyRegisteredApi(client)

    # db_newly_gtld_json parameters:
    #   var_date (datetime.date, optional, keyword): yyyy-MM-dd; omit for latest
    #   tlds (str, optional, keyword)
    domains = api.db_newly_gtld_json(var_date=date(2026, 10, 1))
    print(f"{len(domains)} domains")
    print("\n".join(domains[:10]))
```

#### Newly Registered ccTLD (JSON)

`GET /v3.1/domains/newly/cctld`

```python
"""Newly Registered ccTLD (JSON): GET https://files.whoisfreaks.com/v3.1/domains/newly/cctld

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DbNewlyCctldJson.py
"""
import os
from datetime import date

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesNewlyRegisteredApi(client)

    # db_newly_cctld_json parameters:
    #   var_date (datetime.date, optional, keyword): yyyy-MM-dd; omit for latest
    #   tlds (str, optional, keyword)
    domains = api.db_newly_cctld_json(var_date=date(2026, 10, 1))
    print(f"{len(domains)} domains")
    print("\n".join(domains[:10]))
```

#### Newly Registered With DNS

`GET /v3.1/download/domainer/newly/dns`

```python
"""Newly Registered With DNS: GET https://files.whoisfreaks.com/v3.1/download/domainer/newly/dns

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DbNewlyDns.py
"""
import os
from datetime import date

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesNewlyRegisteredApi(client)

    # db_newly_dns parameters:
    #   var_date (datetime.date, optional, keyword): yyyy-MM-dd; omit for latest
    data = api.db_newly_dns(var_date=date(2026, 10, 1))  # the file's raw bytes
    path = "DbNewlyDns.json"
    with open(path, "wb") as f:
        f.write(data)
    print(f"Saved {len(data)} bytes to {os.path.abspath(path)}")
```

### Databases - Expiring & Dropped

#### Expiring Domains

`GET /v3.1/download/domainer/expired`

```python
"""Expiring Domains: GET https://files.whoisfreaks.com/v3.1/download/domainer/expired

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DbExpired.py
"""
import os
from datetime import date

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesExpiringDroppedApi(client)

    # db_expired parameters:
    #   whois (bool, required)
    #   var_date (datetime.date, optional, keyword): yyyy-MM-dd; omit for latest
    data = api.db_expired(True, var_date=date(2026, 10, 1))  # the file's raw bytes
    path = "DbExpired.csv"
    with open(path, "wb") as f:
        f.write(data)
    print(f"Saved {len(data)} bytes to {os.path.abspath(path)}")
```

#### Expiring Cleaned WHOIS

`GET /v3.1/download/domainer/expired/cleaned`

```python
"""Expiring Cleaned WHOIS: GET https://files.whoisfreaks.com/v3.1/download/domainer/expired/cleaned

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DbExpiredCleaned.py
"""
import os
from datetime import date

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesExpiringDroppedApi(client)

    # db_expired_cleaned parameters:
    #   var_date (datetime.date, optional, keyword): yyyy-MM-dd; omit for latest
    data = api.db_expired_cleaned(var_date=date(2026, 10, 1))  # the file's raw bytes
    path = "DbExpiredCleaned.csv"
    with open(path, "wb") as f:
        f.write(data)
    print(f"Saved {len(data)} bytes to {os.path.abspath(path)}")
```

#### Dropped Domains

`GET /v3.1/download/domainer/dropped`

```python
"""Dropped Domains: GET https://files.whoisfreaks.com/v3.1/download/domainer/dropped

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DbDropped.py
"""
import os
from datetime import date

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesExpiringDroppedApi(client)

    # db_dropped parameters:
    #   whois (bool, required)
    #   var_date (datetime.date, optional, keyword): yyyy-MM-dd; omit for latest
    data = api.db_dropped(True, var_date=date(2026, 10, 1))  # the file's raw bytes
    path = "DbDropped.csv"
    with open(path, "wb") as f:
        f.write(data)
    print(f"Saved {len(data)} bytes to {os.path.abspath(path)}")
```

#### Dropped Domains (JSON)

`GET /v3.1/domains/dropped`

```python
"""Dropped Domains (JSON): GET https://files.whoisfreaks.com/v3.1/domains/dropped

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DbDroppedJson.py
"""
import os
from datetime import date

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesExpiringDroppedApi(client)

    # db_dropped_json parameters:
    #   var_date (datetime.date, optional, keyword): yyyy-MM-dd; omit for latest
    #   tlds (str, optional, keyword)
    domains = api.db_dropped_json(var_date=date(2026, 10, 1))
    print(f"{len(domains)} domains")
    print("\n".join(domains[:10]))
```

#### Dropped With Backlinks

`GET /v3.3/download/domainer/dropped/backlinks`

```python
"""Dropped With Backlinks: GET https://files.whoisfreaks.com/v3.3/download/domainer/dropped/backlinks

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DbDroppedBacklinks.py
"""
import os
from datetime import date

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesExpiringDroppedApi(client)

    # db_dropped_backlinks parameters:
    #   whois (bool, optional, keyword)
    #   var_date (datetime.date, optional, keyword): yyyy-MM-dd; omit for latest
    data = api.db_dropped_backlinks(var_date=date(2026, 10, 1))  # the file's raw bytes
    path = "DbDroppedBacklinks.csv"
    with open(path, "wb") as f:
        f.write(data)
    print(f"Saved {len(data)} bytes to {os.path.abspath(path)}")
```

### Databases - WHOIS

#### WHOIS Database Daily

`GET /v3.3/download/dbupdate/daily/domains/whois`

```python
"""WHOIS Database Daily: GET https://files.whoisfreaks.com/v3.3/download/dbupdate/daily/domains/whois

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DbWhoisDaily.py
"""
import os
from datetime import date

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesWHOISApi(client)

    # db_whois_daily parameters:
    #   var_date (datetime.date, optional, keyword): yyyy-MM-dd; omit for latest
    data = api.db_whois_daily(var_date=date(2026, 10, 1))  # the file's raw bytes
    path = "DbWhoisDaily.csv"
    with open(path, "wb") as f:
        f.write(data)
    print(f"Saved {len(data)} bytes to {os.path.abspath(path)}")
```

#### WHOIS Database Weekly

`GET /v3.3/download/dbupdate/weekly/domains/whois`

```python
"""WHOIS Database Weekly: GET https://files.whoisfreaks.com/v3.3/download/dbupdate/weekly/domains/whois

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DbWhoisWeekly.py
"""
import os
from datetime import date

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesWHOISApi(client)

    # db_whois_weekly parameters:
    #   var_date (datetime.date, optional, keyword): yyyy-MM-dd; omit for latest
    data = api.db_whois_weekly(var_date=date(2026, 10, 1))  # the file's raw bytes
    path = "DbWhoisWeekly.csv"
    with open(path, "wb") as f:
        f.write(data)
    print(f"Saved {len(data)} bytes to {os.path.abspath(path)}")
```

#### WHOIS Database Monthly

`GET /v3.3/download/dbupdate/monthly/domains/whois`

```python
"""WHOIS Database Monthly: GET https://files.whoisfreaks.com/v3.3/download/dbupdate/monthly/domains/whois

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DbWhoisMonthly.py
"""
import os
from datetime import date

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesWHOISApi(client)

    # db_whois_monthly parameters:
    #   var_date (datetime.date, optional, keyword): yyyy-MM-dd; omit for latest
    data = api.db_whois_monthly(var_date=date(2026, 10, 1))  # the file's raw bytes
    path = "DbWhoisMonthly.csv"
    with open(path, "wb") as f:
        f.write(data)
    print(f"Saved {len(data)} bytes to {os.path.abspath(path)}")
```

### Databases - DNS

#### DNS Database Daily

`GET /v3.2/download/dbupdate/daily/dns`

```python
"""DNS Database Daily: GET https://files.whoisfreaks.com/v3.2/download/dbupdate/daily/dns

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DbDnsDaily.py
"""
import os
from datetime import date

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesDNSApi(client)

    # db_dns_daily parameters:
    #   var_date (datetime.date, optional, keyword): yyyy-MM-dd; omit for latest
    data = api.db_dns_daily(var_date=date(2026, 10, 1))  # the file's raw bytes
    path = "DbDnsDaily.csv"
    with open(path, "wb") as f:
        f.write(data)
    print(f"Saved {len(data)} bytes to {os.path.abspath(path)}")
```

#### DNS Database Weekly

`GET /v3.2/download/dbupdate/weekly/dns`

```python
"""DNS Database Weekly: GET https://files.whoisfreaks.com/v3.2/download/dbupdate/weekly/dns

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DbDnsWeekly.py
"""
import os
from datetime import date

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesDNSApi(client)

    # db_dns_weekly parameters:
    #   var_date (datetime.date, optional, keyword): yyyy-MM-dd; omit for latest
    data = api.db_dns_weekly(var_date=date(2026, 10, 1))  # the file's raw bytes
    path = "DbDnsWeekly.csv"
    with open(path, "wb") as f:
        f.write(data)
    print(f"Saved {len(data)} bytes to {os.path.abspath(path)}")
```

#### DNS Database Monthly

`GET /v3.2/download/dbupdate/monthly/dns`

```python
"""DNS Database Monthly: GET https://files.whoisfreaks.com/v3.2/download/dbupdate/monthly/dns

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DbDnsMonthly.py
"""
import os
from datetime import date

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesDNSApi(client)

    # db_dns_monthly parameters:
    #   var_date (datetime.date, optional, keyword): yyyy-MM-dd; omit for latest
    data = api.db_dns_monthly(var_date=date(2026, 10, 1))  # the file's raw bytes
    path = "DbDnsMonthly.csv"
    with open(path, "wb") as f:
        f.write(data)
    print(f"Saved {len(data)} bytes to {os.path.abspath(path)}")
```

### Databases - Subdomains

#### Subdomains Daily

`GET /v3.2/download/dbupdate/daily/subdomains`

```python
"""Subdomains Daily: GET https://files.whoisfreaks.com/v3.2/download/dbupdate/daily/subdomains

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DbSubdomainsDaily.py
"""
import os
from datetime import date

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesSubdomainsApi(client)

    # db_subdomains_daily parameters:
    #   var_date (datetime.date, optional, keyword): yyyy-MM-dd; omit for latest
    data = api.db_subdomains_daily(var_date=date(2026, 10, 1))  # the file's raw bytes
    path = "DbSubdomainsDaily.csv"
    with open(path, "wb") as f:
        f.write(data)
    print(f"Saved {len(data)} bytes to {os.path.abspath(path)}")
```

#### Subdomains Weekly

`GET /v3.2/download/dbupdate/weekly/subdomains`

```python
"""Subdomains Weekly: GET https://files.whoisfreaks.com/v3.2/download/dbupdate/weekly/subdomains

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DbSubdomainsWeekly.py
"""
import os
from datetime import date

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesSubdomainsApi(client)

    # db_subdomains_weekly parameters:
    #   var_date (datetime.date, optional, keyword): yyyy-MM-dd; omit for latest
    data = api.db_subdomains_weekly(var_date=date(2026, 10, 1))  # the file's raw bytes
    path = "DbSubdomainsWeekly.csv"
    with open(path, "wb") as f:
        f.write(data)
    print(f"Saved {len(data)} bytes to {os.path.abspath(path)}")
```

#### Subdomains Monthly

`GET /v3.2/download/dbupdate/monthly/subdomains`

```python
"""Subdomains Monthly: GET https://files.whoisfreaks.com/v3.2/download/dbupdate/monthly/subdomains

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DbSubdomainsMonthly.py
"""
import os
from datetime import date

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesSubdomainsApi(client)

    # db_subdomains_monthly parameters:
    #   var_date (datetime.date, optional, keyword): yyyy-MM-dd; omit for latest
    data = api.db_subdomains_monthly(var_date=date(2026, 10, 1))  # the file's raw bytes
    path = "DbSubdomainsMonthly.csv"
    with open(path, "wb") as f:
        f.write(data)
    print(f"Saved {len(data)} bytes to {os.path.abspath(path)}")
```

### Databases - IP Geolocation

#### IP to Country Snapshot Status

`GET /v3.3/status/snapshot/ip/country`

```python
"""IP to Country Snapshot Status: GET https://files.whoisfreaks.com/v3.3/status/snapshot/ip/country

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DbIpCountryStatus.py
"""
import json
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesIPGeolocationApi(client)

    # db_ip_country_status takes no parameters.
    result = api.db_ip_country_status()
    print(json.dumps(result.to_dict(), indent=2))
```

#### IP to Country Snapshot

`GET /v3.3/download/snapshot/ip/country`

```python
"""IP to Country Snapshot: GET https://files.whoisfreaks.com/v3.3/download/snapshot/ip/country

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DbIpCountry.py
"""
import os
from datetime import date

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesIPGeolocationApi(client)

    # db_ip_country parameters:
    #   var_date (datetime.date, required)
    data = api.db_ip_country(date(2026, 10, 1))  # the file's raw bytes
    path = "DbIpCountry.zip"
    with open(path, "wb") as f:
        f.write(data)
    print(f"Saved {len(data)} bytes to {os.path.abspath(path)}")
```

#### IP to City Snapshot Status

`GET /v3.3/status/snapshot/ip/city`

```python
"""IP to City Snapshot Status: GET https://files.whoisfreaks.com/v3.3/status/snapshot/ip/city

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DbIpCityStatus.py
"""
import json
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesIPGeolocationApi(client)

    # db_ip_city_status takes no parameters.
    result = api.db_ip_city_status()
    print(json.dumps(result.to_dict(), indent=2))
```

#### IP to City Snapshot

`GET /v3.3/download/snapshot/ip/city`

```python
"""IP to City Snapshot: GET https://files.whoisfreaks.com/v3.3/download/snapshot/ip/city

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DbIpCity.py
"""
import os
from datetime import date

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesIPGeolocationApi(client)

    # db_ip_city parameters:
    #   var_date (datetime.date, required)
    data = api.db_ip_city(date(2026, 10, 1))  # the file's raw bytes
    path = "DbIpCity.zip"
    with open(path, "wb") as f:
        f.write(data)
    print(f"Saved {len(data)} bytes to {os.path.abspath(path)}")
```

### Databases - ASN WHOIS

#### ASN WHOIS Snapshot

`GET /v3.3/download/snapshot/asn/whois`

```python
"""ASN WHOIS Snapshot: GET https://files.whoisfreaks.com/v3.3/download/snapshot/asn/whois

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DbAsnWhois.py
"""
import os
from datetime import date

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesASNWHOISApi(client)

    # db_asn_whois parameters:
    #   var_date (datetime.date, required)
    data = api.db_asn_whois(date(2026, 10, 1))  # the file's raw bytes
    path = "DbAsnWhois.json.gz"
    with open(path, "wb") as f:
        f.write(data)
    print(f"Saved {len(data)} bytes to {os.path.abspath(path)}")
```

#### ASN WHOIS Snapshot Status

`GET /v3.3/status/snapshot/asn/whois`

```python
"""ASN WHOIS Snapshot Status: GET https://files.whoisfreaks.com/v3.3/status/snapshot/asn/whois

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DbAsnWhoisStatus.py
"""
import json
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesASNWHOISApi(client)

    # db_asn_whois_status takes no parameters.
    result = api.db_asn_whois_status()
    print(json.dumps(result.to_dict(), indent=2))
```

### Databases - IP WHOIS

#### IP WHOIS Snapshot

`GET /v3.3/download/snapshot/ip/whois`

```python
"""IP WHOIS Snapshot: GET https://files.whoisfreaks.com/v3.3/download/snapshot/ip/whois

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DbIpWhois.py
"""
import os
from datetime import date

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesIPWHOISApi(client)

    # db_ip_whois parameters:
    #   var_date (datetime.date, required)
    data = api.db_ip_whois(date(2026, 10, 1))  # the file's raw bytes
    path = "DbIpWhois.json.gz"
    with open(path, "wb") as f:
        f.write(data)
    print(f"Saved {len(data)} bytes to {os.path.abspath(path)}")
```

#### IP WHOIS Snapshot Status

`GET /v3.3/status/snapshot/ip/whois`

```python
"""IP WHOIS Snapshot Status: GET https://files.whoisfreaks.com/v3.3/status/snapshot/ip/whois

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DbIpWhoisStatus.py
"""
import json
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesIPWHOISApi(client)

    # db_ip_whois_status takes no parameters.
    result = api.db_ip_whois_status()
    print(json.dumps(result.to_dict(), indent=2))
```

### Databases - IP Security

#### IP Security Snapshot

`GET /v3.3/download/snapshot/ip/security`

```python
"""IP Security Snapshot: GET https://files.whoisfreaks.com/v3.3/download/snapshot/ip/security

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DbIpSecurity.py
"""
import os
from datetime import date

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesIPSecurityApi(client)

    # db_ip_security parameters:
    #   var_date (datetime.date, required)
    data = api.db_ip_security(date(2026, 10, 1))  # the file's raw bytes
    path = "DbIpSecurity.csv"
    with open(path, "wb") as f:
        f.write(data)
    print(f"Saved {len(data)} bytes to {os.path.abspath(path)}")
```

#### IP Security Snapshot Status

`GET /v3.3/status/snapshot/ip/security`

```python
"""IP Security Snapshot Status: GET https://files.whoisfreaks.com/v3.3/status/snapshot/ip/security

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DbIpSecurityStatus.py
"""
import json
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesIPSecurityApi(client)

    # db_ip_security_status takes no parameters.
    result = api.db_ip_security_status()
    print(json.dumps(result.to_dict(), indent=2))
```

### Databases - Threat Feed

#### Download the daily phishing threat feed (CSV)

`GET /v3.4/download/threat-feed/phishing`

```python
"""Download the daily phishing threat feed (CSV): GET https://files.whoisfreaks.com/v3.4/download/threat-feed/phishing

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DownloadThreatFeedPhishing.py
"""
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesThreatFeedApi(client)

    # download_threat_feed_phishing parameters:
    #   var_date (str, optional, keyword): Feed date (yyyy-MM-dd); omit for the full dump of the feed
    data = api.download_threat_feed_phishing(var_date="2026-10-01")  # the file's raw bytes
    path = "DownloadThreatFeedPhishing.csv"
    with open(path, "wb") as f:
        f.write(data)
    print(f"Saved {len(data)} bytes to {os.path.abspath(path)}")
```

#### Download a sample of the phishing threat feed (CSV)

`GET /v3.4/download/threat-feed/phishing/sample`

```python
"""Download a sample of the phishing threat feed (CSV): GET https://files.whoisfreaks.com/v3.4/download/threat-feed/phishing/sample

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DownloadThreatFeedPhishingSample.py
"""
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesThreatFeedApi(client)

    # download_threat_feed_phishing_sample takes no parameters.
    data = api.download_threat_feed_phishing_sample()  # the file's raw bytes
    path = "DownloadThreatFeedPhishingSample.csv"
    with open(path, "wb") as f:
        f.write(data)
    print(f"Saved {len(data)} bytes to {os.path.abspath(path)}")
```

#### Download the daily malware threat feed (CSV)

`GET /v3.4/download/threat-feed/malware`

```python
"""Download the daily malware threat feed (CSV): GET https://files.whoisfreaks.com/v3.4/download/threat-feed/malware

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DownloadThreatFeedMalware.py
"""
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesThreatFeedApi(client)

    # download_threat_feed_malware parameters:
    #   var_date (str, optional, keyword): Feed date (yyyy-MM-dd); omit for the full dump of the feed
    data = api.download_threat_feed_malware(var_date="2026-10-01")  # the file's raw bytes
    path = "DownloadThreatFeedMalware.csv"
    with open(path, "wb") as f:
        f.write(data)
    print(f"Saved {len(data)} bytes to {os.path.abspath(path)}")
```

#### Download a sample of the malware threat feed (CSV)

`GET /v3.4/download/threat-feed/malware/sample`

```python
"""Download a sample of the malware threat feed (CSV): GET https://files.whoisfreaks.com/v3.4/download/threat-feed/malware/sample

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DownloadThreatFeedMalwareSample.py
"""
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesThreatFeedApi(client)

    # download_threat_feed_malware_sample takes no parameters.
    data = api.download_threat_feed_malware_sample()  # the file's raw bytes
    path = "DownloadThreatFeedMalwareSample.csv"
    with open(path, "wb") as f:
        f.write(data)
    print(f"Saved {len(data)} bytes to {os.path.abspath(path)}")
```

#### Download the daily spam threat feed (CSV)

`GET /v3.4/download/threat-feed/spam`

```python
"""Download the daily spam threat feed (CSV): GET https://files.whoisfreaks.com/v3.4/download/threat-feed/spam

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DownloadThreatFeedSpam.py
"""
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesThreatFeedApi(client)

    # download_threat_feed_spam parameters:
    #   var_date (str, optional, keyword): Feed date (yyyy-MM-dd); omit for the full dump of the feed
    data = api.download_threat_feed_spam(var_date="2026-10-01")  # the file's raw bytes
    path = "DownloadThreatFeedSpam.csv"
    with open(path, "wb") as f:
        f.write(data)
    print(f"Saved {len(data)} bytes to {os.path.abspath(path)}")
```

#### Download a sample of the spam threat feed (CSV)

`GET /v3.4/download/threat-feed/spam/sample`

```python
"""Download a sample of the spam threat feed (CSV): GET https://files.whoisfreaks.com/v3.4/download/threat-feed/spam/sample

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DownloadThreatFeedSpamSample.py
"""
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesThreatFeedApi(client)

    # download_threat_feed_spam_sample takes no parameters.
    data = api.download_threat_feed_spam_sample()  # the file's raw bytes
    path = "DownloadThreatFeedSpamSample.csv"
    with open(path, "wb") as f:
        f.write(data)
    print(f"Saved {len(data)} bytes to {os.path.abspath(path)}")
```
