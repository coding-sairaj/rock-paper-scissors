# Rock Paper Scissors

Built the application using python. Did the backend only part of the assignment. We can play the app from console.

Run the app
```
> python main.py
```
## Features
1. [Play vs Computer](#vs-computer)
2. [Play vs opponent](#vs-opponent)
3. [Show Games](#show-games)
4. [Load played games](#load-games)

## vs Computer
1. Select option 1 Single player.
2. Enter players name (We default computers name to Computer1).
3. Select one of the options rock(0), paper(1), scissors(2).
4. We compare it with random generated computers choice and show the game result for all the rounds played till now.
5. We can continue playing the game or save the game and exit or directly exit.
## vs Opponent
1. Select option 2 for Multi player.
2. Enter both player names one after another.
3. Enter choices of the players as prompted.
4. We compare the choices and show the winners name.
5. We can continue playing the game or save the game and exit or directly exit.
## Show Games
1. Select option 3 to show all the games that are saved.
2. If there is no saved data returns back to the menu.
## Load Games
1. Loads the game based on the index. We can get index from show games.
2. Selecting option 4 Load saved games prompts to see all the games. If we select option 3 it shows the game and we can pick index from there.


# What can be done
1. UI for the application.
2. Logging implementation.
3. Better error handling. Currently we are just showing the menu again to enter the input and error handling was only done in one case.
4. Currently we are saving games in memory which will get out of hand as the usage increases. We can choose some other kind of persisting mechanism.