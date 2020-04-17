"""
Tic Tac Toe Player
"""

import math
import copy
import itertools

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]
    

def player(board):
    """
    Returns player who has the next turn on a board.
    """
    Xinboard = sum(row.count('X') for row in board)
    Oinboard = sum(row.count('O') for row in board)

    if terminal(board) :
       return EMPTY
    elif Xinboard > Oinboard : 
    #if Xinboard > Oinboard :
        return O
    else :
        return X
    

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    action_set = set()
    i=0
    for row in board :
        j=0
        for cell in row :
            if cell == EMPTY :
                print("in cell")
                print((i,j))
                action_set.add((i,j))
                print(action_set)
            j+=1 
        i+=1    
    return action_set


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board) :
        raise Exception("Wrong Action !")
    else :
        #keeping original intact
        newboard = copy.deepcopy(board)
        #finding player whose turn it is
        player_turn = player(board)
        #passing action to newboard state
        (row,cell) = action
        #newboard state
        newboard[row][cell] = player_turn
    
    return newboard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #make a working copy of board
    board_C = copy.deepcopy(board)
    L = len(board_C)
    #8 cases where we can win
    #3 vertical, 3 horizontal and 2 diagonal
    #Horizontal cases
    for row in board_C : 
           Xinrow = sum(x is X for x in row)
           #print(Xinrow)
           Oinrow = sum(o is O for o in row)
           #print(Oinrow)
           if Xinrow == 3 :
               #print(("Row Winner"))
               return X   
           if Oinrow == 3 :
               #print(("Row Winner"))
               return O

    #Vertical cases
    #transpose board_copy using list comprehension
    board_CT = [[board_C[j][i] for j in range(L)] \
                for i in range(L)]
    #print(board_CT)
    for col in board_CT : 
           Xincol = sum(x is X for x in col)
           #print(Xincol)
           Oincol = sum(o is O for o in col)
           #print(Oincol)
           if Xincol == 3 :
               #print(("Column Winner"))
               return X   
           if Oincol == 3 :
               #print(("Column Winner"))
               return O

    #Diagonal cases
    diag1  = [board_C[r][r] for r in range(L)]
    #print(diag1)
    diag2  = [board_C[L-1-r][r] for r in range(L)] 
    #print(diag2)
    Xindiag1 = sum(x is X for x in diag1)
    Oindiag1 = sum(o is O for o in diag1)
    if Xindiag1 == 3 :
               #print(("Diag1 Winner"))
               return X   
    if Oindiag1 == 3 :
               #print(("Diag1 Winner"))
               return O
    Xindiag2 = sum(x is X for x in diag2)
    Oindiag2 = sum(o is O for o in diag2)
    if Xindiag2 == 3 :
               #print(("Diag2 Winner"))
               return X   
    if Oindiag2 == 3 :
               #print(("Diag2 Winner"))
               return O

    #Tie
    #print("No Winner") 
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    #Somebody wins, game over
    if winner(board) != None :
        return True
    else:
    
        for row in board :
          for cell in row :
            if cell == EMPTY :
                return False
    return True
    
   
def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board) == True :
        game_winner = winner(board)
        if game_winner == X:
            return 1
        elif game_winner == O:
            return -1
        else :
            return 0
    else :
        return None


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """


#using pusedocode
def MAXValue(board) :
    #checking if game is over
    if terminal(board) :
        return utility(board)
    #initial value as low as possible
    v = float("-inf")
    #actions in a state
    for action in actions(board):
        #best that min player can do comes from MINValue()
        v = max(v,MINValue(result(board,action)))
    return v

def MINValue(board) :
    #checking if game is over
    if terminal(board) :
        return utility(board)
    #initial value as high as possible
    v = float("inf")
    #actions in a state
    for action in actions(board):
        #best that max player can do is given by MAXValue()
        v = min(v,MAXValue(result(board,action)))
    return v

    

