"""String Compression: Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z). 
"""


# start with the first letter
# check if the next letter is the same
# if yes increase count
# if not then the current active letter becomes the new letter

string = 'aabcccccaaa'
string2 = 'abs'

def compressor(string):
	constructor = ''
	currentVal = 1
	currentChar = string[0]
	for count, char in enumerate(string):
		try:
			if string[count+1] == currentChar:
				currentVal += 1
			else:
				constructor += (currentChar+str(currentVal))
				currentChar = string[count+1]
				currentVal = 1
		except IndexError:
			constructor += (currentChar+str(currentVal))
	if len(constructor) < len(string):
		return constructor
	else:
		return string

print(compressor(string))

print(compressor(string2))