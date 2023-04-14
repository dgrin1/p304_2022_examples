from random import random,randrange
from math import exp,pi
from numpy import ones
from matplotlib.pyplot import plot,ylabel,show

T = 10.0 #Temperature
N = 1000 #This specifies how many particles, E_i=
steps = 250000

# Create a 2D array to store the quantum numbers
#number of particles by 3 spatial dimensions
n = ones([N,3],int)

# Main loop
eplot = []

#initial starting total energy of the system
E = 3*N*pi*pi/2

#for the number of large steps we wanted to try
for k in range(steps):

    # Choose the particle and the move
#pick one particle to adjust randomly
    i = randrange(N)
# pick a dimension (x,y,z)
    j = randrange(3)
    if random()<0.5:
        dn = 1
        dE = (2*n[i,j]+1)*pi*pi/2
    else:
#decrease excitation nunber
        dn = -1
#change in energy in situatio        
        dE = (-2*n[i,j]+1)*pi*pi/2

    # Decide whether to accept the move
#these are the moves decrease
    if n[i,j]>1 or dn==1:
        if random()<exp(-dE/T):
            n[i,j] += dn
            E += dE

    eplot.append(E)

# Make the graph
plot(eplot)
ylabel("Energy")
show()