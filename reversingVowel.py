# Given a string consisting of lowercase english alphabets, reverse only the vowels 
# present in it and print the resulting string.

def reverse_vowels(s):
	"""Reverse only the vowels in the given string."""
	vowels = "aeiou"
	
	# Extract vowels from the string in the order they appear
	vowel_list = [char for char in s if char in vowels]
	# Initialize an empty list to store the characters of the result
	result = []
	
	# Iterate over the input string
	for char in s:
		# If the character is a vowel, take the last vowel from the vowel_list
		if char in vowels:
			result.append(vowel_list.pop())
			print(result)
		# If not a vowel, keep the character as it is
		else:
			result.append(char)
	
	return ''.join(result)

# Testing the function with the provided examples
test_string_1 = "geeksforgeeks"
test_string_2 = "practice"
output_1 = reverse_vowels(test_string_1)
output_2 = reverse_vowels(test_string_2)
print(output_1, output_2)
