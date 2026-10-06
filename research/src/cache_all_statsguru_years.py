import urllib.request
import re
import os
import json
import time

CACHE_DIR = os.path.join(os.getcwd(), "research", "data", "statsguru_cache")
os.makedirs(CACHE_DIR, exist_ok=True)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def fetch_statsguru_page(url, retries=3):
    req = urllib.request.Request(url, headers=HEADERS)
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(req, timeout=15) as resp:
                return resp.read().decode("utf-8", errors="replace")
        except Exception as e:
            if attempt == retries - 1:
                print(f"Failed to fetch {url}: {e}")
                return ""
            time.sleep(1)
    return ""

def get_statsguru_data_for_year(year, force=False):
    cache_file = os.path.join(CACHE_DIR, f"statsguru_{year}.json")
    if not force and os.path.exists(cache_file):
        with open(cache_file, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
                # Verify it has all pages (if len is not a multiple of 50 or if properly verified)
                if data.get("complete", False):
                    return data
            except:
                pass
            
    # 1. Fetch view=results
    results_rows = []
    page = 1
    total_pages = 1
    while page <= total_pages:
        url = f"https://stats.espncricinfo.com/ci/engine/stats/index.html?class=2;page={page};spanmax1=31+Dec+{year};spanmin1=01+Jan+{year};spanval1=span;template=results;type=team;view=results"
        html = fetch_statsguru_page(url)
        m_pag = re.search(r'Page <b>\d+</b> of <b>(\d+)</b>', html)
        if m_pag:
            total_pages = int(m_pag.group(1))
            
        rows = re.findall(r'<tr class="data1"[^>]*>(.*?)</tr>', html, re.DOTALL)
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
        page += 1
        time.sleep(0.04)
        
    # 2. Fetch view=match (innings details)
    innings_rows = []
    page = 1
    total_pages = 1
    while page <= total_pages:
        url = f"https://stats.espncricinfo.com/ci/engine/stats/index.html?class=2;page={page};spanmax1=31+Dec+{year};spanmin1=01+Jan+{year};spanval1=span;template=results;type=team;view=match"
        html = fetch_statsguru_page(url)
        m_pag = re.search(r'Page <b>\d+</b> of <b>(\d+)</b>', html)
        if m_pag:
            total_pages = int(m_pag.group(1))
            
        rows = re.findall(r'<tr class="data1"[^>]*>(.*?)</tr>', html, re.DOTALL)
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
        page += 1
        time.sleep(0.04)
        
    data = {
        "year": year,
        "complete": True,
        "results": results_rows,
        "innings": innings_rows
    }
    with open(cache_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    return data

def main():
    print("Beginning Complete Statsguru data caching for all 51 years (1975-2025)...")
    total_res = 0
    total_inn = 0
    for yr in range(1975, 2026):
        d = get_statsguru_data_for_year(yr, force=True)
        r_cnt = len(d.get("results", []))
        i_cnt = len(d.get("innings", []))
        total_res += r_cnt
        total_inn += i_cnt
        print(f"Year {yr:4d}: {r_cnt:3d} team results | {i_cnt:3d} team innings cached.")
    print("=" * 70)
    print(f"Caching complete! Total results: {total_res}, Total innings: {total_inn}")

if __name__ == "__main__":
    main()
