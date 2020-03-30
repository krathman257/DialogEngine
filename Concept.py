import random

class Concept:

        def __init__(self, n, w=[]):
                self.name = n
                self.words = w

        #Add word to concept
        def addWord(self, w):
                if self.words.count(w) == 0:
                        self.words.append(w)

        #Return random word
        def getRandWord(self):
                if len(self.words) > 0:
                        return self.words[random.randint(0,len(self.words)-1)]

        #Check if word is in concept
        def checkWord(self, w):
                return self.words.count(w) > 0
