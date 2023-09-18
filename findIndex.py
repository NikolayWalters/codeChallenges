# Given an unsorted array Arr[] of N integers and a Key which is present in this array. 
# You need to write a program to find the start index( index where the element is first 
# found from left in the array ) and end index( index where the element is first found
# from right in the array ).If the key does not exist in the array then return -1 for
# both start and end index in this case.

def findIndex(arr, val):
	try: 
		first = arr.index(val)
		last = len(arr) - arr[::-1].index(val) - 1
		return first, last
	except ValueError:
		return -1, -1

arr = [1,2,4,5,3,4,6,4]
print(findIndex(arr, 4))

arr = [1,2,3,5,7,9]
print(findIndex(arr, 4))