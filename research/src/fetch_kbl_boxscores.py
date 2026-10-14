import os
import sqlite3
import json
import time
import glob
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

db_path = 'research/data/kbl/kbl_boxscores.db'
conn = sqlite3.connect(db_path)
conn.execute('''
CREATE TABLE IF NOT EXISTS boxscores (
    gmkey TEXT PRIMARY KEY,
    json_data TEXT
)
''')
conn.commit()

# Find existing cached gmkeys
cached_keys = set(r[0] for r in conn.execute('SELECT gmkey FROM boxscores'))
print(f'Already cached in SQLite: {len(cached_keys)} boxscores.')

# Gather all gmkeys from match files that have been played
all_matches = []
for f in glob.glob('research/data/kbl/kbl_matches_s*.json'):
    with open(f, 'r', encoding='utf-8') as fp:
        matches = json.load(fp)
        for m in matches:
            gm = m.get('gmkey')
            scoreH = m.get('scoreH')
            isEnded = m.get('isEnded')
            if gm and (isEnded == 1 or (scoreH is not None and scoreH > 0)):
                all_matches.append(gm)

keys_to_fetch = [k for k in set(all_matches) if k not in cached_keys]
print(f'Total played matches to fetch: {len(keys_to_fetch)}')

headers = {
    'teamcode': 'XX',
    'lang': 'ko',
    'channel': 'WEB',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
}

def fetch_boxscore(gmkey):
    url = f'https://api.kbl.or.kr/match/{gmkey}'
    try:
        r = requests.get(url, headers=headers, timeout=10)
        if r.status_code == 200:
            return gmkey, json.dumps(r.json(), ensure_ascii=False)
    except Exception as e:
        pass
    return gmkey, None

BATCH_SIZE = 100
t0 = time.time()
fetched_count = 0

with ThreadPoolExecutor(max_workers=20) as executor:
    futures = {executor.submit(fetch_boxscore, k): k for k in keys_to_fetch}
    batch = []
    for fut in as_completed(futures):
        gmkey, data = fut.result()
        if data:
            batch.append((gmkey, data))
            fetched_count += 1
            if len(batch) >= BATCH_SIZE:
                conn.executemany('INSERT OR REPLACE INTO boxscores VALUES (?, ?)', batch)
                conn.commit()
                batch = []
                elapsed = time.time() - t0
                rate = fetched_count / elapsed if elapsed > 0 else 0
                print(f'Progress: {fetched_count}/{len(keys_to_fetch)} fetched ({rate:.1f} req/s)')
    if batch:
        conn.executemany('INSERT OR REPLACE INTO boxscores VALUES (?, ?)', batch)
        conn.commit()

conn.close()
elapsed = time.time() - t0
print(f'Done! Successfully fetched {fetched_count} boxscores in {elapsed:.2f} seconds.')
