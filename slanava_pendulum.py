from math import sin
from numpy import array,arange
#from pylab import plot,xlabel,show
import matplotlib.pyplot as plt

g = 9.81
l = float(input("input l value"))
theta_0 = float(input("input inital theta value"))
omega_0 = 0

def f(r,t):
    theta = r[0]
    omega = r[1]
    ftheta = omega
    fomega = (-g/l)*sin(theta)
    return array([ftheta,fomega],float)

a = 0.0
b = 10.0
N = 1000
h = (b-a)/N

tpoints = arange(a,b,h)
theta_points = []
omega_points = []

r = array([theta_0,omega_0],float)
for t in tpoints:
    theta_points.append(r[0])
    omega_points.append(r[1])
    k1 = h*f(r,t)
    k2 = h*f(r+0.5*k1,t+0.5*h)
    k3 = h*f(r+0.5*k2,t+0.5*h)
    k4 = h*f(r+k3,t+h)
    r += (k1+2*k2+2*k3+k4)/6
#plt.ion()
#plt.figure(1)
plt.plot(tpoints,theta_points)
#plt.plot(tpoints,omega_points)
#plt.figure(2)

#plt.plot(theta_points,omega_points)

plt.xlabel("t")
plt.show()
