# Given two arrays a[] and b[] of size n and m respectively. The task is to find the 
# number of elements in the union between these two arrays.

# Union of the two arrays can be defined as the set containing distinct elements from both 
# the arrays. If there are repetitions, then only one occurrence of element should be printed in the union.

# Note : Elements are not necessarily distinct.

def union_count(a, b):
	"""Count the number of elements in the union of two arrays."""
	# Using set to get the union of the two arrays
	union_set = set(a) | set(b)
	return len(union_set)

# Testing the function with the provided examples
a1 = [1, 2, 3, 4, 5]
b1 = [1, 2, 3]

a2 = [85, 25, 1, 32, 54, 6]
b2 = [85, 2]

result1 = union_count(a1, b1)
result2 = union_count(a2, b2)
print(result1, result2)
