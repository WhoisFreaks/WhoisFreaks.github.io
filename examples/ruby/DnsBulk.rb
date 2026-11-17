# Bulk DNS Lookup
#
# Parameters for dnsBulk (POST /v2.0/dns/bulk/live):
#   - type (string, required): Comma separated DNS record types to return, for example A,MX,TXT. Defaults to all.
#   - cname_depth (integer, optional): How many CNAME links to follow before returning the records they point at. 0, the defau...
#   - is_authoritative (boolean, optional): Set true to read the records from each zone's own nameservers instead of a recursive re...
#   - format (string (one of: json, xml), optional): Response format. JSON when the parameter is left out.
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
