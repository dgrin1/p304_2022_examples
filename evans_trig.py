import numpy as np
import matplotlib.pyplot as plt

def factorial(y):
    if y == 1 or y == 0:
        return 1
    else:
        return (y*factorial(y-1))

def sin(x,N):
    sum = 0
    for n in range(0, N+1):
        num = ((-1)**n)*(x**(2*n+1))
        den = (2*n+1)
        denom = factorial(den)
        term = num/denom
        sum += term
    return sum

def cos(x,N):
    sum = 0
    for n in range(0, N+1):
        num = ((-1)**n)*(x**(2*n))
        den = (2*n)
        denom = factorial(den)
        term = num/denom
        sum += term
    return sum


def tan(x,N):
    return sin(x,N)/cos(x,N)

def sec(x,N):
    return 1/cos(x,N)

def csec(x,N):
    return 1/sin(x,N)

def cotan(x,N):
    return 1/tan(x,N)


sin_y = []
theta = np.linspace(0,4*np.pi, 100)
for n in theta:
    res = sin(n, 60)
    sin_y.append(res)

cos_y = []
theta = np.linspace(0,4*np.pi, 100)
for n in theta:
    res = cos(n, 60)
    cos_y.append(res)

plt.subplot(211)

plt.plot(theta, sin_y)


plt.subplot(221)

plt.plot(theta, cos_y)


plt.show()






    
