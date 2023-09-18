# Given a string S, write a program to count the occurrence of Lowercase characters, Uppercase characters, 
# Special characters and Numeric values in the string.
# Note: There are no white spaces in the string.

# Example 1:

# Input:
# S = "#GeeKs01fOr@gEEks07"
# Output:
# 5
# 8
# 4
# 2
# Explanation: There are 5 uppercase characters,
# 8 lowercase characters, 4 numeric characters
# and 2 special characters.


def count_chars(s):
	"""Count the occurrence of different types of characters in the string."""
	# Initialize counters
	lowercase_count = 0
	uppercase_count = 0
	numeric_count = 0
	special_count = 0
	
	# Iterate over each character in the string
	for char in s:
		if char.islower():
			lowercase_count += 1
		elif char.isupper():
			uppercase_count += 1
		elif char.isdigit():
			numeric_count += 1
		else:
			special_count += 1

	return uppercase_count, lowercase_count, numeric_count, special_count

# Testing the function with the provided example
test_string = "#GeeKs01fOr@gEEks07"
print(count_chars(test_string))