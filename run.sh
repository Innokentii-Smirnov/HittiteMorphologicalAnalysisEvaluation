clear
cth="$1"
if [ -z "$cth" ]; then
  echo 'A CTH text group should be specified as the first argument.'
  exit
fi
source="$2"
if [ -z "$source" ]; then
  echo 'A source (HFR, TLH, etc) should be specified as the second argument.'
  exit
fi
dataset="CTH ${cth}_XML_$source"
outdir=~/Hittite/data/annotations/"$dataset"
mkdir -p "$outdir"
pred_count=$(python src/extract_annotations.py \
  ~/HFR/data/lemmatized-xml/"$dataset" \
  "$outdir/predicted.json")
exp_count=$(python src/extract_annotations.py \
  ~/HFR/data/expected/"$dataset" \
  "$outdir/expected.json")
echo "Number of words in the expected corpus: $exp_count."
echo "Number of words in the automatically annotated corpus: $pred_count."
