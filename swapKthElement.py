# Given an array Arr of size N, swap the Kth element from beginning with Kth element from end.

def swapKthElement(arr, K):
	kStart = arr[K-1]
	kEnd = arr[-K]
	arr[K-1], arr[-K] = kEnd, kStart
	return arr

array = [1, 2, 3, 4, 5, 6, 7, 8]
print(swapKthElement(array, 3))