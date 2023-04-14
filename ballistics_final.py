from math import sin,cos
from numpy import arange
from pylab import plot,xlabel,ylabel,show
import numpy as np

m = 0.15
B = 4.1e-4
omega = 1800 # rpm
g = 9.81 #m/s

def F_v(v):
    F_v = 0.0039 + (0.0058/(1+(np.exp(v-35))/5))
    return(F_v)

def pitch(position,velocity,theta,phi):
    x = position[0]
    y = position[1]
    z = position[2]
    v_x = velocity[0]
    v_y = velocity[1]
    v_z = velocity[2]
    speed = np.sqrt(v_x**2+v_y**2+v_z**2)
    dx = v_x
    dy = v_y
    dz = v_z
    position_sol = [dx,dy,dz]
    dv_x = -F_v(speed)*v_x + B*omega*(v_z*sin(phi)-v_y*cos(phi))
    dv_y = -F_v(speed)*v_y + B*omega*v_x*cos(phi)
    dv_z = -g-F_v(speed)*v_z + B*omega*v_x*sin(phi)
    velocity_solution = [dv_x,dv_y,dv_z]
    return (position_sol,velocity_solution)

a = 0.0
b = 60
N = 10000
h = (b-a)/N

tpoints = arange(a,b,h)
xpoints = []

# initial conditions for fastball
v_0 = 35 # m/s
theta = 1 * np.pi/180 # radians
phi = 225 * np.pi/180
position = [0,0,0]
velocity = [v_0*cos(theta),0,v_0*sin(theta)]


for t in tpoints:
    xpoints.append(x)
    k1 = h*f(x,t)
    k2 = h*f(x+0.5*k1,t+0.5*h)
    k3 = h*f(x+0.5*k2,t+0.5*h)
    k4 = h*f(x+k3,t+h)
    x += (k1+2*k2+2*k3+k4)/6


N_o = 1000000
def g(x):
    return N_o*np.exp(-l*x)

points = np.linspace(a,b,20)
ypoints = [g(x) for x in points]

plot(points,ypoints,"o")
xlabel("theta")
ylabel("y(t)")

plot(tpoints,xpoints)
xlabel("theta")
ylabel("y(t)")
show()
