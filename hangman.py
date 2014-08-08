#!/usr/bin/python

# Let's win at Hangman, shall we?

# API Reference:
# hangman(word_length[, dictionary_url]).guess()

from __future__ import absolute_import, with_statement, print_function, unicode_literals
import urllib

def makestr(inputobj):
    if isinstance(inputobj, unicode):
        return inputobj
    elif isinstance(inputobj, str):
        return unicode(inputobj, "UTF")
    elif isinstance(inputobj, list):
        return "".join(map(makestr, inputobj))
    else:
        raise ValueError("Cannot convert to unicode "+repr(inputobj))

def swaptuple(tuplelist):
    out = []
    for x,y in tuplelist:
        out.append((y,x))
    return out

class hangman(object):
    """A Hang Man AI."""
    def guess(self):
        """The Public API function. Returns a tuple: (guess_letter, answer_function) where
    guess_letter = A single unicode char representing the AI's next guess.
    answer_function = A function that should be called to respond to the AI's guess with arguments
        answer_function(indexlist) where indexlist is a list of all the string indexes where that letter was found.
        The answer_function will then return this function again for use in getting the next guess.
    If the AI has found your word exactly, it will return that as the first argument and a function to print it as the second."""
        self.clean()
        if len(self.words) == 0:
            raise ValueError("Your word doesn't exist in the dictionary!")
        elif len(self.words) == 1:
            return (self.words[0], lambda: print("Your word is "+self.words[0]+"."))
        else:
            letter = self.get_letter()
            def _answer(indexes=[]):
                if len(indexes) == 0:
                    self.addno(letter)
                else:
                    for index in indexes:
                        self.addyes(letter, index)
                return self.guess
            return (letter, _answer)
    def __init__(self, word_length, dictionary_url="https://raw.githubusercontent.com/evhub/Hangman/master/dictionary.txt"):
        """Call with the length of the word in question as the first argument, and the url where a dictionary can be accessed as the second."""
        self.wordlen = int(word_length)
        self.get_dictionary(dictionary_url)
        self.yes = {}
        self.no = ""
    def get_dictionary(self, url):
        url = makestr(url)
        self.words = []
        path = str(urllib.urlretrieve(url)[0])
        with open(path, "rb") as f:
            for line in f:
                line = line.strip()
                if self.wordlen == len(line):
                    self.words.append(line)
    def check(self, word):
        for p,c in self.yes.iteritems():
            if word[p] != c:
                return False
        for c in word:
            if c in self.no:
                return False
        return True
    def clean(self):
        if len(self.yes) + len(self.no) > 0:
            words, self.words = self.words, []
            for word in words:
                if self.check(word):
                    self.words.append(word)
    def get_letter(self):
        yes = makestr(self.yes.values())
        letters = {}
        for word in self.words:
            for c in word:
                if c not in yes:
                    if c in letters:
                        letters[c] += 1
                    else:
                        letters[c] = 0
        return max(swaptuple(letters.items()))[1]
    def addyes(self, letter, pos):
        self.yes[int(pos)] = makestr(letter)
    def addno(self, letter):
        self.no += makestr(letter)
