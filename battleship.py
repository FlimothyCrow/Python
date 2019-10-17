import copy

beginBoard = [[0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]

shipsBoard = [[0, 2, 0, 0],
              [0, 2, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 2, 2]]

def updateGame(game, move, player):
    [row, col] = move
    newGame = copy.deepcopy(game)
    newGame[row][col] = player
    return newGame

#updateGame(beginBoard, [0,0], 1)

def printGame(game) :
    for row in game :
        print(row)


def moveValid(game, move) :
    x, y = move
    if game[x][y] == 1 :
        return False
    else:
        return True

moveValid(shipsBoard, [0,0])

def hitMiss(game, move) : # remember (move) == player-entered coordinates
    x, y = move
    if game[x][y] == 2:
      return True

def playerMove(name):
    print("Player", name, "pick a move using row/col coordinates, e.g. 1,1 or 4,12")
    return list(map(int, input().split(",")))
# remember that playerMove doesn't need to update the game
# its only purpose is to extract the move data from the user
# that data can be returned to another function


def playGame():
    game = [[2,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0]]
    currentPlayer = 1
    while True:
        move = playerMove(currentPlayer)
        if moveValid(game, move) :

            if hitMiss(game, move) :
                print("Hit!")
                game = updateGame(game, move, currentPlayer)
                printGame(game)
            else :
                print("Miss")
        else :
            print("Invalid move, try again")

# wait until completion for player 2
#playGame()
"""""
a = [[1,2,3,4], [5,6,7,8], [0,0,0,0],[0,0,0,0]]
b = [8,9]
var0, var1, var2, var3 = a

print(var1)
"""""
playGame()