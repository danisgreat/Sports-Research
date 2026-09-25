"""Pull NFL, AFL and NRL seasons from the ESPN site API (one date per call, cached) — 2026-09-25(e).

These leagues had no population reference at all (every card printed NOT_YET_DERIVED), and they
carry the framework's worst Rank-1/Rank-2 record. The pulls feed oval_base_rates.py and the TB-1
validation. Market-blind: only scores, dates, venues and neutral-site flags are read.
The season list is research/base_rates_2026-09-25/pull_oval_specs.py.
Usage: python pull_oval.py
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
BR = os.path.join(HERE, '..', 'base_rates_2026-09-25')
sys.path.insert(0, BR)
os.chdir(BR)
from fetch import espn_scoreboard  # noqa: E402
from pull_oval_specs import OVAL  # noqa: E402

if __name__ == '__main__':
    for label, (path, s, e, _k) in OVAL.items():
        d = espn_scoreboard(path, s, e)
        done = sum(1 for x in d['events'] if x['status']['type'].get('completed'))
        print(label, 'days', d['n_days'], 'failed', len(d['failed_days']), 'events', len(d['events']), 'completed', done,
              flush=True)
