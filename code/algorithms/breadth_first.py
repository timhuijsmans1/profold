from collections import deque
import copy
import math

global possibilites
global best_string
global best_score
global new_string
best_score = 0
best_string = []
def breadth_first(matrix, protein_string, amino_acid, protein, connections):
	""" 
	matrix: populates a 2d matrix with 0's, updates a cell in that matrix with a given value, returns itself
    protein_string: list of single char strings containing the amino acid to fold into a protein
    amino_acid: places the amino accids within the grid
    protein: remembers what amino acid has been placed where
    connections: stores the previous amino acid location and looks for adjecent cells

	matrix.update_matrix(amino_acid.row, amino_acid.column, amino_acid.value)
	"""

	global possibilites
	global best_score
	global new_string
	best_score = 0
	new_string = protein
	possibilites = []

	initial_string = protein
	print(initial_string.protein)
	start_string = initial_string

	# setup the deque
	string_deque = deque()
	string_deque.append(start_string)
	initial_lenght = len(initial_string.protein)
	# increase the size of the strings with 1 node every loop
	while string_deque:
		# pop first string from deque
		temp_string = string_deque.popleft()
		length = len(temp_string.protein)
		print(length)
		
		# determine whether to continue building or finish a string by checking it's score
		if length is not initial_lenght:
			# check possible places for the new node
			possibilities = check_possibilities(temp_string, length)
			print(possibilities)
			# get possible builds
			builds = form_string(temp_string, length, possibilities, initial_string)
			print(builds)
			# build new strings
			string_deque = build_strings(builds, string_deque)
			print(string_deque)
		else:
			check_score(temp_string)

	 #= best_string
	# return string
	return matrix, protein
	
def form_string(temp_string, i, possibilities, initial_string):
	builds = []
	possibilities = []
	# make a new (possible) string
	for option in possibilities:
		new_string = temp_string[:]
		new_node = copy.deepcopy(initial_string[i])
		new_node.connections.set_connections = option
		new_string.append(new_node)
		builds.append(new_string)
	# return all possible strings
	return builds
	
def build_strings(builds, string_deque):
	# add new strings to the deque
	for build in builds:
		string_deque.append(build)
			
	return string_deque

def check_possibilities(temp_string, i):
		
	# remember coordinates of the previous aminioacid in current string
	x = temp_string[i - 1][0]
	print(x)
	y = temp_string[i - 1][1]
	print(y)
	# create array containing possible positions
	options = [[x - 1, y], [x + 1, y], [x, y - 1], [x, y + 1]]
	print(options)
	return options	
	
def check_score(temp_string):
	new_string = temp_string
	new_string.score_function()
	new_score = new_string.protein.score_function()

	# replace best_string and best_score if the new_score is better
	if(new_score <= best_score):
		best_string = temp_string
		best_score = new_score
