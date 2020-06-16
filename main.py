from code.classes.matrix import Matrix
from code.classes.aminoacid import AminoAcid
from code.classes.protein import Protein
from code.classes.connection import Connection

from code.helpers.matrixinit import matrix_initializer
from code.helpers.stringconverter import string_converter

from code.algorithms.matrixupdate import matrix_updater
from code.algorithms.greedy import greedy
from code.algorithms.depth import depth_first_search

from code.visualizations.visualize import visualizer

from sys import argv

def main(string_input, algorithm_input):
    
    # set initial values
    height = 30
    width = 30

    # analyse user input to choose the string and convert to numerical string
    if string_input == 1:
        protein_string = ["H","H","P","H","H","H","P","H","P","H","H","H","P","H"]
    
    if string_input == 2:
        protein_string = ["H","P","H","P","P","H","H","P","H","P","P","H","P","H","H","P","P","H","P","H"]
    
    protein_string_converted = string_converter(protein_string)
    
    # create matrix object
    initial_matrix = Matrix(width, height)
    
    # create the first amino acid object with coordinates in the middle of the matrix    
    amino_acid = AminoAcid(height/2, width/2, protein_string_converted[0])
    
    # add coordinates and value to protein
    protein = Protein()
    
    # initilize connection
    connections = Connection()
    
    # ---------------- Initilize grid with first amino acid --------------------
    initial_matrix = matrix_initializer(initial_matrix, amino_acid, protein)
    
    # -------------------- Random protein construction -------------------------
    if algorithm_input == "random":
        matrix = matrix_updater(initial_matrix[0], protein_string_converted[1:], initial_matrix[1], initial_matrix[2], connections)

    # ----------------------- Greedy construction ------------------------------
    if algorithm_input == "greedy":
        matrix = greedy(initial_matrix[0], protein_string_converted[1:], initial_matrix[1], initial_matrix[2], connections)

    # ------------------------ depth search construction -----------------------
    if algorithm_input == "depth-first":
        matrix = depth_first_search(initial_matrix[0], protein_string_converted[1:], initial_matrix[1], initial_matrix[2], connections)

    # make plot
    visualizer(matrix[0], matrix[1])
    
if __name__ == "__main__":
    if len(argv) != 3:
        print("Please provide a protein string and an algorithm in the command line")
        quit()
    
    string_input = int(argv[1])

    if string_input not in [1,2]:
        print("please choose one of the following strings by integer:\n 1: HHPHHHPHPHHHPH \n 2: HPHPPHHPHPPHPHHPPHPH")
        quit()
    if argv[2].lower() not in ["greedy", "random", "depth-first"]:
        print("please choose one of the following algorithms: \n random \n greedy \n depth-first")
        quit()

    main(string_input, argv[2].lower())
