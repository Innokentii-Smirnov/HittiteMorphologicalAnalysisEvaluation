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
    expected_annotations.extend(exp_text.annotations)
    pred_annotations.extend(pred_text.annotations)
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

print('Precision: {0:.2f}'.format(100 * precision))
print('Recall: {0:.2f}'.format(100 * recall))
print('F1-score: {0:.2f}'.format(100 * fscore))
