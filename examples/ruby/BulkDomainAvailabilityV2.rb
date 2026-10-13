# Bulk Domain Availability Check
#
# Parameters for bulkDomainAvailabilityV2 (POST /v2.0/domain/availability):
#   - domain (string, optional): Required for TLD-mode bulk check (base domain).
#   - format (string (one of: json, xml), optional)
#   - body: BulkDomainAvailabilityRequest (required): request body object

require "json"
require "whoisfreaks"

# Read the API key from the environment and set it once.
WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = ENV.fetch("WHOISFREAKS_API_KEY")
end

api = WhoisFreaks::DomainAvailabilityApi.new

request = WhoisFreaks::BulkDomainAvailabilityRequest.new(domain_names: ["whoisfreaks.com", "example.com"])

begin
  result = api.bulk_domain_availability_v2(request)
  puts JSON.pretty_generate(result.to_hash)
rescue WhoisFreaks::ApiError => e
  warn "Request failed: HTTP #{e.code} #{e.response_body}"
  exit 1
end
