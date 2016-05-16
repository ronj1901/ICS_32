
# Shambhu Thapa 10677794
# Project 5  Othello Gui


import tkinter
import Othello
import math


DEFAULT_FONT = ('Helvetica, 16')


class Othello_Game:
    def __init__(self,game:Othello.Othello,winner:str):
        '''
        Default  constructor  , initializes the game board in gui
        '''
        self._state = game
       
        self._state.game_board()

        self.roow_window = tkinter.Tk()
        self.roow_window.title("OTHELLO")
        self.roow_window.configure(bg='#002222')
        self.score_board=tkinter.Frame(master=self.roow_window)

        self.white = tkinter.StringVar()
        self.white.set('WHITE : {}  '.format(self._state.get_count('W')))
        self.black = tkinter.StringVar()
        self.black.set('BLACK : {}  '.format(self._state.get_count('B')))
        self._turn_text = tkinter.StringVar()
        self._turn_text.set('Turn:{}' .format(self._state._turn))

        self.score_board.grid(row=10,column=2,padx=10,pady=10,sticky=tkinter.S+tkinter.N)
        self.score_board.config(bg="BLACK")

        self._black=tkinter.Label(master=self.score_board,textvariable=self.black,font=DEFAULT_FONT)
        self._black.config(bg="ORANGE",foreground="WHITE")
        self._black.grid(row=2,column=4,padx=10,pady=10,sticky=tkinter.W)

        self._turn=tkinter.Label(master=self.score_board,textvariable=self._turn_text,font=DEFAULT_FONT)
        self._turn.grid(row=4,column=2,padx=10,pady=10,)
        self._turn.config(bg="ORANGE",foreground="BLUE")

        self._white=tkinter.Label(master=self.score_board,textvariable=self.white,font=DEFAULT_FONT)
        self._white.grid(row=2,column=1,padx=10,pady=10,)
        self._white.config(bg="ORANGE",foreground="BLACK")

        x = tkinter.Label(self.score_board,text="OTHELLO",foreground="WHITE",font=DEFAULT_FONT)
        x.grid(row=0,column=2,padx=10,pady=10,)
        x.config(bg="ORANGE",foreground="WHITE")

        w = tkinter.Label(self.roow_window,text="WELCOME TO THE GAME OF OTHELLO",foreground="WHITE")
        w.grid(row=0,column=4,padx=10,pady=10,)
        w.config(bg="WHITE",foreground="BLUE")
        
        
        self._canvas = tkinter.Canvas(
            master = self.roow_window, width = 600, height = 600,
            background = '#006222')

        self._counter=0
        self._tiles=[]
        self._winner=winner
        self._canvas.grid(
            row = 10, column = 6, padx = 10, pady = 10,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)
        self._row=self._state._row
        self._col=self._state._col
        self._board=self._state._board
        self._canvas.bind('<Configure>', self._on_canvas_resized)
        self._canvas.bind('<Button-1>', self._on_canvas_clicked)
        self.score_board.rowconfigure(0, weight = 1)
        self.score_board.columnconfigure(0, weight = 0)
        self.score_board.columnconfigure(1, weight = 0)
        self.score_board.columnconfigure(2, weight = 0)
        self.roow_window.rowconfigure(1,weight=1)
        self.roow_window.columnconfigure(0, weight = 1)
    
    def start(self) -> None:
        '''
         start the tkinter window
        '''
        self.roow_window.mainloop()

    def _on_canvas_resized(self, event: tkinter.Event) -> None:
        '''
        on resizing it ,it maintains the ratio all of the discs 
        '''
        self._redraw_all_spots()

    def print_board(self,row,col):
        '''
        create a game board with given numbers of rows and cols
        '''
        self._canvas
        width = self._canvas.winfo_width()
        height = self._canvas.winfo_height()
        rowX=math.ceil(width/row)
        colY=math.ceil(height/col)
        for x in range((rowX),width+rowX,(rowX)):
            self._canvas.create_line(x,0,x,height)
        for y in range((colY),height+colY,(colY)):
            self._canvas.create_line(0,y,width,y)
        
        
    def _on_canvas_clicked(self, event: tkinter.Event) -> None:
        '''
         handle the move made my the players and update the board
        '''
        width = self._canvas.winfo_width()
        height = self._canvas.winfo_height()
        rowX=math.ceil(width/self._row)
        colY=math.ceil(height/self._col)        
        y=int(event.x/rowX)
        x=int(event.y/colY)
        y1 = y+1
        x1 = x+1
        move=self._state.plug_piece(y,x)
        if(move != False):
            self._redraw_all_spots()
            self.black.set('Black:{}'.format(self._state.get_count('B')))
            self.white.set('White:{}'.format(self._state.get_count('W')))
            self._turn_text.set('Turn:{}'.format(self._state._turn))
            self._counter=0
            if(self._state.getValidMoves()==[]):
                self._state._turn=self._state.switch_turn()
                self._turn_text.set('Turn:{}'.format(self._state._turn))
                if(self._state.getValidMoves()==[]):
                    self.find_winner()

    def find_winner(self):
        '''
         get who won the game
        '''
        self.black.set("")
        self.white.set("")
        if(self._winner=='More'):
             self._turn_text.set(self._state.winner_more())
             self._canvas.bind('<Button-1>', None)
        else:
            self._turn_text.set(self._state.winner_less())
            self._canvas.bind('<Button-1>', None)
    
    def _redraw_all_spots(self) -> None:
        '''
        Redraws all of the spots on the board.
        '''
        self._canvas.delete(tkinter.ALL)
        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()
        self.print_board(self._row,self._col)
        for x in range(len(self._state._board)):
            for y in range(len(self._state._board[0])):
                if(self._state._board[x][y]!=" "):
                    self._canvas.create_oval(x*(canvas_width/self._row),y*(canvas_height/self._col),(x+1)*(canvas_width/self._row),(y+1)*(canvas_height/self._col),fill=self.color_switch(self._state._board[x][y]))
  
    def color_switch(self,color:str):
        '''
        switch the color in the board
        '''
        if(color=='W'):
            return 'white'
        else:
            return 'black'

class game_menu:
    def __init__(self):
        '''
        Let the user show the game settings and grab the data from the set
        '''
        
        self.welcome_menu=tkinter.Tk()
        self.welcome_menu.title("Options")
        self.welcome_menu.resizable(width=False,height=False)


        rows_label=tkinter.Label(master=self.welcome_menu,text='How Many Rows?',font=DEFAULT_FONT)
        rows_label.grid(row=1,column=0,padx = 10, pady = 10,
            sticky = tkinter.W)
        rows_label.config(bg="BLUE",foreground="WHITE")
        cols_label=tkinter.Label(master=self.welcome_menu,text='How Many Cols?',font=DEFAULT_FONT)
        cols_label.grid(row=2,column=0,padx = 10, pady = 10,
            sticky = tkinter.W)

        cols_label.config(bg="GREEN",foreground="RED")

        turn_label=tkinter.Label(master=self.welcome_menu,text='Who Goes First?',font=DEFAULT_FONT)
        turn_label.grid(row=3,column=0,padx = 10, pady = 10,
            sticky = tkinter.W)
        turn_label.config(bg="BLACK",foreground="WHITE")

        corner_label=tkinter.Label(master=self.welcome_menu,text='Which pieces starts in the top left?',font=DEFAULT_FONT)
        corner_label.grid(row=4,column=0,padx = 10, pady = 10,
            sticky = tkinter.W)
        corner_label.config(bg="#FF8000",foreground="BLACK")

        winning_label=tkinter.Label(master=self.welcome_menu,text='More pieces win,or less pieces win?',font=DEFAULT_FONT)

        winning_label.config(bg="#FF8000",foreground="BLACK")

        winning_label.grid(row=5,column=0,padx = 10, pady = 10,
            sticky = tkinter.W)
        ok_Button=tkinter.Button(master=self.welcome_menu,text='Done ',command=self.validate_Data)
        ok_Button.config(bg="GREEN",foreground="yellow",background='green',height=1,width=5)
        ok_Button.grid(row=6,columnspan=2,padx=10,pady=10)

        self._row=tkinter.StringVar(self.welcome_menu)
        self._col=tkinter.StringVar(self.welcome_menu)
        self._turn=tkinter.StringVar(self.welcome_menu)
        self._corner=tkinter.StringVar(self.welcome_menu)
        self._winner=tkinter.StringVar(self.welcome_menu)
        number_options=[4,6,8,10,12,16]
        turn_options=['B','W']
        winners=['More','Less']
        self._row.set(4)
        self._col.set(4)
        self._turn.set("B")
        self._corner.set("B")
        self._winner.set("More")
        row_drop=tkinter.OptionMenu(self.welcome_menu,self._row,*number_options)
        row_drop.config(bg="BLUE",foreground="WHITE",height=1,width=5)
        row_drop.grid(row=1,column=1,padx=10,pady=10,sticky=tkinter.E)

        col_menu=tkinter.OptionMenu(self.welcome_menu,self._col,*number_options)
        col_menu.config(bg="GREEN",foreground="yellow",background='green',height=1,width=5)
        col_menu.grid(row=2,column=1,padx=10,pady=10,sticky=tkinter.E)

        turn_menu=tkinter.OptionMenu(self.welcome_menu,self._turn,*turn_options)
        turn_menu.config(bg="BLACK",foreground="WHITE",height=1,width=5)
        turn_menu.grid(row=3,column=1,padx=10,pady=10,sticky=tkinter.E)

        corner_menu=tkinter.OptionMenu(self.welcome_menu,self._corner,*turn_options)
        corner_menu.config(foreground="BLACK",background="#FF8000",height=1,width=5)
        corner_menu.grid(row=4,column=1,padx=10,pady=10,sticky=tkinter.E)

        who_win_menu=tkinter.OptionMenu(self.welcome_menu,self._winner,*winners)
        who_win_menu.config(foreground="BLUE",background="#FF8000",height=1,width=5)
        who_win_menu.grid(row=5,column=1,padx=10,pady=10,sticky=tkinter.E)
        

        self.welcome_menu.grid()
        self.welcome_menu.mainloop()

    def validate_Data(self): 

        '''
         retrieve the values that  the user inputs from the game menu
         '''
       
        
        self._row=(self._row.get())
        self._col=(self._col.get())
        self._turn=self._turn.get()
        self._corner=self._corner.get()
        self._winner=self._winner.get()
        self.welcome_menu.destroy()

    def gstart(self):
        ''' start the menu window '''
        self.welcome_menu.mainloop()

    def othello(self):

        return Othello.Othello(int(self._col), int(self._row), self._turn, self._corner,[])
        
    
        
if __name__ == '__main__':
    print("FUll")

    game_option =  game_menu()

    game_option.gstart()
    game = game_option.othello()
    winner = game_option._winner
    othello_game = Othello_Game(game, winner)
    othello_game.start()

