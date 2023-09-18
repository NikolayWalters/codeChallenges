# Given an array of N distinct elements, the task is to find all elements in array 
# except two greatest elements in sorted order.

def twoGreatest(arr):
	arr = sorted(arr)
	return arr[:-2]

arr = [1,4,2,3,6,1]
print(twoGreatest(arr))