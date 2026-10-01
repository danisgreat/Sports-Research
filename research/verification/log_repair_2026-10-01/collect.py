import json, sys, hashlib, re, html
from pathlib import Path
from datetime import datetime, timezone
from urllib.request import Request, urlopen
from concurrent.futures import ThreadPoolExecutor
ROOT=Path(__file__).resolve().parents[3]
A=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT))
from research.src.sources import fetch_source, verified_body

if not (A/'initial.json').exists():
    paths=['METHOD.md','CURRENT_RULES.md','CARD_AND_LOG_TEMPLATES.md','RECORD_ELIGIBILITY_SCHEMA.md','SCORING_AND_VALIDATION.md','research/README.md','GAME_LOG_STATUS_CURRENT.md','CHANGELOG.md','PROMPTS.md','SOURCES.md','prediction logs/PREDICTION_LOG_COMBINED_6.md','Mini logs (to be sent to actual log later)/Mini Prediction Log - P-523 onward - 2026-10-01/PREDICTION_MINI_RUNNING_LOG_P523_ONWARD.md']
    inventory=[]
    for rel in paths:
        path=ROOT/rel
        if not path.exists():continue
        raw=path.read_bytes();target=A/'originals'/rel;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(raw)
        inventory.append({'path':rel,'sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw)})
    (A/'initial.json').write_text(json.dumps({'observed_utc':datetime.now(timezone.utc).isoformat(),'files':inventory},indent=2)+'\n',encoding='utf-8')

registry={'sources':{}}
for key,host in [('kbo','www.koreabaseball.com'),('kbo_en','eng.koreabaseball.com'),('samsung','www.samsunglions.com'),('weather','api.open-meteo.com')]:
    registry['sources'][key]={'publisher':host,'upstream_lineage_id':key,'independence_status':'UNKNOWN','access_mode':'AUTOMATED_ALLOWED','allowed_url_prefixes':['https://'+host+'/'],'market_fields_possible':False,'parser_id':'RAW_HTML_OR_JSON_MANUAL_READBACK_V1'}
reg=A/'sources_registry.json';reg.write_text(json.dumps(registry,indent=2)+'\n',encoding='utf-8')
urls={
 'gamecentre':('kbo','https://www.koreabaseball.com/Schedule/GameCenter/Main.aspx'),
 'rank':('kbo','https://www.koreabaseball.com/Record/TeamRank/TeamRank.aspx'),
 'hwang':('kbo','https://www.koreabaseball.com/Record/Player/PitcherDetail/Basic.aspx?playerId=54729'),
 'won':('kbo','https://www.koreabaseball.com/Record/Player/PitcherDetail/Basic.aspx?playerId=69446'),
 'team_bat':('kbo','https://www.koreabaseball.com/Record/Team/Hitter/Basic1.aspx'),
 'team_pitch':('kbo','https://www.koreabaseball.com/Record/Team/Pitcher/Basic1.aspx'),
 'prior_game':('kbo','https://www.koreabaseball.com/MediaNews/News/BreakingNews/View.aspx?bdSe=62459'),
 'samsung_schedule':('samsung','https://www.samsunglions.com/index.asp'),
 'regulations':('kbo','https://www.koreabaseball.com/Kbo/Rule/RuleChange.aspx'),
 'weather':('weather','https://api.open-meteo.com/v1/forecast?latitude=35.841&longitude=128.681&hourly=temperature_2m,relative_humidity_2m,precipitation,wind_speed_10m,wind_direction_10m,wind_gusts_10m&timezone=Asia%2FSeoul&forecast_days=1')}
def fetch(item):
    label,(key,url)=item
    try:
        receipt=fetch_source(key,url,registry_path=reg,timeout=15,attempts=1)
        raw=verified_body(receipt,ROOT)
        (A/(label+'.html')).write_bytes(raw)
        text=html.unescape(re.sub('<[^>]+>',' ',raw.decode('utf-8',errors='replace')))
        text=re.sub(r'[ \t]+',' ',text)
        (A/(label+'.txt')).write_text(text,encoding='utf-8')
        return label,{'status':'FETCHED','receipt':receipt}
    except Exception as e:return label,{'status':'FAILED','url':url,'reason':str(e)}
with ThreadPoolExecutor(max_workers=6) as pool:results=dict(pool.map(fetch,urls.items()))
(A/'sources.json').write_text(json.dumps(results,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:{'status':v['status'],'bytes':v.get('receipt',{}).get('response_bytes'),'reason':v.get('reason')} for k,v in results.items()},indent=2))
main=(A/'gamecentre.html').read_text(encoding='utf-8')
print('OFFICIAL_JS',re.findall(r'<script[^>]+src="([^"]+)"',main)[-20:])
