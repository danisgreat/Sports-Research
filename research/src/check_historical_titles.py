import urllib.request
import urllib.parse
import json

headers = {'User-Agent': 'SportsResearchBot/1.0'}

def check_title(title):
    url = f"https://en.wikipedia.org/w/api.php?action=parse&page={urllib.parse.quote(title)}&format=json&prop=wikitext"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            wt = data.get('parse', {}).get('wikitext', {}).get('*', '')
            return len(wt)
    except Exception as e:
        return 0

for y in range(1975, 2002):
    y2 = str((y + 1) % 100).zfill(2)
    y2_long = str(y + 1)
    
    if y <= 1990:
        candidates = [
            f"{y}–{y2} FIBA European Cup Winners' Cup",
            f"{y}–{y2} FIBA European Cup Winner's Cup"
        ]
    elif y <= 1995:
        candidates = [
            f"{y}–{y2} FIBA European Cup"
        ]
    elif y <= 1997:
        candidates = [
            f"{y}–{y2} FIBA EuroCup"
        ]
    else:
        candidates = [
            f"{y}–{y2} FIBA Saporta Cup",
            f"{y}–{y2_long} FIBA Saporta Cup"
        ]
        
    found = False
    for c in candidates:
        l = check_title(c)
        if l > 100:
            print(f"Year {y}: '{c}' -> {l} bytes", flush=True)
            found = True
            break
    if not found:
        print(f"Year {y}: NOT FOUND in {candidates}", flush=True)
