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


class AcceptedWordsConverter(WordConverter):
    accepted_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 's', 'i']

    def convert(self, tokens):
        filtered_words = self._filterWords(tokens)

        return filtered_words

    def _filterWords(self, tokens):
        filtered_words = []

        for token in tokens:
            token_string = str(token)
            filtered_word = ''

            for letter in token_string:
                if letter in AcceptedWordsConverter.accepted_letters:
                    filtered_word += letter

            filtered_words.append(filtered_word)

        return filtered_words
