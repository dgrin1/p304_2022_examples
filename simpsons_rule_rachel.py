# imports 
import numpy as np 
from matplotlib import pyplot as plt

# Def random function f(x)
def f(x, t): 
	return np.cos(t - x * np.sin(x))**2
	
# set N 
N = 1000

# Write Python function F(x1, t1) using Simpson's rule?
def F(x1, t1):
	# BCs of integral
	a = 0.0
	b = np.pi
	
	# step size of integral
	h = (b - a) / N

	# Simpson's rule
	Sum = f(x, a) + f(x, b)
	for i in range(1, N):
		t = a + i*h
		if i % 2 == 1:  # If odd
			Sum += 4.0 * f(x, t)
		else: # if even
			Sum += 2.0 * f(x, t)
			
	# multiply by h/3 to get the integrand and divide by pi to get the input func
	return Sum * h / (3.0 * np.pi)

# Test our function here, call on x values 0-20
#for x in range(21): 
#	print(x, F(0, x), F(1, x), F(2, x)) #okay yay this works so let's plot

# Pretty plotting time: 
for x in range(21): # for a range of x integer values from 1-20
	plt.plot(x, F(0, x), 'ro-') # idk why they aren't showing up as connected lines
	plt.plot(x, F(1, x), 'bo-')
	plt.plot(x, F(2, x), 'go-')
	plt.xlabel('X-Values from 0-20')
	plt.ylabel('Function Values')
#	plt.legend(['J0','J1', 'J2'])

#plt.savefig('/Users/rachellanggin/Desktop/langgin_hw4_5_4a.png')	
plt.show()

	
	
