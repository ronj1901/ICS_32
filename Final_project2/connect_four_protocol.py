# SHAMBHU THAPA 10677794  , DANIEL RAMIREZ 57298305

# This module is a protocol for project 2 


import connectfour
import my_connectfour
import connectfour_console
import socket 
from collections import namedtuple

Connection = namedtuple(
        'Connection',
        ['socket', 'socket_input', 'socket_output'])

def create_connection(host:str, port:int)->Connection:
        ''' create a connection between the client and the server'''

        connect_socket = socket.socket()
        connect_socket.connect((host, port))
        connect_socket_input = connect_socket.makefile('r')
        connect_socket_output = connect_socket.makefile('w')

        return Connection(connect_socket, connect_socket_input, connect_socket_output)


        
def _login(connection: Connection, username:str) -> None:
        '''writes message to the server as the user is logged in '''

        send_message(connection, "I32CFSP_HELLO " +username)

def close_connection(connection: Connection) -> None:  
        ''' closes the connection'''

        connection.socket_input.close()
        connection.socket_output.close()
        connection.socket.close()


def send_message(connection: Connection, message: str) -> None:
        ''' sends message to the server'''

        connection.socket_output.write(message + '\r\n')
        connection.socket_output.flush()

def recv_message(connection: Connection) -> str:
        ''' receives messafe from the server '''

        return connection.socket_input.readline()[:-1]

def init_game(connection: Connection) ->None:
        ''' initiate the game by sending the message to the server '''

        send_message(connection, "AI_GAME")


    


