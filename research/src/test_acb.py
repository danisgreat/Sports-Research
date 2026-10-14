import urllib.request
import re
import json

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

url = 'https://www.acb.com/es/liga/calendario'
req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req, timeout=15) as resp:
    html = resp.read().decode('utf-8', errors='ignore')

print("calendario page length:", len(html))

# Check for JSON data inside script tags
scripts = re.findall(r'<script[^>]*>(.*?)</script>', html, re.DOTALL)
print("Total script tags:", len(scripts))
for i, s in enumerate(scripts):
    if len(s) > 1000 and ('partido' in s or 'jornada' in s or 'teams' in s or 'match' in s):
        print(f"Script {i} length: {len(s)}")
        print("  Snippet:", s[:300].strip())

# Check for match cards in HTML
matches = re.findall(r'href=[\'"]https://live\.acb\.com/es/partidos/([^\'"]+)[\'"]', html)
print(f"Total live.acb.com match links in page: {len(matches)}")
print("Sample match links:", matches[:10])

# Check for season selector
seasons = re.findall(r'<option[^>]*value=[\'"]([^\'"]+)[\'"][^>]*>([^<]+)</option>', html)
print("Dropdown options count:", len(seasons))
for val, text in seasons[:20]:
    print(f"  Option: {val} -> {text.strip()}")
