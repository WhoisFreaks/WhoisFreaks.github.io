# ASN WHOIS Snapshot Status
#
# Parameters for dbAsnWhoisStatus (GET /v3.3/status/snapshot/asn/whois):
#   (no parameters; the API key is set on the client)

require "json"
require "whoisfreaks"

# Read the API key from the environment and set it once.
WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = ENV.fetch("WHOISFREAKS_API_KEY")
end

api = WhoisFreaks::DatabasesASNWHOISApi.new

begin
  result = api.db_asn_whois_status
  puts JSON.pretty_generate(result.to_hash)
rescue WhoisFreaks::ApiError => e
  warn "Request failed: HTTP #{e.code} #{e.response_body}"
  exit 1
end
