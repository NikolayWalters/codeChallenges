"""
Palindrome Permutation: Given a string, write a function to check if it is a permutation 
of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation
is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.

EXAMPLE
Input: Tact Coa
Output: True (permutations: "taco cat", "atco eta", etc.)
"""

# Initial attempt:
# check if the number of unique characters is even
# except one char
# keep in mind if there are capital letters -> lowercase everything

string = "Tact Coa"
# using dictionary
def is_permutation_of_palindrome(string):

	# String preparation
	string = string.replace(" ", "")
	string = string.lower()
	char_count = {}
	
	# Count the occurrences of each character
	for char in string:
		if char in char_count:
			char_count[char] += 1
		else:
			char_count[char] = 1

	# Check the counts
	odd_count = 0
	for count in char_count.values():
		if count % 2 != 0:
			odd_count += 1
		if odd_count > 1:
			return False
			print('here')
	return True


print(is_permutation_of_palindrome(string))
