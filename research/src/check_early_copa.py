import urllib.request
import re
import json

headers = {'User-Agent': 'Mozilla/5.0'}

def check_comp_matches(comp, ed):
    url = f"https://acb.com/es/{comp}/calendario?temporada={ed}"
    try:
        req = urllib.request.Request(url, headers=headers)
        html = urllib.request.urlopen(req, timeout=8).read().decode('utf-8', errors='ignore')
        chunks = re.findall(r'self\.__next_f\.push\(\[1,"(.*?)"\]\)', html, re.DOTALL)
        full_text = ''.join(c.encode().decode('unicode_escape', errors='ignore') for c in chunks)
        
        r_pos = full_text.find('"rounds":[{"id":')
        if r_pos == -1: return 0
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
        played = sum(1 for r in rounds for m in r.get('matches', []) if m.get('homeTeamScore') is not None and m.get('awayTeamScore') is not None)
        return played
    except Exception as e:
        return 0

for ed in [40, 45, 48, 50, 52, 55, 58, 60, 62, 64]:
    c = check_comp_matches('copa-del-rey', ed)
    s = check_comp_matches('supercopa', ed)
    print(f"Ed {ed} (Year {1935+ed}): Copa matches={c}, Supercopa matches={s}", flush=True)
