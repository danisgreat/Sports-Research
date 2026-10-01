from pathlib import Path
import sys,json,re
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlencode
A=Path(__file__).resolve().parent;ROOT=A.parents[2];sys.path.insert(0,str(ROOT))
from research.src.sources import fetch_source,verified_body
from inspect_tables import Tables
reg=A/'sources_registry.json'
base={'leId':'1','srId':'0','seasonId':'2026','gameId':'20261001HHSS0','awayTeam':'HH','homeTeam':'SS','awayPit':'54729','homePit':'69446'}
urls={k:'https://www.koreabaseball.com/Schedule/GameCenter/Preview/'+route+'.aspx?'+urlencode(base) for k,route in [('start','StartPitcher'),('teams','Team'),('lineup','LineUp')]}
urls.update({'rule2026':'https://www.koreabaseball.com/Kbo/League/GameManage2026.aspx','operation':'https://www.koreabaseball.com/Kbo/League/GameManageRule/GameManage.aspx','prior_review':'https://www.koreabaseball.com/Schedule/GameCenter/ReviewNew.aspx?'+urlencode({**base,'gameId':'20260930HHSS0'})})
def fetch(item):
    label,url=item
    try:
        r=fetch_source('kbo',url,registry_path=reg,timeout=15,attempts=1)
        raw=verified_body(r,ROOT);(A/(label+'.html')).write_bytes(raw)
        p=Tables();p.feed(raw.decode('utf-8-sig'))
        (A/(label+'_tables.json')).write_text(json.dumps(p.tables,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
        return label,{'receipt':r,'tables':p.tables}
    except Exception as e:return label,{'error':str(e),'url':url}
with ThreadPoolExecutor(max_workers=6) as pool:out=dict(pool.map(fetch,urls.items()))
(A/'extra_sources.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
for k,v in out.items():print(k,json.dumps(v.get('tables',v.get('error')),ensure_ascii=False))
