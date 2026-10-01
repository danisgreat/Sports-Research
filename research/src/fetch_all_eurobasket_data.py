#!/usr/bin/env python3
"""
Comprehensive Extractor for EuroBasket 1975-2025
Fetches matches from tournament articles, match subpages, and bracket templates.
Saves extracted structured data into research/data/eurobasket_cache.json.
"""

import os
import sys
import json
import re
import time
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')

USER_AGENT = 'SportsResearchAssistant/1.0 (academic research; eurobasket@sportsresearch.org)'

def fetch_html(page_title):
    url = f"https://en.wikipedia.org/w/api.php?action=parse&page={urllib.parse.quote(page_title)}&format=json&prop=text"
    req = urllib.request.Request(url, headers={'User-Agent': USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            if 'error' in data:
                return None
            return data.get('parse', {}).get('text', {}).get('*', '')
    except Exception as e:
        print(f"  Error fetching {page_title}: {e}")
        return None

def clean_text(t):
    if not t: return ""
    t = re.sub(r'\[.*?\]', '', t)
    t = re.sub(r'\s+', ' ', t).strip()
    return t

def parse_box_div(d, default_phase=""):
    full_text = d.get_text(separator='\n', strip=True)
    lines = [l.strip() for l in full_text.split('\n') if l.strip()]
    tables = d.find_all('table')
    
    # 1. Uncollapsed modern table (2015-2022)
    for t in tables:
        rows = t.find_all('tr')
        if len(rows) >= 2:
            r0_cells = [clean_text(c.get_text()) for c in rows[0].find_all(['td', 'th'])]
            if len(r0_cells) >= 4:
                m_score = re.search(r'(\d{2,3})\s*[\u2013\u2014\-–]\s*(\d{2,3})', r0_cells[2])
                if m_score:
                    score1 = int(m_score.group(1))
                    score2 = int(m_score.group(2))
                    date_val = r0_cells[0]
                    team1 = r0_cells[1]
                    team2 = r0_cells[3]
                    venue_val = r0_cells[4] if len(r0_cells) > 4 else ""
                    
                    time_val = ""
                    partials_val = ""
                    att_val = ""
                    ref_val = ""
                    players_val = ""
                    
                    if len(rows) > 1:
                        r1_cells = [clean_text(c.get_text()) for c in rows[1].find_all(['td', 'th'])]
                        if len(r1_cells) >= 1 and re.match(r'^\d{1,2}:\d{2}', r1_cells[0]):
                            time_val = r1_cells[0]
                        for c in r1_cells:
                            if 'Scoring' in c or 'quarter' in c.lower() or 'half' in c.lower():
                                partials_val = c
                                
                    if len(rows) > 2:
                        r2_text = rows[2].get_text(separator=' ', strip=True)
                        m_att = re.search(r'Attendance:\s*([0-9,]+)', r2_text)
                        if m_att: att_val = m_att.group(1)
                        m_ref = re.search(r'Referees?:\s*([^\.]+)', r2_text)
                        if m_ref: ref_val = m_ref.group(1).strip()
                        pts_matches = re.findall(r'(?:Pts|Rebs|Asts):\s*([a-zA-Z\s\.\,\-]+?\d+)', r2_text)
                        if pts_matches:
                            players_val = '; '.join(pts_matches[:4])
                            
                    return {
                        "date_raw": date_val,
                        "time_raw": time_val,
                        "team1": team1,
                        "team2": team2,
                        "score1": score1,
                        "score2": score2,
                        "venue": venue_val,
                        "partials": partials_val,
                        "attendance": att_val,
                        "referees": ref_val,
                        "players": players_val,
                        "phase": default_phase
                    }
                    
    # 2. Traditional 3-table basketballbox (1983-2013)
    if len(tables) >= 3:
        dt_text = tables[0].get_text(separator=' ', strip=True)
        score_table = tables[2]
        tds = score_table.find_all('td')
        if len(tds) >= 3:
            t1 = clean_text(tds[0].get_text())
            score_text = tds[1].get_text(strip=True)
            t2 = clean_text(tds[2].get_text())
            m_s = re.search(r'(\d{2,3})\s*[\u2013\u2014\-–]\s*(\d{2,3})', score_text)
            if m_s:
                s1 = int(m_s.group(1))
                s2 = int(m_s.group(2))
                
                parts = ""
                att = ""
                ref = ""
                ven = ""
                players = []
                
                for l in lines:
                    if 'Scoring' in l or 'half' in l.lower() or 'quarter' in l.lower():
                        parts = l
                    elif 'Attendance:' in l:
                        att = l.split('Attendance:')[-1].strip()
                    elif 'Referees:' in l or 'Referee:' in l:
                        ref = re.sub(r'^Referees?:\s*', '', l).strip()
                    elif any(v in l for v in ['Arena', 'Stadium', 'Hall', 'Palacio', 'Palasport', 'Center', 'Centre', 'Pabellón', 'Dvorana']):
                        ven = l.strip()
                    elif 'Pts:' in l:
                        players.append(l.strip())
                        
                date_val = dt_text
                time_val = ""
                m_t = re.search(r'\b\d{1,2}:\d{2}\b', dt_text)
                if m_t:
                    time_val = m_t.group(0)
                    date_val = dt_text.replace(time_val, '').strip()
                    
                return {
                    "date_raw": date_val,
                    "time_raw": time_val,
                    "team1": t1,
                    "team2": t2,
                    "score1": s1,
                    "score2": s2,
                    "venue": ven,
                    "partials": parts,
                    "attendance": att,
                    "referees": ref,
                    "players": '; '.join(players[:3]),
                    "phase": default_phase
                }
    return None

def parse_early_tables(soup, default_phase=""):
    matches = []
    tables = soup.find_all('table')
    for t in tables:
        prev_h = t.find_previous(['h2', 'h3', 'h4'])
        ph = clean_text(prev_h.get_text()) if prev_h else default_phase
        
        # 1. Row by row score check
        for r in t.find_all('tr'):
            cells = [clean_text(c.get_text()) for c in r.find_all(['td', 'th'])]
            for idx, c in enumerate(cells):
                m = re.search(r'(\d{2,3})\s*[\u2013\u2014\-–\x96]\s*(\d{2,3})', c)
                if m:
                    team1, team2 = "", ""
                    if idx >= 2 and len(cells) >= 3:
                        if idx == 2 and len(cells) >= 3 and not cells[0].isdigit() and not cells[1].isdigit():
                            team1 = cells[0]
                            team2 = cells[1]
                        elif idx == 2 and len(cells) >= 4:
                            team1 = cells[1]
                            team2 = cells[3]
                    elif idx == 1 and len(cells) >= 3:
                        team1 = cells[0]
                        team2 = cells[2]
                        
                    if team1 and team2 and len(team1) > 2 and len(team2) > 2 and not team1.isdigit() and not team2.isdigit():
                        matches.append({
                            "date_raw": "",
                            "time_raw": "",
                            "team1": team1,
                            "team2": team2,
                            "score1": int(m.group(1)),
                            "score2": int(m.group(2)),
                            "venue": "",
                            "partials": "",
                            "attendance": "",
                            "referees": "",
                            "players": "",
                            "phase": ph
                        })
                        break
                        
        # 2. Tournament bracket pairs check
        bracket_rows = []
        for r in t.find_all('tr'):
            cells = [clean_text(c.get_text()) for c in r.find_all(['td', 'th']) if clean_text(c.get_text())]
            if len(cells) == 2 and re.match(r'^\d{2,3}$', cells[1]) and len(cells[0]) > 2 and not cells[0].isdigit():
                bracket_rows.append((cells[0], int(cells[1])))
                
        # Group bracket rows in pairs of 2
        for i in range(0, len(bracket_rows) - 1, 2):
            teamA, scoreA = bracket_rows[i]
            teamB, scoreB = bracket_rows[i+1]
            matches.append({
                "date_raw": "",
                "time_raw": "",
                "team1": teamA,
                "team2": teamB,
                "score1": scoreA,
                "score2": scoreB,
                "venue": "",
                "partials": "",
                "attendance": "",
                "referees": "",
                "players": "",
                "phase": ph
            })
            
    return matches

def extract_tournament_games(year):
    print(f"\nExtracting EuroBasket {year}...")
    pages_to_fetch = [f"EuroBasket_{year}"]
    
    if year in [2011, 2013]:
        for g in ['A', 'B', 'C', 'D', 'E', 'F']:
            pages_to_fetch.append(f"EuroBasket_{year}_Group_{g}")
    elif year in [2015, 2017]:
        for g in ['A', 'B', 'C', 'D']:
            pages_to_fetch.append(f"EuroBasket_{year}_Group_{g}")
        pages_to_fetch.append(f"EuroBasket_{year}_knockout_stage")
    elif year == 2022:
        for g in ['A', 'B', 'C', 'D']:
            pages_to_fetch.append(f"Template:EuroBasket_2022_Group_{g}_matches")
        pages_to_fetch.append("Template:EuroBasket_2022_knockout_stage_matches")
        
    all_games = []
    
    for page in pages_to_fetch:
        html = fetch_html(page)
        if not html:
            continue
        soup = BeautifulSoup(html, 'html.parser')
        
        # 1. Parse basketballbox divs
        for d in soup.find_all('div'):
            if d.find('table'):
                prev_h = d.find_previous(['h2', 'h3', 'h4'])
                ph = clean_text(prev_h.get_text()) if prev_h else page.replace('_', ' ')
                res = parse_box_div(d, ph)
                if res:
                    all_games.append(res)
                    
        # 2. Parse early wikitables / bracket matches
        tbl_games = parse_early_tables(soup, page.replace('_', ' '))
        all_games.extend(tbl_games)
        time.sleep(1.0)
        
    # Deduplicate games by (team1, team2, score1, score2)
    seen = set()
    deduped = []
    for g in all_games:
        key = (g['team1'].lower(), g['team2'].lower(), g['score1'], g['score2'])
        rev_key = (g['team2'].lower(), g['team1'].lower(), g['score2'], g['score1'])
        if key not in seen and rev_key not in seen:
            seen.add(key)
            deduped.append(g)
            
    print(f"  -> Extracted {len(deduped)} distinct games for {year}")
    return deduped

def main():
    tournaments = [1975, 1977, 1979, 1981, 1983, 1985, 1987, 1989, 1991, 1993, 1995, 1997, 1999, 2001, 2003, 2005, 2007, 2009, 2011, 2013, 2015, 2017, 2022]
    
    cache_dir = os.path.abspath("research/data")
    os.makedirs(cache_dir, exist_ok=True)
    cache_file = os.path.join(cache_dir, "eurobasket_cache.json")
    
    data = {}
    if os.path.exists(cache_file):
        with open(cache_file, "r", encoding="utf-8") as f:
            data = json.load(f)
            
    # Force re-extract 1975-1981 to capture all early games
    for y in [1975, 1977, 1979, 1981]:
        data[str(y)] = extract_tournament_games(y)
        
    for y in tournaments:
        if str(y) not in data or len(data[str(y)]) == 0:
            games = extract_tournament_games(y)
            data[str(y)] = games
            time.sleep(1.2)
            
    with open(cache_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        
    print("\nEuroBasket Cache Summary:")
    total_games = sum(len(games) for games in data.values())
    for y in sorted(map(int, data.keys())):
        print(f"  {y}: {len(data[str(y)])} games")
    print(f"Total Cached Games across all tournaments: {total_games}")

if __name__ == "__main__":
    main()
