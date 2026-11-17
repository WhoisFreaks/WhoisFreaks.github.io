# Live DNS Lookup
#
# Parameters for dnsLive (GET /v2.0/dns/live):
#   - domain_name (string, optional): Domain to look up.
#   - ip_address (string, optional): Use for PTR lookups
#   - type (string, required): all or comma-separated: A,MX,NS,TXT,SOA,SPF,AAAA,CNAME
#   - cname_depth (integer, optional): How many CNAME links to follow before returning the records they point at. 0, the defau...
#   - relative_records (boolean, optional): Keeps the records picked up for other names along the way, such as a CNAME target's own...
#   - is_authoritative (boolean, optional): Set true to read the records from the zone's own nameservers instead of a recursive res...
#   - format (string (one of: json, xml), optional): Response format. JSON when the parameter is left out.

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
