import copy
from matplotlib import pyplot as plt
import numpy as np

from code.helpers.pull_move import pull_move

def hill_climb(matrix, protein, iterations, tries):
    """Functie die de pull move een "try" aantal keer herhaalt. Als de pullmove
    een stabieler eiwit returned, wordt dit eiwit geaccepteerd en wordt vervolgens 
    daarop de pullmove weer uitgevoerd"""
    
    scores = []
    old_protein = copy.deepcopy(protein)

    # repeat the hill climb algorithm a "try" times
    for j in range(tries):
        print("climb",j+1,"van de",tries, "is bezig, even geduld")
        check_protein = copy.deepcopy(old_protein)
        all_time_low = copy.deepcopy(check_protein.score_function()[0])

        # repeat the pull move "iterations" times
        for i in range(iterations):
            
            # set the input score to the score of the current protein
            input_score = check_protein.score_function()[0]

            # make a testable copy of the input protein    
            new_protein = copy.deepcopy(check_protein)

            # make a pull change to the testable copy
            new_protein = pull_move(new_protein, j)

            # accept the new protein if it's equal to or better than the previous protein
            if new_protein.score_function()[0] < input_score:
                check_protein = copy.deepcopy(new_protein)

            # set the all time lowest score if it's reached    
            if new_protein.score_function()[0] <= all_time_low:
                all_time_low = copy.deepcopy(new_protein.score_function()[0])
                best_protein = copy.deepcopy(new_protein)

        scores.append(all_time_low)
    plt.hist(scores, 25)
    plt.title("Hill climber fold met enkelvoudige pull move en 2000 iteraties, 50 keer uitgevoerd")
    plt.ylabel("count")
    plt.xlabel("scores")
    plt.show()

    print("laagste scores van de climbs:", scores)
    #print(all_time_low)
    return matrix, best_protein
    


