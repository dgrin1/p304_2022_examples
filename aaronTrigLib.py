####################
# Basic Trig Library
# Aaron Xu 
# Feb 2, 2023 
####################
def sin(x): 
    arr = [0]*order
    for n in range(order):
        arr[n] = x**(2*n+1)
    #print(arr)
    sin = sum([arrN * sinCoefsN for arrN, sinCoefsN in zip(arr,sinCoefs)])
    return sin

def cos(x):
    arr = [0]*order
    for n in range(order):
        arr[n] = x**(2*n)
    #print(arr)
    cos = sum([arrN * cosCoefsN for arrN, cosCoefsN in zip(arr,cosCoefs)])
    return cos

def tan(x):
    tan = sin(x)/cos(x)
    return tan

def csc(x):
    cosec = 1/sin(x)
    return cosec

def sec(x): 
    sec = 1/cos(x)
    return sec

def cot(x):
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
order = 10
sinCoefs = makSinCoefs(order)
cosCoefs = makCosCoefs(order)

#Diagnostics
""" print("Sin Coefficients")
print(sinCoefs)
print(sin(1.45)) 
print(cos(1.45))
print(tan(1.45))
print(csc(1.45))
print(sec(1.45))
print(cot(1.45)) """

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