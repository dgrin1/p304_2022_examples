# Author: Seamus Flannery
# Madelung Potential Class Example
# Run this file from the command line, all functions are called in the executable.

import numpy as np
epsilon_naught = 1  # update with actual value
A = 1  # update with actual value


# finds the pair potential for two particles which are separated by ((i**2)+(j**2)+(k**2))**0.5
def pair_potential(i, j, k):
    return ((-1)**(i+j+k) * np.e) / (4 * np.pi * epsilon_naught * A * ((i**2)+(j**2)+(k**2))**0.5)


# returns the madelung potential on a single particle at position (i, j, k) in a crystal with dimensions (x, y, z)
def single_particle_madelung_potential(x, y, z, i, j, k):
    potential = 0
    for a in range(x):
        for b in range(y):
            for c in range(z):
                potential += pair_potential(i - a, j - b, k - c)
    return potential


# finds the total potential for a crystal with x, y, z dimensions, created before single particle potential
# and could be updated to use single particle potential to simplify/optimize
def whole_crystal_madelung_potential(x, y, z):
    crystal = np.zeros([x, y, z])
    for i in crystal:
        for j in crystal[i]:
            for k in crystal[i][j]:
                for a in crystal:
                    for b in crystal[a]:
                        for c in crystal[a][b]:
                            crystal[i][j][k] = pair_potential(i-a, j-b, k-c)
    total_potential = 0
    for i in crystal:
        for j in crystal[i]:
            for k in crystal[i][j]:
                total_potential += crystal[i][j][k]
    return total_potential


