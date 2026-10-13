# WHOIS Database Weekly
#
# Parameters for dbWhoisWeekly (GET /v3.3/download/dbupdate/weekly/domains/whois):
#   - date (string, optional): yyyy-MM-dd; omit for latest

require "date"
require "fileutils"
require "whoisfreaks"

# Read the API key from the environment and set it once.
WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = ENV.fetch("WHOISFREAKS_API_KEY")
end

api = WhoisFreaks::DatabasesWHOISApi.new

begin
  file = api.db_whois_weekly(date: Date.parse("2026-10-01"))
  # The SDK returns a Tempfile that is deleted when the program exits: copy it.
  save_as = "DbWhoisWeekly.csv"
  FileUtils.cp(file.path, save_as)
  puts "Saved #{File.expand_path(save_as)} (#{File.size(save_as)} bytes)"
rescue WhoisFreaks::ApiError => e
  warn "Request failed: HTTP #{e.code} #{e.response_body}"
  exit 1
end
