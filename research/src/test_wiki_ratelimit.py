import urllib.request
import urllib.parse
import json
import time

headers = {'User-Agent': 'SportsResearchCollector/2.0 (contact: info@sportsresearch.org)'}

def get_page(title):
    url = f"https://en.wikipedia.org/w/api.php?action=parse&page={urllib.parse.quote(title)}&format=json&prop=wikitext"
    try:
        time.sleep(0.8)
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=12) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            wt = data.get('parse', {}).get('wikitext', {}).get('*', '')
            return len(wt), None
    except Exception as e:
        return 0, str(e)

for y in [1981, 1990, 1991, 1992, 1995, 1996, 1998, 2000, 2001]:
    y2 = str((y + 1) % 100).zfill(2)
    if y <= 1990:
        c = f"{y}–{y2} FIBA European Cup Winners' Cup"
    elif y <= 1995:
        c = f"{y}–{y2} FIBA European Cup"
    elif y <= 1997:
        c = f"{y}–{y2} FIBA EuroCup"
    else:
        c = f"{y}–{y2} FIBA Saporta Cup"
        
    length, err = get_page(c)
    print(f"Year {y}: '{c}' -> {length} bytes (err: {err})")
