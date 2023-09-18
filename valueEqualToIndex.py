# Given an array Arr of N positive integers. Your task is to find the elements whose 
# value is equal to that of its index value ( Consider 1-based indexing ).

def valueEqualToIndex(arr):
	for index, el in enumerate(arr):
		if el == index:
			return True
	return False


arr = [5,4,3,5,4]
print(valueEqualToIndex(arr))