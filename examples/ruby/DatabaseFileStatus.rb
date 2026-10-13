# Database File Status (Public)
#
# Parameters for databaseFileStatus (GET /v3.4/status):
#   (no parameters; no API key required)

require "json"
require "whoisfreaks"

# Read the API key from the environment and set it once.
# (This endpoint is public, so the key is not sent with this request.)
WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = ENV.fetch("WHOISFREAKS_API_KEY")
end

api = WhoisFreaks::AccountApi.new

begin
  result = api.database_file_status
  puts JSON.pretty_generate(result.to_hash)
rescue WhoisFreaks::ApiError => e
  warn "Request failed: HTTP #{e.code} #{e.response_body}"
  exit 1
end
