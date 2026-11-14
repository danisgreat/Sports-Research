"""RESEARCH-ONLY sensitivity diagnostic, NOT a fitted or published forecast.
2026-11-13 Kawasaki Brave Thunders v Saga Ballooners. Market-blind.
All scores/parameters must be understood as input assumptions and source checks.
Run: python bleague_kawasaki_saga_scenario_20261113.py
"""
import json
from pathlib import Path
import numpy as np

DATA = {
 'Kawasaki': [
 ('2026-11-11','Shimane','H',74,95),('2026-11-09','Altiri Chiba','H',76,85),
 ('2026-11-06','Shiga','A',75,81),('2026-11-01','Yokohama BC','H',66,77),
 ('2026-10-31','Yokohama BC','H',65,75),('2026-10-26','Utsunomiya','A',92,89),
 ('2026-10-24','Sendai','H',82,93),('2026-10-21','Osaka','H',101,67),
 ('2026-10-19','Shimane','A',69,80),('2026-10-16','Ibaraki','H',74,82),
 ('2026-10-10','Alvark Tokyo','H',82,94),('2026-10-08','Akita','A',87,81),
 ('2026-10-04','Altiri Chiba','A',82,74),('2026-10-03','Altiri Chiba','A',90,99),
 ('2026-09-27','Nagoya D','H',78,90),('2026-09-26','Nagoya D','H',63,93)],
 'Saga': [
 ('2026-11-08','Chiba Jets','H',103,111),('2026-11-01','Mikawa','A',78,84),
 ('2026-10-31','Mikawa','A',83,100),('2026-10-26','Alvark Tokyo','H',88,112),
 ('2026-10-21','Nagasaki','H',66,84),('2026-10-18','Kyoto','A',70,115),
 ('2026-10-16','Hokkaido','H',90,109),('2026-10-12','Gunma','H',61,72),
 ('2026-10-10','Kobe','A',84,77),('2026-10-08','Alvark Tokyo','A',74,90),
 ('2026-10-04','San-En','H',89,93),('2026-10-03','San-En','H',61,97),
 ('2026-09-27','Hiroshima','H',61,89),('2026-09-25','Hiroshima','H',87,100)]
}
source_urls={
 'official_game':'https://www.bleague.jp/game_detail/?ScheduleKey=506581',
 'official_kawasaki':'https://www.bleague.jp/record/?club1=727&club2=0',
 'official_saga':'https://www.bleague.jp/record/?club1=1638&club2=0',
 'secondary_kawasaki':'https://bleague.sports-shirabe.com/kawasaki-brave-thunders/',
 'secondary_saga':'https://bleague.sports-shirabe.com/saga-ballooners/',
 'eff_kawasaki':'https://www.bleague-db.com/teams/727',
 'eff_saga':'https://www.bleague-db.com/teams/1638',
 'saga_dudzinski_injury':'https://ballooners.jp/news/detail/id=52366',
 'saga_uchio_injury':'https://ballooners.jp/news/detail/id=48255?nf=0',
 'kawasaki_araya_injury':'https://kawasaki-bravethunders.com/news/detail/id=25908',
}
team_season={'Kawasaki':{'ppg':78.5,'opp_ppg':84.7,'offrtg':106.4,'defrtg':116.2,'games':16},'Saga':{'ppg':78.2,'opp_ppg':95.2,'offrtg':103.9,'defrtg':126.5,'games':14}}
league_assumed_eff=112.0 # ANALYST ASSUMPTION: contemporaneous league strength, not measured full 26-team exposure
league_old_total=159.19
raw_total_sd=17.66
raw_margin_sd=14.94
width_stale_multiplier=1.10  # assumption: early-season / uncertain roster width expansion
model_sd_total=raw_total_sd*width_stale_multiplier
model_sd_margin=raw_margin_sd*width_stale_multiplier
assumed_corr=0.08  # unmeasured, sensitivity only
home_margin_assumption=0.61 # historical B League season baseline in PARAMETERS.md; not new measured team edge
recency_blend=0.20 # analyst assumption, not tuned

windows={}
for name,rows in DATA.items():
    for n in [5,10,15,20]:
        use=rows[:n]
        windows.setdefault(name,{})[f'L{n}']={
           'n':len(use),'points_for':round(np.mean([z[3] for z in use]),3),
           'points_against':round(np.mean([z[4] for z in use]),3),
           'mean_total':round(np.mean([z[3]+z[4] for z in use]),3),
           'wins':sum(z[3]>z[4] for z in use),
           'losses':sum(z[3]<z[4] for z in use),
           'full_window_available':len(rows)>=n,
        }
    windows[name]['season']={'n':len(rows),'pf':round(np.mean([z[3] for z in rows]),3),'pa':round(np.mean([z[4] for z in rows]),3),'record':f"{sum(z[3]>z[4] for z in rows)}-{sum(z[3]<z[4] for z in rows)}"}

pace=np.mean([team_season[k]['ppg']/(team_season[k]['offrtg']/100) for k in team_season])
mid_k=pace*(team_season['Kawasaki']['offrtg']+team_season['Saga']['defrtg'])/200
mid_s=pace*(team_season['Saga']['offrtg']+team_season['Kawasaki']['defrtg'])/200
add_k=pace*(team_season['Kawasaki']['offrtg']+team_season['Saga']['defrtg']-league_assumed_eff)/100
add_s=pace*(team_season['Saga']['offrtg']+team_season['Kawasaki']['defrtg']-league_assumed_eff)/100
rec_k=recency_blend*(windows['Kawasaki']['L5']['points_for']-team_season['Kawasaki']['ppg'])
rec_s=recency_blend*(windows['Saga']['L5']['points_for']-team_season['Saga']['ppg'])
# Scenarios allow uncertainty over pace and how to reconcile opponent adjusted strengths.
cases=[
 ('LOW_SLOW_MIDPOINT',.25,.97,mid_k,mid_s),
 ('BASE_BLEND',.50,1.00,0.5*(mid_k+add_k),0.5*(mid_s+add_s)),
 ('HIGH_FAST_ADDITIVE',.25,1.03,add_k,add_s)]
N=600000
rng=np.random.default_rng(20261113)
results=[]
all_x=[];all_y=[]
for name,weight,pace_ratio,k_base,s_base in cases:
    n=int(round(N*weight))
    mean_k=k_base*pace_ratio +rec_k+home_margin_assumption/2
    mean_s=s_base*pace_ratio +rec_s-home_margin_assumption/2
    mean_total=mean_k+mean_s
    mean_margin=mean_k-mean_s
    # One joint score object (total and signed margin), not independently priced handicaps/totals.
    z=rng.standard_normal((n,2))
    total=mean_total+model_sd_total*z[:,0]
    margin=mean_margin+model_sd_margin*(assumed_corr*z[:,0]+np.sqrt(1-assumed_corr**2)*z[:,1])
    k=np.maximum(0,np.rint((total+margin)/2)).astype(np.int32)
    s=np.maximum(0,np.rint((total-margin)/2)).astype(np.int32)
    # Full match includes 5-minute OT in tied regulation games; 9.5 per team per period assumption.
    ties=(k==s)
    ot_first=int(ties.sum())
    num_ties=ties.copy(); ot_round=0
    while np.any(ties) and ot_round<12:
        nt=int(ties.sum());
        k[ties]+=rng.poisson(9.5,nt)
        s[ties]+=rng.poisson(9.5,nt)
        ties=(k==s)
        ot_round+=1
    assert not ties.any(),"Unexpected tie after 12 OTs; need keep simulating"
    ar={'KAWASAKI_MINUS_9_5':float(np.mean(k-s>=10)),
        'SAGA_PLUS_9_5':float(np.mean(k-s<=9)),
        'OVER_169_5':float(np.mean(k+s>=170)),
        'UNDER_169_5':float(np.mean(k+s<=169))}
    results.append({'case':name,'weight':weight,'N':n,'expected_reg_kawasaki':round(mean_k,4),'expected_reg_saga':round(mean_s,4),'expected_reg_total':round(mean_total,4),'expected_reg_kawasaki_margin':round(mean_margin,4),'initial_regulation_tie_rate':round(ot_first/n,5),'final_mean_kawasaki':round(float(k.mean()),4),'final_mean_saga':round(float(s.mean()),4),'final_mean_total':round(float((k+s).mean()),4),'final_mean_margin':round(float((k-s).mean()),4),'rates':ar})
    all_x.append(k);all_y.append(s)
k=np.concatenate(all_x);s=np.concatenate(all_y)
assert len(k)==N
pct={'KAWASAKI_MINUS_9_5':float(np.mean(k-s>=10)),
     'SAGA_PLUS_9_5':float(np.mean(k-s<=9)),
     'OVER_169_5':float(np.mean(k+s>=170)),
     'UNDER_169_5':float(np.mean(k+s<=169))}
assert abs(pct['KAWASAKI_MINUS_9_5']+pct['SAGA_PLUS_9_5']-1)<1e-10
assert abs(pct['OVER_169_5']+pct['UNDER_169_5']-1)<1e-10
ranked=sorted(pct,key=lambda x:-pct[x])
joint=float(np.mean((k-s>=10)&(k+s>=170))) if ranked[:2]==['SAGA_PLUS_9_5','UNDER_169_5'] else float(np.mean((k-s>=10)&(k+s<=169)))
result={
 'status':'ILLUSTRATIVE_NOT_PRIMARY; UNCALIBRATED_QUALITATIVE; NO_OFFICIAL_REFERENCE_RUN',
 'event':'Kawasaki Brave Thunders vs Saga Ballooners',
 'nominal_start':'2026-11-13T21:05:00+11:00',
 'model':{'seed':20261113,'N':N,'method':'Three-scenario bivariate normal regulation total and margin with integer rounding and explicit 5-min OT Poisson branching','widths':{'total':model_sd_total,'home_margin':model_sd_margin},'correlation_assumed':assumed_corr,'regulation_ot_poisson_pts_per_team':9.5,'low_base_high_weights':[.25,.5,.25],'league_efficiency_benchmark_ASSUMED':league_assumed_eff,'possessions_per_game_derived':pace,'form_blend_ASSUMED':recency_blend,'venue_margin_assumed':home_margin_assumption,'league_profile_old_not_frozen':{'total_mean':league_old_total,'margin_sd':raw_margin_sd,'total_sd':raw_total_sd},'input_rating_approach':'range from average of team OFFRTG and opponent DEFRTG to additive league-centered strength; not calibrated'},
 'source_urls':source_urls,'season':team_season,'history':DATA,'windows':windows,
 'cases':results,'overall':{'rates':pct,'MC_standard_error_max':max(np.sqrt(p*(1-p)/N) for p in pct.values()),'ranking':ranked,'mean_score':[float(k.mean()),float(s.mean())],'mean_total':float((k+s).mean()),'mean_kawasaki_margin':float((k-s).mean()),'total_sd':float(np.std(k+s)),'margin_sd':float(np.std(k-s)),'P_home_win':float(np.mean(k>s)),'P_away_win':float(np.mean(s>k)),'joint_failure_first_two':joint},
 'limits':['Input sources reflect pre-13-Nov results, but publishing times not independently verified for every row.','Neither exact tip time nor starters/bench confirmed.','No venue-specific rest/fouling/possession model fit.','Prior B League width parameters are development-only and not validated for 2026-27 B.Premier.','Assumed midpoint/additive rate reconciliation and home effect are NOT approved adjustments.','No formal league-only baseline run or model reference freeze.','No official issued numerical probability or certified accuracy.','No market odds/predictions used.']
}
out=Path('/mnt/data/bleague_kawasaki_saga_scenario_20261113.json')
out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print('windows',json.dumps(windows,indent=2));print('center',result['overall']);print('cases',json.dumps(results,indent=2));print('file',str(out))
