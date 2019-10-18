import copy


def updateGame(game, move, player):
    [row, col] = move
    newGame = game
    newGame[row][col] = player
    return newGame

#updateGame(beginBoard, [0,0], 1)

def printGame(game) :
    for row in game :
        print(row)


def moveValid(game, move) :
    x, y = move
    if game[x][y] == 9 :
        return False
    else:
        return True

#moveValid(shipsBoard, [0,0])

def hitMiss(game, move) : # remember (move) == player-entered coordinates
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

def gameOver(game) :
    data = any(0 in sublist for sublist in game)
    return data




def playGame():
    playerBoard = [[0, 0, 0, 0],
                   [0, 0, 0, 0],
                   [0, 0, 0, 0],
                   [0, 0, 0, 0]]

    shipsBoard = [[2,0,0,0],
                  [2,0,0,0],
                  [0,0,0,0],
                  [0,0,2,2]]
    currentPlayer = 1
    while True:
        move = playerMove(currentPlayer)
        if moveValid(shipsBoard, move) :
            if hitMiss(shipsBoard, move) :
                print("Hit!")
                playerBoard = updateGame(playerBoard, move, 9)
                printGame(playerBoard)
            else :
                print("Miss")
                playerBoard = updateGame(playerBoard, move, 8)
                printGame(playerBoard)
        else :
            print("That space was already attempted")

# shouldn't updateGame be redefining shipsBoard within playGame?
# currently we're printing an updated playerBoard, but NOT redefining it
# hitMiss is only giving us good data until we make a hit
# if we attempt the same coordinate, we get a correct failure from moveValid
# after that, everything registers as miss

# wait until completion for player 2

#playGame()






"""""
a = [[1,2,3,4], [5,6,7,8], [0,0,0,0],[0,0,0,0]]
b = [8,9]
var0, var1, var2, var3 = a

print(var1)

----------------

if shipsBoard[0][1] == beginBoard[0][1] :
    print(True)
else :
    print(None)
"""""