import sys
import requests
import json
import re

sys.stdout.reconfigure(encoding='utf-8')

events_to_check = [
    (2, "B1 Regular Season"),
    (3, "B1 Championship Playoffs"),
    (4, "B1 Relegation Playoff"),
    (5, "All-Star Game"),
    (7, "B2 Regular Season"),
    (8, "B2 Playoffs"),
    (20, "Early Cup"),
]

for year in range(2016, 2026):
    year_totals = {}
    for ev_id, ev_name in events_to_check:
        index = 0
        game_count = 0
        while True:
            url = f"https://www.bleague.jp/schedule/?data_format=json&year={year}&event={ev_id}&mon=all&index={index}"
            try:
                resp = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=10).json()
                topics = resp.get('topics', [])
                if not topics:
                    break
                game_count += len(topics)
                next_index = resp.get('index')
                if not next_index or next_index <= index:
                    break
                index = next_index
            except Exception as e:
                break
        if game_count > 0:
            year_totals[ev_name] = game_count
    print(f"Season {year}-{year+1-2000:02d}: {year_totals} (Total: {sum(year_totals.values())})")
