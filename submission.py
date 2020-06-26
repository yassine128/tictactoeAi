import numpy as np
import sys
import random
import numpy as np
from math import inf as infinity

global c
grid = [0, 0, 0, 0, 0, 0, 0, 0, 0]
gridn = grid.copy()

def isboardfull():
    full = []
    for i in range(9):
        if grid[i] == 0:
            full.append(i)
    if len(full) == 0:
        print("Tie")


def confirmO():
    global c
    c=0
    c1 = gridn[0] + gridn[3] + gridn[6]
    c2 = gridn[1] + gridn[4] + gridn[7]
    c3 = gridn[2] + gridn[5] + gridn[8]
    d1 = gridn[0] + gridn[4] + gridn[8]
    d2 = gridn[2] + gridn[4] + gridn[6]

    #[1, 1, 4, 0, 0, 0, 4, 0, 0]
    if sum(gridn[:3]) == 12 or sum(gridn[3:6]) == 12 or sum(gridn[6:9]) == 12:
        c = 1
    elif c1 == 12 or c2 == 12  or c3 == 12:
        c = 1
    elif d1 == 12  or d2 == 12:
        c = 1
    elif sum(gridn[:3]) == 6 or sum(gridn[3:6]) == 6 or sum(gridn[6:9]) == 6:
        c=-1
    elif c1 == 6 or c2 == 6  or c3 == 6:
        c = -1
    elif d1 == 6  or d2 == 6:
        c = -1

def winningO():
    c1 = grid[0] + grid[3] + grid[6]
    c2 = grid[1] + grid[4] + grid[7]
    c3 = grid[2] + grid[5] + grid[8]
    d1 = grid[0] + grid[4] + grid[8]
    d2 = grid[2] + grid[4] + grid[6]
    if sum(grid[:3]) == 12 or sum(grid[3:6]) ==12 or sum(grid[6:9]) == 12:
        print("O WON")
        sys.exit()
    elif c1 == 12 or c2 == 12 or c3 ==12:
        print("O WON")
        sys.exit()
    elif d1 == 12 or d2 == 12:
        print("O WON")
        sys.exit()

#===================Ennemy logic===========================
mini = []
score = []
w1 = 0
def bot():
    mini.clear()
    for m in range(9):
        if grid[m] == 0:
            mini.append(m)
    for n in range(len(mini)):
        global gridn 
        gridn = grid.copy()
        v2 = mini[n]
        gridn[v2] = 4
        confirmO()        
        if c == 1:
            board[v2] = 'O'
            grid[v2] = 4
            break
        elif c == -1:
            board[v2] = 'O'
            grid[v2] = 4  
            gridn.clear()
            break   
        elif n+1==len(mini):
            v3 = random.choice(mini)
            grid[v3] = 4
            board[v3] = 'O'
            gridn.clear()
        else:
            gridn.clear()

"""
doit faire une liste du genre [-1,1,1,-1,0]
pseudocode:
si il y a une valeur de 1 (chance de gagner) Prendre
sinon si il y a -1 tu prends -1 
sinon prendre 0
"""
#=====================Game Logic============================

board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
grid = [0, 0, 0, 0, 0, 0, 0, 0, 0]


def winningX():
    c1 = grid[0] + grid[3] + grid[6]
    c2 = grid[1] + grid[4] + grid[7]
    c3 = grid[2] + grid[5] + grid[8]
    d1 = grid[0] + grid[4] + grid[8]
    d2 = grid[2] + grid[4] + grid[6]
    if sum(grid[:3]) == 3 or sum(grid[3:6]) ==3 or sum(grid[6:9]) == 3:
        print("X WON")
        sys.exit()
    elif c1 == 3 or c2 == 3 or c3 ==3:
        print("X WON")
        sys.exit()
    elif d1 == 3 or d2 == 3:
        print("X WON")
        sys.exit()


def printboard():
    print('')
    print('')
    print(str(board[0])+"|"+str(board[1])+"|"+str(board[2]))
    print("-+-+-")
    print(str(board[3])+"|"+str(board[4])+"|"+str(board[5]))
    print("-+-+-")
    print(str(board[6])+"|"+str(board[7])+"|"+str(board[8]))

printboard()

m = 0 
possiblemove = []
wo = 0

while(True):
    if (m/2).is_integer() == True:
        v1 = int(input("Case: "))
        if board[v1-1] == ' ':
            board[v1-1] = "X"        
            m=m+1
            grid[v1-1] = 1
            printboard()
            winningX()
            isboardfull()
    if (m/2).is_integer() == False:
        m=m+1
        bot()
        printboard()
        winningO()
        isboardfull()