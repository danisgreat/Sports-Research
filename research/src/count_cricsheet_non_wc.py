import os
import json

MATCHES_DIR = os.path.join(os.getcwd(), "research", "data", "cricsheet_odi", "matches")

wc_count = 0
non_wc_count = 0
years_coverage = {}

for fname in os.listdir(MATCHES_DIR):
    if not fname.endswith(".json"):
        continue
    fpath = os.path.join(MATCHES_DIR, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        data = json.load(f)
    info = data.get("info", {})
    dates = info.get("dates", [])
    if not dates:
        continue
    yr = int(dates[0].split("-")[0])
    if yr > 2025:
        continue
    event = (info.get("event", {}).get("name") or "").lower()
    # Check if World Cup main tournament
    is_wc = False
    if "world cup" in event:
        # Check if it's qualifier or league 2 or super league
        if "qualifier" in event or "league 2" in event or "super league" in event or "play-off" in event:
            is_wc = False
        else:
            is_wc = True
            
    if is_wc:
        wc_count += 1
    else:
        non_wc_count += 1
        years_coverage[yr] = years_coverage.get(yr, 0) + 1

print(f"In Cricsheet (2002-2025):")
print(f"  World Cup matches: {wc_count}")
print(f"  Non-World Cup matches: {non_wc_count}")
print("\nNon-World Cup matches per year in Cricsheet:")
for yr in sorted(years_coverage.keys()):
    print(f"  {yr}: {years_coverage[yr]}")
