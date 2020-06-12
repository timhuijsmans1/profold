import matplotlib.pyplot as plt

def visualizer(matrix, protein):
    """Output: h*w matrix showing the folded protein and the
     list of aminoacid location in order of bonds"""    
    
    for row in matrix.get_matrix():
        print (row)
    print(protein.protein)
    #plt.imshow(matrix.get_matrix(), cmap=plt.cm.bwr)
<<<<<<< HEAD
    #plt.show()

    x = []
    y = []
=======

    y = []
    x = []
>>>>>>> ed8535aab33faf5d848f63457a7052ec838c0afa

    for item in protein.protein:
        x.append(item[0])
        y.append(item[1])

    plt.plot(x, y, "bo-", linewidth=2, markersize=12)
    plt.grid(True)

    plt.show()  