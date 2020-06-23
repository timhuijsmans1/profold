import random

class Connection:
    """Store the connections of the previous amino acid"""
    def __init__(self):
        self.connections = {}
        
    def set_connections(self, direction, row, column):
        self.connections[direction] = [row,column]
        return self.connections

    def get_connections(self):
        return self.connections 

    def get_random_connection(self):
        if len(self.connections) == 0:    
            return False
        else:
            return random.choice(list(self.connections.items()))
        
    def clear_connections(self):
        self.connections = {}
        return self.connections