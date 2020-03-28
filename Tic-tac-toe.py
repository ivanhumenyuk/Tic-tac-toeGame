# Game Board
board  = ['-', '-', '-',
          '-', '-', '-',
          '-', '-', '-',]

# IF game still going
game_still_going = True

# Who won? Who tie?
winner = None

# Who's turn is it
current_player = 'X'

# field for a plaing
def display_board():
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])

# main play function Tic-Tac-Toe
def play_game():
    display_board()

# While game is still going
    while game_still_going:
        # handle a single turn of an arbitrary player
        handle_turn(current_player)
        # check if game has ended
        check_if_g_over()
        # Flip to the other player
        flip_player()
# The game has ended
    if winner == 'X' or winner == 'O':
        print(winner + ' won.')
    elif winner == None:
        print("Tie.")

    # handle a single turn of an arbitrary player
def handle_turn(player):
    print (player +"'s turn.")
    position = input('Choose a position from 1-9:')

    valid = False
    while not valid:
        while position not in ['1', '2', '3', '4','5', '6', '7', '8', '9']:
            position = input('Invalid input. Choose a position from 1-9:')
        position = int(position) - 1
        if board[position] == "-":
            valid = True
        else:
            print("You can't go there. Go again")
    board[position] = player
    display_board()

def check_if_g_over():
    check_for_win()
    check_if_tie()

def check_for_win():
    # Set up global variables
    global winner
    #check_rows
    row_winner = check_rows()
    # check columns
    column_winner = check_columns()
    # check diagonals
    diagonal_winner = check_diagonals()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return

def check_rows():
    global game_still_going
    # check the rows same values
    row1 = board[0] == board[1] == board[2] != '-'
    row2 = board[3] == board[4] == board[5] != '-'
    row3 = board[6] == board[7] == board[8] != '-'
    if row1 or row2 or row3:
        game_still_going = False
    if row1:
        return board[0]
    if row2:
        return board[3]
    if row3:
        return board[6]
    return

def check_columns():
    global game_still_going
    # check the rows same columns
    column1 = board[0] == board[3] == board[6] != '-'
    column2 = board[1] == board[4] == board[7] != '-'
    column3 = board[2] == board[5] == board[8] != '-'
    if column1 or column2 or column3:
        game_still_going = False
    if column1:
        return board[0]
    if column2:
        return board[1]
    if column3:
        return board[2]
    return

def check_diagonals():
    global game_still_going
    # check the diagonals same columns
    diagonl1 = board[0] == board[4] == board[8] != '-'
    diagonl2 = board[2] == board[4] == board[6] != '-'
    if diagonl1 or diagonl2:
        game_still_going = False
    if diagonl1:
        return board[0]
    if diagonl2:
        return board[3]
    return

def check_if_tie():
    global game_still_going
    if '-' not in board:
        game_still_going = False

    return

def flip_player():
    global current_player

    if current_player == 'X':
        current_player='O'
    elif current_player == 'O':
        current_player ='X'
    return

play_game()
# logic:
    # board
    # display board
    # play game

    # check win
        # check rows
        # check columns
        # check diagonals
    # check tie
    # flip player