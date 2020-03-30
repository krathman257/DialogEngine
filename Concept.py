import random

class Concept:
        name = ""
        words = []

        def __init__(self, n):
                self.name = n

        def addWord(self, w):
                if self.words.count(w) == 0:
                        self.words.append(w)

        def getRandWord(self):
                if len(self.words) > 0:
                        return self.words[random.randint(0,len(self.words)-1)]

        def checkWord(self, w):
                return self.words.count(w) > 0
