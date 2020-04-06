import random

class Concept:

        def __init__(self, n, w=[]):
                self.name = n
                self.words = w

        #Add word to concept
        def addWord(self, w):
                if self.words.count(w) == 0:
                        self.words.append(w)
						
        def getConceptList(self):
                return self.words

        def getComplexConceptList(self, start, end):
                tempArr = []
                for i in range(0, len(self.words)):
                        tempStr = start + self.words[i] + end
                        tempArr.append(tempStr)
                return tempArr
