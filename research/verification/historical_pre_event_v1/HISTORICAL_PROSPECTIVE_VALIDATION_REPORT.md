# Historical pre-event validation — HPPV-v1

Track H verdict: **HISTORICAL_EVIDENCE_INSUFFICIENT**.

Frozen census: 685 cards, 3150 contract rows, P-001–P-685.
Cards with stated probabilities: 280. Tier-A contracts: 0;
cards with at least one Tier-A contract: 0; fully Tier-A cards: 0.
Independently verified decisive events: 0. Same-contract supplied-line paired events: 0.
Event-mean Brier advantage: NOT_COMPUTABLE;
95% event-level interval: [NA, NA].

Every row is retained with a qualification reason. Preserved source references, dates
inside documents, later imports and byte hashes alone do not prove pre-event issuance.
No evidence has been inferred from a winning or losing outcome. Default C classification
means original publication is unverified, not that the forecast was necessarily late.
Missing probabilities are not invented; PUSH, VOID, UNRESOLVED and UNATTAINABLE are
unscored. Conditional decisive probabilities are scored only on decisive outcomes;
three-way probabilities require a separate multiclass protocol. Duplicate exact verified
event-contracts are retained and excluded from repeated scoring.

`HISTORICAL_PERFORMANCE.csv` separates original recovered method, era proxy, sport,
competition, contract family, date and baseline kind. All subgroup comparisons are
exploratory. The pooled estimand is the observed mixture of historical methods, not
one fixed model. The primary paired mean and interval give each sporting event one
vote, including when several P-IDs refer to it. Date, competition and connected-team
block sensitivities report their own block counts; one-block intervals are unavailable.
Effective event n assumes independence across games; block counts show its limits.
Calibration gives each event equal weight within a bin. Log loss alone clips p at 1e-15.

The 100-event and 0.01 Brier gates were adopted after outcomes were observed. Even a
positive verdict is historical evidence, never prospectively preregistered certification.
The evidence reviews are human findings against retained captures; the software validates
their consistency and hashes, and does not itself authenticate a chat export or a result.
Original-method/cutoff/endpoint defects block Tier A or paired admission. A baseline
must be sports-only, market-blind, same-contract, and frozen or explicitly reconstructed
without future features, labels or outcome-informed tuning. Alternative lines cannot
enter the supplied-contract headline. Raw captures and reviewer findings remain required.

Coverage and exclusions: `COVERAGE.csv`, `HISTORICAL_CENSUS.csv`,
`HISTORICAL_QUALIFICATION.csv`. Request-level abstention frequency is unknown until a
complete request census is recovered. Historical training admissions are retained and
do not imply evidence qualification. Existing CARD-TRAIN-v1 approximate-time studies
remain separate; the strict-cutoff backtest command is a new retrospective model study
and cannot establish who generated an original forecast.

Track P: ONE-CHAT-v3 / v27.0 remains independent. Its registry, 400-game horizon,
benchmark, evidence threshold and sequential procedure are unchanged. Use
`python -m ml one-chat score --help` for its live-scoring arguments. No historical rows or counts
are imported into that track and no H/P statistical verdict is pooled.

Reproduce: `python -m ml historical-pre-event verify --run research/verification/historical_pre_event_v1`.
Add evidence through the append command, then generate a new immutable run directory.
`MANIFEST.csv` hashes every input and output except itself; verification regenerates
all tables and this report and checks the complete output inventory.
