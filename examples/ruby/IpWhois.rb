# IP WHOIS Lookup
#
# Parameters for ipWhois (GET /v1.0/ip-whois):
#   - ip (string, required): IP address to look up.
#   - format (string (one of: json, xml), optional): Response format. JSON when the parameter is left out.

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
