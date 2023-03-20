from math import sin

import numpy as np
from numpy import array,arange
#from pylab import plot,xlabel,show
import matplotlib.pyplot as plt

def f(r,t,l,g):

    theta = r[0]
    omega = r[1]
    ftheta = omega
    fomega = -(g/l)*np.sin(theta)
    return array([ftheta,fomega],float)

a = 0.0
b = 10.0
N = 1000
h = (b-a)/N

tpoints = arange(a,b,h)
thetapoints = []
ypoints = []
theta_0=float(input("what is the initial theta"))
l=float(input("what is the length op the pendulum"))
g=float(input("what is gravity?"))
r = array([theta_0,0],float)
for t in tpoints:
    thetapoints.append(r[0])
    ypoints.append(r[1])
    k1 = h*f(r,t,l,g)
    k2 = h*f(r+0.5*k1,t+0.5*h,l,g)
    k3 = h*f(r+0.5*k2,t+0.5*h,l,g)
    k4 = h*f(r+k3,t+h,l,g)
    r += (k1+2*k2+2*k3+k4)/6
plt.ion()
plt.figure(1)
plt.plot(tpoints,thetapoints)
#plt.plot(tpoints,ypoints)
#plt.figure(2)

#plt.plot(xpoints,ypoints)

plt.xlabel("t")
plt.show()