# Dropped Domains (JSON)
#
# Parameters for dbDroppedJson (GET /v3.1/domains/dropped):
#   - date (string, optional): yyyy-MM-dd; omit for latest
#   - tlds (string, optional)

require "date"
require "whoisfreaks"

# Read the API key from the environment and set it once.
WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = ENV.fetch("WHOISFREAKS_API_KEY")
end

api = WhoisFreaks::DatabasesExpiringDroppedApi.new

begin
  domains = api.db_dropped_json(date: Date.parse("2026-10-01"))
  puts domains
rescue WhoisFreaks::ApiError => e
  warn "Request failed: HTTP #{e.code} #{e.response_body}"
  exit 1
end
