import os
import json
from collections import defaultdict

MATCHES_DIR = os.path.join(os.getcwd(), "research", "data", "cricsheet_odi", "matches")

year_counts = defaultdict(int)
total = 0
events = set()

for fname in os.listdir(MATCHES_DIR):
    if not fname.endswith(".json"):
        continue
    fpath = os.path.join(MATCHES_DIR, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        data = json.load(f)
    info = data.get("info", {})
    dates = info.get("dates", [])
    if dates:
        yr = int(dates[0].split("-")[0])
        year_counts[yr] += 1
        total += 1
    event = info.get("event", {}).get("name")
    if event:
        events.add(event)

print(f"Total matches in Cricsheet: {total}")
print("Coverage by year:")
for yr in sorted(year_counts.keys()):
    print(f"  {yr}: {year_counts[yr]} matches")

world_cup_events = [e for e in events if "world cup" in e.lower()]
print("\nSample World Cup event names:")
for e in sorted(world_cup_events)[:15]:
    print("  -", e)
