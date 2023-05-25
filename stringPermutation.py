"""
Given two strings, write a method to decide if one is a permutation of the other
"""

# NB didn't realise permutation = same number of unique chars

string1 = 'abcde'
string2 = 'dcb'

def createDict(string):
	stringDict = {}
	for char in string:
		if char in stringDict:
			stringDict[char]+=1
		else:
			stringDict[char] = 1
	return stringDict

def permutationCheck(string1, string2):
	"""
	Initial attempt using dictionaries
	"""

	stringDict1 = createDict(string1)
	stringDict2 = createDict(string2)
	for key in stringDict2:
		try:
			diff = stringDict1[key]-stringDict2[key]
		except:
			return False
		if diff < 0:
			return False
	return True

print('is string2 permutation of string1?', permutationCheck(string1, string2))

string1 = 'abcde'
string2 = 'dcbz'
print('is string2 permutation of string1?', permutationCheck(string1, string2))




# A much better way using sorting and understanding what permutation actually means

def checkPermutation(string1, string2):
    sorted1 = sorted(string1)
    sorted2 = sorted(string2)

    if sorted1 == sorted2:
        return True
    else:
        return False

string1 = "abc"
string2 = "bca"
isPermutation = checkPermutation(string1, string2)
print(isPermutation)