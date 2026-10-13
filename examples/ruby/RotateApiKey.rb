# Rotate API Key
#
# Parameters for rotateApiKey (GET /v1.0/api-key/rotate):
#   (no parameters; the API key is set on the client)

require "whoisfreaks"

# Read the API key from the environment and set it once.
WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = ENV.fetch("WHOISFREAKS_API_KEY")
end

api = WhoisFreaks::AccountApi.new

begin
  new_key = api.rotate_api_key
  # The old key stops working now: store the new one before making more calls.
  puts "New API key: #{new_key}"
rescue WhoisFreaks::ApiError => e
  warn "Request failed: HTTP #{e.code} #{e.response_body}"
  exit 1
end
