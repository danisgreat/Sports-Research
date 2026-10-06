import urllib.request
import re
import os
import json
import time

CACHE_DIR = os.path.join(os.getcwd(), "research", "data", "match_results_cache")
os.makedirs(CACHE_DIR, exist_ok=True)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

# 1. Fetch World Cup ODI numbers to exclude
wc_url = "https://stats.espncricinfo.com/ci/engine/records/team/match_results.html?class=2;id=12;type=trophy"
req_wc = urllib.request.Request(wc_url, headers=HEADERS)
html_wc = urllib.request.urlopen(req_wc, timeout=15).read().decode("utf-8", errors="replace")

wc_odi_numbers = set()
for r in re.findall(r'<tr class="data1"[^>]*>(.*?)</tr>', html_wc, re.DOTALL):
    m = re.search(r'ODI # (\d+)', r)
    if m:
        wc_odi_numbers.add(f"ODI # {m.group(1)}")

print(f"Loaded {len(wc_odi_numbers)} World Cup ODI identifiers.")

# Save WC match numbers to file
wc_file = os.path.join(os.getcwd(), "research", "data", "wc_odi_numbers.json")
with open(wc_file, "w", encoding="utf-8") as f:
    json.dump(sorted(list(wc_odi_numbers), key=lambda x: int(x.split("# ")[1])), f, indent=2)

def cache_year_match_results(year):
    cache_file = os.path.join(CACHE_DIR, f"match_results_{year}.json")
    if os.path.exists(cache_file):
        with open(cache_file, "r", encoding="utf-8") as f:
            return json.load(f)
            
    url = f"https://stats.espncricinfo.com/ci/engine/records/team/match_results.html?class=2;id={year};type=year"
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        html = urllib.request.urlopen(req, timeout=15).read().decode("utf-8", errors="replace")
    except Exception as e:
        print(f"Error fetching year {year}: {e}")
        return []
        
    rows = re.findall(r'<tr class="data1"[^>]*>(.*?)</tr>', html, re.DOTALL)
    matches = []
    
    for r in rows:
        m = re.search(r'ODI # (\d+)', r)
        if not m:
            continue
        odi_num = f"ODI # {m.group(1)}"
        is_wc = odi_num in wc_odi_numbers
        
        cells = [re.sub(r'<[^>]+>', '', c).strip() for c in re.findall(r'<td[^>]*>(.*?)</td>', r, re.DOTALL)]
        link = re.search(r'/ci/engine/match/(\d+)\.html', r)
        mid = link.group(1) if link else ""
        
        team1 = cells[0]
        team2 = cells[1]
        winner = cells[2]
        if len(cells) == 7:
            margin = cells[3]
            ground = cells[4]
            date_str = cells[5]
        else:
            margin = ""
            ground = cells[3]
            date_str = cells[4]
            
        matches.append({
            "odi_num": odi_num,
            "odi_num_int": int(m.group(1)),
            "match_id": mid,
            "is_world_cup": is_wc,
            "team1": team1,
            "team2": team2,
            "winner": winner,
            "margin": margin,
            "ground": ground,
            "date": date_str
        })
        
    with open(cache_file, "w", encoding="utf-8") as f:
        json.dump(matches, f, indent=2)
    return matches

print("Caching match_results for all 51 years...")
total_matches = 0
total_non_wc = 0
for yr in range(1975, 2026):
    m_list = cache_year_match_results(yr)
    non_wc = [m for m in m_list if not m["is_world_cup"]]
    total_matches += len(m_list)
    total_non_wc += len(non_wc)
    time.sleep(0.04)

print("=" * 70)
print(f"Completed match_results caching:")
print(f"  Total official ODIs: {total_matches}")
print(f"  Total non-World Cup ODIs: {total_non_wc}")
