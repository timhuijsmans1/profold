import copy

class BreadthFirst:    
    def __init__(self, protein_string, amino_acid, protein):  
        self.protein_string = protein_string
        self.amino_acid = amino_acid
        self.protein = protein
        self.lowest_score = 0   

        self.queue = [self.protein]
        #self.visited = [[self.protein.protein[0][0],self.protein.protein[0][1]]]

    # take the parent out of the queue
    def breadth_pop(self, length, index):
        print(length,index)
        self.parent_protein = self.queue.pop(0)
        print("---------------")
        return self.parent_protein # object
    
    def get_last_amino(self, parent_protein):
        self.amino_acid_list = self.parent_protein.protein[-1]

        return self.amino_acid_list # list

    def create_children(self, amino_acid, index): # list and int
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

                # create a list of visited coordinates
                visited = []
                for amino in self.parent_protein.protein:
                    visited.append([amino[0],amino[1]])

                # alter the child amino according to the available connections
                self.child_amino[j] += i # change list

                if [self.child_amino[0],self.child_amino[1]] not in visited: # check if list in list
                    
                    # make the next amino acid for the child protein
                    self.amino_object.make_amino(self.child_amino[0], self.child_amino[1], self.protein_string[index])
                    amino_children.append(copy.deepcopy(self.amino_object))

        # create all the individual children and add them to the queue
        for child_amino in amino_children: # search list of objects

            self.child = copy.deepcopy(self.parent_protein) # copy the original protein object

            # add child_amino to self.child
            self.child.add_amino_acid(child_amino.row, child_amino.column, child_amino.value)

            # check the score and save the lowest score and its protein
            self.score = self.child.score_function()[0]
        
            if self.score <= self.lowest_score:
                self.lowest_score = copy.deepcopy(self.score)
                self.best_protein = copy.deepcopy(self.child)

            # append a deepcopy of the child to the queue
            self.queue.append(copy.deepcopy(self.child))

        return self.queue, self.lowest_score, self.best_protein

    # run the object for every index
    def run(self):
        
        new_queue = self.queue

        for index in range(0,len(self.protein_string)):
            while len(new_queue[0].protein) - 1 == index:
                parent_protein = self.breadth_pop(len(new_queue[0].protein) - 1, index)

                amino = self.get_last_amino(parent_protein)

                result = self.create_children(amino, index)
                new_queue = result[0]
        print("best score:", result[1])
        return [[]], result[2]