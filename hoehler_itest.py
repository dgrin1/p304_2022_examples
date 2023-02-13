from __future__ import print_function,division
import numpy as np
N=100 #setting number of points
a=0 #setting limits of integral
b=2

ivec=range(0,N+1) #list of integers containing the indices of every point
s=0
x=0
h=float(b-a)/float(N) #delta x

def f(x): #function that i want to integrate
	f=np.sin(x)
	return f


for i in ivec:
	s+=f(x)*h #adding to a sum, riemann sum
	x=a+i*h #cycling through every point

def trape(a,b,f,N): #trapezoidal rule approx to integral
	h=(b-a)/N #step size
	s=(f(a)+f(b))*h #edge points
	for i in range(1,N): #sum over all the points
		s+=2.*f(a+i*h)*h #here I add all the intermediate points
	s/=2.0 #factor of in front
	return s
	
trape(a,b,f,N) #compute trapezoidal rule -  give it limits of integrations, N, and the function

print(s,trape(a,b,f,N)) #print Riemann sum and trapezoidal rule
