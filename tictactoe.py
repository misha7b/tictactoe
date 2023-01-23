import numpy as np


board = np.array([["-","-","-"],["-","-","-"],["-","-","-"]])
turnNo = 0
winner = ''



def placeX(x,y):
    board[x,y] = 'X'

def placeO(x,y):
    board[x,y] = 'O'


def validMove(x,y):
    if (board[x,y] == '-' and (0 <= x <= 3) and (0 <= x <= 3) ):
        return True
    else:
        return False
    

def checkWin(x,y,playerNo):
    
    if ((board[x,0] == board[x,1] == board[x,2]) or 
        (board[0,y] == board[1,y] == board[2,y]) or 
        (board[0,0] == board[1,1] == board[2,2]) or 
        (board[2,0] == board[1,1] == board[0,2])):
            print("Player " + str(playerNo) +  " wins!")
            return True



print(board)

while (True):

    if (turnNo == 9):
        print("Draw!")
        break

    playerNo = (turnNo % 2) + 1

    print("Player " + str(playerNo) + "'s turn")
    x,y = map(int, (input().split()))
    
    while(validMove(x,y) == False):
        print("Invalid move!")
        x,y = map(int, (input().split()))
    
    
    if (turnNo % 2 == 0):
        placeX(x,y)
    else:
        placeO(x,y)
        

    print(board)

    if (checkWin(x,y,playerNo)):
        break

    
    
    turnNo += 1


