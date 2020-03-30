from DialogMachine import DialogMachine
from Concept import Concept

dm = DialogMachine()

dm.setProposal(["I am a FUCKING robot", "Talk to me if you want to live!"])

dm.addRule(["how are you?", "how are you doing?"], ["Pretty good", "Just fine"], 0)
dm.addRule(["happy?", "feeling good?"], ["Yep", "Abso-didily-oodily"], 1)
dm.addRule(["fuck off", "go fuck yourself"], ["You too!", "That was mean..."], 0)
dm.addRule(["i'm sorry", "that was rude of me"], ["It's OK", "Just be nicer in the future..."], 1)

dm.run()
