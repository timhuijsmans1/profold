import matplotlib.pyplot as plt

def visualizer(matrix, protein):
    """Output: h*w matrix showing the folded protein and the
     list of aminoacid location in order of bonds"""    
    
    for row in matrix.get_matrix():
        print (row)
    print(protein.protein)
    #plt.imshow(matrix.get_matrix(), cmap=plt.cm.bwr)

    y = []
    x = []

    for item in protein.protein:
        x.append(item[0])
        y.append(item[1])

    plt.plot(x, y, "bo-", linewidth=2, markersize=12)
    plt.grid(True)

    plt.show()  