import random
import copy

def pull_move(protein_string):

    # define protein list
    old_protein = protein_string.protein
    new_protein_string = copy.deepcopy(protein_string)
    new_protein = copy.deepcopy(new_protein_string.protein)

    occupied_coordinates = []

    for amino in new_protein:
        occupied_coordinates.append([amino[0],amino[1]])
    
    # choose random point i in the string
    vertex_index = random.randint(0, (len(new_protein)-1))
    
    pulled = False
    
    # keep trying new vertices until a valid pull vertex is found
    while pulled == False:
        # make direct initial fold of the endpoint
        if vertex_index == len(new_protein) - 1:
            # ---------find initial diagonals for i and i - 1------------

            print("I folded the end")
            pulled = True

        # make a pull move for all but the last amino acid
        else: 
            x_i = new_protein[vertex_index][0]
            y_i = new_protein[vertex_index][1]

            x_i1 = new_protein[vertex_index + 1][0]
            y_i1 = new_protein[vertex_index + 1][1]

            x_imin1 = new_protein[vertex_index - 1][0]
            y_imin1 = new_protein[vertex_index - 1][1]
            
            # make a pull move to down-left
            if x_i > x_i1:
                #print("I'm going down left")
                direction = "down-left"
                diagonal_adjecent_min1 = [x_imin1 - 1, y_imin1 - 1]

            # make a pull move to up-right
            if x_i < x_i1:
                #print("I'm going up right")
                direction = "up-right"
                diagonal_adjecent_min1 = [x_imin1 + 1, y_imin1 + 1]
            
            # make a pull move to up-left
            if y_i < y_i1:
                #print("I'm going up left")
                direction = "up-left"
                diagonal_adjecent_min1 = [x_imin1 - 1, y_imin1 + 1]
            
            # make a pull move to down-right
            if y_i > y_i1:
                #print("I'm going down right")
                direction = "down-right"
                diagonal_adjecent_min1 = [x_imin1 + 1, y_imin1 - 1]

            # set diagonal coordinates
            new_protein_string.set_diagonals(direction, x_i, y_i)

            # diagonals in matrix and protein objects
            x_L = new_protein_string.x_L
            y_L = new_protein_string.y_L
            x_LL = new_protein_string.x_LL
            y_LL = new_protein_string.y_LL
            x_C = new_protein_string.x_C
            y_C = new_protein_string.y_C

            # folding the string start protein
            if vertex_index == 0:
                
                # make a move to L or LL depending on which one is available
                if [x_L,y_L] not in occupied_coordinates:
                    new_protein_string.change_amino_acid(x_L,y_L,vertex_index)
                    
                    # update occupied coordinates
                    occupied_coordinates[vertex_index] = [x_L,y_L]

                    print("I folded begin to L")
                    pulled = True
                
                elif [x_LL, y_LL] not in occupied_coordinates:
                    #make move to LL
                    new_protein_string.change_amino_acid(x_LL,y_LL,vertex_index)
                    
                    # update occupied coordinates
                    occupied_coordinates[vertex_index] = [x_LL,y_LL]

                    print("I folded begin to LL")
                    pulled = True
                
                else:
                    print("I did not pull")
                    vertex_index = random.randint(0, len(new_protein) - 1)
                
            else:
                # check if C is occupied by i - 1
                if ([x_L,y_L] not in occupied_coordinates and x_imin1 == x_C and y_imin1 == y_C):
                    # execute the pull move only on i
                    new_protein_string.change_amino_acid(x_L, y_L, vertex_index)

                    # update occupied coordinates
                    occupied_coordinates[vertex_index] = [x_L,y_L]

                    print("I pulled sneak")
                    pulled = True

                
                # check if C is empty but diagonally adjecent to i -1 and L is empty
                elif ([x_L,y_L] not in occupied_coordinates and [x_C,y_C] not in occupied_coordinates and [x_C, y_C] == diagonal_adjecent_min1):
                    # execute the pull move on both i and i - 1
                    new_protein_string.change_amino_acid(x_L, y_L, vertex_index)
                    new_protein_string.change_amino_acid(x_C, y_C, vertex_index - 1)

                    # update occupied coordinates
                    occupied_coordinates[vertex_index] = [x_L,y_L]
                    occupied_coordinates[vertex_index - 1] = [x_C,y_C]

                    print("I pulled ching")
                    pulled = True
                
                else:
                    vertex_index = random.randint(0, len(new_protein) - 1) 
    
    neighbours = new_protein_string.get_neighbours()
    valid = new_protein_string.is_valid(neighbours)
    #print(valid)

    while valid == False:
        for j in range(len(new_protein)):
            
            new_protein_string.change_amino_acid(old_protein[vertex_index - j][0], old_protein[vertex_index - j][1], (vertex_index - (2 + j)) ) 

            new_neighbours = new_protein_string.get_neighbours()
            valid = new_protein_string.is_valid(new_neighbours)

            if valid == True:
                
                break

    return(new_protein_string)

    
    