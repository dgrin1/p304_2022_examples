from __future__ import print_function,division
import numpy as np
from flannery_trig import sin

N=1000
a=0
b=3*np.pi

ivec=range(0,N+1)
s=0
x=0
h=float(b-a)/float(N)

def f(x):
	f=np.power(x,4.e0)-2.*x+1.
	return f


def f2(x):
	f=np.sin(x)
	return f

for i in ivec:
	s+=f2(x)*h
	x=a+i*h

def trape(a,b,f,N):
	h=(b-a)/N
	s=(f(a)+f(b))*h
	for i in range(1,N):
		s+=2.*f(a+i*h)*h
	s/=2.0
	return s
	
trape(a,b,f2,N)

print(s,trape(a,b,f2,N))
