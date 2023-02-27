# Author: Seamus Flannery
# Madelung Potential Class Example
# Run this file from the command line, all functions are called in the executable.
# This file finds the madelung potential of a particle in a crystal, and also sums that for each particle in a
# crystal to find the entire crystal's madelung potential

import numpy as np
import matplotlib.pyplot as plt
# epsilon_naught = 8.8541878128(13)*(10**(-12))  # Farads/Meter
# e = 1.6022 * (10**(-19))  # coulombs per electron
# A = 1  # update with actual value


# finds the pair potential for two particles which are separated by ((i**2)+(j**2)+(k**2))**0.5
def pair_potential(i, j, k):
    return ((-1)**(i+j+k)) / (((i**2)+(j**2)+(k**2))**0.5)


# returns the madelung potential on a single particle at position (i, j, k) in a crystal with dimensions (x, y, z)
def single_particle_madelung_potential(x, y, z, i, j, k):
    potential = 0
    for a in range(x):
        for b in range(y):
            for c in range(z):
                if i != a and j != b and k != c:
                    potential += pair_potential(i - a, j - b, k - c)
    return potential


# finds the total potential for a crystal with x, y, z dimensions
def whole_crystal_madelung_potential(x, y, z):
    potential = 0
    for a in range(x):
        for b in range(y):
            for c in range(z):
                potential += single_particle_madelung_potential(x, y, z, a, b, c)
    return potential


print(single_particle_madelung_potential(5, 5, 5, 2, 2, 1), "Unitless?")
print(whole_crystal_madelung_potential(5, 5, 5), "Unitless?")
# print(whole_crystal_madelung_potential(50, 50, 50), "Coulombs?")  # WILL NOT RUN QUICKLY :)


def plot_madelung_cubes(domain):
    data = np.zeros(domain)
    for i in range(domain):
        data[i] = whole_crystal_madelung_potential(i, i, i)
    plt.plot(np.linspace(0, domain, domain), data, marker=".", markersize="5")
    plt.xlabel("Side Length of Square Crystal")
    plt.ylabel("Madelung Unitless Potential")
    plt.title("Madelung Crystal Potential Energy")
    plt.show()


plot_madelung_cubes(12)


