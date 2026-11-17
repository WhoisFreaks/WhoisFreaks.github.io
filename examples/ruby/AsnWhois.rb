# ASN WHOIS Lookup
#
# Parameters for asnWhois (GET /v2.0/asn-whois):
#   - asn (string, required): Autonomous system number to look up, with or without the AS prefix.
#   - format (string (one of: json, xml), optional): Response format. JSON when the parameter is left out.

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
