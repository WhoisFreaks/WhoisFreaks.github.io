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
