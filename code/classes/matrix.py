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
    
    def get_matrix(self):
        return self.matrix