from __future__ import print_function, division
import numpy as np
from math import exp
import matplotlib.pyplot as plt


def f(x):
    return 2. - exp(-x)


def g(x):
    return exp(1. - np.power(x, 2.e0))


def h(x):
    return np.sqrt(1.e0 - np.log(x))


def gauss(x, a, b, c, d):
    return -a * exp((-((x - b) ** 2)) / 2 * (c ** 2)) + d


eps = 4
x = eps
eps_target = 1.e-8
xold = x
xarr = [x]
i = 0
iarr = [i]
epsarr = [eps]
# cap is put in there to make sure code doesn't take forever
while (eps > eps_target and i < 500):
    x = gauss(x, 1.3, 3.0, 0.4, 0.6)
    eps = abs(x - xold)
    # setting the new comparison case to last guees
    xold = x
    # augmenting m count
    i = i + 1
    iarr.append(i)
    xarr.append(x)
    epsarr.append(eps)

print(x, eps_target)
plt.xlim(1, 10)
plt.figure(1)
plt.title("Gaussian")
plot_domain = np.linspace(-10, 10, 1000)
gaussarr = []
for x in plot_domain:
    gaussarr.append(gauss(x, 1.3, 3.0, 0.4, 0.6))
plt.plot(plot_domain, gaussarr)
plt.xlim(-10, 10)
plt.show()
plt.figure(2)
plt.title("Right Root")
plt.plot(iarr, xarr)
plt.xlabel("Iteration")
plt.ylabel("Best Root Val")
plt.show()
plt.figure(3)
plt.title("Aprox. Error on Right Root")
plt.plot(iarr, epsarr)
plt.xlabel("Iteration")
plt.ylabel("Error")
plt.show()
