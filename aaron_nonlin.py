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

def inAxisForcePerMassOfSatellite(x_M1, x_M2,x): 
	G = 1 
	M1 = 1000 
	M2 = 1000 
	displace_1 = x_M1 - x
	displace_2 = x_M2 - x
	
	force1 = G*M1/(x_M1-x)**2 * (x_M1-x)/(abs(x_M1-x))
	force2 = G*M2/(x_M2-x)**2 * (x_M2-x)/(abs(x_M2-x))
	return force1+force2
eps=2
x=eps
eps_target=1.e-8
xold=x
xarr=[x]
i=0
iarr=[i]
#cap is put in there to make sure code doesn't take forever
while (eps>eps_target and i<500):
	x=inAxisForcePerMassOfSatellite(-1,1,x)
	eps=abs(x-xold)
#setting the new comparison case to last guees
	xold=x
#augmenting m count
	i=i+1
	iarr.append(i)
	xarr.append(x)
	
print(x,eps_target)
plt.xlim(-10,10)
plt.ion()
plt.plot(iarr,xarr)
plt.show()
