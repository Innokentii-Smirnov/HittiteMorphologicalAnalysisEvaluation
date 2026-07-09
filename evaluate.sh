dataset="$1"
python src/evaluate.py \
  ~/HFR/data/expected/"$dataset" \
  ~/HFR/data/lemmatized-xml/"$dataset"
