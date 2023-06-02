"""
Design a method to find the frequency of occurrences of any given word in a book
"""

import re

def main(string, tar):
	# Convert the book text to lowercase to ignore case sensitivity
	string = string.lower()
	# Remove punctuation marks using regular expressions
	string = re.sub(r'[^\w\s]', '', string)
	# Split the book text into individual words
	words = string.split()
	# Count the occurrences of the target word
	frequency = 0
	for word in words:
		if word == tar:
			frequency += 1
	return frequency

test = 'this is, a test; string. right is test string'

print(main(test, 'is'))
print(main(test, 'test'))
print(main(test, 'string'))
print(main(test, 'this'))


# What if we were running this algorithm multiple times?
# 1) process the book by removing punctuation+lowercase
# 2) create a frequency dictionary for each word
# 3) use target word as the dictionary key to get its frequency
# 4) add error handling if target word not in book