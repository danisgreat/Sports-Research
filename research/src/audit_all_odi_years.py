import urllib.request
import re
import json
import time
import os

# First load World Cup match IDs
WC_URL = "https://stats.espncricinfo.com/ci/engine/records/team/match_results.html?class=2;id=12;type=trophy"
req = urllib.request.Request(WC_URL, headers={"User-Agent": "Mozilla/5.0"})
html = urllib.request.urlopen(req, timeout=15).read().decode("utf-8", errors="replace")

wc_odi_numbers = set()
for r in re.findall(r'<tr class="data1"[^>]*>(.*?)</tr>', html, re.DOTALL):
    m = re.search(r'ODI # (\d+)', r)
    if m:
        wc_odi_numbers.add(f"ODI # {m.group(1)}")

print(f"Loaded {len(wc_odi_numbers)} World Cup ODI identifiers.")

yearly_stats = {}
total_all_odis = 0
total_all_non_wc = 0
total_all_wc = 0

for yr in range(1975, 2026):
    url = f"https://stats.espncricinfo.com/ci/engine/records/team/match_results.html?class=2;id={yr};type=year"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        html = urllib.request.urlopen(req, timeout=15).read().decode("utf-8", errors="replace")
        rows = re.findall(r'<tr class="data1"[^>]*>(.*?)</tr>', html, re.DOTALL)
        
        matches = []
        wc_in_year = 0
        non_wc_in_year = 0
        
        for r in rows:
            m = re.search(r'ODI # (\d+)', r)
            if not m:
                continue
            odi_num = f"ODI # {m.group(1)}"
            is_wc = odi_num in wc_odi_numbers
            if is_wc:
                wc_in_year += 1
            else:
                non_wc_in_year += 1
                
        yearly_stats[yr] = {
            "total_odis": len(rows),
            "wc_matches": wc_in_year,
            "non_wc_matches": non_wc_in_year
        }
        total_all_odis += len(rows)
        total_all_wc += wc_in_year
        total_all_non_wc += non_wc_in_year
        
        if yr % 5 == 0 or wc_in_year > 0:
            print(f"Year {yr:4d}: Total {len(rows):3d} | WC: {wc_in_year:2d} | Non-WC: {non_wc_in_year:3d}")
    except Exception as e:
        print(f"Year {yr}: Error: {e}")
    time.sleep(0.1)

print("=" * 80)
print(f"Grand Totals (1975-2025):")
print(f"  Total ODIs in history: {total_all_odis}")
print(f"  Total World Cup ODIs:  {total_all_wc}")
print(f"  Total Non-World Cup ODIs: {total_all_non_wc}")
print("=" * 80)

# Save to json for reuse
out_path = os.path.join(os.getcwd(), "research", "data", "yearly_odi_counts.json")
os.makedirs(os.path.dirname(out_path), exist_ok=True)
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(yearly_stats, f, indent=2)
print(f"Saved counts to {out_path}")
