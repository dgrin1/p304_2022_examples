from math import sin
from numpy import arange,log,exp
import matplotlib.pyplot as plt

rate=log(2.)/5730.
#Exponential decay rate
def f(x,t):
    return -rate*x
#bounaries and lists
a = 0.0
b = 800000.0
N = 4000
h = (b-a)/N

tpoints = arange(a,b,h)
xpoints = []
x = 1.

#Rk4
for t in tpoints:
    xpoints.append(x)
    k1 = h*f(x,t)
    k2 = h*f(x+0.5*k1,t+0.5*h)
    k3 = h*f(x+0.5*k2,t+0.5*h)
    k4 = h*f(x+k3,t+h)
    x += (k1+2*k2+2*k3+k4)/6
#plots
plt.plot(tpoints,xpoints,'m')
plt.plot(tpoints,exp(-rate*tpoints),'b*')
plt.xlabel('years')
plt.ylabel('Fractional remaining populations')

plt.xlim([1.e4,1.e6])
plt.ion()
plt.show()
plt.xscale('log')
plt.yscale('log')
