import urllib.request
import re

headers = {'User-Agent': 'Mozilla/5.0'}
for ed in [87, 86, 85, 84, 83, 82, 81, 80, 75, 70, 60, 50, 40, 30]:
    url = f'https://acb.com/es/liga/calendario?temporada={ed}'
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            chunks = re.findall(r'self\.__next_f\.push\(\[1,"(.*?)"\]\)', html, re.DOTALL)
            full_text = ''.join(c.encode().decode('unicode_escape', errors='ignore') for c in chunks)
            yr_m = re.search(r'"seasonStartYear":(\d{4})', full_text)
            yr = yr_m.group(1) if yr_m else 'unknown'
            has_rounds = '"rounds":' in full_text
            num_matches = len(re.findall(r'"roundNumber":', full_text))
            print(f"Edition {ed}: year={yr}, rounds_found={has_rounds}, num_rounds_tags={num_matches}")
    except Exception as e:
        print(f"Edition {ed}: error {e}")
