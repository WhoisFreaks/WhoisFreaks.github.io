# SSL Certificate Lookup
#
# Parameters for sslLookup (GET /v1.0/ssl/live):
#   - domain_name (string, required)
#   - chain (boolean, optional)
#   - ssl_raw (boolean, optional)
#   - format (string (one of: json, xml), optional)

require "json"
require "whoisfreaks"

# Read the API key from the environment and set it once.
WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = ENV.fetch("WHOISFREAKS_API_KEY")
end

api = WhoisFreaks::SSLApi.new

begin
  result = api.ssl_lookup("whoisfreaks.com")
  puts JSON.pretty_generate(result.to_hash)
rescue WhoisFreaks::ApiError => e
  warn "Request failed: HTTP #{e.code} #{e.response_body}"
  exit 1
end
