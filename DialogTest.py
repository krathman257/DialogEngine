from DialogMachine import DialogMachine

dm = DialogMachine()

dm.setProposal(["I am a FUCKING robot", "Talk to me if you want to live!"])

dm.addRule(["How are you?", "How are you doing?"], ["Pretty good", "Just fine"], 0)
dm.addRule(["Happy?", "Feeling good?"], ["Yep", "Abso-didily-oodily"], 1)
dm.addRule(["Fuck off", "Go fuck yourself"], ["You too!", "That was mean..."], 0)
dm.addRule(["I'm sorry", "That was rude of me"], ["It's OK", "Just be nicer in the future..."], 1)

dm.run()
