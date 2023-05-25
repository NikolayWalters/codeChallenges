"""
URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given the "true"
length of the string.

EXAMPLE
Input: "Mr John Smith ", 13
Output: "Mr%20John%20Smith" 
"""

# the true length is given but if not could find the last non space character
# and truncate everything after it

def URLify(string, length):
	"""
	Initial approach using in-built functions
	"""
	truncated = string[:length]
	return truncated.replace(' ', '%20')

string = "Mr John Smith "
length = 13
print(URLify(string,length))


# if can't use replace would just have to go iteratively, check if char is a space
# if yes drop ' ' and append '%20'