import numpy as np
from scipy.special import expit

def hold(p):
 q=1-p
 return p**4*(1+4*q+10*q*q)+20*p**3*q**3*p*p/(p*p+q*q)

def sim(n,pS,pV,seed=7):
 rng=np.random.default_rng(seed)
 ps=np.array([pS,pV])
 hs=hold(ps)
 overall=np.zeros((n,2),dtype=np.int16)
 sets=np.zeros((n,2),dtype=np.int8)
 first=rng.integers(0,2,n,dtype=np.int8)
 tb_count=np.zeros(n,dtype=np.int8)
 for sett in range(3):
  active=np.where((sets[:,0]<2)&(sets[:,1]<2))[0]
  if not len(active):break
  gs=np.zeros((len(active),2),dtype=np.int8)
  fs=first[active]
  for g in range(13):
   playing=((gs.max(axis=1)<6)|((np.abs(gs[:,0]-gs[:,1])<2)&(gs.max(axis=1)<7))) & ((gs[:,0]+gs[:,1])<12)
   if not np.any(playing): break
   ix=np.where(playing)[0]
   svr=(fs[ix]+(gs[ix,0]+gs[ix,1]))%2
   r=rng.random(len(ix))
   winner=np.where(r<hs[svr],svr,1-svr)
   gs[ix,winner]+=1
  tieidx=np.where((gs[:,0]==6)&(gs[:,1]==6))[0]
  if len(tieidx):
   # individual point-level tiebreak, first serve next game index from service order
   tbs=np.zeros((len(tieidx),2),dtype=np.int16)
   sfirst=fs[tieidx]
   for pt in range(90):
    play=((tbs.max(axis=1)<7)|(np.abs(tbs[:,0]-tbs[:,1])<2))
    if not np.any(play): break
    j=np.where(play)[0]; num=tbs[j,0]+tbs[j,1]
    # points 0 A, 1+2 B, 3+4 A, etc
    svr=(sfirst[j]+((num+1)//2)%2)%2
    r=rng.random(len(j)); winner=np.where(r<ps[svr],svr,1-svr)
    tbs[j,winner]+=1
   win=np.argmax(tbs,axis=1)
   gs[tieidx,win]+=1
   tb_count[active[tieidx]]+=1
  overall[active]+=gs
  sets[active,np.argmax(gs,axis=1)]+=1
  first[active]=(first[active]+(gs[:,0]+gs[:,1]))%2
 diff=overall[:,1]-overall[:,0]
 tot=overall.sum(axis=1)
 return {'serve_point_S':pS,'serve_point_V':pV,'hold_S':hs[0], 'hold_V':hs[1], 'Vmatch':(sets[:,1]==2).mean(),'Vmoregames':(diff>=1).mean(),'Smoregames':(diff<=-1).mean(),'equalgames':(diff==0).mean(),'under23.5':(tot<=23).mean(),'over23.5':(tot>=24).mean(),'mean_games':tot.mean(),'mean_game_margin_V':diff.mean(),'pct_3sets':(sets.sum(axis=1)==3).mean(),'pct_tb':(tb_count>0).mean(),'mean_Vgames':overall[:,1].mean(),'mean_Sgames':overall[:,0].mean(),'sd_games':tot.std(ddof=0),'sd_margin_V':diff.std(ddof=0),'cov_margin_total':np.cov(diff,tot,bias=True)[0,1],'joint_loss_Vminus05_and_over235':((diff<=0)&(tot<=23)).mean(),'joint_win_Vminus05_and_over235':((diff>=1)&(tot>=24)).mean()}

import json
scenarios=[('V_strength',.607,.659),('base',.626,.645),('S_strength',.645,.632)]
out={name:sim(200000,s,v,seed=i+17) for i,(name,s,v) in enumerate(scenarios)}
weights={'V_strength':.25,'base':.5,'S_strength':.25}
cols=['Vmatch','Vmoregames','Smoregames','equalgames','under23.5','over23.5','mean_games','mean_game_margin_V','pct_3sets','pct_tb','mean_Vgames','mean_Sgames','sd_games','sd_margin_V','cov_margin_total','joint_loss_Vminus05_and_over235','joint_win_Vminus05_and_over235']
out['mixture']={k:sum(weights[z]*out[z][k] for z in weights) for k in cols}
print(json.dumps(out,indent=2))
with open('/mnt/data/tennis_illustrative_model_20261112.json','w') as f:json.dump(out,f,indent=2)
