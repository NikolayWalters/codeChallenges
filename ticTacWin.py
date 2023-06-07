"""
Design an algorithm to figure out if someone has won a game of tic-tac-toe. 
"""

# let x = 1
# let o = -1
# let empty = 0
# let board = array

# horizontal check
def horizontal_check(array):
	for row in array:
    	count = 0
    	for col3 in range(len(array[0])-2):
        	check = sum(row[count:count+3])
        	count = count+1
        	if abs(check)==3:
            	print('Winner!')
            	break

# vertical check
def vertical_check(array):
	pass

# diagonal check
def diagonal_check(array):
	pass

def full_check(array):
	horizontal_check(array)
	vertical_check(array)
	diagonal_check(array)

testNegative = [[1, 2, 3, 4],
				[4, 5, 6, 4],
				[7, -1, -1, 1],
				[1, 2, 3, 4]]
testHorz = [[1, 2, 3, 4],
			[4, 5, 6, 4],
			[7, -1, -1, 1],
			[1, 1, 1, 4]]


