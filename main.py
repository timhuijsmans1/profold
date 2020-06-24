from code.classes.matrix import Matrix
from code.classes.aminoacid import AminoAcid
from code.classes.protein import Protein
from code.classes.connection import Connection

from code.helpers.matrixinit import matrix_initializer
from code.helpers.stringconverter import string_converter

from code.algorithms.random import random_algorithm
from code.algorithms.greedy import greedy
from code.algorithms import breadthfirstheur as bf
from code.algorithms.hillclimb import hill_climb

from code.visualizations.visualize import visualizer

from matplotlib import pyplot as plt
from sys import argv
import numpy as np

def main(string_input, algorithm_input):

    # analyse user input to choose the string and convert to numerical string
    if string_input == 1:
        protein_string = ["H", "H", "P", "H", "H", "H", "P", "H", "P", "H", "H", "H", "P", "H"]
    
    if string_input == 2:
        protein_string = ["H", "P", "H", "P", "P", "H", "H", "P", "H", "P", "P", "H", "P", "H", "H", "P", "P", "H", "P", "H"]

    if string_input == 3:
        protein_string = ["P","P","P","H","H","P","P","H","P","P","P","P","P","H","H","H","H","H","H","H","P","P","H","H","P","P","P","P","H","H","P","P","H","P","P"]

    if string_input == 4:
        protein_string = ["H", "H", "P", "H", "P", "H", "P", "H", "P", "H", "H", "H", "H", "P", "H", "P", "P", "P", "H", "P", "P" , "P", "H", "P", "P", "P", "P", "H", "P", "P", "P", "H", "P", "P", "P", "H", "P", "H", "H", "H", "H", "P", "H", "P", "H", "P", "H", "P", "H", "H"]
    
    if string_input == 5:
        protein_string = ["P", "P", "C", "H", "H", "P", "P", "C", "H", "P", "P", "P", "P", "C", "H", "H", "H", "H", "C", "H", "H", "P", "P", "H", "H", "P", "P", "P", "H", "H", "P", "P", "H", "P", "P"]

    if string_input == 6:
        protein_string = ["C", "P", "P", "C", "H", "P", "P", "C", "H", "P", "P", "C", "P", "P", "H", "H", "H", "H", "H", "H", "C", "C", "P", "C", "H", "P", "P", "C", "P", "C", "H", "P", "P", "H", "P", "C"]

    if string_input == 7:
        protein_string = ["H", "C", "P", "H", "P", "C", "P", "H", "P", "C", "H", "C", "H", "P", "H", "P", "P", "P", "H", "P", "P", "P", "H", "P", "P", "P", "P", "H", "P", "C", "P", "H", "P", "P", "P", "H", "P", "H", "H", "H", "C", "C", "H", "C", "H", "C", "H", "C", "H", "H"]

    if string_input == 8:
        protein_string = ["H", "C", "P", "H", "P", "H", "P", "H", "C", "H", "H", "H", "H", "P", "C", "C", "P", "P", "H", "P", "P", "P", "H", "P", "P", "P", "P", "C", "P", "P", "P", "H", "P", "P", "P", "H", "P", "H", "H", "H", "H", "C", "H", "P", "H", "P", "H", "P", "H", "H"]  
        
    protein_string_converted = string_converter(protein_string)

    # set initial values
    height = int(len(protein_string_converted) * 2)
    width = int(len(protein_string_converted) * 2)
    
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
    # run the entire algorithm 1000 times and store all the scores, plot a histogram
    if algorithm_input == "random":
        scores = []
        
        for i in range(5000):
            solution = random_algorithm(initial_matrix[0], protein_string_converted[1:], initial_matrix[1], initial_matrix[2], connections)
            print("solution:",i,"out of 10.000")
            if solution == "Terminate":
                pass
            else: 
                matrix, protein, score = solution
                scores.append(score)

        plt.hist(scores, 20)
        plt.title("Counts for random scores of 10.000 iterations")
        plt.xticks(np.arange(-50,0,1.0))
        plt.ylabel("count")
        plt.xlabel("score")
        plt.show()


    # ----------------------- Greedy construction ------------------------------
    if algorithm_input == "greedy":
        scores = []
        for i in range(5000):
            solution = greedy(initial_matrix[0], protein_string_converted[1:], initial_matrix[1], initial_matrix[2], connections)
            print("solution:",i,"out of 10.000")
            if solution == "Terminate":
                pass
            else: 
                matrix, protein, score = solution
                scores.append(score)

        plt.hist(scores, 20)
        plt.title("Counts for greedy scores of 10.000 iterations")
        plt.xticks(np.arange(-30,0,5))
        plt.ylabel("count")
        plt.xlabel("score")
        plt.show()
    # ----------------------- Breadth-search construction ----------------------
    if algorithm_input == "breadth-first": 
        matrix = bf.BreadthFirst(protein_string_converted[1:], initial_matrix[1], initial_matrix[2])
        matrix, protein = matrix.run()

    # ------------------------- Hill climber algorithm -------------------------
    if algorithm_input == "hillclimb":
        input_matrix = random_algorithm(initial_matrix[0], protein_string_converted[1:], initial_matrix[1], initial_matrix[2], connections)
        matrix, protein = hill_climb(input_matrix[0], input_matrix[1], 300, 1)
        
    visualizer(matrix, protein, algorithm_input)

# call main function and process the command line arguments    
if __name__ == "__main__":

    # return error if the command line arguments are to few
    if len(argv) != 3:
        print("Please provide a protein string and an algorithm in the command line")
        quit()
    
    # process the second argument as an integer for usage below
    string_input = int(argv[1])

    # check if the given
    if string_input not in [1, 2, 3, 4, 5, 6, 7, 8]:
        print("please choose one of the following strings by integer:\n1: HHPHHHPHPHHHPH \n2: HPHPPHHPHPPHPHHPPHPH \n3: PPPHHPPHHPPPPPHHHHHHHPPHHPPPPHHPPHPP \n" + \
        "4: HHPHPHPHPHHHHPHPPPHPPPHPPPPHPPPHPPPHPHHHHPHPHPHPHH \n5: PPCHHPPCHPPPPCHHHHCHHPPHHPPPPHHPPHPP \n"+ \
        "6: CPPCHPPCHPPCPPHHHHHHCCPCHPPCPCHPPHPC \n" + \
        "7: HCPHPCPHPCHCHPHPPPHPPPHPPPPHPCPHPPPHPHHHCCHCHCHCHH \n" + \
        "8: HCPHPHPHCHHHHPCCPPHPPPHPPPPCPPPHPPPHPHHHHCHPHPHPHH")
        quit()

    # check the algorithm input
    if argv[2].lower() not in ["greedy", "random", "hillclimb", "breadth-first"]:
        print("please choose one of the following algorithms: \n random \n greedy \n breadth-first \n hillclimb")
        quit()

    main(string_input, argv[2].lower())