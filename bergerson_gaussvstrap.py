import numpy as np
import matplotlib.pyplot as plt
from bergerson_integration import gaussint
from bergerson_integration import trap

plt.rc('text',usetex=True)
plt.rc('font', family='sans-serif')


nmax = 20


def factorial(x):
    if x == 1 or x == 0:
        fac = 1
    else:
        fac = x * factorial(x - 1)
    return (fac)


def sin(x):
    sum = 0

    for n in range(0, nmax + 1):
        denominator = factorial(2 * n + 1)
        numerator = ((-1) ** n) * (x ** (2 * n + 1))
        term = numerator / denominator
        sum += term

    return (sum)


x = np.linspace(-2 * np.pi, 2 * np.pi, 200)

def f(x):
    y = sin(x)
    return y

for i in range(1,10):
    plt.plot(x,[trap(0, value, f, i) for value in x],"b")
    plt.plot(x, [gaussint(0, value, f, i) for value in x],"r")
    plt.suptitle(r'Trapezoidal (red) and Gaussian Quadrature (blue) methods of integration for $\sin{x}$')
plt.show()




