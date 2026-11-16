# Stream newly registered gTLD domains (CSV)
#
# Parameters for streamDomainerGtld (GET /v3.3/stream/domainer/gtld):
#   - date (string, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints.
#   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
#   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
#   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...

require "date"
require "whoisfreaks"

# Read the API key from the environment and set it once.
WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = ENV.fetch("WHOISFREAKS_API_KEY")
end

api = WhoisFreaks::DatabasesStreamingApi.new

begin
  result = api.stream_domainer_gtld(Date.parse("2026-10-01"))
  puts result
rescue WhoisFreaks::ApiError => e
  warn "Request failed: HTTP #{e.code} #{e.response_body}"
  exit 1
end
