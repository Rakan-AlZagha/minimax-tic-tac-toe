# minimax_tic_tac_toe

This project is part of a programming assignment for the Artificial Intelligence course taught at Trinity College-Hartford.

We were tasked to write an implementation of Tic-Tac-Toe using MINIMAX algorithm.

## Tic-Tac-Toe Game Description
Tic-Tac-Toe is played on a 3 x 3 grid. The two players are X and O. X always goes first. On each turn, a player
marks its letter (X or O) on an empty square of the grid. The game ends when either:
(a) one player has succeeded in filling a row, column, or diagonal with its letter, or
(b) as a tie when there are no more empty squares and neither player has won.


We’ll consider the score to be +1 for a win, -1 for a loss, and 0 for a draw.
Your program will be X and the user will play O. On each turn, your program will
(a) Run MINIMAX to determine the best move for X and update the game accordingly
(b) Prompt the user for its turn and update the game accordingly

Everything worked with all of my test conditions. 

## Compilation and Input
Compilation and input is standard, you will be prompted with a question if you would like to choose X or O for your representation. 

Inputting 'Y' for yes and 'N' for no is valid input. 

If N: simply input your next move 1-9

If Y: choose 'X' or 'O' then simply input your next move 1-9

## General Comments

1) Chose to represent the game as a dictionary in Python for simplicity of code and ability to represent board from 1:9 vs 0:8 and string representation

## Algorithm Utilized
function MINIMAX(state, maxPlayer)
// state is current grid; Boolean maxPlayer true when X’s turn
if TERM-TEST(state)
 return VALUE(state)
else if MaxPlayer
 maxEval ← -∞
 for each child c of state
 eval ← MINIMAX(c, false)
 maxEval ← max(maxEval, eval) // also need to track maxMove
 return maxEval
else
 minEval ← ∞
 for each child c of state
 eval ← MINIMAX(c, true)
 minEval ← min(minEval, eval)
 return minEval


