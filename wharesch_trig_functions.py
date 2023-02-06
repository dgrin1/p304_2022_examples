import numpy as np
nMax=5

def factorial (x):
    if(x==1 or x==0):
        fac=1
    else:
        fac=x*factorial(x-1)
    return fac

def sin_wharesch(x):
    sum=0
    for n in range(0,nMax+1):
        numerator=((-1)**n)*np.power(x,2*n+1)
        int_want=2*n+1
        denominator=factorial(int_want)
        term=numerator/denominator
        sum+=term
    return sum

def cos_wharesch(x):
    return sin_wharesch(np.pi/2-x)
    

def tan_wharesch(x):
    return sin_wharesch(x)/cos_wharesch(x)

def sec_wharesch(x):
    return 1/cos_wharesch(x)

def csc_wharesch(x):
    return 1/sin_wharesch(x)

def cot_wharesch(x):
    return 1/tan_wharesch(x)

