# Subdomains Lookup
#
# Parameters for subdomains (GET /v1.0/subdomains):
#   - domain (string, required): Domain whose subdomains you want.
#   - after (string, optional): Only return records created after this date, in YYYY-MM-DD format. Defaults to the olde...
#   - before (string, optional): Only return records created before this date, in YYYY-MM-DD format. Defaults to today, ...
#   - status (string (one of: active, inactive), optional): Limit results to active or inactive subdomains. Both are returned when the parameter is...
#   - page (integer, optional): Page of results to return. Defaults to 1.
#   - format (string (one of: json, xml), optional): Response format. JSON when the parameter is left out.

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
