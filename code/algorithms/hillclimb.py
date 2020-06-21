import copy

from code.helpers.pull_move import pull_move

def hill_climb(matrix, protein, iterations):

    old_protein = copy.deepcopy(protein)
    old_score = old_protein.score_function()
    all_time_low = old_score

    for i in range(iterations):
        
        # -------------!!!!!!!!!!!! original protein string is used as input for the fold again, we want the new protein string to become the input--------!!!!!!
        test_protein = copy.deepcopy(old_protein)
        plot_protein = pull_move(test_protein, matrix)
        old_protein = plot_protein

        # check the score of the molecule
        #if test_protein.score_function() < old_score and test_protein.score_function() < all_time_low:
        #    old_score = test_protein.score_function()
        #    all_time_low = test_protein.score_function()
        #    old_protein = test_protein

    # return the new molecule if a better one was found, otherwise return the old molecule
    return matrix,plot_protein