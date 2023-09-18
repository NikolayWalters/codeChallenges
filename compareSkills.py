# A and B are good friend and programmers. They are always in a healthy competition with each other. 
# They decide to judge the best among them by competing. They do so by comparing their three 
# skills as per their values. Please help them doing so as they are busy.

# Set for A are like [a1, a2, a3]
# Set for B are like [b1, b2, b3]

# Compare ith skill of A with ith skill of B
# if a[i] > b[i] , A's score increases by 1
# if a[i] < b[i] , B's score increases by 1
# if a[i] = b[i] , nothing happens

def compareSkills(arrA, arrB):
	Ascore = 0
	Bscore = 0
	for idx, el in enumerate(arrA):
		if el > arrB[idx]:
			Ascore +=1
		elif el < arrB[idx]:
			Bscore +=1
		else:
			pass
	return Ascore, Bscore

arrA = [4, 2, 7]
arrB = [5, 6, 3]
print(compareSkills(arrA, arrB))