
# SHAMBHU THAPA 10677794  , DANIEL RAMIREZ 57298305

import connectfour
import my_connectfour

def user_interface()->None:
    ''' main part of the program that controls the game functionality'''
    print("Welcome to ConnectFour Game...\n")

    game =  connectfour.new_game()
    
    while True:
        my_connectfour.print_game_board(game)
        
        if(game.turn == 1):
            print("Player Red Turn")
        elif(game.turn == 2):
            print("Player Yellow Turn")

        column = my_connectfour.get_column()
        move  = my_connectfour.select_move()
        game = my_connectfour.handle_move(game,column, move)
        
        my_connectfour.winner = connectfour.winner(game)

        if my_connectfour.winner != 0:

            my_connectfour.print_game_board(game)
            my_connectfour.game_over(my_connectfour.winner)
            break


def player_turn(_game : 'connectfour.ConnectFourGameState') ->str:
    ''' returns the turn of the player'''
    return _game.turn

if __name__ == '__main__':
    
    user_interface()
    
    



