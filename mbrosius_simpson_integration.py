from __future__ import print_function,division
import numpy as np
import matplotlib.pyplot as plt
plt.rc('text',usetex=True)
plt.rc('font', family='serif',serif='Palatino')

def f(x):
    f=x**4-2*x+1
    return f


def simpson(a,b,f,N):
     h=(b-a)/N
     half_N=int(N/2)
     s_1=0
     s_2=0
     for k in range (1,half_N):
         s_1+=f(a+(2*k-1)*h)
     
     for k in range (1,half_N+1):
         s_2+=f(a+2*k*h)
         
     I=(1/3)*h*(f(a)+f(b)+4*s_1+2*s_2)
     return I
         
print(simpson(0,2,f,1000))

error_list=[]
N_list=[]
for N in range (2,1000,2):
    simpson1=simpson(0,2,f,N)
    simpson_better=simpson(0,2,f,N+2)
    error=(simpson_better-simpson1)/simpson1
    error_list.append(error)
    N_list.append(N)
    
plt.plot(N_list,error_list)
plt.title(r'Simpson Integration Error ',fontsize=24,color='k')
plt.xlabel(r'Number of Points Used (N)')
plt.ylabel(r'Error of Simpson Integral')
plt.yscale('log')
plt.show()
