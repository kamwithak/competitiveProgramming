class Sudoku():

    def __init__(self, board):
        self.board = board

    """
    Naive:

        Iterate over all rows: verify uniqueness fir all numbers in rows
        Iterate over all columns using zip(*vector): verify uniqueness for all numbers in column
        Iterate over all boxes: using python slicing board[i:j], get the box, verify uniqueness for all numbers in block

        for ... O(1)
    
        for ... O(1)
        
        for ... O(1)

        additive property => summation of above time complexities

    Better:

        Init an empty hashSet, set()
        Iterate over each entry (i, j)
        Check if entry is non-empty:
            
            row_str = f"{entry} {i} row_str"
            col_str = f"{entry} {j} col_str"
            box_str = f"{entry} {i // 3} {j // 3} box_str"

            if (rows_str in _set or col_str in _set or box_str in _set):
                return False

            set.add(row_str)
            set.add(col_str)
            set.add(box_str)

        return True

    """

    def efficientSolution(self):
        cache = set()
        for i in range(9):
            for j in range(9):
                if (self.board[i][j] != '.'):
                    row = f"{self.board[i][j]} row {i}"
                    col = f"{self.board[i][j]} col {j}"
                    square = f"{self.board[i][j]} square {i//3} {j//3}"
					
                    if (row in cache or col in cache or square in cache):
                        return False
					
                    cache.add(row)
                    cache.add(col)
                    cache.add(square)
        return True

class Solution:
    def isValidSudoku(self, board):
        
        def is_valid_row():
            for row in board:
                if not is_valid(row):
                    return False
            return True
        
        def is_valid_col():
            for col in zip(*board):
                if not is_valid(col):
                    return False
            return True
        
        def is_valid_square():
            for i in (0,3,6):
                for j in (0,3,6):
                    square = [board[x][y] for x in range(i,i+3) 
                                        for y in range(j,j+3)]
                    if not is_valid(square):
                        return False
            return True
    
        def is_valid(value):
            res=[i for i in value if i!="."]
            return len(res)==len(set(res))
        
        return is_valid_row() and is_valid_col() and is_valid_square()

