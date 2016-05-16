'''
shambhu thapa 10677794 Project 4

UserException.py
        
'''


class OutOfBoundError(RuntimeError):
	"Exception for rows or columns out of bounds"
	def __init__(self, arg):
		self.args = arg

class InvalidPlayerError(RuntimeError):
	"Exception for invalid value of player"
	def __init__(self, arg):
		self.args = arg

class InvalidWinningCriteria(RuntimeError):
	"Exception for invalid value for winning criteria"
	def __init__(self, arg):
		self.args = arg
