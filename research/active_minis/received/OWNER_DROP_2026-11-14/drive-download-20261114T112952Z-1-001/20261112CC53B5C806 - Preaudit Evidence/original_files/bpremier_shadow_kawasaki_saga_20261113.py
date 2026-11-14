"""UNVALIDATED chat-local B.Premier source-based sensitivity diagnostic; not a released primary forecast."""
import json, hashlib, datetime
import numpy as np
from pathlib import Path
root=Path('/mnt/data')
MINI='20261112CC53B5C806';KEY=f'LOCAL-{MINI}-G0006'
seed=20261113506
rng=np.random.default_rng(seed)
# all source values pre-target, official 2026-27 prior results
K_F=1256/16; K_A=1355/16
S_F=1095/14; S_A=1333/14
cross_home=(K_F+S_A)/2; cross_away=(S_F+K_A)/2
cross_total=cross_home+cross_away;cross_margin=cross_home-cross_away
# Pre-declared scenarios, fixed counts and descriptive weights; NO fit/calibration
scenarios=[
 {'name':'low','weight':0.25,'n':300000,'reg_total':160.0,'reg_margin':2.5,'sd_total':18.5,'sd_margin':15.2},
 {'name':'base','weight':0.50,'n':600000,'reg_total':164.0,'reg_margin':4.9,'sd_total':18.5,'sd_margin':15.2},
 {'name':'high','weight':0.25,'n':300000,'reg_total':174.0,'reg_margin':7.4,'sd_total':18.5,'sd_margin':15.2},
]
parts=[]; stats={}
for s in scenarios:
 n=s['n']
 total=rng.normal(s['reg_total'],s['sd_total'],n)
 margin=rng.normal(s['reg_margin'],s['sd_margin'],n)
 h=np.maximum(20,np.rint((total+margin)/2)).astype(np.int16)
 a=np.maximum(20,np.rint((total-margin)/2)).astype(np.int16)
 # OT for regulation tie; small same-team extra periods; finish to no tie
 tied=(h==a)
 ot_flag=tied.copy()
 k=0
 while np.any(tied) and k<9:
  count=int(tied.sum());delta_h=rng.integers(4,13,size=count,dtype=np.int16);delta_a=rng.integers(4,13,size=count,dtype=np.int16)
  h[tied]+=delta_h;a[tied]+=delta_a
  tied=(h==a); k+=1
 if np.any(tied): h[tied]+=1
 d=h.astype(np.int32)-a.astype(np.int32); t=h.astype(np.int32)+a.astype(np.int32)
 row={'games':n,'mean_kawasaki':round(float(h.mean()),4),'mean_saga':round(float(a.mean()),4),'mean_total':round(float(t.mean()),4),'mean_margin':round(float(d.mean()),4),'reg_tie_OT_rate':round(float(ot_flag.mean()),5),'kawasaki_winner':round(float(np.mean(d>0)),6),'kawasaki_minus9_5':round(float(np.mean(d>=10)),6),'saga_plus9_5':round(float(np.mean(d<=9)),6),'over169_5':round(float(np.mean(t>=170)),6),'under169_5':round(float(np.mean(t<=169)),6),'both_saga_cushion_and_under':round(float(np.mean((d<=9)&(t<=169))),6),'joint_failure_saga_cushion_and_under':round(float(np.mean((d>=10)&(t>=170))),6)}
 stats[s['name']]=row
 parts.append({'h':h,'a':a,'d':d,'t':t})
h=np.concatenate([p['h'] for p in parts]);a=np.concatenate([p['a'] for p in parts]);d=np.concatenate([p['d'] for p in parts]);t=np.concatenate([p['t'] for p in parts]);
agg={'games':len(t),'mean_kawasaki':float(h.mean()),'mean_saga':float(a.mean()),'mean_total':float(t.mean()),'mean_margin':float(d.mean()),'p_kawasaki_win':float(np.mean(d>0)),'p_saga_win':float(np.mean(d<0)),'p_k_minus9_5':float(np.mean(d>=10)),'p_s_plus9_5':float(np.mean(d<=9)),'p_under169_5':float(np.mean(t<=169)),'p_over169_5':float(np.mean(t>=170)),'joint_saga_plus_and_under':float(np.mean((d<=9)&(t<=169))),'joint_both_fail':float(np.mean((d>=10)&(t>=170))),'OT_rate':float(sum(v['reg_tie_OT_rate']*v['games'] for v in stats.values())/len(t))}
agg={k:round(v,6) if isinstance(v,float) else v for k,v in agg.items()}
res={'identity':{'local_key':KEY,'game':'Kawasaki Brave Thunders vs Saga Ballooners','native_schedule_key':'506581','date':'2026-11-13','league':'2026-27 B.LEAGUE PREMIER'},'version':'shadow-research-v1','status':'UNVALIDATED_CONDITIONAL_DIAGNOSTIC_NOT_PRIMARY','seed':seed,'source_inputs':{'kawasaki_record':'4-12','saga_record':'1-13','K_points_for_season':1256,'K_points_against_season':1355,'K_games':16,'S_points_for_season':1095,'S_points_against_season':1333,'S_games':14,'cross_means_before_shrink':{'home':cross_home,'away':cross_away,'total':cross_total,'margin':cross_margin},'src_k':'https://www.bleague.jp/en/club_detail/?TeamID=727&tab=2','src_s':'https://www.bleague.jp/club_detail/?TeamID=1638','src_teams':'https://www.bleague.jp/game_detail/?ScheduleKey=506581'},'method':'Three predetermined uncalibrated regulation total/margin independent Gaussian scenarios with 40-min game, independent margins/total, integer team score rounding; explicit five-minute OT when tied via discrete scoring branch; no actual possession, referee, shot variance, injury effect fit, covariance fit or verified prestart freeze; scenarios are sensitivity only. The centres are deliberately shrunk toward historical B League FIBA40 context; no validated release. Do not treat sample error as epistemic uncertainty.','scenarios':scenarios,'per_scenario':stats,'aggregate':agg,'endpoint':'Full match including all OT, as rules framework BK-OT-1; ±9.5 spread and 169.5 total no pushes','integrity':{'all_mass_pairs_complement':(int(np.sum(d>=10))+int(np.sum(d<=9))==len(d)) and(int(np.sum(t>=170))+int(np.sum(t<=169))==len(t)),'winner_not_tied':bool(np.all(d!=0)),'scenarios_sum_n':int(sum(s['n'] for s in scenarios))}}
out=root/f'BPREMIER_SHADOW_DIAGNOSTIC_{MINI}-G0006.json';out.write_text(json.dumps(res,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'outputs':str(out),'cross_means':res['source_inputs']['cross_means_before_shrink'],'aggregate':agg,'per_scenario':stats,'checks':res['integrity']},indent=2))
