"""
Write a program that prints the numbers 1 to 100. But for multiples of 3, print "Fizz"
instead of the number, and for the multiples of 5, print "Buzz". For numbers that are
multiples of both 3 and 5, print "FizzBuzz".
"""

# multiples of 3 and 5 -> 15

def fizz():
	for i in range (1,101):
		if i % 15 == 0:
			print('FizzBuzz')
		elif i % 5 == 0:
			print('Buzz')
		elif i % 3 == 0:
			print('Fizz')
		else:
			print(i)

# or using a list comprehension
def fizzN(N):
	result = ["FizzBuzz" if i % 3 == 0 and i % 5 == 0 else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else i for i in range(1, N+1)]
	for item in result:
		print(item)

fizzN(20)