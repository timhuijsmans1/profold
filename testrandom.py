"""Random matrix generator with a few H's and P's"""
import random
import numpy as np
import matplotlib.pyplot as plt

class Matrix:
    """Matrix object, originally populated by 0's,
        can be populated by amino acids"""
    
    def __init__(self, width, height):
        # initiate matrix with 0's
        self.matrix = [[0]*width for n in range(height)]
    
    def update_matrix(self, row, column, value):
        self.matrix[row][column] = value
        return self.matrix
    
    def get_matrix(self):
        return self.matrix

    
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
    
    def update_value(self, value):
        self.value = value
        return self.value

class Connection:
    """Store the connections of the previous amino acid"""
    def __init__(self):
        self.connections = {}
        
    def set_connections(self, direction, row, column):
        self.connections[direction] = [row,column]
        return self.connections
        
    def get_random_connection(self):
        return random.choice(list(self.connections.items()))
        
    def clear_connections(self):
        self.connections = {}
        return self.connections

class Protein:
    """Keeps track of all the amino acids placed in the grid
       to represent the string as a protein"""
    
    def __init__(self):
        self.protein = []
    
    # add amino acid to a list that defines the protein
    def add_amino_acid(self, row, column, value):
        self.protein.append([row, column, value])
        return self.protein
        
    def get_protein(self):
        return self.protein

def matrix_initializer(width,height):
    """initialize the matrix with first amino acid at the center"""
    
    # create matrix object
    initial_matrix = Matrix(width,height)
    
    # define the string to map as a list of H or P values:
    #protein_string = ["H","H","P","H","H","H","P","H","P","H","H","H","P","H"]
    protein_string = [1,1,2,1,1,1,2,1,2,1,1,1,2,1]
    
    # create the first amino acid object with coordinates in the middle of the matrix    
    amino_acid = AminoAcid(height/2, width/2, protein_string[0])
    
    # place this first amino acid in the middle of the matrix
    initial_matrix.update_matrix(amino_acid.row, amino_acid.column, amino_acid.value)
    
    # add coordinates and value to protein
    protein = Protein()
    
    # add initial amino acid to the protein
    protein.add_amino_acid(amino_acid.row, amino_acid.column, amino_acid.value)
    
    return initial_matrix, protein_string, amino_acid, protein


def matrix_updater(matrix, protein_string, amino_acid, protein):    
    """Update the matrix with the remaining values of the protein string"""
    
    # place all other amino acids in the string on a random connected point
    print(protein_string)
    for value in protein_string:    
        
        connections = Connection()
        # check available positions in the x dimension
        if matrix.get_matrix()[amino_acid.row + 1][amino_acid.column] == 0:
            connections.set_connections("right", 1, 0)
        
        if matrix.get_matrix()[amino_acid.row - 1][amino_acid.column] == 0:
            connections.set_connections("left", -1, 0)
        
        # check available posisitions in the y dimension    
        if matrix.get_matrix()[amino_acid.row][amino_acid.column + 1] == 0:
            connections.set_connections("up", 0, 1)
            
        if matrix.get_matrix()[amino_acid.row][amino_acid.column - 1] == 0:
            connections.set_connections("down", 0, -1)
            
        # pick a random connection from the connections
        step = connections.get_random_connection()
        
        amino_acid.update_value(value)
        
        # update matrix with next amino acid
        matrix.update_matrix(amino_acid.row + step[1][0], amino_acid.column + step[1][1], amino_acid.value)
        
        # add the the coordinates and value of the amino acid to the Protein
        protein.add_amino_acid(amino_acid.row + step[1][0], amino_acid.column + step[1][1], amino_acid.value)
        
        # update the value and position of the amino acid
        amino_acid.update_position(step[1][0], step[1][1])
        
        connections.clear_connections()
        
    return matrix, protein
        
        
def main():
    height = 20
    width = 20
    
    # initialize a matrix of given height and width with the first amino acid in the center
    initial_matrix = matrix_initializer(width,height)
    
    # update the matrix with the rest of the protein string
    matrix = matrix_updater(initial_matrix[0], initial_matrix[1][1:], initial_matrix[2], initial_matrix[3])
    
    
    """Output: h*w matrix showing the folded protein and the list of aminoacid location in order of bonds"""    
    for row in matrix[0].get_matrix():
        print (row)
    print(matrix[1].protein)
    plt.imshow(matrix[0].get_matrix(), cmap=plt.cm.bwr)
    plt.show()
    
if __name__ == "__main__":
    main()