import numpy as np
import matplotlib.pyplot as plt

plt.rc('text',usetex=True)
plt.rc('font', family='sans-serif')


nmax = 65


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


def cos(x):
    sum = 0

    for n in range(0, nmax + 1):
        denominator = factorial(2 * n)
        numerator = ((-1) ** n) * (x ** (2 * n))
        term = numerator / denominator
        sum += term

    return (sum)


def tan(x):
    tan = sin(x) / cos(x)
    return tan


def sec(x):
    sec = 1 / cos(x)
    return sec


def csc(x):
    csc = 1 / sin(x)
    return csc


def cot(x):
    cot = 1 / tan(x)
    return cot


x = np.linspace(-2 * np.pi, 2 * np.pi, 200)
y_sin = [sin(value) for value in x]
y_cos = [cos(value) for value in x]
y_tan = [tan(value) for value in x]
y_sec = [sec(value) for value in x]
y_csc = [csc(value) for value in x]
y_cot = [cot(value) for value in x]

# plot sin
plt.plot(x, y_sin, "r")
plt.scatter(x, np.sin(x))
plt.suptitle(r'$\sin{x}$ vs $x$')
plt.xlabel(r'$x$')
plt.ylabel(r'$\sin{x}$')
plt.ylim(-1, 1)
plt.show()

# plot cos
plt.plot(x, y_cos, "r")
plt.scatter(x, np.cos(x))
plt.suptitle(r'$\cos{x}$ vs $x$')
plt.xlabel(r'$x$')
plt.ylabel(r'$\cos{x}$')
plt.ylim(-1, 1)
plt.show()

# plot tan
plt.plot(x, y_tan, "r")
plt.scatter(x, np.tan(x))
plt.suptitle(r'$\tan{x}$ vs $x$')
plt.xlabel(r'$x$')
plt.ylabel(r'$\tan{x}$')
plt.ylim(-5, 5)
plt.show()

# plot sec
plt.plot(x, y_sec, "r")
plt.scatter(x, 1 / np.cos(x))
plt.suptitle(r'$\sec{x}$ vs $x$')
plt.xlabel(r'$x$')
plt.ylabel(r'$\sec{x}$')
plt.ylim(-5, 5)
plt.show()

# plot csc
plt.plot(x, y_csc, "r")
plt.scatter(x, 1 / np.sin(x))
plt.suptitle(r'$\csc{x}$ vs $x$')
plt.xlabel(r'$x$')
plt.ylabel(r'$\sec{x}$')
plt.ylim(-5, 5)
plt.show()

# plot cot
plt.plot(x, y_cot, "r")
plt.scatter(x, 1 / np.tan(x))
plt.suptitle(r'$\cot{x}$ vs $x$')
plt.xlabel(r'$x$')
plt.ylabel(r'$\cot{x}$')
plt.ylim(-5, 5)
plt.show()

# delta sin
delta_sin = y_sin - np.sin(x)
plt.plot(x, delta_sin)
plt.suptitle(r'Sin $\Delta$')
plt.ylim(-1, 1)
plt.show()

print("foo")
