import numpy as np
x=0.3
Nmax=10


def sin_sl(x):
    sumsin=0
#loop up to Nmax
    for n in range(0,Nmax+1):
        #print(n)
        numsin=((-1)**n)*(x**(2*n+1)) #taylor series numerator
        #sum+=term
        int_want_sin=2*n+1 #determine integer whose factorial we want
        #print(int_want)
        #factorial=1
        #for j in range(int_want,0,-1): #write downward running loop that gets from factorial target to 1
            #factorial=factorial*j
        #print(n,int_want,factorial)
        denomsin=factorial(int_want_sin)
        termsin=numsin/denomsin
        sumsin+=termsin
        #print(n,factorial)
    return sumsin
#print(sin_sl(0.3))

def cos_sl(x):
    sumcos=0
    for n in range(0,Nmax+1):
        numcos=((-1)**n)*(x**(2*n))
        int_want_cos=2*n
        denomcos=factorial(int_want_cos)
        termcos=numcos/denomcos
        sumcos+=termcos
    return sumcos

def factorial(x):
  if(x==0 or x==1):
    fac=1
  else:
    fac=x*factorial(x-1)
  return fac
