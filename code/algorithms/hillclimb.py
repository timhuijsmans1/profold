import copy

from code.helpers.pull_move import pull_move

def hill_climb(matrix, protein, iterations):

    all_time_low = copy.deepcopy(protein.score_function()[0])

    for i in range(iterations):
        
        # set the input score to the score of the current protein
        input_score = protein.score_function()[0]

        # make a testable copy of the input protein    
        new_protein = copy.deepcopy(protein)

        # make a pull change to the testable copy
        new_protein = pull_move(new_protein)

        print("protein:", protein.protein)
        print("new_protein:", new_protein.protein)

        # accept the new protein if it's equal to or better than the previous protein
        if new_protein.score_function()[0] <= input_score:
            protein = copy.deepcopy(new_protein)
            
        if new_protein.score_function()[0] <= all_time_low:
            all_time_low = copy.deepcopy(new_protein.score_function()[0])
            best_protein = copy.deepcopy(new_protein)

        
    
    print(all_time_low)
    return matrix, best_protein
    


