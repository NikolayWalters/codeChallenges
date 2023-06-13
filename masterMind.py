"""
Master Mind: The G ame of Master Mind is played as follows:
The computer has four slots, and each slot will contain a ball that is red (R), yellow (Y), green (G) or
blue (B). For example, the computer might have RGGB (Slot #1 is red, Slots #2 and #3 are green, Slot
#4 is blue).
You, the user, are trying to guess the solution. You might, for example, guess YRGB.
When you guess the correct color for the correct slot, you get a "hit:' If you guess a color that exists
but is in the wrong slot, you get a "pseudo-hit:' Note that a slot that is a hit can never count as a
pseudo-hit.
For example, if the actual solution is RGBY and you guess GGRR, you have one hit and one pseudohit
Write a method that, given a guess and a solution, returns the number of hits and pseudo-hits.
"""

def calculate_hits_and_pseudo_hits(guess, solution):
	# Initialize counts for hits and pseudo-hits
	hits = 0
	pseudo_hits = 0

	# Create dictionaries to track counts of colors in guess and solution
	guess_counts = {}
	solution_counts = {}

	# Iterate over each position in guess and solution
	for i in range(len(guess)):
		if guess[i] == solution[i]:
			# Count hits
			hits += 1
		else:
			# Count colors in guess and solution for pseudo-hits
			guess_counts[guess[i]] = guess_counts.get(guess[i], 0) + 1
			solution_counts[solution[i]] = solution_counts.get(solution[i], 0) + 1

	# Calculate pseudo-hits
	for color, count in guess_counts.items():
		if color in solution_counts:
			pseudo_hits += min(count, solution_counts[color])

	return hits, pseudo_hits


# Example usage
guess = "GGRR"
solution = "RGBY"
hits, pseudo_hits = calculate_hits_and_pseudo_hits(guess, solution)

print(f"Number of hits: {hits}")
print(f"Number of pseudo-hits: {pseudo_hits}")

guess = "GGRR"
solution = "GGRR"
hits, pseudo_hits = calculate_hits_and_pseudo_hits(guess, solution)

print(f"Number of hits: {hits}")
print(f"Number of pseudo-hits: {pseudo_hits}")

guess = "RRGG"
solution = "GGRR"
hits, pseudo_hits = calculate_hits_and_pseudo_hits(guess, solution)

print(f"Number of hits: {hits}")
print(f"Number of pseudo-hits: {pseudo_hits}")