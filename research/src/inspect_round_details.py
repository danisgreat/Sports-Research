import urllib.request
import re
import json

headers = {'User-Agent': 'Mozilla/5.0'}
url = 'https://acb.com/es/liga/calendario?temporada=88'
req = urllib.request.Request(url, headers=headers)
html = urllib.request.urlopen(req, timeout=10).read().decode('utf-8', errors='ignore')
chunks = re.findall(r'self\.__next_f\.push\(\[1,"(.*?)"\]\)', html, re.DOTALL)
full_text = ''.join(c.encode().decode('unicode_escape', errors='ignore') for c in chunks)

r_pos = full_text.find('"rounds":[{"id":')
start_bracket = r_pos + 9
depth = 0
end_bracket = -1
for i in range(start_bracket, len(full_text)):
    if full_text[i] == '[':
        depth += 1
    elif full_text[i] == ']':
        depth -= 1
        if depth == 0:
            end_bracket = i
            break

rounds_clean = re.sub(r'"\$[^\"]+:teams:(\d+)"', r'\1', full_text[start_bracket:end_bracket+1]).replace('"$undefined"', 'null')
rounds = json.loads(rounds_clean)

for r in rounds[-8:]:
    print('Round:', {k: v for k, v in r.items() if k != 'matches'})
    if r.get('matches'):
        m0 = r.get('matches')[0]
        print('  Sample match:', {k: m0[k] for k in ['id', 'homeTeamScore', 'awayTeamScore', 'startDateTime'] if k in m0})
