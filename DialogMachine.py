from Concept import Concept
from Proposal import Proposal
from RuleNode import RuleNode

class DialogMachine:
                
        proposal = None
        concepts = []
        rules = [RuleNode("", "", -1)]

        def __init__(self):
                pass

        def addRule(self, i, o, l=0):
                rn = RuleNode(i, o, l)
                if l >= -1:
                        for p in range(len(self.rules), 0, -1):
                                if self.rules[p-1].level == l-1:
                                        rn.setParent(self.rules[p-1])
                                        self.rules[p-1].addSubRule(rn)
                self.rules.append(rn)

        def addConcept(self, c):
                self.concepts.append(c)

        def setProposal(self, p):
                self.proposal = p

        def getConcept(self, n):
                for i in range(0,len(self.concepts)):
                        if self.concepts[i].name == n:
                                return self.concepts[i]
                print('ERR: Concept Not Found')
                return None

        def run(self):
                stop = False
                currentRule = ""
                if len(self.rules) == 0:
                        stop == True
                elif self.proposal is not None:
                        currentRule = proposal
                        currentRule.speak()
                else:
                        currentRule = self.rules[0]
                while not stop:
                        humanIn = input()
                        nextRule = currentRule.getNext(humanIn)
                        if not nextRule == "REPEAT":
                                currentRule = nextRule
                        if currentRule is None or currentRule == False:
                                stop = True
                print("Shutting down...")
                        



