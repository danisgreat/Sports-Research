# NRL nrlR standalone ingestion script
# Pulls match results and play statistics from nrlR and exports clean Parquet tables.
# Run via Rscript without Python rpy2 coupling.

suppressPackageStartupMessages({
  if (!requireNamespace("remotes", quietly = TRUE)) {
    install.packages("remotes", repos = "https://cloud.r-project.org")
  }
  if (!requireNamespace("nrlR", quietly = TRUE)) {
    remotes::install_github("itsjase/nrlR")
  }
  if (!requireNamespace("arrow", quietly = TRUE)) {
    install.packages("arrow", repos = "https://cloud.r-project.org")
  }
  library(nrlR)
  library(arrow)
})

args <- commandArgs(trailingOnly = TRUE)
output_dir <- ifelse(length(args) > 0, args[1], "data/h0/nrl")
dir.create(output_dir, recursive = TRUE, showWarnings = FALSE)

cat("Fetching NRL match data...\n")
nrl_matches <- nrlR::get_matches(seasons = 2021:2026)

output_file <- file.path(output_dir, "nrl_matches.parquet")
arrow::write_parquet(nrl_matches, output_file)
cat("Exported", nrow(nrl_matches), "matches to", output_file, "\n")

