import matplotlib.pyplot as plt

def visualizer(matrix, protein):
    """Output: h*w matrix showing the folded protein and the
     list of aminoacid location in order of bonds"""    
    
    for row in matrix.get_matrix():
        print (row)
    print(protein.protein)
    plt.imshow(matrix.get_matrix(), cmap=plt.cm.bwr)
    plt.show()