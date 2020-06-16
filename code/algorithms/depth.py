"""
graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

visited = set() # Set to keep track of visited nodes.

def dfs(visited, graph, node):
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Driver Code
dfs(visited, graph, 'A')
"""


def depth_first_search(matrix, protein_string, amino_acid, protein, connections):
    """
    matrix: populates a 2d matrix with 0's, updates a cell in that matrix with a given value, returns itself
    protein_string: list of single char strings containing the amino acid to fold into a protein
    amino_acid: connects the placed proteins
    protein: remembers what amino acid has been placed where
    connections: stores the previous amino acid location and looks for adjecent cells
    """

    def position_levels(depth_level):

        depth_level = int(depth_level)

        directions = dict(
            up=['right', 'down', 'left'],
            right=['down', 'left', 'up'],
            down=['left', 'up', 'right'],
            left=['up', 'right', 'down']
        )

        for i in range(depth_level):
            print(i)
            for key, value in directions.items():
                print(key)
                for i in range(len(value)):
                    print(value[i])

        return None

    positions = position_levels(4)

    """
    for value in protein_string:


        # check y connections and add to connections
        if matrix.get_matrix()[amino_acid.row + 1][amino_acid.column] == 0:
            connections.set_connections("up", 1, 0)

        if matrix.get_matrix()[amino_acid.row - 1][amino_acid.column] == 0:
            connections.set_connections("down", -1, 0)

        # check x connections and add to connections
        if matrix.get_matrix()[amino_acid.row][amino_acid.column + 1] == 0:
            connections.set_connections("right", 0, 1)

        if matrix.get_matrix()[amino_acid.row][amino_acid.column - 1] == 0:
            connections.set_connections("left", 0, -1)

        # from connections, find the best connection (high energy stability)
        # get connections
        options = connections.connections

        change = False

        for key in options:
        """

    return matrix, protein, positions







