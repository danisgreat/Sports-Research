import urllib.request
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

for ed in [91, 90, 89, 88, 87]:
    url = f"https://acb.com/es/liga/calendario?temporada={ed}"
    req = urllib.request.Request(url, headers=headers)
    try:
        html = urllib.request.urlopen(req, timeout=12).read().decode('utf-8', errors='ignore')
        matches = set(re.findall(r'"id":(\d{6})', html))
        rounds = set(re.findall(r'"roundNumber":(\d+)', html))
        print(f"Edition {ed}: HTML len={len(html)}, matches={len(matches)}, rounds={len(rounds)}")
    except Exception as e:
        print(f"Edition {ed}: error {e}")
