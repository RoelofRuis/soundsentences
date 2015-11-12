# Main file for the soundsentences program.
# By Roelof Ruis <roelof.ruis@gmail.com>
from text.tokenizers import SimpleSentenceTokenizer

input = 'input/text.txt'

parser = SimpleSentenceTokenizer()

with open(input, 'r') as f:
    data = f.readlines()
    tokens = parser.parse(data[0])

for token in tokens:
    print token.getLetters()