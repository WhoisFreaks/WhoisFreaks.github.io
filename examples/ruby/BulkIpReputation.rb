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
