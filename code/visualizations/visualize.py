import matplotlib.pyplot as plt
import numpy as np

def visualizer(matrix, protein, algorithm_name):
    """Output: h*w matrix showing the folded protein and the
     list of aminoacid location in order of bonds"""    

    score = protein.score_function()[0]
    neighbours = protein.score_function()[1]

    x_H = []
    y_H = []

    x_P = []
    y_P = []

    #x_C = []
    #y_C = []

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

        #if item[2] == 3:
            #x_C.append(item[0])
            #y_C.append(item[1])

    for neighbour in neighbours:
        plt.plot([neighbour[0],neighbour[1]], [neighbour[2], neighbour[3]], color="k", linestyle="dotted")
    plt.plot(x, y, "k-", linewidth=2)
<<<<<<< HEAD
    plt.plot(x_H, y_H, "bo", markersize=12)
    plt.plot(x_P, y_P, "ro", markersize=12)
=======
    plt.plot(x_H, y_H, "ro", markersize=12)
    plt.plot(x_P, y_P, "bo", markersize=12)
    #plt.plot(x_C, y_C, "w", markersize=12)
>>>>>>> 24b114fe27dae04d5bf2b933d7a897310faa88b0
    plt.xticks(np.arange(8,22,1.0))
    plt.yticks(np.arange(8,22,1.0))
    plt.ylabel('protein height')
    plt.xlabel('protein width')
    plt.grid(True)
<<<<<<< HEAD
    plt.title(f"algorithm: {algorithm_name}")
=======
    plt.title("hill-climb fold")
>>>>>>> 24b114fe27dae04d5bf2b933d7a897310faa88b0
    plt.suptitle(f"score: {score}")

    plt.show()  