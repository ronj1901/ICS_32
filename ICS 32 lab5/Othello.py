
# Othello Game Logic


DIRECTIONS=[[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]


class Othello:
    
    

    def __init__(self,row,col,turn,corner,board):
        ''' default constructor'''
        self._row=row
        self._col=col
        self._turn=turn
        self._corner=corner
        self._board=board


    def game_board(self):
        '''
         create a game board as per the given row and col size , set the game state
        '''
        if(self._corner.upper()== 'W'):
            opponent= 'B'
        else:
            opponent='W'
            
        board = []
        for i in range(self._row):
            board.append([' '] * self._col)
        board[int(self._row/2)-1][int(self._col/2)-1]=self._corner
        board[int((self._row/2))][int((self._col/2))]=self._corner
        board[int(self._row/2)-1][int(self._col/2)]=opponent
        board[int((self._row/2))][int((self._col/2)-1)]=opponent
        self._board=board


    def display_board(self):
        '''
         display the game board 
        '''

              
        for row in range(len(self._board)):
            for column in range(len(self._board[row])):
                print(self._board[row][column], end = ' ')
            print()


    def plug_piece(self,i:int, j:int):
        '''
        plug in the desired piece onto the board 
        '''
        self.valid_row(i)
        self.valid_col(j)    
        if(self.isValid(i,j)):
            moves=self.getMoves(i,j)
            if(len(moves)>0):
                return self.makeMove(moves)
            else:
                return False
      

    def isValid(self,i:int, j:int):
        '''
        Checks if the move passed in was valid. IF it  is valid, it will return True, other wise it will return false.
        '''
        if((self._board[i][j] !=' ') or (not self.onBound(i,j))):
            return False
        else:
            return True
         
    def onBound(self,i:int,j:int)->bool:
        '''
        check the boundary of the row and col  that are allowed
        '''
        return((i>=0 and i<=len(self._board)) and (j>=0 and j<=len(self._board[0])))


    def getMoves(self,i:int,j:int)->list:
        '''
        set the move and alternate the player's turn
        '''
        opposite=self.switch_turn()
        validboxes=[]
        for a ,b in DIRECTIONS:
            x,y= i ,j
            x += a
            y += b
            try:
                if(self.onBound(x,y)and self._board[x][y]==opposite):
                        x += a 
                        y += b
                        
                        while self._board[x][y]==opposite:
                            x += a
                            y += b
                           
                        if self._board[x][y]==self._turn:
                            while True:
                                x -= a
                                y -= b
                                validboxes.append([x,y]) 
                                if x == i and y == j:
                                    break                                       
            except:
                continue

        return validboxes

    def getValidMoves(self):
        
        AllowedMoves=[]
        for x in range(len(self._board)):
            for y in range(len(self._board[0])):
                if (self.getMoves(x,y)) != [] and self.isValid(x,y):
                    AllowedMoves.append([x+1,y+1])
        return AllowedMoves
           
    def makeMove(self,List:[]):
       
        for x,y in List:
            N_Board=self._board[:]
            N_Board[x][y]=self._turn
        self._board=N_Board
        self._turn=self.switch_turn()
        return Othello(self._row,self._col,self._turn,self._corner,self._board)
  

    def switch_turn(self)->str:
        '''
        Returns the opposite turn.
        '''
        if self._turn=='W':
            return 'B'
        else:
            return 'W'

    def get_count(self,color:str):
        '''
        Counts the Total number of disc for each plauer .
        '''
        total =0
        for x in range(len(self._board)):
            for y in range(len(self._board[0])):
                if self._board[x][y]==color:
                    total +=1
        return total

  

    def winner_more(self):
        '''
         determine winning condition for player with more discs        
        '''
        white_piece=self.get_count("W")
        black_piece=self.get_count("B")
        if(white_piece>black_piece):
            return("Player White wins")
        elif(white_piece < black_piece):
            return("Black  Player Wins")
        elif(white_piece  == black_piece):
           return("It is a Tie, No one is winner")
        

    def winner_less(self):
        '''
         determine winning condition for player with less discs       
        '''
        white_piece=self.get_count("W")
        black_piece=self.get_count("B")
        if(white_piece < black_piece):
            return("Player white wins")
        elif(white_piece  > black_piece):
            return("Player black wins")
        elif(white_piece  == black_piece):
            return("It is a Tie, No one is winner")
                
                        
    def valid_row(self,row):
        ''' handle the exception when invalid row is given'''
        if (type(row)!= int) or (not self.validate_row(row)):
             raise ValueError('Invalid')

    def validate_row(self,row) -> bool:
        '''check if the given row is valid or not'''
        return 0 <= row < len(self._board)


    def valid_col(self,column_num):
        ''' handle the exception when invalid col is given'''
        if (type(column_num)!= int) or (not self.validate_col(column_num)):
             raise ValueError("Inavalid")

    def validate_col(self,col) -> bool:
        '''check if the given row is valid or not'''
        return 0 <= col < len(self._board[0])
