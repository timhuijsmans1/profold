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
        
        # from connections, find the best connection (high energy stability)
            # get connections
        options = connections.connections
        print(options)

        change = False
        for key in options:
            print(key)
            if key == "up":
                # check up right left
                # if coordinaat van up + up == H: choose connection
                if matrix.get_matrix()[amino_acid.row + 2][amino_acid.column] == "H":
                    amino_acid.update_position(options[key][0], options[key][1])
                    change = True
                    break

                # if coordinaat van up + right == H: choose connection
                if matrix.get_matrix()[amino_acid.row + 1][amino_acid.column + 1] == "H":
                    amino_acid.update_position(options[key][0], options[key][1])
                    change = True
                    break

                # if coordinaat van up + left == H: choose connection
                if matrix.get_matrix()[amino_acid.row + 1][amino_acid.column - 1] == "H":
                    amino_acid.update_position(options[key][0], options[key][1])
                    change = True
                    break
                    
            if key == "down":
                # check down right left
                # if coordinaat van down + down == H: choose connection
                if matrix.get_matrix()[amino_acid.row - 2][amino_acid.column] == "H":
                    amino_acid.update_position(options[key][0], options[key][1])
                    change = True
                    break

                # if coordinaat van down + right == H: choose connection
                if matrix.get_matrix()[amino_acid.row - 1][amino_acid.column + 1] == "H":
                    amino_acid.update_position(options[key][0], options[key][1])
                    change = True
                    break

                # if coordinaat van down + left == H: choose connection
                if matrix.get_matrix()[amino_acid.row - 1][amino_acid.column - 1] == "H":
                    amino_acid.update_position(options[key][0], options[key][1])
                    change = True
                    break


            if key == "left":
                # check up down left
                # if coordinaat van left + left == H: choose connection
                if matrix.get_matrix()[amino_acid.row][amino_acid.column - 2] == "H":
                    amino_acid.update_position(options[key][0], options[key][1])
                    change = True
                    break

                # if coordinaat van up + left == H: choose connection
                if matrix.get_matrix()[amino_acid.row + 1][amino_acid.column - 1] == "H":
                    amino_acid.update_position(options[key][0], options[key][1])
                    change = True
                    break

                # if coordinaat van down + left == H: choose connection
                if matrix.get_matrix()[amino_acid.row - 1][amino_acid.column - 1] == "H":
                    amino_acid.update_position(options[key][0], options[key][1])
                    change = True
                    break

            if key == "right":
                # check up right down
                # if coordinaat van right + right == H: choose connection
                if matrix.get_matrix()[amino_acid.row][amino_acid.column + 2] == "H":
                    amino_acid.update_position(options[key][0], options[key][1])
                    change = True
                    break

                # if coordinaat van up + right == H: choose connection
                if matrix.get_matrix()[amino_acid.row + 1][amino_acid.column + 1] == "H":
                    amino_acid.update_position(options[key][0], options[key][1])
                    change = True
                    break

                # if coordinaat van down + right == H: choose connection
                if matrix.get_matrix()[amino_acid.row - 1][amino_acid.column + 1] == "H":
                    amino_acid.update_position(options[key][0], options[key][1])
                    change = True
                    break
        
        # if no updates to amino_acid made, make a random step
        if change == False:
            step = connections.get_random_connection()
            amino_acid.update_position(step[1][0], step[1][1])
        
        # update amino acid value
        amino_acid.update_value(value)

        #place amino acid in matrix
        matrix.update_matrix(amino_acid.row, amino_acid.column, amino_acid.value)

        # place amino acid in protein string
        protein.add_amino_acid(amino_acid.row, amino_acid.column, amino_acid.value)

        # clear out connections  
        connections.clear_connections()

    return matrix, protein