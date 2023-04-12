# code author: Ben Bergerson
# worked with George Evans


from math import sin
import matplotlib.pyplot as plt
from numpy import arange,array,pi
from pylab import plot,xlabel,ylabel,show

# define gravity and arm length
g = 9.81
l = 0.1

# define function given by Eq. 8.44
def f(x,t):
    theta = x[0]
    omega = x[1]
    ftheta = omega
    fomega = -(g/l)*sin(theta)
    return array([ftheta,fomega],float)

# chose first few periods of oscillation
a = 0
b = 10

# step size large enough to make the curve smooth
N = 1000
h = (b-a)/N

tpoints = arange(a,b,h)
xpoints = []

# convert degrees to radians
# 179 degrees in radians
# x = (initial position, initial angular velocity)
x = array([179*pi/180,0],float)

for t in tpoints:
    # note that we only want the position component of x
    xpoints.append(x[0])
    k1 = h*f(x,t)
    k2 = h*f(x+0.5*k1,t+0.5*h)
    k3 = h*f(x+0.5*k2,t+0.5*h)
    k4 = h*f(x+k3,t+h)
    x += (k1+2*k2+2*k3+k4)/6

# plot motion of pendulum
plot(tpoints,xpoints)
plt.suptitle(r'Motion of a Nonlinear Pendulum')
xlabel(r'$t$')
ylabel(r'$\theta(t)$')
show()