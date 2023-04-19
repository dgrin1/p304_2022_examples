from math import sin,cos
from numpy import arange
from pylab import plot,xlabel,ylabel,show
import numpy as np

m = 0.15
B = 4.1e-4
omega = 1800 # rpm
g = 9.81 #m/s

def F_v(v):
    F_v = 0.0039 + (0.0058/(1+((np.exp(v-35))/5)))
    return(F_v)

def pitch(r,t):
    x = r[0]
    y = r[1]
    z = r[2]
    v_x = r[3]
    v_y = r[4]
    v_z = r[5]
    theta = r[6]
    phi = r[7]
    speed = np.sqrt(v_x**2+v_y**2+v_z**2)
    dx = v_x
    dy = v_y
    dz = v_z
    dv_x = -F_v(v_x)*v_x + B*omega*(v_z*sin(phi)-v_y*cos(phi))
    dv_y = -F_v(v_y)*v_y + B*omega*v_x*cos(phi)
    dv_z = -g-F_v(v_z)*v_z + B*omega*v_x*sin(phi)
    r = np.array([dx,dy,dz,dv_x,dv_y,dv_z,theta,phi],float)
    return (r)

a = 0.0
b = 60.0
N = 100000
h = (b-a)/N

tpoints = arange(a,b,h)
ypoints = []
xpoints = []

# initial conditions for fastball
v_0 = 85 # m/s
theta = 1 * np.pi/180 # radians
phi = 225 * np.pi/180 #radians
position = [0,0,0]
velocity = [v_0*cos(theta),0,v_0*sin(theta)]

r = position + velocity
r.append(theta)
r.append(phi)

r = np.array(r,float)
# r = [x positon, y position, z position, x velocity, y velocity, z velocity, theta, phi]

for t in tpoints:
    xpoints.append(r[0])
    ypoints.append(r[1])
    k1 = h*pitch(r,t)
    k2 = h*pitch(r+0.5*k1,t+0.5*h)
    k3 = h*pitch(r+0.5*k2,t+0.5*h)
    k4 = h*pitch(r+k3,t+h)
    r += (k1+2*k2+2*k3+k4)/6

plot(xpoints,ypoints)
xlabel("x")
ylabel("y")
show()


plot(tpoints,xpoints)
xlabel("theta")
ylabel("y(t)")
show()
