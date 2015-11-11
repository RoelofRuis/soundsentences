# Part of the Soundsentences program
# By Roelof Ruis <roelof.ruis@gmail.com>

# The WordToken class is the base word token class.
class WordToken():
    def __init__(self, word):
        self.word = word
        
    def getWord(self):
        return self.word

    def getLetters(self):
        return list(self.word)

    def __str__(self):
        return 'Base WordToken class that should be subclassed.'

# The SimpleWordToken class represents a single word as a token.
class SimpleWordToken(WordToken):
    def __init(self, word):
        super(SimpleWordToken, self).__init__(word)
        
    def __str__(self):
        return self.word