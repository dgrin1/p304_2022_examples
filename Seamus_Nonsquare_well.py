import numpy as np
import matplotlib.pyplot as plt

# my program to plot the phi for different E  values

# Constants
m = 9.1094e-31     # Mass of electron
hbar = 1.0546e-34  # Planck's constant over 2*pi
e = 1.6022e-19     # Electron charge
L = 5.2918e-11     # Bohr radius
N = 1000
h = L/N
a = 10.e-11  # meters
v_0 = 50 * e # eV

# Potential function
def V(x):
    return (v_0 * x**2) / a**2

def f(r,x,E):
    psi = r[0]
    phi = r[1]
    fpsi = phi
    fphi = (2*m/hbar**2)*(V(x)-E)*psi
    return np.array([fpsi,fphi],float)

# Calculate the wavefunction for a particular energy
def solve(E):
    psi = 0.0
    phi = 1.0
    r = np.array([psi,phi],float)

    for x in np.arange(0,L,h):
        k1 = h*f(r,x,E)
        k2 = h*f(r+0.5*k1,x+0.5*h,E)
        k3 = h*f(r+0.5*k2,x+0.5*h,E)
        k4 = h*f(r+k3,x+h,E)
        r += (k1+2*k2+2*k3+k4)/6

    return r[0]


def plot_psi2_vs_E():
    E_list = np.arange(0, 6.e-16, 1.e-18)
    psi_list = []
    for E in E_list:
        psi_list.append(solve(E))
    plt.plot(E_list, psi_list)
    plt.show()


# Main program to find the energy using the secant method
def secant_method_solve():
    E1 = 0.0
    E2 = 100 * e
    psi2 = solve(E1)

    target = e/1000
    while abs(E1-E2)>target:
        psi1,psi2 = psi2,solve(E2)
        E1,E2 = E2,E2-psi2*(E2-E1)/(psi2-psi1)
    print("E =",E2/e,"eV")

plot_psi2_vs_E()