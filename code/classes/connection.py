import random

class Connection:
    """Store the connections of the previous amino acid"""
    def __init__(self):
        self.connections = {}
        
    def set_connections(self, direction, row, column):
        self.connections[direction] = [row,column]
        return self.connections
    
    def set_connections_breadth(self, current, row, column):
        self.connections[current] = [row, column]
        return self.connections

    def get_connections(self):
        return self.connections 

    def get_random_connection(self):
        return random.choice(list(self.connections.items()))
        
    def clear_connections(self):
        self.connections = {}
        return self.connections