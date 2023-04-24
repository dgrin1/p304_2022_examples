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



# initial conditions for curveball
v_0 = 85 * 0.44704 # m/s
theta = 1 * np.pi/180 # radians
phi = 45 * np.pi/180
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

# y vs x for curveball
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

#z vs x for curveball
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
plt.suptitle("Trajectory of a Curveball")
plt.xlim(0, 18)
plt.ylim(-1.25,0.65)
ylabel(r'Displacement in the $yz$-plane (meters)')
xlabel(r'Displacement along the x-axis (meters')
plt.legend()
plt.savefig("Curveball")
show()

from math import sin,cos

import matplotlib.pyplot as plt
from numpy import arange
from pylab import plot,xlabel,ylabel,show
import numpy as np
from matplotlib.animation import FuncAnimation

## Imports with a few new libraries you haven't seen before
import numpy as np
# import SDutils
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import rc # Useful for control linestyles and plot markers
from IPython.display import HTML
rc('animation', html='html5')

import matplotlib.animation as animation
print(animation.writers.list())


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



# initial conditions for fastball
v_0 = 95 * 0.44704 # m/s
theta = 1 * np.pi/180 # radians
phi = 225 * np.pi/180
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

# y vs x for fastball
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

#z vs x for fastball
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
plt.suptitle("Trajectory of a Fastball")
plt.xlim(0, 18)
plt.ylim(-1.25,0.65)
ylabel(r'Displacement in the $yz$-plane (meters)')
xlabel(r'Displacement along the x-axis (meters')
plt.legend()
plt.savefig("Fastball")
show()


number_of_frames=30# Number of frames in the animation
fig, ax = plt.subplots(1, 1, figsize=(10, 6));  # creating figures and axis objects
# ax = SDutils.plotparams(ax);
ax.set_xlim(0, 18);   # Notice you can use axis methods set_xlim and xet_ylim to modify the axis now
ax.set_ylim(-1.25,0.65);
line, = ax.plot([], [], lw=3, ls='-', color='xkcd:aqua', marker='o'); # plot

# Let's make sure I can animate it the same way:
def animate(i):  # Define an animation function that returns a "line" object that
    # represents one frame of the movie
    x = xpoints_y
    y = ypoints[i]
    line.set_data(x,y)
    return line,

def init():   #  Initializing function - it'll look like this every time, so I'm
    # not going to talk about this.  Just use it just like this!
    line.set_data([],[])
    return line,

anim = FuncAnimation(fig, animate, init_func=init, frames=number_of_frames,
                     interval=10, blit=True, save_count=0);

print("foo")

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



# initial conditions for screwball
v_0 = 85 * 0.44704 # m/s
theta = 1 * np.pi/180 # radians
phi = 135 * np.pi/180
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

# y vs x for screwball
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

#z vs x for screwball
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
plt.suptitle("Trajectory of a Screwball")
plt.xlim(0, 18)
plt.ylim(-1.25,0.65)
ylabel(r'Displacement in the $yz$-plane (meters)')
xlabel(r'Displacement along the x-axis (meters')
plt.legend()
plt.savefig("Screwball")
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
plt.suptitle("Trajectory of a Slider")
plt.xlim(0, 18)
plt.ylim(-1.25,0.65)
ylabel(r'Displacement in the $yz$-plane (meters)')
xlabel(r'Displacement along the x-axis (meters')
plt.legend()
plt.savefig("Slider")
show()
