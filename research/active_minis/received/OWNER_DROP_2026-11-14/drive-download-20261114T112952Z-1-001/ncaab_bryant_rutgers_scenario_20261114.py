"""Research-only uncalibrated 600,000 game scenario; no market inputs, no fitted NCAA model."""
import numpy as np, json, hashlib
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
SEED=20261114
rng=np.random.default_rng(SEED)
# Both teams' official 2026-27 cumulative stats at 13 Nov 2026; entered manually.
inputs={"Rutgers":{"games":2,"points":182,"points_allowed":118,"fga":120,"fta":59,"oreb":25,"tov":19,"opp_fga":116,"opp_fta":33,"opp_oreb":19,"opp_tov":29},"Bryant":{"games":4,"points":250,"points_allowed":287,"fga":227,"fta":69,"oreb":39,"tov":71,"opp_fga":239,"opp_fta":90,"opp_oreb":45,"opp_tov":56}}
for t,v in inputs.items():
    g=v['games'];v['possessions_per_game']=(v['fga']-v['oreb']+v['tov']+0.475*v['fta'])/g
    v['opponent_possessions_per_game']=(v['opp_fga']-v['opp_oreb']+v['opp_tov']+0.475*v['opp_fta'])/g
    v['off_rating']=100*v['points']/(v['possessions_per_game']*g)
    v['def_rating']=100*v['points_allowed']/(v['opponent_possessions_per_game']*g)
pace=(inputs['Rutgers']['possessions_per_game']+inputs['Bryant']['possessions_per_game'])/2
rug_off=(inputs['Rutgers']['off_rating']+inputs['Bryant']['def_rating'])/2
bry_off=(inputs['Bryant']['off_rating']+inputs['Rutgers']['def_rating'])/2
base_pace_scores={"Rutgers":pace*rug_off/100,"Bryant":pace*bry_off/100}
# Low/base/high score centres, chosen as broad manual scenarios around possessions x opponent-averaged efficiencies.
scenarios=[{"name":"low_scoring","weight":0.25,"n":150000,"rutgers_mean":77.,"bryant_mean":58.,"margin_sd":15.5,"total_sd":19.5,"corr_margin_total":0.15},
 {"name":"base","weight":0.5,"n":300000,"rutgers_mean":82.,"bryant_mean":61.,"margin_sd":16.5,"total_sd":21.,"corr_margin_total":0.15},
 {"name":"high_scoring","weight":0.25,"n":150000,"rutgers_mean":88.,"bryant_mean":65.,"margin_sd":17.5,"total_sd":22.5,"corr_margin_total":0.15}]
all_r=[];all_b=[];all_ot=[];cases=[]
for d in scenarios:
 n=d['n']; x=rng.standard_normal(n);z=rng.standard_normal(n)
 m=d['rutgers_mean']-d['bryant_mean']+d['margin_sd']*x
 t=d['rutgers_mean']+d['bryant_mean']+d['total_sd']*(0.15*x+np.sqrt(1-0.15**2)*z)
 r=np.maximum(np.rint((t+m)/2),0).astype(int); b=np.maximum(np.rint((t-m)/2),0).astype(int)
 ot=np.zeros(n,dtype=int)
 # NCAA 5-minute overtime until score unequal; simulated added points are Poisson placeholders, not fitted to NCAA.
 for period in range(1,7):
  tied=r==b
  if not np.any(tied):break
  count=tied.sum();ot[tied]+=1
  r[tied]+=rng.poisson(8.4,count)
  b[tied]+=rng.poisson(8.1,count)
 # Failsafe: ultra-rare tie after six OTs; random winner gets 1 point (none expected).
 tied=r==b
 if np.any(tied):r[tied]+=rng.integers(0,2,size=tied.sum());b[tied]+=(r[tied]==b[tied]).astype(int)
 tot=r+b; margin=r-b
 probs={"bryant_plus_21_5":float(np.mean(margin<=21)),"rutgers_minus_21_5":float(np.mean(margin>=22)),"over_148_5":float(np.mean(tot>=149)),"under_148_5":float(np.mean(tot<=148)),"rutgers_wins":float(np.mean(margin>0)),"bryant_wins":float(np.mean(margin<0))}
 cases.append({**d,"probabilities":probs,"expected_rutgers":float(np.mean(r)),"expected_bryant":float(np.mean(b)),"expected_total":float(np.mean(tot)),"expected_margin":float(np.mean(margin)),"ot_rate":float(np.mean(ot>0))})
 all_r.append(r);all_b.append(b);all_ot.append(ot)
r=np.concatenate(all_r);b=np.concatenate(all_b);ot=np.concatenate(all_ot);tot=r+b;margin=r-b
p={"bryant_plus_21_5":float(np.mean(margin<=21)),"rutgers_minus_21_5":float(np.mean(margin>=22)),"over_148_5":float(np.mean(tot>=149)),"under_148_5":float(np.mean(tot<=148)),"rutgers_wins":float(np.mean(margin>0)),"bryant_wins":float(np.mean(margin<0))}
loss_under=tot>=149;loss_bryant=margin>=22
result={"label":"UNCALIBRATED_RESEARCH_DIAGNOSTIC_ONLY_NOT_PRIMARY","seed":SEED,"n":len(r),"scenarios":cases,"inputs":inputs,"possessions_estimator":"FGA-OREB+TO+0.475*FTA","pace_estimate":pace,"opponent_average_off_efficiency":{"Rutgers":rug_off,"Bryant":bry_off},"pace_times_efficiency_centres":base_pace_scores,"reference_status":"NOT_RUN_NO_RELEASE; NCAA tournament/season profile not validated","model_status":"NO_FIT_NO_ISSUE","rank_scope":"SUPPLIED_ONLY","endpoint":"full-game including NCAA 5-minute OT","overtime_assumption":"draw at regulation; independent Poi(8.4),Poi(8.1) points each 5-min OT; uncalibrated","overall_probabilities":p,"means":{"rutgers":float(r.mean()),"bryant":float(b.mean()),"total":float(tot.mean()),"margin_rutgers":float(margin.mean()),"total_sd":float(tot.std()),"margin_sd":float(margin.std())},"ot_rate":float(np.mean(ot>0)),"joint_failure_of_under148_5_and_bryant_plus21_5":float(np.mean(loss_under&loss_bryant)),"margin_total_corr":float(np.corrcoef(margin,tot)[0,1]),"complement_check":{"side":p['bryant_plus_21_5']+p['rutgers_minus_21_5'],"total":p['under_148_5']+p['over_148_5']},"mc_se_max":float(max(np.sqrt(v*(1-v)/len(r)) for v in p.values()))}
out=Path('/mnt/data/ncaab_bryant_rutgers_scenario_20261114.json');out.write_text(json.dumps(result,indent=2))
print(json.dumps({"overall":p,"means":result['means'],"cases":[{"name":a['name'],"probabilities":a['probabilities']} for a in cases],"pace":pace,"base":base_pace_scores,"joint":result['joint_failure_of_under148_5_and_bryant_plus21_5'],"OT":result['ot_rate'],"mcse":result['mc_se_max']},indent=2))
