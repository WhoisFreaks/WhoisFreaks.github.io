# IP Geolocation Lookup
#
# Parameters for geolocation (GET /v1.0/geolocation):
#   - ip (string, required)

require "json"
require "whoisfreaks"

# Read the API key from the environment and set it once.
WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = ENV.fetch("WHOISFREAKS_API_KEY")
end

api = WhoisFreaks::GeolocationApi.new

begin
  result = api.geolocation("8.8.8.8")
  puts JSON.pretty_generate(result.to_hash)
rescue WhoisFreaks::ApiError => e
  warn "Request failed: HTTP #{e.code} #{e.response_body}"
  exit 1
end
