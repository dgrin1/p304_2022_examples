import numpy as np
Nmax=65

def factorial(x):
    if x == 1 or x == 0:
        return 1
    else:
        return (x*factorial(x-1))

def sin(x):
    sum = 0
    for n in range(0, Nmax+1):
        num = ((-1)**n)*(x**(2*n+1))
        intw = (2*n+1)
        deno = factorial(intw)
        term = num/deno
        sum += term
    return sum
print(sin(15))

def cos(x):
    sum = 0
    for n in range(0, Nmax+1): #failed at n=0 #fixed
        num = ((-1)**n)*(x**(2*n))
        intw = (2*n)
        deno = factorial(intw)
        term = num/deno
        sum += term
    return sum#+1 #I'm not sure why it adds 1 for cos here so I add +1 in sum to -1 for the answer #fixed
print(cos(3.14))

def tan(x):
    return sin(x)/cos(x)

def sec(x):
    return 1/cos(x)

def csec(x):
    return 1/sin(x)

def cotan(x):
    return 1/tan(x)
