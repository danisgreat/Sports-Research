import urllib.request
import urllib.parse
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

headers = {'User-Agent': 'SportsResearchCollector/2.0 (contact: info@sportsresearch.org)'}

def clean_wiki_text(text):
    text = re.sub(r'\[\[(?:[^|\]]+\|)?([^\]]+)\]\]', r'\1', text)
    text = re.sub(r'\{\{[^}]+\}\}', '', text)
    text = re.sub(r'<[^>]+>', '', text)
    text = re.sub(r'[\'\"*]', '', text)
    return text.strip()

def parse_score(score_str):
    # Matches patterns like 88-83, 88–83, '''99'''-83
    score_str = re.sub(r'[\'\"*]', '', score_str).strip()
    m = re.search(r'(\d{1,3})\s*[-–]\s*(\d{1,3})', score_str)
    if m:
        return int(m.group(1)), int(m.group(2))
    return None, None

def test_parse_season(title, year):
    url = f"https://en.wikipedia.org/w/api.php?action=parse&page={urllib.parse.quote(title)}&format=json&prop=wikitext"
    try:
        req = urllib.request.Request(url, headers=headers)
        data = json.loads(urllib.request.urlopen(req, timeout=12).read().decode('utf-8'))
        wt = data.get('parse', {}).get('wikitext', {}).get('*', '')
    except Exception as e:
        print(f"Error fetching {title}: {e}")
        return []

    games = []
    
    # 1. Parse TwoLegResult templates
    # {{TwoLegResult|Team 1|C1|agg|Team 2|C2|leg1|leg2|...}}
    for m in re.finditer(r'\{\{TwoLegResult\s*\|([^}]+)\}\}', wt):
        parts = [p.strip() for p in m.group(1).split('|') if not p.strip().startswith(('var', 'winner', 'ganador'))]
        if len(parts) >= 6:
            t1 = clean_wiki_text(parts[0])
            t2 = clean_wiki_text(parts[2] if len(parts) == 6 else parts[3])
            # Leg 1 and Leg 2 are typically the last two score parts
            scores_found = []
            for p in parts:
                s1, s2 = parse_score(p)
                if s1 is not None and s2 is not None:
                    scores_found.append((s1, s2, p))
            if len(scores_found) >= 3:
                # First is aggregate, next two are leg 1 and leg 2
                leg1_h, leg1_a = scores_found[1][0], scores_found[1][1]
                leg2_s1, leg2_s2 = scores_found[2][0], scores_found[2][1]
                # Leg 1: t1 home, t2 away
                games.append(('Preliminary / Knockout', t1, t2, leg1_h, leg1_a))
                # Leg 2: t2 home, t1 away (scores_found[2] is typically written t1_score - t2_score or t2_score - t1_score)
                # In European basketball, leg 2 is t2 home vs t1 away
                games.append(('Preliminary / Knockout', t2, t1, leg2_s2, leg2_s1))

    # 2. Parse Group stage results lines
    # |{{flagicon|...}} [[Team 1]] - {{flagicon|...}} [[Team 2]]
    # |'''99'''-83
    # |90-'''107'''
    group_lines = wt.splitlines()
    for idx, l in enumerate(group_lines):
        if ' - ' in l and ('[[' in l or '{{flagicon' in l) and not l.startswith('=='):
            teams_part = l.lstrip('|').strip()
            # Split team 1 and team 2
            t_match = re.search(r'^(.*?)\s*[-–]\s*(.*?)$', teams_part)
            if t_match and idx + 2 < len(group_lines):
                t1 = clean_wiki_text(t_match.group(1))
                t2 = clean_wiki_text(t_match.group(2))
                l1_line = group_lines[idx+1].lstrip('|').strip()
                l2_line = group_lines[idx+2].lstrip('|').strip()
                s1_h, s1_a = parse_score(l1_line)
                s2_1, s2_2 = parse_score(l2_line)
                if s1_h is not None and s2_1 is not None:
                    games.append(('Quarterfinal Group Stage', t1, t2, s1_h, s1_a))
                    games.append(('Quarterfinal Group Stage', t2, t1, s2_2, s2_1))

    # 3. Parse OneLegResult / Final
    final_match = re.search(r'\{\{OneLegResult\s*\|([^}]+)\}\}', wt)
    if final_match:
        parts = [p.strip() for p in final_match.group(1).split('|') if not p.strip().startswith(('winner', 'ganador'))]
        if len(parts) >= 3:
            t1 = clean_wiki_text(parts[0])
            t2 = clean_wiki_text(parts[2] if len(parts) == 4 else parts[3])
            score_part = parts[1] if len(parts) == 3 else (parts[2] if len(parts) >= 4 else parts[-1])
            s1, s2 = parse_score(score_part)
            if s1 is not None:
                games.append(('Final', t1, t2, s1, s2))

    print(f"{year} ({title}): parsed {len(games)} matches")
    if games:
        print(f"  Sample: {games[0]}")
        print(f"  Final: {games[-1]}")
    return games

for y in [1975, 1980, 1985]:
    y2 = str((y + 1) % 100).zfill(2)
    test_parse_season(f"{y}–{y2} FIBA European Cup Winners' Cup", y)
