import numpy as np
import matplotlib.pyplot as plt


nmax = 60


def factorial(x):
    if x==1 or x==0:
        fac = 1
    else:
        fac = x*factorial(x-1)
    return(fac)


def sin(x):
    sum = 0

    for n in range(0, nmax + 1):
        denominator = factorial(2*n+1)
        numerator = ((-1)**n) * (x**(2*n+1))
        term = numerator/denominator
        sum += term

    return(sum)


def cos(x):
    sum = 0

    for n in range(0, nmax + 1):
        denominator = factorial(2*n)
        numerator = ((-1)**n) * (x**(2*n))
        term = numerator/denominator
        sum += term

    return(sum)


def tan(x):
    tan = sin(x)/cos(x)
    return tan


def sec(x):
    sec = 1/cos(x)
    return sec


def csc(x):
    csc = 1/sin(x)
    return csc


def cot(x):
    cot = 1/tan(x)
    return cot

x = np.linspace(-2*np.pi,2*np.pi,200)
y_sin = [sin(value) for value in np.linspace(0,2*np.pi,200)]
y_cos = [cos(value) for value in np.linspace(0,2*np.pi,200)]
y_tan = [tan(value) for value in np.linspace(-np.pi/2,np.pi/2,200)]
y_sec = [sec(value) for value in np.linspace(-np.pi,np.pi,200)]
y_csc = [csc(value) for value in np.linspace(-np.pi,np.pi,200)]
y_cot = [cot(value) for value in np.linspace(-np.pi/2,np.pi/2,200)]

plt.plot(x,y_sin)
plt.suptitle("Sin")
plt.ylim(-1,1)
plt.show()
plt.plot(x,y_cos)
plt.suptitle("Cos")
plt.ylim(-1,1)
plt.show()
plt.plot(x,y_tan)
plt.suptitle("Tan")
plt.ylim(-5,5)
plt.show()
plt.plot(x,y_sec)
plt.suptitle("Sec")
plt.ylim(-5,5)
plt.show()
plt.plot(x,y_csc)
plt.suptitle("Csc")
plt.ylim(-5,5)
plt.show()
plt.plot(x,y_cot)
plt.suptitle("Cot")
plt.ylim(-5,5)
plt.show()

print("foo")