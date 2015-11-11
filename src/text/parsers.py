# Part of the Soundsentences program
# By Roelof Ruis <roelof.ruis@gmail.com>
from tokens import SimpleWordToken

# Base sentence parser class defining the basics that a sentence parser needs
# to be able to do.
class SentenceParser():
    
    def parse(self, sentence):
        raise NotImplementedError("Please implement this method")


# The sentence parser produces word tokens from a sentence.
# It is very simple in its function.
class SimpleSentenceParser(SentenceParser):
    def __init__(self, *args):
        if 'tokenType' in args:
            self.tokenType = args['tokenType']
        else:
            self.tokenType = SimpleWordToken
        
    def parse(self, sentence):
        cleanSentence = self._cleanText(sentence)
        words         = self._splitText(cleanSentence)
        tokens        = self._asTokens(words)
        self.tokens = tokens
        return tokens
        
    def _cleanText(self, sentence):
        cleanSentence = sentence.translate(None, '.!?')
        return cleanSentence.lower()
        
    def _splitText(self, sentence):
        return sentence.split()
    
    def _asTokens(self, words):
        tokens = []
        for word in words:
            tokens.append(self.tokenType(word))
        return tokens