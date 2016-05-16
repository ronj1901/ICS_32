#   Othello 
DIRECTIONS=[[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]
WHITE='W'
BLACK='B'

class Othello:
    def __init__(self,row,col,turn,corner,board):
        self._row=row
        self._col=col
        self._turn=turn
        self._corner=corner
        self._board=board


    def _new_game_board(self):
        '''
         Create a new game board size rxc based on the imformation passed in when the
         Othello Object was created
        '''
        if(self._corner.upper()==WHITE):
            opposite=BLACK
        else:
            opposite=WHITE
            
        board = []
        for i in range(self._row):
            board.append([' '] * self._col)
        board[int(self._row/2)-1][int(self._col/2)-1]=self._corner
        board[int((self._row/2))][int((self._col/2))]=self._corner
        board[int(self._row/2)-1][int(self._col/2)]=opposite
        board[int((self._row/2))][int((self._col/2)-1)]=opposite
        self._board=board


    def print_board(self):
        '''
        Prints the Whole board with row and column printed. When the row or col reaches 10, it resets to 0
        '''
        count=1
        count2=1
        print(end='    ')
        for col in range(len(self._board[0])):
            if(count>=10):
                count=0
            print(count,sep='   ',end='   ')
            count+=1
        print()

        for r in range(len(self._board)):
            if(count2>=10):
                count2=0
            print(count2,sep='     ',end='   ')
            count2+=1
            for c in range(len(self._board[0])):
                if(self._board[r][c]==' '):
                    print('.',sep='     ',end='   ')
                else:
                    print(self._board[r][c],sep='     ',end='   ')
            print()
        print()



    def place_piece(self,row:int,col:int):
        '''
        Takes in the piece from the user then checks if it is a valid move.
        If it is, it will get the pieces that need to be flipped then will
        execute the move by updating the Game Board.
        '''
        self._require_valid_row_number(row)
        self._require_valid_col_number(col)    
        if(self.isValid(row,col)):
            moves=self.getMoves(row,col)
            if(len(moves)>0):
                return self.makeMove(moves)
            else:
                return False
      

    def isValid(self,r:int,c:int):
        '''
        Checks if the move passed in was valid. IF it  is valid, it will return True, other wise it will return false.
        '''
        if((self._board[r][c] !=' ') or not self.onBoard(r,c)):
            return False
        else:
            return True
         
    def onBoard(self,r:int,c:int)->bool:
        return((r>=0 and r<=len(self._board)) and (c>=0 and c<=len(self._board[0])))


    def getMoves(self,row:int,col:int)->list:
        '''
        Loops through the 8 directions at the top of the Class.
        Will look for the opposite colored piece.
        Once it find our own piece, Back track trough the spaces I went though
        then append those locations to the list and return that.
        That list contains the locations of all the tiles that need to be flipped.
        Any time the move is not on the board,it will go to the except block and continue onto
        the next iteration of the loop until i reach the end. 
        '''
        opposite=self._opposite_turn()
        flippedTiles=[]
        for horizontal,vertical in DIRECTIONS:
            x,y=row,col
            x+=horizontal
            y+=vertical
            try:
                if(self.onBoard(x,y)and self._board[x][y]==opposite):
                        x+=horizontal
                        y+=vertical
                        
                        while self._board[x][y]==opposite:
                            x+=horizontal
                            y+=vertical
                           
                        if self._board[x][y]==self._turn:
                            while (True):
                                x-=horizontal
                                y-=vertical
                                flippedTiles.append([x,y]) 
                                if x==row and y==col:
                                    break                                       
            except:
                continue

        return flippedTiles

    def getValidMoves(self):
        '''
        Checks if there is a single valid move for a player on the entire board.
        If this method returns [] then we know they have no moves and it switches turns.
        '''
        validMoves=[]
        for x in range(len(self._board)):
            for y in range(len(self._board[0])):
                if (self.getMoves(x,y)) != [] and self.isValid(x,y):
                    validMoves.append([x+1,y+1])
        return validMoves
           
    def makeMove(self,l:list):
        '''
        Takes the list from getMoves and makes those changes on the game board
        then returns the state of the game.
        '''
        for x,y in l:
            newBoard=self._board[:]
            newBoard[x][y]=self._turn
        self._board=newBoard
        self._turn=self._opposite_turn()
        return Othello(self._row,self._col,self._turn,self._corner,self._board)
  

    def _opposite_turn(self)->str:
        '''
        Returns the opposite turn.
        '''
        if self._turn=='W':
            return BLACK
        else:
            return WHITE

    def countPieces(self,color:str):
        '''
        Counts the Total number of pieces on the board for the specified player.
        '''
        count=0
        for x in range(len(self._board)):
            for y in range(len(self._board[0])):
                if self._board[x][y]==color:
                    count+=1
        return count

    '''
    For the Next 2 functions, They determine the winner based on the win contition. Either the most pieces , or the least pieces. The
    Methods will count the toal number of pieces on the board for each player, then decide who win the game.
    '''

    def determineWinner(self):
        white=self.countPieces("W")
        black=self.countPieces("B")
        if(white>black):
            return("White Wins",white,"to",black)
        elif(black>white):
            return("Black Wins",black,"to",white)
        elif(black==white):
           return("The game is a draw")

    def determineWinnerLeast(self):
        white=self.countPieces("W")
        black=self.countPieces("B")
        if(white<black):
            return("White Wins",white,"to",black)
        elif(black<white):
            return("Black Wins",black,"to",white)
        elif(black==white):
            return("The game is a draw")
                
                        
    def _require_valid_row_number(self,row):
        if type(row)!= int or not self._is_valid_row_number(row):
             raise ValueError('row_number must be int between 0 and {}'.format(len(board)))

    def _is_valid_row_number(self,row) -> bool:
        '''Returns True if the given column number is valid; returns False otherwise'''
        return 0 <= row < len(self._board)


    def _require_valid_col_number(self,column_num):
        if type(column_num)!= int or not self._is_valid_column_number(column_num):
             raise ValueError('column_number must be int between 0 and {}'.format(len(board[0])-1))

    def _is_valid_column_number(self,column_number) -> bool:
        '''Returns True if the given column number is valid; returns False otherwise'''
        return 0 <= column_number < len(self._board[0])
