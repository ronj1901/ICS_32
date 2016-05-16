class Othello:
	directions = [[0,1], [1,1], [1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,-1]]      ## move towars the direction 

	def __intit__(self, rows, columns, turn,top_left_corner, winning_criteria, board):
		''' Default constructor''' 

		self._rows =  rows 
		self._columns = columns 
		self._turn = turn 
		self_.top_left_corner  = top_left_corner
		self._board = board 
		self._winning_criteria   = winning_criteria 


		# now I am going to make functions or methods that makes a game logic 


		def get_rows(self): 
			''' return the number of rows in a board ''' 
			return self._rows

		def get_columns(self):
			''' return the  number of columns in a board ''' 
			return self._columns

		def print_board(self):
			''' prints the game board ''' 
			for i in range(0, len(self._board)):
				for j in range(0, len(self._rows)):
					print(self._board[i][j], end = '')
				print('')

		def get_opposite_of(self, color):
			''' returns the opposite color value ''' 
			if color == 'B':
				return 'W'
			else: 
				return 'B'

		def  get_count(self, color):
			'''  returns the number of cells  occupied by the specific colored disc  ''' 
			count = 0 
			for i in range(0, self._rows):
				for j in range(0, self._columns):
					if self._board[i][j] == color:
						count += 1 
			return count 



		def in_bound(self, i , j ):
			''' checks if the index belongs to the array or it has gone out of range from either side ''' 
			if (((i >= 0 and i < len(self._board)) and (j >= 0 and j < len(self._board)))):
				return True 
			else: 
				return False

		def is_move_valid(self, i, j ):
			''' checks if the move can be made to this cell given by i , j for the current player given by turn variable '''

			valid_boxes = [] 
			for a,b in self.directions:
				x, y = i, j 
				x += a 
				y += b 

				if(self.in_bound(x,y) and self._board[x][y] == self.get_opposite_of(self._turn)):
					x += a
					y -=  b

				






