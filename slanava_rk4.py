from math import sin
from numpy import arange
import numpy as np
from pylab import plot,xlabel,ylabel,show

def f(x,t):
    return -(1.2*10**(-4))*x

a = 0.0
b = 10000.0
N = 100
h = (b-a)/N

tpoints = arange(a,b,h)
xpoints = []
x2points = []
x = 10000 #starting number of atoms

for t in tpoints: #runge-kutta 4th order
    xpoints.append(x)
    k1 = h*f(x,t)
    k2 = h*f(x+0.5*k1,t+0.5*h)
    k3 = h*f(x+0.5*k2,t+0.5*h)
    k4 = h*f(x+k3,t+h)
    x += (k1+2*k2+2*k3+k4)/6

for t in tpoints: #analytical solution
    x2 = 10000*np.exp(-1.2*10**(-4)*t)
    x2points.append(x2)

plot(xpoints,tpoints) #plot runge-kutta solution
plot(x2points,tpoints,'r') #plot analyticaln solution
xlabel("Years")
ylabel("Number of Remaining Atoms")
show()
