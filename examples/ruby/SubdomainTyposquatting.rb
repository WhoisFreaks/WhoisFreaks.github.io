# Subdomain Typosquatting Lookup
#
# Parameters for subdomainTyposquatting (GET /v3.0/subdomains/typos):
#   - keyword (string, optional): Brand or label to find typo variants for. 3 to 63 characters, letters, digits and hyphe...
#   - pattern (string, optional): Wildcard search string, where '*' matches any characters and '?' matches one. At most 2...
#   - page_token (string, optional): Token from nextPageToken in the previous response, needed from page 2 onward. Send it w...
#   - fetch_size (integer, optional): Subdomains per page. 100 when the parameter is left out, and values above 10000 are cap...

require "json"
require "whoisfreaks"

# Read the API key from the environment and set it once.
WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = ENV.fetch("WHOISFREAKS_API_KEY")
end

api = WhoisFreaks::TyposquattingApi.new

begin
  result = api.subdomain_typosquatting(keyword: "paypal")
  puts JSON.pretty_generate(result.to_hash)
rescue WhoisFreaks::ApiError => e
  warn "Request failed: HTTP #{e.code} #{e.response_body}"
  exit 1
end
