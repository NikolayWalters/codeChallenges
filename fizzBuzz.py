"""
Write a program that prints the numbers 1 to 100. But for multiples of 3, print "Fizz"
instead of the number, and for the multiples of 5, print "Buzz". For numbers that are
multiples of both 3 and 5, print "FizzBuzz".
"""

# multiples of 3 and 5 -> 15

for i in range (1,101):
	if i % 15 == 0:
		print('FizzBuzz')
	elif i % 5 == 0:
		print('Buzz')
	elif i % 3 == 0:
		print('Fizz')
	else:
		print(i)