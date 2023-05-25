"""
There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away.
EXAMPLE
pale, ple -> true
pales, pale -> true
pale, bale -> true
pale, bake -> false
"""

# first, check if two strings are identical

# for removal check if len(string1) = len(string2)+1
# and string2 is in string1

# for insert similar to the above but
# len(string1) = len(string2) - 1 and string1 is in string2

# for replace both lengths are the same
# but i think have to go char by char iterativily 
# while keeping track of differences

string1 = 'pale'
string2 = 'ple' # removal
string3 = 'pales' # insert
string4 = 'bale' # edit
string5 = 'bake' # false case

def removal(string1,string2):
	if (len(string1) == len(string2)+1) and (string2 in string1):

		return 1
	return 0
# nope, doesn't work; 


def replace(string1, string2):
	edits = 0
	shorter_str = string1 if len(string1) < len(string2) else string2
	longer_str = string2 if len(string1) < len(string2) else string1
	for count, char in enumerate(shorter_str):
		if char != longer_str[count]:
			edits += 1
			if edits > 1:
				return False
	return True

def createDict(string):
	stringDict = {}
	for char in string:
		if char in stringDict:
			stringDict[char] += 1
		else:
			stringDict[char] = 1
	return stringDict

def removalOrInsert(string1, string2):
	edits = replace(string1, string2)
	if edits > 1:
		return False
	dict1 = createDict(string1)
	dict2 = createDict(string2)
	for key in dict1:
		if key in dict2 and dict1[key] == dict2[key]:
			continue
		elif key not in dict2 or abs(dict1[key] - dict2[key]) > 1:
			return False
	return True

# the above is bugged
# another approach: check string length and based on that send it to either remov/insert/change


def createDict(string):
	stringDict = {}
	for char in string:
		if char in stringDict:
			stringDict[char] += 1
		else:
			stringDict[char] = 1
	return stringDict

def replace(string1, string2):
	edits = 0
	for count, char in enumerate(string1):
		if char != string2[count]:
			edits += 1
			if edits > 1:
				return False
	return True

def insert(string1, string2):
	shorter_str = string1 if len(string1) < len(string2) else string2
	longer_str = string2 if len(string1) < len(string2) else string1
	dict1 = createDict(shorter_str)
	dict2 = createDict(longer_str)
	edits = 0
	for key in dict2:
		if key not in dict1 and dict2[key] > 1:
			return False
		elif key not in dict1 and dict2[key] == 1:
			edits += 1
			if edits > 1:
				return False
		elif abs(dict2[key] - dict1[key]) == 1:
			edits += 1
			if edits > 1:
				return False
		elif abs(dict2[key] - dict1[key]) > 1:
			return False
	return True


def mainM(string1, string2):
	delL = len(string1) - len(string2)
	if delL == 0:
		return replace(string1, string2)
	elif abs(delL) == 1:
		return insert(string1, string2)
	else:
		return False



print(mainM(string1,string2))
print(mainM(string1,string3))
print(mainM(string1,string4))
print(mainM(string1,string5))
# i don't know if it's buggy but seems to work on the test cases