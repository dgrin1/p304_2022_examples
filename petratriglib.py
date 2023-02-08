import numpy as np
#x=float(input("Please enter an angle:"))
Nmax=65

def factorial(y):
	fac=1
	for i in range (y,0,-1):
		fac=fac*i
	return fac
#print(factorial(3))
def cos(x):
	sum=0
	for n in range (0,Nmax+1):
		#print(n)
		numerator=((-1)**n)*np.power(x,2*n) #numerator in Taylor series - need np power function to represent exponential
		denominator=factorial(2*n)
		term=numerator/denominator
		sum+=term
	return sum
#print("For your given value of x, these are the following trigonometric values:")
#print("The cosine is:", cos(x))

def sin(x):
	sum=0
	for n in range (0,Nmax+1):
		#print(n)
		numerator=((-1)**n)*np.power(x,2*n+1) #numerator in Taylor series - need np power function to represent exponential
		denominator=factorial(2*n+1)
		term=numerator/denominator
		sum+=term
	return sum
#print("The sine is:", sin(x))

def tan(x):
	tan=sin(x)/cos(x)
	return tan
#print("The tangent is:", tan(x))

def cot(x):
	cot=1/tan(x)
	return cot
#print("The cotangent is:", cot(x))

def csec(x):
	csec=1/sin(x)
	return csec
#print("The cosecant is:", csec(x))

def sec(x):
	sec=1/cos(x)
	return sec
#print("The secant is:", sec(x))