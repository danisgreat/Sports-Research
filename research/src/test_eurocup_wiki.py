import urllib.request
import urllib.parse
import json

headers = {'User-Agent': 'SportsResearchBot/1.0 (contact@sportsresearch.org)'}

def get_wiki_page(title):
    url = f"https://en.wikipedia.org/w/api.php?action=parse&page={urllib.parse.quote(title)}&format=json&prop=wikitext"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            return data.get('parse', {}).get('wikitext', {}).get('*', '')
    except Exception as e:
        return f"Error: {e}"

for title in [
    '1975–76 FIBA European Cup Winner\'s Cup',
    '1980–81 FIBA European Cup Winner\'s Cup',
    '1985–86 FIBA European Cup Winner\'s Cup',
    '1991–92 FIBA European Cup',
    '1996–97 FIBA EuroCup',
    '1998–99 FIBA Saporta Cup',
    '2001–02 FIBA Saporta Cup',
    '2002–03 ULEB Cup',
    '2008–09 Eurocup Basketball',
    '2015–16 Eurocup Basketball',
    '2023–24 EuroCup Basketball'
]:
    wt = get_wiki_page(title)
    print(f"Title: '{title}' -> len: {len(wt)}")
