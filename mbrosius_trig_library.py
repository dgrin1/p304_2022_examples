#library of trig functions

import numpy as np
Nmax = 65

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
