#Matt Layman CS213 fib.py

def fib_recursive(n):
	if n < 2:
		return n
	else:
		return fib_recursive(n-1) + fib_recursive(n-2)

def fib_memoize(n):
	cache = {0:0, 1:1}

	def fib(n):
		if n in cache:
			return cache[n]
		cache[n] = fib(n-1) + fib(n-2)
		return cache[n]

	return fib(n)

def fib_bottom_up(n):
	fibs = [0, 1, 1]

	for f in range(2, n):
		fibs.append(fibs[-1] + fibs[-2])

	return fibs[n]

def fib_in_place(n):
	a, b = 0, 1

	for i in range(0, n):
		a, b = b, a + b
		
	return a
