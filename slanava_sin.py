import numpy as np
x=0.3
Nmax=7


def sin_sl(x):
    sum=0
#loop up to Nmax
    for n in range(0,Nmax+1):
        #print(n)
        numerator=((-1)**n)*(x**(2*n+1)) #taylor series numerator
        #sum+=term
        int_want=2*n+1 #determine integer whose factorial we want
        #print(int_want)
        #factorial=1
        #for j in range(int_want,0,-1): #write downward running loop that gets from factorial target to 1
            #factorial=factorial*j
        #print(n,int_want,factorial)
        denominator=factorial(int_want)
        term=numerator/denominator
        sum+=term
        #print(n,factorial)
    return sum
#print(sin_sl(0.3))

def factorial(x):
  if(x==1):
    fac=1
  else:
    fac=x*factorial(x-1)
  return fac
print(factorial(3))
