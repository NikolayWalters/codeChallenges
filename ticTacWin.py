"""
Design an algorithm to figure out if someone has won a game of tic-tac-toe. 
"""

# let x = 1
# let o = -1
# let empty = 0
# let board = array

# horizontal check
def horizontal_check(array, rows, cols):
	for row in array:
		count = 0
		for col3 in range(cols-2):
			check = sum(row[count:count+3])
			count = count+1
			if abs(check)==3:
				print('Winner!')
				break

# vertical check
# NB very easy to just convert into a numpy array
# then transpose it and send it to horizontal_check
# but I'll pretend that we can't import numpy
def vertical_check(array, rows, cols):
	for col in range(cols):
	count = 0
		for row3 in range(cols-2):
			tmpArr = [array[count][col],array[count+1][col],array[count+1][col]]
			check = sum(tmpArr)
			count = count+1
			if abs(check)==3:
				print('Winner!')
				break


	

# diagonal check
# I think need to make it n by n before running diagonal check
# I think that's easier but not sure

def square_Check(array, rows, cols):

	# If the shape is already n by n, return the array as is
	if rows == cols:
		return 0
	else:
		return max([rows,cols])

N = square_Check(array, rows, cols)

def pad(array, N):
	new_arr = [[0] * n for _ in range(n)]
	for i in range(min(rows, n)):
		for j in range(min(cols, n)):
			new_arr[i][j] = arr[i][j]
	return new_arr


def diagonal_check(array):
	# could look into matrix rotation and then pass into vertical+horizontal check
	# or if small could hardcode all elements to check
	# a much better approach would be to just check where the point was placed
	# and segment that region into a sub-board and check only that 
	pass

def full_check(array):
	rows = len(array)
	cols = len(array[0])
	horizontal_check(array, rows, cols)
	vertical_check(array, rows, cols)
	N = square_Check(array, rows, cols)
	if N != 0:
		array = pad(array, N)
	diagonal_check(array, rows, cols)

testNegative = [[1, 2, 3, 4],
				[4, 5, 6, 4],
				[7, -1, -1, 1],
				[1, 2, 3, 4]]
testHorz = [[1, 2, 3, 4],
			[4, 5, 6, 4],
			[7, -1, -1, 1],
			[1, 1, 1, 4]]


