# Given an array of size N and you have to tell whether the array is perfect or not. 
# An array is said to be perfect if its reverse array matches the original array. 
# If the array is perfect then return True else return False.

# Input : Arr[] = {1, 2, 3, 2, 1}
# Output : PERFECT

def perfect_arr(arr):
	if arr == arr[::-1]:
		return 'Perfect'
	else:
		return 'Not perfect'

arr = [1, 2, 3, 2, 1]
print(perfect_arr(arr))