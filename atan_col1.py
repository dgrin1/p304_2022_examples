# Ben, Danny, George, Simon

from math import tanh,cosh,sin,cos,tan

import matplotlib.pyplot as plt
import numpy as np
from pylab import plot,show,scatter

accuracy = 1e-12

# trying to get arctan function

def arctan(u):
    x = 0.0
    delta = 1.0
    while abs(delta)>accuracy:
        # f(x) is tan(x)-u
        # f'(x) is sec^2
        delta = (tan(x)-u)*cos(x)**2
        x -= delta
    return x

upoints = np.linspace(-0.99,0.99,100)
xpoints = []
for u in upoints:
    xpoints.append(arctan(u))
upoints_new = np.linspace(-0.99,0.99,20)
plot(upoints,xpoints,label = "function")

# check arctan with numpy
plot(upoints_new,np.arctan(upoints_new),"o",label = "numpy")
plt.legend()
show()
