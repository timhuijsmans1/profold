import matplotlib.pyplot as plt

from code.classes.matrix import Matrix
from code.classes.aminoacid import AminoAcid
from code.classes.protein import Protein
from code.classes.connection import Connection

from code.algorithms.matrixinit import matrix_initializer
from code.algorithms.matrixupdate import matrix_updater

def main():
    
    # set initial values
    height = 20
    width = 20
    #protein_string = ["H","H","P","H","H","H","P","H","P","H","H","H","P","H"]
    protein_string = [1,1,2,1,1,1,2,1,2,1,1,1,2,1]
    
    # create matrix object
    initial_matrix = Matrix(width,height)    
    
    # create the first amino acid object with coordinates in the middle of the matrix    
    amino_acid = AminoAcid(height/2, width/2, protein_string[0])
    
    # add coordinates and value to protein
    protein = Protein()
    
    # initilize connection
    connections = Connection()
    
  
    # --------------------------- Initilize grid with first amino acid --------------------------
    initial_matrix = matrix_initializer(initial_matrix, amino_acid, protein)
    
    
    # --------------------------- Random protein construction --------------------------
    matrix = matrix_updater(initial_matrix[0], protein_string[1:], initial_matrix[1], initial_matrix[2], connections)
    
    
    
    
    """Output: h*w matrix showing the folded protein and the list of aminoacid location in order of bonds"""    
    for row in matrix[0].get_matrix():
        print (row)
    print(matrix[1].protein)
    plt.imshow(matrix[0].get_matrix(), cmap=plt.cm.bwr)
    plt.show()
    
if __name__ == "__main__":
    main()