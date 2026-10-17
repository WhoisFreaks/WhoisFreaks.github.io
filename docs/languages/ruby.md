# Ruby SDK

## About

The official **WhoisFreaks Ruby SDK**: a complete client for WHOIS, DNS, SSL, domain availability, subdomain, IP geolocation, IP reputation, ASN, typosquatting, and domain reputation lookups, plus bulk database downloads. Query real-time and historical domain data, reverse WHOIS, and threat intelligence from Ruby with a single API key. Generated from the WhoisFreaks OpenAPI specification and published to RubyGems.

**Keywords:** ruby whois api, ruby whois sdk, whoisfreaks ruby, ruby domain lookup, ruby dns api, whois api, whois lookup, domain api, dns api, dns lookup, reverse whois, historical whois, domain availability api, ssl certificate api, ip geolocation api, ip reputation api, asn lookup, subdomain finder, typosquatting api, domain reputation, threat intelligence api, domain data api, whois sdk, domain monitoring, brand protection api

- **Registry:** RubyGems
- **Package:** `whoisfreaks`

## Install

```bash
gem install whoisfreaks
```

## Build from Source

Prefer to build the SDK yourself instead of installing from RubyGems? Clone the Ruby SDK repository and build it locally:

```bash
git clone https://github.com/WhoisFreaks/whoisfreaks-ruby
cd whoisfreaks-ruby
gem build *.gemspec
gem install ./whoisfreaks-*.gem
```

## Getting Started

A complete walkthrough from an empty directory to a running program:

You need Ruby 2.7 or later and Bundler.

1. Create a project directory:

```bash
mkdir whoisfreaks-test && cd whoisfreaks-test
```

2. Create a `Gemfile` that pins the SDK:

```ruby
source "https://rubygems.org"

gem "whoisfreaks", "~> 0.24.0"
```

3. Install it:

```bash
bundle install
```

4. Create `main.rb`:

```ruby
require "whoisfreaks"

# Read the API key from the environment and set it once.
WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = ENV.fetch("WHOISFREAKS_API_KEY")
end

record = WhoisFreaks::WHOISApi.new.whois_live("whoisfreaks.com")

puts "Registrar: #{record.domain_registrar&.registrar_name}"
puts "Created:   #{record.create_date}"
puts "Expires:   #{record.expiry_date}"
```

5. Set your API key and run it:

```bash
export WHOISFREAKS_API_KEY="your_api_key"
bundle exec ruby main.rb
```

## Configure

See [Authentication](../authentication.md) for how to obtain a key. Minimal setup:

```ruby
# Live WHOIS Lookup
#
# Parameters for whoisLive (GET /v2.0/whois/live):
#   - domain_name (string, required)
#   - format (string (one of: json, xml), optional)

require "json"
require "whoisfreaks"

# Read the API key from the environment and set it once.
WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = ENV.fetch("WHOISFREAKS_API_KEY")
end

api = WhoisFreaks::WHOISApi.new

begin
  result = api.whois_live("whoisfreaks.com")
  puts JSON.pretty_generate(result.to_hash)
rescue WhoisFreaks::ApiError => e
  warn "Request failed: HTTP #{e.code} #{e.response_body}"
  exit 1
end

```

## Endpoints

All 60 endpoints are shown below, grouped by category. Each includes its method, path, parameters, and a runnable example. See the [full endpoint reference](../endpoints/README.md) for response shapes and field details.

### WHOIS

#### Live WHOIS Lookup

`GET /v2.0/whois/live`

```ruby
# Live WHOIS Lookup
#
# Parameters for whoisLive (GET /v2.0/whois/live):
#   - domain_name (string, required)
#   - format (string (one of: json, xml), optional)

require "json"
require "whoisfreaks"

# Read the API key from the environment and set it once.
WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = ENV.fetch("WHOISFREAKS_API_KEY")
end

api = WhoisFreaks::WHOISApi.new

begin
  result = api.whois_live("whoisfreaks.com")
  puts JSON.pretty_generate(result.to_hash)
rescue WhoisFreaks::ApiError => e
  warn "Request failed: HTTP #{e.code} #{e.response_body}"
  exit 1
end

```

#### Bulk WHOIS Lookup

`POST /v2.0/bulkwhois/live`

```ruby
# Bulk WHOIS Lookup
#
# Parameters for bulkWhois (POST /v2.0/bulkwhois/live):
#   - format (string (one of: json, xml), optional)
#   - body: BulkWhoisRequest (required): request body object

require "json"
require "whoisfreaks"

# Read the API key from the environment and set it once.
WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = ENV.fetch("WHOISFREAKS_API_KEY")
end

api = WhoisFreaks::WHOISApi.new

request = WhoisFreaks::BulkWhoisRequest.new(domain_names: ["whoisfreaks.com", "jfreaks.com"])

begin
  result = api.bulk_whois(request)
  puts JSON.pretty_generate(result.to_hash)
rescue WhoisFreaks::ApiError => e
  warn "Request failed: HTTP #{e.code} #{e.response_body}"
  exit 1
end

```

#### Historical WHOIS records for a domain

`GET /v2.0/whois/history`

```ruby
# Historical WHOIS records for a domain
#
# Parameters for whoisHistory (GET /v2.0/whois/history):
#   - domain_name (string, required): Domain to fetch historical WHOIS records for
#   - format (string (one of: json, xml), optional)

require "json"
require "whoisfreaks"

# Read the API key from the environment and set it once.
WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = ENV.fetch("WHOISFREAKS_API_KEY")
end

api = WhoisFreaks::WHOISApi.new

begin
  result = api.whois_history("whoisfreaks.com")
  puts JSON.pretty_generate(result.to_hash)
rescue WhoisFreaks::ApiError => e
  warn "Request failed: HTTP #{e.code} #{e.response_body}"
  exit 1
end

```

#### Reverse WHOIS lookup by keyword

`GET /v2.0/whois/reverse`

```ruby
# Reverse WHOIS lookup by keyword
#
# Parameters for whoisReverse (GET /v2.0/whois/reverse):
#   - keyword (string, required): Keyword to search across WHOIS records
#   - page (integer, optional): Page number
#   - format (string (one of: json, xml), optional)

require "json"
require "whoisfreaks"

# Read the API key from the environment and set it once.
WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = ENV.fetch("WHOISFREAKS_API_KEY")
end

api = WhoisFreaks::WHOISApi.new

begin
  result = api.whois_reverse("whoisfreaks", page: 1)
  puts JSON.pretty_generate(result.to_hash)
rescue WhoisFreaks::ApiError => e
  warn "Request failed: HTTP #{e.code} #{e.response_body}"
  exit 1
end

```

### DNS

#### Live DNS Lookup

`GET /v2.0/dns/live`

```ruby
# Live DNS Lookup
#
# Parameters for dnsLive (GET /v2.0/dns/live):
#   - domain_name (string, optional)
#   - ip_address (string, optional): Use for PTR lookups
#   - type (string, required): all or comma-separated: A,MX,NS,TXT,SOA,SPF,AAAA,CNAME
#   - format (string (one of: json, xml), optional)

require "json"
require "whoisfreaks"

# Read the API key from the environment and set it once.
WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = ENV.fetch("WHOISFREAKS_API_KEY")
end

api = WhoisFreaks::DNSApi.new

begin
  result = api.dns_live("A,MX,TXT", domain_name: "whoisfreaks.com")
  puts JSON.pretty_generate(result.to_hash)
rescue WhoisFreaks::ApiError => e
  warn "Request failed: HTTP #{e.code} #{e.response_body}"
  exit 1
end

```

#### Historical DNS Lookup

`GET /v2.0/dns/historical`

```ruby
# Historical DNS Lookup
#
# Parameters for dnsHistorical (GET /v2.0/dns/historical):
#   - domain_name (string, required)
#   - type (string, required)
#   - page (integer, optional)
#   - format (string (one of: json, xml), optional)

require "json"
require "whoisfreaks"

# Read the API key from the environment and set it once.
WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = ENV.fetch("WHOISFREAKS_API_KEY")
end

api = WhoisFreaks::DNSApi.new

begin
  result = api.dns_historical("whoisfreaks.com", "A,MX,TXT", page: 1)
  puts JSON.pretty_generate(result.to_hash)
rescue WhoisFreaks::ApiError => e
  warn "Request failed: HTTP #{e.code} #{e.response_body}"
  exit 1
end

```

#### Reverse DNS Lookup

`GET /v2.1/dns/reverse`

```ruby
# Reverse DNS Lookup
#
# Parameters for dnsReverse (GET /v2.1/dns/reverse):
#   - value (string, required): IP, CIDR, or record value
#   - type (string (one of: a, mx, cname, ns, aaaa, txt, soa), required)
#   - exact (boolean, optional)
#   - page (integer, optional)
#   - format (string (one of: json, xml), optional)

require "json"
require "whoisfreaks"

# Read the API key from the environment and set it once.
WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = ENV.fetch("WHOISFREAKS_API_KEY")
end

api = WhoisFreaks::DNSApi.new

begin
  result = api.dns_reverse("8.8.8.8", "a", page: 1)
  puts JSON.pretty_generate(result.to_hash)
rescue WhoisFreaks::ApiError => e
  warn "Request failed: HTTP #{e.code} #{e.response_body}"
  exit 1
end

```

#### Bulk DNS Lookup

`POST /v2.0/dns/bulk/live`

```ruby
# Bulk DNS Lookup
#
# Parameters for dnsBulk (POST /v2.0/dns/bulk/live):
#   - type (string, required)
#   - format (string (one of: json, xml), optional)
#   - body: DnsBulkRequest (required): request body object

require "json"
require "whoisfreaks"

# Read the API key from the environment and set it once.
WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = ENV.fetch("WHOISFREAKS_API_KEY")
end

api = WhoisFreaks::DNSApi.new

request = WhoisFreaks::DnsBulkRequest.new(domain_names: ["whoisfreaks.com", "example.com"])

begin
  result = api.dns_bulk("A,MX,TXT", request)
  puts JSON.pretty_generate(result.to_hash)
rescue WhoisFreaks::ApiError => e
  warn "Request failed: HTTP #{e.code} #{e.response_body}"
  exit 1
end

```

### Domain Availability

#### Domain Availability Check with Suggestions

`GET /v2.0/domain/availability`

```ruby
# Domain Availability Check with Suggestions
#
# Parameters for domainAvailabilityV2 (GET /v2.0/domain/availability):
#   - domain (string, required): The domain name to check
#   - sug (boolean, optional): Whether to return TLD suggestions alongside the queried domain.
#   - count (integer, optional): Number of TLD suggestions to return when sug=true. Maximum is 100.
#   - format (string (one of: json, xml), optional)

require "json"
require "whoisfreaks"

# Read the API key from the environment and set it once.
WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = ENV.fetch("WHOISFREAKS_API_KEY")
end

api = WhoisFreaks::DomainAvailabilityApi.new

begin
  result = api.domain_availability_v2("google.com", sug: true, count: 5)
  puts JSON.pretty_generate(result.to_hash)
rescue WhoisFreaks::ApiError => e
  warn "Request failed: HTTP #{e.code} #{e.response_body}"
  exit 1
end

```

#### Bulk Domain Availability Check

`POST /v2.0/domain/availability`

```ruby
# Bulk Domain Availability Check
#
# Parameters for bulkDomainAvailabilityV2 (POST /v2.0/domain/availability):
#   - domain (string, optional): Required for TLD-mode bulk check (base domain).
#   - format (string (one of: json, xml), optional)
#   - body: BulkDomainAvailabilityRequest (required): request body object

require "json"
require "whoisfreaks"

# Read the API key from the environment and set it once.
WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = ENV.fetch("WHOISFREAKS_API_KEY")
end

api = WhoisFreaks::DomainAvailabilityApi.new

request = WhoisFreaks::BulkDomainAvailabilityRequest.new(domain_names: ["whoisfreaks.com", "example.com"])

begin
  result = api.bulk_domain_availability_v2(request)
  puts JSON.pretty_generate(result.to_hash)
rescue WhoisFreaks::ApiError => e
  warn "Request failed: HTTP #{e.code} #{e.response_body}"
  exit 1
end

```

### Typosquatting

#### Typosquatting Lookup

`GET /v3.0/domain/typos`

```ruby
# Typosquatting Lookup
#
# Parameters for typosquatting (GET /v3.0/domain/typos):
#   - keyword (string, optional)
#   - pattern (string, optional)
#   - page_token (string, optional)

require "json"
require "whoisfreaks"

# Read the API key from the environment and set it once.
WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = ENV.fetch("WHOISFREAKS_API_KEY")
end

api = WhoisFreaks::TyposquattingApi.new

begin
  result = api.typosquatting(keyword: "whoisfreaks")
  puts JSON.pretty_generate(result.to_hash)
rescue WhoisFreaks::ApiError => e
  warn "Request failed: HTTP #{e.code} #{e.response_body}"
  exit 1
end

```

### SSL

#### SSL Certificate Lookup

`GET /v1.0/ssl/live`

```ruby
# SSL Certificate Lookup
#
# Parameters for sslLookup (GET /v1.0/ssl/live):
#   - domain_name (string, required)
#   - chain (boolean, optional)
#   - ssl_raw (boolean, optional)
#   - format (string (one of: json, xml), optional)

require "json"
require "whoisfreaks"

# Read the API key from the environment and set it once.
WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = ENV.fetch("WHOISFREAKS_API_KEY")
end

api = WhoisFreaks::SSLApi.new

begin
  result = api.ssl_lookup("whoisfreaks.com")
  puts JSON.pretty_generate(result.to_hash)
rescue WhoisFreaks::ApiError => e
  warn "Request failed: HTTP #{e.code} #{e.response_body}"
  exit 1
end

```

### Geolocation

#### IP Geolocation Lookup

`GET /v1.0/geolocation`

```ruby
# IP Geolocation Lookup
#
# Parameters for geolocation (GET /v1.0/geolocation):
#   - ip (string, required)

require "json"
require "whoisfreaks"

# Read the API key from the environment and set it once.
WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = ENV.fetch("WHOISFREAKS_API_KEY")
end

api = WhoisFreaks::GeolocationApi.new

begin
  result = api.geolocation("8.8.8.8")
  puts JSON.pretty_generate(result.to_hash)
rescue WhoisFreaks::ApiError => e
  warn "Request failed: HTTP #{e.code} #{e.response_body}"
  exit 1
end

```

#### Bulk IP Geolocation

`POST /v1.0/geolocation`

```ruby
# Bulk IP Geolocation
#
# Parameters for bulkGeolocation (POST /v1.0/geolocation):
#   - body: BulkGeolocationRequest (required): request body object

require "json"
require "whoisfreaks"

# Read the API key from the environment and set it once.
WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = ENV.fetch("WHOISFREAKS_API_KEY")
end

api = WhoisFreaks::GeolocationApi.new

request = WhoisFreaks::BulkGeolocationRequest.new(ips: ["8.8.8.8", "1.1.1.1"])

begin
  results = api.bulk_geolocation(request)
  puts JSON.pretty_generate(results.map(&:to_hash))
rescue WhoisFreaks::ApiError => e
  warn "Request failed: HTTP #{e.code} #{e.response_body}"
  exit 1
end

```

### Subdomains

#### Subdomains Lookup

`GET /v1.0/subdomains`

```ruby
# Subdomains Lookup
#
# Parameters for subdomains (GET /v1.0/subdomains):
#   - domain (string, required)
#   - after (string, optional)
#   - before (string, optional)
#   - status (string (one of: active, inactive), optional)
#   - page (integer, optional)
#   - format (string (one of: json, xml), optional)

require "json"
require "whoisfreaks"

# Read the API key from the environment and set it once.
WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = ENV.fetch("WHOISFREAKS_API_KEY")
end

api = WhoisFreaks::SubdomainsApi.new

begin
  result = api.subdomains("whoisfreaks.com", page: 1)
  puts JSON.pretty_generate(result.to_hash)
rescue WhoisFreaks::ApiError => e
  warn "Request failed: HTTP #{e.code} #{e.response_body}"
  exit 1
end

```

### IP Reputation

#### IP Reputation Lookup

`GET /v1.0/security`

```ruby
# IP Reputation Lookup
#
# Parameters for ipReputation (GET /v1.0/security):
#   - ip (string, required)

require "json"
require "whoisfreaks"

# Read the API key from the environment and set it once.
WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = ENV.fetch("WHOISFREAKS_API_KEY")
end

api = WhoisFreaks::IPReputationApi.new

begin
  result = api.ip_reputation("8.8.8.8")
  puts JSON.pretty_generate(result.to_hash)
rescue WhoisFreaks::ApiError => e
  warn "Request failed: HTTP #{e.code} #{e.response_body}"
  exit 1
end

```

#### Bulk IP Reputation

`POST /v1.0/security`

```ruby
# Bulk IP Reputation
#
# Parameters for bulkIpReputation (POST /v1.0/security):
#   - body: BulkGeolocationRequest (required): request body object

require "json"
require "whoisfreaks"

# Read the API key from the environment and set it once.
WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = ENV.fetch("WHOISFREAKS_API_KEY")
end

api = WhoisFreaks::IPReputationApi.new

request = WhoisFreaks::BulkGeolocationRequest.new(ips: ["8.8.8.8", "1.1.1.1"])

begin
  results = api.bulk_ip_reputation(request)
  puts JSON.pretty_generate(results.map(&:to_hash))
rescue WhoisFreaks::ApiError => e
  warn "Request failed: HTTP #{e.code} #{e.response_body}"
  exit 1
end

```

### Domain Reputation

#### Domain Reputation Lookup

`GET /v1/domain/security`

```ruby
# Domain Reputation Lookup
#
# Parameters for domainReputation (GET /v1/domain/security):
#   - domain_name (string, required): The domain name to assess
#   - format (string (one of: json, xml), optional)

require "json"
require "whoisfreaks"

# Read the API key from the environment and set it once.
WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = ENV.fetch("WHOISFREAKS_API_KEY")
end

api = WhoisFreaks::DomainReputationApi.new

begin
  result = api.domain_reputation("amazon.com")
  puts JSON.pretty_generate(result.to_hash)
rescue WhoisFreaks::ApiError => e
  warn "Request failed: HTTP #{e.code} #{e.response_body}"
  exit 1
end

```

### ASN WHOIS

#### ASN WHOIS Lookup

`GET /v2.0/asn-whois`

```ruby
# ASN WHOIS Lookup
#
# Parameters for asnWhois (GET /v2.0/asn-whois):
#   - asn (string, required)
#   - format (string (one of: json, xml), optional)

require "json"
require "whoisfreaks"

# Read the API key from the environment and set it once.
WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = ENV.fetch("WHOISFREAKS_API_KEY")
end

api = WhoisFreaks::ASNWHOISApi.new

begin
  result = api.asn_whois("as15169")
  puts JSON.pretty_generate(result.to_hash)
rescue WhoisFreaks::ApiError => e
  warn "Request failed: HTTP #{e.code} #{e.response_body}"
  exit 1
end

```

### IP WHOIS

#### IP WHOIS Lookup

`GET /v1.0/ip-whois`

```ruby
# IP WHOIS Lookup
#
# Parameters for ipWhois (GET /v1.0/ip-whois):
#   - ip (string, required)
#   - format (string (one of: json, xml), optional)

require "json"
require "whoisfreaks"

# Read the API key from the environment and set it once.
WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = ENV.fetch("WHOISFREAKS_API_KEY")
end

api = WhoisFreaks::IPWHOISApi.new

begin
  result = api.ip_whois("8.8.8.8")
  puts JSON.pretty_generate(result.to_hash)
rescue WhoisFreaks::ApiError => e
  warn "Request failed: HTTP #{e.code} #{e.response_body}"
  exit 1
end

```

### Account

#### Rotate API Key

`GET /v1.0/api-key/rotate`

```ruby
# Rotate API Key
#
# Parameters for rotateApiKey (GET /v1.0/api-key/rotate):
#   (no parameters; the API key is set on the client)

require "whoisfreaks"

# Read the API key from the environment and set it once.
WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = ENV.fetch("WHOISFREAKS_API_KEY")
end

api = WhoisFreaks::AccountApi.new

begin
  new_key = api.rotate_api_key
  # The old key stops working now: store the new one before making more calls.
  puts "New API key: #{new_key}"
rescue WhoisFreaks::ApiError => e
  warn "Request failed: HTTP #{e.code} #{e.response_body}"
  exit 1
end

```

#### Account Usage

`GET /v1.0/whoisapi/usage`

```ruby
# Account Usage
#
# Parameters for accountUsage (GET /v1.0/whoisapi/usage):
#   (no parameters; the API key is set on the client)

require "json"
require "whoisfreaks"

# Read the API key from the environment and set it once.
WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = ENV.fetch("WHOISFREAKS_API_KEY")
end

api = WhoisFreaks::AccountApi.new

begin
  result = api.account_usage
  puts JSON.pretty_generate(result.to_hash)
rescue WhoisFreaks::ApiError => e
  warn "Request failed: HTTP #{e.code} #{e.response_body}"
  exit 1
end

```

#### Database File Status (Public)

`GET /v3.4/status`

```ruby
# Database File Status (Public)
#
# Parameters for databaseFileStatus (GET /v3.4/status):
#   (no parameters; no API key required)

require "json"
require "whoisfreaks"

# Read the API key from the environment and set it once.
# (This endpoint is public, so the key is not sent with this request.)
WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = ENV.fetch("WHOISFREAKS_API_KEY")
end

api = WhoisFreaks::AccountApi.new

begin
  result = api.database_file_status
  puts JSON.pretty_generate(result.to_hash)
rescue WhoisFreaks::ApiError => e
  warn "Request failed: HTTP #{e.code} #{e.response_body}"
  exit 1
end

```

### Databases - Newly Registered

#### Newly Registered gTLD (CSV)

`GET /v3.1/download/domainer/gtld`

```ruby
# Newly Registered gTLD (CSV)
#
# Parameters for dbNewlyGtld (GET /v3.1/download/domainer/gtld):
#   - whois (boolean, required)
#   - date (string, optional): yyyy-MM-dd; omit for latest
#   - tlds (string, optional)

require "date"
require "fileutils"
require "whoisfreaks"

# Read the API key from the environment and set it once.
WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = ENV.fetch("WHOISFREAKS_API_KEY")
end

api = WhoisFreaks::DatabasesNewlyRegisteredApi.new

begin
  file = api.db_newly_gtld(true, date: Date.parse("2026-10-01"))
  # The SDK returns a Tempfile that is deleted when the program exits: copy it.
  save_as = "DbNewlyGtld.csv"
  FileUtils.cp(file.path, save_as)
  puts "Saved #{File.expand_path(save_as)} (#{File.size(save_as)} bytes)"
rescue WhoisFreaks::ApiError => e
  warn "Request failed: HTTP #{e.code} #{e.response_body}"
  exit 1
end

```

#### Newly Registered ccTLD (CSV)

`GET /v3.1/download/domainer/cctld`

```ruby
# Newly Registered ccTLD (CSV)
#
# Parameters for dbNewlyCctld (GET /v3.1/download/domainer/cctld):
#   - whois (boolean, required)
#   - date (string, optional): yyyy-MM-dd; omit for latest
#   - tlds (string, optional)

require "date"
require "fileutils"
require "whoisfreaks"

# Read the API key from the environment and set it once.
WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = ENV.fetch("WHOISFREAKS_API_KEY")
end

api = WhoisFreaks::DatabasesNewlyRegisteredApi.new

begin
  file = api.db_newly_cctld(true, date: Date.parse("2026-10-01"))
  # The SDK returns a Tempfile that is deleted when the program exits: copy it.
  save_as = "DbNewlyCctld.csv"
  FileUtils.cp(file.path, save_as)
  puts "Saved #{File.expand_path(save_as)} (#{File.size(save_as)} bytes)"
rescue WhoisFreaks::ApiError => e
  warn "Request failed: HTTP #{e.code} #{e.response_body}"
  exit 1
end

```

#### Newly Registered gTLD Cleaned WHOIS (CSV)

`GET /v3.1/download/domainer/gtld/cleaned`

```ruby
# Newly Registered gTLD Cleaned WHOIS (CSV)
#
# Parameters for dbNewlyGtldCleaned (GET /v3.1/download/domainer/gtld/cleaned):
#   - date (string, optional): yyyy-MM-dd; omit for latest

require "date"
require "fileutils"
require "whoisfreaks"

# Read the API key from the environment and set it once.
WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = ENV.fetch("WHOISFREAKS_API_KEY")
end

api = WhoisFreaks::DatabasesNewlyRegisteredApi.new

begin
  file = api.db_newly_gtld_cleaned(date: Date.parse("2026-10-01"))
  # The SDK returns a Tempfile that is deleted when the program exits: copy it.
  save_as = "DbNewlyGtldCleaned.csv"
  FileUtils.cp(file.path, save_as)
  puts "Saved #{File.expand_path(save_as)} (#{File.size(save_as)} bytes)"
rescue WhoisFreaks::ApiError => e
  warn "Request failed: HTTP #{e.code} #{e.response_body}"
  exit 1
end

```

#### Newly Registered ccTLD Cleaned WHOIS (CSV)

`GET /v3.1/download/domainer/cctld/cleaned`

```ruby
# Newly Registered ccTLD Cleaned WHOIS (CSV)
#
# Parameters for dbNewlyCctldCleaned (GET /v3.1/download/domainer/cctld/cleaned):
#   - date (string, optional): yyyy-MM-dd; omit for latest

require "date"
require "fileutils"
require "whoisfreaks"

# Read the API key from the environment and set it once.
WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = ENV.fetch("WHOISFREAKS_API_KEY")
end

api = WhoisFreaks::DatabasesNewlyRegisteredApi.new

begin
  file = api.db_newly_cctld_cleaned(date: Date.parse("2026-10-01"))
  # The SDK returns a Tempfile that is deleted when the program exits: copy it.
  save_as = "DbNewlyCctldCleaned.csv"
  FileUtils.cp(file.path, save_as)
  puts "Saved #{File.expand_path(save_as)} (#{File.size(save_as)} bytes)"
rescue WhoisFreaks::ApiError => e
  warn "Request failed: HTTP #{e.code} #{e.response_body}"
  exit 1
end

```

#### Newly Registered gTLD (JSON)

`GET /v3.1/domains/newly/gtld`

```ruby
# Newly Registered gTLD (JSON)
#
# Parameters for dbNewlyGtldJson (GET /v3.1/domains/newly/gtld):
#   - date (string, optional): yyyy-MM-dd; omit for latest
#   - tlds (string, optional)

require "date"
require "whoisfreaks"

# Read the API key from the environment and set it once.
WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = ENV.fetch("WHOISFREAKS_API_KEY")
end

api = WhoisFreaks::DatabasesNewlyRegisteredApi.new

begin
  domains = api.db_newly_gtld_json(date: Date.parse("2026-10-01"))
  puts domains
rescue WhoisFreaks::ApiError => e
  warn "Request failed: HTTP #{e.code} #{e.response_body}"
  exit 1
end

```

#### Newly Registered ccTLD (JSON)

`GET /v3.1/domains/newly/cctld`

```ruby
# Newly Registered ccTLD (JSON)
#
# Parameters for dbNewlyCctldJson (GET /v3.1/domains/newly/cctld):
#   - date (string, optional): yyyy-MM-dd; omit for latest
#   - tlds (string, optional)

require "date"
require "whoisfreaks"

# Read the API key from the environment and set it once.
WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = ENV.fetch("WHOISFREAKS_API_KEY")
end

api = WhoisFreaks::DatabasesNewlyRegisteredApi.new

begin
  domains = api.db_newly_cctld_json(date: Date.parse("2026-10-01"))
  puts domains
rescue WhoisFreaks::ApiError => e
  warn "Request failed: HTTP #{e.code} #{e.response_body}"
  exit 1
end

```

#### Newly Registered With DNS

`GET /v3.1/download/domainer/newly/dns`

```ruby
# Newly Registered With DNS
#
# Parameters for dbNewlyDns (GET /v3.1/download/domainer/newly/dns):
#   - date (string, optional): yyyy-MM-dd; omit for latest

require "date"
require "fileutils"
require "whoisfreaks"

# Read the API key from the environment and set it once.
WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = ENV.fetch("WHOISFREAKS_API_KEY")
end

api = WhoisFreaks::DatabasesNewlyRegisteredApi.new

begin
  file = api.db_newly_dns(date: Date.parse("2026-10-01"))
  # The SDK returns a Tempfile that is deleted when the program exits: copy it.
  save_as = "DbNewlyDns.json"
  FileUtils.cp(file.path, save_as)
  puts "Saved #{File.expand_path(save_as)} (#{File.size(save_as)} bytes)"
rescue WhoisFreaks::ApiError => e
  warn "Request failed: HTTP #{e.code} #{e.response_body}"
  exit 1
end

```

### Databases - Expiring & Dropped

#### Expiring Domains

`GET /v3.1/download/domainer/expired`

```ruby
# Expiring Domains
#
# Parameters for dbExpired (GET /v3.1/download/domainer/expired):
#   - whois (boolean, required)
#   - date (string, optional): yyyy-MM-dd; omit for latest

require "date"
require "fileutils"
require "whoisfreaks"

# Read the API key from the environment and set it once.
WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = ENV.fetch("WHOISFREAKS_API_KEY")
end

api = WhoisFreaks::DatabasesExpiringDroppedApi.new

begin
  file = api.db_expired(true, date: Date.parse("2026-10-01"))
  # The SDK returns a Tempfile that is deleted when the program exits: copy it.
  save_as = "DbExpired.csv"
  FileUtils.cp(file.path, save_as)
  puts "Saved #{File.expand_path(save_as)} (#{File.size(save_as)} bytes)"
rescue WhoisFreaks::ApiError => e
  warn "Request failed: HTTP #{e.code} #{e.response_body}"
  exit 1
end

```

#### Expiring Cleaned WHOIS

`GET /v3.1/download/domainer/expired/cleaned`

```ruby
# Expiring Cleaned WHOIS
#
# Parameters for dbExpiredCleaned (GET /v3.1/download/domainer/expired/cleaned):
#   - date (string, optional): yyyy-MM-dd; omit for latest

require "date"
require "fileutils"
require "whoisfreaks"

# Read the API key from the environment and set it once.
WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = ENV.fetch("WHOISFREAKS_API_KEY")
end

api = WhoisFreaks::DatabasesExpiringDroppedApi.new

begin
  file = api.db_expired_cleaned(date: Date.parse("2026-10-01"))
  # The SDK returns a Tempfile that is deleted when the program exits: copy it.
  save_as = "DbExpiredCleaned.csv"
  FileUtils.cp(file.path, save_as)
  puts "Saved #{File.expand_path(save_as)} (#{File.size(save_as)} bytes)"
rescue WhoisFreaks::ApiError => e
  warn "Request failed: HTTP #{e.code} #{e.response_body}"
  exit 1
end

```

#### Dropped Domains

`GET /v3.1/download/domainer/dropped`

```ruby
# Dropped Domains
#
# Parameters for dbDropped (GET /v3.1/download/domainer/dropped):
#   - whois (boolean, required)
#   - date (string, optional): yyyy-MM-dd; omit for latest

require "date"
require "fileutils"
require "whoisfreaks"

# Read the API key from the environment and set it once.
WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = ENV.fetch("WHOISFREAKS_API_KEY")
end

api = WhoisFreaks::DatabasesExpiringDroppedApi.new

begin
  file = api.db_dropped(true, date: Date.parse("2026-10-01"))
  # The SDK returns a Tempfile that is deleted when the program exits: copy it.
  save_as = "DbDropped.csv"
  FileUtils.cp(file.path, save_as)
  puts "Saved #{File.expand_path(save_as)} (#{File.size(save_as)} bytes)"
rescue WhoisFreaks::ApiError => e
  warn "Request failed: HTTP #{e.code} #{e.response_body}"
  exit 1
end

```

#### Dropped Domains (JSON)

`GET /v3.1/domains/dropped`

```ruby
# Dropped Domains (JSON)
#
# Parameters for dbDroppedJson (GET /v3.1/domains/dropped):
#   - date (string, optional): yyyy-MM-dd; omit for latest
#   - tlds (string, optional)

require "date"
require "whoisfreaks"

# Read the API key from the environment and set it once.
WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = ENV.fetch("WHOISFREAKS_API_KEY")
end

api = WhoisFreaks::DatabasesExpiringDroppedApi.new

begin
  domains = api.db_dropped_json(date: Date.parse("2026-10-01"))
  puts domains
rescue WhoisFreaks::ApiError => e
  warn "Request failed: HTTP #{e.code} #{e.response_body}"
  exit 1
end

```

#### Dropped With Backlinks

`GET /v3.3/download/domainer/dropped/backlinks`

```ruby
# Dropped With Backlinks
#
# Parameters for dbDroppedBacklinks (GET /v3.3/download/domainer/dropped/backlinks):
#   - whois (boolean, optional)
#   - date (string, optional): yyyy-MM-dd; omit for latest

require "date"
require "fileutils"
require "whoisfreaks"

# Read the API key from the environment and set it once.
WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = ENV.fetch("WHOISFREAKS_API_KEY")
end

api = WhoisFreaks::DatabasesExpiringDroppedApi.new

begin
  file = api.db_dropped_backlinks(date: Date.parse("2026-10-01"))
  # The SDK returns a Tempfile that is deleted when the program exits: copy it.
  save_as = "DbDroppedBacklinks.csv"
  FileUtils.cp(file.path, save_as)
  puts "Saved #{File.expand_path(save_as)} (#{File.size(save_as)} bytes)"
rescue WhoisFreaks::ApiError => e
  warn "Request failed: HTTP #{e.code} #{e.response_body}"
  exit 1
end

```

### Databases - WHOIS

#### WHOIS Database Daily

`GET /v3.3/download/dbupdate/daily/domains/whois`

```ruby
# WHOIS Database Daily
#
# Parameters for dbWhoisDaily (GET /v3.3/download/dbupdate/daily/domains/whois):
#   - date (string, optional): yyyy-MM-dd; omit for latest

require "date"
require "fileutils"
require "whoisfreaks"

# Read the API key from the environment and set it once.
WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = ENV.fetch("WHOISFREAKS_API_KEY")
end

api = WhoisFreaks::DatabasesWHOISApi.new

begin
  file = api.db_whois_daily(date: Date.parse("2026-10-01"))
  # The SDK returns a Tempfile that is deleted when the program exits: copy it.
  save_as = "DbWhoisDaily.csv"
  FileUtils.cp(file.path, save_as)
  puts "Saved #{File.expand_path(save_as)} (#{File.size(save_as)} bytes)"
rescue WhoisFreaks::ApiError => e
  warn "Request failed: HTTP #{e.code} #{e.response_body}"
  exit 1
end

```

#### WHOIS Database Weekly

`GET /v3.3/download/dbupdate/weekly/domains/whois`

```ruby
# WHOIS Database Weekly
#
# Parameters for dbWhoisWeekly (GET /v3.3/download/dbupdate/weekly/domains/whois):
#   - date (string, optional): yyyy-MM-dd; omit for latest

require "date"
require "fileutils"
require "whoisfreaks"

# Read the API key from the environment and set it once.
WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = ENV.fetch("WHOISFREAKS_API_KEY")
end

api = WhoisFreaks::DatabasesWHOISApi.new

begin
  file = api.db_whois_weekly(date: Date.parse("2026-10-01"))
  # The SDK returns a Tempfile that is deleted when the program exits: copy it.
  save_as = "DbWhoisWeekly.csv"
  FileUtils.cp(file.path, save_as)
  puts "Saved #{File.expand_path(save_as)} (#{File.size(save_as)} bytes)"
rescue WhoisFreaks::ApiError => e
  warn "Request failed: HTTP #{e.code} #{e.response_body}"
  exit 1
end

```

#### WHOIS Database Monthly

`GET /v3.3/download/dbupdate/monthly/domains/whois`

```ruby
# WHOIS Database Monthly
#
# Parameters for dbWhoisMonthly (GET /v3.3/download/dbupdate/monthly/domains/whois):
#   - date (string, optional): yyyy-MM-dd; omit for latest

require "date"
require "fileutils"
require "whoisfreaks"

# Read the API key from the environment and set it once.
WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = ENV.fetch("WHOISFREAKS_API_KEY")
end

api = WhoisFreaks::DatabasesWHOISApi.new

begin
  file = api.db_whois_monthly(date: Date.parse("2026-10-01"))
  # The SDK returns a Tempfile that is deleted when the program exits: copy it.
  save_as = "DbWhoisMonthly.csv"
  FileUtils.cp(file.path, save_as)
  puts "Saved #{File.expand_path(save_as)} (#{File.size(save_as)} bytes)"
rescue WhoisFreaks::ApiError => e
  warn "Request failed: HTTP #{e.code} #{e.response_body}"
  exit 1
end

```

### Databases - DNS

#### DNS Database Daily

`GET /v3.2/download/dbupdate/daily/dns`

```ruby
# DNS Database Daily
#
# Parameters for dbDnsDaily (GET /v3.2/download/dbupdate/daily/dns):
#   - date (string, optional): yyyy-MM-dd; omit for latest

require "date"
require "fileutils"
require "whoisfreaks"

# Read the API key from the environment and set it once.
WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = ENV.fetch("WHOISFREAKS_API_KEY")
end

api = WhoisFreaks::DatabasesDNSApi.new

begin
  file = api.db_dns_daily(date: Date.parse("2026-10-01"))
  # The SDK returns a Tempfile that is deleted when the program exits: copy it.
  save_as = "DbDnsDaily.csv"
  FileUtils.cp(file.path, save_as)
  puts "Saved #{File.expand_path(save_as)} (#{File.size(save_as)} bytes)"
rescue WhoisFreaks::ApiError => e
  warn "Request failed: HTTP #{e.code} #{e.response_body}"
  exit 1
end

```

#### DNS Database Weekly

`GET /v3.2/download/dbupdate/weekly/dns`

```ruby
# DNS Database Weekly
#
# Parameters for dbDnsWeekly (GET /v3.2/download/dbupdate/weekly/dns):
#   - date (string, optional): yyyy-MM-dd; omit for latest

require "date"
require "fileutils"
require "whoisfreaks"

# Read the API key from the environment and set it once.
WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = ENV.fetch("WHOISFREAKS_API_KEY")
end

api = WhoisFreaks::DatabasesDNSApi.new

begin
  file = api.db_dns_weekly(date: Date.parse("2026-10-01"))
  # The SDK returns a Tempfile that is deleted when the program exits: copy it.
  save_as = "DbDnsWeekly.csv"
  FileUtils.cp(file.path, save_as)
  puts "Saved #{File.expand_path(save_as)} (#{File.size(save_as)} bytes)"
rescue WhoisFreaks::ApiError => e
  warn "Request failed: HTTP #{e.code} #{e.response_body}"
  exit 1
end

```

#### DNS Database Monthly

`GET /v3.2/download/dbupdate/monthly/dns`

```ruby
# DNS Database Monthly
#
# Parameters for dbDnsMonthly (GET /v3.2/download/dbupdate/monthly/dns):
#   - date (string, optional): yyyy-MM-dd; omit for latest

require "date"
require "fileutils"
require "whoisfreaks"

# Read the API key from the environment and set it once.
WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = ENV.fetch("WHOISFREAKS_API_KEY")
end

api = WhoisFreaks::DatabasesDNSApi.new

begin
  file = api.db_dns_monthly(date: Date.parse("2026-10-01"))
  # The SDK returns a Tempfile that is deleted when the program exits: copy it.
  save_as = "DbDnsMonthly.csv"
  FileUtils.cp(file.path, save_as)
  puts "Saved #{File.expand_path(save_as)} (#{File.size(save_as)} bytes)"
rescue WhoisFreaks::ApiError => e
  warn "Request failed: HTTP #{e.code} #{e.response_body}"
  exit 1
end

```

### Databases - Subdomains

#### Subdomains Daily

`GET /v3.2/download/dbupdate/daily/subdomains`

```ruby
# Subdomains Daily
#
# Parameters for dbSubdomainsDaily (GET /v3.2/download/dbupdate/daily/subdomains):
#   - date (string, optional): yyyy-MM-dd; omit for latest

require "date"
require "fileutils"
require "whoisfreaks"

# Read the API key from the environment and set it once.
WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = ENV.fetch("WHOISFREAKS_API_KEY")
end

api = WhoisFreaks::DatabasesSubdomainsApi.new

begin
  file = api.db_subdomains_daily(date: Date.parse("2026-10-01"))
  # The SDK returns a Tempfile that is deleted when the program exits: copy it.
  save_as = "DbSubdomainsDaily.csv"
  FileUtils.cp(file.path, save_as)
  puts "Saved #{File.expand_path(save_as)} (#{File.size(save_as)} bytes)"
rescue WhoisFreaks::ApiError => e
  warn "Request failed: HTTP #{e.code} #{e.response_body}"
  exit 1
end

```

#### Subdomains Weekly

`GET /v3.2/download/dbupdate/weekly/subdomains`

```ruby
# Subdomains Weekly
#
# Parameters for dbSubdomainsWeekly (GET /v3.2/download/dbupdate/weekly/subdomains):
#   - date (string, optional): yyyy-MM-dd; omit for latest

require "date"
require "fileutils"
require "whoisfreaks"

# Read the API key from the environment and set it once.
WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = ENV.fetch("WHOISFREAKS_API_KEY")
end

api = WhoisFreaks::DatabasesSubdomainsApi.new

begin
  file = api.db_subdomains_weekly(date: Date.parse("2026-10-01"))
  # The SDK returns a Tempfile that is deleted when the program exits: copy it.
  save_as = "DbSubdomainsWeekly.csv"
  FileUtils.cp(file.path, save_as)
  puts "Saved #{File.expand_path(save_as)} (#{File.size(save_as)} bytes)"
rescue WhoisFreaks::ApiError => e
  warn "Request failed: HTTP #{e.code} #{e.response_body}"
  exit 1
end

```

#### Subdomains Monthly

`GET /v3.2/download/dbupdate/monthly/subdomains`

```ruby
# Subdomains Monthly
#
# Parameters for dbSubdomainsMonthly (GET /v3.2/download/dbupdate/monthly/subdomains):
#   - date (string, optional): yyyy-MM-dd; omit for latest

require "date"
require "fileutils"
require "whoisfreaks"

# Read the API key from the environment and set it once.
WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = ENV.fetch("WHOISFREAKS_API_KEY")
end

api = WhoisFreaks::DatabasesSubdomainsApi.new

begin
  file = api.db_subdomains_monthly(date: Date.parse("2026-10-01"))
  # The SDK returns a Tempfile that is deleted when the program exits: copy it.
  save_as = "DbSubdomainsMonthly.csv"
  FileUtils.cp(file.path, save_as)
  puts "Saved #{File.expand_path(save_as)} (#{File.size(save_as)} bytes)"
rescue WhoisFreaks::ApiError => e
  warn "Request failed: HTTP #{e.code} #{e.response_body}"
  exit 1
end

```

### Databases - IP Geolocation

#### IP to Country Snapshot Status

`GET /v3.3/status/snapshot/ip/country`

```ruby
# IP to Country Snapshot Status
#
# Parameters for dbIpCountryStatus (GET /v3.3/status/snapshot/ip/country):
#   (no parameters; the API key is set on the client)

require "json"
require "whoisfreaks"

# Read the API key from the environment and set it once.
WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = ENV.fetch("WHOISFREAKS_API_KEY")
end

api = WhoisFreaks::DatabasesIPGeolocationApi.new

begin
  result = api.db_ip_country_status
  puts JSON.pretty_generate(result.to_hash)
rescue WhoisFreaks::ApiError => e
  warn "Request failed: HTTP #{e.code} #{e.response_body}"
  exit 1
end

```

#### IP to Country Snapshot

`GET /v3.3/download/snapshot/ip/country`

```ruby
# IP to Country Snapshot
#
# Parameters for dbIpCountry (GET /v3.3/download/snapshot/ip/country):
#   - date (string, required)

require "date"
require "fileutils"
require "whoisfreaks"

# Read the API key from the environment and set it once.
WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = ENV.fetch("WHOISFREAKS_API_KEY")
end

api = WhoisFreaks::DatabasesIPGeolocationApi.new

begin
  file = api.db_ip_country(Date.parse("2026-10-01"))
  # The SDK returns a Tempfile that is deleted when the program exits: copy it.
  save_as = "DbIpCountry.zip"
  FileUtils.cp(file.path, save_as)
  puts "Saved #{File.expand_path(save_as)} (#{File.size(save_as)} bytes)"
rescue WhoisFreaks::ApiError => e
  warn "Request failed: HTTP #{e.code} #{e.response_body}"
  exit 1
end

```

#### IP to City Snapshot Status

`GET /v3.3/status/snapshot/ip/city`

```ruby
# IP to City Snapshot Status
#
# Parameters for dbIpCityStatus (GET /v3.3/status/snapshot/ip/city):
#   (no parameters; the API key is set on the client)

require "json"
require "whoisfreaks"

# Read the API key from the environment and set it once.
WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = ENV.fetch("WHOISFREAKS_API_KEY")
end

api = WhoisFreaks::DatabasesIPGeolocationApi.new

begin
  result = api.db_ip_city_status
  puts JSON.pretty_generate(result.to_hash)
rescue WhoisFreaks::ApiError => e
  warn "Request failed: HTTP #{e.code} #{e.response_body}"
  exit 1
end

```

#### IP to City Snapshot

`GET /v3.3/download/snapshot/ip/city`

```ruby
# IP to City Snapshot
#
# Parameters for dbIpCity (GET /v3.3/download/snapshot/ip/city):
#   - date (string, required)

require "date"
require "fileutils"
require "whoisfreaks"

# Read the API key from the environment and set it once.
WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = ENV.fetch("WHOISFREAKS_API_KEY")
end

api = WhoisFreaks::DatabasesIPGeolocationApi.new

begin
  file = api.db_ip_city(Date.parse("2026-10-01"))
  # The SDK returns a Tempfile that is deleted when the program exits: copy it.
  save_as = "DbIpCity.zip"
  FileUtils.cp(file.path, save_as)
  puts "Saved #{File.expand_path(save_as)} (#{File.size(save_as)} bytes)"
rescue WhoisFreaks::ApiError => e
  warn "Request failed: HTTP #{e.code} #{e.response_body}"
  exit 1
end

```

### Databases - ASN WHOIS

#### ASN WHOIS Snapshot

`GET /v3.3/download/snapshot/asn/whois`

```ruby
# ASN WHOIS Snapshot
#
# Parameters for dbAsnWhois (GET /v3.3/download/snapshot/asn/whois):
#   - date (string, required)

require "date"
require "fileutils"
require "whoisfreaks"

# Read the API key from the environment and set it once.
WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = ENV.fetch("WHOISFREAKS_API_KEY")
end

api = WhoisFreaks::DatabasesASNWHOISApi.new

begin
  file = api.db_asn_whois(Date.parse("2026-10-01"))
  # The SDK returns a Tempfile that is deleted when the program exits: copy it.
  save_as = "DbAsnWhois.json.gz"
  FileUtils.cp(file.path, save_as)
  puts "Saved #{File.expand_path(save_as)} (#{File.size(save_as)} bytes)"
rescue WhoisFreaks::ApiError => e
  warn "Request failed: HTTP #{e.code} #{e.response_body}"
  exit 1
end

```

#### ASN WHOIS Snapshot Status

`GET /v3.3/status/snapshot/asn/whois`

```ruby
# ASN WHOIS Snapshot Status
#
# Parameters for dbAsnWhoisStatus (GET /v3.3/status/snapshot/asn/whois):
#   (no parameters; the API key is set on the client)

require "json"
require "whoisfreaks"

# Read the API key from the environment and set it once.
WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = ENV.fetch("WHOISFREAKS_API_KEY")
end

api = WhoisFreaks::DatabasesASNWHOISApi.new

begin
  result = api.db_asn_whois_status
  puts JSON.pretty_generate(result.to_hash)
rescue WhoisFreaks::ApiError => e
  warn "Request failed: HTTP #{e.code} #{e.response_body}"
  exit 1
end

```

### Databases - IP WHOIS

#### IP WHOIS Snapshot

`GET /v3.3/download/snapshot/ip/whois`

```ruby
# IP WHOIS Snapshot
#
# Parameters for dbIpWhois (GET /v3.3/download/snapshot/ip/whois):
#   - date (string, required)

require "date"
require "fileutils"
require "whoisfreaks"

# Read the API key from the environment and set it once.
WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = ENV.fetch("WHOISFREAKS_API_KEY")
end

api = WhoisFreaks::DatabasesIPWHOISApi.new

begin
  file = api.db_ip_whois(Date.parse("2026-10-01"))
  # The SDK returns a Tempfile that is deleted when the program exits: copy it.
  save_as = "DbIpWhois.json.gz"
  FileUtils.cp(file.path, save_as)
  puts "Saved #{File.expand_path(save_as)} (#{File.size(save_as)} bytes)"
rescue WhoisFreaks::ApiError => e
  warn "Request failed: HTTP #{e.code} #{e.response_body}"
  exit 1
end

```

#### IP WHOIS Snapshot Status

`GET /v3.3/status/snapshot/ip/whois`

```ruby
# IP WHOIS Snapshot Status
#
# Parameters for dbIpWhoisStatus (GET /v3.3/status/snapshot/ip/whois):
#   (no parameters; the API key is set on the client)

require "json"
require "whoisfreaks"

# Read the API key from the environment and set it once.
WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = ENV.fetch("WHOISFREAKS_API_KEY")
end

api = WhoisFreaks::DatabasesIPWHOISApi.new

begin
  result = api.db_ip_whois_status
  puts JSON.pretty_generate(result.to_hash)
rescue WhoisFreaks::ApiError => e
  warn "Request failed: HTTP #{e.code} #{e.response_body}"
  exit 1
end

```

### Databases - IP Security

#### IP Security Snapshot

`GET /v3.3/download/snapshot/ip/security`

```ruby
# IP Security Snapshot
#
# Parameters for dbIpSecurity (GET /v3.3/download/snapshot/ip/security):
#   - date (string, required)

require "date"
require "fileutils"
require "whoisfreaks"

# Read the API key from the environment and set it once.
WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = ENV.fetch("WHOISFREAKS_API_KEY")
end

api = WhoisFreaks::DatabasesIPSecurityApi.new

begin
  file = api.db_ip_security(Date.parse("2026-10-01"))
  # The SDK returns a Tempfile that is deleted when the program exits: copy it.
  save_as = "DbIpSecurity.csv"
  FileUtils.cp(file.path, save_as)
  puts "Saved #{File.expand_path(save_as)} (#{File.size(save_as)} bytes)"
rescue WhoisFreaks::ApiError => e
  warn "Request failed: HTTP #{e.code} #{e.response_body}"
  exit 1
end

```

#### IP Security Snapshot Status

`GET /v3.3/status/snapshot/ip/security`

```ruby
# IP Security Snapshot Status
#
# Parameters for dbIpSecurityStatus (GET /v3.3/status/snapshot/ip/security):
#   (no parameters; the API key is set on the client)

require "json"
require "whoisfreaks"

# Read the API key from the environment and set it once.
WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = ENV.fetch("WHOISFREAKS_API_KEY")
end

api = WhoisFreaks::DatabasesIPSecurityApi.new

begin
  result = api.db_ip_security_status
  puts JSON.pretty_generate(result.to_hash)
rescue WhoisFreaks::ApiError => e
  warn "Request failed: HTTP #{e.code} #{e.response_body}"
  exit 1
end

```

### Databases - Threat Feed

#### Download the daily phishing threat feed (CSV)

`GET /v3.4/download/threat-feed/phishing`

```ruby
# Download the daily phishing threat feed (CSV)
#
# Parameters for downloadThreatFeedPhishing (GET /v3.4/download/threat-feed/phishing):
#   - date (string, optional): Feed date (yyyy-MM-dd); omit for the full dump of the feed

require "fileutils"
require "whoisfreaks"

# Read the API key from the environment and set it once.
WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = ENV.fetch("WHOISFREAKS_API_KEY")
end

api = WhoisFreaks::DatabasesThreatFeedApi.new

begin
  file = api.download_threat_feed_phishing(date: "2026-10-01")
  # The SDK returns a Tempfile that is deleted when the program exits: copy it.
  save_as = "DownloadThreatFeedPhishing.csv"
  FileUtils.cp(file.path, save_as)
  puts "Saved #{File.expand_path(save_as)} (#{File.size(save_as)} bytes)"
rescue WhoisFreaks::ApiError => e
  warn "Request failed: HTTP #{e.code} #{e.response_body}"
  exit 1
end

```

#### Download a sample of the phishing threat feed (CSV)

`GET /v3.4/download/threat-feed/phishing/sample`

```ruby
# Download a sample of the phishing threat feed (CSV)
#
# Parameters for downloadThreatFeedPhishingSample (GET /v3.4/download/threat-feed/phishing/sample):
#   (no parameters; the API key is set on the client)

require "fileutils"
require "whoisfreaks"

# Read the API key from the environment and set it once.
WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = ENV.fetch("WHOISFREAKS_API_KEY")
end

api = WhoisFreaks::DatabasesThreatFeedApi.new

begin
  file = api.download_threat_feed_phishing_sample
  # The SDK returns a Tempfile that is deleted when the program exits: copy it.
  save_as = "DownloadThreatFeedPhishingSample.csv"
  FileUtils.cp(file.path, save_as)
  puts "Saved #{File.expand_path(save_as)} (#{File.size(save_as)} bytes)"
rescue WhoisFreaks::ApiError => e
  warn "Request failed: HTTP #{e.code} #{e.response_body}"
  exit 1
end

```

#### Download the daily malware threat feed (CSV)

`GET /v3.4/download/threat-feed/malware`

```ruby
# Download the daily malware threat feed (CSV)
#
# Parameters for downloadThreatFeedMalware (GET /v3.4/download/threat-feed/malware):
#   - date (string, optional): Feed date (yyyy-MM-dd); omit for the full dump of the feed

require "fileutils"
require "whoisfreaks"

# Read the API key from the environment and set it once.
WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = ENV.fetch("WHOISFREAKS_API_KEY")
end

api = WhoisFreaks::DatabasesThreatFeedApi.new

begin
  file = api.download_threat_feed_malware(date: "2026-10-01")
  # The SDK returns a Tempfile that is deleted when the program exits: copy it.
  save_as = "DownloadThreatFeedMalware.csv"
  FileUtils.cp(file.path, save_as)
  puts "Saved #{File.expand_path(save_as)} (#{File.size(save_as)} bytes)"
rescue WhoisFreaks::ApiError => e
  warn "Request failed: HTTP #{e.code} #{e.response_body}"
  exit 1
end

```

#### Download a sample of the malware threat feed (CSV)

`GET /v3.4/download/threat-feed/malware/sample`

```ruby
# Download a sample of the malware threat feed (CSV)
#
# Parameters for downloadThreatFeedMalwareSample (GET /v3.4/download/threat-feed/malware/sample):
#   (no parameters; the API key is set on the client)

require "fileutils"
require "whoisfreaks"

# Read the API key from the environment and set it once.
WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = ENV.fetch("WHOISFREAKS_API_KEY")
end

api = WhoisFreaks::DatabasesThreatFeedApi.new

begin
  file = api.download_threat_feed_malware_sample
  # The SDK returns a Tempfile that is deleted when the program exits: copy it.
  save_as = "DownloadThreatFeedMalwareSample.csv"
  FileUtils.cp(file.path, save_as)
  puts "Saved #{File.expand_path(save_as)} (#{File.size(save_as)} bytes)"
rescue WhoisFreaks::ApiError => e
  warn "Request failed: HTTP #{e.code} #{e.response_body}"
  exit 1
end

```

#### Download the daily spam threat feed (CSV)

`GET /v3.4/download/threat-feed/spam`

```ruby
# Download the daily spam threat feed (CSV)
#
# Parameters for downloadThreatFeedSpam (GET /v3.4/download/threat-feed/spam):
#   - date (string, optional): Feed date (yyyy-MM-dd); omit for the full dump of the feed

require "fileutils"
require "whoisfreaks"

# Read the API key from the environment and set it once.
WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = ENV.fetch("WHOISFREAKS_API_KEY")
end

api = WhoisFreaks::DatabasesThreatFeedApi.new

begin
  file = api.download_threat_feed_spam(date: "2026-10-01")
  # The SDK returns a Tempfile that is deleted when the program exits: copy it.
  save_as = "DownloadThreatFeedSpam.csv"
  FileUtils.cp(file.path, save_as)
  puts "Saved #{File.expand_path(save_as)} (#{File.size(save_as)} bytes)"
rescue WhoisFreaks::ApiError => e
  warn "Request failed: HTTP #{e.code} #{e.response_body}"
  exit 1
end

```

#### Download a sample of the spam threat feed (CSV)

`GET /v3.4/download/threat-feed/spam/sample`

```ruby
# Download a sample of the spam threat feed (CSV)
#
# Parameters for downloadThreatFeedSpamSample (GET /v3.4/download/threat-feed/spam/sample):
#   (no parameters; the API key is set on the client)

require "fileutils"
require "whoisfreaks"

# Read the API key from the environment and set it once.
WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = ENV.fetch("WHOISFREAKS_API_KEY")
end

api = WhoisFreaks::DatabasesThreatFeedApi.new

begin
  file = api.download_threat_feed_spam_sample
  # The SDK returns a Tempfile that is deleted when the program exits: copy it.
  save_as = "DownloadThreatFeedSpamSample.csv"
  FileUtils.cp(file.path, save_as)
  puts "Saved #{File.expand_path(save_as)} (#{File.size(save_as)} bytes)"
rescue WhoisFreaks::ApiError => e
  warn "Request failed: HTTP #{e.code} #{e.response_body}"
  exit 1
end

```
