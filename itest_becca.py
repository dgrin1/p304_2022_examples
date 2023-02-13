from __future__ import print_function,division
import numpy as np
N=100
a=-np.pi
b=np.pi

ivec=range(0,N+1)
s=0
x=0
h=float(b-a)/float(N)

def f(x):
	f=np.power(x,4.e0)-2.*x+1.
	return f

def funct(x):
	fun = np.sin(x)*np.cos(x)
	return fun

for i in ivec:
	s+=funct(x)*h
	x=a+i*h

def trape(a,b,f,N):
	h=(b-a)/N
	s=(funct(a)+funct(b))*h
	for i in range(1,N):
		s+=2.*funct(a+i*h)*h
	s/=2.0
	return s



trape(a,b,funct,N)

print(s,trape(a,b,funct,N))
