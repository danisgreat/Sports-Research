import sys
import requests
import json

sys.stdout.reconfigure(encoding='utf-8')
headers = {'User-Agent': 'Mozilla/5.0'}

queries = [
    "bjリーグ 2005",
    "bjリーグ 2015",
    "NBL 2013-14 バスケットボール",
    "バスケットボール日本リーグ 1975",
    "バスケットボール日本リーグ 1980",
    "天皇杯 バスケットボール 2023",
]

for q in queries:
    url = f"https://ja.wikipedia.org/w/api.php?action=query&list=search&srsearch={q}&format=json"
    r = requests.get(url, headers=headers).json()
    hits = r.get('query', {}).get('search', [])
    print(f"\nQuery: '{q}' -> {len(hits)} results:")
    for h in hits[:4]:
        print(f"  - {h['title']}")
