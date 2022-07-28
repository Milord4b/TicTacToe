# Code made by Miłosz Łyczywek
# print game board

import random
game_running= True
current_player="X"
winner = None

board=["-","-","-","-","-","-","-","-","-"]

def print_board():
    print("|"+board[0]+"|"+board[1]+"|"+board[2]+"|")
    print("|"+board[3]+"|"+board[4]+"|"+board[5]+"|")
    print("|"+board[6]+"|"+board[7]+"|"+board[8]+"|")


# player move


def player_move(board):
    move=int(input("Choose place from 1 to 9: "))
    if move>=1 and move<=9 and board[move-1]=="-":
        board[move-1]= current_player
    else:
        print("You did something wrong!")
        return False

# check win or tie
def horiz_check(board):
    global winner
    if board[0]== board[1]== board[2] and board[0]!="-":
        winner=board[0] 
        print("The winner is: "+board[0])
        return True
    elif board[3]== board[4]== board[5] and board[3]!="-":
        winner=board[3]
        print("The winner is: "+board[3])
        return True
    elif board[6]== board[7]== board[8] and board[6]!="-":
        winner=board[6]
        print("The winner is: "+board[6])
        return True

def row_check(board):
    global winner
    if board[0]== board[3]== board[6] and board[0]!="-":
        winner=board[0] 
        print("The winner is: "+board[0])
        return True
    elif board[1]== board[4]== board[7] and board[1]!="-":
        winner=board[1]
        print("The winner is: "+board[1])
        return True
    elif board[2]== board[5]== board[8] and board[2]!="-":
        winner=board[2]
        print("The winner is: "+board[2])
        return True

def diag_check(board):
    global winner
    if board[0]== board[4]== board[8] and board[0]!="-":
        winner=board[0] 
        print("The winner is: "+board[0])
        return True
    elif board[6]== board[4]== board[2] and board[6]!="-":
        winner=board[6]
        print("The winner is: "+board[6])
        return True

def check_tie(board):
    global game_running
    if "-" not in board:
        print("It's a tie!")
        game_running=False

def check_win():
    global game_running
    if horiz_check(board) or row_check(board) or diag_check(board)==True:
        game_running=False
# switch player

def switch_player():
    global current_player
    if current_player=="X":
        current_player="O"
    else:
        current_player="X"

# computer
    
    
def computer(board):
    global game_running
    while current_player=="O":
        position=random.randint(0,8)
        if board[position]=="-":
            board[position]="O"
            switch_player()   
                
# over

while game_running==True:
    
    player_move(board)
    print("Your move:")
    print_board()
    horiz_check(board)
    row_check(board)
    diag_check(board)
    check_tie(board)
    check_win()
    if game_running==False:
        break
    print("Computer's move:")
    switch_player()
    computer(board)
    print_board()
    horiz_check(board)
    row_check(board)
    diag_check(board)
    check_tie(board)
    check_win()
    
    