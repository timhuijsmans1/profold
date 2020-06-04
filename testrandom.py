"""Random matrix generator with a few H's and P's"""
import random
import numpy as np
import matplotlib.pyplot as plt

class Matrix:
    """Matrix object, originally populated by 0's,
        can be populated by amino acids"""
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
        # initiate matrix with 0's
        self.matrix = [[0]*width for n in range(height)]

    
class AminoAcid:
    """Amino acid object that can be placed into to the previously 
       placed amino acid the grid and can only be relative"""
      
    def __init__(self, row, column, value):
        self.row = int(row) 
        self.column = int(column)
        self.value = value
    
    def step_right(self):
        self.row += 1
        return self.row
        
    def step_left(self):
        self.row += -1
        return self.row
    
    def step_up(self):
        self.column += 1
        return self.column
        
    def step_down(self):
        self.column += -1
        return self.column
        
    def update_value(self, value):
        self.value = value
        return self.value


class Protein:
    """Keeps track of all the amino acids placed in the grid
       to represent the string as a protein"""
    
    def __init__(self):
        self.protein = []
    
    # add amino acid to a list that defines the protein
    def add_amino_acid(self, row, column, value):
        self.protein.append([row, column, value])
        return self.protein

def matrix_initializer(width,height):
    """initialize the matrix with first amino acid at the center"""
    
    # create matrix object
    initial_matrix = Matrix(width,height).matrix
    
    # define the string to map as a list of H or P values:
    protein_string = ["H","H","P","H","H","H","P","H","P","H","H","H","P","H"]
    
    # create the first amino acid object with coordinates in the middle of the matrix    
    amino_acid = AminoAcid(height/2, width/2, protein_string[0])
    
    # place this first amino acid in the middle of the matrix
    initial_matrix[amino_acid.row][amino_acid.column] = amino_acid.value
    
    # add coordinates and value to protein
    protein = Protein()
    
    # add initial amino acid to the protein
    protein.add_amino_acid(amino_acid.row, amino_acid.column, amino_acid.value)
    
    return initial_matrix, protein_string, amino_acid, protein


def matrix_updater(matrix, protein_string, amino_acid, protein):    
    """Update the matrix with the remaining values of the protein string"""
    
    # place all other amino acids in the string on a random connected point
    for value in protein_string:    
        
        # check available positions around the most recent placed amino_acid and add to list
        available_positions = []
        if matrix[amino_acid.row + 1][amino_acid.column] == 0:
            available_positions.append("+1")
        
        if matrix[amino_acid.row - 1][amino_acid.column] == 0:
            available_positions.append("-1")
            
        if matrix[amino_acid.row][amino_acid.column + 1] == 0:
            available_positions.append("+2")
            
        if matrix[amino_acid.row][amino_acid.column - 1] == 0:
            available_positions.append("-2")
        
        # if only one position available, choose that one
        if len(available_positions) == 1:
            random_direction = available_positions[0]
        # randomly choose one of the directions from the list of possible directions 
        elif len(available_positions) > 1: 
            random_direction = available_positions[random.randint(0,len(available_positions)-1)]
        
        # update the new position of the amino acid
        if random_direction == "+1":
            amino_acid.step_right()
        if random_direction == "-1":
            amino_acid.step_left()
        if random_direction == "+2":
            amino_acid.step_up()
        if random_direction == "-2":
            amino_acid.step_down()
        
        # update the value of the amino acid with P or H
        amino_acid.update_value(value)
        
        # update matrix with next amino acid
        matrix[amino_acid.row][amino_acid.column] = amino_acid.value
        
        # add the the coordinates and value of the amino acid to the Protein
        protein.add_amino_acid(amino_acid.row, amino_acid.column, amino_acid.value)
        
    return matrix, protein
        
        
def main():
    height = 20
    width = 20
    
    # initialize a matrix of given height and width with the first amino acid in the center
    initial_matrix = matrix_initializer(width,height)
    
    # update the matrix with the rest of the protein string
    matrix = matrix_updater(initial_matrix[0], initial_matrix[1], initial_matrix[2], initial_matrix[3])
    
    
    """Output: h*w matrix showing the folded protein and the list of aminoacid location in order of bonds"""    
    for row in matrix[0]:
        print (row)
    print(matrix[1].protein)
    
if __name__ == "__main__":
    main()