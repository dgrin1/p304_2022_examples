import math as math
import numpy as np
import matplotlib.pyplot as plt

accuracy = 1e-12

def tan(u):
    x = 0.0
    delta = 1.0
    while abs(delta)>accuracy:
        delta = (tan(x)-u)*np.cos(x)**2
        x -= delta
    return x

upoints = np.linspace(-0.99,0.99,100)
xpoints = []
for u in upoints:
    xpoints.append(tan(u))
plt.plot(upoints,xpoints)
show()