import urllib.request
import re
import json

headers = {'User-Agent': 'Mozilla/5.0'}

def test_comp(comp, ed):
    url = f'https://acb.com/es/{comp}/calendario?temporada={ed}'
    req = urllib.request.Request(url, headers=headers)
    html = urllib.request.urlopen(req, timeout=10).read().decode('utf-8', errors='ignore')
    chunks = re.findall(r'self\.__next_f\.push\(\[1,"(.*?)"\]\)', html, re.DOTALL)
    full_text = ''.join(c.encode().decode('unicode_escape', errors='ignore') for c in chunks)
    
    # check rounds
    r_pos = full_text.find('"rounds":[{"id":')
    if r_pos == -1:
        print(f"{comp} ed {ed}: No rounds found")
        return
        
    start_bracket = r_pos + 9
    depth = 0
    end_bracket = -1
    for i in range(start_bracket, len(full_text)):
        if full_text[i] == '[': depth += 1
        elif full_text[i] == ']':
            depth -= 1
            if depth == 0:
                end_bracket = i
                break
                
    rounds_clean = re.sub(r'"\$[^\"]+:teams:(\d+)"', r'\1', full_text[start_bracket:end_bracket+1]).replace('"$undefined"', 'null')
    rounds = json.loads(rounds_clean)
    num_matches = sum(len(r.get('matches', [])) for r in rounds)
    print(f"{comp} ed {ed}: {len(rounds)} rounds, {num_matches} matches")
    for r in rounds:
        for m in r.get('matches', []):
            print(f"   Match {m.get('id')}: {m.get('startDateTime')} | score: {m.get('homeTeamScore')} - {m.get('awayTeamScore')}")

test_comp('copa-del-rey', 88)
test_comp('supercopa', 88)
