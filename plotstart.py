from __future__ import division,print_function

def gfactorial(n):
	if type(n) == type(1):
		if n == 1:
			return n
		else:
			return n*gfactorial(n-1)
	else:
		print('Not an integer input')