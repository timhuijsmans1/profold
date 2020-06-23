import copy

from code.helpers.pull_move import pull_move

def hill_climb(matrix, protein, iterations, tries):
    scores = []
    old_protein = copy.deepcopy(protein)

    for j in range(tries):
        check_protein = copy.deepcopy(old_protein)
        print(check_protein)
        print("old:",check_protein.protein)
        all_time_low = copy.deepcopy(check_protein.score_function()[0])

        for i in range(iterations):
            
            # set the input score to the score of the current protein
            input_score = check_protein.score_function()[0]

            # make a testable copy of the input protein    
            new_protein = copy.deepcopy(check_protein)

            # make a pull change to the testable copy
            new_protein = pull_move(new_protein, j)

            # accept the new protein if it's equal to or better than the previous protein
            if new_protein.score_function()[0] <= input_score:
                check_protein = copy.deepcopy(new_protein)
                
            if new_protein.score_function()[0] <= all_time_low:
                all_time_low = copy.deepcopy(new_protein.score_function()[0])
                best_protein = copy.deepcopy(new_protein)

        print("new",new_protein.protein)
        scores.append(all_time_low)

        print("try",j,"uit",tries)
    print(scores)
    #print(all_time_low)
    return matrix, best_protein
    


