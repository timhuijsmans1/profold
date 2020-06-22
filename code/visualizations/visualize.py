import matplotlib.pyplot as plt
import numpy as np

def visualizer(matrix, protein):
    """Output: h*w matrix showing the folded protein and the
     list of aminoacid location in order of bonds"""    

    score = protein.score_function()[0]
    neighbours = protein.score_function()[1]

    x_H = []
    y_H = []

    x_P = []
    y_P = []

    x = []
    y = []   

    for item in protein.protein:
        x.append(item[0])
        y.append(item[1])

        if item[2] == 1:
            x_H.append(item[0])
            y_H.append(item[1])

        if item[2] == 2:
            x_P.append(item[0])
            y_P.append(item[1])

    for neighbour in neighbours:
        plt.plot([neighbour[0],neighbour[1]], [neighbour[2], neighbour[3]], color="k", linestyle="dotted")
    plt.plot(x, y, "k-", linewidth=2)
    plt.plot(x_H, y_H, "ro", markersize=12)
    plt.plot(x_P, y_P, "bo", markersize=12)
    plt.xticks(np.arange(8,22,1.0))
    plt.yticks(np.arange(8,22,1.0))
    plt.grid(True)
    #plt.title("random fold")
    plt.suptitle(f"score: {score}")

    plt.show()  