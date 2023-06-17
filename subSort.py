"""
Sub Sort: Given an array of integers, write a method to find indices m and n such that if you sorted
elements m through n, the entire array would be sorted. Minimize n - m (that is, find the smallest
such sequence).
EXAMPLE
lnput:1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19
Output: (3, 9) 
"""

# def isSorted(arr):
# 	if arr == sorted(arr):
# 		return True
# 	else:
# 		return False

# def start(arr):
# 	passedI = 0
# 	for i in range(len(arr)):
# 		if isSorted(arr[0:i+1]):
# 			passedI = i
# 		else:
# 			return passedI-2 # first i is empty array, second i is one element, so need - 2

# def end(arr):
# 	passedI = 0
# 	N = len(arr)
# 	for i in range(N):
# 		if isSorted(arr[N-i:N]):
# 			passedI = i
# 		else:
# 			return N - passedI + 1 # again since N:N is empty
# # need a check that the last element is greater than everything in the smaller array
# testArr = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
# #print(start(testArr))
# #print(end(testArr))

# testArr = [1, 2, 4, 7, 10, 11, 20, 7, 12, 6, 7, 16, 18, 19]
# print(start(testArr))
# print(end(testArr))


def subSort(arr):
	length = len(arr)
	sortedArr = sorted(arr)
	inverseSort = sortedArr[::-1]
	inverseArr = arr[::-1]
	start = subSortStart(arr, sortedArr)
	end = subSortRev(inverseArr, inverseSort, length)
	return start, end




def subSortStart(arr,sortedArr):
	for count, val in enumerate(arr):
		if val == sortedArr[count]:
			pass
		else:
			return count
			
def subSortRev(inverseArr,inverseSort, length):
	for count, val in enumerate(inverseArr):
		if val == inverseSort[count]:
			pass
		else:
			return length - count - 1

testArr = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
print(subSort(testArr))