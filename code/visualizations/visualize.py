import matplotlib.pyplot as plt
import numpy as np

def visualizer(matrix, protein):
    """Output: h*w matrix showing the folded protein and the
     list of aminoacid location in order of bonds"""    
    
    for row in matrix.get_matrix():
        print (row)
    print(protein.protein)
    #plt.imshow(matrix.get_matrix(), cmap=plt.cm.bwr)

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

    plt.plot(x, y, "k-", linewidth=2)
    plt.plot(x_H, y_H, "bo", markersize=12)
    plt.plot(x_P, y_P, "ro", markersize=12)
    plt.xticks(np.arange(10,20,1.0))
    plt.yticks(np.arange(10,20,1.0))
    plt.grid(True)

    plt.show()  