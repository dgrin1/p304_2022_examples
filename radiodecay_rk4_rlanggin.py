from math import sin
from numpy import arange
from pylab import plot,xlabel,ylabel,show
import numpy as np

#Radioactive decay
l = 1.2*10**(-4)

def f(x):
    return -l*x #operating on the differential equation
    
#RK4 Method
a = 0.0 # left most time point
b = 1000.0 # right most time point
N = 10000
h = (b-a)/N # determine step size

tpoints = arange(a,b,h) # np array of points
xpoints = [] # empty list for sols
x = 1000.0 # initial condition on x, this should be the starting height?

for t in tpoints:
    xpoints.append(x)
    k1 = h*f(x)
    k2 = h*f(x+0.5*k1)
    k3 = h*f(x+0.5*k2)
    k4 = h*f(x+k3)
    x += (k1+2*k2+2*k3+k4)/6
    
# # # Analytic Solution (this is for the decay problem)
# N_0 = tpoints
# N_a = N_0 * np.e**(-xpoints)

plot(tpoints,xpoints)
# you should also plot the error here 
#(tpoints,N_a)
xlabel("x") 
ylabel("f(x)")
show()
