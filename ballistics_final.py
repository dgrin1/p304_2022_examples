from math import sin,cos

import matplotlib.pyplot as plt
from numpy import arange
from pylab import plot,xlabel,ylabel,show
import numpy as np

B = 4.1e-4
omega = 20 * 0.1047198 # rpm
g = 9.81 #m/s
l = 18.44

def F(v):
    F = 0.0039 + (0.0058/(1+((np.exp(v-35))/5)))
    return(F)

def G(phi):
    G = 0.5 * (sin(4*phi) - 0.25 * sin(8*phi) + 0.08 * sin(12*phi) - 0.025 * sin(16*phi))
    return(G)

def pitch(r,t):
    x = r[0]
    y = r[1]
    z = r[2]
    v_x = r[3]
    v_y = r[4]
    v_z = r[5]
    phi = r[6]
    speed = np.sqrt(v_x**2+v_y**2+v_z**2)
    dx = v_x
    dy = v_y
    dz = v_z
    dv_x = -F(speed) *speed * v_x
    dv_y = -F(speed) *speed * v_y + g * G(phi)
    dv_z = -g - F(speed) *speed * v_z
    dphi = omega
    r = np.array([dx,dy,dz,dv_x,dv_y,dv_z,dphi],float)
    return (r)



# initial conditions for screwball
v_0 = 65 * 0.44704 # m/s
theta = 4 * np.pi/180 # radians
phi_0 = 22.5 * np.pi/180
position = [0,0,0]
velocity = [v_0*cos(theta),0,v_0*sin(theta)]

r = position + velocity
r.append(phi_0)

r = np.array(r,float)
# r = [x position, y position, z position, x velocity, y velocity, z velocity, phi]

a = 0.0
b = l/v_0
N = 1000
h = (b-a)/N
tpoints = arange(a,b,h)

# y vs x for screwball
# reset initial conditions

r0 = r.copy()
r22 = r.copy()
r45 = r.copy()
r67 = r.copy()

xpoints0 = []
ypoints0 = []

for t in tpoints:
    xpoints0.append(r0[0])
    ypoints0.append(r0[1])
    k1 = h*pitch(r0,t)
    k2 = h*pitch(r0+0.5*k1,t+0.5*h)
    k3 = h*pitch(r0+0.5*k2,t+0.5*h)
    k4 = h*pitch(r0+k3,t+h)
    r0 += (k1+2*k2+2*k3+k4)/6

xpoints22 = []
ypoints22 = []

for t in tpoints:
    xpoints22.append(r22[0])
    ypoints22.append(r22[1])
    k1 = h*pitch(r22,t)
    k2 = h*pitch(r22+0.5*k1,t+0.5*h)
    k3 = h*pitch(r22+0.5*k2,t+0.5*h)
    k4 = h*pitch(r22+k3,t+h)
    r22 += (k1+2*k2+2*k3+k4)/6

xpoints45 = []
ypoints45 = []

for t in tpoints:
    xpoints45.append(r45[0])
    ypoints0.append(r45[1])
    k1 = h*pitch(r45,t)
    k2 = h*pitch(r45+0.5*k1,t+0.5*h)
    k3 = h*pitch(r45+0.5*k2,t+0.5*h)
    k4 = h*pitch(r45+k3,t+h)
    r45 += (k1+2*k2+2*k3+k4)/6

xpoints67 = []
ypoints67 = []

for t in tpoints:
    xpoints67.append(r67[0])
    ypoints0.append(r67[1])
    k1 = h*pitch(r67,t)
    k2 = h*pitch(r67+0.5*k1,t+0.5*h)
    k3 = h*pitch(r67+0.5*k2,t+0.5*h)
    k4 = h*pitch(r67+k3,t+h)
    r67 += (k1+2*k2+2*k3+k4)/6

plot(xpoints0,ypoints0,label = "0")
plot(xpoints22,ypoints22,label = "22.5")
plot(xpoints45,ypoints45,label = "45")
plot(xpoints67,ypoints67,label = "67.5")
plt.suptitle("Position of a Screwball Pitch")
plt.xlim(0, 18)
plt.ylim(-1.25,0.65)
ylabel(r'Displacement in the $yz$-plane (meters)')
plt.legend()
show()


from math import sin,cos

import matplotlib.pyplot as plt
from numpy import arange
from pylab import plot,xlabel,ylabel,show
import numpy as np

B = 4.1e-4
omega = 1800 * 0.1047198 # rpm
g = 9.81 #m/s
l = 18.44

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
    dv_x = (-F(speed) *speed * v_x) + (B * omega * (v_z * sin(phi) - v_y * cos(phi)))
    dv_y = (-F(speed) *speed * v_y) + (B * omega * v_x * cos(phi))
    dv_z = (-g - F(speed) *speed * v_z) - (B * omega * v_x * sin(phi))
    r = np.array([dx,dy,dz,dv_x,dv_y,dv_z],float)
    return (r)


# initial conditions for slider
v_0 = 85 * 0.44704 # m/s
theta = 1 * np.pi/180 # radians
phi = 0 * np.pi/180
position = [0,0,0]
velocity = [v_0*cos(theta),0,v_0*sin(theta)]

r = position + velocity

r = np.array(r,float)
# r = [x position, y position, z position, x velocity, y velocity, z velocity, theta, phi]

a = 0.0
b = l/v_0
N = 1000
h = (b-a)/N
tpoints = arange(a,b,h)

# y vs x for slider
# reset initial conditions

r_xy = r.copy()
r_xz = r.copy()

xpoints_y = []
ypoints = []

for t in tpoints:
    xpoints_y.append(r_xy[0])
    ypoints.append(r_xy[1])
    k1 = h*pitch(r_xy,t)
    k2 = h*pitch(r_xy+0.5*k1,t+0.5*h)
    k3 = h*pitch(r_xy+0.5*k2,t+0.5*h)
    k4 = h*pitch(r_xy+k3,t+h)
    r_xy += (k1+2*k2+2*k3+k4)/6

#z vs x for slider
# reset initial conditions

xpoints_z = []
zpoints = []

for t in tpoints:
    xpoints_z.append(r_xz[0])
    zpoints.append(r_xz[2])
    k1 = h*pitch(r_xz,t)
    k2 = h*pitch(r_xz+0.5*k1,t+0.5*h)
    k3 = h*pitch(r_xz+0.5*k2,t+0.5*h)
    k4 = h*pitch(r_xz+k3,t+h)
    r_xz += (k1+2*k2+2*k3+k4)/6

plot(xpoints_z,zpoints,label = "z")
plot(xpoints_y,ypoints,label = "y")
plt.suptitle("Position of a Slider Pitch")
plt.xlim(0, 18)
plt.ylim(-1.25,0.65)
ylabel(r'Displacement in the $yz$-plane (meters)')
plt.legend()
show()
