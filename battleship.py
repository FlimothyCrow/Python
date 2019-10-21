import copy


def updateGame(game, move, player):
    [row, col] = move
    newGame = game
    newGame[row][col] = player
    return newGame


# updateGame(beginBoard, [0,0], 1)

def printGame(game):
    for row in game:
        print(row)


def moveValid(game, move):
    x, y = move
    if game[x][y] == 9 :
        return False
    elif game[x][y] == 8 :
        return False
    else :
        return True


# moveValid(shipsBoard, [0,0])

def hitMiss(game, move):  # remember (move) == player-entered coordinates
    x, y = move
    if game[x][y] == 2:
        return True


def playerMove(name):
    print("Player", name, "pick a move using row/col coordinates, e.g. 1,1"
                          "\nRemember, 8 = miss, and 9 = hit")
    return list(map(int, input().split(",")))


# remember that playerMove doesn't need to update the game
# its only purpose is to extract the move data from the user
# that data can be returned to another function

def gameOver(game):
    newGroup = [y for x in game for y in x]
    if newGroup.count(9) == 4 :
        return True
    else :
        return False


def run(currentPlayer, playerBoard, shipsBoard):
    move = playerMove(currentPlayer)
    if moveValid(playerBoard, move):
        if hitMiss(shipsBoard, move):
            print("Hit!")
            playerBoard = updateGame(playerBoard, move, 9)
            printGame(playerBoard)
            if gameOver(playerBoard):
                    print(currentPlayer, "is the winner!")
        else:
            print("Miss")
            playerBoard = updateGame(playerBoard, move, 8)
            printGame(playerBoard)
    else:
        print("That space was already attempted")



def playGame():
    playerBoard1 = [[0, 0, 0, 0],
                   [0, 0, 0, 0],
                   [0, 0, 0, 0],
                   [0, 0, 0, 0]]

    shipsBoard1 = [[2, 0, 0, 0],
                   [2, 0, 0, 0],
                   [0, 0, 0, 0],
                   [0, 0, 2, 2]]

    playerBoard2 = [[0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0]]

    shipsBoard2 = [[0, 0, 0, 0],
                   [0, 2, 2, 0],
                   [0, 0, 0, 0],
                   [0, 2, 2, 0]]

    while True:
      run(1, playerBoard1, shipsBoard1)
      run(2, playerBoard2, shipsBoard2)

# can we build it so that an attempted invalid move restarts that turn?
# the victory conditional from gameOver only prints after a "failed" move
# right now gameOver is based on having 4 hits, shouldn't that vary?
# can we put meat in moveValid so the game doesn't crash with string inputs?

playGame()

















