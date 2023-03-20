from math import sin
from numpy import array,arange
#from pylab import plot,xlabel,show
import matplotlib.pyplot as plt

g=-9.8
l=float(input("please input an initial length of the pendulum"))
omega_0=0
theta_0=float(input("please input an initial theta"))

def f(r,t):
    theta = r[0]
    omega = r[1]
    ftheta = omega
    fomega = -(g/l)*sin(theta)
    return array([ftheta,fomega],float)

a = 0.0
b = 100.0
N = 10000
h = (b-a)/N

tpoints = arange(a,b,h)
thetapoints = []
omegapoints = []

r = array([theta_0,omega_0],float)
for t in tpoints:
    thetapoints.append(r[0])
    omegapoints.append(r[1])
    k1 = h*f(r,t)
    k2 = h*f(r+0.5*k1,t+0.5*h)
    k3 = h*f(r+0.5*k2,t+0.5*h)
    k4 = h*f(r+k3,t+h)
    r += (k1+2*k2+2*k3+k4)/6


plt.plot(tpoints,thetapoints)
plt.xlabel("t")
plt.show()
