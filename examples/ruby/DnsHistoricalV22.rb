# Historical DNS Lookup (v2.2)
#
# Parameters for dnsHistoricalV22 (GET /v2.2/dns/historical):
#   - domain_name (string, required)
#   - type (string, required)
#   - page (integer, optional)
#   - sort (string (one of: asc, desc), optional): Sort direction. Omit to leave the results unsorted.
#   - sort_by (string (one of: firstSeen, lastSeen), optional): Field to sort on. Only applies when sort is given.
#   - format (string (one of: json, xml), optional)

require "json"
require "whoisfreaks"

# Read the API key from the environment and set it once.
WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = ENV.fetch("WHOISFREAKS_API_KEY")
end

api = WhoisFreaks::DNSApi.new

begin
  result = api.dns_historical_v22("whoisfreaks.com", "A,MX,TXT", page: 1)
  puts JSON.pretty_generate(result.to_hash)
rescue WhoisFreaks::ApiError => e
  warn "Request failed: HTTP #{e.code} #{e.response_body}"
  exit 1
end
