import urllib.request
import re

headers = {'User-Agent': 'Mozilla/5.0'}
url = 'https://acb.com/es/liga/calendario?temporada=88'
req = urllib.request.Request(url, headers=headers)
html = urllib.request.urlopen(req, timeout=10).read().decode('utf-8', errors='ignore')
chunks = re.findall(r'self\.__next_f\.push\(\[1,"(.*?)"\]\)', html, re.DOTALL)
full_text = ''.join(c.encode().decode('unicode_escape', errors='ignore') for c in chunks)

for m in re.finditer(r'"subphase[s]?":', full_text):
    start = max(0, m.start() - 50)
    end = min(len(full_text), m.end() + 200)
    print("Match snippet:", full_text[start:end])
