#
# Author: Rakan AlZagha
# Date: 4/12/2021
#
# Assignment: Project #2
# Comments: 
#

# library to represent infinity in minimax
import math

# global variables/game representation for use by all functions
player_representation = 'O'
program_representation = 'X'

# TTT is represented by a dictionary of 9 elements
game = {1: '_', 2: '_', 3: '_',
        4: '_', 5: '_', 6: '_',
        7: '_', 8: '_', 9: '_'}

#
# Function: main
# Purpose: drive the TTT game
# Parameters: N/A
#

def main():
    global player_representation, program_representation, game
    print("Welcome to TTT! Would you like to go first ('Y' or 'N')?")
    player_decision = (input("--> "))

    if(player_decision == "Y"): # player goes first
        print("Your move first! Please choose if you want to be X or O ('X' or 'O'):")
        player_representation = (input("--> "))
        if(player_representation == 'X'):
            program_representation = 'O'
        elif(player_representation == 'O'):
            program_representation = 'X'
        else:
            print("Unknown character!\n")
            exit()

    elif(player_decision == "N"): # bot goes first
        print("Computer's move!")
        player_representation = 'O'
        program_representation = 'X'
    
    else: # command unknown, quit game 
        print("Unknown command!")
        exit()

    # dictionary representation of game
    game = {1: '_', 2: '_', 3: '_',
            4: '_', 5: '_', 6: '_',
            7: '_', 8: '_', 9: '_'}

    print("Here are the board positions:\n\n1\t2\t3\n4\t5\t6\n7\t8\t9\n")
    while not (game_win()): # terminates only when game won by either party
        if(player_decision == 'Y'):
            turns(is_user = True) # user goes first
            turns(is_user = False)
        else:
            turns(is_user = False) # user goes second
            turns(is_user = True)

#
# Function: print_game()
# Purpose: print dictionary representation of TTT
# Parameters: game
#

def print_game(game):
    print(game[1] + ' | ' + game[2] + ' | ' + game[3])
    print('----------')
    print(game[4] + ' | ' + game[5] + ' | ' + game[6])
    print('----------')
    print(game[7] + ' | ' + game[8] + ' | ' + game[9])
    print()

#
# Function: valid_move()
# Purpose: determine if space on board is available
# Parameters: board_position
#

def valid_move(board_position):
    if(game[board_position] != '_'): # if something is found at curr pos
        return 0
    else:
        return 1

#
# Function: game_draw()
# Purpose: determine if game ended in a draw
# Parameters: N/A
#

def game_draw():
    for i in game:
        if(game[i] == '_'): # more moves are possible
            return 0
    return 1

#
# Function: game_win()
# Purpose: determine if current board has any combinations of a win
# Parameters: N/A
#

def game_win():
    # diagonals
    if (game[1] == game[5] and game[1] == game[9] and game[1] != '_'):
        win = True
    elif (game[7] == game[5] and game[7] == game[3] and game[7] != '_'):
        win = True
    # rows
    elif (game[1] == game[2] and game[1] == game[3] and game[1] != '_'):
        win = True
    elif (game[4] == game[5] and game[4] == game[6] and game[4] != '_'):
        win = True
    elif (game[7] == game[8] and game[7] == game[9] and game[7] != '_'):
        win = True
    # columns
    elif (game[1] == game[4] and game[1] == game[7] and game[1] != '_'):
        win = True
    elif (game[2] == game[5] and game[2] == game[8] and game[2] != '_'):
        win = True
    elif (game[3] == game[6] and game[3] == game[9] and game[3] != '_'):
        win = True
    else:
        win = False
    return win

#
# Function: winner()
# Purpose: determine from a given possibilities who the winner would be
# Parameters: representation
#

def winner(representation):
    # diagonals
    if (game[1] == game[5] and game[1] == game[9] and game[1] == representation):
        winner = True
    elif (game[7] == game[5] and game[7] == game[3] and game[7] == representation):
        winner = True
    # rows
    elif game[1] == game[2] and game[1] == game[3] and game[1] == representation:
        winner = True
    elif (game[4] == game[5] and game[4] == game[6] and game[4] == representation):
        winner = True
    elif (game[7] == game[8] and game[7] == game[9] and game[7] == representation):
        winner = True
    # columns
    elif (game[1] == game[4] and game[1] == game[7] and game[1] == representation):
        winner = True
    elif (game[2] == game[5] and game[2] == game[8] and game[2] == representation):
        winner = True
    elif (game[3] == game[6] and game[3] == game[9] and game[3] == representation):
        winner = True
    else:
        winner = False
    return winner

#
# Function: status()
# Purpose: determine if a win or draw exists and exit game
# Parameters: representation
#

def status(representation):
    if(game_draw() == 1): # draw
        print("Draw between computer and user!")
        exit_game()
    if(game_win() == True): # game win
        if(representation == player_representation):
            print("User wins!")
            exit_game()
        else:
            print("Computer wins!")
            exit_game()

#
# Function: exit_game()
# Purpose: terminate game at end condition in status()
# Parameters: N/A
#

def exit_game():
    exit()

#
# Function: make_move()
# Purpose: place move onto TTT board
# Parameters: representation, board_position
#

def make_move(representation, board_position):
    if(valid_move(board_position) == 1): # valid move
        game[board_position] = representation # assign move to board position
        print_game(game) # print curr version of game
        status(representation) # did this move result in a termination condition
    else:
        print("Unable to perform that move, position is occupied! Pleast try again.") # space is filled
        board_position = int(input("Enter a position: "))
        make_move(representation, board_position)

#
# Function: turns()
# Purpose: take user input for a move and maximize comp plays (using minimax)
# Parameters: is_user
#

def turns(is_user):
    if(is_user): # users turn
        board_position = int(input("Enter a position: "))
        if(board_position >= 1 and board_position <= 9):
            make_move(player_representation, board_position)
        else:
            board_position = print("Out of bounds!")
            exit()
    else: # bots turn...minimax implementation
        max_eval = -math.inf
        for i in game:
            if(game[i] == '_'):
                game[i] = program_representation
                evaluation = minimax(game, max_player = False)
                game[i] = '_'
                maximum = max(evaluation, max_eval) # take max of two variables
                if(maximum != max_eval): # check if it is the same value or not
                    max_eval = evaluation
                    position = i # best move
        make_move(program_representation, position) # take the move on the board

#
# Function: term_test()
# Purpose: determine if next move results in a termination of the game 
# Parameters: game
#

def term_test(game):
    if(winner(program_representation)):
        return 1
    elif(winner(player_representation)):
        return -1
    elif(game_draw()):
        return 0
    else: #continue game, no condition reached successfully
        return 'CONTINUE'

#
# Function: minimax()
# Purpose: determine what the most effective move is using minimax
# Parameters: game, max_player
#

def minimax(game, max_player): 
    if(term_test(game) != 'CONTINUE'): # no terminating condition was met
        return(term_test(game))
    elif(max_player == 1): # maximizing player
        max_eval = -math.inf # -infinity
        for i in game:
            if(game[i] == '_'): # make sure square is empty
                game[i] = program_representation # test move
                evaluation = minimax(game, max_player = False) # recursion
                game[i] = '_' # reset square
                maximum = max(evaluation, max_eval) # take max
                if(maximum != max_eval):
                    max_eval = evaluation
        return max_eval
    else: # minimizing player
        min_eval = math.inf # infinity
        for i in game:
            if(game[i] == '_'): # make sure square is empty
                game[i] = player_representation # test move
                evaluation = minimax(game, max_player = True) # recursion
                game[i] = '_' # reset square
                minimum = min(evaluation, min_eval) # take min
                if(minimum != min_eval):
                    min_eval = evaluation
        return min_eval

if __name__ == "__main__":
    main()
