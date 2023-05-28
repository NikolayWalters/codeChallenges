"""Compute the nth Fibonacci number"""

import time

def fibonacci(n):
	if n == 0:
		return 0
	if n == 1:
		return 1
	return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(5))
start_time = time.time()
print(fibonacci(32))
elapsed_time = time.time() - start_time
print("Elapsed time: {:.2f} seconds".format(elapsed_time))


# with memoization

def memoize(k): 
    cache = {}  
    def check(l): 
        if l not in cache: 
            cache[l] = k(l) 
        return cache[l] 
    return check
def fibonacciMemo(n): 
	if n == 0:
		return 0
	if n == 1:
		return 1  
	return (fibonacciMemo(n-1) + fibonacciMemo(n-2))  
start_time = time.time()
fibonacciMemo = memoize(fibonacciMemo)  
print(fibonacciMemo(32))  
elapsed_time = time.time() - start_time
print("Elapsed time: {:.2f} seconds".format(elapsed_time))

# using a decorator

class Memoize:
    def __init__(self, f):
        self.f = f
        self.memo = {}
    def __call__(self, *args):
        if not args in self.memo:
            self.memo[args] = self.f(*args)
        return self.memo[args]


@Memoize
def fibonacciDec(n):
	if n == 0:
		return 0
	if n == 1:
		return 1
	return fibonacciDec(n-1)+fibonacciDec(n-2)
print(fibonacciDec(32))
elapsed_time = time.time() - start_time
print("Elapsed time: {:.2f} seconds".format(elapsed_time))