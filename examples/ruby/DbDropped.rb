# Dropped Domains
#
# Parameters for dbDropped (GET /v3.1/download/domainer/dropped):
#   - whois (boolean, required)
#   - date (string, optional): yyyy-MM-dd; omit for latest

require "date"
require "fileutils"
require "whoisfreaks"

# Read the API key from the environment and set it once.
WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = ENV.fetch("WHOISFREAKS_API_KEY")
end

api = WhoisFreaks::DatabasesExpiringDroppedApi.new

begin
  file = api.db_dropped(true, date: Date.parse("2026-10-01"))
  # The SDK returns a Tempfile that is deleted when the program exits: copy it.
  save_as = "DbDropped.csv"
  FileUtils.cp(file.path, save_as)
  puts "Saved #{File.expand_path(save_as)} (#{File.size(save_as)} bytes)"
rescue WhoisFreaks::ApiError => e
  warn "Request failed: HTTP #{e.code} #{e.response_body}"
  exit 1
end
