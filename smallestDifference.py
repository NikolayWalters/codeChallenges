"""
Smallest Difference: Given two arrays of integers, compute the pair of values (one value in each
array) with the smallest (non-negative) difference. Return the difference.
EXAMPLE
Input: {1, 3, 15, 11, 2}, {23, 127,235, 19, 8}
Output: 3. That is, the pair (11, 8). 

The obvious approach is to iterate through each element
Could be optimised by terminating early if difference is zero

A better approach:
1) sort both arrays
2) let array 1 be a and array 2 be b
3) then each element in array a is a_i and in b - b_i
4) compute a_i - b_i and store difference
5) if a_i - b_i > 0 then compute a_i - b_{i+1}
6) else compute a_{i+1} - b_{i+1}
"""

def compute_smallest_difference(arr1, arr2):
	arr1.sort()
	arr2.sort()

	smallest_difference = max(arr1[-1], arr2[-1]) # maximum possible difference
	i = 0
	j = 0

	while i < len(arr1) and j < len(arr2):
		difference = abs(arr1[i] - arr2[j])
		if difference == 0: # early termination
			return 0
		smallest_difference = min(smallest_difference, difference)

		if arr1[i] < arr2[j]:
			i += 1
		else:
			j += 1
	return smallest_difference


arr1 = [1, 3, 15, 11, 2]
arr2 = [23, 127,235, 19, 8]

print(compute_smallest_difference(arr1, arr2))

arr1 = [1, 3, 15, 11, 2, 23]
arr2 = [23, 127,235, 19, 8]

print(compute_smallest_difference(arr1, arr2))