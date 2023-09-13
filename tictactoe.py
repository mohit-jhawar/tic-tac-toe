#from IPython.display import clear_output
def display_board(board):
    #clear_output()
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])
def player_input():
    marker = ''
    while not (marker == 'X' and marker == 'O'):
        marker = input ('Player 1:Do you want to be X OR O?').upper()
        if marker == 'X':
            return ('X','O')
        else :
            return ('O','X')
def place_marker(board,marker,position):
    board [position]=marker
def win_check(board,mark):
    return ((board[1]==mark and board[2]==mark and board[3]==mark)or
           (board[4]==mark and board[5]==mark and board[6]==mark)or
           (board[7]==mark and board[8]==mark and board[9]==mark)or
           (board[1]==mark and board[4]==mark and board[7]==mark)or
           (board[2]==mark and board[5]==mark and board[8]==mark)or
           (board[3]==mark and board[6]==mark and board[9]==mark)or
           (board[1]==mark and board[5]==mark and board[9]==mark)or
           (board[3]==mark and board[2]==mark and board[7]==mark)
           )
import random 
def choose_first():
    if random.randint == 0:
        return 'player 2'
    else :
        return 'player 1'
def space_check(board,position):
    return board[position]==' '
def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True
def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input("Choose your next position:(1-9)"))
    return position
def replay():
    return input ("Do you want to play again?yes or no:").lower().startswith('y')
print("Welcome to TIC TAC TOE")
while True:
    the_board = [' ']*10
    player1_marker,player2_marker = player_input()
    turn = choose_first ()
    print(turn + ' will go first ')
    play_game = input("Are you ready to play game? Enter Yes or No")
    if play_game == 'Yes':
        game_on = True 
    else :
        game_on = False
    while game_on:
        if turn == 'Player 1':
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board,player1_marker,position)
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print("Congratulations! Player 1 have won the game!")
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("The game is draw!")
                    game_on = False
                else:
                    turn = 'Player 2'
        else:
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board,player2_marker,position)
            if win_check(the_board,player2_marker):
                display_board(the_board)
                print("Congratulations! Player 2 have won the game!")
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("The game is draw!")
                    game_on = False
                else:
                    turn = 'Player 1'
    if not replay():
        break
            