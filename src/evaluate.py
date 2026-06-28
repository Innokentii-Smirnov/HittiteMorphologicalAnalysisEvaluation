from argparse import ArgumentParser
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.metrics import precision_recall_fscore_support
from model.corpus import Corpus
from model.morph import Annotation

parser = ArgumentParser(
  prog='evaluate.py',
  description='Compute the precision, recall and F1-score of morphological annotation'
)
parser.add_argument('expected_corpus',
                    help='A pass to the corpus with expected annotation')
parser.add_argument('automatically_annotated_corpus',
                    help='A path to the automatically annotated corpus')
args = parser.parse_args()

expected_corpus = Corpus(args.expected_corpus)
pred_corpus = Corpus(args.automatically_annotated_corpus)

expected_annotations = list[list[Annotation]]()
pred_annotations = list[list[Annotation]]()

for exp_text, pred_text in expected_corpus.zip(pred_corpus):
  if len(exp_text) == len(pred_text):
    print('Matched', exp_text.text_id)
    for exp_word, pred_word in exp_text.zip(pred_text):
      if exp_word.lang == 'Hit' and pred_word.is_ambiguous():
        expected_annotations.append(exp_word.annotations)
        pred_annotations.append(pred_word.annotations)
  else:
    print('Ignoring', exp_text.text_id)

mlb = MultiLabelBinarizer(sparse_output=True)
exp = mlb.fit_transform(expected_annotations)
pred = mlb.transform(pred_annotations)

precision, recall, fscore, support = precision_recall_fscore_support(
  exp, pred, average='micro'
)

assert isinstance(precision, float)
assert isinstance(recall, float)
assert isinstance(fscore, float)

print('Number of word tokens in the matched texts: {0}'.format(len(expected_annotations)))
print('Number of distinct expected annotations: {0}'.format(len(mlb.classes_)))

print('Precision: {0:.2f}'.format(100 * precision))
print('Recall: {0:.2f}'.format(100 * recall))
print('F1-score: {0:.2f}'.format(100 * fscore))
