"""""
def playerMove(name):
    print("Player ", name, " pick a move using row/col coordinates, e.g. 1,1 or 4,12")
    return list(map(int, input().split(",")))

def printGame(game):
    for row in game:
        print(row)

"""""

beginBoard = [[0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]



def updateGame(game, move, player):
    [row, col] = move
    game[row][col] = player
    return game

updateGame(beginBoard, [0,0], 1)

"""""
def moveValid(game, move) :
    return True

def gameOver(game) :
    return False

def playGame():
    game = [[0,0,0,0],
            [0,1,2,0]
            [0,2,1,0],
            [0,0,0,0]]
    currentPlayer = 1
    while True:
        move = playerMove(currentPlayer)
        if not moveValid(game, move) :
            print ("Invalid move, try again")
            continue
        else :
            game = updateGame(game, move, currentPlayer)
            printGame(game)
            if gameOver(game):
                print("someone won")
                return
            else :
                if currentPlayer == 1:
                    currentPlayer = 2
                else :
                    currentPlayer = 1


 playGame() """