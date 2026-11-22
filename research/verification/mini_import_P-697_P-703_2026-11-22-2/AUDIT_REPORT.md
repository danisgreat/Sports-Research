# Audit · mini 20261120-495CEEB69E9540938CF6A7DAA7B546B4 · 7 cards (3 sealed, 4 refused) · P-697 to P-703

Written for the owner and prompt 6. Framework of the cards: MDS-2026.11.18-v29.1, ONE-CHAT-v3. Audited under AUDIT-v1, TIMING-v3, SRC-ALT-v3, DEEPLOSS-v1 and FREEZE-v1 at v29.2.

## 1. Inventory and custody

- **Source branches:** `origin/forecast-seals` (7 registered requests; 3 sealed cards: G0001, G0003, G0007) and `origin/card-drops` (4 refused card drops: G0002, G0004, G0005, G0006). Pulled byte-exact; [FROZEN_MANIFEST.csv](../../../archive/settled_minis_2026-11-22/20261120-495CEEB69E9540938CF6A7DAA7B546B4/FROZEN_MANIFEST.csv).
- **Canonical assignment:** 7 events, **P-697 to P-703**, in scheduled-start UTC order. No key was left without an ID.
- **Four of seven cards could not be sealed.** Two of the refusals were deadlocks that registration should have caught: G0004 was registered with one side per label, and G0006 with "+4.5" and "−3.5" under one label. G0005 used a non-page source in FACTS, and G0002 had no not-started page. v29.2 now refuses the first two at registration, and check drops catch the format errors before sealing.
- **Contract defect:** P-700's L1 and L2 are one winner contract (OT/SO, no draw) registered twice, as with P-689 in the previous mini. P-702's L1 holds two different contracts, so its two rows are not complementary (they sum to 1.109). Both are settled literally and flagged in every table.

## 2. Timing and Track P (ONE-CHAT-v3)

- **No game qualifies yet.** None of the three sealed cards has a verified first play.
  - G0003 (P-699) was sealed 89 s before its scheduled tip. It qualifies once a permitted page gives a later tip-off; nba.com is refused under the script rule.
  - G0001 (P-697) was sealed 5m24s and G0007 (P-703) 2m42s after their scheduled starts. They count only if play began later. The WBBL scorecard's "1:55 PM" start, in an unstated time zone, hints at a delay but is not evidence.
- **Late requests were the norm.** All seven requests were registered within ten minutes of the scheduled start, and G0004's six minutes after it. G0006 was researched in 81 seconds. From v29.2, a late request counts whenever the not-started page and the seal both precede the real first play. The cards here had their not-started evidence from preview or upcoming pages, which do not prove play had not begun.

## 3. Source access (SRC-ALT-v3) and market firewall

- **Settlement sources:** every capture came from an `ALLOWED` or `NO_RULES_FILE` host through `ml.source_access` ([SOURCE_ACCESS_AUDIT.csv](SOURCE_ACCESS_AUDIT.csv)). Refused hosts (nba.com, api.foxsports.com, api-web.nhle.com, AP, Yahoo, ESPN AU, Sporting News, ABC, cricbuzz) and unknown-rules hosts (thecfa.cn, sofascore, besoccer, dongqiudi, espncricinfo, wbbl.com.au) were not opened.
- **URLs cited by the cards** ([CITED_URL_ACCESS_AUDIT_CHATGPT.csv](CITED_URL_ACCESS_AUDIT_CHATGPT.csv)): 51 distinct, for the ChatGPT reader 43 `ALLOWED`, 3 `NO_RULES_FILE`, **3 `BLOCKED`** and 2 `RULES_UNKNOWN`.
  - Blocked: G0003 cited two nba.com pages (fixture and the Pacers' preview), and G0007 cited a Reddit match thread for the toss.
  - Unknown rules: G0002 cited thecfa.cn and weather.com.cn.
  - The Reddit thread is also a live-match venue, an outcome-exposure risk; the card recorded no outcome seen.
- **Market firewall:** no price, odds or tip in any ONECHAT_V1 block. The G0003 card says the TeamRankings betting sections were not used; shaiba.kz betting widgets were not read at settlement.

## 4. Results and findings

- **30 rows:** 15 WIN, 15 LOSS, **0 UNRESOLVED**. Rank 1 **3W / 4L**; Rank 2 **2W / 5L**. Mean card Brier 0.2498 (`d = +0.0002`); the three sealed cards 0.2868 (`d = −0.0368`). Seven games prove nothing either way.
- **Finding 1, rank on no-direction numbers.** Five of the seven rank-1 rows had p within 0.08 of 0.5, and the cards themselves refused to rank them against their 62%/58% gates. The registered ranker ranks them anyway; four of those five lost. This is what SELECT-SHADOW-v1 now tests.
- **Finding 2, unmeasured availability priced everywhere.** Six of the seven cards priced every row with `UNMEASURED` availability (G0006 used a non-vocabulary basis). G0005 also moved its numbers by an unmeasured −3 for Davis: the total missed by 31 points, and the side won by 15.5.
- **Finding 3, basketball totals without a pace model.** P-701 (raw points, total 219 against a centre of 187.9) is the 4th `BASKETBALL_TOTAL_WITHOUT_PACE_MODEL` review: an established pattern for prompt 8. P-699, which did use pace × efficiency, still missed by 16 on 42% three-point shooting (VARIANCE).
- **Finding 4, shared drivers in the top two.** P-699, P-700 and P-703 each ranked two rows beaten by one shared driver: Cleveland's 43-point quarter, Columbus's late goals, and the Stars' 57/0 powerplay. The cards priced those rows as independent.
- **Finding 5, small samples.** P-697 (six IBSL games, no home edge, no opponent adjustment) is `SMALL_SAMPLE_STRENGTH_OVERREACH`. P-703 priced a six-over line from four innings with an assumed SD.
- **What worked:** of the favoured plus handicaps, Brisbane +4.5 and Aktobe +4.5 (on a malformed label) won, and Indiana +5.5 lost. P-698's arithmetic reproduced exactly. G0003's availability list was right in every name checked.

## 5. Deep loss reviews

Nine reviews, `DLR-2026-11-22-011` to `019`: 7 VARIANCE and 2 MIXED (P-697 `SMALL_SAMPLE_STRENGTH_OVERREACH`, P-701 `BASKETBALL_TOTAL_WITHOUT_PACE_MODEL`), plus three joint sections. `ml deep-loss tally` is clean (no register problems).

## 6. Code finding during settlement (v29.3)

Intake from seals flagged G0007 `INCOHERENT_ACROSS_LINES` because the v29.2 check compared a 6-over score (41.5) with a 20-over innings total (148.5). Card rows carry no endpoint, so from v29.3 two totals are compared only when their lines are within 25% of each other. The intake was rebuilt and carries no false flag.
