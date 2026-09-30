"""Collect football archive evidence. No forecasts or market fields are retained.
Run: python -u collect.py [afl|nfl|api|wafl]. Cached successful requests are reused.
Requires requests and beautifulsoup4. Source bodies are gzip compressed; credentials
are never saved. Each receipt identifies the requested URL and exact body hash.
"""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from collections import defaultdict
from urllib.parse import urljoin
import requests, gzip, hashlib, json, csv, io, re, sys, time
from datetime import datetime, timezone
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parent
CACHE = ROOT / 'sources'
CACHE.mkdir(exist_ok=True)
YEARS = range(1900, 2026)

def get(url, headers=None, persist=True):
    key = hashlib.sha256(url.encode()).hexdigest()
    path = CACHE / (key + '.gz')
    if path.exists():
        return gzip.decompress(path.read_bytes()).decode('utf-8')
    last = None
    for attempt in range(3):
        try:
            r = requests.get(url, headers=headers, timeout=45)
            r.raise_for_status()
            body = r.content
            value = r.text
            # Preserve a normalized UTF-8 source and separately hash transport bytes.
            stored = re.sub(r'<script>window\.__NUXT__=\{\};window\.__NUXT__\.config=.*?</script>', '', value, flags=re.S) if 'wafl.com.au/' in url else value
            normalized = stored.encode('utf-8')
            if persist:
                path.write_bytes(gzip.compress(normalized))
            receipt = {'url':url, 'retrieved_utc':datetime.now(timezone.utc).isoformat(),
                       'http_status':r.status_code,'transport_sha256':hashlib.sha256(body).hexdigest(),
                       'stored_sha256':hashlib.sha256(normalized).hexdigest() if persist else '',
                       'stored_body':path.name if persist else 'not retained (market fields excluded)'}
            (CACHE / (key + '.json')).write_text(json.dumps(receipt,indent=2),encoding='utf-8')
            return value
        except Exception as exc:
            last = exc
            time.sleep(0.5 * (attempt + 1))
    raise RuntimeError(f'{url}: {last}')

def soup(url):
    return BeautifulSoup(get(url), 'html.parser')

def save(name, value):
    (ROOT / (name + '.json')).write_text(json.dumps(value,ensure_ascii=False,indent=2),encoding='utf-8')

def batch(tasks, fn, workers=4):
    results, errors = [], []
    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = {pool.submit(fn, task):task for task in tasks}
        for n, fut in enumerate(as_completed(futures),1):
            try:
                results.append(fut.result())
            except Exception as exc:
                errors.append({'task':str(futures[fut]),'error':str(exc)})
                print('ERROR',str(exc),flush=True)
            if n % 25 == 0:
                print(f'{n}/{len(tasks)} collected',flush=True)
    return results, errors

def collect_afl_year(year):
    url = f'https://afltables.com/afl/stats/{year}.html'
    s = soup(url)
    rows, counts = [], []
    for table in s.select('table.sortable'):
        heading = table.find('thead')
        team_a = heading.find('a',href=re.compile(r'\.\./teams/')) if heading else None
        if not team_a:
            continue
        team = team_a.get_text(' ',strip=True)
        added = 0
        for tr in table.select('tbody tr'):
            cells = tr.find_all('td',recursive=False)
            if len(cells)<3:
                continue
            a = cells[1].find('a',href=re.compile(r'players/'))
            if a and cells[2].get_text(strip=True).isdigit():
                games = int(cells[2].get_text(strip=True))
                if games>0:
                    rows.append({'year':year,'edition':str(year),'player':a.get_text(' ',strip=True),
                                 'player_id':urljoin(url,a['href']),'team':team,'games':games,'source':url})
                    added+=1
        text = table.get_text(' ',strip=True)
        m=re.search(r'(\d+) players used',text)
        if m:
            assert added==int(m[1]),(year,team,added,m[1])
        counts.append({'team':team,'parsed':added,'source_players_used':int(m[1]) if m else None})
    assert len(rows)>100, (year,len(rows))
    seasonurl=f'https://afltables.com/afl/seas/{year}.html'
    ss=soup(seasonurl)
    venues={urljoin(seasonurl,a['href']):a.get_text(' ',strip=True) for a in ss.find_all('a',href=re.compile(r'\.\./venues/'))}
    # Identify actual Grand Final sections, including replays, rather than using the last game.
    gfs=[]
    for label in ss.find_all(string=re.compile(r'^Grand Final(?: Replay)?$')):
        table=label.parent.find_next('table')
        if table:
            for link in table.find_all('a',href=re.compile(r'\.\./stats/games/')):
                gfs.append(urljoin(seasonurl,link['href']))
    return {'year':year,'players':rows,'team_counts':counts,'venues':venues,'grand_final_urls':list(dict.fromkeys(gfs))}

def collect_profile(task):
    kind, name, url=task
    s=soup(url)
    table=s.find('table')
    rows=[]
    year=None
    if table:
        for tr in table.find_all('tr'):
            cells=[c.get_text(' ',strip=True) for c in tr.find_all('td',recursive=False)]
            if not cells: continue
            if re.fullmatch(r'\d{4}',cells[0]):
                year=int(cells[0]); cells=cells[1:]
            else:
                # A rowspan can repeat a year for a second team; inspect source markup.
                if not (kind=='coach' and year and tr.find('a',href=re.compile(r'teams/'))): continue
            if year not in YEARS: continue
            if kind=='coach' and len(cells)>=2:
                rows.append({'year':year,'name':name,'team':cells[0],'role':'Head coach','source':url})
            elif kind=='umpire' and cells and cells[0].isdigit() and int(cells[0])>0:
                rows.append({'year':year,'name':name,'role':'Field umpire','games':int(cells[0]),
                             'grand_finals':int(cells[2]) if len(cells)>2 and cells[2].isdigit() else 0,'source':url})
    return {'kind':kind,'name':name,'url':url,'rows':rows}

def collect_gf(url):
    s=soup(url); rows=[]
    for table in s.select('table.sortable'):
        head=table.find('thead')
        if not head: continue
        team_a=head.find('a',href=re.compile(r'teams/'))
        if not team_a: continue
        team=team_a.get_text(' ',strip=True)
        for tr in table.select('tbody tr'):
            a=tr.find('a',href=re.compile(r'players/'))
            if a:
                rows.append({'player':a.get_text(' ',strip=True),'player_id':urljoin(url,a['href']),
                             'team':team,'games':1,'source':url})
    # For pre-statistical seasons player names can sit in tables without class sortable.
    if not rows:
        for table in s.find_all('table'):
            anchors=table.find_all('a',href=re.compile(r'players/'))
            if not anchors: continue
            team_a=table.find('a',href=re.compile(r'teams/'))
            if not team_a: continue
            team=team_a.get_text(' ',strip=True)
            rows.extend({'player':a.get_text(' ',strip=True),'player_id':urljoin(url,a['href']),
                         'team':team,'games':1,'source':url} for a in anchors)
    return {'url':url,'players':rows,'text':s.get_text(' ',strip=True)[:1800]}

def afl():
    results,errors=batch(list(YEARS),collect_afl_year)
    save('afl_years',sorted(results,key=lambda r:r['year'])); save('afl_errors',errors)
    tasks=[]
    for kind,path in [('coach','coaches/coaches_idx.html'),('umpire','umpires/umpires_idx.html')]:
        url='https://afltables.com/afl/stats/'+path
        ss=soup(url)
        table=ss.find('table')
        for tr in table.select('tbody tr'):
            a=tr.find('a')
            if not a: continue
            # Read only profiles whose recorded career intersects 1900-2025.
            cells=[td.get_text(' ',strip=True) for td in tr.find_all('td')]
            era=cells[2] if kind=='coach' else cells[1]
            yrs=[int(y) for y in re.findall(r'\d{4}',era)]
            if yrs and min(yrs)>2025: continue
            tasks.append((kind,a.get_text(' ',strip=True),urljoin(url,a['href'])))
    profiles,pe=batch(tasks,collect_profile)
    save('afl_profiles',profiles); save('afl_profile_errors',pe)
    gfurls=sorted(set(u for r in results for u in r['grand_final_urls']))
    gfs,ge=batch(gfurls,collect_gf)
    save('afl_grand_finals',gfs);save('afl_gf_errors',ge)

def nfl():
    base='https://github.com/nflverse/nflverse-data/releases/download/'
    def snaps(y):
        url=base+f'snap_counts/snap_counts_{y}.csv'
        rows=list(csv.DictReader(io.StringIO(get(url))))
        assert rows and 'pfr_player_id' in rows[0]
        assert all(int(r['season'])==y for r in rows)
        return {'year':y,'url':url,'rows':rows}
    data,errors=batch(list(range(2012,2026)),snaps)
    save('nfl_snaps',data);save('nfl_snap_errors',errors)
    url=base+'officials/officials.csv'
    officials=[r for r in csv.DictReader(io.StringIO(get(url))) if r['season'].isdigit() and int(r['season'])<=2025]
    save('nfl_officials',{'url':url,'rows':officials})
    url='https://raw.githubusercontent.com/nflverse/nfldata/master/data/games.csv'
    fields=['game_id','season','game_type','week','gameday','away_team','home_team','away_coach','home_coach','referee','stadium','stadium_id','roof','surface','old_game_id','gsis','pfr']
    rows=[{k:r.get(k,'') for k in fields} for r in csv.DictReader(io.StringIO(get(url,persist=False))) if r['season'].isdigit() and int(r['season'])<=2025]
    save('nfl_games',{'url':url,'rows':rows})
    def stats(y):
        url=base+f'stats_player/stats_player_week_{y}.csv'
        fields=['player_id','player_name','player_display_name','season','season_type','week','team','recent_team']
        rows=[{k:r.get(k,'') for k in fields} for r in csv.DictReader(io.StringIO(get(url))) if r.get('season')==str(y)]
        return {'year':y,'url':url,'rows':rows}
    data,errors=batch(list(range(1999,2012)),stats)
    save('nfl_early_stats',data);save('nfl_early_errors',errors)

def rosters():
    def fetch(y):
        url=f'https://github.com/nflverse/nflverse-data/releases/download/rosters/roster_{y}.csv'
        rows=list(csv.DictReader(io.StringIO(get(url))))
        assert rows and all(int(r['season'])==y for r in rows),(y,'empty or mixed-season roster')
        return {'year':y,'url':url,'rows':rows}
    data,errors=batch(list(range(1920,2026)),fetch)
    save('nfl_rosters',data);save('nfl_roster_errors',errors)

def api():
    token=requests.post('https://api.afl.com.au/cfs/afl/WMCTok',data='',timeout=30).json()['token']
    headers={'x-media-mis-token':token}
    public='https://aflapi.afl.com.au/afl/v2/'
    comps=json.loads(get(public+'competitions?pageSize=100'))['competitions']
    selected=[c for c in comps if c.get('code') in ['AFLW','VFL','VFLW','SANFL','WAFL'] and 'Preseason' not in c['name'] and 'Ireland' not in c['name']]
    tasks=[]
    for c in selected:
        seasons=json.loads(get(public+f"competitions/{c['id']}/compseasons?pageSize=100"))['compSeasons']
        for se in seasons:
            years=re.findall(r'(?:19|20)\d{2}',se['name'])
            if not years: continue
            year=int(years[0])
            if year not in YEARS: continue
            tasks.append((c['code'],year,se))
    def fetch(task):
        code,year,se=task
        url=f"https://api.afl.com.au/statspro/playersStats/seasons/{se['providerId']}?includeBenchmarks=false"
        stats=json.loads(get(url,headers=headers))
        assert len(stats.get('players',[]))==stats.get('totalResults',-1),(code,year,'pagination or missing results')
        players=[]
        for p in stats['players']:
            if p.get('gamesPlayed',0)>0:
                players.append({'year':year,'edition':se['name'],'player':p['playerDetails']['givenName']+' '+p['playerDetails']['surname'],
                                'player_id':p['playerId'],'team':p['team']['teamName'],'games':p['gamesPlayed'],'source':url})
        fixtureurl=public+f"matches?compSeasonId={se['id']}&pageSize=1000"
        fixtures=json.loads(get(fixtureurl))
        assert len(fixtures.get('matches',[]))==fixtures['meta']['pagination']['numEntries'],('pagination',code,year)
        return {'league':code,'year':year,'edition':se,'url':url,'players':players,'fixture_url':fixtureurl,'matches':fixtures['matches']}
    data,errors=batch(tasks,fetch)
    save('afl_api',data);save('afl_api_errors',errors)

def wafl():
    url='https://wafl.com.au/stats/players'
    # Public client credentials are obtained transiently from the official site.
    # No token is printed, saved, or embedded in a receipt.
    html=requests.get(url,timeout=30).text
    s=BeautifulSoup(html,'html.parser')
    base=re.search(r'apiUrl:"([^"]+)"',html)[1]
    key=re.search(r'apiKey:"([^"]+)"',html)[1]
    tenant=re.search(r'tenantId:"([^"]+)"',html)[1]
    headers={'Accept':'application/json','Authorization':'Bearer '+key,'tenant-id':tenant}
    years={int(o.get_text()):o['value'] for o in s.find('select',attrs={'name':'season'}).find_all('option') if o.get_text().isdigit() and int(o.get_text()) in YEARS}
    save('wafl_season_ids',years)
    comps={o.get_text():o['value'] for o in s.find('select',attrs={'name':'rounds'}).find_all('option')}
    tasks=[(league,y,seasonid,comps['League' if league=='WAFL' else 'WAFLW']) for y,seasonid in years.items() for league in ['WAFL','WAFLW'] if league=='WAFL' or y>=2019]
    def fetch(task):
        league,year,se,co=task
        qs=requests.models.RequestEncodingMixin._encode_params({'competition':co,'club':'','season':se,'orderColumn':'last','orderDirection':'asc'})
        src=base+'/statistics?'+qs
        j=json.loads(get(src,headers=headers))
        assert isinstance(j,list),(league,year,'unexpected schema or pagination')
        players=[]
        for p in j:
            if float(p.get('games') or 0)>0:
                players.append({'year':year,'edition':str(year),'player':((p.get('first') or '')+' '+(p.get('last') or '')).strip(),
                                'player_id':str(p.get('player_id') or p.get('id') or ''),'team':p['club']['name'],
                                'games':float(p['games']),'source':src})
        return {'league':league,'year':year,'players':players,'url':src,'source_rows':len(j)}
    data,errors=batch(tasks,fetch)
    save('wafl_years',data);save('wafl_errors',errors)

def early():
    base='https://github.com/nflverse/nflverse-data/releases/download/'
    def fetch(y):
        url=base+f'stats_player/stats_player_week_{y}.csv'
        fields=['player_id','player_name','player_display_name','season','season_type','week','team','recent_team']
        rows=[{k:r.get(k,'') for k in fields} for r in csv.DictReader(io.StringIO(get(url))) if r.get('season')==str(y)]
        return {'year':y,'url':url,'rows':rows}
    data,errors=batch(list(range(1999,2013)),fetch)
    save('nfl_early_stats',data);save('nfl_early_errors',errors)

def gf():
    def links(y):
        url=f'https://afltables.com/afl/seas/{y}.html'
        s=soup(url);found=[]
        for label in s.find_all(string=re.compile(r'^Grand Final(?: Replay)?$')):
            table=label.parent.find_next('table')
            if table:
                found.extend(urljoin(url,a['href']) for a in table.find_all('a',href=re.compile(r'\.\./stats/games/')))
        return {'year':y,'urls':list(dict.fromkeys(found))}
    data,errors=batch(list(YEARS),links)
    save('afl_gf_links',data);save('afl_gf_link_errors',errors)
    data,errors=batch(sorted(set(u for r in data for u in r['urls'])),collect_gf)
    save('afl_grand_finals',data);save('afl_gf_errors',errors)

if __name__=='__main__':
    globals()[sys.argv[1] if len(sys.argv)>1 else 'afl']()
