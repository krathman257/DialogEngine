import random

class RuleNode:

    def __init__(self, si, so, l):
        self.level = l
        self.speechIn = si
        self.speechOut = so
        self.parentRule = None
        self.subRules = []

    def addSubRule(self, sr):
        self.subRules.append(sr)

    def setParent(self, p):
        self.parentRule = p

    def speak(self):
        chosen = self.speechOut[random.randint(0,len(self.speechOut)-1)]
        print(chosen)

    #Bool, checks if input is a string in speechIn
    def checkInput(self, input):
        for i in range(0, len(self.speechIn)):
            if self.speechIn[i].lower() in input.lower():
                return True
        return False

    #Tries to get next rule given input
    def getNext(self, humanIn):
        if len(self.subRules) == 0:
            return None
        for r in range(0, len(self.subRules)):
            if self.subRules[r].checkInput(humanIn):
                self.subRules[r].speak()
                return self.subRules[r]
        if self.parentRule is None:
            print("I didn't catch that")
            return "REPEAT"
        else:
            return self.parentRule.getNext(humanIn)

    def toString(self):
        return "RuleNode: "+str(self.level)+") "+self.speechIn+", "+self.speechOut

    def printSubRules(self):
        print("SUBRULES OF " + self.toString())
        for i in range(0, len(self.subRules)):
            print("SUBRULE "+str(i)+") "+self.subRules[i].toString())

    def printParents(self):
        if self.parentRule is None:
            print("PARENT OF " + self.toString() + " IS NONE")
        else:
            print("PARENT OF " + self.toString() + " IS " + self.parentRule.toString())
