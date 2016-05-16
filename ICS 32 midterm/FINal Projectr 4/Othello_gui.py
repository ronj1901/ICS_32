'''
 
 Project 5
 Othello GUI
 '''


import tkinter
import Othello
import math

##class OthelloGame:
##
##    def __init__(self, game: Othello.Othello, winner :str):
##        '''
##
##        Initializes the game board, and prepares the menu  to the user
##        , update the score of the board
##
##        '''
##
##        self._state = game
##        self._state._game_board()   # creates a new game board size
##        


root_window = tkinter.Tk()
root_window.title("GAME OF OTHELLO")
root_window.configure(bg = 'black')
# score_frame   begins here 
score_frame = tkinter.Frame(master = root_window, bg = "orange")
white_text = tkinter.StringVar()
white_text.set('WHITE :  500 ')

black_text = tkinter.StringVar()
black_text.set('BLACK : 263')

turn_frame = tkinter.Frame(master = root_window)
turn_text = tkinter.StringVar()

turn_text.set("TURN :    PLAYER HARRIS T.")

score_frame.grid(row = 0, column = 0, padx = 15, pady = 15, sticky = tkinter.S + tkinter.N, )



black = tkinter.Label(master = score_frame, textvariable = black_text,  bg = "magenta", font = ('Helvetica', 18))
black.grid(row = 1, column = 0,padx = 15, pady = 15, sticky = tkinter.W)

white = tkinter.Label(master = score_frame, textvariable = white_text, bg = "green",font = ('Helvetica', 18))
white.grid(row = 2, column = 0 ,padx = 15, pady = 15, sticky = tkinter.W)

turn = tkinter.Label(master = score_frame, textvariable = turn_text, bg = "red", font = ('Helvetica', 18))
turn.grid(row = 1, column = 5, rowspan = 3,columnspan = 3, padx = 15, pady =  15)



# score_board ends


# canvas begins here

canvas = tkinter.Canvas(
    master = root_window, width = 600, height = 600, bg = "yellow")

canvas.grid(
    row = 1, column = 0, padx = 10, pady = 10,
    sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)



score_frame.rowconfigure(0, weight = 1)
score_frame.columnconfigure(0, weight = 0)
score_frame.columnconfigure(1, weight = 0)
score_frame.columnconfigure(2, weight = 0)
root_window.rowconfigure(1,weight=1)
root_window.columnconfigure(0, weight = 1)

def _on_canvas_sized():
    print("Canvas Resized")

def _on_canvas_clicked():
    print("mouse button was clicked")


# Draw board
row  = 8

col = 8

width = canvas.winfo_width()
height = canvas.winfo_height()

spaceX=math.ceil(width/row)
spaceY=math.ceil(height/col)
for x in range((spaceX),width+spaceX,(spaceX)):
    canvas.create_line(x,0,x,height, fill = "black")
for y in range((spaceY),height+spaceY,(spaceY)):
    canvas.create_line(0,y,width,y, fill= "black")
 

# canvas ends here
root_window.mainloop()


