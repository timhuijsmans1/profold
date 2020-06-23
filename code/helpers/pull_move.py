import random
import copy

def pull_move(protein_string, matrix_input):

    # define protein list
    protein = protein_string.get_protein()
    print(protein)
    matrix = matrix_input.get_matrix()
    
    # choose random point i in the string
    vertex_index = random.randint(0, (len(protein)-1))
    
    pulled = False
    
    # keep trying new vertices until a valid pull vertex is found
    while pulled == False:
        print(vertex_index)
        # make direct initial fold of the endpoint
        if vertex_index == len(protein) - 1:
            # ---------find initial diagonals for i and i - 1------------

            print("I folded the end")
            pulled = True

        # make a pull move for all but the last amino acid
        else: 
            x_i = protein[vertex_index][0]
            y_i = protein[vertex_index][1]

            x_i1 = protein[vertex_index + 1][0]
            y_i1 = protein[vertex_index + 1][1]

            x_imin1 = protein[vertex_index - 1][0]
            y_imin1 = protein[vertex_index - 1][1]
            
            # make a pull move to down-left
            if x_i > x_i1:
                print("I'm going down left")
                direction = "down-left"
                diagonal_adjecent_min1 = [x_imin1 - 1, y_imin1 - 1]

            # make a pull move to up-right
            if x_i < x_i1:
                print("I'm going up right")
                direction = "up-right"
                diagonal_adjecent_min1 = [x_imin1 + 1, y_imin1 + 1]
            
            # make a pull move to up-left
            if y_i < y_i1:
                print("I'm going up left")
                direction = "up-left"
                diagonal_adjecent_min1 = [x_imin1 - 1, y_imin1 + 1]
            
            # make a pull move to down-right
            if y_i > y_i1:
                print("I'm going down right")
                direction = "down-right"
                diagonal_adjecent_min1 = [x_imin1 + 1, y_imin1 - 1]

            # set diagonal coordinates
            protein_string.set_diagonals(direction, x_i, y_i)
            matrix_input.set_diagonals(direction, x_i, y_i)   

            # diagonals in matrix and protein objects
            x_L = protein_string.x_L
            y_L = protein_string.y_L
            x_LL = protein_string.x_LL
            y_LL = protein_string.y_LL
            x_C = protein_string.x_C
            y_C = protein_string.y_C

            col_L = matrix_input.col_L
            row_L = matrix_input.row_L
            col_C = matrix_input.col_C
            row_C = matrix_input.row_C

            # folding the string start protein
            if vertex_index == 0:
                # make a move to L or LL depending on which one is available
                if matrix[y_L][x_L] == 0:
                    protein_string.change_amino_acid(x_L,y_L,vertex_index)
                    print("I folded begin to L")
                    pulled = True
                if matrix[y_LL][x_LL] == 0:
                    #make move to LL
                    protein_string.change_amino_acid(x_LL,y_LL,vertex_index)
                    print("I folded begin to LL")
                    pulled = True
                
            else:
                print ("sneak",x_imin1, x_C, y_imin1, y_C)
                print("ching",row_C,col_C,[x_C, y_C], diagonal_adjecent_min1)
                # check if C is occupied by i - 1
                if (matrix[row_L][col_L] == 0 and x_imin1 == x_C and y_imin1 == y_C):
                    # execute the pull move only on i
                    protein_string.change_amino_acid(x_L, y_L, vertex_index)
                    print("I pulled sneak")
                    pulled = True

                
                # check if C is empty but diagonally adjecent to i -1
                elif (matrix[row_L][col_L] == 0 and matrix[row_C][col_C] == 0 and [x_C, y_C] == diagonal_adjecent_min1):
                    # execute the pull move on both i and i - 1
                    protein_string.change_amino_acid(x_L, y_L, vertex_index)
                    protein_string.change_amino_acid(x_C, y_C, vertex_index - 1)
                    print("I pulled ching")
                    pulled = True
                
                else:
                    print("I did not pull")
                    vertex_index = random.randint(0, len(protein) - 1) 
        
        # check if the protein is now a valid adjecent protein
        # by checking if the string is actually a continues string

        # while the protein is not valid, keep shifting previous aminos two vertices up the old chain coordinates for the new string

        # after everything is sorted out, update the old chain to the found right chain such that both copies are now equal


        



    # make the diagonal move of i

    # check the occupation of C: if occupied by i - 1, the protein is valid and can be returned

    # if C if free, make the move of i - 1 to C

    # return the protein molecule that was found as the new molecule
    return(protein_string)

    
    