from math import sin,cos
import numpy as np
import matplotlib.pyplot as plt
import math as math


l = .1 # length in meters
g = 9.81

def f(r,t):   # function in terms of vector r and time
    theta = r[0]  # defining theta in our vector
    omega = r[1]   # defining omega from the vector 
    ftheta = omega  # defining omega in terms of diff eq
    fomega = -(g/l)*sin(theta)  # defining func in terms of diff eq of omega
    return np.array([ftheta,fomega],float)   # returns array answer

def d(r,t):   # function in terms of vector r and time
    theta = r[0]  # defining theta in our vector
    omega = r[1]   # defining omega from the vector 
    ftheta = omega  # defining omega in terms of diff eq
    fomega = -(g/l)*theta  # defining func in terms of diff eq of omega
    return np.array([ftheta,fomega],float)   # returns array answer

a = 0.0   # defining time interval
b = 100.0
N = 10000   # set number of steps
h = (b-a)/N

tpoints = np.arange(a,b,h)  #setting array for time values
xpoints = []
x = np.array([(17*np.pi)/180,0.0],float) # sets initial vector as given theta in radians and 0

for t in tpoints:   # iterates through time values
    xpoints.append(x[0])   # appends the theta values only
    k1 = h*f(x,t)   #rk4 iteration
    k2 = h*f(x+0.5*k1,t+0.5*h)
    k3 = h*f(x+0.5*k2,t+0.5*h)
    k4 = h*f(x+k3,t+h)
    x += (k1+2*k2+2*k3+k4)/6  # adds to the vector

t2points = np.arange(a,b,h)  #setting array for time values
x2points = []
x = np.array([(17*np.pi)/180,0.0],float) # sets initial vector as given theta in radians and 0

for t in t2points:   # iterates through time values
    x2points.append(x[0])   # appends the theta values only
    k1 = h*d(x,t)   #rk4 iteration
    k2 = h*d(x+0.5*k1,t+0.5*h)
    k3 = h*d(x+0.5*k2,t+0.5*h)
    k4 = h*d(x+k3,t+h)
    x += (k1+2*k2+2*k3+k4)/6  # adds to the vector

plt.plot(t2points,x2points, label ='Harmonic Oscillator')
plt.plot(tpoints,xpoints, label ='Pendulum Position')  # plots and labels
plt.title("Pendulum Position over Time")
plt.xlabel("Time")
plt.ylabel("Angle in Radians")
plt.legend()
plt.show()
