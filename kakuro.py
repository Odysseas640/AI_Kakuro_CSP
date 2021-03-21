import cspORIGINAL as csp
import time

# We need 7 extra variables to turn this into a binary problem. One for each row or column of the game board.
gamestate = ['v1', 'v2', 'v3', 'v4', 'v5', 'v6', 'v7', 'v8', 'v9', 'v10', 'v11', 'v12', 'v13', 'v14', 'v15']

domains_dictionary = {gamestate[0]:(1,2,3,4,5,6,7,8,9), gamestate[1]:(1,2,3,4,5,6,7,8,9),\
	gamestate[2]:(1,2,3,4,5,6,7,8,9), gamestate[3]:(1,2,3,4,5,6,7,8,9),\
	gamestate[4]:(1,2,3,4,5,6,7,8,9), gamestate[5]:(1,2,3,4,5,6,7,8,9),\
	gamestate[6]:(1,2,3,4,5,6,7,8,9), gamestate[7]:(1,2,3,4,5,6,7,8,9),\
	}
# The extra variables correspond to a row or column on the game board, and contain every "normal" variable
# in that row or column.
# The domain of these extra variables is all the values that the variables they contain can take, and still
# add up to the number they should. That's how I sneak the constraints into the AIMA code.
domain_c8 = ((1,2,('v1','v2')), (2,1,('v1','v2')))
domain_c9= []
for x1 in range(1,10):
	for x2 in range(1,10):
		for x3 in range(1,10):
			for x4 in range(1,10):
				if x1 != x2 and x1 != x3 and x1 != x4 and x2 != x3 and x2 != x4 and x3 != x4 and x1+x2+x3+x4==10: # If they're different and add up to 10
					domain_c9.append((x1,x2,x3,x4,('v3','v4','v5','v6'))) # add them to the domain of that row
domain_c10 = ((1,2,('v7','v8')), (2,1,('v7','v8')))
domain_c11 = ((1,2,('v2','v6')), (2,1,('v2','v6')))
domain_c12 = ((1,5,('v1','v5')), (2,4,('v1','v5')), (3,3,('v1','v5')), (4,2,('v1','v5')), (5,1,('v1','v5')))
domain_c13 = ((1,2,('v4','v8')), (2,1,('v4','v8')))
domain_c14 = ((1,3,('v3','v7')), (2,2,('v3','v7')), (3,1,('v3','v7')))
domains_dictionary.update({gamestate[8]:domain_c8})
domains_dictionary.update({gamestate[9]:domain_c9})
domains_dictionary.update({gamestate[10]:domain_c10})
domains_dictionary.update({gamestate[11]:domain_c11})
domains_dictionary.update({gamestate[12]:domain_c12})
domains_dictionary.update({gamestate[13]:domain_c13})
domains_dictionary.update({gamestate[14]:domain_c14})

# Every empty spot on the board is neighbors with all the others in the same row and column, plus that row and that column
neighbors_dictionary = {gamestate[0]:[gamestate[1], gamestate[4], gamestate[8], gamestate[12]],\
	gamestate[1]:[gamestate[0], gamestate[5], gamestate[8], gamestate[11]],\
	gamestate[2]:[gamestate[3], gamestate[4], gamestate[5], gamestate[6], gamestate[9], gamestate[14]],\
	gamestate[3]:[gamestate[2], gamestate[4], gamestate[5], gamestate[7], gamestate[9], gamestate[13]],\
	gamestate[4]:[gamestate[2], gamestate[3], gamestate[5], gamestate[0], gamestate[9], gamestate[12]],\
	gamestate[5]:[gamestate[2], gamestate[3], gamestate[4], gamestate[1], gamestate[9], gamestate[11]],\
	gamestate[6]:[gamestate[7], gamestate[2], gamestate[10], gamestate[14]],\
	gamestate[7]:[gamestate[6], gamestate[3], gamestate[10], gamestate[13]],\
	gamestate[8]:[gamestate[0], gamestate[1]],\
	gamestate[9]:[gamestate[2], gamestate[3], gamestate[4], gamestate[5]],\
	gamestate[10]:[gamestate[6], gamestate[7]],\
	gamestate[11]:[gamestate[1], gamestate[5]],\
	gamestate[12]:[gamestate[0], gamestate[4]],\
	gamestate[13]:[gamestate[3], gamestate[7]],\
	gamestate[14]:[gamestate[2], gamestate[6]],\
	}

constraintz_called = 0
	
def constraintz(A, a, B, b):
	global constraintz_called
	constraintz_called += 1
	if (isinstance(a, int) and isinstance(b, int)):
		if a == b: # If both variables are numbers, they should not be equal
			return False
		else:
			return True
	elif isinstance(a, list) or isinstance(a, tuple):
		length1 = len(a) # One variable is a number and the other is one of those extra variables we need
		for i in range(length1 - 1): # to convert the problem into binary form. Say variable "a" looks
			if B == a[length1-1][i]: # like this: (2,4,1,7,('v1', 'v2', 'v3', 'v4')). Variable "B" will be
				position = i # one of v1, v2, v3, v4, with "b" from 1 to 9. If "B" is v1, "b" must be 2.
				break; # If "B" is v2, "b" must be 4. If "B" is v3, "b" must be 1. If "B" is v4, "b" must be 7.
		if b == a[position]:
			return True
		return False
	elif isinstance(b, list) or isinstance(b, tuple):
		length1 = len(b)
		for i in range(length1 - 1):
			if A == b[length1-1][i]:
				position = i
				break;
		if a == b[position]:
			return True
		return False

start_time = time.time()
print("Running FC on given problem...")
probblem = csp.CSP(gamestate,domains_dictionary,neighbors_dictionary,constraintz)
given_problem = csp.backtracking_search(probblem,select_unassigned_variable=csp.mrv,order_domain_values=csp.lcv,inference=csp.forward_checking)
print('Done in %.4f seconds' % (time.time() - start_time))
print('Assigns:', probblem.nassigns, ', constraints called:', constraintz_called)
constraintz_called = 0

start_time = time.time()
print("Running MAC on given problem...")
probblem = csp.CSP(gamestate,domains_dictionary,neighbors_dictionary,constraintz)
given_problem = csp.backtracking_search(probblem,select_unassigned_variable=csp.mrv,order_domain_values=csp.lcv,inference=csp.mac)
print('Done in %.4f seconds' % (time.time() - start_time))
print('Assigns:', probblem.nassigns, ', constraints called:', constraintz_called, '\n')
constraintz_called = 0


start_time = time.time()
print('Initializing 8x8 medium puzzle...')
import medium_puzzle
medium_probblem = csp.CSP(medium_puzzle.medium_pazl, medium_puzzle.domains_medium, medium_puzzle.neighbors_medium, constraintz)
print('Took %.4f seconds to initialize' % (time.time() - start_time))

start_time = time.time()
print('Running FC on 8x8 medium puzzle...')
medium_probblem = csp.CSP(medium_puzzle.medium_pazl, medium_puzzle.domains_medium, medium_puzzle.neighbors_medium, constraintz)
medium_problem_result = csp.backtracking_search(medium_probblem,select_unassigned_variable=csp.mrv,order_domain_values=csp.lcv,inference=csp.forward_checking)
print('Took %.4f seconds to run' % (time.time() - start_time))
print('Assigns:', medium_probblem.nassigns, ', constraints called:', constraintz_called)
constraintz_called = 0

start_time = time.time()
print('Running MAC on 8x8 medium puzzle...')
medium_probblem = csp.CSP(medium_puzzle.medium_pazl, medium_puzzle.domains_medium, medium_puzzle.neighbors_medium, constraintz)
medium_problem_result = csp.backtracking_search(medium_probblem,select_unassigned_variable=csp.mrv,order_domain_values=csp.lcv,inference=csp.mac)
print('Took %.4f seconds to run' % (time.time() - start_time))
print('Assigns:', medium_probblem.nassigns, ', constraints called:', constraintz_called, '\n')
constraintz_called = 0


start_time = time.time()
print('Initializing easy 10x10 puzzle...')
import easy_10x10
easy10_probblem = csp.CSP(easy_10x10.pazl, easy_10x10.domains, easy_10x10.neighbors, constraintz)
print('Took %.4f seconds to initialize' % (time.time() - start_time))

start_time = time.time()
print('Running FC on easy 10x10 puzzle...')
easy10_probblem = csp.CSP(easy_10x10.pazl, easy_10x10.domains, easy_10x10.neighbors, constraintz)
easy10_problem_result = csp.backtracking_search(easy10_probblem,select_unassigned_variable=csp.mrv,order_domain_values=csp.lcv,inference=csp.forward_checking)
print('Took %.4f seconds to run' % (time.time() - start_time))
print('Assigns:', easy10_probblem.nassigns, ', constraints called:', constraintz_called)
constraintz_called = 0

start_time = time.time()
print('Running MAC on easy 10x10 puzzle...')
easy10_probblem = csp.CSP(easy_10x10.pazl, easy_10x10.domains, easy_10x10.neighbors, constraintz)
easy10_problem_result = csp.backtracking_search(easy10_probblem,select_unassigned_variable=csp.mrv,order_domain_values=csp.lcv,inference=csp.mac)
print('Took %.4f seconds to run' % (time.time() - start_time))
print('Assigns:', easy10_probblem.nassigns, ', constraints called:', constraintz_called, '\n')
constraintz_called = 0


start_time = time.time()
print('Initializing 10x10 hard puzzle...')
import hard_puzzle
hard_probblem = csp.CSP(hard_puzzle.pazl, hard_puzzle.domains, hard_puzzle.neighbors, constraintz)
print('Took %.4f seconds to initialize' % (time.time() - start_time))

start_time = time.time()
print('Running FC on 10x10 hard puzzle...')
hard_probblem = csp.CSP(hard_puzzle.pazl, hard_puzzle.domains, hard_puzzle.neighbors, constraintz)
hard_problem_result = csp.backtracking_search(hard_probblem,select_unassigned_variable=csp.mrv,order_domain_values=csp.lcv,inference=csp.forward_checking)
print('Took %.4f seconds to run' % (time.time() - start_time))
print('Assigns:', hard_probblem.nassigns, ', constraints called:', constraintz_called)
constraintz_called = 0

start_time = time.time()
print('Running MAC on 10x10 hard puzzle...')
hard_probblem = csp.CSP(hard_puzzle.pazl, hard_puzzle.domains, hard_puzzle.neighbors, constraintz)
hard_problem_result = csp.backtracking_search(hard_probblem,select_unassigned_variable=csp.mrv,order_domain_values=csp.lcv,inference=csp.mac)
print('Took %.4f seconds to run' % (time.time() - start_time))
print('Assigns:', hard_probblem.nassigns, ', constraints called:', constraintz_called)