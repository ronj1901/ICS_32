

import tictactoe
# user interface
# DDIRections / Welcome
#the format the user should enter , how do you want your user to input

# print updated board
# ask for move  , switch player 
# Print winner
#exception Handling
# 
# 


## make  a new game stae 
_game = tictactoe.new_game()
board =  _game[2]



def print_board(board:[[str]]) -> None:
    '''
    prints TicTacToe board represented as 2D list to the console
    in the format board[column][row]
    '''

    for row in range(0,3):
        row_str = ''
        for col in range(0,3):
            row_str += board[col][row] + ' | '

        print(row_str[:-2])
        if row != 2:
            print('---------')

            
def get_move() ->tuple:
    ''' prompt the user to enter the move they wanna make'''
    print("Please enter two numbers:  ")
    x = int(input())
    y = int(input())
    
    return tuple(x,y)

print(get_move())

print_board(board)
get_move()
