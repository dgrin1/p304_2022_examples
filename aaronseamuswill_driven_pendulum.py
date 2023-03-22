# Author: Seamus Flannery
# Newman Exercise 8.5ab
# Run this file from the command line, all functions are called in the executable.
# In Collaboration with Aaron Xu and Will Flanders
import numpy as np
import matplotlib.pyplot as plt


plt.rc('text', usetex=True)
plt.rc('font', family='serif', serif='Palatino')
g = -9.8  # m/s^2
length = 1  # meters
C = 2  # s^-2
cap_omega = 4.9  # s^-1
# TODO find the cap_omega value for which the oscillator resonates - swinging widely from side to side


def f(r, t):
    w = r[0]
    theta = r[1]
    fw = (-g/length)*np.sin(theta)+C*np.cos(theta)*np.sin(cap_omega*t)
    ftheta = w
    return np.array([fw, ftheta], float)


a = 0.0
b = 6.0
N = 400000  # TODO how to pick the right one here?
h = (b-a)/N

tpoints = np.arange(a, b, h)
thetapoints = []
omegapoints = []

r = np.array([0, 0], float)
for t in tpoints:
    omegapoints.append(r[0])
    thetapoints.append(r[1])
    k1 = h*f(r, t)
    k2 = h*f(r*0.5*k1, t+0.5*h)
    k3 = h*f(r+0.5*k2, t+0.5*h)
    k4 = h*f(r+k3, t+h)
    r += (k1+2*k2+2*k3+k4)
plt.plot(tpoints, thetapoints, label="theta")
plt.plot(tpoints, omegapoints, label="omega")
plt.xlabel("t")
plt.legend()
plt.title("theta vs. time")
plt.show()
