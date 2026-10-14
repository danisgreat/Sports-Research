import urllib.request
import json
import sys

headers = {'User-Agent': 'Mozilla/5.0'}

for yr in range(2002, 2027):
    url = f'https://api-live.euroleague.net/v2/competitions/U/seasons/U{yr}/games'
    try:
        req = urllib.request.Request(url, headers=headers)
        data = json.loads(urllib.request.urlopen(req, timeout=8).read().decode('utf-8'))
        total = data.get('total', 0)
        games = data.get('data', [])
        played = sum(1 for g in games if g.get('played') and g.get('local', {}).get('score') is not None)
        print(f"Season U{yr}: total={total}, played={played}", flush=True)
    except Exception as e:
        print(f"Season U{yr}: error {e}", flush=True)
