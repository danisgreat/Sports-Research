import urllib.request
import re
import json
from acb_teams import resolve_acb_team

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

def parse_edition_calendar(edition_id):
    url = f"https://acb.com/es/liga/calendario?temporada={edition_id}"
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
    except Exception as e:
        print(f"Error fetching edition {edition_id}: {e}")
        return []
    
    chunks = re.findall(r'self\.__next_f\.push\(\[1,"(.*?)"\]\)', html, re.DOTALL)
    full_text = ''.join(c.encode().decode('unicode_escape', errors='ignore') for c in chunks)
    
    # Locate rounds and teams block
    # Find last occurrences of "teams":[{ and "rounds":[{
    teams_matches = list(re.finditer(r'"teams":\s*(\[\{"id":\d+.*?"displayTextColor":"#[0-9a-fA-F]+"[^\}]*\}\])', full_text))
    if not teams_matches:
        # Fallback search
        t_pos = full_text.rfind('"teams":[{"id":')
        end_t = full_text.find('],"rounds"', t_pos)
        teams_raw = full_text[t_pos+8:end_t+1]
    else:
        teams_raw = teams_matches[-1].group(1)
        
    teams_json = teams_raw.replace('"$undefined"', 'null')
    try:
        teams = json.loads(teams_json)
    except Exception as e:
        print(f"Error decoding teams for edition {edition_id}: {e}")
        return []
    
    # Locate rounds
    r_pos = full_text.find('"rounds":[{"id":')
    if r_pos == -1:
        print(f"No rounds array found for edition {edition_id}")
        return []
    
    # Find matching closing bracket for rounds array
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
                
    if end_bracket == -1:
        print(f"Could not balance brackets for rounds in edition {edition_id}")
        return []
        
    rounds_raw = full_text[start_bracket:end_bracket+1]
    # Replace team references "$30:props:data:teams:16" -> 16
    rounds_clean = re.sub(r'"\$[^\"]+:teams:(\d+)"', r'\1', rounds_raw).replace('"$undefined"', 'null')
    try:
        rounds = json.loads(rounds_clean)
    except Exception as e:
        print(f"Error decoding rounds for edition {edition_id}: {e}")
        return []
        
    games = []
    for r in rounds:
        r_num = r.get('roundNumber', 0)
        subphase = r.get('subphase', '')
        for m in r.get('matches', []):
            m_id = m.get('id')
            h_idx = m.get('homeTeam')
            a_idx = m.get('awayTeam')
            h_score = m.get('homeTeamScore')
            a_score = m.get('awayTeamScore')
            start_dt = m.get('startDateTime', '')
            status = m.get('matchStatus', '')
            season_year = m.get('seasonStartYear')
            
            # Skip unplayed / null score matches unless future fixture
            if h_score is None or a_score is None:
                continue
                
            h_name = teams[h_idx]['fullName'] if isinstance(h_idx, int) and h_idx < len(teams) else "Home Team"
            a_name = teams[a_idx]['fullName'] if isinstance(a_idx, int) and a_idx < len(teams) else "Away Team"
            
            h_canon, venue, city, region = resolve_acb_team(h_name)
            a_canon, _, _, _ = resolve_acb_team(a_name)
            
            # Determine game type & stage
            if r_num <= 34:
                game_type = "Regular Season"
                stage_round = f"Regular Season Round {r_num}"
            else:
                game_type = "Playoffs"
                stage_round = f"Playoffs Round {r_num}"
                
            date_str = start_dt[:10] if start_dt else f"{season_year}-01-01"
            start_time = start_dt[11:16] if len(start_dt) > 16 else ""
            
            # OT indication
            q_final = m.get('currentQuarter', 4)
            ot_str = "No" if q_final <= 4 else f"{q_final - 4} OT"
            
            games.append({
                'game_id': f"ACB_{m_id}",
                'season': f"{season_year}-{str((season_year+1)%100).zfill(2)}",
                'season_year': season_year,
                'league_name': "Liga ACB",
                'era': "Modern Liga ACB Era",
                'game_type': game_type,
                'stage_round': stage_round,
                'date': date_str,
                'start_time': start_time,
                'home_team': h_canon,
                'away_team': a_canon,
                'home_score': int(h_score),
                'away_score': int(a_score),
                'overtime': ot_str,
                'venue': venue,
                'city': city,
                'attendance': "",
                'referees': "",
                'notes': f"ACB Official Match ID {m_id}. Status: {status}.",
                'source': f"Official ACB Schedule API (acb.com, edition {edition_id})"
            })
            
    return games

if __name__ == '__main__':
    for ed in [88, 89, 90, 91]:
        res = parse_edition_calendar(ed)
        print(f"Edition {ed}: extracted {len(res)} completed matches!")
        if res:
            sample = res[0]
            print(f"  Sample: {sample['date']} | {sample['home_team']} {sample['home_score']} - {sample['away_score']} {sample['away_team']} ({sample['game_type']})")
