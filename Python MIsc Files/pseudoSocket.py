'''
pseudo_socket.py

This module allows you to use a simplified "socket" -- it's not really a socket,
however, the functionalities are very similar. You can connect to a PseudoSocket,
send messages to the PseudoSocket, and close the PseudoSocket. If the proper
protocol is not followed, the PseudoSocket raises a SocketError that can cause
your program to crash.

The proper protocol for a PsuedoSocket is as follows:
    -- connect to the Host 'ICS32_LARC' and the Port 42
    -- if the connection goes through, receive the message 'Connected!'
    -- send the message "Hello!"
    -- receive the message "Hello!"
    -- send any message other than an empty string or "quit", receive a movie quote
        -- sending an empty string or attempting to send to an unconnected socket raises a SocketError
        -- sending quit returns "EXIT" and raises a SocketError if the user attempts to send another message
    -- after closing the PseudoSocket, receive the message "Closed!"

'''



from random import randint

response = ["The name's Bond. James Bond.", "ET phone home.",
        "Go ahead, make my day.", "I am Groot", "I am Spartacus.",
        "I want to play a game...", "If you build it, they will come.",
        "If you are looking for ransom, I can tell you I don't have money. But what I do have are a very particular set of skills, skills I have acquired over a very long career. Skills that make me a nightmare for people like you.",
        "I'll be back.", "Just keep swimming.","Life is a box of chocolates, Forrest. You never know what you're gonna get.",
        "May the Force be with you.","Say hello to my little friend.",
        "To infinityâ€¦ and beyond!","Toto, I've a feeling we're not in Kansas anymore.",
        "Why so serious?","You go Glen Coco!", "Turn to page 394"]


class SocketError(Exception):
    pass

class PseudoSocket:
    connected = False
    socket_closed = True
    quitting = False
    message_count = 0



def connect(connect_tuple: (str,int)) -> str:
    '''
    attempts to connect to a PseudoSocket, raises SocketError if
    connection is not established
    '''
    host,port = connect_tuple
        
    if host == "ICS32_LARC" and port == 42:
        socket.connected = True
        return "Connected!"
    else:
        raise SocketError()


def send(message: str) -> str:
    '''
    sends a message through the PseudoSocket, raises a SocketError if
    the first message is not Hello! or if you attempt to send an empty
    string. if 'quit' is sent, returns the string 'EXIT' and if a message
    is sent after stating quit, raises a SocketError. Otherwise, returns
    a random movie quote as a response.
    '''
    if socket.message_count == 0 and socket.connected:
        if message != "Hello!":
            raise SocketError()
        else:
            socket.message_count += 1
            return "Hello!"
    
    elif not socket.connected or socket.quitting or message == "":
        raise SocketError()


    elif message.lower() == "quit":
        socket.quitting = True
        return "EXIT"
    
    else:
        return response[randint(0,len(response)-1)]

def close() -> str:
    '''
    Closes the PseudoSocket (returns variables to defaults)
    '''
    socket.socket_closed = True
    socket.connected = False
    socket.quitting = False
    socket.message_count = 0
    return "Closed!"


'''
create a socket so that by importing this module, you can simply
type pseudo_socket.connect() instead of having to instantiate an
instance of the class
'''
socket = PseudoSocket()




