import numpy as np
from functools import lru_cache
def hold(p):
    q=1-p; d=p*p/(1-2*p*q)
    return p**4*(1+4*q+10*q*q)+20*p**3*q**3*d
def tb(pa,pb):
    # tiebreak win prob for A, A serves first point then alternate 2-2; simple DP
    @lru_cache(None)
    def f(a,b):
        if a>=7 and a-b>=2: return 1.0
        if b>=7 and b-a>=2: return 0.0
        if a==b and a>=6: # deuce-like
            # two points: one each server, approximate by stationary
            pt=pa; pt2=1-pb
            w=pt*pt2; l=(1-pt)*(1-pt2)
            return w/(w+l)
        n=a+b
        server_A = (n==0) or ((n-1)//2)%2==1
        p = pa if server_A else 1-pb
        return p*f(a+1,b)+(1-p)*f(a,b+1)
    return f(0,0)
def set_dist(ha,hb,ta,a_serves_first):
    # returns dict (ga,gb)->prob
    from collections import defaultdict
    dist=defaultdict(float)
    @lru_cache(None)
    def g(a,b):
        out={}
        if (a>=6 and a-b>=2) or a==7: return {(a,b):1.0}
        if (b>=6 and b-a>=2) or b==7: return {(a,b):1.0}
        if a==6 and b==6:
            return {(7,6):ta,(6,7):1-ta}
        n=a+b
        a_srv = (n%2==0)==a_serves_first
        pw = ha if a_srv else 1-hb
        for k,v in g(a+1,b).items(): out[k]=out.get(k,0)+pw*v
        for k,v in g(a,b+1).items(): out[k]=out.get(k,0)+(1-pw)*v
        return out
    return g(0,0)
def match(pa,pb):
    ha,hb=hold(pa),hold(pb); ta=tb(pa,pb)
    res={}
    for first in (True,False):
        s1=set_dist(ha,hb,ta,first)
        for (a1,b1),p1 in s1.items():
            f2 = first if (a1+b1)%2==0 else not first
            s2=set_dist(ha,hb,ta,f2)
            for (a2,b2),p2 in s2.items():
                w1=a1>b1; w2=a2>b2
                if w1==w2:
                    key=(a1+a2,b1+b2,2 if w1 else 0); res[key]=res.get(key,0)+0.5*p1*p2
                else:
                    f3 = f2 if (a2+b2)%2==0 else not f2
                    for (a3,b3),p3 in set_dist(ha,hb,ta,f3).items():
                        key=(a1+a2+a3,b1+b2+b3,1 if a3>b3 else -1); res[key]=res.get(key,0)+0.5*p1*p2*p3
    return res
def summarize(res,line_total,hcap_b):  # hcap for player B (+)
    over=sum(v for (a,b,s),v in res.items() if a+b>line_total)
    three=sum(v for (a,b,s),v in res.items() if s in (1,-1))
    bcov=sum(v for (a,b,s),v in res.items() if b-a+hcap_b>0)
    blow=sum(v for (a,b,s),v in res.items() if abs(a-b)>=6)
    return over,three,bcov,blow
def mix(pa,pb,sd,n=400,seed=1):
    rng=np.random.default_rng(seed); acc={}
    for _ in range(n):
        f=rng.normal(0,sd)  # relative form shock: + favours A on both serve and return
        r=match(min(max(pa+f,0.4),0.85),min(max(pb-f,0.4),0.85))
        for k,v in r.items(): acc[k]=acc.get(k,0)+v/n
    return acc
for name,pa,pb,line,h in [('P-551 Vallejo(A) v Royer(B): Over22.5, Royer+1.5',0.6370,0.6300,22.5,1.5),('P-555 Bergs(A) v Kopriva(B): Over22.5, Kopriva+3.5',0.641,0.614,22.5,3.5)]:
    print(name)
    o,t,c,b=summarize(match(pa,pb),line,h); print('  iid      : P(Over)=%.3f P(3 sets)=%.3f P(B cover)=%.3f P(|margin|>=6)=%.3f'%(o,t,c,b))
    for sd in (0.03,0.05):
        o,t,c,b=summarize(mix(pa,pb,sd),line,h); print('  shock sd=%.2f: P(Over)=%.3f P(3 sets)=%.3f P(B cover)=%.3f P(|margin|>=6)=%.3f'%(sd,o,t,c,b))
