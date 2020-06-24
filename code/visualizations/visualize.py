import matplotlib.pyplot as plt
import numpy as np

def visualizer(matrix, protein, algorithm_name):
    """Output: h*w matrix showing the folded protein and the
     list of aminoacid location in order of bonds"""    
    
    # for random algorithm just show the histogram
    if algorithm_name not in ["sneak"]:
        score = protein.score_function()[0]
        neighbours = protein.score_function()[1]

        # make H amino item
        x_H = []
        y_H = []

        # make P amino item
        x_P = []
        y_P = []
        
        # make C amino item
        x_C = []
        y_C = []

        # make line between amino acids
        x = []
        y = []   

        # make proteins
        for item in protein.protein:
            x.append(item[0])
            y.append(item[1])

            if item[2] == 1:
                x_H.append(item[0])
                y_H.append(item[1])

            if item[2] == 2:
                x_P.append(item[0])
                y_P.append(item[1])

            if item[2] == 3:
                x_C.append(item[0])
                y_C.append(item[1])

        # draw dotted line between neighbours
        for neighbour in neighbours:
            plt.plot([neighbour[0],neighbour[1]], [neighbour[2], neighbour[3]], color="k", linestyle="dotted")
        plt.plot([neighbours[-1][0],neighbours[-1][1]], [neighbours[-1][2], neighbours[-1][3]], color="k", linestyle="dotted", label ="neighbours")
        plt.plot(x, y, "k-", linewidth=2, label ="connected amino's")

        #plt.plot(x_H, y_H, "bo", markersize=12,)
        #plt.plot(x_P, y_P, "ro", markersize=12)

        plt.plot(x_H, y_H, "ro", markersize=12, label ="H")
        plt.plot(x_P, y_P, "bo", markersize=12, label ="P")

        # plot the C amino acid if present
        if len(x_C) > 0:    
            plt.plot(x_C, y_C, "go", markersize=12, label ="C")

        plt.xticks(np.arange(36,57,1.0))
        plt.yticks(np.arange(40,58,1.0))
        plt.ylabel('protein height')
        plt.xlabel('protein width')
        plt.grid(True)
        plt.title(f"algorithm: {algorithm_name}")
        plt.suptitle(f"score: {score}")
        plt.legend()
        

        plt.show()  
