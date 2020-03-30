class Proposal:

        startConvo = ""
        subRules = []

        def __init__(self, sc):
                self.startConvo = sc

        def addSubRule(self, sr):
                self.subRules.append(sr)

        def speak(self):
                print(self.startConvo)

        def getNext(self, humanIn):
                if len(self.subRules) == 0:
                        return None
                for r in range(0,len(self.subRules)):
                        if self.subRules[r].speechIn == humanIn:
                                return self.subRules[r]
                print("I didn't understand that")
                return self
