import os
import time
import json
import requests

os.makedirs('research/data/kbl', exist_ok=True)

headers = {
    'teamcode': 'XX',
    'lang': 'ko',
    'channel': 'WEB',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
}

# 1. Fetch seasons list
r = requests.get('https://api.kbl.or.kr/season/list?seasonCategory=R&gameCode=01&seasonGrade=1', headers=headers)
seasons = r.json()

with open('research/data/kbl/seasons_list.json', 'w', encoding='utf-8') as f:
    json.dump(seasons, f, ensure_ascii=False, indent=2)

print(f'Fetched {len(seasons)} seasons from KBL API.')

# 2. For each season, fetch the full match list
# Date buffers: start from Aug 1 to June 30 of the season cycle
total_matches = 0
summary = []

for s in sorted(seasons, key=lambda x: x['seasonCode']):
    sc = s['seasonCode']
    sn = s['seasonName']
    ds = s.get('gamedateStart')
    de = s.get('gamedateEnd')
    
    # Expand date window to catch preseason cups, all-stars, and postseasons
    start_year = int(ds[:4])
    end_year = int(de[:4])
    query_start = f'{start_year}0801' if start_year == end_year else f'{start_year}0801'
    query_end = f'{end_year}0630'
    
    # For season 1 (1997), start in 19970101
    if sc == 1:
        query_start = '19970101'
        query_end = '19970531'
    elif sc == 2:
        query_start = '19970901'
        query_end = '19980531'
        
    cache_file = f'research/data/kbl/kbl_matches_s{sc}_{sn.replace("/", "_")}.json'
    
    if os.path.exists(cache_file):
        with open(cache_file, 'r', encoding='utf-8') as f:
            matches = json.load(f)
    else:
        url = f'https://api.kbl.or.kr/match/list?fromDate={query_start}&toDate={query_end}&tcodeList=all'
        resp = requests.get(url, headers=headers, timeout=15)
        matches = resp.json()
        with open(cache_file, 'w', encoding='utf-8') as f:
            json.dump(matches, f, ensure_ascii=False, indent=2)
        time.sleep(0.15)
        
    tier1_matches = [m for m in matches if m.get('seasonGrade') == 1]
    summary.append((sc, sn, len(matches), len(tier1_matches)))
    total_matches += len(tier1_matches)
    print(f'Season {sc:2d} ({sn:10s}): Total={len(matches):3d}, Tier-1={len(tier1_matches):3d}')

print(f'=== Grand Total Tier-1 KBL Matches: {total_matches} ===')
