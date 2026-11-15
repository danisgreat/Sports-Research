# Scope · on-request comprehensive audit · 16 November 2026

Written before the analysis. Trigger: owner request (AUDIT-ANYTIME-v1, CR-2026.11.15-R3). Level COMPREHENSIVE, scope ALL. Prompt 6 at P-2026.11.15-v24.18, method MDS-2026.11.15-v24.20, scoring SCV-2026.11.15-v15. Authority mode LOCAL_WORKING_TREE, branch `main`, HEAD `4e60611bc`, clean tree at the start of the run.

| Item | Value |
|---|---|
| Cards | Every settled canonical card P-001 to P-685 (685 cards, 30 July to 15 November 2026, 14 ISO weeks) |
| Row source | `research/card_training/2026-11-15-2/ROWS.csv` (SHA-256 `30f24f0beee331be1c4ac179adcd4ee5f769810f0fb3c43236d22b2cf10b1c2b`), built by CARD-TRAIN-v1 from the rank log, the effective settlements and the import inventories |
| Included | 3,029 decisive rows on 655 cards; 1,273 of them carry a stated probability (279 cards) |
| Excluded, with reason | 121 rows: 82 UNRESOLVED (32 cards), 12 UNATTAINABLE, 12 VOID, 10 PUSH, 5 UNDATED |
| Outcome exposure | Complete. Every outcome was known before this analysis. Everything here is retrospective and descriptive |
| Cohorts kept apart | Issued primary cards (ANALYST_PRIMARY_V1, 16 cards), rank-log cards, research-only and chat-local cards (NOT_PRIMARY), legacy views |
| Baselines | No frozen same-row pregame baseline exists for any card in scope. The only fixed comparator is the constant 0.5 that a two-way line implies |
| Model lanes | MLB-CYCLE-4, NHL-CYCLE-6, NBA-CYCLE-4: all three reviewed from `ml pregame status` |
| Also reviewed | Every root operating document, the eight prompts and eleven sport files, the external-chat upload package, `ml/` code and tests, the learning store, the registers and the two latest import packages |
| Not in scope | The decision lab. No market data was read or used |
| Comparisons declared | Stated p against 0.5 by card; stated p against its own win rate by band, rank, sport, month and era; win rates by rank, sport and contract family; deep loss verdicts for P-660 to P-685 |
| What this cannot show | Prospective skill. No selection, statistical or model rule is changed by this audit (FREEZE-v1) |
