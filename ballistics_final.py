from math import sin,cos

import matplotlib.pyplot as plt
from numpy import arange
from pylab import plot,xlabel,ylabel,show
import numpy as np

m = 0.15
B = 4.1e-4
omega = 1800 # rpm
g = 9.81 #m/s

def F(v):
    F = 0.0039 + (0.0058/(1+((np.exp(v-35))/5)))
    return(F)

def pitch(r,t):
    x = r[0]
    y = r[1]
    z = r[2]
    v_x = r[3]
    v_y = r[4]
    v_z = r[5]
    speed = np.sqrt(v_x**2+v_y**2+v_z**2)
    dx = v_x
    dy = v_y
    dz = v_z
    dv_x = -F(v_x) * v_x + B * omega_vec[0] * (v_z * sin(phi) - v_y * cos(phi))
    dv_y = -F(v_y) * v_y + B * omega_vec[1] * v_x * cos(phi)
    dv_z = -g - F(v_z) * v_z + B * omega_vec[2] * v_x * sin(phi)
    r = np.array([dx,dy,dz,dv_x,dv_y,dv_z],float)
    return (r)

a = 0.0
b = 18.44/85
N = 10000
h = (b-a)/N
# h = 18.44/85

tpoints = arange(a,b,h)

# initial conditions for fastball
v_0 = 85 # m/s
theta = 1 * np.pi/180 # radians
phi = 225 * np.pi/180
position = [0,0,0]
velocity = [v_0*cos(theta),0,v_0*sin(theta)]
omega_vec = [omega*0,omega*sin(phi),omega*cos(phi)]

r = position + velocity

r = np.array(r,float)

# r = r_0.copy()
# r = [x position, y position, z position, x velocity, y velocity, z velocity, theta, phi]

# y vs x for fastball
# reset initial conditions
# r = r_0.copy()

xpoints_y = []
ypoints = []

for t in tpoints:
    xpoints_y.append(r[0])
    ypoints.append(r[1])
    k1 = h*pitch(r,t)
    k2 = h*pitch(r+0.5*k1,t+0.5*h)
    k3 = h*pitch(r+0.5*k2,t+0.5*h)
    k4 = h*pitch(r+k3,t+h)
    r += (k1+2*k2+2*k3+k4)/6

#z vs x for fastball
# reset initial conditions
r = r_0.copy()


xpoints_z = []
zpoints = []

for t in tpoints:
    xpoints_z.append(r[0])
    zpoints.append(r[2])
    k1 = h*pitch(r,t)
    k2 = h*pitch(r+0.5*k1,t+0.5*h)
    k3 = h*pitch(r+0.5*k2,t+0.5*h)
    k4 = h*pitch(r+k3,t+h)
    r += (k1+2*k2+2*k3+k4)/6

plot(xpoints_z,zpoints,label = "z")
plot(xpoints_y,ypoints,label = "y")
plt.suptitle("Position of a Fastball Pitch")
xlabel(r'$x$ (meters)')
ylabel(r'Displacement in the $yz$-plane')
plt.legend()
show()






# initial conditions for curveball
v_0 = 85 # m/s
theta = 1 * np.pi/180 # radians
phi = 45 * np.pi/180
position = [0,0,0]
velocity = [v_0*cos(theta),0,v_0*sin(theta)]

r = position + velocity
r.append(theta)
r.append(phi)

r_0 = np.array(r,float)

r = r_0.copy()
# r = [x position, y position, z position, x velocity, y velocity, z velocity, theta, phi]

# y vs x for fastball
# reset initial conditions
r = r_0.copy()

xpoints_y = []
ypoints = []

for t in tpoints:
    xpoints_y.append(r[0])
    ypoints.append(r[1])
    k1 = h*pitch(r,t)
    k2 = h*pitch(r+0.5*k1,t+0.5*h)
    k3 = h*pitch(r+0.5*k2,t+0.5*h)
    k4 = h*pitch(r+k3,t+h)
    r += (k1+2*k2+2*k3+k4)/6

#z vs x for fastball
# reset initial conditions
r = r_0.copy()


xpoints_z = []
zpoints = []

for t in tpoints:
    xpoints_z.append(r[0])
    zpoints.append(r[2])
    k1 = h*pitch(r,t)
    k2 = h*pitch(r+0.5*k1,t+0.5*h)
    k3 = h*pitch(r+0.5*k2,t+0.5*h)
    k4 = h*pitch(r+k3,t+h)
    r += (k1+2*k2+2*k3+k4)/6

plot(xpoints_z,zpoints,label = "z")
plot(xpoints_y,ypoints,label = "y")
plt.suptitle("Position of a Slider Pitch")
xlabel(r'$x$ (meters)')
ylabel(r'Displacement in the $yz$-plane')
plt.legend()
show()
