import matplotlib.pyplot as plt
import numpy as np

def visualizer(matrix, protein, algorithm_name):
    """Output: h*w matrix showing the folded protein and the
     list of aminoacid location in order of bonds"""    

    score = protein.score_function()[0]
    neighbours = protein.score_function()[1]
    # make H amino acid
    x_H = []
    y_H = []

    # make P amino acid
    x_P = []
    y_P = []
    # make C amino cid
    x_C = []
    y_C = []

    # make the X and Y axes
    x = []
    y = []   
    
    # place amino acids
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

    # show dotted line for neighbours
    for neighbour in neighbours:
        plt.plot([neighbour[0],neighbour[1]], [neighbour[2], neighbour[3]], color="k", linestyle="dotted")
    
    # set the connection lines
    plt.plot(x, y, "k-", linewidth=2)
    plt.plot(x_H, y_H, "bo", markersize=12)
    plt.plot(x_P, y_P, "ro", markersize=12)
    plt.plot(x_H, y_H, "ro", markersize=12)
    plt.plot(x_P, y_P, "bo", markersize=12)

    if len(x_C) > 0:    
        plt.plot(x_C, y_C, "go", markersize=12)

    # set ticks
    plt.xticks(np.arange(8, 22, 1.0))
    plt.yticks(np.arange(8, 22, 1.0))

    # make, place and show labels, title and score
    plt.ylabel('protein height')
    plt.xlabel('protein width')
    plt.grid(True)
    plt.title(f"algorithm: {algorithm_name}")
    plt.suptitle(f"score: {score}")
    plt.show()  