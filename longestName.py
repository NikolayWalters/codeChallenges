# Given a list of names, display the longest name.

def longestName(arr):
	longest = ''
	for el in arr:
		if len(el) > len(longest):
			longest = el
	return longest

names = ["Geek", "Geeks", "Geeksfor", "GeeksforGeek", "GeeksforGeeks"]

print(longestName(names))