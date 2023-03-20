from math import sin
from numpy import arange
from pylab import plot,xlabel,ylabel,show,ylim,xlim

def f(x,t):
	L = 1.2*10**(-4)
	return -L*x #N=x

a = 0.0
b = 100000.0
N = 1000
h = (b-a)/N

tpoints = arange(a,b,h)
xpoints = []
x = 100.0

for t in tpoints:
    xpoints.append(x)
    k1 = h*f(x,t)
    k2 = h*f(x+0.5*k1,t+0.5*h)
    k3 = h*f(x+0.5*k2,t+0.5*h)
    k4 = h*f(x+k3,t+h)
    x += (k1+2*k2+2*k3+k4)/6

plot(tpoints,xpoints)
xlabel("t")
ylabel("N(t)")
show()
