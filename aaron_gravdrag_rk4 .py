from math import sin
from numpy import arange
from pylab import plot,xlabel,ylabel,show,title

g = 9.81
ba = 1

def f(x,t):
    return g-ba*x

a = 0.0
b = 100.
N = 32
#N = 36 # is the marginal case
h = (b-a)/N

tpoints = arange(a,b,h)
xpoints = []
x = 0.

for t in tpoints:
    xpoints.append(x)
    k1 = h*f(x,t)
    k2 = h*f(x+0.5*k1,t+0.5*h)
    k3 = h*f(x+0.5*k2,t+0.5*h)
    k4 = h*f(x+k3,t+h)
    x += (k1+2*k2+2*k3+k4)/6

plot(tpoints,xpoints)
xlabel("t")
ylabel("v(t)")
title("N=32")
show()
