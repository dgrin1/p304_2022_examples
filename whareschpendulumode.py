from math import sin
from numpy import array,arange
#from pylab import plot,xlabel,show
import matplotlib.pyplot as plt

def f(r,t):
    g=9.8
    l=5
    theta = r[0]
    thetadot = r[1]
    ftheta = thetadot
    fthetadot = (-g*sin(theta))/l
    return array([ftheta,fthetadot],float)

a = 0.0
b = 10.0
N = 1000
h = (b-a)/N

tpoints = arange(a,b,h)
xpoints = []
ypoints = []

r = array([1.0,0],float)
for t in tpoints:
    xpoints.append(r[0])
    ypoints.append(r[1])
    k1 = h*f(r,t)
    k2 = h*f(r+0.5*k1,t+0.5*h)
    k3 = h*f(r+0.5*k2,t+0.5*h)
    k4 = h*f(r+k3,t+h)
    r += (k1+2*k2+2*k3+k4)/6

plt.figure(1)
plt.plot(tpoints,xpoints)
plt.plot(tpoints,ypoints)
plt.figure(2)

plt.plot(xpoints,ypoints)

plt.xlabel("t")
plt.show()
