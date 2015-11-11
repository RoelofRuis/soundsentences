# Main file for the soundsentences program.
# By Roelof Ruis <roelof.ruis@gmail.com>
from text.parsers import SimpleSentenceParser

input = 'input/text.txt'

parser = SimpleSentenceParser()

with open(input, 'r') as f:
    data = f.readlines()
    tokens = parser.parse(data[0])

for token in tokens:
    print token