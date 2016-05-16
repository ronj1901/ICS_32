

class Othello:
    directions = [[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]


    def __init__(self, rows, columns, turn, top_left_corner, winning_criteria, board):
        "Default constructor"

        self._rows =   rows
        self._column = columns
        self._turn =  turn

        self._top_left_corner = top_left_corner
        self._board = board

        self.winning_criteria = winning_criteria

    def get_rows(self):
        " returns the number of rows in board"
        return self._rows

    def get_columns(self):
        "returns the number of columns in board"
        return self._columns


    def print_board(self):
        "print the board"
        for i in range(0, len(self._board)):
            for j in range(0, len(self._board[0])):
                print(self._board[i][j], end = ' ')
    def get_opposite_of(self, color):
        "return opposite color value, here B and W are opposites"
        if color = "B" :
            return "W"
        else:
            return "B"

    def get_count(self, color):
        "return the number of cells occupied by each disc "

        count =  0
        for i in range(0, self._rows):
            for j in range(0, self._columns):
                if self._board = color:
                    count += 1

        return count

    def is_valid_row_or_column(self, real_value, entered_value):
        "check if the value is within the specified board size"

        if (entered_value >=4 and entered_value <= real_value):
            return True
        else:
            return False

    def in_bound(self, i , j ):
        "checks if the index belongs to the array or it has gone out of the range from either side"

        return ((i >= 0 and i < len(self._board))  and (j>=0 and j <len(self._board[0])))
    

    def is_move_valid(self, i , j):
        "checks if a ,move can be made to this cell given by i ,j   for the current player given by turn variable"
        valid_boxes = []
        for a , b in self._directions:
            x, y = i, j
            x += a
            y += b

            if(self.in_bound(x,y) and (self._board[x][y] == self.get_opposite_of(self._turn))):
                x += a
                y += b

                while (self.in_bound(x,y) and (self._board[x][y] == self.get_opposite_of(self._turn))):
                    x += a
                    y += b
                if self.in_bound(x,y) and self._board[x][y] == self._turn :
                    while True:
                        x -= a
                        y -= b
                        valid_boxes.append([x,y])
                        if x == i and y == j :
                            break
            
        return valid_boxes

    
