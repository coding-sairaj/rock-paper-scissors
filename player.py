from choice import Choice


class Player:
    def __init__(self, name):
        self.name = name
        self.wins = 0
        self.choice = Choice.default

    def setChoice(self, choice:int):
        self.choice = Choice(choice)
