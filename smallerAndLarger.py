# Given a sorted array Arr of size N and a value X, find the number of array elements less than 
# or equal to X and elements more than or equal to X. 

def smallerAndLarger(arr, X):
	idx = arr.index(X)
	return len(arr[:idx]), len(arr[idx+1:])

arr = [1, 2, 8, 10, 11, 12, 19]
print(smallerAndLarger(arr, 1))

# what if value not in array?

def countElements(arr, X):
	"""Count elements less than or equal to X and elements more than or equal to X."""
	# Count elements less than or equal to X
	less_than_or_equal_count = sum(1 for el in arr if el <= X)
	
	# Count elements more than or equal to X
	more_than_or_equal_count = sum(1 for el in arr if el >= X)
	
	return less_than_or_equal_count, more_than_or_equal_count

# Testing the function with the provided example
test_array = [1, 2, 8, 10, 11, 12, 19]
X_value = 0
print(countElements(test_array, X_value))
