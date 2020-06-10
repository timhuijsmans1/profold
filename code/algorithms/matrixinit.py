"""Random matrix generator with a few H's and P's"""
import random
import numpy as np


def matrix_initializer(initial_matrix, amino_acid, protein):
    """initialize the matrix with first amino acid at the center"""
        
    # place this first amino acid in the middle of the matrix
    initial_matrix.update_matrix(amino_acid.row, amino_acid.column, amino_acid.value)
    
    # add initial amino acid to the protein
    protein.add_amino_acid(amino_acid.row, amino_acid.column, amino_acid.value)
    
    return initial_matrix, amino_acid, protein


