import connectfour
import connectfour_console
import my_connectfour
import connect_four_protocol



HOST = 'www.woodhouse.ics.uci.edu'
PORT = 5151

def user_interface() -> None:
    ''' handles the game and its inteface '''
    connection = connect_four_protocol.create_connection(HOST, PORT)
    username = get_username()

    try:
        connect_four_protocol._login(connection,username)
        print(connect_four_protocol.recv_message(connection))
        connect_four_protocol.init_game(connection)
        print(connect_four_protocol.recv_message(connection))
        start_game()
    finally:
        connect_four_protocol.close_connection(connection)


def start_game(connection: connect_four_protocol.connection) -> None:
    ''' start the game and handle the move made by the players '''            
    game = connectfour.new_game()
    connectfour.print_game_board(game)

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
        

'''
def client_turn(connection: connect_four_protocol.connection, _game) ->_game:
     

    column = my_connectfour.get_column()
    move  = my_connectfour.select_move()

    _game = my_connectfour.handle_move(_game, move, column)

    # give turn to the server

    give_turn_to_server(connection,move, column)

    
    return _game

'''


'''
def server_turn(connection:connect_four_protocol.connection, _game)  -> _game:
 

    print()
    print("player AI turn. ")

    server_move = connect_four_protocol.recv_message(connection).split()
    sever_move_type = server_move[0].upper()
    try:
        server_column = int(server_move[1])
    except ValueError:
        return _game
    if (sever_move_type == 'DROP' or 'POP') and (server_column > 0 and server_column <connectfour.BOARD_COLUMNS):
        _game = my_connectfour.handle_move(_game, server_column, sever_move_type)
        return _game
    else:
        return _game
'''    
    


def get_username()->str:
    ''' prompt the user to make a username'''
    while True: 
        username = input(" Please enter username: ")

        if len(username) > 1 and username != " ":
            return username
        else:
            print("Please enter the username that is valid, no whitespace in between. ")


def handle_command(connection: connect_four_protocol.connection, game )->bool:
    
    ''' checks whether the user command is valid or not '''
    pass        

     

    
def drop_it(connection:connect_four_protocol.connection, game )->None:
    ''' handle the game when the drop command is made by the player'''

    pass

def give_turn_to_server(connection:connect_four_protocol.connection,move, column) ->None:
    ''' alternate the player by giving turn to the server '''
    print(move.upper()+" "+str(column))           
    #connect_four_protocol.send_message(connection,move.upper()+" "+str(column))
    
        
    

if __name__ == '__main__':
    
    
    user_interface()
   

            
