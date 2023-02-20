# Author: Seamus Flannery
# Code Simpson's rule, eq. 5.10 in Newman, page 147
# Run this file from the command line, all functions are called in the executable.
import numpy as np
import matplotlib.pyplot as plt
plotters = False
plt.rc('text',usetex=True)
plt.rc('font', family='serif',serif='Palatino')


def integrand(x):
    return np.sin(x)


def simpson_int(N, x_min, x_max):
    x_range = x_max-x_min
    h = x_range / N
    sample_domain = np.linspace(x_min, x_max, N)
    sample_range = []
    for x in sample_domain:
        sample_range.append(integrand(x))
    odd_sum = 0.0
    even_sum = 0.0
    for k in range(int(N/2)):
        odd_sum += integrand(x_min + (2*k-1)*h)
    for k in range(int(N/2-1)):
        even_sum += integrand(x_min + 2*k*h)
    return (1/3)*h*(integrand(x_min) + integrand(x_max) + 4 * odd_sum + 2 * even_sum)


print("The integral of sin(x) from 0 to pi is ", simpson_int(1000, 0, np.pi))
