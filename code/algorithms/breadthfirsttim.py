import copy

class BreadthFirst:    
    def __init__(self, protein_string, amino_acid, protein):  
        self.protein_string = protein_string
        self.amino_acid = amino_acid
        self.protein = protein
        self.lowest_score = 0   

        self.queue = [self.protein] 

    # haal de parent uit de queue, 
    def breadth_pop(self):
        self.parent_protein = self.queue.pop(0)
        print("parent_protein", self.parent_protein.protein)
        return self.parent_protein # object

    def get_last_amino(self, parent_protein):
        self.amino_acid_list = self.parent_protein.protein[-1]
        print("last amino", self.amino_acid_list)
        return self.amino_acid_list # list

    def create_children(self, amino_acid, value): # list and int
        """Creates a list of all the free possible neighbours
             of the last amino acid of the parent protein"""
        
        amino_children = []
        directions = [-1,1]
        coordinates = [0,1]

        # up, down, left, right
        for i in directions:
            for j in coordinates:
                
                # keep track of the initial amino aciod
                self.child_amino = copy.deepcopy(amino_acid) # copy of list
                self.amino_object = copy.deepcopy(self.amino_acid)

                # alter the child amino according to the available connections
                self.child_amino[j] += i # change list
                if self.child_amino not in self.protein.protein: # check if list in list
                    
                    # make the next amino acid for the child protein
                    self.amino_object.make_amino(self.child_amino[0], self.child_amino[1], value)
                    amino_children.append(copy.deepcopy(self.amino_object))

        # create all the individual children and add them to the queue
        for child_amino in amino_children: # search list of objects

            self.child = copy.deepcopy(self.parent_protein) # copy the original protein object

            # aan self.child voegen we amino_child toe
            self.child.add_amino_acid(child_amino.row, child_amino.column, child_amino.value)

            # check the score and save the lowest score and it's protein
            self.score = self.child.score_function()[0]
        
            if self.score <= self.lowest_score:
                
                self.lowest_score = self.score
                self.best_protein = copy.deepcopy(self.child)

            # append a deepcopy of the child to the queue
            self.queue.append(copy.deepcopy(self.child))
            print("I appended", self.child.protein)
        print(self.queue)


        return self.queue, self.best_protein, self.lowest_score

    # run the object for every 
    def run(self):
        
        for value in self.protein_string:
            print(value)
            parent_protein = self.breadth_pop()

            amino = self.get_last_amino(parent_protein)

            new_queue = self.create_children(amino, value)
            
        return(new_queue)