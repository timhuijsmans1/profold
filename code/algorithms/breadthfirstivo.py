import copy

class BreadthFirst:

    def __init__(self, protein_string, amino_acid, protein):  
        self.protein_string = protein_string
        self.amino_acid = amino_acid
        self.protein = protein
        self.lowest_score = 0   

        self.queue = [self.protein]
        #self.visited = [[self.protein.protein[0][0],self.protein.protein[0][1]]]

    # haal de parent uit de queue, 
    def breadth_pop(self, length, index):
        print(length, index)
        self.parent_protein = self.queue.pop(0)
        print("---------------")
        
        return self.parent_protein # object
    
    def get_last_amino(self, parent_protein):
        self.amino_acid_list = self.parent_protein.protein[-1]
        
        return self.amino_acid_list # list

    def create_child(self, amino_acid, index):
        """  """
        
        amino_children = []
        directions = [-1, 1]
        coordinates = [0, 1]
        
        # up, down, left, right
        for i in directions:
            for j in coordinates:
                
                # keep track of the initial amino aciod
                self.child_amino = copy.deepcopy(amino_acid) # copy of list
                self.amino_object = copy.deepcopy(self.amino_acid)

                # create a list of visited coordinates
                visited = []
                for amino in self.parent_protein.protein:
                    #print('this is the append: ' + str([amino[0], amino[1]]))
                    #print('whole amino: ' + str(amino))
                    visited.append([amino[0], amino[1]])

                # alter the child amino according to the available connections
                self.child_amino[j] += i # change list

                if [self.child_amino[0], self.child_amino[1]] not in visited: # check if list in list
                    
                    # make the next amino acid for the child protein
                    self.amino_object.make_amino(self.child_amino[0], self.child_amino[1], self.protein_string[index])
                    amino_children.append(copy.deepcopy(self.amino_object))

        # create all the individual children and add them to the queue
        counter = 0

        for child_amino in amino_children: # search list of objects

            if counter == 0:

                counter += 1

                self.child = copy.deepcopy(self.parent_protein) # copy the original protein object

                # aan self.child voegen we amino_child toe
                self.child.add_amino_acid(child_amino.row, child_amino.column, child_amino.value)

                # check the score and save the lowest score and it's protein
                self.score = self.child.score_function()[0]

                if self.score <= self.lowest_score:
                    self.lowest_score = copy.deepcopy(self.score)
                    self.best_protein = copy.deepcopy(self.child)

                # append a deepcopy of the child to the queue
                self.queue.append(copy.deepcopy(self.child))

        return self.queue, self.lowest_score, self.best_protein

    def create_children(self, amino_acid, index):
        """Creates a list of all the free possible neighbours
             of the last amino acid of the parent protein"""

        amino_children = []
        directions = [-1, 1]
        coordinates = [0, 1]

        # up, down, left, right
        for i in directions:
            for j in coordinates:

                # keep track of the initial amino aciod
                self.child_amino = copy.deepcopy(amino_acid)  # copy of list
                self.amino_object = copy.deepcopy(self.amino_acid)

                # create a list of visited coordinates
                visited = []
                for amino in self.parent_protein.protein:
                    #print('this is the append: ' + str([amino[0], amino[1]]))
                    #print('whole amino: ' + str(amino))
                    visited.append([amino[0], amino[1]])

                # alter the child amino according to the available connections
                self.child_amino[j] += i  # change list

                if [self.child_amino[0], self.child_amino[1]] not in visited:  # check if list in list

                    # make the next amino acid for the child protein
                    self.amino_object.make_amino(self.child_amino[0], self.child_amino[1], self.protein_string[index])
                    amino_children.append(copy.deepcopy(self.amino_object))

        # create all the individual children and add them to the queue
        for child_amino in amino_children:  # search list of objects

            self.child = copy.deepcopy(self.parent_protein)  # copy the original protein object

            # aan self.child voegen we amino_child toe
            self.child.add_amino_acid(child_amino.row, child_amino.column, child_amino.value)

            # check the score and save the lowest score and it's protein
            self.score = self.child.score_function()[0]
            print(self.score)

            if self.score <= self.lowest_score:
                self.lowest_score = copy.deepcopy(self.score)
                self.best_protein = copy.deepcopy(self.child)
                self.queue.append(copy.deepcopy(self.child))

            # append a deepcopy of the child to the queue
            #self.queue.append(copy.deepcopy(self.child))

        return self.queue, self.lowest_score, self.best_protein


    # run the object for every
    def run(self):
        
        new_queue = self.queue
        #print('what is new que: ' + str(new_queue))

        iterate_counter = 0

        for index in range(0, len(self.protein_string)):
            #print('new que: ' + str(new_queue))
            while len(new_queue[0].protein) - 1 == index:
                iterate_counter += 1
                if iterate_counter == 1:
                    parent_protein = self.breadth_pop(len(new_queue[0].protein) - 1, index)

                    amino = self.get_last_amino(parent_protein)

                    result = self.create_child(amino, index)
                    new_queue = result[0]
                else:
                    parent_protein = self.breadth_pop(len(new_queue[0].protein) - 1, index)

                    print('parent_protein: ' + str(parent_protein.protein))
                    try:
                        print('new_queue: ' + str(new_queue[0]))
                        print('new_queue[0]: ' + str(new_queue[0]))
                        print('new_queue[0].protein: ' + str(new_queue[0].protein))
                    except IndexError:
                        print('fcked')
                    print('index: ' + str(index))

                    amino = self.get_last_amino(parent_protein)

                    result = self.create_children(amino, index)
                    new_queue = result[0]
        print("best score:", result[1])

        return [[]], result[2]