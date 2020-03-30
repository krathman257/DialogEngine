from DialogMachine import DialogMachine

dm = DialogMachine()
dm.addRule("How are you?", "Pretty good", 0)
dm.addRule("Fuck off", "You too!", 0)

dm.run()
