import requests
import json
from collections import Counter

headers = {
    'teamcode': 'XX',
    'lang': 'ko',
    'channel': 'WEB',
    'User-Agent': 'Mozilla/5.0'
}

# Test across 3 seasons: 1997 (spring), 2012-13 (pro-am era), 2023-24 (cup + all-star + playoffs)
ranges = [
    ('1997', '19970101', '19970531'),
    ('2012-13', '20120901', '20130531'),
    ('2023-24', '20230901', '20240531'),
]

for label, start, end in ranges:
    url = f'https://api.kbl.or.kr/match/list?fromDate={start}&toDate={end}&tcodeList=all'
    r = requests.get(url, headers=headers)
    matches = r.json()
    cats = Counter((m.get('gameCode'), m.get('seasonCategoryName')) for m in matches)
    print(f'=== {label} Total matches: {len(matches)} ===')
    for (gc, scn), count in cats.items():
        print(f'  gameCode: {gc} | Category: {ascii(scn)} -> {count} games')
