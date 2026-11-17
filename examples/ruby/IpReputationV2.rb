# IP Reputation Lookup (v2.0)
#
# Parameters for ipReputationV2 (GET /v2.0/security):
#   - ip (string, required): IP address to look up.

require "json"
require "whoisfreaks"

# Read the API key from the environment and set it once.
WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = ENV.fetch("WHOISFREAKS_API_KEY")
end

api = WhoisFreaks::IPReputationApi.new

begin
  result = api.ip_reputation_v2("8.8.8.8")
  puts JSON.pretty_generate(result.to_hash)
rescue WhoisFreaks::ApiError => e
  warn "Request failed: HTTP #{e.code} #{e.response_body}"
  exit 1
end
