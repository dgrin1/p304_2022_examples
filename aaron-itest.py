from __future__ import print_function,division
import numpy as np
import matplotlib.pyplot as plt
N=100
a=0
b=12

ivec=range(0,N+1)
s=0
x=0
#h=float(b-a)/float(N)

def f(x):
	f=np.power(x,4.e0)-2.*x+1.
	return f

def f2(x):
	f =  np.sin(x)
	return f 

# reiman sum
def reisum(a,b,f,N):
	s = 0
	x=0
	h=float(b-a)/float(N)
	ivec=range(0,N+1)
	for i in ivec:
		s+=f(x)*h
		x=a+i*h
	return s

#trapezoid 
def trape(a,b,f,N):
	h=(b-a)/N
	s=(f(a)+f(b))*h
	for i in range(1,N):
		s+=2.*f(a+i*h)*h
	s/=2.0
	return s
	
trape(a,b,f2,N)

print(s,trape(a,b,f2,N))
result_cache_rei = []
result_cache_trape = []
for n in range(1,N):
	result_cache_rei = result_cache_rei + [reisum(a,b,f2,n)]
	result_cache_trape = result_cache_trape + [trape(a,b,f2,n)]

print("------------------")
print(result_cache_rei)
print("------------------")
print(result_cache_trape)
plt.figure(1)
plt.plot(range(1,N),result_cache_rei,label = "Reiman Sum")
plt.plot(range(1,N),result_cache_trape,label = "Trapezoid")
plt.legend()
plt.xlabel("N")
plt.ylabel("Evaluated")
plt.show()

plt.figure(2) 
error = [abs(rei - trape) for rei,trape  in zip(result_cache_rei,result_cache_trape)]
print(error)
plt.loglog(range(1,N),error)
plt.show()
