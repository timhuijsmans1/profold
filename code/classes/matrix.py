class Matrix:
    """Matrix object, originally populated by 0's,
        can be populated by amino acids"""
    
    def __init__(self, width, height):
        # initiate matrix with 0's
        self.matrix = [[0]*width for n in range(height)]
        self.protein = []
    
    def update_matrix(self, row, column, value):
        self.matrix[row][column] = value
        return self.matrix

    # retrun matrix
    def get_matrix(self):
        return self.matrix
    
    def set_diagonals(self, direction, x, y):
        if direction == "down-left":
            self.col_L = x - 1
            self.row_L = y - 1
            self.col_C = x
            self.row_C = y - 1
        if direction == "up-right":
            self.col_L = x + 1
            self.row_L = y + 1
            self.col_C = x
            self.row_C = y + 1
        if direction == "up-left":
            self.col_L = x - 1
            self.row_L = y + 1
            self.col_C = x - 1
            self.row_C = y            
        if direction == "down-right":
            self.col_L = x + 1
            self.row_L = y - 1
            self.col_C = x + 1
            self.row_C = y