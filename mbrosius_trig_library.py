#library of trig functions

import numpy as np
import matplotlib.pyplot as plt
Nmax = 5

#functions time

def factorial(x):
    if(x==1):
        fac=1
    else:
        fac=x*factorial(x-1)
    return fac

def sin(x):
    sum=0
    for n in range(0,Nmax+1):
        numerator=((-1)**n)*(x**(2*n+1))
        int_want=2*n+1
        denominator=factorial(int_want)
        term=numerator/denominator
        sum+=term
    return sum

def cos(x):
    sum=0
    for n in range(0,Nmax+1):
        numerator=((-1)**n)*(x**(2*n))
        if (n==0):
            denominator=1
        else:
            int_want=2*n
            denominator=factorial(int_want)
        term=numerator/denominator
        sum+=term
    return sum
    

def tan(x):
    tan=sin(x)/cos(x)
    return tan

def sec(x):
   sec=cos(x)**-1
   return sec

def csc(x):
   csc=sin(x)**-1
   return csc

def cot(x):
   cot=cos(x)/sin(x)
   return cot
   
   
#plot time!
   
data = []
error = []
for n in range(0,100):
    temp=(2*np.pi/100)*n
    term=cos(temp)
    Nmax=2*Nmax
    temp2=(2*np.pi/100)*n
    term2=cos(temp2)
    Nmax=int((1/2)*Nmax)
    print(term2-term)

    
#x=np.linspace(0,2*np.pi,100)
#y=data


#plt.ylim([-1.1,1.1])



#plt.plot
#plt.show()


