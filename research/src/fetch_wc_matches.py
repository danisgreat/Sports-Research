import urllib.request
import re

url = "https://stats.espncricinfo.com/ci/engine/records/team/match_results.html?class=2;id=12;type=trophy"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
html = urllib.request.urlopen(req, timeout=10).read().decode("utf-8", errors="replace")

wc_matches = set()
rows = re.findall(r'<tr class="data1"[^>]*>(.*?)</tr>', html, re.DOTALL)
for r in rows:
    odi_match = re.search(r'ODI # (\d+)', r)
    if odi_match:
        wc_matches.add(f"ODI # {odi_match.group(1)}")

print(f"Total World Cup matches extracted: {len(wc_matches)}")
sample = sorted(list(wc_matches), key=lambda x: int(x.split('# ')[1]))
print(f"First 5: {sample[:5]}")
print(f"Last 5: {sample[-5:]}")
