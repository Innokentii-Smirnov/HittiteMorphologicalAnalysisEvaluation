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
python src/evaluate.py \
  ~/HFR/data/expected/"$dataset" \
  ~/HFR/data/lemmatized-xml/"$dataset"
