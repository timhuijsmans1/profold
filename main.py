from code.classes.matrix import Matrix
from code.classes.aminoacid import AminoAcid
from code.classes.protein import Protein
from code.classes.connection import Connection

from code.algorithms.matrixinit import matrix_initializer
from code.algorithms.matrixupdate import matrix_updater
from code.algorithms.greedy import greedy
from code.algorithms.depth import depth_first_search


from code.visualizations.visualize import visualizer


def main():
    
    # set initial values
    height = 30
    width = 30

    protein_string = ["H","H","P","H","H","H","P","H","P","H","H","H","P","H"]
    # protein_string_converted = [1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1]
    protein_string_converted = []

    for i in range(len(protein_string)):

        if protein_string[i] == 'H':
            protein_string_converted.append(1)
        elif protein_string[i] == 'P':
            protein_string_converted.append(2)

    # create matrix object
    initial_matrix = Matrix(width, height)
    
    # create the first amino acid object with coordinates in the middle of the matrix    
    amino_acid = AminoAcid(height/2, width/2, protein_string_converted[0])
    
    # add coordinates and value to protein
    protein = Protein()
    
    # initilize connection
    connections = Connection()
    
    # --------------------------- Initilize grid with first amino acid --------------------------
    initial_matrix = matrix_initializer(initial_matrix, amino_acid, protein)
    
    # --------------------------- Random protein construction --------------------------
    #matrix = matrix_updater(initial_matrix[0], protein_string_converted[1:], initial_matrix[1], initial_matrix[2], connections)

    # --------------------------- Greedy construction --------------------------
    greed = greedy(initial_matrix[0], protein_string_converted[1:], initial_matrix[1], initial_matrix[2], connections)

    # --------------------------- depth search construction --------------------------
    #depth = depth_first_search(initial_matrix[0], protein_string_converted[1:], initial_matrix[1], initial_matrix[2], connections)

    #---------------------------- Breadth search construction -------------------------------------
    #breadth = breadth_first(initial_matrix[0], protein_string_converted[1:], initial_matrix[1], initial_matrix[2], connections)

    # make plot
    visualizer(greed[0], greed[1])
    #print(depth[2])
    
if __name__ == "__main__":
    main()
