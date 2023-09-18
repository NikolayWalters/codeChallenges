# A Toeplitz (or diagonal-constant) matrix is a matrix in which each descending diagonal from left to right 
# is constant, i.e., all elements in a diagonal are same.
# Given a matrix A of order N X M your task is to complete the function isToeplitz which returns 
# true if the matrix is Toeplitz otherwise returns false.

import numpy as np

def isToeplitz(matrix):
	# Convert list to numpy array
	matrix = np.array(matrix)
	
	# Get shape of the matrix
	rows, cols = matrix.shape
	
	# Check diagonals starting from first row
	for j in range(cols):
		if not np.all(np.diag(matrix, k=j) == matrix[0, j]):
			return False

	# Check diagonals starting from first column (excluding the first element which we already checked)
	for i in range(1, rows):
		if not np.all(np.diag(matrix, k=-i) == matrix[i, 0]):
			return False

	return True

# Test the function
test_matrix = [
	[6, 7, 8, 9],
	[4, 6, 7, 8],
	[1, 4, 6, 7],
	[0, 1, 4, 6],
	[5, 0, 1, 4]
]
print(isToeplitz(test_matrix))
