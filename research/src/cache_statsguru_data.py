import urllib.request
import re
import os
import json
import time

CACHE_DIR = os.path.join(os.getcwd(), "research", "data", "statsguru_cache")
os.makedirs(CACHE_DIR, exist_ok=True)

def fetch_statsguru_page(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        html = urllib.request.urlopen(req, timeout=15).read().decode("utf-8", errors="replace")
        return html
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return ""

def get_statsguru_data_for_year(year):
    cache_file = os.path.join(CACHE_DIR, f"statsguru_{year}.json")
    if os.path.exists(cache_file):
        with open(cache_file, "r", encoding="utf-8") as f:
            return json.load(f)
            
    # 1. Fetch view=results
    results_rows = []
    page = 1
    while True:
        url = f"https://stats.espncricinfo.com/ci/engine/stats/index.html?class=2;page={page};spanmax1=31+Dec+{year};spanmin1=01+Jan+{year};spanval1=span;template=results;type=team;view=results"
        html = fetch_statsguru_page(url)
        rows = re.findall(r'<tr class="data1"[^>]*>(.*?)</tr>', html, re.DOTALL)
        if not rows:
            break
        for r in rows:
            cells = [re.sub(r'<[^>]+>', '', c).strip() for c in re.findall(r'<td[^>]*>(.*?)</td>', r, re.DOTALL)]
            if len(cells) >= 10:
                results_rows.append({
                    "team": cells[0],
                    "result": cells[1],
                    "margin": cells[2],
                    "br": cells[3] if len(cells) > 3 else "",
                    "toss": cells[4],
                    "bat": cells[5],
                    "opposition": cells[7].replace("v ", ""),
                    "ground": cells[8],
                    "date": cells[9]
                })
        if 'class="PaginationLink" title="Next page"' not in html:
            break
        page += 1
        time.sleep(0.05)
        
    # 2. Fetch view=match (innings details)
    innings_rows = []
    page = 1
    while True:
        url = f"https://stats.espncricinfo.com/ci/engine/stats/index.html?class=2;page={page};spanmax1=31+Dec+{year};spanmin1=01+Jan+{year};spanval1=span;template=results;type=team;view=match"
        html = fetch_statsguru_page(url)
        rows = re.findall(r'<tr class="data1"[^>]*>(.*?)</tr>', html, re.DOTALL)
        if not rows:
            break
        for r in rows:
            cells = [re.sub(r'<[^>]+>', '', c).strip() for c in re.findall(r'<td[^>]*>(.*?)</td>', r, re.DOTALL)]
            if len(cells) >= 11:
                innings_rows.append({
                    "team": cells[0],
                    "runs": cells[1],
                    "wkts": cells[2],
                    "balls": cells[3],
                    "rpo": cells[5],
                    "result": cells[6],
                    "opposition": cells[8].replace("v ", ""),
                    "ground": cells[9],
                    "date": cells[10]
                })
        if 'class="PaginationLink" title="Next page"' not in html:
            break
        page += 1
        time.sleep(0.05)
        
    data = {
        "year": year,
        "results": results_rows,
        "innings": innings_rows
    }
    with open(cache_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    return data

# Test on 1975 to 1980
print("Testing Statsguru caching for 1975-1980...")
for y in range(1975, 1981):
    d = get_statsguru_data_for_year(y)
    print(f"Year {y}: {len(d['results'])} result rows, {len(d['innings'])} innings rows cached.")
