from __future__ import print_function,division
import numpy as np
N=10
a=0
b=2

ivec=range(0,N+1)    #integters for indices of every point
s=0
x=0
h=float(b-a)/float(N)

#def f(x):   
#	f=np.power(x,4.e0)-2.*x+1.
#	return f

def f(x):   
	f= np.sin(x)**2 + np.cos(x)**2
	return f

for i in ivec:
	s+=f(x)*h   #adding to a sum
	x=a+i*h

def trape(a,b,f,N):    #trapezoid approx for integral
	h=(b-a)/N
	s=(f(a)+f(b))*h
	for i in range(1,N):   #sum over all points
		s+=2.*f(a+i*h)*h   #add intermediate points
	s/=2.0    #factor of in front
	return s
	
trape(a,b,f,N)     #sompute trapezoid rule of int

print(s,trape(a,b,f,N))
