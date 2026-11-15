# Card-record training runs (CARD-TRAIN-v1)

Each subfolder is one immutable run of `python -m ml card-training run --out research/card_training/<YYYY-MM-DD-n>`: ROWS.csv (every ingested settled contract row with its admission status), ADMISSION.csv, PREDICTIONS.csv (walk-forward predictions), SCORES.csv, INPUTS.csv (hash of every input file) and RECEIPT.csv. `python -m ml card-training verify --run <folder>` must rebuild the predictions byte for byte. Runs are studies: nothing is applied to a card (ML-SEP-v1). See [ML_PIPELINE](../../ML_PIPELINE.md) section 12.
