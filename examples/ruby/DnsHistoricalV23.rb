# Historical DNS Lookup (v2.3)
#
# Parameters for dnsHistoricalV23 (GET /v2.3/dns/historical):
#   - domain_name (string, required): Domain to look up.
#   - type (string, required): Comma separated DNS record types to return, for example A,MX,TXT. Defaults to all.
#   - page (integer, optional): Page of results to return. Defaults to 1.
#   - sort (string (one of: asc, desc), optional): Sort direction. Omit to leave the results unsorted.
#   - sort_by (string (one of: firstSeen, lastSeen), optional): Field to sort on. Only applies when sort is given.
#   - format (string (one of: json, xml), optional): Response format. JSON when the parameter is left out.

require "json"
require "whoisfreaks"

# Read the API key from the environment and set it once.
WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = ENV.fetch("WHOISFREAKS_API_KEY")
end

api = WhoisFreaks::DNSApi.new

begin
  result = api.dns_historical_v23("whoisfreaks.com", "A,MX,TXT", page: 1)
  puts JSON.pretty_generate(result.to_hash)
rescue WhoisFreaks::ApiError => e
  warn "Request failed: HTTP #{e.code} #{e.response_body}"
  exit 1
end
