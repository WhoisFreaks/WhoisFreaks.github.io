# Reverse DNS Lookup (v2.3)
#
# Parameters for dnsReverseV23 (GET /v2.3/dns/reverse):
#   - value (string, required): IP, CIDR, or record value
#   - type (string (one of: a, mx, cname, ns, aaaa, txt, soa), required)
#   - exact (boolean, optional): When false the value is matched as a substring, which is far slower than an exact match...
#   - page (integer, optional)
#   - sort (string (one of: asc, desc), optional): Sort direction. Omit to leave the results unsorted.
#   - sort_by (string (one of: firstSeen, lastSeen), optional): Field to sort on. Only applies when sort is given.
#   - format (string (one of: json, xml), optional)

require "json"
require "whoisfreaks"

# Read the API key from the environment and set it once.
WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = ENV.fetch("WHOISFREAKS_API_KEY")
end

api = WhoisFreaks::DNSApi.new

begin
  result = api.dns_reverse_v23("8.8.8.8", "a", page: 1)
  puts JSON.pretty_generate(result.to_hash)
rescue WhoisFreaks::ApiError => e
  warn "Request failed: HTTP #{e.code} #{e.response_body}"
  exit 1
end
