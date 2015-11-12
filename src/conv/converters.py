# Part of the Soundsentences program
# By Roelof Ruis <roelof.ruis@gmail.com>

# Base Converter class
class WordConverter():
    def convert(self, token):
        raise NotImplementedError('Please implement the convert method')

# Simple word converter converts word tokens to sets of numbers based on the 
# letters the word contains.
class SimpleWordConverter(WordConverter):
    def convert(self, token):
        letters = token.getLetters()
        codes = []
        for letter in letters:
            newCode = self._convertLetter(letter)
            if newCode not in codes:
                codes.append(newCode)
        return codes
        
    def _convertLetter(self, letter):
        return ord(letter) - 97
    