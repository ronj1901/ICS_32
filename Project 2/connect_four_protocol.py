# This module is a protocol for project 2 
#ICS 32 : send me on my way 


import socket 
from collections import namedtuple

connection = namedtuple(						# making a  connection object
	'connection',
	['socket', 'socket_input', 'socket_output'])


def create_connection(host :str , port :int) -> connection:

	''' create a connection and make a pseudo file object '''

	connect_socket =  socket.socket()

	connect_socket.connect((host, port))   # connects a socket 

	connect_socket_input = connect_socket.makefile('r')   # creates a pseudofile object for input

	connect_socket_output = connect.socket.makefile('w') # creates a pseudo dile object for output
	return connection(connect_socket , connect_socket_input,connect_socket_output) 


def close_connection(connection: connection) -> None:                   # closes connection 
        ''' closes the connection'''

        connection.socket_input.close()
        connection.socket_output.close()
        connection.socket.close()


def send_message(connection: connection, message: str) -> None:
        ''' sends message to the server'''

        write_line(connection, message)


def recv_message(connection: connection) -> str:
        ''' receives messafe from the server '''

        return connection.socket_input.readline()[:-1]

def init_game(connection: connection) ->None:
        ''' initiate the game by sending the message to the server '''

        send_message(connection, "AI GAME")
        
def _login(connection: connection, username:str) -> None:
        ''' writes message to the server as the user is logged in '''

        send_message(connection, "I32CFSP_HELLO" + username)

def write_line(connection: connection, line:str) -> None:
        ''' writes a line to the server and along with newline sequence '''

        
        connection.socket_output.write(message + '\r\n')
        connection.socket_output.flush()
        

def _expect_line(connection: connection, expected : str) -> bool:
        ''' checks whether the  line send to the server contains exact and expected line'''

        line = recv_messsage(connection)
        if line == 'WINNER_RED' or line == 'WINNER_YELLOW':

                return True
        else:
                return False
        

 
class serverError(Exception):
    '''Raised when server is not ready'''
    pass                
                 


