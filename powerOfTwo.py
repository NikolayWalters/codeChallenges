# Given a non-negative integer N. The task is to check if N is a power of 2. 
# More formally, check if N can be expressed as 2x for some integer x.

def powerOfTwo(num):
	# 0 is not a power of 2
	if num == 0:
		return False
	
	numDivided = num
	while numDivided != 1:
		numDivided = numDivided // 2
		if numDivided == 1:
			return True
		if numDivided % 2 != 0:
			return False

	return True

print(powerOfTwo(8))