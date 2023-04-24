import numpy as np
import matplotlib.pyplot as plt
from vpython import curve

"""
Sasha Levina
Problem 9.5: FTCS Solution of the Wave Equation

Use FTCS to solve the complete set of simultaneous first oder equations for the vibrating piano string as a result of being struck by the piano hammer.
Using h = 10E-6

"""
#fonts for plotting
plt.rc('text',usetex=True)
plt.rc('font', family='Helvetica')

def wavef(x): #wave equation for string length L struck distance d from x=0
    exponent = -(x-d)**2/(2*sigma**2)
    return(C*x*(L-x)*np.exp(exponent)/L**2)

#constants
L = 1 #m, length of string
d = 0.1 #m, distance of hammer from x=0
C = 1 #m/s
sigma = 0.3 #m
v = 100 #m/s
N = 100 #number of divisions in grid
a = L/N #grid spacing

h = 1E-6 #s, time step
epsilon = h/1000


#FTCS adapted from heat.py

#define initial, mid, and end values 
#all are zero at endpoints of string, as string is fixed on ends
phi_low = 0
phi_mid = 0 
phi_high = 0
psi_low = 0
psi_high = 0

#define time steps
tvals = [2E-3, 20E-3, 40E-3, 60E-3, 80E-3]
tend = tvals[-1] + epsilon

# create arrays of values of phi
phi = np.empty(N+1,float)
phi[0] = phi_low
phi[N] = phi_high
phi[1:N] = phi_mid #phi(x) = 0 everywhere initially
phip = np.empty(N+1,float)
phip[0] = phi_low
phip[N] = phi_high

#create arrays of values of psi
psi = np.empty(N+1,float)
psi[0] = psi_low
psi[N] = psi_high
for i in range(1,N): # use wave equation to calculate psi (velocity) values
    psi[i] = wavef(i*a) # nonzero values of psi initially
psip = np.empty(N+1, float)
psip[0] = psi_low
psip[N] = psi_high

# Main loop of FTCS
t = 0.0 #start time
D = h*(v**2)/(a**2)
while t<tend:

    # Calculate the new values of phi and psi
    for i in range(1,N):
        phip[i] = phi[i] + h*psi[i]
        psip[i] = psi[i] + D*(phi[i+1]+phi[i-1]-2*phi[i])
    psi,psip = psip,psi
    phi,phip = phip,phi
    t += h

    for i in tvals:
        if abs(t-i)<epsilon:
            plt.plot(psi, label=r"t=%s s"%i)

#plot psi as a function of x (the shape of the string) for different time steps
plt.title(r"$\psi(x)$ vs $x$ for piano string for $h = 10^{-6}$")
plt.xlabel(r"$x$ (m)")
plt.ylabel(r"$\psi(x)$")
plt.legend()
plt.savefig("pianostring2.png")
plt.show()

