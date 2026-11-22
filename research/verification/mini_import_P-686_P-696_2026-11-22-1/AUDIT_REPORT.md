# Audit · mini 20261118DA6D9F6251746B979F5895FA · 11 cards (10 sealed, 1 unsealed) + 2 non-card requests · P-686 to P-696

Written for the owner and prompt 6. Framework: MDS-2026.11.18-v29.1, ONE-CHAT-v3, AUDIT-v1, TIMING-v3, SRC-ALT-v3, DEEPLOSS-v1, FREEZE-v1.

## 1. Inventory & custody

- **Source branches:** `origin/forecast-seals` (12 registered requests `G0001`–`G0003`, `G0005`–`G0013`; 10 sealed cards `G0002`, `G0003`, `G0005`, `G0006`, `G0008`–`G0013`) and `origin/card-drops` (`G0001` unsealed card + `G0004` unregistered draft request).
- **Canonical assignment:** 11 distinct events assigned **P-686 to P-696** in scheduled-start UTC order (ties broken by card key order). `G0004` (draft `ML` request replaced by `G0005` for `AHL:1029340`) and `G0007` (`NBA:0022600258`, registered request with no card dropped) consumed zero canonical IDs.
- **Unsealed card defect (`G0001` / P-686):** refused by `DROP-SEAL-v1` because 4 FACTS rows (`HOME/AWAY travel_km`, `HOME/AWAY adjustment_basis`) omitted source URLs.
- **Duplicate side line (`G0005` / P-689):** AHL request included both `Americans -0.5` (`L1`) and `Crunch -0.5` (`L2`) under `INCLUDE_OT_SO`; since AHL games cannot tie after OT/SO, `L1` and `L2` are identical 2-way contracts (`p=0.5822 / 0.4178`), giving the side 2/3 weight in card-mean Brier.

## 2. Timing & Track P (`ONE-CHAT-v3`) eligibility

- **1 game verified pre-start (`SEALED_PRE_START_SERVER`):** `P-689` (`G0005`, AHL `1029340`) — official HockeyTech JSON verifies puck drop `7:05 pm EST` (`00:05:00Z`), 7m20s after GitHub's server seal (`23:57:40Z`).
- **4 sealed cards before scheduled start, first play unverified:** `G0002` (-9s), `G0008` (-4m52s), `G0010` (-17s), `G0013` (-2m57s). Under `EVALUATION_PLAN_v29.0.md`, scheduled start is never silently substituted for official first play (`FIRST_PLAY_UNVERIFIED` until official tip/first-ball captures exist).
- **5 sealed cards after scheduled start:** `G0003` (+22s), `G0006` (+6m05s), `G0009` (+6m10s), `G0011` (+14m19s; request arrived +5m after schedule), `G0012` (+8m16s; card self-labelled `POST_SCHEDULED_START`).

## 3. Source access (`SRC-ALT-v3`) & market firewall

- **Settlement sources (`SOURCE_ACCESS_AUDIT.csv`):** 100% of captured box-score files came from `ALLOWED` or `NO_RULES_FILE` hosts (`foxsports.com`, `bleague.jp`, `lscluster.hockeytech.com`, `samfordsports.com`, `nblfixtures.com`, `sportsguff.com`, plus official `utsports.com`, `upstatespartans.com`, `nbl.com.au`, `cricket.com.au`). Blocked/unknown hosts (`cdn.nba.com`, `site.api.espn.com`, `www.espn.com`) were strictly skipped.
- **Cited URLs in the 11 cards (`CITED_URL_ACCESS_AUDIT_CHATGPT.csv`):** 73 distinct URLs audited for `CHATGPT_BROWSING`: {'ALLOWED': 54, 'RULES_UNKNOWN': 1, 'BLOCKED': 18}. 19 cited URLs (26.0%) were `BLOCKED` or `RULES_UNKNOWN` for `ChatGPT-User`.
- **Market firewall:** Clean across all 11 cards (`0` market/odds pricing violations in `ONECHAT_V1` blocks).

## 4. Results & honest findings

- **All 11 cards (46 rows):** 23 WIN, 23 LOSS, **0 UNRESOLVED**. Rank 1: **8W / 3L (72.7%)**. Rank 2: **5W / 6L (45.5%)**.
- **Card-mean Brier vs 0.25:** All 11 cards = **0.2422** (`d = +0.0078`); 10 sealed cards = **0.2449** (`d = +0.0051`).
- **Finding 1 — `UNMEASURED` availability priced on 46/46 rows:** Every single row carried `availability_basis=UNMEASURED` and 0 lines were left `UNPRICED`. Most costly example: `P-690` (Pacers +8.5 at `0.6042` without Haliburton/Nembhard, lost by 15).
- **Finding 2 — Plus-handicap opponent-strength overreach repeated:** `P-693` (USC Upstate +8.5 at `0.7354`, actual loss by 10, Brier `0.5408`, card `d = -0.1685`) repeated the exact `PLUS_HANDICAP_WITHOUT_OPPONENT_CHECK` failure class from `P-660` and `P-685` (now at **3 reviews** in `DEEP_LOSS_REGISTER.csv`, crossing the pattern threshold for prompt 8 after `FREEZE-v1`).
- **Finding 3 — Persistent Over-bias on totals (`3W / 6L` on Over leans):** Cards leaned Over on 9 of 10 full-game totals and lost 6 of them (`P-687`, `P-688`, `P-689`, `P-690`, `P-693`, `P-694`), including a double-B2B NBA game (`P-694`, total 206 vs 229.5).
- **Finding 4 — What worked:** Underdog spreads went **6W / 2L** (winning P-686, P-688, P-691, P-692, P-694, P-695) and WBBL 6-over Under 42.5 won comfortably (32/1). Sample size (`n=11`) is tiny; **no predictive advantage is established**.
