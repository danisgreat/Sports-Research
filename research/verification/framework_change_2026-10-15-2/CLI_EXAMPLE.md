# Executed synthetic CLI example

EXAMPLE only: not sporting evidence, a live forecast or predictive validation. Used the actual Basketball/NBL route configuration with synthetic team/score history and a deliberately labelled synthetic source capture. Source truth NOT_CERTIFIED. No P-ID.

Executed primary predict -> primary settle -> next primary predict with retained feedback. Both output bundles read back by verify_bundle; all grids/probabilities/baselines/input/config hashes matched.

Cold behaviour: RATINGS_FAST:0.33333333333333331;RATINGS_SLOW:0.33333333333333331;LEAGUE_BASELINE:0.33333333333333331

After available original top-two feedback: RATINGS_FAST:0.32480648268366075;RATINGS_SLOW:0.3503870346326784;LEAGUE_BASELINE:0.32480648268366075

Selected first expert: RATINGS_SLOW; issued receipt SHA256 543377e070621658dd4f5d01a1bb6ea8357c6693eedf2c39856e459ba8638589.

Second receipt SHA256 56bb1b00873b7ab6e3d3173119eb1a9ab1803579842d4aa626709bb627a2665a. Both declare EXPERIMENTAL_PRIMARY_NOT_CERTIFIED. Explicit seed19 is a reproducibility option, not searched for results. Normal runs use fresh system randomness.

Local-only inputs/bundles/capture/feedback: `C:\Users\danie\Downloads\primary_integration_2026-10-15_custody\cli_demo`. Only this summary is published. First request declared 2023 issue times; actual generation is recorded independently, so this demonstrates mechanics, never pre-start publication.
