import copy

class BreadthFirst:
    """
    Breadth-first algoritm, adding proteine's to a que (FIFO)
    """

    # initialize all other classes
    def __init__(self, protein_string, amino_acid, protein):  
        self.protein_string = protein_string
        self.amino_acid = amino_acid
        self.protein = protein
        self.lowest_score = 0
        self.checker = 0

        self.queue = [self.protein]

    # take the first parent protein string out of the queue (FIFO) and pass it's length and index
    def breadth_pop(self, length, index):
        print(length, index)
        self.parent_protein = self.queue.pop(0)
        print("---------------")
        
        return self.parent_protein
    
    # get the last amino acid from the protein
    def get_last_amino(self, parent_protein):
        self.amino_acid_list = self.parent_protein.protein[-1]
        
        return self.amino_acid_list

    # for the first time a child needs to be created, this method needs to be run instead of create_children, in order
    # to cut the matrix into 1/4 and thus preventing allot of mirrored protein strings
    def create_child(self, amino_acid, index):

        # initialze list used in this method 
        amino_children = []
        directions = [-1, 1]
        coordinates = [0, 1]
        
        # look in the different directions (up, down, left and right)
        for i in directions:
            for j in coordinates:
                
                # keep track of the initial amino acid
                self.child_amino = copy.deepcopy(amino_acid) # copy of list
                self.amino_object = copy.deepcopy(self.amino_acid)

                # create a list of visited coordinates
                visited = []
                for amino in self.parent_protein.protein:
                    visited.append([amino[0], amino[1]])

                # alter the child_amino according to the available connections
                self.child_amino[j] += i # change list

                if [self.child_amino[0], self.child_amino[1]] not in visited: # check if list in list
                    
                    # make the next amino acid for the child protein
                    self.amino_object.make_amino(self.child_amino[0], self.child_amino[1], self.protein_string[index])
                    amino_children.append(copy.deepcopy(self.amino_object))

        # counter regulates the placement of only 1 child the first iteration in order to reduce the matrix by 1/4
        counter = 0
        
        # Place only 1 child the first iteration in order to reduce the matrix by 1/4
        for child_amino in amino_children:

            # place first child
            if counter == 0:

                counter += 1

                # copy the original protein object
                self.child = copy.deepcopy(self.parent_protein) 

                # add child_amino to self.child
                self.child.add_amino_acid(child_amino.row, child_amino.column, child_amino.value)

                # check the score and save the lowest score and its protein
                self.score = self.child.score_function()[0]

                # check for the lowest score
                if self.score <= self.lowest_score:
                    self.lowest_score = copy.deepcopy(self.score)
                    self.best_protein = copy.deepcopy(self.child)

                # append a deepcopy of the child to the queue
                self.queue.append(copy.deepcopy(self.child))

        return self.queue, self.lowest_score, self.best_protein


    def create_children(self, amino_acid, index):
        """
        Creates a list of all the free possible neighbours of the last amino acid of the parent protein
        """

        # initialze list used in this method 
        amino_children = []
        directions = [-1, 1]
        coordinates = [0, 1]

        # look in the different directions (up, down, left and right)
        for i in directions:
            for j in coordinates:

                # keep track of the initial amino acid
                self.child_amino = copy.deepcopy(amino_acid)
                self.amino_object = copy.deepcopy(self.amino_acid)

                # create a list of visited coordinates
                visited = []
                for amino in self.parent_protein.protein:
                    visited.append([amino[0], amino[1]])

                # alter the child amino according to the available connections
                self.child_amino[j] += i  # change list

                if [self.child_amino[0], self.child_amino[1]] not in visited:

                    # make the next amino acid for the child protein
                    self.amino_object.make_amino(self.child_amino[0], self.child_amino[1], self.protein_string[index])
                    amino_children.append(copy.deepcopy(self.amino_object))
       
        # create all the individual children and add them to the queue
        for child_amino in amino_children:  # search list of objects

            # copy the original protein object
            self.child = copy.deepcopy(self.parent_protein)  
            
            # add child_amino to self.child
            self.child.add_amino_acid(child_amino.row, child_amino.column, child_amino.value)

            # check the score and save the lowest score and its protein
            self.score = self.child.score_function()[0]
            
            # prune, in case of a protein string that is shorter than 21 amino acids, append all children of the first 11 amino acids
            if len(self.protein_string) < 21:

                # append all the children                                                                             
                if len(self.parent_protein.protein) <= 11:
                    self.queue.append(copy.deepcopy(self.child))

                # append the best children
                elif self.score <= self.lowest_score:
                    self.lowest_score = copy.deepcopy(self.score)
                    self.best_protein = copy.deepcopy(self.child)
                    self.queue.append(copy.deepcopy(self.child))
                
            else:
                # append all the children
                if len(self.parent_protein.protein) <= 5:
                    self.queue.append(copy.deepcopy(self.child))
                    
                # append the best children
                elif self.score <= self.lowest_score:
                    self.lowest_score = copy.deepcopy(self.score)
                    self.best_protein = copy.deepcopy(self.child)
                    self.queue.append(copy.deepcopy(self.child))                

        return self.queue, self.lowest_score, self.best_protein

    # run the object for one of 8 strings
    def run(self):
        
        # declare variables for this method
        new_queue = self.queue
        iterate_counter = 0

        # loop over amino acids of the given proteine string
        for index in range(0, len(self.protein_string)):

            # print the index of the current amino in the protein string
            print('starting: ' + str(index))

            # keep repeating while the length of the created string equals the length
            while len(new_queue[0].protein) - 1 == index:
                print('protein string index: ' + str(index))
                iterate_counter += 1

                # place only the first child amino acid in order to limit the matrix by 1/4
                if iterate_counter == 1:
                    parent_protein = self.breadth_pop(len(new_queue[0].protein) - 1, index)
                    amino = self.get_last_amino(parent_protein)
                    result = self.create_child(amino, index)
                    new_queue = result[0]

                # for the remaining iterations, investigate all other children
                else:
                    parent_protein = self.breadth_pop(len(new_queue[0].protein) - 1, index)
                    amino = self.get_last_amino(parent_protein)
                    result = self.create_children(amino, index)
                    new_queue = result[0]

        # print the best sstring and it's score
        print("best score: ", result[1])

        return [[]], result[2]