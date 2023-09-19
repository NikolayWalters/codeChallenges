# Given a sorted array of size N and an integer K, find the position(0-based indexing) at which K 
# is present in the array using binary search.

def binary_search(arr, K):
	"""Find the position of K in the array using binary search."""
	low, high = 0, len(arr) - 1
	
	while low <= high:
		mid = (low + high) // 2
		
		# Check if K is present at mid
		if arr[mid] == K:
			return mid
		# If K is greater, ignore left half
		elif arr[mid] < K:
			low = mid + 1
		# If K is smaller, ignore right half
		else:
			high = mid - 1
			
	# If the element was not present
	return -1

# Testing the function with the provided example
test_array = [1, 2, 3, 4, 5]
K_value = 4
position = binary_search(test_array, K_value)
position
