#the radioactive decay problem
#N=N0e^-{lamdba*t}
from math import sin

import matplotlib.pyplot as plt
from numpy import arange
from pylab import plot,xlabel,ylabel,show
import numpy as np

lam=-1.2*(10**-4) # set variables
def f(x,t):
    return lam*x

a = 0.0 #sets bounds for graph
b = 10000
N = 100
h = (b-a)/N

tpoints = arange(a,b,h)
xpoints = []
x = 10000

for t in tpoints: #kr4 process
    xpoints.append(x)
    k1 = h*f(x,t)
    k2 = h*f(x+0.5*k1,t+0.5*h)
    k3 = h*f(x+0.5*k2,t+0.5*h)
    k4 = h*f(x+k3,t+h)
    x += (k1+2*k2+2*k3+k4)/6
x=10000
analytic_x=[] #creating the analytic solution to compare to
for t in tpoints:
    y=np.exp(lam*t)*x
    analytic_x.append(y)
plot(xpoints,tpoints)#plot code
plot(analytic_x,tpoints)
xlabel("years")
ylabel("number of atoms")
plt.title("Radioactive decay")
show()

