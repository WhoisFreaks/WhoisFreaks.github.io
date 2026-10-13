# Typosquatting Lookup
#
# Parameters for typosquatting (GET /v3.0/domain/typos):
#   - keyword (string, optional)
#   - pattern (string, optional)
#   - page_token (string, optional)

require "json"
require "whoisfreaks"

# Read the API key from the environment and set it once.
WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = ENV.fetch("WHOISFREAKS_API_KEY")
end

api = WhoisFreaks::TyposquattingApi.new

begin
  result = api.typosquatting(keyword: "whoisfreaks")
  puts JSON.pretty_generate(result.to_hash)
rescue WhoisFreaks::ApiError => e
  warn "Request failed: HTTP #{e.code} #{e.response_body}"
  exit 1
end
