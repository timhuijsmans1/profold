from collections import deque
from queue import Queue
import copy
import math

from code.classes.matrix import Matrix


def breadth_first(matrix, protein_string, amino_acid, protein, connections):

    def graph(width, height):
 
    # REMOVE LATER - initiate matrix
        width = width
        height = height

        get_matrix = Matrix(width, height)

        neighbours = {}

        for i, row in enumerate(get_matrix.get_matrix()):

            for j, cell in enumerate(row):

                if i == 0 and j == 0:
                    neighbours[i, j] = [(i, j + 1), (i + 1, j)]
                elif i == 0 and j == height - 1:
                    neighbours[i, j] = [(i, j - 1), (i + 1, j)]
                elif i == width - 1 and j == 0:
                    neighbours[i, j] = [(i - 1, j), (i, j + 1)]
                elif i == width - 1 and j == height - 1:
                    neighbours[i, j] = [(i - 1, j), (i, j - 1)]
                elif i == 0:
                    neighbours[i, j] = [(i, j - 1), (i + 1, j), (i, j + 1)]
                elif j == 0:
                    neighbours[i, j] = [(i, j + 1), (i - 1, j), (i + 1, j)]
                elif i == width - 1:
                    neighbours[i, j] = [(i, j - 1), (i - 1, j), (i, j + 1)]
                elif j == height - 1:
                    neighbours[i, j] = [(i + 1, j), (i, j - 1), (i - 1, j)]
                else:
                    neighbours[i, j] = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]

        return neighbours

    neighbours_graph = graph(30, 30)

    new_graph = copy.deepcopy(neighbours_graph)

    Protein_String = protein_string

    Amino_Acid = amino_acid

    Protein = protein

    Connections = connections

    #length = len(protein_string)

    #def d_search():

    visited = set()
    stack = Queue()

    stack.put(Protein.get_protein()[0])

    # ff correct doen
    visited.add((15, 15))
    #stack.append[]

    i = 0

    while stack:

        #for i in range(6):

        current = stack.get(0)
        #print('current: ' + str(current))
        for i, item in enumerate(neighbours_graph[(current[0], current[1])]):

            matrix.update_matrix(current[0], current[1], protein_string[i + 1])

            print(matrix.get_matrix)

            #print('item iterate:' + str(item))
            if item not in visited:
                visited.add(item)
                #print('item added:' + str(item))
                stack.put(item)
                #i += 1
                #print('current stack: ' + str(stack.queue))
                #print('current visited: ' + str(visited))

                #if len(stack.queue) >= 14
                #    for i, value in enumerate(protein_string):
                #        if matrix.get_matrix()[amino_acid.row][amino_acid.column]
                #            connections.set_connections

        print('counting:' + str(i) + str(stack.queue))

        print(len(stack.queue))

    return matrix, protein


'''
import copy


class DepthFirst:
    """
    A Depth First algorithm that builds a stack of graphs with a unique assignment of nodes for each instance.
    """
    def __init__(self, graph, transmitters):
        self.graph = copy.deepcopy(graph)
        self.transmitters = transmitters

        self.states = [copy.deepcopy(self.graph)]

        self.best_solution = None
        self.best_value = float('inf')

    def get_next_state(self):
        """
        Method that gets the next state from the list of states.
        If we would want to make a breath first out of this, we could just
        make this pop(0).
        """
        return self.states.pop()

    def build_children(self, graph, node):
        """
        Creates all possible child-states and adds them to the list of states.
        """
        # Retrieve all valid possible values for the node.
        values = node.get_possibilities(self.transmitters)

        # Add an instance of the graph to the stack, with each unique value assigned to the node.
        for value in values:
            new_graph = copy.deepcopy(graph)
            new_graph.nodes[node.id].set_value(value)
            self.states.append(new_graph)

    def check_solution(self, new_graph):
        """
        Checks and accepts better solutions than the current solution.
        """
        new_value = new_graph.calculate_value()
        old_value = self.best_value

        # We are looking for maps that cost less!
        if new_value <= old_value:
            self.best_solution = new_graph
            self.best_value = new_value
            print(f"New best value: {self.best_value}")

    def run(self):
        """
        Runs the algorithm untill all possible states are visited.
        """
        while self.states:
            new_graph = self.get_next_state()

            # Retrieve the next empty node.
            node = new_graph.get_empty_node()

            if node is not None:
                self.build_children(new_graph, node)
            else:
                # Stop if we find a solution
                # self.graph = new_graph
                # return

                # Continue looking for better graphs.
                self.check_solution(new_graph)

        # Update the input graph with the best result found.
        self.graph = self.best_solution

'''



#def bfs(visited, graph, node):
#  visited.append(node)
#  queue.append(node)

#  while queue:
#    s = queue.pop(0) 
#    print (s, end = " ") 

#    for neighbour in graph[s]:
#      if neighbour not in visited:
#        visited.append(neighbour)
#        queue.append(neighbour)



    #print(Connections.set_connections('up', current[0], current[0]))

    # return Matrix, Protein

    #for value in protein_string:

        # check y connections and add to connections
        #if matrix.get_matrix()[amino_acid.row + 1][amino_acid.column] == 0:
            #connections.set_connections("up", 1, 0)
            
        #if matrix.get_matrix()[amino_acid.row - 1][amino_acid.column] == 0:
            #connections.set_connections("down", -1, 0)
        
        # check x connections and add to connections
        #if matrix.get_matrix()[amino_acid.row][amino_acid.column + 1] == 0:
            #connections.set_connections("right", 0, 1)
            
        #if matrix.get_matrix()[amino_acid.row][amino_acid.column - 1] == 0:
            #connections.set_connections("left", 0, -1)
        
        # from connections, find the best connection (high energy stability)
            # get connections
        #options = connections.connections

    #if Matrix.get_matrix()[amino_acid.row + 1][amino_acid.column] == 0:
    #        connections.set_connections("up", 1, 0)



    # for connections around initial aminoacid, make new proteins
      # 4 eiwitten: initial+up, initial+down, initial+left, initial+right
      # stack.append(initial+up)
    



    #visited = set()
    #deque = []

    #while deque:

    #    current = stack.popleft()

    #    print(stack)

        #for Connections.get_connections in current:
        #    print(Connections.get_connections)

    #search()


            #csacsd.append()

            #if neighbour