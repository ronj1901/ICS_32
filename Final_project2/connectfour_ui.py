# SHAMBHU THAPA 10677794  , DANIEL RAMIREZ 57298305


import connectfour
import connectfour_console
import my_connectfour
import connect_four_protocol
    
def user_interface() -> None:
    ''' handles the game and its interface '''
    
    host = get_host()
    port = get_port()
    
    connection = connect_four_protocol.create_connection(host, port)
    
    username = get_username()

    try:
        connect_four_protocol._login(connection,username)
        connect_four_protocol.recv_message(connection)
        connect_four_protocol.init_game(connection)
        connect_four_protocol.recv_message(connection)
        start_game(connection)
    finally:
        connect_four_protocol.close_connection(connection)


def client_turn(connection: connect_four_protocol.Connection, _game:connectfour.GameState) ->None:
     

    column = my_connectfour.get_column()
    move  = my_connectfour.select_move()

    _game = my_connectfour.handle_move(_game, column, move)

    give_turn_to_server(connection,move, column)
    return _game


def server_turn(connection:connect_four_protocol.Connection, _game:connectfour.GameState)  ->None:
 
    print("AI PLAYER PLAYING...")

    server_moves = connect_four_protocol.recv_message(connection)
    server_move = server_moves.split()
    server_move_type = server_move[0].lower()
    try:
        server_column = int(server_move[1])
        _game = my_connectfour.handle_move(_game, server_column, server_move_type)
        return _game
    except ValueError:
        return _game

def get_username()->str:
    ''' prompt the user to make a username'''
    while True: 
        username = input("Please enter username: ").strip()

        if len(username) > 1 and " " not in username:
            return username
        else:
            print("Please enter the username that is valid, no whitespace in between. ")



def give_turn_to_server(connection:connect_four_protocol.Connection,move:str, column:int) ->None:
    ''' alternate the player by giving turn to the server '''
           
    connect_four_protocol.send_message(connection,move.upper()+" "+str(column))



def get_host()->int:
    ''' get host from the player '''
    while True:
        host = input("Please enter the host: \n")
        if host == "":
            print("please enter a valid host")
        else:
            return host

def get_port() -> int:
    '''
    prompt the user to specify what port they'd like to connect to,
    continuing to ask until a valid answer is given.
    '''

    while True:
        try:
            port = int(input('Port: ').strip())

            if port < 0 or port > 65535:
                print('Ports must be an integer between 0 and 65535')
            else:
                return port

        except ValueError:
            print('Ports must be an integer between 0 and 65535')

def start_game(connection: connect_four_protocol.Connection,) -> None:
    ''' start the game and handle the move made by the players '''
    
    _game = connectfour.new_game()
    my_connectfour.print_game_board(_game)
    _game = client_turn(connection, _game)
    while True:
                
        winner = connectfour.winner(_game)
        if winner == 1:
            my_connectfour.print_game_board(_game)
            print('You (Red Player) won')
            break
        elif winner == 2:
            print('Player Yellow won')
            break
        else:
            my_connectfour.print_game_board(_game)
 
        AI_message = connect_four_protocol.recv_message(connection)

        if AI_message  == "OKAY":
            _new_game = server_turn(connection,_game)
            
            _game = _new_game
            my_connectfour.print_game_board(_game)

        AI_message = connect_four_protocol.recv_message(connection)

        if AI_message == "READY":
            print("Player red's turn ")
            _game = client_turn(connection, _game)
            print()



if __name__ == '__main__':
    
    user_interface()
   

            
