import sys
import requests
import re

sys.stdout.reconfigure(encoding='utf-8')

months = ['09', '10', '11', '12', '01', '02', '03', '04', '05', '06']
total_keys = set()

for m in months:
    url = f"https://www.bleague.jp/schedule/?tab=1&year=2023&mon={m}"
    resp = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=15)
    keys = set(re.findall(r'ScheduleKey=(\d+)', resp.text))
    print(f"Month {m}: found {len(keys)} keys")
    total_keys.update(keys)

print(f"Total unique B1 keys found across all months for 2023: {len(total_keys)}")
