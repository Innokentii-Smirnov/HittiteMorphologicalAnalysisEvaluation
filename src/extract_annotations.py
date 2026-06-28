from argparse import ArgumentParser
from json import dump
from model.corpus import Corpus
import loggers

parser = ArgumentParser(
    prog='extract_annotations.py',
    description='Extract morphological annotation (lemmata and morphological analyses) from XML files'
)
parser.add_argument('input_directory',
                    help='a directory containing morphologically annotated texts in XML files')
parser.add_argument('outfile',
                    help='a name for the JSON file to store the result')
args = parser.parse_args()

corpus = Corpus(args.input_directory)
annotations = list(corpus.annotations)

with open(args.outfile, 'w', encoding='utf-8') as fout:
    dump(annotations, fout, ensure_ascii=False, indent=4)

print(len(annotations))
