#krathman

from Proposal import Proposal
from RuleNode import RuleNode

class DialogMachine:

    def __init__(self):
        self.proposal = False
        self.concepts = []
        self.rules = [RuleNode("", "", -1)]
        pass

    #Adds rule, sets parent-child relationship
    #given level and previous rules
    def addRule(self, i, o, l=0):
        rn = RuleNode(i, o, l)
        if l > -1:
            for p in range(len(self.rules)-1, -1, -1):
                if self.rules[p].level == l - 1:
                    rn.setParent(self.rules[p])
                    self.rules[p].addSubRule(rn)
                    break
        self.rules.append(rn)

    #When building machine, call before any
    #addRules if proposal is present
    def setProposal(self, p):
        self.proposal = True
        self.rules[0] = Proposal(p)

    #Returns concept with name n
    def getConcept(self, n):
        for i in range(0, len(self.concepts)):
            if self.concepts[i].name == n:
                return self.concepts[i]
        print('ERR: Concept Not Found')
        return None

    def printRules(self):
        for i in range(0, len(self.rules)):
            print(self.rules[i].toString())

    #Runs dialog machine
    def run(self):
        stop = False
        currentRule = self.rules[0]
        if self.proposal == True:
            currentRule.speak()
        while not stop:
            humanIn = input()
            nextRule = currentRule.getNext(humanIn)

            if not nextRule == "REPEAT":
                currentRule = nextRule
        print("\nENDING SCRIPT...")
