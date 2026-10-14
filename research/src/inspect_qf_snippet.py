import urllib.request
import urllib.parse
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

headers = {'User-Agent': 'SportsResearchCollector/2.0'}

def get_page(title):
    url = f"https://en.wikipedia.org/w/api.php?action=parse&page={urllib.parse.quote(title)}&format=json&prop=wikitext"
    try:
        req = urllib.request.Request(url, headers=headers)
        data = json.loads(urllib.request.urlopen(req, timeout=12).read().decode('utf-8'))
        return data.get('parse', {}).get('wikitext', {}).get('*', '')
    except Exception as e:
        return ""

wt = get_page("1975–76 FIBA European Cup Winners' Cup")

qf_pos = wt.find("==Quarterfinals==")
print("Quarterfinals snippet:")
print(wt[qf_pos:qf_pos+2500])
