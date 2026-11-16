# Deep loss register (DEEPLOSS-v1)

`DEEP_LOSS_REGISTER.csv` holds one appended row per deep loss review: `review_id,canonical_id,contract,trigger,verdict,registered_class,alias,class_basis,source,recorded_at`. The review itself stays in its settlement document (`source`). `registered_class` is a failure class of [RULES_REFERENCE](../../RULES_REFERENCE.md) Part B §8; `alias` is the review's own name for it where it used one.

`python -m ml deep-loss check` validates the file; `python -m ml deep-loss tally` counts reviews per failure. Three or more reviews of one failure is a pattern routed to prompt 8; VARIANCE is never a pattern.

Seeded on 16 November 2026 with the 21 reviews of P-660 to P-685, whose classes were assigned from each review's verdict text (`class_basis`); their triggers were not recorded per review. The 30 reviews of P-639 to P-659 have free-text verdicts and are not in the register.
