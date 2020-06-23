import math

class Protein:
    """Keeps track of all the amino acids placed in the grid
       to represent the string as a protein"""
    
    def __init__(self):
        self.protein = []
    
    # add amino acid to a list that defines the protein
    def add_amino_acid(self, row, column, value):
        self.protein.append([column, row, value])
        return self.protein

    def change_amino_acid(self, x, y, vertex):
        self.protein[vertex][0] = x
        self.protein[vertex][1] = y
        return self.protein 
        
    def get_protein(self):
        return self.protein
    
    def set_diagonals(self, direction, x, y):
        if direction == "down-left":
            self.x_L = x - 1
            self.y_L = y - 1
            self.x_LL = x - 1
            self.y_LL = y + 1
            self.x_C = x
            self.y_C = y - 1
        if direction == "up-right":
            self.x_L = x + 1
            self.y_L = y + 1
            self.x_LL = x + 1
            self.y_LL = y - 1
            self.x_C = x
            self.y_C = y + 1
        if direction == "up-left":
            self.x_L = x - 1
            self.y_L = y + 1
            self.x_LL = x + 1
            self.y_LL = y + 1
            self.x_C = x - 1
            self.y_C = y
        if direction == "down-right":
            self.x_L = x + 1
            self.y_L = y - 1
            self.x_LL = x - 1
            self.y_LL = y - 1
            self.x_C = x + 1
            self.y_C = y

    def score_function(self):
        """Check the score for all H and C amino acid combinations"""
        stability = 0
        coordinates = []
        for amino_acid in self.protein:
            for next_amino_acid in self.protein:
                
                # only proceed if the amino acids are non P
                if amino_acid[2] != 2 and next_amino_acid[2] != 2:

                    # only proceed if amino acid or not the same or sequential 
                    if amino_acid != next_amino_acid and abs(self.protein.index(amino_acid)-self.protein.index(next_amino_acid)) != 1:
                        
                        # if they are next to eachother, increase stability
                        if (abs(amino_acid[0] - next_amino_acid[0]) == 1 and abs(amino_acid[1] - next_amino_acid[1]) == 0) or (abs(amino_acid[1] - next_amino_acid[1]) == 1 and abs(amino_acid[0] - next_amino_acid[0]) == 0):
                            coordinates.append([amino_acid[0],next_amino_acid[0],amino_acid[1],next_amino_acid[1]])
                            stability += 1
        
        return -int(stability/2), coordinates



