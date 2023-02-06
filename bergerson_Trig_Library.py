import numpy as np

# how do get sin(x)
# sin(x) is the limit as N-> infinity of the gross sum
# my plan is to define the different terms using loops and then combine them
Nmax = 65

def factorial(x):
    if x==1:
        fac = 1
    else:
        fac = x*factorial(x-1)
    return(fac)

def sin(x):
    sum = 0

    for n in range(0, Nmax + 1):
        denominator = factorial(2*n+1)
        numerator = ((-1)**n) * (x**(2*n+1))
        term = numerator/denominator
        sum += term

    return(sum)

def cos(x):
    sum = 0

    for n in range(0, Nmax + 1):
        denominator = factorial(2*n)
        numerator = ((-1)**n) * (x**(2*n))
        term = numerator/denominator
        sum += term

    return(sum)




print("foo")