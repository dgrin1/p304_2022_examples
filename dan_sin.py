import numpy as np
#x=0.3
Nmax=65


def sin_dan(x):
 sum=0
#Big loop up to Nmax
 for n in range(0,Nmax+1):
	 #print(n)
	 numerator=((-1)**n)*np.power(x,2*n+1) #numerator in taylor series for 
 #	sum+=term #accumulate
	 int_want=2*n+1   # determine integer whose factorial we want right here
	 #print(int_want)
# 	 factorial=1
# 	 for j in range(int_want,0,-1):  #write a downward running loop that gets us from factorial target to 1
# 		 factorial=factorial*j
	 #print(n,int_want,factorial)
	 denominator=factorial(int_want)
	 term=numerator/denominator
	 sum+=term
 return sum
	 #print(n,factorial)


def factorial(x):
	if(x==1):	
		fac=1
	else:
		fac=x*factorial(x-1)
	return fac	
	
print(sin_dan(0.3))

#print(factorial(5))




