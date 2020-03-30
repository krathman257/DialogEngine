import random

class Proposal:

    def __init__(self, sc):
        self.level = -1
        self.startConvo = sc
        self.subRules = []

    def addSubRule(self, sr):
        self.subRules.append(sr)

    def speak(self):
        chosen = self.startConvo[random.randint(0, len(self.startConvo)-1)]
        print(chosen)

    #Tries to get next rule given input
    def getNext(self, humanIn):
        if len(self.subRules) == 0:
            return None
        for r in range(0, len(self.subRules)):
            if self.subRules[r].checkInput(humanIn):
                self.subRules[r].speak()
                return self.subRules[r]
        print("I didn't understand that")
        return "REPEAT"

    def toString(self):
        return "Proposal: "+str(self.level)+") "+self.startConvo

    def printSubRules(self):
        print("SUBRULES OF " + self.toString())
        for i in range(0, len(self.subRules)):
            print("SUBRULE "+str(i)+") "+self.subRules[i].toString())
