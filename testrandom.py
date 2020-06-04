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
    
    # add the position of a new amino acid to a dict of amino acids with H or P key and value
    # being a coordinate lists in order to keep track of all linked amino acid position
    def add_amino_acid:
        
def main():
    # create matrix object
    
    # define the string to map as a list of H or P values:
    protein_string = [H,H,P,H,H,H,P,H,P,H,H,H,P,H]
    
    # create the first amino acid object with coordinates in the middle of the matrix
    amino_acid = AminoAcid(height/2, width/2, protein_string[0])
    # Place this first amino acid in the middle of the matrix
    
    """This part needs to loop for all the other amino acids in protein_string after the first one is placed"""
    
    # check available positions around the most recent placed amino_acid
    
    # create a new amino acid object with coordinates of a random possible 
    # position around the previous amino acid
    
    # update the Matrix position with the value at the coordinates of the new amino acid object
    
    # add the the coordinates and value of the amino acid to the Protein
    
if __name__ == "__main__":
    main()