from math import sin
from numpy import arange
from pylab import plot,xlabel,ylabel,show
import numpy as np

l = 1.2e-4

def f(x,t):
    return -l*x

a = 0.0
b = 40000
N = 100000
h = (b-a)/N

tpoints = arange(a,b,h)
xpoints = []
x = 1000000

for t in tpoints:
    xpoints.append(x)
    k1 = h*f(x,t)
    k2 = h*f(x+0.5*k1,t+0.5*h)
    k3 = h*f(x+0.5*k2,t+0.5*h)
    k4 = h*f(x+k3,t+h)
    x += (k1+2*k2+2*k3+k4)/6


N_o = 1000000
def g(x):
    return N_o*np.exp(-l*x)

points = np.linspace(a,b,20)
ypoints = [g(x) for x in points]

plot(points,ypoints,"o")
xlabel("theta")
ylabel("y(t)")

plot(tpoints,xpoints)
xlabel("theta")
ylabel("y(t)")
show()
