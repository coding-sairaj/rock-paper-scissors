from secrets import choice
from choice import Choice
from random import getrandbits, randint

def generateRandomChoice():
    return Choice(randint(0,2))

def playerWins(player1Choice:Choice, player2Choice:Choice):
    if player2Choice == Choice.default:
        player2Choice = generateRandomChoice()
    if player1Choice == Choice.Rock:
        return player2Choice == Choice.Scissors
    elif player1Choice == Choice.Paper:
        return player2Choice == Choice.Rock
    else:
        return player2Choice == Choice.Paper

