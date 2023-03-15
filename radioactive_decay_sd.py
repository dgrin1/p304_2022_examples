import math as math
import numpy as np
import matplotlib.pyplot as plt

l = 1.2*10**(-4)

def f(x):
    return -l*x #operating on the differential equation

#initial conditions
a = 0.0
b = 100000.0
N = 100000
h = (b-a)/N

tpoints = np.arange(a,b,h)
xpoints = []
x = 10000.0

for t in tpoints:
    xpoints.append(x)
    k1 = h*f(x)
    k2 = h*f(x+0.5*k1)
    k3 = h*f(x+0.5*k2)
    k4 = h*f(x+k3)
    x += (k1+2*k2+2*k3+k4)/6

plt.plot(tpoints,xpoints)
plt.xlabel("theta")
plt.ylabel("y(t)")
plt.show()
