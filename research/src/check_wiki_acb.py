import urllib.request
import json
import re

def check_season(year):
    # Liga ACB seasons are typically named 'Liga ACB YYYY-YY' e.g. 1983-84, 1994-95, 2023-24
    y2 = str((year + 1) % 100).zfill(2)
    page_name = f"Liga_ACB_{year}-{y2}"
    url = f"https://es.wikipedia.org/w/api.php?action=parse&page={page_name}&format=json&prop=sections|wikitext"
    req = urllib.request.Request(url, headers={'User-Agent': 'SportsBot/1.0'})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            if 'error' in data:
                return False, data['error'].get('info', '')
            sections = [s['line'] for s in data.get('parse', {}).get('sections', [])]
            wikitext = data.get('parse', {}).get('wikitext', {}).get('*', '')
            has_results = any('resultado' in s.lower() or 'clasificaci' in s.lower() or 'playoff' in s.lower() for s in sections)
            has_scores = bool(re.search(r'\b[0-9]{2,3}\s*[-–]\s*[0-9]{2,3}\b', wikitext))
            return True, f"Len: {len(wikitext)}, Scores: {has_scores}, Sections: {len(sections)}"
    except Exception as e:
        return False, str(e)

print("Checking sample ACB seasons on Spanish Wikipedia:")
for y in [1983, 1984, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2023, 2024]:
    ok, info = check_season(y)
    print(f"Season {y}-{y+1}: {ok} | {info}")

print("\nChecking sample Liga Nacional (pre-1983) seasons:")
for y in [1975, 1976, 1980, 1982]:
    y2 = str((y + 1) % 100).zfill(2)
    page_name = f"Liga_Nacional_de_Baloncesto_{y}-{y2}"
    url = f"https://es.wikipedia.org/w/api.php?action=parse&page={page_name}&format=json&prop=sections"
    req = urllib.request.Request(url, headers={'User-Agent': 'SportsBot/1.0'})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            if 'error' in data:
                print(f"Liga Nacional {y}: Error {data['error'].get('info')}")
            else:
                secs = [s['line'] for s in data.get('parse', {}).get('sections', [])]
                print(f"Liga Nacional {y}: OK, Sections: {secs}")
    except Exception as e:
        print(f"Liga Nacional {y}: {e}")
