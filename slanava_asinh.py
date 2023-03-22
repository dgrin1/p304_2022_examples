from math import tanh,cosh,sinh
from numpy import arcsinh as asinh
from numpy import linspace
import numpy as np
import matplotlib.pyplot as plt

accuracy = 1e-12

def arcsinh(u):
    x = 0.0
    delta = 1.0
    while abs(delta)>accuracy:
        delta = (sinh(x)-u)/cosh(x)
        x -= delta
    return x

upoints = linspace(-0.99,0.99,100)
xpoints = []
for u in upoints:
    xpoints.append(arcsinh(u))
plt.plot(upoints,xpoints,'r')
plt.plot(upoints,asinh(upoints),'b')
plt.show()

error = xpoints - asinh(upoints)
error/=xpoints
plt.plot(upoints,np.abs(error))
plt.yscale('log')
plt.show()
