# Domain Reputation Lookup
#
# Parameters for domainReputation (GET /v1/domain/security):
#   - domain_name (string, required): The domain name to assess
#   - format (string (one of: json, xml), optional)

require "json"
require "whoisfreaks"

# Read the API key from the environment and set it once.
WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = ENV.fetch("WHOISFREAKS_API_KEY")
end

api = WhoisFreaks::DomainReputationApi.new

begin
  result = api.domain_reputation("amazon.com")
  puts JSON.pretty_generate(result.to_hash)
rescue WhoisFreaks::ApiError => e
  warn "Request failed: HTTP #{e.code} #{e.response_body}"
  exit 1
end
