import random

class Concept:

        def __init__(self, n, w=[]):
                self.name = n
                self.words = w

        #Add word to concept
        def addWord(self, w):
                if self.words.count(w) == 0:
                        self.words.append(w)
