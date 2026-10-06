import urllib.request
import re

url = "https://stats.espncricinfo.com/ci/engine/records/team/match_results.html?class=2;id=1975;type=year"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
html = urllib.request.urlopen(req, timeout=10).read().decode("utf-8", errors="replace")

# Print the text in the table
lines = [l.strip() for l in re.findall(r'<tr[^>]*>(.*?)</tr>', html, re.DOTALL)]
print(f"Total tr rows in 1975 page: {len(lines)}")
for idx, l in enumerate(lines):
    text = " | ".join([re.sub(r'<[^>]+>', '', c).strip() for c in re.findall(r'<td[^>]*>(.*?)</td>', l, re.DOTALL)])
    if text:
        print(f"Row {idx}: {text}")

# Check any footer or notes
notes = re.findall(r'<div class="ciNotes"[^>]*>(.*?)</div>', html, re.DOTALL)
print("Notes:", notes)
