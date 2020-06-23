import random


def random_algorithm(matrix, protein_string, amino_acid, protein, connections):    
    """Update the matrix with the remaining values of the protein string"""
    
    # place all other amino acids in the string on a random connected point

    for value in protein_string:    
        
        
        # check available positions in the y dimension
        if matrix.get_matrix()[amino_acid.row + 1][amino_acid.column] == 0:
            connections.set_connections("up", 1, 0)
        
        if matrix.get_matrix()[amino_acid.row - 1][amino_acid.column] == 0:
            connections.set_connections("down", -1, 0)
        
        # check available posisitions in the x dimension    
        if matrix.get_matrix()[amino_acid.row][amino_acid.column + 1] == 0:
            connections.set_connections("right", 0, 1)
            
        if matrix.get_matrix()[amino_acid.row][amino_acid.column - 1] == 0:
            connections.set_connections("left", 0, -1)
        
        # pick a random connection from the connections
        step = connections.get_random_connection()

        # update the value and position of the amino acid
        amino_acid.update_value(value)
        amino_acid.update_position(step[1][0], step[1][1])
        
        # update the matrix with the next amino acid
        matrix.update_matrix(amino_acid.row, amino_acid.column, amino_acid.value)
        
        # add the coordinates and value of the amino acid to the Protein
        protein.add_amino_acid(amino_acid.row, amino_acid.column, amino_acid.value)
        
        connections.clear_connections()
        #print(protein.get_protein())
        
    return matrix, protein
        
        
