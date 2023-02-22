import numpy as np
import matplotlib.pyplot as plt
def f(x):
	f=x**2+x**3-5
	return f

def simpson(a,b,N):
	sum_odd=0
	sum_even=0
	h=(b-a)/N
	for i in np.arange (1,N/2):
		sum_odd+=f(a+(2*i-1)*h)
	for j in np.arange (1,N/2-1):
		sum_even+=f(a+2*j*h)
	I=h/3*(f(a)+f(b)+4*sum_odd +2*sum_even)
	return I
print(simpson(0,3,65))
