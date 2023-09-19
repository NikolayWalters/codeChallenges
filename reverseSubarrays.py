# Given an array arr[] of positive integers of size N. Reverse every sub-array group of size K.

# Note: If at any instance, there are no more subarrays of size greater than or equal to K, then 
# reverse the last subarray (irrespective of its size). You shouldn't return any array, modify the given array in-place.

# Example 1:

# Input:
# N = 5, K = 3
# arr[] = {1,2,3,4,5}
# Output: 3 2 1 5 4

def reverse_subarrays(arr, K):
	"""Reverse every sub-array of size K in-place."""
	n = len(arr)
	
	# Iterate through the array with a step of K
	for i in range(0, n, K):
		# Compute the starting and ending indices for the current subarray
		start = i
		end = min(i + K - 1, n - 1)
		
		# Reverse the subarray
		while start < end:
			arr[start], arr[end] = arr[end], arr[start]
			start += 1
			end -= 1

# Testing the function with the provided example
test_array = [1, 2, 3, 4, 5]
K_value = 3
reverse_subarrays(test_array, K_value)
print(test_array)
test_array = [1, 2, 3, 4, 5]
reverse_subarrays(test_array, 4)
print(test_array)
