from math import tanh,cosh,cos, tan
import  numpy as np
from pylab import plot,show, legend, scatter

accuracy = 1e-12

def arctanh(u):
    x = 0.0
    delta = 1.0
    while abs(delta)>accuracy:
        delta = (tanh(x)-u)*cosh(x)**2
        x -= delta
    return x

def sin(u):
    x = 0.0
    delta = 1.0
    while abs(delta)>accuracy:
        delta = (np.sin(x)-u)/np.cos(x)
        x -= delta
    return x

def atan(u):   # using Newton-Rapsom method to solve the intial guess iteration
    x = 0.0
    delta = 1.0
    while abs(delta)>accuracy:
        delta = (tan(x)-u)*np.cos(x)**2
        x -= delta
    return x

upoints = np.linspace(-0.99,0.99,100)
xpoints = []
for u in upoints:
    xpoints.append(atan(u))
plot(upoints,xpoints, label = 'Function')    # plots the arctan we calculated
scatter(upoints,np.arctan(upoints), s=2, c='r', label = 'numpy')   # plots the arctan from numpy
legend()
show()
