import requests
import json

headers = {
    'teamcode': 'XX',
    'lang': 'ko',
    'channel': 'WEB',
    'User-Agent': 'Mozilla/5.0'
}

r = requests.get('https://api.kbl.or.kr/season/list?seasonCategory=R&gameCode=01&seasonGrade=1', headers=headers)
seasons = r.json()
print(f'Total seasons: {len(seasons)}')
for s in sorted(seasons, key=lambda x: x['seasonCode']):
    sc = s['seasonCode']
    gl = s['glkey']
    sn = s['seasonName']
    ds = s.get('gamedateStart')
    de = s.get('gamedateEnd')
    print(f'seasonCode: {sc:2d} | glkey: {gl:7s} | Name: {sn:10s} | Dates: {ds} to {de}')
