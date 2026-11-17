# Newly Registered gTLD (CSV)
#
# Parameters for dbNewlyGtld (GET /v3.1/download/domainer/gtld):
#   - whois (boolean, required): Set true for the file with full WHOIS records, false for domain names only.
#   - date (string, optional): yyyy-MM-dd; omit for latest
#   - tlds (string, optional): Comma separated TLDs to limit the file to, for example com,net. Every TLD is included w...

require "date"
require "fileutils"
require "whoisfreaks"

# Read the API key from the environment and set it once.
WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = ENV.fetch("WHOISFREAKS_API_KEY")
end

api = WhoisFreaks::DatabasesNewlyRegisteredApi.new

begin
  file = api.db_newly_gtld(true, date: Date.parse("2026-10-01"))
  # The SDK returns a Tempfile that is deleted when the program exits: copy it.
  save_as = "DbNewlyGtld.csv"
  FileUtils.cp(file.path, save_as)
  puts "Saved #{File.expand_path(save_as)} (#{File.size(save_as)} bytes)"
rescue WhoisFreaks::ApiError => e
  warn "Request failed: HTTP #{e.code} #{e.response_body}"
  exit 1
end
