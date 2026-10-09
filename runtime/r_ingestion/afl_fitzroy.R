# AFL fitzRoy standalone ingestion script
# Pulls match, player, and fixture tables from fitzRoy and exports clean Parquet tables.
# Run via Rscript without Python rpy2 coupling. Register the output afterwards:
#   python -B -m runtime.src.common.snapshots register runtime/data/canonical/afl/afl_matches.parquet --sport afl --provider fitzroy --endpoint fetch_results_afl

suppressPackageStartupMessages({
  if (!requireNamespace("fitzRoy", quietly = TRUE)) {
    install.packages("fitzRoy", repos = "https://cloud.r-project.org")
  }
  if (!requireNamespace("arrow", quietly = TRUE)) {
    install.packages("arrow", repos = "https://cloud.r-project.org")
  }
  library(fitzRoy)
  library(arrow)
})

args <- commandArgs(trailingOnly = TRUE)
output_dir <- ifelse(length(args) > 0, args[1], "runtime/data/canonical/afl")
dir.create(output_dir, recursive = TRUE, showWarnings = FALSE)

cat("Fetching AFL match results...\n")
match_data <- fitzRoy::fetch_results_afl(season = 2021:2026)

output_file <- file.path(output_dir, "afl_matches.parquet")
arrow::write_parquet(match_data, output_file)
cat("Exported", nrow(match_data), "matches to", output_file, "\n")

