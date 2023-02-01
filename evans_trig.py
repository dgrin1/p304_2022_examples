import numpy as np


def factorial(y):
    if y == 1 or y == 1:
        return 1
    else:
        return (y*factorial(y-1))

def sin(x,N):
    sum = 0
    for n in range(1, N+1):
        num = ((-1)**n)*(x**(2*n+1))
        den = (2*n+1)
        denom = factorial(den)
        term = num/denom
        sum += term
    return sum

def cos(x,N):
    sum = 0
    for n in range(1, N+1):
        num = ((-1)**n)*(x**(2*n))
        den = (2*n)
        denom = factorial(den)
        term = num/denom
        sum += term
    return sum


def tan(x,N):
    return sin(x,N)/cos(x,N)

def sec(x,N):
    return 1/cos(x,N)

def csec(x,N):
    return 1/sin(x,N)

def cotan(x,N):
    return 1/tan(x,N)


