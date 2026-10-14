import urllib.request
import re

headers = {'User-Agent': 'Mozilla/5.0'}
for ed in [91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30]:
    url = f'https://acb.com/es/liga/calendario?temporada={ed}'
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            chunks = re.findall(r'self\.__next_f\.push\(\[1,"(.*?)"\]\)', html, re.DOTALL)
            full_text = ''.join(c.encode().decode('unicode_escape', errors='ignore') for c in chunks)
            # Look for dates in matches: "startDateTime":"2023-..." or "matchDateTime"
            dates = re.findall(r'"startDateTime":"(\d{4})-\d{2}-\d{2}', full_text)
            if not dates:
                dates = re.findall(r'(\d{4})-\d{2}-\d{2}', full_text)
            years = sorted(list(set(dates)))
            # Also check competition / edition label
            title_m = re.search(r'<title>(.*?)</title>', html)
            title = title_m.group(1) if title_m else ''
            print(f"Edition {ed}: Title: {title} | Sample Years: {years[:5]}")
    except Exception as e:
        print(f"Edition {ed}: error {e}")
