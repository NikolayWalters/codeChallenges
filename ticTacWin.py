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
# NB very easy to just convert into a numpy array
# then transpose it and send it to horizontal_check
# but I'll pretend that we can't import numpy
def vertical_check(array):
	for col in range(len(array[0])):
	count = 0
		for row3 in range(len(array)-2):
			tmpArr = [array[count][col],array[count+1][col],array[count+1][col]]
			check = sum(tmpArr)
			count = count+1
			if abs(check)==3:
				print('Winner!')
				break


	

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


