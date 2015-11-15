# Main file for the soundsentences program.
# By Roelof Ruis <roelof.ruis@gmail.com>
from text.tokenizers import SimpleSentenceTokenizer
from conv.converters import AcceptedWordsConverter

input     = 'input/text.txt'
tokenizer = SimpleSentenceTokenizer()
converter = AcceptedWordsConverter()

with open(input, 'r') as f:
    data   = f.readlines()
    tokens = tokenizer.tokenize(data[0])

print converter.convert(tokens)
