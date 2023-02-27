import numpy as np


def f(x):
	return x**4-2*x+1

def simp(a,b,N):
	
	h = (b-a)/N
	
	sum1 = 0
	for k in range(1,N,2):
		sum1 += f(a+k*h)
		
	sum2 = 0
	for k in range(2,N,2):
		sum2 += f(a+k*h)

	
	E = (h/3)*(f(a)+f(b)+4*sum1+2*sum2)
	
	return E

print(simp(0,2,10))
