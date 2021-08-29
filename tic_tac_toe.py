''' Tic Tac Toe Game using Python '''

# The Game Board which stores X and O at position specified by user
# '-' indicates empty position
game_board = ['-','-','-',
         '-','-','-',
         '-','-','-']

# Tells whether game is over yet or not
game_still_going = True

# Store the winner, if any otherwise stores None
winner = None

# Store the current player i.e X or O, starting player being X
current_player = 'X'


# Begin the Tic Tac Toe game
def play_game():
    
    # Display the initial game board
    display_board()
    
    # Loop while the game is still going on i.e not ended or resulted in a win or a tie
    while game_still_going:
        
        # Handles a turn of the current player
        handle_turn(current_player)
        
        # Checks if there is a winner or a tie yet
        check_if_game_over()
        
        # Flips the turn to other player
        flip_player()
        
    # Display result after the game has ended
    if(winner=='X' or winner=='O'):
        print(winner+" won!")
    else:
        print("Tie.")


# Displays the current game board
def display_board():
    print("\n")
    print(game_board[0]+' | '+game_board[1]+' | '+game_board[2])
    print("---------")
    print(game_board[3]+' | '+game_board[4]+' | '+game_board[5])
    print("---------")
    print(game_board[6]+' | '+game_board[7]+' | '+game_board[8])
    print("\n")


# Handles a turn of the current player
def handle_turn(player):
    
    print("\n"+current_player+"'s turn..")
    
    # To check if entered position is valid and not taken already
    valid = False
    
    # Loop while a valid position is not entered
    while not valid:
        
        position = input("Enter a position from 1 to 9 : ")
        
        # Check if entered position is valid or not
        while position not in ['1','2','3','4','5','6','7','8','9'] :
            position = input("Invalid position!\nEnter a position from 1 to 9 : ")

        position = int(position)-1;
        
        # Check if entered postion is already filled or not
        if(game_board[position]=='-'):
            valid=True
        else:
              print("Entered position already taken! Choose another.")

    # Update the game board and display it        
    game_board[position] = player
    display_board()


# checks if the game is over i.e. if there is a win or a tie yet
def check_if_game_over():
    check_for_winner()
    check_if_tie()
  
    
# checks if there is a win
def check_for_winner():
    
    global winner
    
    # check rows
    row_winner = check_rows()
    
    # check columns
    column_winner = check_columns()
    
    # check diagonals
    diagonal_winner = check_diagonals()
    
    if(row_winner):
        winner = row_winner
    elif(column_winner):
        winner = column_winner
    elif(diagonal_winner):
        winner = diagonal_winner
    else:
        winner = None


def check_rows():

    global game_still_going
    
    #check if any row has same value and it is not empty
    row_1 = game_board[0] == game_board[1] == game_board[2] != '-'
    row_2 = game_board[3] == game_board[4] == game_board[5] != '-'
    row_3 = game_board[6] == game_board[7] == game_board[8] != '-'
    
    if row_1 or row_2 or row_3:
        game_still_going = False
    
    # Returns the winner X or O or none if there is no winner
    if row_1:
        return game_board[0]
    elif row_2:
        return game_board[3]
    elif row_3:
        return game_board[6]
    else:
        return None
    
    
def check_columns():

    global game_still_going
    
    #check if any row has same value and it is not '-'
    column_1 = game_board[0] == game_board[3] == game_board[6] != '-'
    column_2 = game_board[1] == game_board[4] == game_board[7] != '-'
    column_3 = game_board[2] == game_board[5] == game_board[8] != '-'
    
    if column_1 or column_2 or column_3:
        game_still_going = False
    
    # Returns the winner X or O or none if there is no winner
    if column_1:
        return game_board[0]
    elif column_2:
        return game_board[1]
    elif column_3:
        return game_board[2]
    else:
        return None


def check_diagonals():
    
    global game_still_going
    
    #check if any diagonal has same value and it is not '-'
    diagonal_1 = game_board[0] == game_board[4] == game_board[8] != '-'
    diagonal_2 = game_board[2] == game_board[4] == game_board[6] != '-'
    
    if diagonal_1 or diagonal_2:
        game_still_going = False;
    
    # Returns the winner X or O or none if there is no winner
    if diagonal_1:
        return game_board[0]
    elif diagonal_2:
        return game_board[2]
    else:
        return None


# Check if there is a tie
def check_if_tie():
    
    global game_still_going
    
    # '-' indicates empty postion, if it is not in game board then all the positions must have been filled
    if '-' not in game_board:
        game_still_going = False


# Flips the turn to other player
def flip_player():
    
    global current_player
    
    if(current_player == 'X'):
        current_player = 'O'
    else:
        current_player = 'X'
        
# Function call to begin the game of Tic Tac Toe
play_game()
input("Press enter to exit.")