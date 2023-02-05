import numpy as np
import math


board = np.array([['-','-','-'],['-','-','-'],['-','-','-']])
turnNo = 0
winner = ''



def getScore(rowScore):
    
    tempScore = 0

    if (rowScore == 3):
        tempScore += math.inf
    elif (rowScore == 2):
        tempScore += 100
    elif (rowScore == 1):
        tempScore += 1
    elif (rowScore == 0):
        pass
    elif (rowScore == -1):
        tempScore += -1
    elif (rowScore == -2): 
        tempScore += -100
    elif (rowScore == -3):
        tempScore += -math.inf
    
    return tempScore

def evalPos():
     
    posScore = 0
     
    for i in range(3):

        #rows

        noOfX = 0
        noOfO = 0
    
        for j in range(3):
            
            if(board[i,j] == 'X'):
                noOfX += 1
            elif(board[i,j] == 'O'):
                noOfO += 1
        
        rowScore = noOfX - noOfO
        
        posScore += getScore(rowScore)

        
        #collumns

        noOfX = 0
        noOfO = 0
    
        for j in range(3):
            
            if(board[j,i] == 'X'):
                noOfX += 1
            elif(board[j,i] == 'O'):
                noOfO += 1
        
        rowScore = noOfX - noOfO

        posScore += getScore(rowScore)

    #down diagonal  

    noOfX = 0
    noOfO = 0
    
    for i in range(3):
        if(board[i,i] == 'X'):
            noOfX += 1
        elif(board[i,i] == 'O'):
            noOfO += 1
    rowScore = noOfX - noOfO

    posScore += getScore(rowScore)

    #up diagonal
    
    noOfX = 0
    noOfO = 0
    
    j = 2
    for i in range(3):
        if(board[j,i] == 'X'):
            noOfX += 1
        elif(board[j,i] == 'O'):
            noOfO += 1
        j -= 1
    
    rowScore = noOfX - noOfO

    posScore += getScore(rowScore)


       
        
    return posScore


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
        (board[0,y] == board[1,y] == board[2,y])):
            print("Player " + str(playerNo) +  " wins!")
            return True
        
    elif((board[0,0] == board[1,1] == board[2,2]==('X' or 'O')) or 
        (board[2,0] == board[1,1] == board[0,2] == ('X' or 'O'))):
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

    print(evalPos())

    if (checkWin(x,y,playerNo)):
        break
    
    turnNo += 1


