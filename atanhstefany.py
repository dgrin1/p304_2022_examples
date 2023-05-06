from math import tanh,cosh
from numpy import linspace
import numpy as np
import matplotlib.pyplot as plt

accuracy = 1e-12

def arctanh(u):
    x = 0.0
    delta = 1.0
    while abs(delta)>accuracy:
        delta = (np.tanh(x)-u)*np.cosh(x)**2
        x -= delta
    return x

upoints = linspace(-0.99,0.99,100)
xpoints = [arctanh(u) for u in upoints]
plt.plot(upoints,xpoints)
plt.show()
