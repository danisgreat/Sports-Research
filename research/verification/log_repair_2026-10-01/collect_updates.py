from pathlib import Path
from datetime import datetime,timedelta,timezone
from urllib.request import Request,urlopen
from urllib.parse import urlencode
from concurrent.futures import ThreadPoolExecutor
import hashlib,json
A=Path(__file__).resolve().parent; ROOT=A.parents[2]
OUT=A/('updates_'+datetime.now(timezone.utc).strftime('%H%M%SZ'));OUT.mkdir()
def fetch(item):
    label,url,params=item
    request=Request(url,data=urlencode(params).encode() if params else None,headers={'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8','Referer':'https://www.koreabaseball.com/Schedule/GameCenter/Main.aspx','User-Agent':'Mozilla/5.0','X-Requested-With':'XMLHttpRequest'})
    try:
        with urlopen(request,timeout=20) as response:raw=response.read(12000000);ct=response.headers.get('Content-Type')
        path=OUT/(label+'.body');path.write_bytes(raw)
        r={'source_url':url,'request_params':params,'request_method':'POST' if params else 'GET','retrieved_utc':datetime.now(timezone.utc).isoformat(),'response_sha256':hashlib.sha256(raw).hexdigest(),'response_bytes':len(raw),'body_path':path.relative_to(ROOT).as_posix(),'content_type':ct,'independence_status':'UNKNOWN'}
        (OUT/(label+'_receipt.json')).write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
        try:data=json.loads(raw)
        except Exception:data=None
        return label,{'receipt':r,'data':data}
    except Exception as e:return label,{'error':str(e)}
jobs=[]
for i in range(32):
    date=(datetime(2026,10,1)-timedelta(days=i)).strftime('%Y%m%d')
    jobs.append((date,'https://www.koreabaseball.com/ws/Main.asmx/GetKboGameList',{'leId':'1','srId':'0,1,3,4,5,6,7,8,9','date':date}))
base={'leId':'1','srId':'0','seasonId':'2026','gameId':'20260929HHSS0'}
jobs.extend([('box_sep29','https://www.koreabaseball.com/ws/Schedule.asmx/GetBoxScoreScroll',base),
 ('operations_image','https://6ptotvmi5753.edge.naverncp.com/KBO_IMAGE/KBOHome/resources/images/sub/game_manage.png',None),
 ('npb_current','https://npb.jp/scores/2026/1001/c-d-25/',None),
 ('yahoo_current','https://baseball.yahoo.co.jp/npb/game/2021048568/top',None)])
with ThreadPoolExecutor(max_workers=4) as pool:out=dict(pool.map(fetch,jobs))
(OUT/'results.json').write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
(A/'latest_updates_dir.txt').write_text(str(OUT),encoding='utf-8')
print('Retained',len(out),'responses:',OUT)
print('Failures', {k:v for k,v in out.items() if 'error' in v})
games=out['20261001'].get('data',{}).get('game',[])
for g in games:
    if g.get('G_ID') in ['20261001HHSS0','20261001KTHT0']:print(json.dumps(g,ensure_ascii=False))
