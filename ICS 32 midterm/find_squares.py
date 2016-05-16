board = [
    ['', '', '', '', ''],
    ['', '', '', '', ''],
    ['', '', '', '', ''],
    ['', '', '', '', ''],
    ['', '', '', '', '']]

rows = 5
cols = 5

def print_board(board):
    for row in board:
        print(row)

def make_move(board, row, col):
    if row >= rows or col >= cols or row < 0 or col < 0:
        return
    
    if board[row][col] == '':
        board[row][col] = '.'
        
def directions(row, col):
    make_move(board, row, col) #mark the original square
    directions = [(0,1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1,-1)]
    for direction in directions:
        mul = 1
        new_row = row
        new_col = col
        while 0 <= new_row < rows and 0<= new_col < cols:
            new_row = row+(direction[0]*mul)
            new_col = col+(direction[1]*mul)
            make_move(board, new_row, new_col)
            mul += 1


print_board(board)
print("-------")
directions(2, 2)
print_board(board)
