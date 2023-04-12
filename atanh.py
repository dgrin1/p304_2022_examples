from math import tanh,cosh,sin,cos

import matplotlib.pyplot as plt
import numpy as np
from pylab import plot,show

accuracy = 1e-12

def arctanh(u):
    x = 0.0
    delta = 1.0
    while abs(delta)>accuracy:
        delta = (tanh(x)-u)*cosh(x)**2
        x -= delta
    return xz

def arcsin(u):
    x = 0.0
    delta = 1.0
    while abs(delta)>accuracy:
        delta = (np.sin(x)-u)/(np.cos(x))
        x -= delta
    return x

upoints = np.linspace(-0.99,0.99,100)
xpoints = []
for u in upoints:
    xpoints.append(sin(u))
plot(upoints,xpoints,label = "function")
plot(upoints,np.arcsin(upoints),label = "numpy")
plt.legend()
show()
