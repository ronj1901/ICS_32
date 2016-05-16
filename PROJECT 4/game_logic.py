 # SHAMBHU THAPA 10677794 
 # in this module i  am going to make a game logic 

## make a class for gamestate 


class GameState:

	def __init__(self, row, col, turn):
		self._row = row 
		sel._col = col 
		self._turn = turn 

	def print_board(self):

		'''
		Draws the board 
		'''

	def print_board(self)->list:
        '''  return the gamestate'''
        board = []
        for i in range(self._col):
            board.append([' '] * self._row)

        board[int(self._col- 1)][int(self._row-1)] = 'B'
        board[int(self._col/2)-1][int(self._row/2)] = 'B'
        board[int(self._co/2)][int(self._row/2)-1] = 'W'
        board[int(self._col/2)][int(self._row/2)] = 'W'

        return board 


      def take_turn(self):
      	''' track the turn of the players ''' 
      	if self._turn = 'B':
                return 'W'

      	else:
      		return 'B'




##### the code below shoould go to another module #############
def get_col():

	col = int(input("Please enter the column number "))


	return col 

def get_row():

	row = int(input( "Please enter the row number"))

	return row 

# def who_first(self)->str:


# 	while True:

# 	    choice = input(' B for Black and  W for White -- play first: ')

# 	    if choice == 'B':
# 	        return 'B'
# 	    elif choice == 'W':
# 	        return  'W'

def who_first():
	'''
	decides which player goes first
	'''
	while True:
                choice = input(' B for Black and  W for White -- play first: ')

		if choice == 'B':
			return 'B'
		elif choice  == 'W':
			return 'W'



     
def get_arrow():
	''' determine how the game shoulld chose winner '''
	arrow = input()
	return arrow




 if __name__ == '__main__': 

	'''call the modules and functions '''

	print("FULL")

	get_col()
	get_row()
	who_first()
	get_arrow()










# functions 



