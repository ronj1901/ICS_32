# bhaskar


directions=[[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]

def print_board(temp_board):
	for i in range(0,len(temp_board)):
		for j in range(0,len(temp_board[0])):
			print(temp_board[i][j], end=' ')
		print("")

def get_opposite_of(color):
	if color == "B":
		return "W"
	else:
		return "B"

def get_count(board, color):
	count = 0
	for i in range(0,len(board)):
		for j in range(0,len(board[i])):
			if board[i][j] == color:
				count += 1
	return count

def is_valid_rows_or_column(real_value, entered_value):
	if (entered_value >= 4 and entered_value <= real_value):
		return True
	else :
		return False

def in_bound(board,i,j):
	if((i >=0 and i < len(board)) and (j >=0 and j < len(board[0]))):
		return True
	else:
		return False

def is_move_valid(board,i,j,color):

	valid_boxes = []
	for a,b in directions:
		x,y = i,j
		x += a
		y += b
		if(in_bound(board,x,y) and board[x][y] == get_opposite_of(color)):
			x += a
			y += b

			while (in_bound(board,x,y) and (board[x][y] == get_opposite_of(color))):
				x+=a
				y+=b

			if (in_bound(board,x,y) and board[x][y] == color):
				while True:
					x -= a
					y -= b
					valid_boxes.append([x,y])
					if x==i and y==j:
						break
	return valid_boxes


def get_winner(board,winning_criteria):
	if(winning_criteria == ">"):
		if (get_count(board,"B") > get_count(board,"W")):
			return "B"
		elif (get_count(board,"B") == get_count(board,"W")):
			return "NONE"
		else:
			return "W"
	else:
		if (get_count(board,"B") < get_count(board,"W")):
			return "B"
		elif (get_count(board,"B") == get_count(board,"W")):
			return "NONE"
		else:
			return "W"

def is_empty(board):
	for x in range(0,len(board)):
		for y in range(0,len(board[0])):
			if board[x][y] == ".":
				return True
			continue
	return False

while True:
	rows = int(input())
	if ((rows >= 4) and (rows <= 16) and (rows%2==0)):
		break
	else:
		print("INVALID")
while True:
	columns = int(input())
	if ((columns >= 4) and (columns <= 16) and (columns%2==0)):
		break
	else:
		print("INVALID")

while True:
	first_mover =  input()
	if (first_mover == "B" or first_mover == "W"):
		break
	else:
		print("INVALID")

while True:
	top_left_corner = input()
	if (top_left_corner == "B" or top_left_corner == "W"):
		break
	else:
		print("INVALID")

while True:
	winning_criteria = input()
	if (winning_criteria == ">" or winning_criteria == "<"):
		break
	else:
		print("INVALID")

turn = first_mover
board = []
count = 0


for i in range(0,rows):
	board.append([])
	for j in range(0,columns):
		board[i].append(".")

board[int(rows/2)-1][int(columns/2)-1] = top_left_corner
board[int(rows/2)][int(columns/2)] = top_left_corner
board[int(rows/2)-1][int(columns/2)] = get_opposite_of(top_left_corner)
board[int(rows/2)][int(columns/2)-1] = get_opposite_of(top_left_corner)


while True:
	print("B: %d  W: %d" %(get_count(board, "B"),get_count(board,"W")))
	print_board(board)
	
	boxes = []
	for i in range(0,len(board)):
		for j in range(0,len(board[0])):
			if(is_move_valid(board,i,j,turn)):
				boxes.append([i+1,j+1])
	
	if not is_empty(board):
		print("WINNER:", get_winner(board,winning_criteria))
		break

	if (boxes == []):
		count += 1
		if count==2:
			print("WINNER:", get_winner(board,winning_criteria))
			break
		turn = get_opposite_of(turn)
		continue
	
	print("TURN: ", turn)

	while True:
		str = input()
		str = str.split()
		x = int(str[0])
		y = int(str[1])

		if([x,y] in boxes):
			moves = is_move_valid(board,x-1,y-1,turn)
			print("VALID")
			for p,q in moves:
				board[p][q] = turn
			turn = get_opposite_of(turn)
			count = 0
			break
		else:
			print("INVALID")
