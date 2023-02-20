from __future__ import print_function,division
import numpy as np

N=1000
half_N=int(N/2)
a=0
b=2

def f(x):
    f=x**4-2*x+1
    return f


def simpson(a,b,f,N):
     h=(b-a)/N
     s_1=0
     s_2=0
     for k in range (1,half_N):
         s_1+=f(a+(2*k-1)*h)
     
     for k in range (1,half_N+1):
         s_2+=f(a+2*k*h)
         
     I=(1/3)*h*(f(a)+f(b)+4*s_1+2*s_2)
     return I
         
print(simpson(a,b,f,N))
