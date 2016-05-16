import connectfour
import my_connectfour



def player_turn(_game : 'connectfour.ConnectFourGameState') ->str:
    ''' returns the turn of the player'''
    return _game.turn

def user_interface()->None:
    ''' main part of the program that controls the game functionality'''

    game =  connectfour.new_game()
    
    while True:
        my_connectfour.print_game_board(game)
        
        if(game.turn == 1):
            print("Player Red Turn")
        elif(game.turn == 2):
            print("Player Yellow Turn")
        print()

        column = my_connectfour.get_column()
        move  = my_connectfour.select_move()
        
        game = my_connectfour.handle_move(game,column, move)

        my_connectfour.winner = connectfour.winner(game)

        if my_connectfour.winner != connectfour.NONE:

            
            my_connectfour.print_game_board(game)
            my_connectfour.game_over()
            break

if __name__ == '__main__':
    
    user_interface()
    
    



