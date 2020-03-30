class RuleNode:
        
        level = 0
        speechIn = ""
        speechOut = ""
        parentRule = None
        subRules = []

        def __init__(self, si, so, l):
                self.level = l
                self.speechIn = si
                self.speechOut = so

        def addSubRule(self, sr):
                self.subRules.append(sr)

        def setParent(self, p):
                parentRule = p

        def speak(self):
                print(self.speechOut)

        def getNext(self, humanIn):
                if len(self.subRules) == 0:
                        self.speak()
                        return False
                for r in range(0,len(self.subRules)):
                        if self.subRules[r].speechIn == humanIn:
                                return self.subRules[r]
                if self.parentRule is None:
                        print("I didn't catch that")
                        return "REPEAT"
                else:
                        return self.parentRule.getNext(humanIn)

                
