# Given a number N. Your task is to check whether it is fascinating or not.
# Fascinating Number: When a number(should contain 3 digits or more) is multiplied by 2 and 3, 
# and when both these products are concatenated with the original number, then it results in 
# all digits from 1 to 9 present exactly once.

def fascinating(num):
	unique = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	num = str(num) + str(num*2) + str(num*3)
	for digit in unique:
		if str(digit) not in num:
			return False
	return True

print(fascinating(192))
print(fascinating(853))