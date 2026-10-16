"""Experimental, SPORTS_ONLY tennis singles forecast and delayed Hedge feedback.

Independent tennis outcome distribution: match winner is NOT inferred from total games.
This lane is separate from MODEL_ASSISTED_PRIMARY_V3 until prospectively qualified.
Inputs must be source-reviewed point statistics; no odds or market predictors.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import math
from collections import defaultdict
from datetime import datetime, timezone
from functools import lru_cache
from pathlib import Path

ARMS = ("SURFACE_FAST", "SURFACE_SLOW", "SURFACE_ELO", "COHORT_BASE")
POLICY = "TENNIS_EXPERIMENTAL_HEDGE_V1"
SURFACES = {"HARD", "CLAY", "GRASS", "CARPET"}
MIN_HISTORY, MIN_PLAYER_MATCHES = 40, 5
ETA = 2.0  # fixed provisional policy; NOT calibrated or prospectively qualified


class TennisAdmissionError(ValueError):
    pass


def stamp(value):
    try:
        d = datetime.fromisoformat(str(value).replace("Z", "+00:00"))
        if d.tzinfo is None:
            raise ValueError("missing time zone")
        return d.astimezone(timezone.utc)
    except (ValueError, TypeError) as e:
        raise TennisAdmissionError(f"invalid timezone-aware timestamp: {value}") from e


def rows(path):
    with Path(path).open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def csv_content(items):
    if not items:
        raise TennisAdmissionError("cannot write empty CSV")
    f = io.StringIO(newline="")
    w = csv.DictWriter(f, fieldnames=list(items[0]), lineterminator="\n")
    w.writeheader()
    w.writerows(items)
    return f.getvalue().encode()


def sha(b):
    return hashlib.sha256(b).hexdigest()


def finite_int(v, name):
    try:
        x = int(str(v))
        if str(x) != str(v).strip() or x < 0:
            raise ValueError()
        return x
    except (ValueError, TypeError) as e:
        raise TennisAdmissionError(f"invalid nonnegative integer {name}") from e


def source_valid(row):
    if not row.get("source_url", "").startswith("https://"):
        raise TennisAdmissionError("historical source must be HTTPS")
    path = Path(row.get("evidence_path", ""))
    if not path.is_file() or sha(path.read_bytes()) != row.get("evidence_sha256"):
        raise TennisAdmissionError("missing/mismatched original evidence capture")


def prepare(request, history):
    required = ("event_id", "competition", "player1", "player2", "surface", "best_of", "scheduled_start", "issue_at")
    if any(not request.get(k) for k in required):
        raise TennisAdmissionError("missing request identity or timing")
    if request["player1"] == request["player2"] or request["surface"] not in SURFACES:
        raise TennisAdmissionError("invalid players or surface")
    bo = finite_int(request["best_of"], "best_of")
    if bo not in (3, 5):
        raise TennisAdmissionError("tennis singles best_of must be 3 or 5")
    if request.get("format", "SINGLES") != "SINGLES" or request.get("outcome_exposure") != "NONE_RECORDED":
        raise TennisAdmissionError("unsupported match format or outcome exposure")
    horizon = min(stamp(request[k]) for k in ("scheduled_start", "issue_at", "actual_start") if request.get(k))
    seen, admitted = set(), []
    for r in history:
        if r.get("competition") != request["competition"]:
            raise TennisAdmissionError("cross-competition training not allowed")
        key = r.get("event_id")
        if not key or key in seen or key == request["event_id"]:
            raise TennisAdmissionError("duplicate, blank or target history identity")
        seen.add(key)
        if r.get("status") != "FINAL" or r.get("admission") != "RESEARCH_INPUT_REVIEWED":
            raise TennisAdmissionError("unreviewed/retired/unfinished history")
        if r.get("format", "SINGLES") != "SINGLES" or r.get("surface") not in SURFACES:
            raise TennisAdmissionError("unsupported historical tennis scope")
        d, final, available = (stamp(r[k]) for k in ("date", "final_at", "available_at"))
        if not (d <= final <= available <= horizon and d.date() < horizon.date()):
            raise TennisAdmissionError("history known-at or chronology violation")
        if r.get("player1") == r.get("player2") or r.get("winner") not in (r.get("player1"), r.get("player2")):
            raise TennisAdmissionError("invalid historical winner/player")
        vals = [finite_int(r[k], k) for k in ("p1_serve_won", "p1_serve_total", "p2_serve_won", "p2_serve_total")]
        if min(vals[1], vals[3]) < 20 or vals[0] > vals[1] or vals[2] > vals[3]:
            raise TennisAdmissionError("missing/invalid service-point exposure")
        source_valid(r)
        admitted.append(dict(r, _date=d, _points=vals))
    if len(admitted) < MIN_HISTORY:
        raise TennisAdmissionError("insufficient reviewed historical matches")
    counts = {p: sum(p in (r["player1"], r["player2"]) for r in admitted)
              for p in (request["player1"], request["player2"])}
    if min(counts.values()) < MIN_PLAYER_MATCHES:
        raise TennisAdmissionError("insufficient player-level historical matches")
    return sorted(admitted, key=lambda x: (x["_date"], x["event_id"])), horizon, counts


def game_hold(p):
    if not (0 < p < 1):
        raise TennisAdmissionError("serve-point rate outside (0,1)")
    q = 1-p
    return p**4*(1+4*q+10*q*q) + 20*p**3*q**3*(p*p/(p*p+q*q))


def tiebreak_win(p1, p2, first_server):
    # At 6-all consecutive serve points include one per player, with a
    # repeat-until-two-point-margin tail. Exact deuce boundary avoids truncation.
    win_pair = p1*(1-p2)
    lose_pair = (1-p1)*p2
    tied = win_pair/(win_pair+lose_pair)

    @lru_cache(None)
    def dp(a, b):
        if a >= 7 and a-b >= 2:
            return 1.0
        if b >= 7 and b-a >= 2:
            return 0.0
        if a == b and a >= 6:
            return tied
        i = a+b
        srv = first_server if i == 0 else (1-first_server if ((i-1)//2)%2 == 0 else first_server)
        point = p1 if srv == 0 else 1-p2
        return point*dp(a+1,b)+(1-point)*dp(a,b+1)

    return dp(0, 0)


def set_distribution(p1, p2, first_server):
    hold1, hold2 = game_hold(p1), game_hold(p2)
    out = defaultdict(float)

    def walk(g1, g2, server, mass):
        if g1 >= 6 and g1-g2 >= 2 or g2 >= 6 and g2-g1 >= 2:
            out[(g1,g2,server)] += mass
            return
        if g1 == 6 and g2 == 6:
            p = tiebreak_win(p1,p2,server)
            out[(7,6,1-server)] += mass*p
            out[(6,7,1-server)] += mass*(1-p)
            return
        g = hold1 if server == 0 else 1-hold2
        walk(g1+1,g2,1-server,mass*g)
        walk(g1,g2+1,1-server,mass*(1-g))

    walk(0,0,first_server,1.0)
    if abs(sum(out.values())-1) > 1e-10:
        raise TennisAdmissionError("set mass does not sum to one")
    return out


def match_grid(p1,p2,best_of):
    if best_of not in (3,5):
        raise TennisAdmissionError("unsupported best-of format")
    sets_needed=best_of//2+1
    one={s:set_distribution(p1,p2,s) for s in (0,1)}
    states={(0,0,0,0,0):0.5, (0,0,0,0,1):0.5}
    terminal=defaultdict(float)
    for _ in range(best_of):
        nxt=defaultdict(float)
        for (s1,s2,g1,g2,server),weight in states.items():
            for (a,b,new_server),prob in one[server].items():
                ns1,ns2=s1+(a>b),s2+(b>a)
                dest=(ns1,ns2,g1+a,g2+b,new_server)
                if ns1==sets_needed or ns2==sets_needed:
                    terminal[(1 if ns1==sets_needed else 2,g1+a,g2+b,ns1,ns2)]+=weight*prob
                else:
                    nxt[dest]+=weight*prob
        states=nxt
    if states or abs(sum(terminal.values())-1)>1e-9:
        raise TennisAdmissionError("match distribution not normalised")
    return dict(terminal)


def price(grid, contract):
    family=contract.get("family")
    side=contract.get("side")
    line=contract.get("line", "")
    if family=="MATCH_WINNER":
        if side not in ("PLAYER1","PLAYER2") or line not in ("", None):
            raise TennisAdmissionError("match-winner side/line invalid")
    elif family=="GAMES_HANDICAP":
        if side not in ("PLAYER1","PLAYER2"):
            raise TennisAdmissionError("invalid games-handicap side")
    elif family=="GAMES_TOTAL":
        if side not in ("OVER","UNDER"):
            raise TennisAdmissionError("invalid games-total side")
    else:
        raise TennisAdmissionError("unsupported tennis contract family")
    if family!="MATCH_WINNER":
        try:
            line=float(line)
        except (ValueError,TypeError) as e:
            raise TennisAdmissionError("non-numeric tennis line") from e
        if not math.isfinite(line):
            raise TennisAdmissionError("non-finite tennis line")
    w=push=loss=0.0
    for (winner,g1,g2,_,_),mass in grid.items():
        if family=="MATCH_WINNER":
            value=1 if (winner==1)==(side=="PLAYER1") else -1
        elif family=="GAMES_HANDICAP":
            value=(g1-g2 if side=="PLAYER1" else g2-g1)+line
        else:
            value=(g1+g2-line)*(1 if side=="OVER" else -1)
        if value>0:w+=mass
        elif value<0:loss+=mass
        else:push+=mass
    return dict(win=w,push=push,loss=loss,p_card=w/(w+loss) if w+loss else None)


def _logistic(x):
    return 1/(1+math.exp(-max(-40,min(40,x))))


def _logit(p):
    return math.log(p/(1-p))


def learned_points(history, request, horizon, mode):
    # Each expert fits a source-reviewed, surface-aware hierarchical posterior.
    surface=request["surface"]
    cohort=[r for r in history if r["surface"]==surface]
    if len(cohort)<15:
        raise TennisAdmissionError("insufficient exact-surface cohort for tennis probability model")
    total_w=sum(r["_points"][0]+r["_points"][2] for r in cohort)
    total_n=sum(r["_points"][1]+r["_points"][3] for r in cohort)
    prior=total_w/total_n
    if not 0.35<prior<0.80:
        raise TennisAdmissionError("unusual source cohort; investigate before fit")
    if mode=="COHORT_BASE":
        return prior,prior
    half_life=90 if mode=="SURFACE_FAST" else 365
    target_surface_only=(mode=="SURFACE_FAST")

    def player_stats(player):
        sw=sn=rw=rn=0.0
        for r in history:
            if target_surface_only and r["surface"] != surface:
                continue
            age=max(0,(horizon-r["_date"]).total_seconds()/86400)
            weight=2**(-age/half_life)
            a,b,c,d=r["_points"]
            if player==r["player1"]:
                sw+=weight*a; sn+=weight*b
                rw+=weight*(d-c); rn+=weight*d
            if player==r["player2"]:
                sw+=weight*c; sn+=weight*d
                rw+=weight*(b-a); rn+=weight*b
        # Shrink service and return to within-cohort means; units are points.
        serve=(sw+200*prior)/(sn+200)
        ret=(rw+200*(1-prior))/(rn+200)
        return serve,ret

    s1,_=player_stats(request["player1"])
    s2,_=player_stats(request["player2"])
    _,r1=player_stats(request["player1"])
    _,r2=player_stats(request["player2"])
    p1=_logistic(_logit(s1)-_logit(1-r2)+_logit(prior))
    p2=_logistic(_logit(s2)-_logit(1-r1)+_logit(prior))
    return p1,p2


def elo_p1(history, request):
    # Point-in-time, distinct matches only. Surface-specific deviation shrinks.
    global_rating=defaultdict(lambda:1500.0)
    surface_rating=defaultdict(lambda:1500.0)
    for r in history:
        a,b=r["player1"],r["player2"]
        sa,sb=(a,r["surface"]),(b,r["surface"])
        ra=0.7*global_rating[a]+0.3*surface_rating[sa]
        rb=0.7*global_rating[b]+0.3*surface_rating[sb]
        pa=_logistic(math.log(10)*(ra-rb)/400)
        err=(1 if r["winner"]==a else 0)-pa
        global_rating[a]+=14*err;global_rating[b]-=14*err
        surface_rating[sa]+=12*err;surface_rating[sb]-=12*err
    p1,p2=request["player1"],request["player2"]
    surf=request["surface"]
    rating1=0.7*global_rating[p1]+0.3*surface_rating[(p1,surf)]
    rating2=0.7*global_rating[p2]+0.3*surface_rating[(p2,surf)]
    return _logistic(math.log(10)*(rating1-rating2)/400)


def reweight_match(grid, p1):
    old=sum(m for (winner,*_),m in grid.items() if winner==1)
    if not 0<old<1:
        raise TennisAdmissionError("cannot reweight degenerate match grid")
    return {k:m*(p1/old if k[0]==1 else (1-p1)/(1-old)) for k,m in grid.items()}


def weights(feedback, request, horizon):
    sums=[0.0]*len(ARMS)
    seen=set()
    effective=0
    for r in feedback:
        if r.get("competition")!=request["competition"] or r.get("policy")!=POLICY:
            raise TennisAdmissionError("unsupported feedback context")
        eid=r.get("event_id")
        if not eid or eid==request["event_id"] or eid in seen:
            raise TennisAdmissionError("duplicate/target feedback")
        seen.add(eid)
        if stamp(r["available_at"])>horizon:
            continue
        # A written number is not feedback: reverify its original frozen model
        # and recompute each expert's loss from the observed completed sets.
        bundle=Path(r.get("bundle_path", ""))
        original=verify(bundle)
        original_req=rows(bundle/"REQUEST.csv")[0]
        if original["event_id"]!=eid or original_req["competition"]!=r["competition"]:
            raise TennisAdmissionError("feedback event/competition conflicts with frozen bundle")
        if sha((bundle/"RECEIPT.csv").read_bytes())!=r.get("original_receipt_sha256"):
            raise TennisAdmissionError("feedback original receipt hash mismatch")
        if not (stamp(r["final_at"])<=stamp(r["available_at"])):
            raise TennisAdmissionError("feedback chronology invalid")
        source_valid(r)
        winner=tennis_score(r["official_sets"],int(original_req["best_of"]))[0]
        if r.get("winner")!=original_req["player1" if winner==1 else "player2"]:
            raise TennisAdmissionError("feedback winner conflicts with tennis sets")
        gg=read_grids(bundle)
        for i,arm in enumerate(ARMS):
            v=float(r["loss_"+arm])
            p=sum(m for k,m in gg[arm].items() if k[0]==1)
            if not math.isfinite(v) or not 0<=v<=1 or abs(v-(p-(winner==1))**2)>1e-10:
                raise TennisAdmissionError("invalid or forged expert feedback loss")
            sums[i]+=v
        effective+=1
    raw=[math.exp(-ETA*(v-min(sums))) for v in sums]
    return [v/sum(raw) for v in raw],effective


def mixed(grids, ws):
    out=defaultdict(float)
    for arm,w in zip(ARMS,ws):
        for key,prob in grids[arm].items():
            out[key]+=w*prob
    if abs(sum(out.values())-1)>1e-8:
        raise TennisAdmissionError("mixed grid incoherent")
    return dict(out)


def get_predictions(request,history,contracts,feedback=()):
    past,horizon,counts=prepare(request,history)
    if not contracts or any(c.get("contract_key", "")=="" for c in contracts):
        raise TennisAdmissionError("empty/unidentified contract set")
    if len({c["contract_key"] for c in contracts})!=len(contracts):
        raise TennisAdmissionError("duplicate tennis contract")
    grids={}
    for arm in ("SURFACE_FAST","SURFACE_SLOW","COHORT_BASE"):
        a,b=learned_points(past,request,horizon,arm)
        grids[arm]=match_grid(a,b,int(request["best_of"]))
    grids["SURFACE_ELO"]=reweight_match(grids["SURFACE_SLOW"],elo_p1(past,request))
    ws,nfb=weights(feedback,request,horizon)
    final=mixed(grids,ws)
    outputs=[]
    for c in contracts:
        pred=price(final,c)
        base=price(grids["COHORT_BASE"],c)
        outputs.append(dict(contract_key=c["contract_key"],family=c["family"],side=c["side"],line=c.get("line", ""),
                            **pred,baseline_p=base["p_card"],policy=POLICY,qualification="EXPERIMENTAL_NOT_CERTIFIED"))
    return grids,final,outputs,ws,nfb,counts,horizon


def immutable_write(folder,files):
    folder=Path(folder)
    if folder.exists():
        raise TennisAdmissionError("output exists; immutable bundle not overwritten")
    folder.mkdir(parents=True)
    try:
        for k,v in files.items():
            (folder/k).write_bytes(v)
    except Exception:
        raise
    return folder


def encode_grid(grid,arm):
    return [dict(arm=arm,winner=k[0],games_p1=k[1],games_p2=k[2],sets_p1=k[3],sets_p2=k[4],mass=format(v,'.17g'))
            for k,v in sorted(grid.items())]


def forecast(request,history,contracts,feedback,output):
    grids,final,preds,ws,nfb,counts,horizon=get_predictions(request,history,contracts,feedback)
    files={"REQUEST.csv":csv_content([request]),"HISTORY.csv":csv_content(history),"CONTRACTS.csv":csv_content(contracts),
           "PREDICTIONS.csv":csv_content(preds),"FEEDBACK_INPUT.csv":csv_content(feedback) if feedback else b"event_id,competition,policy,available_at\n"}
    all_grids={**grids,"HEDGE_MIX":final}
    files["GRIDS.csv"]=csv_content([row for arm in (*ARMS,"HEDGE_MIX") for row in encode_grid(all_grids[arm],arm)])
    receipt=dict(policy=POLICY,qualification="EXPERIMENTAL_NOT_CERTIFIED",event_id=request["event_id"],
                 horizon=horizon.isoformat(),history_count=len(history),player1_count=counts[request["player1"]],
                 player2_count=counts[request["player2"]],feedback_count=nfb,eta=ETA,
                 weights=json.dumps(dict(zip(ARMS,ws)),sort_keys=True),created_at=datetime.now(timezone.utc).isoformat(),
                 code_sha256=sha(Path(__file__).read_bytes()),
                 **{f"sha256_{k}":sha(v) for k,v in files.items()})
    files["RECEIPT.csv"]=csv_content([receipt])
    folder=immutable_write(output,files)
    verify(folder)
    return folder,preds


def read_grids(folder):
    out=defaultdict(dict)
    for r in rows(Path(folder)/"GRIDS.csv"):
        key=tuple(finite_int(r[x],x) for x in ("winner","games_p1","games_p2","sets_p1","sets_p2"))
        mass=float(r["mass"])
        if key in out[r["arm"]] or not math.isfinite(mass) or mass<0:
            raise TennisAdmissionError("duplicate/bad frozen outcome")
        out[r["arm"]][key]=mass
    if set(out)!=set((*ARMS,"HEDGE_MIX")) or any(abs(sum(g.values())-1)>1e-8 for g in out.values()):
        raise TennisAdmissionError("bad frozen expert grids")
    return out


def verify(folder):
    folder=Path(folder)
    receipts=rows(folder/"RECEIPT.csv")
    if len(receipts)!=1 or receipts[0].get("policy")!=POLICY:
        raise TennisAdmissionError("wrong/missing receipt")
    receipt=receipts[0]
    if receipt.get("code_sha256")!=sha(Path(__file__).read_bytes()):
        raise TennisAdmissionError("tennis runtime version differs from issued code; recover issuing commit")
    for k,v in receipt.items():
        if k.startswith("sha256_"):
            file=k[len("sha256_"):]
            if sha((folder/file).read_bytes())!=v:
                raise TennisAdmissionError("bundle hash mismatch: "+file)
    req=rows(folder/"REQUEST.csv");contracts=rows(folder/"CONTRACTS.csv")
    if len(req)!=1 or req[0]["event_id"]!=receipt["event_id"]:
        raise TennisAdmissionError("bundle event identity mismatch")
    g=read_grids(folder)
    # Independently reconstruct the published mixture weights from its retained
    # feedback inventory, not from the cumulative vector written in the receipt.
    hist=rows(folder/"HISTORY.csv")
    _,horizon,count=prepare(req[0],hist)
    try:
        feed=rows(folder/"FEEDBACK_INPUT.csv")
    except Exception as e:
        raise TennisAdmissionError("feedback input cannot be read") from e
    if len(hist)!=int(receipt["history_count"]) or horizon.isoformat()!=receipt["horizon"]:
        raise TennisAdmissionError("training inventory/horizon does not match receipt")
    accum=[0.0]*len(ARMS); admitted_feedback=0
    for row in feed:
        if row.get("competition")!=req[0]["competition"] or row.get("policy")!=POLICY or row.get("event_id")==req[0]["event_id"]:
            raise TennisAdmissionError("feedback ledger wrong scope")
        if stamp(row["available_at"])>horizon:
            continue
        admitted_feedback+=1
        for i,a in enumerate(ARMS):
            x=float(row["loss_"+a])
            if not math.isfinite(x) or not 0<=x<=1:
                raise TennisAdmissionError("feedback ledger has invalid loss")
            accum[i]+=x
    unscaled=[math.exp(-ETA*(v-min(accum))) for v in accum]
    expected_weights={a:v/sum(unscaled) for a,v in zip(ARMS,unscaled)}
    if admitted_feedback!=int(receipt["feedback_count"]):
        raise TennisAdmissionError("feedback count does not match frozen receipt")
    ws=json.loads(receipt["weights"])
    if set(ws)!=set(expected_weights) or any(abs(ws[a]-expected_weights[a])>1e-12 for a in ARMS):
        raise TennisAdmissionError("frozen weights disagree with feedback ledger")
    if set(ws)!=set(ARMS) or any(not isinstance(x,(int,float)) or not math.isfinite(x) or x<0 for x in ws.values()) or abs(sum(ws.values())-1)>1e-9:
        raise TennisAdmissionError("invalid frozen weights")
    expected=mixed({a:g[a] for a in ARMS},[ws[a] for a in ARMS])
    if any(abs(expected.get(k,0)-g["HEDGE_MIX"].get(k,0))>1e-10 for k in set(expected)|set(g["HEDGE_MIX"])):
        raise TennisAdmissionError("frozen mixed outcome not derived from experts")
    preds=rows(folder/"PREDICTIONS.csv")
    if len(contracts)!=len(preds):
        raise TennisAdmissionError("bundle contract/prediction coverage mismatch")
    for c,p in zip(contracts,preds):
        if p["contract_key"]!=c["contract_key"]:
            raise TennisAdmissionError("contract order changed")
        m=price(expected,c)
        for field in ("win","push","loss","p_card"):
            if m[field] is None or abs(float(p[field])-m[field])>1e-9:
                raise TennisAdmissionError("bundle probability mismatch")
        if abs(float(p["baseline_p"])-price(g["COHORT_BASE"],c)["p_card"])>1e-9:
            raise TennisAdmissionError("baseline probability mismatch")
    return receipt


def tennis_score(sets,best_of):
    # Official complete-set scores only. No retirement, walkover or deciding MTB.
    parts=sets.split(",")
    if len(parts)<2 or len(parts)>best_of:
        raise TennisAdmissionError("invalid completed tennis set count")
    s1=s2=g1=g2=0
    for i,part in enumerate(parts):
        try:
            a,b=map(int,part.split("-"))
        except ValueError as e:
            raise TennisAdmissionError("invalid tennis set score") from e
        valid=((a==6 and 0<=b<=4) or (a==7 and b in (5,6)) or
               (b==6 and 0<=a<=4) or (b==7 and a in (5,6)))
        if not valid or s1==best_of//2+1 or s2==best_of//2+1:
            raise TennisAdmissionError("invalid/extra tennis set")
        s1+=a>b;s2+=b>a;g1+=a;g2+=b
    if max(s1,s2)!=best_of//2+1 or len(parts)!=s1+s2:
        raise TennisAdmissionError("incomplete completed match")
    return (1 if s1>s2 else 2,g1,g2,s1,s2)


def settle(folder,sets,final_at,available_at,source_url,evidence_path,evidence_sha256,out):
    receipt=verify(folder)
    r=rows(Path(folder)/"REQUEST.csv")[0]
    outcome=tennis_score(sets,int(r["best_of"]))
    if not (stamp(r["scheduled_start"])<=stamp(final_at)<=stamp(available_at)):
        raise TennisAdmissionError("invalid tennis settlement timing")
    source_valid(dict(source_url=source_url,evidence_path=evidence_path,evidence_sha256=evidence_sha256))
    g=read_grids(folder)
    answer=outcome[0]
    feedback=dict(event_id=r["event_id"],competition=r["competition"],policy=POLICY,
                  final_at=stamp(final_at).isoformat(),available_at=stamp(available_at).isoformat(),
                  official_sets=sets,winner=r["player1"] if answer==1 else r["player2"],
                  source_url=source_url,evidence_path=evidence_path,evidence_sha256=evidence_sha256,
                  bundle_path=str(Path(folder).resolve()),
                  original_receipt_sha256=sha((Path(folder)/"RECEIPT.csv").read_bytes()))
    for arm in ARMS:
        p=sum(m for k,m in g[arm].items() if k[0]==1)
        feedback["loss_"+arm]=format((p-(1 if answer==1 else 0))**2,'.17g')
    path=Path(out)
    with path.open("xb") as f:
        f.write(csv_content([feedback]))
    return path,feedback


def main(argv=None):
    p=argparse.ArgumentParser(description=__doc__)
    sub=p.add_subparsers(dest="cmd",required=True)
    pr=sub.add_parser("predict")
    for x in ("request","history","contracts","out"):
        pr.add_argument("--"+x,required=True)
    pr.add_argument("--feedback")
    ve=sub.add_parser("verify");ve.add_argument("--bundle",required=True)
    se=sub.add_parser("settle")
    for x in ("bundle","sets","final-at","available-at","source-url","evidence-path","evidence-sha256","out"):
        se.add_argument("--"+x,required=True)
    a=p.parse_args(argv)
    if a.cmd=="predict":
        req=rows(a.request)
        if len(req)!=1:
            raise TennisAdmissionError("exactly one request")
        folder,preds=forecast(req[0],rows(a.history),rows(a.contracts),rows(a.feedback) if a.feedback else [],a.out)
        print(f"{folder}: {len(preds)} EXPERIMENTAL tennis probabilities (not certified)")
    elif a.cmd=="verify":
        print(verify(a.bundle))
    else:
        print(settle(a.bundle,a.sets,a.final_at,a.available_at,a.source_url,a.evidence_path,a.evidence_sha256,a.out)[0])


if __name__=="__main__":
    main()
