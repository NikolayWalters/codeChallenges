""" Sorting algorithms with some basic intuition"""

# Bubble sort
# Runtime: O(n^2); Memory: O(1)
def bubble_sort(arr):
	n = len(arr)
	for i in range(n - 1):
		for j in range(0, n - i - 1):
			if arr[j] > arr[j + 1]:
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
	return arr
test = [82, 45, 73, 97, 10, 55, 16, 92, 68, 21]
test_sorted = bubble_sort(test)
print("Sorted array:", test_sorted)

# Intuition
# 1) Start with an unsorted list of elements.
# 2) Compare the first element with the second element. If the first element is greater than the second element, swap them.
# 3) Compare the second element with the third element. If the second element is greater than the third element, swap them.
# 4) Repeat this process for all adjacent pairs of elements in the list, until reaching the end.
# 5) After the first pass, the largest element will be at the end of the list.
# 6) Repeat the above steps for all elements except the last one.
# 7) Continue the process until the list is completely sorted.



# Selection sort
# Runtime: O(n^2); Memory: O(1)
def selection_sort(arr):
	n = len(arr)
	for i in range(n):
		min_idx = i
		for j in range(i + 1, n):
			if arr[j] < arr[min_idx]:
				min_idx = j
		arr[i], arr[min_idx] = arr[min_idx], arr[i]
	return arr
test_sorted = selection_sort(test)
print("Sorted array:", test_sorted)

# Intuition
# 1) Start with an unsorted list of elements.
# 2) Find the minimum element in the unsorted portion of the list.
# 3) Swap the minimum element with the first element of the unsorted portion.
# 4) Move the boundary of the sorted portion one element to the right.
# 5) Repeat steps 2-4 until the entire list is sorted.



# Merge Sort
# Runtime: O(n log(n)); Memory: depends
def merge_sort(arr):
	if len(arr) <= 1:
		return arr
	# Divide the array into two halves
	mid = len(arr) // 2
	left_half = arr[:mid]
	right_half = arr[mid:]
	# Recursively sort the two halves
	left_half = merge_sort(left_half)
	right_half = merge_sort(right_half)
	# Merge the sorted halves
	return merge(left_half, right_half)


def merge(left, right):
	result = []
	i = j = 0
	# Merge the two sorted subarrays
	while i < len(left) and j < len(right):
		if left[i] <= right[j]:
			result.append(left[i])
			i += 1
		else:
			result.append(right[j])
			j += 1
	# Append the remaining elements, if any
	while i < len(left):
		result.append(left[i])
		i += 1
	while j < len(right):
		result.append(right[j])
		j += 1
	return result

test_sorted = merge_sort(test)
print("Sorted array:", test_sorted)

# Intuition
# 1) Divide the unsorted list into two halves by finding the middle index.
# 2) Recursively apply the Merge Sort algorithm to the left and right halves until each sublist contains only one element 
# or is empty.
# 3) Merge the two sorted sublists back together by comparing the elements from each sublist and placing them in the 
# correct order.
# 4) Continue merging the sublists until a single sorted list is obtained.



# Quick sort
# Runtime: O(n log(n)) average or O(n^2) worst case; Memory: O log(n)
def quicksort(arr):
	if len(arr) <= 1:
		return arr
	else:
		pivot = arr[0]
		smaller = [x for x in arr[1:] if x <= pivot]
		greater = [x for x in arr[1:] if x > pivot]
		return quicksort(smaller) + [pivot] + quicksort(greater)

test_sorted = quicksort(test)
print("Sorted array:", test_sorted)

# Intuition
# 1) Select a pivot element from the array (often the first or last element).
# 2) Partition the array by rearranging its elements such that all elements smaller than the pivot come before the pivot,
#  and all elements greater than the pivot come after it. The pivot element is now in its correct sorted position.
# 3) Recursively apply steps 1 and 2 to the sub-array of elements smaller than the pivot and the sub-array of elements 
# greater than the pivot.
# 4) Continue this process until each sub-array has only one element. At this point, the entire array will be sorted.



# Radix sort
# Runtime: O(kn)
def radix_sort(arr):
	# Find the maximum number to determine the number of digits
	max_value = max(arr)
	num_digits = len(str(max_value))

	# Perform counting sort for each digit, from least significant to most significant
	for digit in range(num_digits):
		counting_sort(arr, digit)
	return arr

def counting_sort(arr, digit):
	n = len(arr)
	output = [0] * n
	count = [0] * 10

	# Count the occurrences of each digit in the given position
	for i in range(n):
		index = (arr[i] // (10 ** digit)) % 10
		count[index] += 1

	# Calculate the cumulative count
	for i in range(1, 10):
		count[i] += count[i - 1]

	# Build the sorted output array based on the count and original array
	i = n - 1
	while i >= 0:
		index = (arr[i] // (10 ** digit)) % 10
		output[count[index] - 1] = arr[i]
		count[index] -= 1
		i -= 1

	# Copy the sorted output array back to the original array
	for i in range(n):
		arr[i] = output[i]

test_sorted = radix_sort(test)
print("Sorted array:", test_sorted)

# Intuition
# 1) Find the maximum number in the given list to determine the number of digits required.
# 2) For each digit position (from the least significant to the most significant), perform a stable counting sort.
# 3) In the counting sort, count the occurrences of each digit at the current position.
# 4) Calculate the cumulative count to determine the correct position for each digit in the sorted array.
# 5) Build the sorted output array based on the count and the original array, considering the current digit position.
# 6) Copy the sorted output array back to the original array.
# 7) Repeat the above steps for each digit position until all digits have been considered.
