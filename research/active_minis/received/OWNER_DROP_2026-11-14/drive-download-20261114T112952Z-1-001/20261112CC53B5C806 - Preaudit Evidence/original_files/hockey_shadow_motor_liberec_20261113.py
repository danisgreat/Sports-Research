"""Chat-local illustrative Czech U20 goal model; never a qualified/published forecast.
Two independent Poisson 60-minute goal counts, stylized OT and empty-net branches.
Every parameter not directly observed is identified as an assumption.
No target-match outcome data are used.
"""
import json, hashlib
from pathlib import Path
import numpy as np
from scipy.stats import poisson

MINI='20261112CC53B5C806'; GAME=f'LOCAL-{MINI}-G0007'
seed=20261113; rng=np.random.default_rng(seed)
league_gf=[62,81,76,82,69,50,46,53,43,63,47,57,45,46,41,49]
league_gp=[19,19,19,18,19,19,19,18,19,19,19,18,19,17,17,18]
LM=sum(league_gf)/sum(league_gp)
# Motor n19 GF69 GA45; Liberec n17 GF41 GA71; toy pseudo-game shrinkage k=10 (assumed)
k=10
OM=(69+k*LM)/(19+k); DM=(45+k*LM)/(19+k)
OL=(41+k*LM)/(17+k); DL=(71+k*LM)/(17+k)
lamM=(OM+DL)/2; lamL=(OL+DM)/2
# No verified goalie assignments or Czech-junior empty-net frequencies. Sensitivity only.
scenarios=[
 dict(name='LOW_CONVERSION',weight=.25,lambda_motor=3.10,lambda_liberec=2.05,p_empty_net_if_leading_by_one=.15),
 dict(name='BASE_SHRUNK_SEASON',weight=.50,lambda_motor=round(lamM,6),lambda_liberec=round(lamL,6),p_empty_net_if_leading_by_one=.30),
 dict(name='HIGH_PACE_WEAK_GOALTENDING',weight=.25,lambda_motor=4.25,lambda_liberec=2.90,p_empty_net_if_leading_by_one=.45),
]
# Official Liberec current-year JUN fixtures: oldest to newest, excluding target.
lib_scores=[('2026-09-04','Litvinov',2,3),('2026-09-05','Karlovy Vary',1,4),('2026-09-11','Vitkovice',3,4),('2026-09-12','Trinec',3,6),('2026-09-18','Jihlava',0,2),('2026-09-19','Motor',3,4),('2026-09-25','Mountfield HK',1,8),('2026-09-26','Pardubice',1,7),('2026-09-28','Mlada Boleslav',3,5),('2026-10-10','Sparta Praha',3,5),('2026-10-16','Plzen',5,6),('2026-10-17','Slavia Praha',2,1),('2026-10-23','Karlovy Vary',1,2),('2026-10-24','Litvinov',4,3),('2026-10-28','Poruba',3,2),('2026-10-30','Trinec',1,5),('2026-10-31','Vitkovice',5,4)]
motor_recent=[('2026-10-17','Litvinov',3,1),('2026-10-19','Slavia Praha',3,1),('2026-10-23','Plzen',5,1),('2026-10-30','Mountfield HK',3,4),('2026-10-31','Pardubice',2,3)]
def windows(rows):
    ans={}
    for n in (5,10,15,20):
        q=rows[-n:];actual=len(q)
        ans['L'+str(n)]={'n':actual,'GF':sum(x[2] for x in q),'GA':sum(x[3] for x in q),'GF_per_game':round(sum(x[2] for x in q)/actual,4),'GA_per_game':round(sum(x[3] for x in q)/actual,4),'total_per_game':round(sum(x[2]+x[3] for x in q)/actual,4),'complete_window':actual==n}
    return ans

MAX_SCORE=24;xs=np.arange(MAX_SCORE+1)
# Monte Carlo determines the shadow only. Same random generation across all rows from a common state tree.
def sim(s,n):
    m=rng.poisson(s['lambda_motor'],size=n)
    l=rng.poisson(s['lambda_liberec'],size=n)
    # Emergency pulled-goalie sensitivity branch when lead = 1; the actual
    # rate and whether already in the Poisson baseline are UNFITTED.
    p=s['p_empty_net_if_leading_by_one']
    one_m=m==l+1;one_l=l==m+1
    rand=rng.random(n)
    m=m+(one_m & (rand<p));l=l+(one_l & (rand<p))
    # For a regulation tie, winner adds exactly one by OT/SO scoring convention.
    # Actual operator settlement may differ and is NOT VERIFIED.
    draw=m==l
    dec=rng.random(n)
    motor_ot=draw & (dec<s['lambda_motor']/(s['lambda_motor']+s['lambda_liberec']))
    lib_ot=draw & ~motor_ot
    m=m+motor_ot;l=l+lib_ot
    total=m+l;margin=m-l
    # half lines => no pushes in this assumed endpoint.
    probs={'motor_minus_1_5':float(np.mean(margin>=2)),'liberec_plus_1_5':float(np.mean(margin<2)),'over_5_5':float(np.mean(total>=6)),'under_5_5':float(np.mean(total<=5)),'motor_win':float(np.mean(margin>0)),'liberec_win':float(np.mean(margin<0))}
    # When R1 is Lib+1.5 and R2 Over 5.5, joint loss occurs if motor wins by >=2 AND total<=5.
    probs['loss_both_lib_plus_and_over']=float(np.mean((margin>=2)&(total<=5)))
    return {'name':s['name'],'weight':s['weight'],'simulations':n,'inputs':s,'probabilities':probs,'moments':{'motor_mean':float(m.mean()),'liberec_mean':float(l.mean()),'total_mean':float(total.mean()),'margin_mean':float(margin.mean()),'total_sd':float(total.std()),'margin_sd':float(margin.std())},'regulation_draw_rate_before_ot':None}

total_n=1_200_000
rows=[sim(s,int(total_n*s['weight'])) for s in scenarios]
keys=rows[0]['probabilities'].keys()
mix={k:sum(r['weight']*r['probabilities'][k] for r in rows) for k in keys}
mom={k:sum(r['weight']*r['moments'][k] for r in rows) for k in rows[0]['moments']}
out={'event_id':GAME,'label':'EXPLORATORY_SHADOW_UNCALIBRATED_NOT_PRIMARY','seed':seed,'execution':'MONTE_CARLO_EXECUTED','total_simulations':total_n,'source_league_goals':sum(league_gf),'source_league_team_games':sum(league_gp),'league_mean_team_goals':LM,'shrinkage_k_assumed':k,'shrunk_rates':{'attack_motor':OM,'defense_motor':DM,'attack_liberec':OL,'defense_liberec':DL,'lambda_motor':lamM,'lambda_liberec':lamL},'scenario_results':rows,'mixture_probabilities':mix,'mixture_means_note':'Scenario-weighted conditional means; SD field is weighted mean of scenario SDs, not exact mixture SD','mixture_moments':mom,'liberec_verified_windows':windows(lib_scores),'motor_verified_L5':windows(motor_recent)['L5'],'source_urls':['https://ceskyhokej.cz/competition/standings/1','https://www.hcbilitygri.cz/matches/JUN','https://www.jchokej.cz/archiv-kratkych-zprav?page=2','https://czehockey.cz/game/detail/178203'],'limitations':['No verified Czech U20-goalie starters or injury/line changes','No independently fitted Czech junior scoring family, EN propensity or OTTie win model','Poisson goal process omits correlated scoring, penalties, score effects and conditional shooting quality','Empty-net branch may double-count an effect in raw season rates and is sensitivity only',"Operator settlement terms for full game including overtime/shootout are unknown",'NOT qualified to publish primary forecast probability; no GitHub pregame run or freeze']}
path=Path('/mnt/data/HOCKEY_SHADOW_DIAGNOSTIC_20261112CC53B5C806-G0007.json')
path.write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps({'mixture':mix,'moments':mom,'scenarios':[{r['name']:r['probabilities']} for r in rows],'liberec_windows':out['liberec_verified_windows'],'file':str(path),'sha256':hashlib.sha256(path.read_bytes()).hexdigest()},indent=2))
