from __future__ import print_function,division
from numpy import array,empty,copy,dot,linalg,abs,power,sqrt,log
from math import exp
import matplotlib.pyplot as plt

def f(x):
	return 2.-exp(-x)
def g(x):
	return exp(1.-power(x,2.e0))
def h(x):
	return sqrt(1.e0-log(x))
	
eps=2
x=eps
eps_target=1.e-8
xold=x
xarr=[x]
i=0
iarr=[i]
#cap is put in there to make sure code doesn't take forever
while (eps>eps_target and i<500):
	x=h(x)
	eps=abs(x-xold)
#setting the new comparison case to last guees
	xold=x
#augmenting m count
	i=i+1
	iarr.append(i)
	xarr.append(x)
	
print(x,eps_target)
plt.xlim(1,10)
plt.ion()
plt.plot(iarr,xarr)
plt.show()
