# Shambhu Thapa  10677794

import connectfour

_game = connectfour.new_game() 
game_winner  = connectfour.winner(_game)

def print_game_board(_game: 'connectfour.ConnectFourGameState') -> None:
    ''' Displays the game state as the game is running '''

    print()
    for i in range(connectfour.BOARD_COLUMNS):
        print(i+1, end = ' ')
    print()

    for row in range(connectfour.BOARD_ROWS):
        for col in range(connectfour.BOARD_COLUMNS):
            if _game.board[col][row] == connectfour.NONE:
                print('.', end = ' ')
            elif _game.board[col][row] == connectfour.RED:
                 print('R', end=' ')
            elif _game.board[col][row] == connectfour.YELLOW:
                 print('Y', end=' ') 
            else:
                print(_game.board[col][row], end =' ')
        print()
    print()

def get_column() ->int:
    ''' prompt the user to choose a desired column'''
    
    while True:
        try:
            column = int(input("Enter the desired column number:\n"))
            if column > 0  and column <= connectfour.BOARD_COLUMNS:
                return column
        
            else:
                print("Invalid input for column, please choose a valid column.")
        except:
            print("please input the column number that is integer")

def select_move()->str:
    ''' prompt the user to choose either drop or pop'''
    while True:
        
            move = input("Do you want to 'drop' or 'pop' ?\n")
            if move == 'drop' or move == 'pop' :
                return move
            else:
                print("Please choose either 'drop' or 'pop'. ")
        
            

def handle_move(_game :'connectfour.ConnectFourGameState', column:int, move:str)-> None:
    ''' handle the command regarding the moves taken bh players'''
    try:
        if move == 'drop':
            return connectfour.drop(_game,column-1)
        elif move == 'pop':
            return connectfour.pop(_game,column-1)
        else:
            print("the given input is not a valid input.")
    except connectfour.InvalidMoveError:
        print("invalid move")
        return _game 
def game_over()->None:
    ''' determines the winner of the game'''

    if winner == connectfour.RED:
            print('The winner is Red!')
           
    else:
            
            print('The winner is Yellow!')
        
         
