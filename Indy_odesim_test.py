from math import sin, cos
from numpy import array,arange
#from pylab import plot,xlabel,show
import matplotlib.pyplot as plt

def f(r,t):
    theta = r[0]
    w = r[1]
    fx = w
    fy = -(g/l)*sin(theta)
    return array([fx,fy],float)

g = 9.8
l = 1
a = 0.0
b = 10.0
N = 10
h = (b-a)/N

tpoints = arange(a,b,h)
xpoints = []
ypoints = []

r = array([1.0,1.0],float)
for t in tpoints:
    xpoints.append(r[0])
    ypoints.append(r[1])
    k1 = h*f(r,t)
    k2 = h*f(r+0.5*k1,t+0.5*h)
    k3 = h*f(r+0.5*k2,t+0.5*h)
    k4 = h*f(r+k3,t+h)
    r += (k1+2*k2+2*k3+k4)/6
#plt.ion()
plt.figure(1)
plt.plot(tpoints,xpoints)
plt.plot(tpoints,ypoints)
plt.figure(2)

plt.plot(xpoints,ypoints)

plt.xlabel("t")
plt.show()
