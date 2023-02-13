from __future__ import print_function,division
import numpy as np
N=10 #setting number of piunts
a=0 # setting limits of integrals
b=2


ivec=range(0,N+1) #list of integers containing the indices of every points
s=0
x=0
h=float(b-a)/float(N) #delta x

def f(x): #function I want to integrate
	f=(np.sin(x)**2)+(np.cos(x)**2)
	return f


for i in ivec: #working out all of the points
	s+=f(x)*h # adding to a sum, Riemann sum version
	x=a+i*h #cycling through every point

def trape(a,b,f,N): #trapezoidal rule approximation to the integral
	h=(b-a)/N #step size
	s=(f(a)+f(b))*h #edge points
	for i in range(1,N): #sum over all the points
		s+=2.*f(a+i*h)*h # here I add the intermediate points
	s/=2.0 #factor of in front
	return s
	
trape(a,b,f,N) #compute trapeziodal rule limits of integration, give it # anf the #number of points

print(s,trape(a,b,f,N))
