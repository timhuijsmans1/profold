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
        
        # initiate matrix based on the size height and width provided
        matrix = [[0]*width for n in range(height)]
    
class AminoAcid:
    """Amino acid object that can be placed into to the previously 
       placed amino acid the grid and can only be relative"""
      
    def __init__(self, row, column, value):
        self.row = row 
        self.column = column
        self.value = value
        
    # check the available directions on the previously placed amino acid (In the algorithm, not in this class!!!!)
    
    # place the amino acid on a new position based on available directions from previous amino acid(update the matrix object for the chosen position)

class Protein:
    """Keeps track of all the amino acids placed in the grid
       to represent the string as a protein"""
    
    def __init__(self):
    
    # add the position of a new amino acid to a list of amino acid coordinate lists
    # in order to keep track of all linked amino acid position
    def add_amino_acid:
        
def main():
    # create matrix object
    
    # define the string to map as a list of H or P values:
    protein_string = [H,H,P,H,H,H,P,H,P,H,H,H,P,H]
    
    # create amino acid object with coordinates in the middle of the matrix
    amino_acid = AminoAcid(height/2, width/2, protein[0])
    
    # check available positions around the most recent placed amino_acid
    if not 
    
if __name__ == "__main__":
    main()