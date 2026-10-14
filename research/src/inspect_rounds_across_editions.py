import urllib.request
import re
import json

headers = {'User-Agent': 'Mozilla/5.0'}

def inspect_edition_structure(ed):
    url = f"https://acb.com/es/liga/calendario?temporada={ed}"
    req = urllib.request.Request(url, headers=headers)
    html = urllib.request.urlopen(req, timeout=12).read().decode('utf-8', errors='ignore')
    chunks = re.findall(r'self\.__next_f\.push\(\[1,"(.*?)"\]\)', html, re.DOTALL)
    full_text = ''.join(c.encode().decode('unicode_escape', errors='ignore') for c in chunks)
    
    # check rounds
    r_pos = full_text.find('"rounds":[{"id":')
    if r_pos == -1:
        print(f"Ed {ed}: No rounds found")
        return
    start_bracket = r_pos + 9
    depth = 0
    end_bracket = -1
    for i in range(start_bracket, len(full_text)):
        if full_text[i] == '[': depth += 1
        elif full_text[i] == ']':
            depth -= 1
            if depth == 0: end_bracket = i; break
    rounds_clean = re.sub(r'"\$[^\"]+:teams:(\d+)"', r'\1', full_text[start_bracket:end_bracket+1]).replace('"$undefined"', 'null')
    rounds = json.loads(rounds_clean)
    
    subphases = set()
    round_nums = []
    for r in rounds:
        round_nums.append(r.get('roundNumber'))
        sp = r.get('subphase')
        if isinstance(sp, dict):
            subphases.add(sp.get('id'))
        elif sp:
            subphases.add(str(sp))
    print(f"Ed {ed} (Year {1935+ed}): {len(rounds)} rounds, round range: {min(round_nums)} to {max(round_nums)}, subphases: {subphases}")

for ed in [40, 48, 55, 65, 75, 84, 88]:
    inspect_edition_structure(ed)
