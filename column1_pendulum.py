from math import sin
from numpy import array,arange
#from pylab import plot,xlabel,show
import matplotlib.pyplot as plt

#input initial conditions
g=-9.8
l=float(input("please input an initial length of the pendulum in meters: "))
omega_0=0
theta_0=float(input("please input an initial angle (from vertical) in radians: "))
#define function in terms of theta and omega
def f(r,t):
    theta = r[0]
    omega = r[1]
    ftheta = omega
    fomega = -(g/l)*sin(theta)
    return array([ftheta,fomega],float)

#set time and step size
a = 0.0
b = 10.0
N = 1000
h = (b-a)/N

#create arrays
tpoints = arange(a,b,h)
thetapoints = []
omegapoints = []

#define r with initial conditions
r = array([theta_0,omega_0],float)

#implement rk4 method
for t in tpoints:
    thetapoints.append(r[0])
    omegapoints.append(r[1])
    k1 = h*f(r,t)
    k2 = h*f(r+0.5*k1,t+0.5*h)
    k3 = h*f(r+0.5*k2,t+0.5*h)
    k4 = h*f(r+k3,t+h)
    r += (k1+2*k2+2*k3+k4)/6

#plot
plt.plot(tpoints,thetapoints)
plt.xlabel("t")
plt.show()
