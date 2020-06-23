import random
import numpy as np
import copy


def greedy(matrix, protein_string, amino_acid, protein, connections):    
    """Update the matrix with the remaining values of the protein string"""
    matrix = copy.deepcopy(matrix)
    protein = copy.deepcopy(protein)
    amino_acid = copy.deepcopy(amino_acid)

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

        if len(options) == 0:
            return "Terminate"

        change = False
        for key in options:
            
            if key == "up":
                # check up right left
                
                # Check for C neighbours, if found choose that position
                if matrix.get_matrix()[amino_acid.row + 2][amino_acid.column] == 3:
                    amino_acid.update_position(options[key][0], options[key][1])
                    change = True
                    break
                if matrix.get_matrix()[amino_acid.row + 1][amino_acid.column + 1] == 3:
                    amino_acid.update_position(options[key][0], options[key][1])
                    change = True
                    break
                if matrix.get_matrix()[amino_acid.row + 1][amino_acid.column - 1] == 3:
                    amino_acid.update_position(options[key][0], options[key][1])
                    change = True
                    break

                # Check for H neighbours, if found choose that position
                if matrix.get_matrix()[amino_acid.row + 2][amino_acid.column] == 1:
                    amino_acid.update_position(options[key][0], options[key][1])
                    change = True
                    break
                if matrix.get_matrix()[amino_acid.row + 1][amino_acid.column + 1] == 1:
                    amino_acid.update_position(options[key][0], options[key][1])
                    change = True
                    break
                if matrix.get_matrix()[amino_acid.row + 1][amino_acid.column - 1] == 1:
                    amino_acid.update_position(options[key][0], options[key][1])
                    change = True
                    break
                    
            if key == "down":
                # check down right left
                
                # check all connections for C neighbours, if one found choose it
                if matrix.get_matrix()[amino_acid.row - 2][amino_acid.column] == 3:
                    amino_acid.update_position(options[key][0], options[key][1])
                    change = True
                    break
                if matrix.get_matrix()[amino_acid.row - 1][amino_acid.column + 1] == 3:
                    amino_acid.update_position(options[key][0], options[key][1])
                    change = True
                    break
                if matrix.get_matrix()[amino_acid.row - 1][amino_acid.column - 1] == 3:
                    amino_acid.update_position(options[key][0], options[key][1])
                    change = True
                    break

                # Check all connections for H neighbours, if found choose one
                if matrix.get_matrix()[amino_acid.row - 2][amino_acid.column] == 1:
                    amino_acid.update_position(options[key][0], options[key][1])
                    change = True
                    break
                if matrix.get_matrix()[amino_acid.row - 1][amino_acid.column + 1] == 1:
                    amino_acid.update_position(options[key][0], options[key][1])
                    change = True
                    break
                if matrix.get_matrix()[amino_acid.row - 1][amino_acid.column - 1] == 1:
                    amino_acid.update_position(options[key][0], options[key][1])
                    change = True
                    break

            if key == "left":
                # check up down left
                # Check all connections for C, if one found, choose it
                if matrix.get_matrix()[amino_acid.row][amino_acid.column - 2] == 3:
                    amino_acid.update_position(options[key][0], options[key][1])
                    change = True
                    break
                if matrix.get_matrix()[amino_acid.row + 1][amino_acid.column - 1] == 3:
                    amino_acid.update_position(options[key][0], options[key][1])
                    change = True
                    break
                if matrix.get_matrix()[amino_acid.row - 1][amino_acid.column - 1] == 3:
                    amino_acid.update_position(options[key][0], options[key][1])
                    change = True
                    break
                # Check all connections for H, if one found, choose it
                if matrix.get_matrix()[amino_acid.row][amino_acid.column - 2] == 1:
                    amino_acid.update_position(options[key][0], options[key][1])
                    change = True
                    break
                if matrix.get_matrix()[amino_acid.row + 1][amino_acid.column - 1] == 1:
                    amino_acid.update_position(options[key][0], options[key][1])
                    change = True
                    break
                if matrix.get_matrix()[amino_acid.row - 1][amino_acid.column - 1] == 1:
                    amino_acid.update_position(options[key][0], options[key][1])
                    change = True
                    break

            if key == "right":
                # check up right down
                
                # check for C neighbours and choose position if found
                if matrix.get_matrix()[amino_acid.row][amino_acid.column + 2] == 3:
                    amino_acid.update_position(options[key][0], options[key][1])
                    change = True
                    break
                if matrix.get_matrix()[amino_acid.row + 1][amino_acid.column + 1] == 3:
                    amino_acid.update_position(options[key][0], options[key][1])
                    change = True
                    break
                if matrix.get_matrix()[amino_acid.row - 1][amino_acid.column + 1] == 3:
                    amino_acid.update_position(options[key][0], options[key][1])
                    change = True
                    break
                
                # check for H neighbours and choose position if found
                if matrix.get_matrix()[amino_acid.row][amino_acid.column + 2] == 1:
                    amino_acid.update_position(options[key][0], options[key][1])
                    change = True
                    break
                if matrix.get_matrix()[amino_acid.row + 1][amino_acid.column + 1] == 1:
                    amino_acid.update_position(options[key][0], options[key][1])
                    change = True
                    break
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


    return matrix, protein, protein.score_function()[0]