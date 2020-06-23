import random
import numpy as np


def greedy(matrix, protein_string, amino_acid, protein, connections):    
    """Update the matrix with the remaining values of the protein string"""

    for value in protein_string:

        # check y connections and add to connections
        if matrix.get_matrix()[amino_acid.row + 1][amino_acid.column] == 0:
            connections.set_connections("up", 1, 0)
            
        if matrix.get_matrix()[amino_acid.row - 1][amino_acid.column] == 0:
            connections.set_connections("down", -1, 0)
        
        # check x connections and add to connections
        if matrix.get_matrix()[amino_acid.row][amino_acid.column + 1] == 0:
            connections.set_connections("right", 0, 1)
            
        if matrix.get_matrix()[amino_acid.row][amino_acid.column - 1] == 0:
            connections.set_connections("left", 0, -1)
        
        # from connections, find the best connection (lowest energy state)
        # get connections
        options = connections.connections

        change = False
        for key in options:
            
            if key == "up":
                # check up right left
                # if coordinate of up + up == H: choose connection
                if matrix.get_matrix()[amino_acid.row + 2][amino_acid.column] == 1:
                    amino_acid.update_position(options[key][0], options[key][1])
                    change = True
                    break

                # if coordinate of up + right == H: choose connection
                if matrix.get_matrix()[amino_acid.row + 1][amino_acid.column + 1] == 1:
                    amino_acid.update_position(options[key][0], options[key][1])
                    change = True
                    break

                # if coordinate of up + left == H: choose connection
                if matrix.get_matrix()[amino_acid.row + 1][amino_acid.column - 1] == 1:
                    amino_acid.update_position(options[key][0], options[key][1])
                    change = True
                    break
                    
            if key == "down":
                # check down right left
                # if coordinate of down + down == H: choose connection
                if matrix.get_matrix()[amino_acid.row - 2][amino_acid.column] == 1:
                    amino_acid.update_position(options[key][0], options[key][1])
                    change = True
                    break

                # if coordinate of down + right == H: choose connection
                if matrix.get_matrix()[amino_acid.row - 1][amino_acid.column + 1] == 1:
                    amino_acid.update_position(options[key][0], options[key][1])
                    change = True
                    break

                # if coordinate of down + left == H: choose connection
                if matrix.get_matrix()[amino_acid.row - 1][amino_acid.column - 1] == 1:
                    amino_acid.update_position(options[key][0], options[key][1])
                    change = True
                    break

            if key == "left":
                # check up down left
                # if coordinate of left + left == H: choose connection
                if matrix.get_matrix()[amino_acid.row][amino_acid.column - 2] == 1:
                    amino_acid.update_position(options[key][0], options[key][1])
                    change = True
                    break

                # if coordinate of up + left == H: choose connection
                if matrix.get_matrix()[amino_acid.row + 1][amino_acid.column - 1] == 1:
                    amino_acid.update_position(options[key][0], options[key][1])
                    change = True
                    break

                # if coordinate of down + left == H: choose connection
                if matrix.get_matrix()[amino_acid.row - 1][amino_acid.column - 1] == 1:
                    amino_acid.update_position(options[key][0], options[key][1])
                    change = True
                    break

            if key == "right":
                # check up right down
                # if coordinate of right + right == H: choose connection
                if matrix.get_matrix()[amino_acid.row][amino_acid.column + 2] == 1:
                    amino_acid.update_position(options[key][0], options[key][1])
                    change = True
                    break

                # if coordinate of up + right == H: choose connection
                if matrix.get_matrix()[amino_acid.row + 1][amino_acid.column + 1] == 1:
                    amino_acid.update_position(options[key][0], options[key][1])
                    change = True
                    break

                # if coordinate of down + right == H: choose connection
                if matrix.get_matrix()[amino_acid.row - 1][amino_acid.column + 1] == 1:
                    amino_acid.update_position(options[key][0], options[key][1])
                    change = True
                    break
                              
        # if the amino_acid made does not get updated, make a random step
        if change == False:
            step = connections.get_random_connection()
            amino_acid.update_position(step[1][0], step[1][1])
        
        # update the amino_acid value
        amino_acid.update_value(value)

        # place amino_acid in matrix
        matrix.update_matrix(amino_acid.row, amino_acid.column, amino_acid.value)

        # place amino_acid in protein string
        protein.add_amino_acid(amino_acid.row, amino_acid.column, amino_acid.value)

        # clear out connections  
        connections.clear_connections()

    print(protein.score_function()[0])

    return matrix, protein