# Write a program to find the sum of the given series 1+2+3+ . . . . . .(N terms) 

def sumOfSeries(N):
	if N == 1:
		return 1
	else:
		return (1+N)*N/2

print(sumOfSeries(5))
