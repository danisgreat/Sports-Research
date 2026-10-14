import urllib.request
import re
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

url = 'https://live.acb.com/es/partidos/barca-vs-valencia-basket-105401/resumen'
req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req, timeout=15) as resp:
    html = resp.read().decode('utf-8', errors='ignore')

next_chunks = re.findall(r'self\.__next_f\.push\(\[1,"(.*?)"\]\)', html, re.DOTALL)
full_text = ''.join(c.encode().decode('unicode_escape', errors='ignore') for c in next_chunks)

# Find json blocks for matchDetails or initialMatchHeader
for target in ['initialMatchHeader', 'matchDetails', 'statsByQuarters', 'referees']:
    pos = full_text.find(f'"{target}":')
    if pos != -1:
        print(f"=== {target} ===")
        print(full_text[pos:pos+400])
