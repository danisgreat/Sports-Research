# Comprehensive retrospective — P-001 through P-060

Audit date: **2026-08-22**
Historical audit method: **MDS-2026.08.22-v1.1**
Current controlling method: **MDS-2026.08.22-v2**; the v2 prospective data roles and evaluation controls supersede the original v1.1 labels in this historical report.
Scope: **all 60 canonical IDs; 59 forecast events; P-021 closed without a forecast**

## 1. Answer first

The log supports a strong audit and research process, but it does **not** support a claim that the current algorithm is calibrated, profitable, or best in market.

The decisive limitation is structural: approximately 60 user-selected events are split across sports, competitions, market families, pregame/live states, and changing record conventions. Several events contain multiple dependent views and four correlated contracts. Probabilities and prices were not consistently issued. The record can train the **process, representation, causal checklist, and historical-case retrieval system**, but fitting outcome weights or a calibration curve to it would overfit the same mistakes the retrospective is trying to correct.

The best improvement is therefore not a more complicated cross-sport formula. It is a versioned champion–challenger system:

1. one common identity/data/validation process;
2. separate sport-specific rate × exposure models;
3. one joint event distribution per game;
4. chronological out-of-sample evaluation against simple and market baselines;
5. proper scoring for genuinely issued probabilities;
6. prospective lesson testing instead of rewriting weights after each result.

These changes are implemented in MODEL_AND_DATA_SPEC.md, ALGORITHM_PORTFOLIO_AND_EVALUATION.md, RULES_GENERAL.md, the sport files, and LEARNING_REGISTER.md.

All P-001–P-060 are therefore frozen as **Historical Development Set D0**. Under v2, P-061 onward begins **E1-Q**, the prospective qualitative process/rank cohort; a distinct **E1-P** probability cohort begins only when a real frozen model generates pre-result shadow outputs.

## 2. Coverage and ledger reconciliation

| Item | Audited result | Interpretation |
|---|---:|---|
| Canonical IDs | 60 | P-001 through P-060 all exist |
| Forecast events | 59 | P-021 was final before delivery and correctly excluded |
| Settled forecast events | 59/59 | No final awaits settlement |
| Final unsettleable rows | 1 | P-003 corners only; the event remains closed |
| Historical P-001–P-034 formal rows | 59-30-1 | Arithmetically reproducible but mixed and non-normalised |
| P-035–P-060 primary formal | 39-14 | Dependence-normalised descriptive decisions |
| P-035–P-060 controlling raw rows | **61-46** | Corrected from the erroneous 63-44 |
| P-035–P-060 higher-ranked exact pairs | 24/36 | Pair-ordering diagnostic only |
| P-035–P-060 potential winners | 19-7 | Contains winner annotations/contracts under historical conventions |
| Proper-score-eligible historical probabilities | 0 | No probabilities were consistently issued |
| Profit/ROI/edge-eligible record | 0 | No consistent prices, stakes, or market universe |

Do not combine the P-001–P-034 and P-035–P-060 ledgers into one accuracy percentage: their verdict, view, eligibility, and dependence conventions differ.

### Raw-ledger correction

The arithmetic error begins after P-039:

- P-035 and P-036 together are 5-5;
- P-037 adds 2-2;
- P-039 adds 2-2;
- therefore the correct total through P-039 is 9-9, not 11-7.

The +2 wins / −2 losses error then propagated through later snapshots.

| Through event | Correct controlling raw result |
|---|---:|
| P-037 | 7-7 |
| P-039 | 9-9 |
| P-040 | 11-12 |
| P-043 | 19-16 |
| P-044 | 21-18 |
| P-045 | 23-20 |
| P-047 | 33-22 |
| P-048 | 35-24 |
| P-049 | 37-26 |
| P-051 | 40-29 |
| P-057 | 54-41 |
| P-058 | 56-43 |
| P-059 | 58-45 |
| P-060 | **61-46** |

P-057 was imported after the final and has no independently recoverable pre-result issue timestamp. It remains part of historical controlling bookkeeping but belongs in a **late-import** cohort and must be excluded from strictly prospective evaluation. Excluding P-057, the prospective-style post-audit descriptive cohort is raw 58-43, exact pairs 23/33, and winners 18-7; primary formal remains 39-14 because P-057 had no primary rows.

## 3. Data-quality and governance defects

| Defect | Evidence | Correction |
|---|---|---|
| Raw tally error | 11-7 stated through P-039 instead of 9-9 | Top snapshot corrected to 61-46; this audit supplies the corrected progression |
| Mixed denominator | Events, views, winner annotations, exact pairs, nested rows and live states shared headline counts | Event, view, contract, phase, provenance and dependence are now separate fields |
| P-057 provenance | Imported after final; no independently recoverable issue timestamp | Keep as late-import evidence; exclude from prospective scoring |
| P-060 duplicate storage | A full second P-059-labelled attachment was embedded inside P-060/V03 | Remove redundant body; retain canonical mapping, ranks, source path and diagnostic settlement |
| Winner duplication | Potential winner could duplicate an existing winner contract | Winner now aliases the canonical contract ID when terms match |
| Integer pair rule | Active rule said exactly one side always wins | Corrected: both sides can push at an integer boundary |
| Eligibility/verdict mixing | FORCED_RANK and AVOID appeared as both verdict and eligibility; P-040 labelled AVOID rows primary then excluded them | Orthogonal verdict, evidence, performance-role and actionability fields |
| Boundary treatment | Close outcomes were described as weak calibration observations | Retain BOUNDARY_SENSITIVE metadata but include fully in proper scores |
| Single-loss strikes | One top loss automatically implied confidence punishment/calibration error | Audit the process; lock only for demonstrated defect or predefined aggregate failure |
| Arbitrary nested windows | Mandatory L5/L10/L15/L20 and H2H5/10/15 repeated and elevated stale data | Store rows once; use adaptive, time-decayed, opponent/regime-adjusted features |
| Distributed tests/strikes | Registries were scattered and internally stale | LEARNING_REGISTER.md is now the sole current registry; strike policy retired |
| Non-monotonic append order | Event grouping and timestamps do not produce literal chronological order | Future schema includes method/view time and should add append sequence when available |
| P-037 table shape | Ranking header and delimiter had different cell counts | Administrative table delimiter corrected |
| Hardcoded source access | Rules claimed specific services were always blocked/available | Probe each session and record access time/status |
| Rule-file case duplication | Long dated game narratives repeated the log | Active sport files now contain operative controls only |

Historical factual corrections already in the log remain controlling:

- P-006 threshold evidence was initially sign-classified incorrectly;
- P-017 identity was corrected before the controlling forecast;
- P-020's claimed 30-ball Hundred powerplay was wrong; official 2026 conditions make the first five five-ball overs 25 legal balls, and grades did not change;
- P-003 corners remain UNSETTLEABLE after the documented official-source retry;
- P-033's total of exactly eight is a PUSH on Over 8.0.

## 4. What repeatedly worked

| Mechanism | Representative IDs | Durable interpretation |
|---|---|---|
| Exact contract and boundary mapping | P-020, P-024, P-028, P-033, P-046, P-060 | Settlement geometry prevents false complements, missed pushes, and duplicate claims |
| Live remaining-exposure re-anchoring | P-019, P-024, P-040 later views, P-050 | Current resources and remaining opportunities outperform elapsed-rate extrapolation |
| Named participant and role chains | P-005, P-016, P-033, P-036, P-043, P-049 | Expected exposure and replacement sequence are more useful than generic team labels |
| Contest-adjusted baseline | P-001, P-016, P-038, P-044, P-049 | Venue/competition level plus current participants is a better starting point than raw streaks |
| Contract overlap disclosure | P-033, P-054, P-060 | Several supplied rows can win without providing independent confirmation |
| Independent phase modelling when applied | P-024, P-035 primary, P-050 | A future phase needs its own possession/resource assumptions |
| Winner separated from a total | P-022, P-041, P-045, P-060 | A total thesis cannot stand in for side or margin distribution |

These are process successes, not evidence that their numerical weight has been validated.

## 5. Recurring failure mechanisms

### Cross-sport

1. **A named kill path was disclosed but not weighted.** The card often knew the adverse branch but still used the central narrative as if disclosure solved the problem.
2. **One thesis appeared in several rows.** Phase and full totals, winner and handicap, or overlapping lines inflated the apparent confirmation.
3. **Outcome statistics replaced process.** Raw Unders, covers, H2H results, or old score averages were allowed to outweigh current exposure and quality.
4. **Proxy variables replaced the market event.** Shots or possession became corners; hitouts became points; a short starter became an Over.
5. **Different event phases were treated as exchangeable.** Q1 became H1/full game; cricket powerplay became full innings; a leading side's early attack became full-match pressure.
6. **A single outcome triggered too much rule change.** This risks overfitting random realisation and contradicts prospective validation.

### Baseball

Recent ERA or Under runs repeatedly outweighed starter HR/contact shape, expected length, and the actual bulk/middle/late relief chain: P-002, P-034, P-036, P-052, P-053, P-055, P-056, and P-059. A short start increases relief exposure but is not itself an Over signal. Low total also failed as a proxy for close margin in P-011, P-034, P-054, and P-060.

### Cricket

Opening phase, middle overs, and full innings were repeatedly treated as transferable in P-007, P-019, P-030, P-032, P-037, P-042, and P-050. The fix is phase-specific run/wicket rates, attack-mapped collapse floors, confirmed-batter resource state, and a separate finisher/death ceiling. Winner calls also need an independent chase/defendability model.

### AFL/AFLW

Old Under/H2H rates and raw clearance/hitout edges lost to current inside-50, marks-inside-50, scoring-shot, venue, and remaining-possession mechanisms in P-025, P-027, P-040, P-048, and P-058. Winner and handicap thresholds also diverged; the full margin distribution must control.

### Soccer

Shots, xG, possession, and territorial dominance were repeatedly used as corner proxies without modelling crosses, blocks, end-line entries, score state, or substitution phase: P-023, P-031, P-047, and related corner cards. Goals and corners require separate rate processes.

### Basketball

Q1, H1, and full-game totals were often several expressions of one pace thesis: P-009, P-024, P-035, and P-057. Q2 needs its own rotation, foul, possession, and shot-quality forecast. A two-game H2H acceleration pattern cannot control the next phase.

### Rugby league/NRL and American football

P-039 is the only NRL event; its named-spine, line-break and set-distance evidence was more useful than historical cover rates, but n=1 cannot calibrate the sport. No current-log American-football forecast exists. The active files therefore contain mechanistic controls and explicit no-calibration boundaries, not performance claims.

## 6. One-row audit of every canonical ID

| ID | Official event result | Main audit outcome | Principal cause class |
|---|---|---|---|
| P-001 | Welsh Fire W 129/3; Trent Rockets W 132/2 | Winner hit; promoted Overs failed | Rate/process; dependence |
| P-002 | Miami 8, Philadelphia 6 | Miami +1.5 hit for another mechanism; Under and PHI winner failed | Starter HR/contact tail; availability versus performance |
| P-003 | Copenhagen 2-1 Polissya | Goal/player rows and winner hit; corners unsettleable | Source/settlement; red-card tail |
| P-004 | MI London 164/5; London Spirit 165/3 | Phase Under/full Under hit; Over and winner missed | Opener role; threshold calibration |
| P-005 | Tampa Bay 3, Texas 2 | Side/winner hit; Over 8 lost | Bulk/relief-chain model |
| P-006 | Southern Brave 128, Birmingham 116 | Innings Under hit; phase Under and winner missed | Data transformation; defendability |
| P-007 | Manchester Super Giants 137/3; Trent 140/4 | Phase Over/winner hit; full Over lost | Phase leakage |
| P-008 | Yankees 2, Cubs 0 | Yankees cushion and Under hit; Cubs winner lost | Recent-start overfit; starter distribution |
| P-009 | Indiana 112, Portland 98 | Winner hit; three correlated Unders lost | Dependence stacking; pace |
| P-010 | Carlton 154, Brisbane 78 | Carlton cushion hit; Brisbane winner/total thesis failed | Conversion sign; winner/handicap mismatch |
| P-011 | Cleveland 5, Arizona 0 | Cleveland winner hit; top Arizona cushion lost | Raw cover rate versus separation branch |
| P-012 | Southern Brave W 121/5; Welsh Fire 122/6 | No formal forecast; Under/watch-side direction right | Historical abstention |
| P-013 | Southern Brave M 115/8; Welsh Fire 116/4 | No formal forecast; Under direction right, phase Over wrong | New-ball/wicket state |
| P-014 | Arizona 5, San Diego 1 | Historical abstention directions and winner correct | Role-chain read |
| P-015 | Sri Lanka W 113/6; Pakistan 115/6 | Both Unders hit; Sri Lanka winner failed | Low-target defendability |
| P-016 | Lotte 3, Kiwoom 2 | All contracts and winner hit; score centre high | Corridor coherence; calibration caution |
| P-017 | London Spirit W 136/7; Sunrisers 142/5 | Full corridor/original winner hit; phase Under/live winner missed | Identity correction; opener/wicket state |
| P-018 | Sunrisers M 241/2; Spirit 204/6 | Phase band/winners hit; full Under failed badly | Source limits; ceiling miss |
| P-019 | Manchester Super Giants W 85/9; Welsh Fire 88/7 | Original Overs/winner failed; live Under/new winner hit | Wicket-cluster tail |
| P-020 | Birmingham 122/7; Trent 124/4 | Four rows and winner hit | Exact state; later rules-source correction |
| P-021 | Baltimore 5, Angels 2 | No forecast; correctly excluded | Administrative closure |
| P-022 | Angels 4, Baltimore 1 | Under/cushion hit; Baltimore winner failed | Direct starter evidence underweighted |
| P-023 | Benfica 6, Hearts 1; eight corners | Goals/side/winner hit; corners lost by one | Corner-event model; boundary |
| P-024 | Portland 97, Toronto 83; Q1 48, H1 88 | Actionable rows 3-1; full Over missed by two | Nested dependence; live re-anchor |
| P-025 | Brisbane 125, Hawthorn 58 | Three of four; Under and Hawthorn winner wrong | Clearance/hitout not converted to shots |
| P-026 | Birmingham 107/9; Sunrisers 111/1 | Three of four plus winner; lower band too high | Early-wicket/collapse floor |
| P-027 | Melbourne 113, Fremantle 109 | Cushion/Over hit; top Under and winner failed | Stale Under rates versus live scoring shots |
| P-028 | Collingwood 117, West Coast 98 | All rows/winner hit; top row by 0.5 | Good live state; boundary |
| P-029 | Carlton 106, St Kilda 62 | Three of four plus winner; cushion ordering wrong | Winner/margin alignment |
| P-030 | Welsh Fire 121/8; Sunrisers 122/4 | Three of four plus winner; lower Over missed by 0.5 | Sample weighting; boundary |
| P-031 | Manchester City 3, Atlético 1; City three corners | Three of four plus winner; corner Over failed | Possession/shots not corners |
| P-032 | London Spirit W 140/4; Birmingham 108/8 | Two-two plus winner; upper Under lost late | Finisher/death ceiling |
| P-033 | Washington 7, Cincinnati 1 | Two wins, one loss, one push plus winner; wrong total ranked first | Fresh role chain underweighted |
| P-034 | Minnesota 9, Baltimore 5 | Two-two; top pick and winner failed | Post-trade starter/length; bullpen exposure |
| P-035 | Atlanta 104, Connecticut 69; Q1 45, H1 83 | Raw 3-3, primary 1-0, winner hit | Q2 regression; nested phases |
| P-036 | Philadelphia 7, Minnesota 1 | Raw 2-2, primary 1-0, winner hit | Pitch-shape/lineup cluster; starter length |
| P-037 | Jamaica 117; Guyana 118/4; phase 26 | Unders/winner hit; central band too high | Collapse-floor calibration |
| P-038 | Bangladesh 426 and 57/1 beat Australia 198 and 284 | Three-one, primary/winner hit; milestone fragile | Player-threshold boundary |
| P-039 | Dolphins 22, Manly 0 | Two-two, primary 1-1; Under/winner right | Spine/territory versus stale covers |
| P-040 | Fremantle 112, Adelaide 88 | Raw 2-3, primary 1-1, winner failed | Remaining-shot chain; boundary; schema |
| P-041 | Wolves 2, Blackburn 2; ten corners | Formal 4-0; Wolves winner failed | Draw branch underweighted |
| P-042 | Manchester Super Giants 186/4, Sunrisers 166/7; phase 30 | Two-two, primary 1-1, winner failed | Direct ceiling/death hitting underweighted |
| P-043 | Cubs 3, Cardinals 0 | Two-two, primary 1-1; side/winner right | Short start did not create scoring |
| P-044 | Richmond 46, Collingwood 28 | Two-two, primary 2-0, winner hit | Territory mechanism transferred |
| P-045 | Hawthorn 92, Collingwood 92 | Two-two, primary 2-0; outright winner lost | Draw branch |
| P-046 | Chelsea 3, Real Sociedad 1; corners 4-2 | Four-zero plus winner; two margins only 0.5 | Boundary success, not calibration proof |
| P-047 | Bayern 3, Leipzig 1; corners 2-1 | Three-one plus winner; corner pick lost | Friendly heat/rotation/substitutions |
| P-048 | Sydney 112, Essendon 76 | Two-two, primary 1-1; winner hit, top Under lost | Two-team scoring/shot balance |
| P-049 | KIA 2, Doosan 1 | Two-two, primary 2-0, winner hit | Suppression right; score corridor high |
| P-050 | Sunrisers 91, Trent 92/2 | Raw 1-1, primary/winner hit | Live Under right; collapse floor high |
| P-051 | Barcelona 5, Basel 2; eight corners | Two-two, primary 2-2, winner hit | Substitution-phase defence; dependence |
| P-052 | Kansas City 9, Athletics 5 | Two-two, primary 2-0, winner hit | Favoured starter HR tail |
| P-053 | DeNA 4, Yomiuri 3 | Two-two, primary 1-1, winner failed | H2H/season versus direct starter/late chain |
| P-054 | Lotte 5, Kiwoom 4 | Three-one, primary 2-0, winner hit | One-run overlap misranked |
| P-055 | Pittsburgh 4, Detroit 3 | Two-two, primary 1-1; cushion/winner right | Short start did not imply Over |
| P-056 | Arizona 7, Boston 6 in ten | Two-two, primary 1-1, winner failed | HR/contact and extra-inning tail |
| P-057 | Minnesota 77, Golden State 66; Q1 34, H1 67 | Three-three, winner hit; no primary rows | Unsupported Q2 acceleration; late import |
| P-058 | Gold Coast 103, St Kilda 80 | Two-two, primary 0-2, winner failed | Marks-I50/ruck-clearance conversion; venue |
| P-059 | St Louis 10, Cincinnati 9 | Two-two, primary 1-1, winner hit | Under streak versus HR/relief mechanisms |
| P-060 | Yankees 6, Baltimore 1 | Three-one, primary 2-0, winner hit | Low total incorrectly linked to close margin |

## 7. Revised data and modelling priorities

| Rank | What matters more | What now matters less |
|---:|---|---|
| 1 | Correct event, contract, rules, state, and information cutoff | Any result trend before identity is frozen |
| 2 | Confirmed participants, role, and expected exposure | Team reputation and active/inactive binaries |
| 3 | Opponent-adjusted process quality | Raw points/runs/goals and W/L |
| 4 | Joint score/resource distribution and explicit tails | Separate narratives for each supplied row |
| 5 | Venue, environment, workload, rest through a mechanism | Generic weather or fatigue labels |
| 6 | Time-decayed comparable history with regime breaks | Arbitrary old H2H and nested window repetition |
| 7 | Same-time market benchmark when price exists | Closing line used as hindsight input |
| 8 | Prospective ablation/score comparison | Counting which narrative appeared in winners |
| 9 | Event-level uncertainty and dependence | Contract-row hit rate as independent accuracy |
| 10 | Scheduled model review | Rule changes after one ordinary outcome |

Source authority remains separate from predictive rank. An official coach quote can be perfectly sourced and still be low-value.

## 8. New evaluation standard

The old record answers only: “How did these recorded qualitative contracts settle under changing conventions?” It does not answer whether a probability model was calibrated or beat a market.

Future quantitative models must:

- use rolling-origin evaluation so all training/tuning data precedes each forecast;
- keep pregame and live horizon families separate;
- log the eligible event universe and one controlling view per event;
- compare with league/home, simple rate × exposure, frozen previous-version, and same-time de-vigged market baselines where available;
- evaluate binary probabilities with Brier/log loss, win-push-loss with multiclass proper scores, and distributions with CRPS/interval coverage;
- report calibration and sharpness together with uncertainty;
- retain boundary-sensitive cases in the score;
- avoid significance or superiority claims until the independent event sequence is adequate.

Proper scoring rewards honest probability distributions rather than result-only confidence. Rolling-origin validation prevents future leakage. Hierarchical partial pooling limits the damage from sparse teams, players, venues, and market slices. These choices follow [Gneiting and Raftery](https://sites.stat.washington.edu/people/raftery/Research/PDF/Gneiting2007jasa.pdf), [calibration and sharpness research](https://doi.org/10.1111/j.1467-9868.2007.00587.x), [rolling-origin forecast evaluation](https://otexts.com/fpp3/tscv.html), and [multilevel modelling](https://sites.stat.columbia.edu/gelman/surveys.course/Gelman2006.pdf).

## 9. Method changes implemented

| File | Material change |
|---|---|
| README.md | Removed stale queue/performance text; made Markdown-only rule and current reading map explicit |
| AGENT_ROLE_AND_TASK.md | Clarified rank objective; separated winner/verdict fields; replaced automatic outcome strike with process audit |
| RULES_GENERAL.md | Consolidated state/live/source/ranking/settlement rules; corrected integer pairs, aliases, boundaries, recency and change governance |
| MODEL_AND_DATA_SPEC.md | Added the ten-stage algorithm, data hierarchy, provenance, joint-distribution architecture, validation, metrics, and canonical schemas |
| LEARNING_REGISTER.md | Centralised promoted controls, current prospective tests, and superseded rules |
| Sport files | Removed repeated general boilerplate and case narratives; added sport-specific exposure/rate/tail controls |
| AUDIT_AND_CHANGES_2026-08-03.md | Condensed redundant non-normative prose to a historical pointer |
| PREDICTION_LOG.md | Corrected top raw tally, removed redundant imported body, fixed P-037 table delimiter, and appended schema/provenance correction |

No historical probability, price, or feature was invented. No result was regraded to improve the record.

## 10. Research foundation and next standard

The new process uses:

- [Strictly Proper Scoring Rules — Gneiting and Raftery](https://sites.stat.washington.edu/people/raftery/Research/PDF/Gneiting2007jasa.pdf)
- [Calibration and Sharpness — Gneiting, Balabdaoui and Raftery](https://doi.org/10.1111/j.1467-9868.2007.00587.x)
- [Rolling-origin cross-validation](https://otexts.com/fpp3/tscv.html)
- [Preregistration and prospective separation — Nosek et al.](https://doi.org/10.1073/pnas.1708274114)
- [Hierarchical partial pooling — Gelman](https://sites.stat.columbia.edu/gelman/surveys.course/Gelman2006.pdf)
- [Predictive stacking — Yao et al.](https://doi.org/10.1214/17-BA1091)
- [Model Cards](https://doi.org/10.1145/3287560.3287596), [Datasheets for Datasets](https://doi.org/10.1145/3458723), and [W3C PROV-O](https://www.w3.org/TR/prov-o/) for versioned limitations and provenance

The next credible milestone is not a larger historical hit-rate table. It is the first closed chronological evaluation block in a homogeneous sport × competition × market × state family, with forecast-time probabilities or distributions, baseline scores, dependence-safe event units, and no retrospective feature construction.

## 11. Development-set activation addendum

D0 now trains the algorithm in four concrete ways:

| Training layer | D0 signal | Algorithm change |
|---|---|---|
| Representation | Every event exposed identity, state, exposure, rate, context, dependence, settlement, or provenance fields | Canonical card stores those dimensions separately instead of mixing them in narrative |
| Mechanism | The one-row-per-ID matrix records what actually drove each outcome and whether it was knowable | New forecasts must model causal rate × exposure chains and explicit ordinary tails |
| Retrieval | Prior cases supply comparable failure modes across sport, market, state, and phase | Run the predeclared query, retrieve up to five genuinely eligible cases, permit zero as `NO COMPARABLE CASE`, and log all eligibility and comparison details |
| Governance | Wins, losses, pushes, unsettleable rows, late imports, and wrong-mechanism wins expose different process risks | Outcome and process grades remain separate; only prospective scoring can promote forecast weights |

No result is discarded because it won, lost, pushed, arrived late, or could not settle. Its **role** changes instead: P-021 trains state control, the P-003 corner row trains settlement provenance, and P-057 trains retrospective mechanism checks but never prospective performance. This preserves all prior learning without letting hindsight masquerade as prediction-time data.
