'''
Shambhu Thapa 10677794

Project 4
OthelloGame.py
'''

import Othello
from UserException import *


def get_opposite_of(color):
	"Function to get opposite of given colour"
	if color == "B":
		return "W"
	else:
		return "B"

def game_setup():
	"Function for first time setup of game, take rows, columns, first mober, top left corner player, winning criteria as input and creates a board object out of it"
	print("FULL")

	while True:
		#Take input for number of rows
		try:
   			rows = int(input())
   			if ((rows >= 4) and (rows <= 16) and (rows%2==0)):
   				break
   			else:
   				raise OutOfBoundError("INVALID")
		except OutOfBoundError as e:
   			print("".join(e))
   	    

	while True:
		#Takes input for number of columns
		try:
			columns = int(input())
			if ((columns >= 4) and (columns <= 16) and (columns%2==0)):
				break
			else:
				raise OutOfBoundError("INVALID")
		except OutOfBoundError as e:
   			print("".join(e))
        
	while True:
		#Takes input for first user to start the game
		try:
			first_mover =  input()
			if (first_mover == "B" or first_mover == "W"):
				break
			else:
				raise InvalidPlayerError("INVALID")
		except InvalidPlayerError as e:
   			print("".join(e))

	while True:
		#Take input for colour in top left corner
		try:
			top_left_corner = input()
			if (top_left_corner == "B" or top_left_corner == "W"):
				break
			else:
				raise InvalidPlayerError("INVALID")
		except InvalidPlayerError as e:
   			print("".join(e))

	while True:
		#Take input for winning criteria i.e more number of pieces or less
		try:
			winning_criteria = input()
			if (winning_criteria == ">" or winning_criteria == "<"):
				break
			else:
				raise InvalidWinningCriteria("INVALID")
		except InvalidWinningCriteria as e:
   			print("".join(e))

	board = []
	for i in range(0,rows):  #Creates borad with "." everwhere
		board.append([])
		for j in range(0,columns):
			board[i].append(".")

	#Put first 4 marker of B and W
	board[int(rows/2)-1][int(columns/2)-1] = top_left_corner
	board[int(rows/2)][int(columns/2)] = top_left_corner
	board[int(rows/2)-1][int(columns/2)] = get_opposite_of(top_left_corner)
	board[int(rows/2)][int(columns/2)-1] = get_opposite_of(top_left_corner)

	#Create and return an instance of Othello game with the specified parameters
	return Othello.Othello(rows,columns,first_mover,top_left_corner,winning_criteria,board)


def play_game(othello_game):
	"Function where the game gets carried, continues until there are no more possible for both B & Y or if the board has got full. Winner decided here based on the winning criteria i.e more discs or less to win. Also before a user makes a move this method calculates the all possible moves for that player then checks if the input value belongs to these possible values if it does then the game proceeds by making a move else user is reprompted to enter the values. Once a move is made the turn is switched."
	count = 0  #This variable keeps count of consecutive times when players had nothing to move, if this count becomes two, i.e both player had no moves back to back, then game gets over
	while True:
		print("B: %d  W: %d" %(othello_game.get_count("B"),othello_game.get_count("W")))
		othello_game.print_board()
		
		boxes = []  #variable to store all possible cells in which a move is possible in the current scenario
		for i in range(0,othello_game.get_rows()):
			for j in range(0,othello_game.get_columns()):
				if(othello_game.is_move_valid(i,j)):
					boxes.append([i+1,j+1])  #all possible box in which we can move the player in the current scenario
		
		if not othello_game.is_empty():
			#checks if the board is not empty i.e completely fulled, then it means the game is over
			print("WINNER:", othello_game.get_winner())
			break

		if (boxes == []):
			#As boxes was the variable storing all possible cells in which move was possible in the current scenario, and as its empty means no move possible for the player in current scenario, hence increase the count
			count += 1

			if count==2:
				#As explained if count gets 2 then game over
				print("WINNER:", othello_game.get_winner())
				break

			othello_game.switch_turn() #used to switch turn between players, since the current player has no possible move it passes
			continue   #skip the whole loop
		
		print("TURN: ", othello_game.get_turn())  #print the player whos turn it is

		while True:
			str = input()  #takes as input the cell to move in
			str = str.split()   #splits the cell into a list of integers, i.e splits "2 4" into [2,4]
			x = int(str[0])   #assigns the first integer 
			y = int(str[1])	  #assigns the second integer

			if([x,y] in boxes):  #as boxes was storing the cells which can be moved into, we check if the entered cell can be moved into
				moves = othello_game.is_move_valid(x-1,y-1)  #we get the flipped cells i.e the cells in board which will change to the current players colour due to this move 
				print("VALID")
				othello_game.move(moves)  #change the whole structure of board due to this move
				
				othello_game.switch_turn()  #switch turns
				count = 0  #reassign count to 0, since there was a move made
				break
			else:
				print("INVALID")   #print that the entered cell cannot be moved into or is not correct, hence INVALID


if __name__=='__main__':
    othello_game = game_setup()  #setup/initailization of game
    play_game(othello_game)  #playing the game

