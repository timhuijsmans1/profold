class AminoAcid:
    """Amino acid object that can be placed into to the previously 
       placed amino acid the grid and can only be relative"""
      
    def __init__(self, row, column, value):
        self.row = int(row) 
        self.column = int(column)
        self.value = value
    
    def update_position(self,row_step,column_step):
        self.row += row_step
        self.column += column_step
        
        return self.row, self.column

    def set_position(self, row, column):
        self.row = row
        self.column = column
    
    def update_value(self, value):
        self.value = value
        return self.value