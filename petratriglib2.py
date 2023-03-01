import numpy as np
def factorial(y):
	fac=1
	for i in range (y,0,-1):
		fac=fac*i
	return fac

def cos(x,Nmax):
	sum=0
	for n in range (0,Nmax+1):
		#print(n)
		numerator=((-1)**n)*np.power(x,2*n) #numerator in Taylor series - need np power function to represent exponential
		denominator=factorial(2*n)
		term=numerator/denominator
		sum+=term
	return sum


def sin(x,Nmax):
	sum=0
	for n in range (0,Nmax+1):
		#print(n)
		numerator=((-1)**n)*np.power(x,2*n+1) #numerator in Taylor series - need np power function to represent exponential
		denominator=factorial(2*n+1)
		term=numerator/denominator
		sum+=term
	return sum


def tan(x,Nmax):
	tan=sin(x,Nmax)/cos(x,Nmax)
	return tan


def cot(x,Nmax):
	cot=1/tan(x,Nmax)
	return cot


def csec(x,Nmax):
	csec=1/sin(x,Nmax)
	return csec


def sec(x,Nmax):
	sec=1/cos(x,Nmax)
	return sec
