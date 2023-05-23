"""
Determine if a string has all unique characters
"""

def uniqueOnlyCheck(string):
	"""
	First attempt using a dictionary
	"""
	flag = True
	stringDic = {string[0]:1}
	for i in range(1,len(string)):
		if string[i] in stringDic:
			print('1. Non unique charcter present in the string')
			flag = False
			break
		else:
			stringDic[string[i]] = 1
	if flag:
		print('1. All characters are unique')

string = 'abcde'
uniqueOnlyCheck(string)



def uniqueOnlyCheckNoFlag(string):
	"""
	Second attempt using a dictionary with no flag
	"""
	stringDic = {string[0]: 1}
	for i in range(1, len(string)):
		if string[i] in stringDic:
			return False
		else:
			stringDic[string[i]] = 1
	return True

string = 'abcdee'
if uniqueOnlyCheckNoFlag(string):
	print("2. All characters are unique")
else:
	print("2. Non-unique character present in the string")



def isUnique(string):
	"""
	Third attempt taking advantage of set properties
	"""
	uniqueChars = set()
	for char in string:
		if char in uniqueChars:
			return False
		uniqueChars.add(char)
	return True


string = "abcdefgg"
if isUnique(string):
	print("3. All characters are unique")
else:
	print("3. Non-unique character present in the string")



def isUniqueWithoutDS(string):
	"""
	Check if a string has all unique characters without using dictionaries or sets
	"""
	n = len(string)
	for i in range(n - 1):
		for j in range(i + 1, n):
			if string[i] == string[j]:
				return False
	return True

string = 'abcde'
if isUniqueWithoutDS(string):
	print("4. All characters are unique")
else:
	print("4. Non-unique character present in the string")
