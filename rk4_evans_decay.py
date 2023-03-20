from math import sin
import numpy as np
from matplotlib.pyplot import plot,xlabel,ylabel,show


l = 1.2e-4
N_o = 10000

def g(t):
    return N_o*np.exp(-l*t)   #solution to the Diff Eq

def f(x, t):
    return -x*l   # Diff Eq

a = 0.0
b = 100000.0
N = 100000
h = (b-a)/N

tpoints = np.arange(a,b,h)
xpoints = []
x = 10000   # number of atoms

for t in tpoints:
    xpoints.append(x)
    k1 = h*f(x,t)
    k2 = h*f(x+0.5*k1,t+0.5*h)
    k3 = h*f(x+0.5*k2,t+0.5*h)
    k4 = h*f(x+k3,t+h)
    x += (k1+2*k2+2*k3+k4)/6

ypoints = [g(t) for t in tpoints]   # y points used for the solution function

error = []
for t in range(len(tpoints)):
    xi = xpoints[t]
    ti = tpoints[t]
    er = f(xi, ti) - g(ti)
    error.append(er)

plot(tpoints, error)  # plotting the error
plot(tpoints,ypoints)   # poltting the solution eq
plot(tpoints,xpoints)   # plotting the diff eq 
xlabel("theta")
ylabel("y(t)")
show()
