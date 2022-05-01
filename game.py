from rpc import playerWins

class Game:
    counter = 1
    def __init__(self, player1, player2):
        self.id = Game.counter
        Game.counter += 1
        self.players = [player1, player2]
        self.rounds = []

    def playGame(self):
        if(self.players[0].choice == self.players[1].choice):
            self.rounds.append('Round draw')
        elif playerWins(self.players[0].choice, self.players[1].choice):
            self.rounds.append(f'{self.players[0].name} wins')
            self.players[0].wins += 1
        else:
            self.rounds.append(f'{self.players[1].name} wins')
            self.players[1].wins += 1

    def results(self):
        print('Game result: ')
        for round in self.rounds:
            print(round)