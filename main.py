from code.classes.matrix import Matrix
from code.classes.aminoacid import AminoAcid
from code.classes.protein import Protein
from code.classes.connection import Connection

from code.helpers.matrixinit import matrix_initializer
from code.helpers.stringconverter import string_converter

from code.algorithms.random import random_algorithm
from code.algorithms.greedy import greedy
from code.algorithms.depth import depth_first_search
from code.algorithms import breadthfirstivo as bf
from code.algorithms import depth_first as df
from code.algorithms.hillclimb import hill_climb

from code.visualizations.visualize import visualizer

from sys import argv

def main(string_input, algorithm_input):

    # analyse user input to choose the string and convert to numerical string
    if string_input == 1:
        protein_string = ["H","H","P","H","H","H","P","H","P","H","H","H","P","H"]
    
    if string_input == 2:
        protein_string = ["H","P","H","P","P","H","H","P","H","P","P","H","P","H","H","P","P","H","P","H"]

    if string_input == 3:
        protein_string = ["H", "H", "H", "H", "H"]

    if string_input == 4:
        protein_string = ["P","P","P","H","H","P","P","H","P","P","P","P","P","H","H","H","H","H","H","H","P","P","H","H","P","P","P","P","H","H","P","P","H","P","P"]
    
    if string_input == 5:
        protein_string = ["H","H","P","H","P","H","P","H","P","H","H","H","H","P","H","P","P","P","H","P","P","P","H","P","P","P","P","H","P","P","P","H","P","P","P","H","P","H","H","H","H","P","H","P","H","P","H","P","H","H"]
        
    protein_string_converted = string_converter(protein_string)

    # set initial values
    height = 30 #int(len(protein_string_converted) * 2)
    width = 30 #int(len(protein_string_converted) * 2)
    
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
        matrix = random_algorithm(initial_matrix[0], protein_string_converted[1:], initial_matrix[1], initial_matrix[2], connections)

    # ----------------------- Greedy construction ------------------------------
    if algorithm_input == "greedy":
        matrix = greedy(initial_matrix[0], protein_string_converted[1:], initial_matrix[1], initial_matrix[2], connections)

    # ----------------------- Breadth-search construction ----------------------
    if algorithm_input == "breadth-first": 
        matrix = bf.BreadthFirst(protein_string_converted[1:], initial_matrix[1], initial_matrix[2])
        matrix, protein = matrix.run()
        visualizer(matrix, protein)
        
    # ----------------------- Depth-first search construction ----------------------
    if algorithm_input == "depth-first":
        try:
            matrix = df.DepthFirst(protein_string_converted[1:], initial_matrix[1], initial_matrix[2])
            matrix, protein = matrix.run()
            visualizer(matrix, protein)
        except IndexError:
            print('finished')

    # ------------------------- Hill climber algorithm -------------------------
    if algorithm_input == "hillclimb":
        input_matrix = random_algorithm(initial_matrix[0], protein_string_converted[1:], initial_matrix[1], initial_matrix[2], connections)
        matrix = hill_climb(input_matrix[0], input_matrix[1], 3)

    #make plot
    #print(matrix[1].get_protein())

    # for row in matrix[0].get_matrix():    
        # print(row)
    # visualizer(matrix[0], matrix[1])
    
    
if __name__ == "__main__":
    if len(argv) != 3:
        print("Please provide a protein string and an algorithm in the command line")
        quit()
    
    string_input = int(argv[1])

    if string_input not in [1, 2, 3, 4, 5]:
        print("please choose one of the following strings by integer:\n 1: HHPHHHPHPHHHPH \n 2: HPHPPHHPHPPHPHHPPHPH")
        quit()

    if argv[2].lower() not in ["greedy", "random", "depth-first", "hillclimb", "breadth-first"]:
        print("please choose one of the following algorithms: \n random \n greedy \n depth-first \n hillclimb")
        quit()

    main(string_input, argv[2].lower())