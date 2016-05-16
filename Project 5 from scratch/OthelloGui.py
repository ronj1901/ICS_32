from tkinter import *
import Othello

import math


class OthelloApplication:
    def __init__(self, gameState: Othello.Othello, winner :str):
        # creates a game board

        self._state = gameState

        self._state._new_game_board()

        self._root_window =Tk()

        self._root_window.configure(bg = 'black')
        self._root_window.title("WELCOME TO OTHELLO")

        self._score_frame  = Frame(master=self._root_window)

        self._white_text = StringVar()
        self._white_text.set('White:{}'.format(self._state.countPieces('W')))
        self._black_text = StringVar()
        self._black_text.set('Black:{}'.format(self._state.countPieces('B')))
        self._turn_text = StringVar()
        self._turn_text.set('Turn:{}'.format(self._state._turn))

        self._score_frame.grid(row=0,column=0,padx=10,pady=10,sticky= S + N)
        self._black=Label(master=self._score_frame,textvariable=self._black_text,font=('Helvetica',16))
        self._black.grid(row=0,column=0,padx=10,pady=10,sticky= W)
        self._turn=Label(master=self._score_frame,textvariable=self._turn_text,font=('Helvetica',16))
        self._turn.grid(row=0,column=1,padx=10,pady=10,)
        self._white=Label(master=self._score_frame,textvariable=self._white_text,font=('Helvetica',16))
        self._white.grid(row=0,column=2,padx=10,pady=10,)

        self._canvas = Canvas(
            master  = self._root_window, width = 600, height = 600,
            background = "green")
        self._counter = 0

        self._tiles = []

        self._winner = winner
        self._canvas.grid(
            row = 1, column = 0,  padx = 10, pady = 10,
            sticky = N + S + E + W)


        self._row=self._state._row
        self._col=self._state._col
        self._board=self._state._board
        self._canvas.bind('<Configure>', self._on_canvas_resized)
        self._canvas.bind('<Button-1>', self._on_canvas_clicked)
        self._score_frame.rowconfigure(0, weight = 1)
        self._score_frame.columnconfigure(0, weight = 0)
        self._score_frame.columnconfigure(1, weight = 0)
        self._score_frame.columnconfigure(2, weight = 0)
        self._root_window.rowconfigure(1,weight=1)
        self._root_window.columnconfigure(0, weight = 1)



    def start(self) -> None:

        self._root_window.mainloop()


    def _on_canvas_resized(self, event:Event) ->None:

        self._redraw_all_spots()

        



    def createBoard(self,row,col):
        # creates the new game board b


        width = self._canvas.winfo_width()
        height = self._canvas.winfo_height()
        spaceX=math.ceil(width/row)
        spaceY=math.ceil(height/col)
        for x in range((spaceX),width+spaceX,(spaceX)):
            self._canvas.create_line(x,0,x,height)               # neeed to change the code later

        for y in range((spaceY),height+spaceY,(spaceY)):
            self._canvas.create_line(0,y,width,y)


    def _on_canvas_clicked(self, event: Event) -> None:
        '''
        When the canvas is clicked, I get the event x and y location. Then from there, I keep andding or subtracting 1 until the
        The Spacing of X modded by the event x is = to 0. Same goes for the y. Once this happens, I know the coordinates of the top
        left and bottom right of the cell and am able to the create a move by converting the coordinates to a coordinate plane pixel and
        passing that into my game logic. O  nce the game logic runs,if it is a valid move, ill update my gui board, switch the score and
        check 2 future moves to see if there is a potential game over. I then append the tile to my self varialbe tiles to keep track of which locations have a tile.
        '''
        width = self._canvas.winfo_width()
        height = self._canvas.winfo_height()
        spaceX=math.ceil(width/self._row)
        spaceY=math.ceil(height/self._col)        
        y=int(event.x/spaceX)
        x=int(event.y/spaceY)
        y1=y+1
        x1=x+1
        move=self._state.place_piece(y,x)
        if(move!=False):
            self._redraw_all_spots()
            self._black_text.set('Black:{}'.format(self._state.countPieces('B')))
            self._white_text.set('White:{}'.format(self._state.countPieces('W')))
            self._turn_text.set('Turn:{}'.format(self._state._turn))
            self._counter=0
            
            if(self._state.getValidMoves()==[]):
                self._state._turn=self._state._opposite_turn()
                self._turn_text.set('Turn:{}'.format(self._state._turn))
                if(self._state.getValidMoves()==[]):
                    self.getWinner()



    
    def getWinner(self):
        '''
        gets the winner of the game and disables mouse clicks on the board.
        The text label on the top is updated to the final score of the game
        '''
        self._black_text.set("")
        self._white_text.set("")
        if(self._winner=='More'):
             self._turn_text.set(self._state.determineWinner())
             self._canvas.bind('<Button-1>', None)
        else:
            self._turn_text.set(self._state.determineWinnerLeast())
            self._canvas.bind('<Button-1>', None)


            
            
    def _redraw_all_spots(self) -> None:
        '''
        Redraws all of the spots on the grid.
        '''
        self._canvas.delete(ALL)
        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()
        self.createBoard(self._row,self._col)
        for x in range(len(self._state._board)):
            for y in range(len(self._state._board[0])):
                if(self._state._board[x][y]!=" "):
                    self._canvas.create_oval(x*(canvas_width/self._row),y*(canvas_height/self._col),(x+1)*(canvas_width/self._row),(y+1)*(canvas_height/self._col),fill=self.fillColor(self._state._board[x][y]))
                


    def fillColor(self,color:str):

        if color  == 'W':
            return 'White'
        else:
            return 'black'

##############################   Optioions Menu  ###################################
class inputs:
    def __init__(self):
        

        self._optionPane = Tk()
        self._optionPane.title("Settings of the game ")
##        self._optionPane.resizable(width=False,height=False)
##        
##        rows_label=Label(master=self._optionPane,text='How Many Rows?',font=('Helvetica',12))
##        rows_label.grid(row=1,column=0,padx = 10, pady = 10,
##            sticky = W)
##        cols_label=Label(master=self._optionPane,text='How Many Cols?',font=('Helvetica',12))
##        cols_label.grid(row=2,column=0,padx = 10, pady = 10,
##            sticky = W)
##        turn_label=Label(master=self._optionPane,text='Who Goes First?',font=('Helvetica',12))
##        turn_label.grid(row=3,column=0,padx = 10, pady = 10,
##            sticky = W)
##        corner_label=Label(master=self._optionPane,text='Which pieces starts in the top left?',font=('Helvetica',12))
##        corner_label.grid(row=4,column=0,padx = 10, pady = 10,
##            sticky = W)
##        winning_label=Label(master=self._optionPane,text='More pieces win,or less pieces win?',font=('Helvetica',12))
##        winning_label.grid(row=5,column=0,padx = 10, pady = 10,
##            sticky = W)
##        
##
##
            
        number=(4,6,8,10,12,16)
        turns=('B','W')
        winners=('More','Less')
        
        
        self._row=StringVar(self._optionPane)
        self._row.set(4)
        row_drop=OptionMenu(self._optionPane,self._row,*number)
        row_drop.pack()

        
        
        self._col=StringVar(self._optionPane)
        self._col.set(4)

        col_drop=OptionMenu(self._optionPane,self._row,*number)
        col_drop.pack()
        
        

        
        self._turn=StringVar(self._optionPane)
        self._turn.set("who goes first (Default B)")
        turn_drop=OptionMenu(self._optionPane,self._turn,*turns)
        turn_drop.pack()
        
        self._corner=StringVar(self._optionPane)
        self._corner.set("Which player will be on the top (default B)")
        corner_drop=OptionMenu(self._optionPane,self._corner,*turns)
        corner_drop.pack()

        
        self._winner=StringVar(self._optionPane)
        self._winner.set("Which winner wins (with more pieces / or with less )")
        winner_drop=OptionMenu(self._optionPane,self._winner,*winners)
        winner_drop.pack()

        self.doneButton = Button(self._optionPane , text='Lets play', command  = self.settings)
        self.doneButton.pack()

        self._optionPane.grid()

        self._optionPane.mainloop()



    def settings(self):
        self._row=(self._row.get())
        self._col=(self._col.get())
        self._turn=self._turn.get()
        self._corner=self._corner.get()
        self._winner=self._winner.get()
        self._optionPane.destroy()



if __name__ == '__main__':
    while True:
        temp=inputs()
        if not (temp._row=="" or temp._col=="" or temp._turn=="" or temp._corner==""):
            break           
    OthelloApplication(Othello.Othello(int(temp._col),int(temp._row),temp._turn,temp._corner,[]),temp._winner).start()




            
        
        
            

            


        
        
        
        
