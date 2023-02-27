from __future__ import print_function,division
import numpy as np
import matplotlib.pyplot as plt
plt.rc('text',usetex=True)
plt.rc('font', family='serif',serif='Palatino')

#define function f
def f(x):
    f=x**4-2*x+1
    return f

#define simpson integration
def simpson(a,b,f,N):

     #set step size and define two sums
     h=(b-a)/N
     half_N=int(N/2)
     s_1=0
     s_2=0
     
     #compute first sum (for odd k values)
     for k in range (1,half_N):
         s_1+=f(a+(2*k-1)*h)
     
     #compute second sum (for even k values)
     for k in range (1,half_N+1):
         s_2+=f(a+2*k*h)
         
     #compute and return integral
     I=(1/3)*h*(f(a)+f(b)+4*s_1+2*s_2)
     return I
         
print(simpson(0,2,f,1000))

#create empty lists
error_list=[]
N_list=[]

#cycle over all even Ns from 2 to 1000
for N in range (2,1000,2):
    #calculcate value of integral, then increase N and calculate another value
    simpson1=simpson(0,2,f,N)
    simpson_better=simpson(0,2,f,N+2)
    
    #calculate error based on two values, add to list
    error=(simpson_better-simpson1)/simpson1
    error_list.append(np.abs(error))
    N_list.append(N)
    
    
#plot error vs N
plt.plot(N_list,error_list)
plt.title(r'Simpson Integration Error ',fontsize=24,color='k')
plt.xlabel(r'Number of Points Used (N)')
plt.ylabel(r'Error of Simpson Integral')
plt.yscale('log')
plt.xscale('log')
plt.show()
