import math
from numpy import arange
from pylab import plot,xlabel,ylabel,show



lamb = 1.2*10**-4

def f(t, N):
    return -lamb * N

a = 0.0
b = 10000.0
n = 80
h = (b-a)/n

tpoints = arange(a,b,h)
xpoints = []
N = 100

for t in tpoints:
    xpoints.append(N)
    k1 = h*f(N,t)
    k2 = h*f(N+0.5*k1,t+0.5*h)
    k3 = h*f(N+0.5*k2,t+0.5*h)
    k4 = h*f(N+k3,t+h)
    N += (k1+2*k2+2*k3+k4)/6

plot(tpoints,xpoints)
xlabel("t")
ylabel("N")
show()
