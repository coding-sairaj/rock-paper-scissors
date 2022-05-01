from multiprocessing.sharedctypes import Value
from game import Game
from player import Player

# To handle input options
def getValidIntegerInput(prompt, choices):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            # logging can be done here
            continue
        if value in choices:
            break
        else:
            continue
    return value

def setPlayerChoice(player1, player2):
    print("Enter choice \n 0 Rock, \n 1 Paper, and \n 2 Scissors \n")
    player1.setChoice(getValidIntegerInput(f'Enter {player1.name} choice:', [0,1,2]))
    if option == 2:
        player2.setChoice(getValidIntegerInput(f'Enter {player2.name} choice:', [0,1,2]))

games = []

def showGames():
    if len(games) > 0:
        for idx, game in enumerate(games):
            print(f'{idx} {game.players[0].name} vs {game.players[1].name}')

while True:
    option = getValidIntegerInput('Enter \n 1 Single player \n 2 Multi player \n 3 Show Games \n 4 Load Saved Game \n 9 Quit \n', [1,2,3,4,9])

    if option == 9:
        break
    if option == 1:
        player1 = Player(input('Enter player 1 name: '))
        player2 = Player('Computer1')
    elif option == 3:
        showGames()
        continue
    elif option == 4:
        listGames = input('Enter game index. To get indexes press 3 to get list of Games, else press enter. ')
        if listGames == 3:
            showGames()
        gameidx = int(input('Enter Game Idx: '))
        game = games[gameidx]
    else:
        player1 = Player(input('Enter player 1 name: '))
        player2 = Player(input('Enter player 2 name: '))
    if option != 4:
        game = Game(player1, player2)

    while True:
        setPlayerChoice(player1, player2)        
        game.playGame()
        game.results()
        
        val = getValidIntegerInput('Enter \n 1 Play Again \n 2 Save & Exit \n 9 Exit Game. \n', [1,2,9])
        if val == 9:
            break
        elif val == 2:
            games.append(game)
            break