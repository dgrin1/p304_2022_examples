####################
# Basic Trig Library
# Aaron Xu 
# Feb 2, 2023 
####################
import numpy as np
def sin(x,terms = 50): 
    x = x % (2*3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706)
    arr = [0]*terms
    for n in range(terms):
        arr[n] = x**(2*n+1)
    #print(arr)
    sin = sum([arrN * sinCoefsN for arrN, sinCoefsN in zip(arr,sinCoefs[0:terms])])
    #sin = np.dot(sinCoefs,arr)
    return sin

def cos(x,terms = 50):
    x = x % (2*3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706)
    arr = [0]*terms
    for n in range(terms):
        arr[n] = x**(2*n)
    #print(arr)
    cos = sum([arrN * cosCoefsN for arrN, cosCoefsN in zip(arr,cosCoefs[0:terms])])
    return cos

def tan(x,terms = 50):
    tan = sin(x,terms)/cos(x,terms)
    return tan

def csc(x,terms = 50):
    cosec = 1/sin(x)
    return cosec

def sec(x,terms = 50): 
    sec = 1/cos(x)
    return sec

def cot(x,terms = 50):
    cotan = 1/tan(x)
    return cotan

def factorial(n): 
    if n == 1:
        out = 1
    elif n == 0: 
        out = 1
    else:
        n = n*factorial(n-1)
    return n

def makSinCoefs(order):
    tempFactorial = 1
    sinCoefs = [0]*order
    for n in range(0,order):
        if n != 0:
            tempFactorial = tempFactorial*(2*n+1)*(2*n) 
        sinCoefs[n] = (-1)**n/(tempFactorial)
    return sinCoefs

def makCosCoefs(order):
    tempFactorial = 1
    cosCoefs = [0]*order
    for n in range(0,order):
        if n != 0:
            tempFactorial = tempFactorial*(2*n-1)*(2*n) 
        cosCoefs[n] = (-1)**n/(tempFactorial)
    return cosCoefs

# Runs upon library import 
order = 1000
sinCoefs = makSinCoefs(order)
cosCoefs = makCosCoefs(order)

#Diagnostics
#print("Sin Coefficients")
#print(sinCoefs)
#print(sin(1.45)) 
#print(cos(1.45))
#print(tan(1.45))
#print(csc(1.45))
#print(sec(1.45))
#print(cot(1.45)) """

# Differences Generally emerge at the 14th or 15th decimal when order is 10
# Mathematica    Sin(1.45) = 0.992712991037589
# Aaron order 10 Sin(1.45) = 0.9927129910375886
#                                            ^
# Mathematica    Cos(1.45) = 0.1205027693673666
# Aaron order 10 Cos(1.45) = 0.12050276936736584
#                                            ^
# Mathematica    Tan(1.45) = 8.23809275296561
# Aaron order 10 Tan(1.45) = 8.238092752965658
#                                           ^
# Mathematica    Csc(1.45) = 1.007340499246207
# Aaron order 10 Csc(1.45) = 1.0073404992462072
#                                             ^
# Mathematica    Sec(1.45) = 8.29856446660893
# Aaron order 10 Sec(1.45) = 8.298564466608987
#                                           ^
# Mathematica    Cot(1.45) = 0.1213873198550736
# Aaron order 10 Sec(1.45) = 0.12138731985507285
#                                            ^
