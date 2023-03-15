from math import sin
from numpy import arange,exp
import matplotlib.pyplot as plt


lamda = 1.2e-4

def f(N,t): #define differential eq
    return -lamda*N

def N_analytic(t): #define solution analytically
    return 1.0*exp(-lamda*t)
    
a=0.0 #set time range and number of data points
b=10000
n=100
h=(b-a)/n

tpoints = arange(a,b,h) #create empty lists for plotting
Npoints = []
Nanalytic = []
errorpoints = []
N = 1.0



for t in tpoints:
    Npoints.append(N) #add computed N and analytic N to lists
    Nanalytic.append(N_analytic(t))
    error=abs((N_analytic(t)-N)/N_analytic(t)) #computer fractional error and add to list
    errorpoints.append(error)
    k1 = h*f(N,t) #go through rk4 process to compute new N
    k2 = h*f(N+0.5*k1,t+0.5*h)
    k3 = h*f(N+0.5*k2,t+0.5*h)
    k4 = h*f(N+k3,t+h)
    N += (k1+2*k2+2*k3+k4)/6
    
    
plt.figure() #plot rk4 and analytic solutions
plt.plot(tpoints,Npoints,label='Runge-Kutta Solution')
plt.plot(tpoints,Nanalytic,label='Analytic Solution')
plt.legend()
plt.xlabel("years")
plt.ylabel("fractional remaining populations")
plt.show()

plt.figure() #plot error
plt.plot(tpoints,errorpoints)
plt.xscale('log')
plt.yscale('log')
plt.xlabel('years')
plt.ylabel('error')
plt.show()
