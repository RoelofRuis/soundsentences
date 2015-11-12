# Main file for the soundsentences program.
# By Roelof Ruis <roelof.ruis@gmail.com>
from text.tokenizers import SimpleSentenceTokenizer
from conv.converters import SimpleWordConverter

input     = 'input/text.txt'
tokenizer = SimpleSentenceTokenizer()
converter = SimpleWordConverter()

with open(input, 'r') as f:
    data   = f.readlines()
    tokens = tokenizer.tokenize(data[0])

for token in tokens:
    print converter.convert(token)