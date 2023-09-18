# Given a array of length N, at each step it is reduced by 1 element. In the first step the maximum 
# element would be removed, while in the second step minimum element of the remaining array would be 
# removed, in the third step again the maximum and so on. Continue this till the array contains only 
# 1 element. And find the final element remaining in the array.

def middleEl(arr):
	arr = sorted(arr)
	length = len(arr)
	if length%2 == 0:
		return arr[int(len(arr)/2)-1]
	else:
		return arr[int(len(arr)/2)]


arr = [7, 8, 3, 4, 2, 9, 5]

print(middleEl(arr))

arr = [8, 1, 2, 9, 4, 3, 7, 5]

print(middleEl(arr))