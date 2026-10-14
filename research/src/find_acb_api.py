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

# Look for api urls in the js chunks
chunks = re.findall(r'/_next/static/chunks/[a-zA-Z0-9_\-\.]+\.js', html)
print("JS chunks found:", len(chunks))

api_urls = []
for c in chunks[:5]:
    try:
        req_c = urllib.request.Request(f'https://live.acb.com{c}', headers=headers)
        with urllib.request.urlopen(req_c, timeout=5) as resp_c:
            js_text = resp_c.read().decode('utf-8', errors='ignore')
            found = re.findall(r'https?://[^\s"\'<>`]+\bapi\b[^\s"\'<>`]*', js_text)
            api_urls.extend(found)
    except Exception as e:
        pass

print("API URLs discovered in JS chunks:", set(api_urls))
