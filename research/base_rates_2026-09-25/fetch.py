"""Small cached fetcher for public JSON endpoints (gzip-aware, no browser User-Agent).

ESPN site API note (verified 2026-09-25): `scoreboard?dates=YYYYMMDD-YYYYMMDD` now returns
HTTP 400 for every range (even 7 days, any limit); single-day `dates=YYYYMMDD` returns 200.
Season pulls therefore go day by day.
"""
import concurrent.futures as cf
import datetime as dt
import gzip
import hashlib
import json
import os
import time
import urllib.request

CACHE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cache')
os.makedirs(CACHE, exist_ok=True)


def get_json(url, tries=3, sleep=0.2):
    key = hashlib.sha1(url.encode()).hexdigest()
    path = os.path.join(CACHE, key + '.json')
    if os.path.exists(path):
        with open(path, encoding='utf-8') as fh:
            return json.load(fh)
    last = None
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={'Accept-Encoding': 'gzip'})
            with urllib.request.urlopen(req, timeout=60) as r:
                raw = r.read()
                if raw[:2] == b'\x1f\x8b':
                    raw = gzip.decompress(raw)
            data = json.loads(raw.decode('utf-8'))
            with open(path, 'w', encoding='utf-8') as fh:
                json.dump(data, fh)
            time.sleep(sleep)
            return data
        except Exception as exc:  # noqa: BLE001
            last = exc
            time.sleep(1.5 * (i + 1))
    raise RuntimeError(f'fetch failed {url}: {last}')


def _days(start, end):
    s = dt.date(int(start[:4]), int(start[4:6]), int(start[6:8]))
    e = dt.date(int(end[:4]), int(end[4:6]), int(end[6:8]))
    while s <= e:
        yield s
        s += dt.timedelta(days=1)


def espn_scoreboard(path, start, end, workers=4):
    """ESPN site API scoreboard, one request per day. Returns {'events': [...]} de-duplicated by id."""
    urls = [f'https://site.api.espn.com/apis/site/v2/sports/{path}/scoreboard?dates={d:%Y%m%d}'
            for d in _days(start, end)]
    events, seen, failed = [], set(), []
    with cf.ThreadPoolExecutor(max_workers=workers) as ex:
        futs = {ex.submit(get_json, u): u for u in urls}
        for f in cf.as_completed(futs):
            try:
                d = f.result()
            except Exception:  # noqa: BLE001
                failed.append(futs[f])
                continue
            for ev in d.get('events', []):
                if ev['id'] not in seen:
                    seen.add(ev['id'])
                    events.append(ev)
    events.sort(key=lambda x: x['date'])
    return {'events': events, 'failed_days': failed, 'n_days': len(urls)}
